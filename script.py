import wikipediaapi
from github import Github
from github.GithubException import GithubException, RateLimitExceededException
import time

# Configuration
GITHUB_TOKEN = "your_github_personal_access_token"  # Replace with your token
REPO_NAME = "your_github_username/article-archive"  # Replace with your repository name
LANGUAGE = "en"  # Language code (e.g., 'en' for English)
CATEGORY = "Python programming language"  # Replace with your desired category

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia(LANGUAGE)

# Initialize GitHub API
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

def scrape_and_store_article(article_title):
    try:
        # Fetch article content
        page = wiki_wiki.page(article_title)
        if not page.exists():
            print(f"Article '{article_title}' does not exist.")
            return

        # Format the file name and content
        file_name = f"{article_title.replace(' ', '_')}.md"
        file_content = f"# {page.title}\n\n{page.text}"

        # Check if the file already exists in the repo
        try:
            contents = repo.get_contents(file_name)
            print(f"File '{file_name}' already exists in the repository.")
        except GithubException:
            contents = None  # File does not exist, safe to create

        # Commit to GitHub
        if contents is None:
            repo.create_file(file_name, f"Add {article_title} article", file_content)
            print(f"Article '{article_title}' has been added to the repository.")
        else:
            print(f"Article '{article_title}' already archived.")

    except RateLimitExceededException:
        print("GitHub API rate limit exceeded. Retrying after a cooldown...")
        time.sleep(60)  # Wait for 60 seconds before retrying
        scrape_and_store_article(article_title)

    except GithubException as e:
        print(f"GitHub API error occurred: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def scrape_category(category_name):
    # Fetch category
    category = wiki_wiki.page(f"Category:{category_name}")
    if not category.exists():
        print(f"Category '{category_name}' does not exist.")
        return

    print(f"Scraping articles in category: {category_name}")
    for title in category.categorymembers.keys():
        if "Category:" not in title:  # Skip subcategories
            scrape_and_store_article(title)

if __name__ == "__main__":
    try:
        scrape_category(CATEGORY)
    except Exception as e:
        print(f"An error occurred: {e}")
