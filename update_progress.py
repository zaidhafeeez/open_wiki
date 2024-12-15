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
import glob

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
    updates_file = "archive_progress.json"
    
    if os.path.exists(updates_file):
        try:
            with open(updates_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                updates = data.get('recent_updates', [])
                if updates:
                    return updates[:limit]
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    
    # Fallback to default updates
    return [
        f"Updated core language articles ({datetime.now().strftime('%Y-%m-%d')})",
        f"Added new framework documentation ({datetime.now().strftime('%Y-%m-%d')})",
        f"Refreshed community articles ({datetime.now().strftime('%Y-%m-%d')})"
    ][:limit]

def save_progress_data(stats: Dict[str, Dict], updates: List[str]):
    """Save progress data to archive_progress.json."""
    progress_file = "archive_progress.json"
    
    # Load existing data if available
    try:
        with open(progress_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {'processed': [], 'last_category': None}
    
    # Update with new statistics
    data.update({
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M UTC'),
        'category_stats': {
            category: {
                'count': info['count'],
                'target': info['target'],
                'progress': info['progress'],
                'last_updated': info['last_updated'],
                'detailed_stats': info['detailed_stats']
            }
            for category, info in stats.items()
        },
        'recent_updates': updates,
        'total_articles': sum(info['count'] for info in stats.values()),
        'total_words': sum(info['detailed_stats'].get('total_words', 0) for info in stats.values()),
        'total_size': sum(info['detailed_stats'].get('total_size', 0) for info in stats.values()),
        'articles_with_refs': sum(info['detailed_stats'].get('has_references', 0) for info in stats.values())
    })
    
    # Save updated data
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def load_progress_data() -> Dict:
    """Load progress data from archive_progress.json."""
    progress_file = "archive_progress.json"
    try:
        with open(progress_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'processed': [], 'last_category': None}

def update_recent_updates(category: str, article_count: int) -> List[str]:
    """Create a new update entry and return recent updates."""
    current_date = datetime.now().strftime('%Y-%m-%d')
    new_update = f"Added {article_count} articles to {category} ({current_date})"
    
    data = load_progress_data()
    updates = data.get('recent_updates', [])
    
    # Add new update at the beginning
    updates.insert(0, new_update)
    
    # Keep only the last 10 updates
    updates = updates[:10]
    
    # Save back to file
    data['recent_updates'] = updates
    with open('archive_progress.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    return updates[:3]  # Return only the 3 most recent updates

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

def get_category_stats_new():
    """
    Calculate comprehensive statistics for all categories.
    
    Returns:
        dict: Detailed statistics for each category
    """
    categories = {}
    total_articles = 0
    total_words = 0
    total_size = 0
    articles_with_refs = 0
    articles_with_toc = 0

    # Walk through all article directories
    for category_dir in glob.glob('wiki_articles/articles_*'):
        category_name = os.path.basename(category_dir).replace('articles_', '')
        
        # Initialize category stats
        categories[category_name] = {
            'count': 0,
            'total_words': 0,
            'total_size': 0,
            'has_references': 0,
            'has_toc': 0,
            'total_lines': 0,
            'target': 50,  # Default target, can be adjusted
            'progress': 0.0,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M UTC')
        }
        
        # Collect article-level stats
        for article_file in glob.glob(os.path.join(category_dir, '*.md')):
            try:
                with open(article_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Update category stats
                    cat_stats = categories[category_name]
                    cat_stats['count'] += 1
                    cat_stats['total_words'] += len(content.split())
                    cat_stats['total_size'] += len(content.encode('utf-8'))
                    cat_stats['has_references'] += 1 if '## References' in content else 0
                    cat_stats['has_toc'] += 1 if '## Table of Contents' in content else 0
                    cat_stats['total_lines'] += len(content.splitlines())
            except Exception as e:
                print(f"Error processing {article_file}: {e}")
        
        # Calculate progress
        cat_stats = categories[category_name]
        cat_stats['progress'] = min(1.0, cat_stats['count'] / cat_stats['target'])
        
        # Aggregate global stats
        total_articles += cat_stats['count']
        total_words += cat_stats['total_words']
        total_size += cat_stats['total_size']
        articles_with_refs += cat_stats['has_references']
        articles_with_toc += cat_stats['has_toc']

    return categories, {
        'total_articles': total_articles,
        'total_words': total_words,
        'total_size': total_size,
        'articles_with_refs': articles_with_refs,
        'articles_with_toc': articles_with_toc
    }

def update_readme_new(stats, global_stats):
    """
    Update README.md with current progress and statistics.
    
    Args:
        stats (dict): Category-level statistics
        global_stats (dict): Overall project statistics
    """
    try:
        # Read existing README
        with open('README.md', 'r', encoding='utf-8') as f:
            readme_content = f.readlines()
        
        # Find and update progress sections
        updated_content = []
        in_progress_section = False
        in_category_section = False
        
        for line in readme_content:
            # Check for progress section
            if '## Project Progress' in line:
                in_progress_section = True
                updated_content.append(line)
                
                # Add global progress details
                updated_content.append(f"\n### Overall Statistics\n")
                updated_content.append(f"- **Total Articles:** {global_stats['total_articles']}\n")
                updated_content.append(f"- **Total Words:** {global_stats['total_words']:,}\n")
                updated_content.append(f"- **Total Size:** {global_stats['total_size']:,} bytes\n")
                updated_content.append(f"- **Articles with References:** {global_stats['articles_with_refs']}\n")
                updated_content.append(f"- **Articles with Table of Contents:** {global_stats['articles_with_toc']}\n")
                continue
            
            # Check for category details section
            if '## Category Details' in line:
                in_category_section = True
                updated_content.append(line)
                
                # Add detailed category information
                for category, details in stats.items():
                    updated_content.append(f"\n### {category}\n")
                    updated_content.append(f"- **Articles:** {details['count']}\n")
                    updated_content.append(f"- **Progress:** {details['progress']*100:.2f}%\n")
                    updated_content.append(f"- **Total Words:** {details['total_words']:,}\n")
                    updated_content.append(f"- **Total Size:** {details['total_size']:,} bytes\n")
                    updated_content.append(f"- **Articles with References:** {details['has_references']}\n")
                    updated_content.append(f"- **Articles with ToC:** {details['has_toc']}\n")
                continue
            
            # Skip existing progress and category details
            if in_progress_section and '##' in line:
                in_progress_section = False
            if in_category_section and '##' in line:
                in_category_section = False
            
            # Add non-progress lines
            if not in_progress_section and not in_category_section:
                updated_content.append(line)
        
        # Write updated README
        with open('README.md', 'w', encoding='utf-8') as f:
            f.writelines(updated_content)
        
    except Exception as e:
        print(f"Error updating README: {e}")

def update_archive_progress_new(stats, global_stats):
    """
    Update archive_progress.json with current statistics.
    
    Args:
        stats (dict): Category-level statistics
        global_stats (dict): Overall project statistics
    """
    try:
        progress_data = {
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M UTC'),
            'global_stats': global_stats,
            'category_stats': stats
        }
        
        with open('archive_progress.json', 'w', encoding='utf-8') as f:
            json.dump(progress_data, f, indent=2)
        
    except Exception as e:
        print(f"Error updating archive_progress.json: {e}")

def main():
    """
    Main function to update progress tracking.
    """
    # Get category and global statistics
    category_stats, global_stats = get_category_stats_new()
    
    # Update README
    update_readme_new(category_stats, global_stats)
    
    # Update archive progress JSON
    update_archive_progress_new(category_stats, global_stats)
    
    print("Progress tracking updated successfully.")

if __name__ == "__main__":
    main()
