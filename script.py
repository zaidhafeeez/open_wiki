import wikipediaapi
from github import Github
from github.GithubException import GithubException, RateLimitExceededException
import time
import json
from datetime import datetime
import os
from tqdm import tqdm
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')  # Get token from environment variable
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable is not set. Please set it in .env file")
REPO_NAME = "zaidhafeeez/open_wiki"  # GitHub repository
LANGUAGE = "en"  # Language code (e.g., 'en' for English)
CATEGORY = "Python (programming language)"  # Wikipedia category name
MAX_DEPTH = 1  # Maximum depth for subcategory traversal
PROGRESS_FILE = "archive_progress.json"
RATE_LIMIT_PAUSE = 120  # Seconds to wait when rate limit is hit

# Initialize Wikipedia API with rate limiting
wiki_wiki = wikipediaapi.Wikipedia(
    language=LANGUAGE,
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent="WikiArchiveScript/1.0"
)

# Initialize GitHub API
g = Github(GITHUB_TOKEN)
try:
    # Try to get the repository
    repo = g.get_repo(REPO_NAME)
    print(f"Found existing repository: {REPO_NAME}")
except GithubException as e:
    if e.status == 404:
        # Repository doesn't exist, create it
        print(f"Repository {REPO_NAME} not found. Creating it...")
        user = g.get_user()
        repo = user.create_repo(
            name=REPO_NAME.split('/')[-1],
            description="Archived Wikipedia articles about Python programming language",
            auto_init=True
        )
        print(f"Created new repository: {REPO_NAME}")
        # Wait a moment for the repository to be fully created
        time.sleep(5)
    else:
        print(f"Error accessing repository: {e}")
        raise e

# Verify repository access
try:
    repo.get_contents("/")
    print("Successfully verified repository access")
except GithubException as e:
    print(f"Error accessing repository contents: {e}")
    raise e

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
        file_name = f"{safe_category}/{get_safe_path(article_title)}.md"
        file_content = format_article_content(page, metadata)
        print(f"Generated content for {file_name} (size: {len(file_content)} bytes)")

        # Check if the file needs updating
        try:
            print(f"Checking if {file_name} exists in repository...")
            try:
                # Try to create the category directory if it doesn't exist
                try:
                    repo.get_contents(safe_category)
                except GithubException as e:
                    if e.status == 404:
                        print(f"Creating category directory: {safe_category}")
                        repo.create_file(
                            f"{safe_category}/README.md",
                            f"Create {category_path} directory",
                            f"# {category_path}\n\nWikipedia articles related to {category_path}"
                        )
                        time.sleep(1)  # Wait for directory creation
            except Exception as e:
                print(f"Error checking/creating directory: {e}")

            contents = repo.get_contents(file_name)
            existing_content = contents.decoded_content.decode('utf-8')
            if "Last updated:" in existing_content:
                print(f"Updating '{article_title}'")
                result = repo.update_file(
                    file_name,
                    f"Update {article_title} article",
                    file_content,
                    contents.sha
                )
                print(f"Updated file: {file_name} (commit: {result['commit'].sha})")
            else:
                print(f"Article '{file_name}' exists but no update needed.")
        except GithubException as e:
            if e.status == 404:
                # File doesn't exist, create it
                print(f"Creating new file: {file_name}")
                try:
                    result = repo.create_file(
                        file_name,
                        f"Add {article_title} article",
                        file_content
                    )
                    print(f"Created new file: {file_name} (commit: {result['commit'].sha})")
                except GithubException as create_error:
                    print(f"Error creating file: {create_error}")
                    print(f"Error data: {create_error.data}")
                    raise create_error
            else:
                print(f"GitHub error: {e}")
                print(f"Error data: {e.data}")
                raise e

        processed_articles.append(article_title)
        save_progress(processed_articles)
        print(f"Saved progress. Waiting 1 second before next article...")
        time.sleep(1)  # Rate limiting precaution

    except RateLimitExceededException:
        print(f"GitHub API rate limit exceeded. Waiting {RATE_LIMIT_PAUSE} seconds...")
        time.sleep(RATE_LIMIT_PAUSE)
        return scrape_and_store_article(article_title, processed_articles, category_path)

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

def cleanup_root_directory():
    print("\nCleaning up root directory...")
    try:
        # Get all files in root
        contents = repo.get_contents("")
        for content in contents:
            if content.path.endswith('.md') and content.path != 'README.md':
                print(f"Removing {content.path} from root...")
                repo.delete_file(
                    content.path,
                    f"Move {content.path} to category directory",
                    content.sha
                )
                print(f"Removed {content.path}")
                time.sleep(1)  # Rate limiting precaution
    except Exception as e:
        print(f"Error cleaning up root directory: {e}")

if __name__ == "__main__":
    try:
        # Clean up root directory first
        cleanup_root_directory()
        
        progress = load_progress()
        start_category = progress['last_category'] or CATEGORY
        if progress['processed']:
            print(f"Resuming from category: {start_category}")
            print(f"Already processed: {len(progress['processed'])} articles")
        
        scrape_category(start_category)
        
        # Clean up progress file after successful completion
        if os.path.exists(PROGRESS_FILE):
            os.remove(PROGRESS_FILE)
            
    except KeyboardInterrupt:
        print("\nScript interrupted. Progress saved.")
    except Exception as e:
        print(f"An error occurred: {e}")
