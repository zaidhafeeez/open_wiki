#!/usr/bin/env python3
"""
Helper script to update the README.md with current archiving progress.
This script is designed to be run by GitHub Actions after each archive run.
"""

import os
import re
from datetime import datetime
from typing import Dict, List, Tuple
import json
from collections import defaultdict

def count_articles_in_category(category_path: str) -> Tuple[int, Dict[str, int]]:
    """Count articles and gather statistics in a category directory."""
    if not os.path.exists(category_path):
        return 0, {}
    
    stats = defaultdict(int)
    articles = [f for f in os.listdir(category_path) if f.endswith('.md')]
    
    for article in articles:
        # Get file size
        size = os.path.getsize(os.path.join(category_path, article))
        stats['total_size'] += size
        
        # Read article to get more stats
        with open(os.path.join(category_path, article), 'r', encoding='utf-8') as f:
            content = f.read()
            stats['total_words'] += len(content.split())
            stats['total_lines'] += len(content.splitlines())
            stats['has_references'] += 1 if '## References' in content else 0
            stats['has_toc'] += 1 if '## Table of Contents' in content else 0
    
    return len(articles), dict(stats)

def format_size(size_bytes: int) -> str:
    """Format size in bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"

def get_category_stats() -> Dict[str, Dict]:
    """Get detailed statistics for each category."""
    categories = {
        'Core Language': 'core_language',
        'Libraries & Frameworks': 'libraries_frameworks',
        'Development Tools': 'development_tools',
        'Community & Culture': 'community_culture',
        'Applications': 'applications'
    }
    
    base_path = "wiki_articles/articles/Python_(programming_language)"
    stats = {}
    total_stats = defaultdict(int)
    
    for display_name, dir_name in categories.items():
        path = os.path.join(base_path, dir_name)
        article_count, detailed_stats = count_articles_in_category(path)
        
        # Update total stats
        for key, value in detailed_stats.items():
            total_stats[key] += value
        
        # Estimate target count for each category
        target_count = {'Core Language': 50, 'Libraries & Frameworks': 100,
                       'Development Tools': 30, 'Community & Culture': 20,
                       'Applications': 40}[display_name]
        
        progress = min(100, (article_count / target_count) * 100)
        
        stats[display_name] = {
            'count': article_count,
            'target': target_count,
            'progress': progress,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M UTC'),
            'detailed_stats': detailed_stats
        }
    
    # Add total stats to each category for percentage calculations
    for category_stats in stats.values():
        category_stats['total_stats'] = dict(total_stats)
    
    return stats

def create_progress_bar(percentage: float) -> str:
    """Create a progress bar string based on percentage."""
    filled = int(percentage / 10)
    empty = 10 - filled
    return f"[{'█' * filled}{'░' * empty}] {percentage:.0f}%"

def get_recent_updates(limit: int = 3) -> List[str]:
    """Get the most recent archive updates."""
    updates_file = "archive_updates.json"
    
    if os.path.exists(updates_file):
        try:
            with open(updates_file, 'r', encoding='utf-8') as f:
                all_updates = json.load(f)
                return all_updates[:limit]
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    
    # Fallback to default updates
    return [
        f"Updated core language articles ({datetime.now().strftime('%Y-%m-%d')})",
        f"Added new framework documentation ({datetime.now().strftime('%Y-%m-%d')})",
        f"Refreshed community articles ({datetime.now().strftime('%Y-%m-%d')})"
    ][:limit]

def update_readme(stats: Dict[str, Dict], updates: List[str]):
    """Update the README.md with current progress."""
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update progress bars section (unchanged)
    progress_section = "Python (programming language)\n"
    total_progress = 0
    
    for category, data in stats.items():
        progress = data['progress']
        total_progress += progress
        progress_bar = create_progress_bar(progress)
        progress_section += f"{progress_bar} - {category}\n"
    
    overall_progress = create_progress_bar(total_progress / len(stats))
    progress_section += f"{overall_progress} - Overall progress"
    
    pattern = r"Python \(programming language\).*?Overall progress"
    content = re.sub(pattern, progress_section, content, flags=re.DOTALL)
    
    # Calculate global statistics
    total_articles = sum(d['count'] for d in stats.values())
    total_size = sum(d['detailed_stats'].get('total_size', 0) for d in stats.values())
    total_words = sum(d['detailed_stats'].get('total_words', 0) for d in stats.values())
    total_refs = sum(d['detailed_stats'].get('has_references', 0) for d in stats.values())
    
    # Update statistics
    replacements = {
        '<!-- PROGRESS_TIMESTAMP -->': datetime.now().strftime('%Y-%m-%d %H:%M UTC'),
        '<!-- TOTAL_ARTICLES -->': str(total_articles),
        '<!-- TOTAL_SIZE -->': format_size(total_size),
        '<!-- TOTAL_WORDS -->': f"{total_words:,}",
        '<!-- ARTICLES_WITH_REFS -->': f"{total_refs:,}",
        '<!-- CATEGORIES_PROCESSED -->': str(len(stats)),
        '<!-- ACTIVE_CONTRIBUTORS -->': str(len(set(u.split()[0] for u in updates))),
        '<!-- AVG_WORDS_PER_ARTICLE -->': f"{int(total_words/total_articles):,}" if total_articles else "0"
    }
    
    # Update category details
    for category, data in stats.items():
        safe_category = category.upper().replace(' & ', '_').replace(' ', '_')
        detailed = data['detailed_stats']
        
        replacements.update({
            f'<!-- {safe_category}_COUNT -->': str(data['count']),
            f'<!-- {safe_category}_UPDATED -->': data['last_updated'],
            f'<!-- {safe_category}_STATUS -->': '✅ Complete' if data['progress'] >= 100 else '🔄 In Progress',
            f'<!-- {safe_category}_WORDS -->': f"{detailed.get('total_words', 0):,}",
            f'<!-- {safe_category}_SIZE -->': format_size(detailed.get('total_size', 0)),
            f'<!-- {safe_category}_REFS -->': str(detailed.get('has_references', 0)),
            f'<!-- {safe_category}_LINES -->': f"{detailed.get('total_lines', 0):,}",
            f'<!-- {safe_category}_TOC -->': str(detailed.get('has_toc', 0))
        })
    
    # Update recent updates
    updates_section = "\n".join(f"- {update}" for update in updates)
    content = re.sub(r'<!-- BEGIN_UPDATES -->.*?<!-- END_UPDATES -->', 
                    f'<!-- BEGIN_UPDATES -->\n{updates_section}\n<!-- END_UPDATES -->', 
                    content, flags=re.DOTALL)
    
    # Apply all replacements
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """Main function to update the README progress."""
    stats = get_category_stats()
    updates = get_recent_updates()
    update_readme(stats, updates)
    print("README.md has been updated with current progress.")

if __name__ == "__main__":
    main()
