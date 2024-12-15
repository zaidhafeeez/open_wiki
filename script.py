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
MAX_RETRIES = 3  # Maximum number of retries for failed API calls
BACKOFF_FACTOR = 2  # Exponential backoff factor for retries

# Initialize Wikipedia API with rate limiting
wiki_wiki = wikipediaapi.Wikipedia(
    language=LANGUAGE,
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent="WikiArchiveScript/1.0 (https://github.com/zaidhafeeez/open_wiki)"
)

# Thread-safe progress tracking
progress_lock = threading.Lock()
processed_articles = set()
api_lock = threading.Lock()  # Lock for API calls
error_count = 0
MAX_ERRORS = 50  # Maximum number of errors before stopping

# Thread-safe queue for logging
log_queue = queue.Queue()

def log_message(msg, level="INFO"):
    """
    Thread-safe logging with timestamp and level.
    Levels: INFO, WARNING, ERROR
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"[{timestamp}] {level}: {msg}"
    log_queue.put(formatted_msg)
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
    - Handles Unicode characters
    
    Args:
        name (str): The original file name
        
    Returns:
        str: A safe file path string
        
    Example:
        >>> get_safe_path("Hello World!")
        'Hello_World'
    """
    if not isinstance(name, str):
        log_message(f"Warning: Non-string input '{name}' converted to string", "WARNING")
        name = str(name)
    
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
        '~': '_',
        '–': '-',  # Special dash character
        '—': '-',  # Em dash
        ''': '_',  # Smart quotes
        ''': '_',
        '"': '_',
        '"': '_',
    }
    
    result = name
    for char, replacement in replacements.items():
        result = result.replace(char, replacement)
    
    # Remove any remaining non-ASCII characters
    result = ''.join(c for c in result if c.isascii())
    
    # Replace multiple underscores with a single one
    while '__' in result:
        result = result.replace('__', '_')
    
    # Remove leading/trailing underscores and spaces
    result = result.strip('_').strip()
    
    # Ensure the path is not empty and has a reasonable length
    if not result:
        result = 'unnamed'
    elif len(result) > 255:  # Maximum filename length for most filesystems
        result = result[:252] + '...'
    
    return result

def retry_with_backoff(func, *args, **kwargs):
    """
    Retry a function with exponential backoff.
    """
    for attempt in range(MAX_RETRIES):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                raise
            wait_time = RATE_LIMIT_DELAY * (BACKOFF_FACTOR ** attempt)
            log_message(f"Attempt {attempt + 1} failed: {str(e)}. Retrying in {wait_time:.1f}s", "WARNING")
            time.sleep(wait_time)

def load_progress():
    """Load progress from the progress file with error handling."""
    try:
        if os.path.exists(PROGRESS_FILE):
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {'processed': set(data['processed']), 'last_category': data['last_category']}
    except Exception as e:
        log_message(f"Error loading progress file: {str(e)}", "ERROR")
        # Backup the corrupted file if it exists
        if os.path.exists(PROGRESS_FILE):
            backup_file = f"{PROGRESS_FILE}.bak"
            try:
                os.rename(PROGRESS_FILE, backup_file)
                log_message(f"Backed up corrupted progress file to {backup_file}", "WARNING")
            except Exception:
                pass
    return {'processed': set(), 'last_category': None}

def save_progress(processed, current_category=None):
    """Save progress with error handling and atomic writes."""
    with progress_lock:
        temp_file = f"{PROGRESS_FILE}.tmp"
        try:
            progress = {
                'processed': list(processed),
                'last_category': current_category,
                'last_updated': datetime.now(timezone.utc).isoformat()
            }
            # Write to temporary file first
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(progress, f, indent=2, ensure_ascii=False)
            # Atomic rename
            os.replace(temp_file, PROGRESS_FILE)
        except Exception as e:
            log_message(f"Error saving progress: {str(e)}", "ERROR")
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except Exception:
                    pass

