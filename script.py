import wikipediaapi
from datetime import datetime, timezone
import time
import json
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import queue

# Configuration
LANGUAGE = "en"
CATEGORY = "Python (programming language)"
MAX_DEPTH = 1
PROGRESS_FILE = "archive_progress.json"
OUTPUT_DIR = "wiki_articles"
MAX_WORKERS = 10  # Increased number of workers
RATE_LIMIT_DELAY = 0.1  # Delay between API calls in seconds

# Initialize Wikipedia API with rate limiting
wiki_wiki = wikipediaapi.Wikipedia(
    language=LANGUAGE,
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent="WikiArchiveScript/1.0"
)

# Thread-safe progress tracking
progress_lock = threading.Lock()
processed_articles = set()
api_lock = threading.Lock()  # Lock for API calls

# Thread-safe queue for logging
log_queue = queue.Queue()

def log_message(msg):
    log_queue.put(msg)
    while not log_queue.empty():
        try:
            print(log_queue.get_nowait())
        except queue.Empty:
            break

def get_safe_path(name):
    """
    Convert a string into a safe file path.
    - Replaces spaces with underscores
    - Removes or replaces special characters
    - Ensures Git compatibility
    """
    # Common replacements for readability
    replacements = {
        ' ': '_',
        '/': '_',
        '\\': '_',
        ':': '_',
        '*': '_',
        '?': '_',
        '"': '_',
        '<': '_',
        '>': '_',
        '|': '_',
        '(': '_',
        ')': '_',
        '[': '_',
        ']': '_',
        '{': '_',
        '}': '_',
        '\'': '_',
        '`': '_',
        '#': '_',
        '%': '_',
        '&': '_',
        '@': '_',
        '!': '_',
        '+': '_',
        '=': '_',
        ';': '_',
        ',': '_',
        '~': '_'
    }
    
    result = name
    for char, replacement in replacements.items():
        result = result.replace(char, replacement)
    
    # Remove any remaining non-ASCII characters
    result = ''.join(c for c in result if c.isascii())
    
    # Replace multiple underscores with a single one
    while '__' in result:
        result = result.replace('__', '_')
    
    # Remove leading/trailing underscores
    result = result.strip('_')
    
    # Ensure the path is not empty
    if not result:
        result = 'unnamed'
        
    return result

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            data = json.load(f)
            return {'processed': set(data['processed']), 'last_category': data['last_category']}
    return {'processed': set(), 'last_category': None}

def save_progress(processed, current_category=None):
    with progress_lock:
        progress = {
            'processed': list(processed),
            'last_category': current_category
        }
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(progress, f)

def get_article_metadata(page):
    with api_lock:
        time.sleep(RATE_LIMIT_DELAY)  # Rate limiting
        metadata = {
            'title': page.title,
            'url': page.fullurl,
            'summary': page.summary[0:500] if page.summary else "",
            'last_updated': datetime.now(timezone.utc).isoformat(),
            'language': page.language,
            'pageid': page.pageid,
        }
    
    # Add categories
    metadata['categories'] = [cat.title for cat in page.categories.values()]
    
    # Check disambiguation
    metadata['is_disambiguation'] = (
        'disambiguation' in page.title.lower() or
        'disambiguation' in [cat.lower() for cat in metadata['categories']] or
        'may refer to' in metadata['summary'].lower()
    )
    
    # Get sections
    metadata['sections'] = [
        {'title': section.title, 'level': section.level}
        for section in page.sections
    ]
    
    # Get links (only existing ones to reduce processing)
    with api_lock:
        time.sleep(RATE_LIMIT_DELAY)  # Rate limiting
        metadata['links'] = [
            {'title': link.title, 'url': link.fullurl}
            for link in page.links.values()
            if link.exists()
        ]
    
    # Get references if available
    metadata['references'] = (
        list(page.references) if hasattr(page, 'references') else []
    )
    
    return metadata

def format_article_content(page, metadata):
    sections = []
    
    # Basic Metadata
    sections.append(f"# {page.title}\n")
    sections.append("## Article Metadata\n")
    sections.extend([
        f"- **Last Updated:** {metadata['last_updated']}",
        f"- **Original Article:** [{page.title}]({metadata['url']})",
        f"- **Language:** {metadata['language']}",
        f"- **Page ID:** {metadata['pageid']}"
    ])
    if metadata['is_disambiguation']:
        sections.append("- **Type:** Disambiguation Page")
    sections.append("")
    
    # Summary
    if metadata['summary']:
        sections.extend([
            "## Summary\n",
            metadata['summary'],
            ""
        ])
    
    # Categories
    if metadata['categories']:
        sections.extend([
            "## Categories\n",
            *[f"- {cat}" for cat in metadata['categories']],
            ""
        ])
    
    # Table of Contents
    if metadata['sections']:
        sections.extend([
            "## Table of Contents\n",
            *[f"{'  ' * (section['level'] - 1)}- {section['title']}"
              for section in metadata['sections']],
            ""
        ])
    
    # Main Content
    sections.extend([
        "## Content\n",
        page.text,
        ""
    ])
    
    # Links
    if metadata['links']:
        sections.extend([
            "## Related Articles\n",
            "### Internal Links\n",
            *[f"- [{link['title']}]({link['url']})"
              for link in metadata['links']],
            ""
        ])
    
    # References
    if metadata['references']:
        sections.extend([
            "## References\n",
            *[f"- {ref}" for ref in metadata['references']],
            ""
        ])
    
    # Footer
    sections.extend([
        "---",
        "_This article is part of the Python Programming Language wiki archive._",
        f"_Retrieved and archived on: {metadata['last_updated']}_"
    ])
    
    return "\n".join(sections)

