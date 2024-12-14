import wikipediaapi
from datetime import datetime
import time
import json
import os
from tqdm import tqdm

# Configuration
LANGUAGE = "en"  # Language code (e.g., 'en' for English)
CATEGORY = "Python (programming language)"  # Wikipedia category name
MAX_DEPTH = 1  # Maximum depth for subcategory traversal
PROGRESS_FILE = "archive_progress.json"
OUTPUT_DIR = "wiki_articles"  # Local directory to store articles

# Initialize Wikipedia API with rate limiting
wiki_wiki = wikipediaapi.Wikipedia(
    language=LANGUAGE,
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent="WikiArchiveScript/1.0"
)

def get_safe_path(name):
    """Convert a string to a safe path name"""
    return name.replace(' ', '_').replace('/', '_').replace('\\', '_')

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {'processed': [], 'last_category': None}

def save_progress(processed_articles, current_category=None):
    progress = {
        'processed': processed_articles,
        'last_category': current_category
    }
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f)

def get_article_metadata(page):
    return {
        'title': page.title,
        'url': page.fullurl,
        'summary': page.summary[0:500] if page.summary else "",
        'last_updated': datetime.utcnow().isoformat(),
        'categories': [cat.title for cat in page.categories.values()]
    }

def format_article_content(page, metadata):
    content = f"# {page.title}\n\n"
    content += f"_Last updated: {metadata['last_updated']}_\n\n"
    content += f"**Original Article:** [{page.title}]({metadata['url']})\n\n"
    content += f"**Summary:** {metadata['summary']}\n\n"
    content += "## Categories\n"
    for cat in metadata['categories']:
        content += f"- {cat}\n"
    content += "\n## Content\n\n"
    content += page.text
    return content

def ensure_directory(directory):
    """Create directory if it doesn't exist"""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def scrape_and_store_article(article_title, processed_articles, category_path='articles'):
    if article_title in processed_articles:
        print(f"Skipping '{article_title}' (already processed)")
        return processed_articles

    try:
        print(f"\nProcessing article: {article_title}")
        # Fetch article content
        page = wiki_wiki.page(article_title)
        if not page.exists():
            print(f"Article '{article_title}' does not exist.")
            return processed_articles

        # Get metadata and format content
        metadata = get_article_metadata(page)
        safe_category = get_safe_path(category_path)
        directory_path = os.path.join(OUTPUT_DIR, safe_category)
        ensure_directory(directory_path)
        
        file_path = os.path.join(directory_path, f"{get_safe_path(article_title)}.md")
        file_content = format_article_content(page, metadata)
        print(f"Generated content for {file_path} (size: {len(file_content)} bytes)")

        # Create README for category if it doesn't exist
        readme_path = os.path.join(directory_path, "README.md")
        if not os.path.exists(readme_path):
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(f"# {category_path}\n\nWikipedia articles related to {category_path}")
            print(f"Created category README: {readme_path}")

        # Save the article
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_content)
        print(f"Saved article to: {file_path}")

        processed_articles.append(article_title)
        save_progress(processed_articles)
        print(f"Saved progress. Waiting 1 second before next article...")
        time.sleep(1)  # Rate limiting precaution

    except Exception as e:
        print(f"Error processing '{article_title}': {e}")
        print(f"Error type: {type(e)}")
        import traceback
        traceback.print_exc()

    return processed_articles

def scrape_category(category_name, depth=0, processed_articles=None):
    if processed_articles is None:
        progress = load_progress()
        processed_articles = progress['processed']

    if depth > MAX_DEPTH:
        return processed_articles

    category = wiki_wiki.page(f"Category:{category_name}")
    if not category.exists():
        print(f"Category '{category_name}' does not exist.")
        return processed_articles

    print(f"Processing category: {category_name} (depth: {depth})")
    members = list(category.categorymembers.keys())
    print(f"Found {len(members)} members in category")
    
    with tqdm(total=len(members), desc=f"Category: {category_name}") as pbar:
        for title in members:
            print(f"Processing member: {title}")
            if "Category:" in title and depth < MAX_DEPTH:
                # Process subcategory
                sub_category = title.replace("Category:", "")
                processed_articles = scrape_category(
                    sub_category, 
                    depth + 1, 
                    processed_articles
                )
            else:
                # Process article
                category_path = f"articles/{get_safe_path(category_name)}"
                processed_articles = scrape_and_store_article(
                    title,
                    processed_articles,
                    category_path
                )
            pbar.update(1)
            save_progress(processed_articles, category_name)

    return processed_articles

if __name__ == "__main__":
    try:
        # Create output directory if it doesn't exist
        ensure_directory(OUTPUT_DIR)
        
        progress = load_progress()
        start_category = progress['last_category'] or CATEGORY
        if progress['processed']:
            print(f"Resuming from category: {start_category}")
            print(f"Already processed: {len(progress['processed'])} articles")
        
        scrape_category(start_category)
        
        # Clean up progress file after successful completion
        if os.path.exists(PROGRESS_FILE):
            os.remove(PROGRESS_FILE)
        
        print(f"\nAll articles have been saved to the '{OUTPUT_DIR}' directory.")
        print("You can now review the articles and commit them to your repository manually.")
            
    except KeyboardInterrupt:
        print("\nScript interrupted. Progress saved.")
    except Exception as e:
        print(f"An error occurred: {e}")
