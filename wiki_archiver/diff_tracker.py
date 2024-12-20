"""
Article Diff Tracking Module for Wikipedia Article Archiver.

Provides functionality to track and analyze changes in Wikipedia articles
over time by comparing different versions of article content.
"""

import os
import json
import difflib
from datetime import datetime
from typing import Dict, List, Optional, Tuple

import wikipediaapi

from .config import OUTPUT_DIR
from .logging import logger

class ArticleDiffTracker:
    """
    Tracks and manages differences between Wikipedia article versions.
    
    Supports:
    - Storing article versions
    - Generating text diffs
    - Tracking article change history
    """
    
    def __init__(self, 
                 language: str = 'en', 
                 output_dir: str = OUTPUT_DIR,
                 user_agent: str = 'WikiArchiver/1.0'):
        """
        Initialize the Article Diff Tracker.
        
        Args:
            language (str, optional): Wikipedia language. Defaults to 'en'.
            output_dir (str, optional): Directory to store diff information.
            user_agent (str, optional): User agent for Wikipedia API.
        """
        self.language = language
        self.output_dir = os.path.join(output_dir, 'article_diffs')
        os.makedirs(self.output_dir, exist_ok=True)
        
        self.wiki = wikipediaapi.Wikipedia(
            language=self.language,
            extract_format=wikipediaapi.ExtractFormat.WIKI,
            user_agent=user_agent
        )
    
    def _get_article_content(self, title: str) -> Optional[str]:
        """
        Retrieve article content from Wikipedia.
        
        Args:
            title (str): Title of the Wikipedia article
        
        Returns:
            Optional[str]: Article content or None if not found
        """
        try:
            page = self.wiki.page(title)
            return page.text if page.exists() else None
        except Exception as e:
            logger.error(f"Error retrieving article {title}: {e}")
            return None
    
    def _save_article_version(self, 
                               title: str, 
                               content: str) -> str:
        """
        Save a specific version of an article.
        
        Args:
            title (str): Article title
            content (str): Article content
        
        Returns:
            str: Path to saved article version
        """
        # Create safe filename
        safe_title = ''.join(c if c.isalnum() or c in [' ', '_'] else '_' for c in title)
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        filename = f"{safe_title}_{timestamp}.txt"
        
        version_path = os.path.join(self.output_dir, filename)
        
        with open(version_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return version_path
    
    def track_article_changes(self, 
                               title: str, 
                               previous_version_path: Optional[str] = None) -> Dict:
        """
        Track changes in a Wikipedia article.
        
        Args:
            title (str): Title of the Wikipedia article
            previous_version_path (str, optional): Path to previous article version
        
        Returns:
            Dict: Change tracking information
        """
        # Retrieve current article content
        current_content = self._get_article_content(title)
        
        if current_content is None:
            logger.warning(f"Could not retrieve article: {title}")
            return {}
        
        # Save current version
        current_version_path = self._save_article_version(title, current_content)
        
        # Compare with previous version if available
        diff_result = {
            'title': title,
            'current_version': current_version_path,
            'previous_version': previous_version_path,
            'changes': []
        }
        
        if previous_version_path:
            try:
                with open(previous_version_path, 'r', encoding='utf-8') as f:
                    previous_content = f.read()
                
                # Generate detailed diff
                differ = difflib.Differ()
                diff = list(differ.compare(
                    previous_content.splitlines(), 
                    current_content.splitlines()
                ))
                
                # Extract change details
                changes = [
                    line for line in diff 
                    if line.startswith('- ') or line.startswith('+ ')
                ]
                
                diff_result['changes'] = changes
                diff_result['change_summary'] = {
                    'added_lines': len([c for c in changes if c.startswith('+ ')]),
                    'removed_lines': len([c for c in changes if c.startswith('- ')])
                }
                
                logger.info(f"Tracked changes for article: {title}")
            
            except Exception as e:
                logger.error(f"Error comparing versions for {title}: {e}")
        
        return diff_result
    
    def get_article_history(self, title: str) -> List[str]:
        """
        Retrieve all saved versions of an article.
        
        Args:
            title (str): Article title
        
        Returns:
            List[str]: Paths to saved article versions
        """
        safe_title = ''.join(c if c.isalnum() or c in [' ', '_'] else '_' for c in title)
        versions = [
            os.path.join(self.output_dir, f) 
            for f in os.listdir(self.output_dir) 
            if f.startswith(safe_title) and f.endswith('.txt')
        ]
        return sorted(versions)

def track_wikipedia_article_changes(
    title: str, 
    language: str = 'en'
) -> Dict:
    """
    Convenience function to track changes in a Wikipedia article.
    
    Args:
        title (str): Title of the Wikipedia article
        language (str, optional): Wikipedia language
    
    Returns:
        Dict: Article change tracking information
    """
    tracker = ArticleDiffTracker(language=language)
    
    # Get previous versions if they exist
    history = tracker.get_article_history(title)
    previous_version = history[-1] if history else None
    
    return tracker.track_article_changes(title, previous_version)
