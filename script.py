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
                return {
                    'processed': set(data.get('processed', [])),
                    'last_category': data.get('last_category'),
                    'category_stats': data.get('category_stats', {})
                }
    except Exception as e:
        log_message(f"Error loading progress: {str(e)}", "ERROR")
    
    # Return default values if file doesn't exist or there's an error
    return {
        'processed': set(),
        'last_category': None,
        'category_stats': {}
    }

def get_article_metadata(page):
    """
    Get metadata for a Wikipedia article with retries and error handling.
    
    Args:
        page: Wikipedia page object
        
    Returns:
        dict: Article metadata including title, URL, summary, etc.
    """
    if not page or not page.exists():
        log_message(f"Page does not exist or is invalid", "ERROR")
        return None

    try:
        with api_lock:
            time.sleep(RATE_LIMIT_DELAY)  # Rate limiting
            metadata = {
                'title': page.title,
                'url': page.fullurl,
                'summary': page.summary if hasattr(page, 'summary') and page.summary else '',
                'last_modified': (
                    datetime.fromtimestamp(time.mktime(time.strptime(page.touched, '%Y-%m-%dT%H:%M:%SZ')))
                    .strftime('%Y-%m-%d %H:%M:%S UTC') if hasattr(page, 'touched') else 
                    datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
                ),
                'categories': [cat.title for cat in page.categories.values()] if hasattr(page, 'categories') else [],
                'references': len(page.references) if hasattr(page, 'references') else 0,
                'word_count': len(page.text.split()) if hasattr(page, 'text') and page.text else 0,
                'content_size': len(page.text.encode('utf-8')) if hasattr(page, 'text') and page.text else 0,
                'has_toc': bool(page.sections) if hasattr(page, 'sections') else False,
                'archive_date': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
            }
            return metadata
    except Exception as e:
        log_message(f"Error getting metadata for {page.title if page else 'unknown page'}: {str(e)}", "ERROR")
        return None