def get_article_metadata(page):
    """
    Get metadata for a Wikipedia article with retries and error handling.
    
    Args:
        page: Wikipedia page object
        
    Returns:
        dict: Article metadata including title, URL, summary, etc.
    """
    metadata = {}
    
    # Basic metadata with retry
    def get_basic_metadata():
        with api_lock:
            time.sleep(RATE_LIMIT_DELAY)
            return {
                'title': page.title,
                'url': page.fullurl,
                'summary': page.summary[0:500] if page.summary else "",
                'last_updated': datetime.now(timezone.utc).isoformat(),
                'language': page.language,
                'pageid': page.pageid,
            }
    
    try:
        metadata = retry_with_backoff(get_basic_metadata)
    except Exception as e:
        log_message(f"Error getting basic metadata for {page.title}: {str(e)}", "ERROR")
        raise
    
    try:
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
        
        # Get links with retry
        def get_links():
            with api_lock:
                time.sleep(RATE_LIMIT_DELAY)
                return [
                    {'title': link.title, 'url': link.fullurl}
                    for link in page.links.values()
                    if link.exists()
                ]
        
        metadata['links'] = retry_with_backoff(get_links)
        
        # Get references if available
        metadata['references'] = (
            list(page.references) if hasattr(page, 'references') else []
        )
        
    except Exception as e:
        log_message(f"Error getting extended metadata for {page.title}: {str(e)}", "WARNING")
        # Don't raise here, return partial metadata
    
    return metadata

def format_article_content(page, metadata):
    """
    Format article content with metadata in Markdown.
    
    Args:
        page: Wikipedia page object
        metadata (dict): Article metadata
        
    Returns:
        str: Formatted article content in Markdown
    """
    sections = []
    
    try:
        # Basic Metadata
        sections.append(f"# {page.title}\n")
        sections.append("## Article Metadata\n")
        sections.extend([
            f"- **Last Updated:** {metadata.get('last_updated', 'Unknown')}",
            f"- **Original Article:** [{page.title}]({metadata.get('url', '')})",
            f"- **Language:** {metadata.get('language', 'Unknown')}",
            f"- **Page ID:** {metadata.get('pageid', 'Unknown')}"
        ])
        if metadata.get('is_disambiguation', False):
            sections.append("- **Type:** Disambiguation Page")
        sections.append("")
        
        # Summary
        if metadata.get('summary'):
            sections.extend([
                "## Summary\n",
                metadata['summary'],
                ""
            ])
        
        # Categories
        if metadata.get('categories'):
            sections.extend([
                "## Categories\n",
                *[f"- {cat}" for cat in metadata['categories']],
                ""
            ])
        
        # Table of Contents
        if metadata.get('sections'):
            sections.extend([
                "## Table of Contents\n",
                *[f"{'  ' * (section['level'] - 1)}- {section['title']}"
                  for section in metadata['sections']],
                ""
            ])
        
        # References
        if metadata.get('references'):
            sections.extend([
                "## References\n",
                *[f"- {ref}" for ref in metadata['references']],
                ""
            ])
        
        # Links
        if metadata.get('links'):
            sections.extend([
                "## Related Articles\n",
                *[f"- [{link['title']}]({link['url']})" for link in metadata['links'][:50]],  # Limit to 50 links
                ""
            ])
            if len(metadata['links']) > 50:
                sections.append(f"*Note: Showing 50 out of {len(metadata['links'])} related articles*\n")
    
    except Exception as e:
        log_message(f"Error formatting article content for {page.title}: {str(e)}", "ERROR")
        # Add error note to the article
        sections.extend([
            "## Error Notice\n",
            "*There was an error formatting some parts of this article. Some content may be missing.*\n",
            f"*Error: {str(e)}*\n"
        ])
    
    return "\n".join(sections)

def ensure_directory(directory):
    """Create directory if it doesn't exist."""
    try:
        os.makedirs(directory, exist_ok=True)
    except Exception as e:
        log_message(f"Error creating directory {directory}: {str(e)}", "ERROR")
        raise

