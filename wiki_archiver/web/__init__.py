"""
Web interface for browsing archived Wikipedia articles.
"""

import os
import json
from typing import List, Dict

def get_archived_articles(category: str = None, search_query: str = None) -> List[Dict]:
    """
    Retrieve archived articles, optionally filtered by category or search query.
    
    Args:
        category (str, optional): Filter articles by category
        search_query (str, optional): Search articles by title or content
    
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
                    if category:
                        category = category.lower()
                        article_categories = [c.lower() for c in article_data.get('categories', [])]
                        if not any(category in c for c in article_categories):
                            continue
                    
                    # Search query filter
                    if search_query:
                        search_query = search_query.lower()
                        title_match = search_query in article_data.get('title', '').lower()
                        content_match = search_query in article_data.get('content', '').lower()
                        summary_match = search_query in article_data.get('summary', '').lower()
                        
                        if not (title_match or content_match or summary_match):
                            continue
                    
                    articles.append(article_data)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    
    # Sort articles by archived date, most recent first
    articles.sort(key=lambda x: x.get('archived_date', ''), reverse=True)
    
    return articles
