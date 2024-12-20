"""
Web interface for browsing archived Wikipedia articles.
"""

import os
import json
from typing import List, Dict

def get_archived_articles(category: str = None) -> List[Dict]:
    """
    Retrieve archived articles, optionally filtered by category.
    
    Args:
        category (str, optional): Filter articles by category
    
    Returns:
        List of archived article metadata
    """
    from ..config import OUTPUT_DIR
    
    articles = []
    articles_dir = os.path.join(OUTPUT_DIR, 'articles')
    
    if not os.path.exists(articles_dir):
        return articles
    
    for filename in os.listdir(articles_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(articles_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    article_data = json.load(f)
                    
                    # Filter by category if specified
                    if category and category.lower() not in article_data.get('categories', []):
                        continue
                    
                    articles.append(article_data)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    
    return articles
