#!/usr/bin/env python3
"""Create test articles for progress visualization."""

import os
import random

def create_test_articles():
    """Create test articles in various categories."""
    base_path = "wiki_articles/articles/Python_(programming_language)"
    categories = {
        'core_language': 25,  # 50% of target
        'libraries_frameworks': 80,  # 80% of target
        'development_tools': 15,  # 50% of target
        'community_culture': 16,  # 80% of target
        'applications': 24,  # 60% of target
    }
    
    for category, count in categories.items():
        category_path = os.path.join(base_path, category)
        os.makedirs(category_path, exist_ok=True)
        
        for i in range(count):
            article_name = f"test_article_{i+1}.md"
            article_path = os.path.join(category_path, article_name)
            
            with open(article_path, 'w', encoding='utf-8') as f:
                f.write(f"# Test Article {i+1}\n\nThis is a test article in the {category} category.")

if __name__ == "__main__":
    create_test_articles()