def process_article(args):
    """
    Process a single article with error handling and retries.
    
    Args:
        args (tuple): (article_title, category_name, depth)
    
    Returns:
        tuple: (success, article_title)
    """
    global error_count
    article_title, category_name, depth = args
    
    try:
        # Skip if already processed
        if article_title in processed_articles:
            return True, article_title
        
        # Get page with retry
        def get_page():
            return wiki_wiki.page(article_title)
        page = retry_with_backoff(get_page)
        
        if not page.exists():
            log_message(f"Article does not exist: {article_title}", "WARNING")
            return False, article_title
        
        # Get metadata and format content
        metadata = get_article_metadata(page)
        content = format_article_content(page, metadata)
        
        # Create category directory
        category_dir = os.path.join(OUTPUT_DIR, f"articles_{get_safe_path(category_name)}")
        ensure_directory(category_dir)
        
        # Save article
        article_path = os.path.join(category_dir, f"{get_safe_path(article_title)}.md")
        with open(article_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        with progress_lock:
            processed_articles.add(article_title)
        
        log_message(f"Processed article: {article_title}")
        return True, article_title
        
    except Exception as e:
        with progress_lock:
            error_count += 1
            if error_count >= MAX_ERRORS:
                log_message("Maximum error count reached. Stopping...", "ERROR")
                raise SystemExit("Too many errors occurred")
        
        log_message(f"Error processing article {article_title}: {str(e)}", "ERROR")
        return False, article_title

def process_category(category_name, depth=0):
    """
    Process a single category and return its articles and subcategories.
    
    Args:
        category_name (str): Name of the category to process
        depth (int): Current depth level
        
    Returns:
        tuple: (articles, subcategories)
    """
    try:
        def get_category():
            with api_lock:
                time.sleep(RATE_LIMIT_DELAY)
                return wiki_wiki.page(f"Category:{category_name}")
        
        category = retry_with_backoff(get_category)
        if not category.exists():
            log_message(f"Category does not exist: {category_name}", "WARNING")
            return [], []
        
        articles = []
        subcategories = []
        
        # Get category members with retry
        def get_members():
            with api_lock:
                time.sleep(RATE_LIMIT_DELAY)
                return category.categorymembers
        
        members = retry_with_backoff(get_members)
        
        for title, member in members.items():
            if 'Category:' in title:
                if depth < MAX_DEPTH:
                    subcategories.append(title.replace('Category:', ''))
            else:
                articles.append(title)
        
        log_message(f"Found {len(articles)} articles and {len(subcategories)} subcategories in {category_name}")
        return articles, subcategories
        
    except Exception as e:
        log_message(f"Error processing category {category_name}: {str(e)}", "ERROR")
        return [], []

def scrape_category(category_name, depth=0):
    """
    Process categories and articles in parallel with error handling.
    
    Args:
        category_name (str): Name of the category to process
        depth (int): Current depth level
    """
    try:
        # Create category directory and README
        category_dir = os.path.join(OUTPUT_DIR, f"articles_{get_safe_path(category_name)}")
        ensure_directory(category_dir)
        
        readme_path = os.path.join(category_dir, "README.md")
        if not os.path.exists(readme_path):
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(f"# {category_name}\n\n")
                f.write(f"Wikipedia articles related to {category_name}\n\n")
                f.write("## Contents\n\n")
                f.write("This directory contains articles from the following categories:\n")
                f.write(f"- {category_name}\n")
        
        # Process the category
        articles, subcategories = process_category(category_name, depth)
        
        # Update progress
        save_progress(processed_articles, category_name)
        
        # Process articles in parallel
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            article_tasks = []
            for article in articles:
                if article not in processed_articles:
                    task = executor.submit(process_article, (article, category_name, depth))
                    article_tasks.append(task)
            
            # Process articles and handle results
            for future in tqdm(as_completed(article_tasks), total=len(article_tasks), desc=f"Processing {category_name}"):
                try:
                    success, article = future.result()
                    if success:
                        save_progress(processed_articles, category_name)
                except Exception as e:
                    log_message(f"Task failed: {str(e)}", "ERROR")
        
        # Recursively process subcategories
        if depth < MAX_DEPTH:
            for subcat in subcategories:
                if error_count >= MAX_ERRORS:
                    log_message("Maximum error count reached. Stopping category processing...", "ERROR")
                    break
                scrape_category(subcat, depth + 1)
        
    except Exception as e:
        log_message(f"Error in category scraping for {category_name}: {str(e)}", "ERROR")

if __name__ == "__main__":
    try:
        # Initialize
        ensure_directory(OUTPUT_DIR)
        progress_data = load_progress()
        processed_articles = progress_data['processed']
        last_category = progress_data['last_category']
        
        log_message("Starting Wikipedia article archiving script", "INFO")
        log_message(f"Target category: {CATEGORY}")
        log_message(f"Maximum depth: {MAX_DEPTH}")
        log_message(f"Previously processed articles: {len(processed_articles)}")
        
        # Main processing
        scrape_category(CATEGORY)
        
        log_message("Archiving complete!", "INFO")
        log_message(f"Total articles processed: {len(processed_articles)}")
        
    except KeyboardInterrupt:
        log_message("Script interrupted by user", "WARNING")
        save_progress(processed_articles, CATEGORY)
        
    except Exception as e:
        log_message(f"Fatal error: {str(e)}", "ERROR")
        save_progress(processed_articles, CATEGORY)
        raise
    
    finally:
        save_progress(processed_articles, CATEGORY)
