"""
Script to scrape and store Wikipedia articles in a GitHub repository.

This script uses the wikipedia-api library to scrape articles from Wikipedia and
the PyGithub library to store them in a GitHub repository.

The script takes three configuration parameters:

- GITHUB_TOKEN: the GitHub API token to use for authentication
- REPO_NAME: the name of the repository where the articles should be stored
- LANGUAGE: the language of the Wikipedia articles to scrape (default: English)

The script uses the following logic to scrape and store articles:

1. Query the Wikipedia API to get the contents of the article
2. If the article does not exist on Wikipedia, print a message and return
3. If the GitHub API rate limit has been exceeded, print a message, wait for 60
   seconds and retry
4. Otherwise, store the article in the specified repository using the PyGithub
   library

"""

import wikipediaapi
from github import Github
from github.GithubException import GithubException, RateLimitExceededException
import time

# Configuration
GITHUB_TOKEN = ""
REPO_NAME = ""
LANGUAGE = "en"

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia(LANGUAGE)

# Initialize GitHub API
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

def scrape_and_store_article(article_title):
    try:
        page = wiki_wiki.page(article_title)
        if not page.exists():
            print(f"Article '{article_title}' not found on Wikipedia.")
            return
        
        # Format the file bane and content
        file_name = f"{article_title.replace(' ', '_')}.md"
        file_content = f"# {page.title}\n\n{page.text}\n"

        # CHeck if the file already exists
        try:
            contents = repo.get_contents(file_name)
            print(f"File '{file_name}' already exists. Skipping...")
        except GithubException:
            contents = None

        # Commit to GitHub
        if contents is None:
            repo.create_file(file_name, f"Add {article_title} article", file_content)
            print(f"Article '{article_title}' has been added to the repository.")
        else:
            print(f"Article '{article_title}' already archived.")

    except RateLimitExceededException as e:
        print("GitHub API rate limit exceeded. Retrying after a cooldown...")
        time.sleep(60)  # Wait for 60 seconds before retrying
        scrape_and_store_article(article_title)

    except GithubException as e:
        print(f"GitHub API error occurred: {e.data['message']}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # List of articles to scrape
    article_to_scrape = [
        "Python_(programming_language)",
        "Linux",
        "Git",
        "Docker",
        "Kubernetes",
        "Amazon_Web_Services",
        "Google_Cloud_Platform",
        "Microsoft_Azure",
        "Oracle_Cloud",
        "IBM_Cloud",
        "Oracle_Cloud",
        "IBM_Cloud",
        "Google_Cloud_Platform",
        "Microsoft_Azure",
        "Amazon_Web_Services",
        "Kubernetes",
        "Docker",
        "Git",
        "Linux",
    ]

    for article in article_to_scrape:
        try:
            scrape_and_store_article(article)
        except RateLimitExceededException:
            print("Rate limit hit during batch processing. Retrying after cooldown...")
            time.sleep(60)  # Wait for 60 seconds before retrying the batch
        except Exception as e:
            print(f"An unexpected error occurred during batch processing: {e}")

    print("Batch processing completed.")