def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def process_article(args):
    article_title, category_path = args
    try:
        with api_lock:
            time.sleep(RATE_LIMIT_DELAY)  # Rate limiting
            page = wiki_wiki.page(article_title)
            if not page.exists():
                log_message(f"Article '{article_title}' does not exist.")
                return

        metadata = get_article_metadata(page)
        safe_category = get_safe_path(category_path)
        directory_path = os.path.join(OUTPUT_DIR, safe_category)
        
        with progress_lock:
            ensure_directory(directory_path)
            
            # Create README for category if needed
            readme_path = os.path.join(directory_path, "README.md")
            if not os.path.exists(readme_path):
                with open(readme_path, 'w', encoding='utf-8') as f:
                    f.write(f"# {category_path}\n\nWikipedia articles related to {category_path}")

        file_path = os.path.join(directory_path, f"{get_safe_path(article_title)}.md")
        content = format_article_content(page, metadata)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        with progress_lock:
            processed_articles.add(article_title)
            
        log_message(f"Processed: {article_title}")
        
    except Exception as e:
        log_message(f"Error processing '{article_title}': {str(e)}")

def process_category(category_name, depth=0):
    """Process a single category and return its articles and subcategories"""
    try:
        with api_lock:
            time.sleep(RATE_LIMIT_DELAY)  # Rate limiting
            category = wiki_wiki.page(f"Category:{category_name}")
            if not category.exists():
                log_message(f"Category '{category_name}' does not exist.")
                return [], []

        members = list(category.categorymembers.keys())
        
        articles = []
        subcategories = []
        
        for title in members:
            if "Category:" in title and depth < MAX_DEPTH:
                subcategories.append(title.replace("Category:", ""))
            else:
                category_path = f"articles/{get_safe_path(category_name)}"
                articles.append((title, category_path))
        
        return articles, subcategories
    except Exception as e:
        log_message(f"Error processing category '{category_name}': {str(e)}")
        return [], []

def scrape_category(category_name, depth=0):
    """Process categories and articles in parallel"""
    if depth > MAX_DEPTH:
        return

    # Get articles and subcategories for current category
    articles, subcategories = process_category(category_name, depth)
    
    # Process articles in parallel
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submit all article processing tasks
        future_to_article = {
            executor.submit(process_article, article): article[0]
            for article in articles
        }
        
        # Process articles with progress bar
        with tqdm(total=len(articles), desc=f"Processing articles in {category_name}") as pbar:
            for future in as_completed(future_to_article):
                article_title = future_to_article[future]
                try:
                    future.result()
                except Exception as e:
                    log_message(f"Error processing article {article_title}: {str(e)}")
                pbar.update(1)
        
        # Process subcategories in parallel
        if subcategories:
            subcategory_futures = [
                executor.submit(scrape_category, subcat, depth + 1)
                for subcat in subcategories
            ]
            
            # Wait for all subcategories to complete
            for future in as_completed(subcategory_futures):
                try:
                    future.result()
                except Exception as e:
                    log_message(f"Error processing subcategory: {str(e)}")
                
        save_progress(processed_articles, category_name)

if __name__ == "__main__":
    try:
        ensure_directory(OUTPUT_DIR)
        
        # Load previous progress
        progress = load_progress()
        processed_articles = progress['processed']
        start_category = progress['last_category'] or CATEGORY
        
        if processed_articles:
            log_message(f"Found {len(processed_articles)} previously processed articles")
            log_message("Note: All articles will be updated with the latest format")
        
        scrape_category(start_category)
        
        if os.path.exists(PROGRESS_FILE):
            os.remove(PROGRESS_FILE)
        
        log_message(f"\nAll articles have been saved to the '{OUTPUT_DIR}' directory.")
        log_message("You can now review the articles and commit them to your repository manually.")
            
    except KeyboardInterrupt:
        log_message("\nScript interrupted. Progress saved.")
        save_progress(processed_articles)
    except Exception as e:
        log_message(f"An error occurred: {e}")
        save_progress(processed_articles)