def format_article_content(page, metadata):
    """
    Format article content with metadata in Markdown.
    
    Args:
        page: Wikipedia page object
        metadata (dict): Article metadata
        
    Returns:
        str: Formatted article content in Markdown
    """
    if not page or not metadata:
        return None
        
    try:
        # Format metadata section
        content = [
            f"# {metadata['title']}",
            "",
            "## Metadata",
            f"- **Last Updated:** {metadata['last_modified']}",
            f"- **Original Article:** [{metadata['title']}]({metadata['url']})",
            f"- **Language:** {page.language}",
            f"- **Page ID:** {page.pageid}",
            "",
            "## Summary",
            metadata['summary'] if metadata['summary'] else "No summary available.",
            "",
        ]
        
        # Add categories section if available
        if metadata['categories']:
            content.extend([
                "## Categories",
                "This article belongs to the following categories:",
                ""
            ])
            for category in metadata['categories']:
                content.append(f"- {category}")
            content.append("")
            
        # Add table of contents if article has sections
        if metadata.get('has_toc', False):
            content.extend([
                "## Table of Contents",
                ""
            ])
            for section in page.sections:
                indent = "  " * (section.level - 1)
                content.append(f"{indent}- {section.title}")
            content.append("")
            
        # Add main content
        content.extend([
            "## Content",
            "",
            page.text if page.text else "No content available.",
            ""
        ])
        
        # Add references if available
        if metadata.get('references', 0) > 0:
            content.extend([
                "## References",
                ""
            ])
            for ref in page.references:
                content.append(f"- {ref}")
            content.append("")
            
        # Add archive info
        content.extend([
            "## Archive Info",
            f"- **Archived on:** {metadata['archive_date']}",
            f"- **Archive Source:** Wikipedia (_{page.language}_)",
            f"- **Total References:** {metadata.get('references', 0)}",
            f"- **Article Size:** {metadata.get('content_size', 0)} bytes",
            f"- **Word Count:** {metadata.get('word_count', 0)} words",
            ""
        ])
        
        return "\n".join(content)
        
    except Exception as e:
        log_message(f"Error formatting content for {page.title if page else 'unknown page'}: {str(e)}", "ERROR")
        return None

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
    article_title, category_name, depth = args
    
    try:
        # Create a local copy of the set to avoid modification during iteration
        with progress_lock:
            if article_title in processed_articles:
                return True, article_title
        
        # Get page with retry
        def get_page():
            with api_lock:
                time.sleep(RATE_LIMIT_DELAY)
                return wiki_wiki.page(article_title)
        
        page = retry_with_backoff(get_page)
        if not page.exists():
            log_message(f"Article does not exist: {article_title}", "WARNING")
            return False, article_title
        
        # Get metadata
        metadata = get_article_metadata(page)
        if metadata is None:
            log_message(f"Failed to get metadata for {article_title}", "ERROR")
            return False, article_title
        
        # Format content
        content = format_article_content(page, metadata)
        if not content:
            log_message(f"Failed to format content for {article_title}", "ERROR")
            return False, article_title
        
        # Save article
        category_dir = os.path.join(OUTPUT_DIR, f"articles_{get_safe_path(category_name)}")
        ensure_directory(category_dir)
        
        article_file = os.path.join(category_dir, f"{get_safe_path(article_title)}.md")
        with open(article_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Update processed articles with lock
        with progress_lock:
            processed_articles.add(article_title)
        
        return True, article_title
        
    except Exception as e:
        global error_count
        with progress_lock:
            error_count += 1
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
        
        # Update progress with category stats
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
                        # Update progress after each successful article
                        save_progress(processed_articles, category_name)
                except Exception as e:
                    log_message(f"Task failed: {str(e)}", "ERROR")
        
        # Update progress file with final category stats
        save_progress(processed_articles, category_name)
        
        # Recursively process subcategories
        if depth < MAX_DEPTH:
            for subcat in subcategories:
                if error_count >= MAX_ERRORS:
                    log_message("Maximum error count reached. Stopping category processing...", "ERROR")
                    break
                scrape_category(subcat, depth + 1)
        
    except Exception as e:
        log_message(f"Error in category scraping for {category_name}: {str(e)}", "ERROR")

def save_progress(processed, current_category=None):
    """Save progress with error handling and atomic writes."""
    try:
        temp_file = PROGRESS_FILE + '.tmp'
        # Convert set to list before processing to prevent modification during iteration
        processed_list = list(processed)
        
        data = {
            'processed': processed_list,
            'last_category': current_category,
            'last_updated': datetime.now(timezone.utc).isoformat()
        }
        
        # Calculate category statistics
        category_stats = {}
        for article in processed_list:  # Use the list instead of the set
            article_path = None
            # Search for the article file
            for root, _, files in os.walk(OUTPUT_DIR):
                for file in files:
                    if file.startswith(get_safe_path(article)) and file.endswith('.md'):
                        article_path = os.path.join(root, file)
                        break
                if article_path:
                    break
            
            if article_path and os.path.exists(article_path):
                try:
                    with open(article_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        category = os.path.basename(os.path.dirname(article_path)).replace('articles_', '')
                        
                        if category not in category_stats:
                            category_stats[category] = {
                                'count': 0,
                                'total_words': 0,
                                'total_size': 0,
                                'has_references': 0,
                                'has_toc': 0,
                                'total_lines': 0
                            }
                        
                        stats = category_stats[category]
                        stats['count'] += 1
                        stats['total_words'] += len(content.split())
                        stats['total_size'] += len(content.encode('utf-8'))
                        stats['has_references'] += 1 if '## References' in content else 0
                        stats['has_toc'] += 1 if '## Table of Contents' in content else 0
                        stats['total_lines'] += len(content.splitlines())
                except Exception as e:
                    log_message(f"Error processing article stats for {article}: {str(e)}", "WARNING")
                    continue
        
        data['category_stats'] = category_stats
        
        # Atomic write with error handling
        try:
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            os.replace(temp_file, PROGRESS_FILE)
        except Exception as e:
            log_message(f"Error writing progress file: {str(e)}", "ERROR")
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except:
                    pass
            raise
        
    except Exception as e:
        log_message(f"Error saving progress: {str(e)}", "ERROR")
        raise  # Re-raise the exception to be handled by the caller

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
        
        # Update progress and README after complete archiving
        try:
            import update_progress
            update_progress.main()
            log_message("Successfully updated README and progress tracking", "INFO")
        except Exception as e:
            log_message(f"Error updating progress: {str(e)}", "ERROR")
        
    except KeyboardInterrupt:
        log_message("Script interrupted by user", "WARNING")
        save_progress(processed_articles, CATEGORY)
        
    except Exception as e:
        log_message(f"Fatal error: {str(e)}", "ERROR")
        save_progress(processed_articles, CATEGORY)
        raise
    
    finally:
        save_progress(processed_articles, CATEGORY)
