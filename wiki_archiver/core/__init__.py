"""
Core processing module for Wikipedia Article Archiver.

Handles article and category processing, metadata extraction, and content formatting.
"""

import os
import json
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import wikipediaapi

from ..config import *
from ..utils import get_safe_path, retry_with_backoff, ensure_directory
from ..logging import logger
from datetime import datetime

class WikiArchiver:
    def __init__(self, language=LANGUAGE, categories=CATEGORIES, max_depth=MAX_DEPTH):
        """
        Initialize the Wikipedia archiver.
        
        Args:
            language (str): Language of Wikipedia articles
            categories (list): List of categories to archive
            max_depth (int): Maximum recursion depth for category processing
        """
        self.language = language
        self.categories = categories if isinstance(categories, list) else [categories]
        self.max_depth = max_depth
        
        self.wiki_wiki = wikipediaapi.Wikipedia(
            language=self.language,
            extract_format=wikipediaapi.ExtractFormat.WIKI,
            user_agent=USER_AGENT
        )
        
        self.processed_articles = set()
        self.progress_lock = threading.Lock()
        self.error_count = 0
    
    def get_article_metadata(self, page):
        """
        Extract metadata from a Wikipedia page.
        
        Args:
            page: Wikipedia page object
        
        Returns:
            dict: Article metadata
        """
        try:
            return {
                'title': page.title,
                'url': page.fullurl,
                'summary': page.summary[:500],  # First 500 characters
                'categories': list(page.categories.keys()),
                'references': len(page.references) if hasattr(page, 'references') else 0,
                'last_modified': page.touched,
                'language': self.language
            }
        except Exception as e:
            logger.error(f"Error extracting metadata for {page.title}: {e}")
            return {}
    
    def format_article_content(self, page, metadata):
        """
        Format article content in Markdown with metadata.
        
        Args:
            page: Wikipedia page object
            metadata (dict): Article metadata
        
        Returns:
            str: Formatted article content in Markdown
        """
        try:
            # Markdown template with front matter
            markdown_content = f"""---
title: {metadata['title']}
url: {metadata['url']}
language: {metadata['language']}
categories: {json.dumps(metadata['categories'])}
references: {metadata['references']}
last_modified: {metadata['last_modified']}
---

# {metadata['title']}

## Summary

{metadata['summary']}

## Full Content

{page.text}
"""
            return markdown_content
        except Exception as e:
            logger.error(f"Error formatting content for {page.title}: {e}")
            return ""
    
    @retry_with_backoff
    def process_article(self, article_title, category_name, depth):
        """
        Process a single article with error handling.
        
        Args:
            article_title (str): Title of the article
            category_name (str): Category of the article
            depth (int): Current processing depth
        
        Returns:
            tuple: (success, article_title)
        """
        try:
            # Check if article has been processed
            with self.progress_lock:
                if article_title in self.processed_articles:
                    return False, article_title
                
                self.processed_articles.add(article_title)
            
            # Fetch page
            page = self.wiki_wiki.page(article_title)
            
            if not page.exists():
                logger.warning(f"Article does not exist: {article_title}")
                return False, article_title
            
            # Extract metadata
            metadata = self.get_article_metadata(page)
            
            # Format content
            content = self.format_article_content(page, metadata)
            
            # Create safe filename
            safe_filename = get_safe_path(article_title)
            category_dir = os.path.join(OUTPUT_DIR, get_safe_path(category_name))
            ensure_directory(category_dir)
            
            # Write article
            file_path = os.path.join(category_dir, f"{safe_filename}.md")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Save JSON for web interface
            article_data = {
                'title': metadata['title'],
                'summary': metadata['summary'],
                'content': content,
                'categories': metadata['categories'],
                'source_url': metadata['url']
            }
            self.save_article_json(article_data, OUTPUT_DIR)
            
            logger.info(f"Processed article: {article_title}")
            return True, article_title
        
        except Exception as e:
            logger.error(f"Error processing {article_title}: {e}")
            return False, article_title
    
    def save_article_json(self, article_data: dict, output_dir: str):
        """
        Save article data as a JSON file for web interface.
        
        Args:
            article_data (dict): Article information
            output_dir (str): Output directory for articles
        """
        # Ensure articles directory exists
        articles_dir = os.path.join(output_dir, 'articles')
        os.makedirs(articles_dir, exist_ok=True)
        
        # Create a safe filename
        safe_title = ''.join(c if c.isalnum() or c in [' ', '_'] else '_' for c in article_data.get('title', 'unknown'))
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        filename = f"{safe_title}_{timestamp}.json"
        
        # Full path for the JSON file
        filepath = os.path.join(articles_dir, filename)
        
        # Prepare article data for web interface
        web_article_data = {
            'title': article_data.get('title', 'Unknown Title'),
            'summary': article_data.get('summary', ''),
            'content': article_data.get('content', ''),
            'categories': article_data.get('categories', []),
            'archived_date': timestamp,
            'source_url': article_data.get('source_url', '')
        }
        
        # Write JSON file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(web_article_data, f, indent=2, ensure_ascii=False)
    
    def process_category(self, category_name, depth=0):
        """
        Process a single category and return its articles and subcategories.
        
        Args:
            category_name (str): Name of the category to process
            depth (int): Current depth level
        
        Returns:
            tuple: (articles, subcategories)
        """
        if depth > self.max_depth:
            return set(), set()
        
        category_page = self.wiki_wiki.page(f"Category:{category_name}")
        
        if not category_page.exists():
            logger.warning(f"Category does not exist: {category_name}")
            return set(), set()
        
        articles = set()
        subcategories = set()
        
        for title, page in category_page.categorymembers.items():
            if page.ns == wikipediaapi.Namespace.CATEGORY:
                subcategories.add(page.title.replace("Category:", ""))
            elif page.ns == wikipediaapi.Namespace.MAIN:
                articles.add(page.title)
        
        return articles, subcategories
    
    def scrape_categories(self):
        """
        Process multiple categories in parallel.
        """
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [
                executor.submit(self.scrape_category, category)
                for category in self.categories
            ]
            
            # Wait for all categories to be processed
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logger.error(f"Error processing category: {e}")
    
    def scrape_category(self, category_name, depth=0):
        """
        Process a single category and its subcategories.
        
        Args:
            category_name (str): Name of the category to process
            depth (int): Current depth level
        """
        logger.info(f"Processing category: {category_name}")
        
        if depth > self.max_depth:
            return
        
        # Get articles and subcategories
        articles, subcategories = self.process_category(category_name, depth)
        
        # Process articles in parallel
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [
                executor.submit(self.process_article, article, category_name, depth)
                for article in articles
            ]
            
            # Wait for all articles to be processed
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logger.error(f"Error processing article: {e}")
        
        # Recursively process subcategories
        for subcategory in subcategories:
            self.scrape_category(subcategory, depth + 1)
    
    def save_progress(self):
        """
        Save the current progress of article archiving.
        
        Handles potential errors during progress saving.
        """
        try:
            progress = {
                'processed': list(self.processed_articles),
                'last_category': self.categories[-1] if self.categories else None,
                'last_updated': datetime.utcnow().isoformat(),
                'category_stats': getattr(self, 'category_stats', {})
            }
            
            # Ensure output directory exists
            ensure_directory(OUTPUT_DIR)
            
            # Save progress to JSON file using the global PROGRESS_FILE path
            progress_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), PROGRESS_FILE)
            with open(progress_file, 'w', encoding='utf-8') as f:
                json.dump(progress, f, indent=2)
            
            logger.info(f"Progress saved to {progress_file}")
        except Exception as e:
            logger.error(f"Error saving progress: {e}")

    def load_progress(self):
        """
        Load progress from the JSON file.
        
        Returns:
            dict: Loaded progress data
        """
        try:
            # Use the global PROGRESS_FILE path
            progress_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), PROGRESS_FILE)
            if os.path.exists(progress_file):
                with open(progress_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            logger.error(f"Error loading progress: {e}")
            return {}
