#!/usr/bin/env python3
"""
Helper script to update the README.md with current archiving progress.
This script is designed to be run by GitHub Actions after each archive run.
"""

import os
import re
from datetime import datetime
from typing import Dict, List, Tuple

def count_articles_in_category(category_path: str) -> int:
    """Count the number of markdown files in a category directory."""
    if not os.path.exists(category_path):
        return 0
    return len([f for f in os.listdir(category_path) if f.endswith('.md')])

def create_progress_bar(percentage: float) -> str:
    """Create a progress bar string based on percentage."""
    filled = int(percentage / 10)
    empty = 10 - filled
    return f"[{'█' * filled}{'░' * empty}] {percentage:.0f}%"

def get_category_stats() -> Dict[str, Dict]:
    """Get statistics for each category."""
    categories = {
        'Core Language': 'core_language',
        'Libraries & Frameworks': 'libraries_frameworks',
        'Development Tools': 'development_tools',
        'Community & Culture': 'community_culture',
        'Applications': 'applications'
    }
    
    base_path = "wiki_articles/articles/Python_(programming_language)"
    stats = {}
    
    for display_name, dir_name in categories.items():
        path = os.path.join(base_path, dir_name)
        article_count = count_articles_in_category(path)
        # Estimate target count for each category
        target_count = {'Core Language': 50, 'Libraries & Frameworks': 100,
                       'Development Tools': 30, 'Community & Culture': 20,
                       'Applications': 40}[display_name]
        
        progress = min(100, (article_count / target_count) * 100)
        
        stats[display_name] = {
            'count': article_count,
            'target': target_count,
            'progress': progress,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M UTC')
        }
    
    return stats

def get_recent_updates(limit: int = 3) -> List[str]:
    """Get the most recent archive updates."""
    # This would typically read from a log file or git history
    # For now, we'll return placeholder updates
    return [
        f"Updated core language articles ({datetime.now().strftime('%Y-%m-%d')})",
        f"Added new framework documentation ({datetime.now().strftime('%Y-%m-%d')})",
        f"Refreshed community articles ({datetime.now().strftime('%Y-%m-%d')})"
    ][:limit]

def update_readme(stats: Dict[str, Dict], updates: List[str]):
    """Update the README.md with current progress."""
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update progress bars
    progress_section = "Python (programming language)\n"
    total_progress = 0
    
    for category, data in stats.items():
        progress = data['progress']
        total_progress += progress
        progress_bar = create_progress_bar(progress)
        progress_section += f"{progress_bar} - {category} articles\n"
    
    overall_progress = create_progress_bar(total_progress / len(stats))
    progress_section += f"{overall_progress} - Overall progress"
    
    # Replace progress section
    pattern = r"Python \(programming language\).*?Overall progress"
    content = re.sub(pattern, progress_section, content, flags=re.DOTALL)
    
    # Update timestamps and counts
    replacements = {
        '<!-- PROGRESS_TIMESTAMP -->': datetime.now().strftime('%Y-%m-%d %H:%M UTC'),
        '<!-- TOTAL_ARTICLES -->': str(sum(d['count'] for d in stats.values())),
        '<!-- CATEGORIES_PROCESSED -->': str(len(stats)),
        '<!-- ACTIVE_CONTRIBUTORS -->': str(len(set(u.split()[0] for u in updates)))
    }
    
    # Update category details
    for category, data in stats.items():
        key_prefix = category.upper().replace(' & ', '_').replace(' ', '_')
        replacements[f'<!-- {key_prefix}_COUNT -->'] = str(data['count'])
        replacements[f'<!-- {key_prefix}_UPDATED -->'] = data['last_updated']
        replacements[f'<!-- {key_prefix}_STATUS -->'] = '✅ Complete' if data['progress'] >= 100 else '🔄 In Progress'
    
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
