"""
Programmatic API for Wikipedia Article Archiver.

Provides a high-level interface for archiving Wikipedia articles 
and managing the archiving process.
"""

import os
import json
from typing import List, Dict, Optional

from .core import WikiArchiver
from .config import LANGUAGE, CATEGORIES, MAX_DEPTH, OUTPUT_DIR
from .logging import logger

class WikiArchiveAPI:
    """
    API for interacting with the Wikipedia Article Archiver.
    
    Provides methods for archiving articles, managing progress, 
    and retrieving archive information.
    """
    
    def __init__(self, 
                 language: str = LANGUAGE, 
                 categories: Optional[List[str]] = None, 
                 max_depth: int = MAX_DEPTH,
                 output_dir: str = OUTPUT_DIR):
        """
        Initialize the Wiki Archive API.
        
        Args:
            language (str, optional): Wikipedia language. Defaults to English.
            categories (List[str], optional): Categories to archive. 
                                             Defaults to predefined categories.
            max_depth (int, optional): Maximum category recursion depth.
            output_dir (str, optional): Directory to store archived articles.
        """
        self.language = language
        self.categories = categories or CATEGORIES
        self.max_depth = max_depth
        self.output_dir = output_dir
        
        # Validate output directory
        os.makedirs(self.output_dir, exist_ok=True)
    
    def archive_categories(self, 
                           categories: Optional[List[str]] = None, 
                           max_depth: Optional[int] = None) -> Dict[str, List[str]]:
        """
        Archive articles from specified categories.
        
        Args:
            categories (List[str], optional): Categories to archive. 
                                             Uses default if not provided.
            max_depth (int, optional): Maximum category recursion depth.
        
        Returns:
            Dict[str, List[str]]: Dictionary of processed categories and their articles
        """
        # Use provided or default categories and depth
        target_categories = categories or self.categories
        target_depth = max_depth if max_depth is not None else self.max_depth
        
        # Create archiver instance
        archiver = WikiArchiver(
            language=self.language, 
            categories=target_categories, 
            max_depth=target_depth
        )
        
        # Perform archiving
        logger.info(f"Starting archive for categories: {target_categories}")
        archiver.scrape_categories()
        
        return {
            'processed_categories': target_categories,
            'processed_articles': list(archiver.processed_articles)
        }
    
    def get_archive_progress(self) -> Dict:
        """
        Retrieve the current archiving progress.
        
        Returns:
            Dict: Progress information including processed articles and categories
        """
        progress_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            'archive_progress.json'
        )
        
        try:
            with open(progress_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning("No progress file found.")
            return {}
        except json.JSONDecodeError:
            logger.error("Invalid progress file format.")
            return {}
    
    def list_archived_articles(self, category: Optional[str] = None) -> List[str]:
        """
        List archived articles, optionally filtered by category.
        
        Args:
            category (str, optional): Filter articles by specific category.
        
        Returns:
            List[str]: List of archived article paths
        """
        archived_articles = []
        for root, _, files in os.walk(self.output_dir):
            for file in files:
                if file.endswith('.md'):
                    article_path = os.path.join(root, file)
                    if category is None or category.lower() in root.lower():
                        archived_articles.append(article_path)
        
        return archived_articles

def archive_wikipedia(
    categories: Optional[List[str]] = None, 
    language: str = LANGUAGE, 
    max_depth: int = MAX_DEPTH
) -> Dict[str, List[str]]:
    """
    Convenience function for quick Wikipedia archiving.
    
    Args:
        categories (List[str], optional): Categories to archive
        language (str, optional): Wikipedia language
        max_depth (int, optional): Maximum category recursion depth
    
    Returns:
        Dict[str, List[str]]: Archiving results
    """
    api = WikiArchiveAPI(language=language)
    return api.archive_categories(categories, max_depth)
