import wikipediaapi
from datetime import datetime, timezone
import time
import json
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import threading

# Configuration
LANGUAGE = "en"
CATEGORY = "Python (programming language)"
MAX_DEPTH = 1
PROGRESS_FILE = "archive_progress.json"
OUTPUT_DIR = "wiki_articles"
MAX_WORKERS = 3  # Number of concurrent article processing threads

# Initialize Wikipedia API with rate limiting
wiki_wiki = wikipediaapi.Wikipedia(
    language=LANGUAGE,
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent="WikiArchiveScript/1.0"
)

# Thread-safe progress tracking
progress_lock = threading.Lock()
processed_articles = set()

def get_safe_path(name):
    """Convert a string to a safe file path by replacing problematic characters."""
    # Replace problematic characters
    safe_name = name.replace(' ', '_')
    safe_name = safe_name.replace('/', '_')
    safe_name = safe_name.replace('\\', '_')
    safe_name = safe_name.replace(':', '_')
    safe_name = safe_name.replace('*', '_')
    safe_name = safe_name.replace('?', '_')
    safe_name = safe_name.replace('"', '_')
    safe_name = safe_name.replace('<', '_')
    safe_name = safe_name.replace('>', '_')
    safe_name = safe_name.replace('|', '_')
    safe_name = safe_name.replace('(', '')
    safe_name = safe_name.replace(')', '')
    
    # Remove any double underscores
    while '__' in safe_name:
        safe_name = safe_name.replace('__', '_')
    
    # Remove leading/trailing underscores
    safe_name = safe_name.strip('_')
    
    return safe_name

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
    # Get essential metadata first
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
        page = wiki_wiki.page(article_title)
        if not page.exists():
            print(f"Article '{article_title}' does not exist.")
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
            
        print(f"Processed: {article_title}")
        
    except Exception as e:
        print(f"Error processing '{article_title}': {str(e)}")

def scrape_category(category_name, depth=0):
    if depth > MAX_DEPTH:
        return

    category = wiki_wiki.page(f"Category:{category_name}")
    if not category.exists():
        print(f"Category '{category_name}' does not exist.")
        return

    print(f"\nProcessing category: {category_name} (depth: {depth})")
    members = list(category.categorymembers.keys())
    print(f"Found {len(members)} members")

    # Separate articles and subcategories
    articles = []
    subcategories = []
    
    for title in members:
        if "Category:" in title and depth < MAX_DEPTH:
            subcategories.append(title.replace("Category:", ""))
        else:
            category_path = f"articles/{get_safe_path(category_name)}"
            articles.append((title, category_path))

    # Process articles in parallel
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        list(tqdm(
            executor.map(process_article, articles),
            total=len(articles),
            desc=f"Processing articles in {category_name}"
        ))

    # Process subcategories
    for subcat in subcategories:
        scrape_category(subcat, depth + 1)
        save_progress(processed_articles, subcat)

if __name__ == "__main__":
    try:
        ensure_directory(OUTPUT_DIR)
        
        # Load previous progress
        progress = load_progress()
        processed_articles = progress['processed']
        start_category = progress['last_category'] or CATEGORY
        
        if processed_articles:
            print(f"Found {len(processed_articles)} previously processed articles")
            print("Note: All articles will be updated with the latest format")
        
        scrape_category(start_category)
        
        if os.path.exists(PROGRESS_FILE):
            os.remove(PROGRESS_FILE)
        
        print(f"\nAll articles have been saved to the '{OUTPUT_DIR}' directory.")
        print("You can now review the articles and commit them to your repository manually.")
            
    except KeyboardInterrupt:
        print("\nScript interrupted. Progress saved.")
        save_progress(processed_articles)
    except Exception as e:
        print(f"An error occurred: {e}")
        save_progress(processed_articles)
