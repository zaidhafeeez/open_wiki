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
        tuple: (dict of category statistics, dict of global statistics)
    """
    try:
        # Load existing progress data
        with open('archive_progress.json', 'r', encoding='utf-8') as f:
            progress_data = json.load(f)
        
        # Global statistics
        global_stats = progress_data.get('global_stats', {})
        
        # Add total progress calculation
        total_articles = global_stats.get('total_articles', 0)
        total_target = 0
        total_progress = 0
        
        # Process category statistics
        category_stats = {}
        for category_key, category_data in progress_data.get('category_stats', {}).items():
            # Clean up category name for display
            display_name = category_key.replace('_', ' ').replace('(programming language)', '').strip()
            
            # Ensure display name matches the README's expected names
            category_name_mapping = {
                'Articles with example Python programming language code': 'Libraries & Frameworks',
                'Articles with example Python (programming language) code': 'Development Tools',
                'Python (programming language)': 'Core Language',
                'Python (programming language) development tools': 'Development Tools',
                # Add more mappings as needed
            }
            
            display_name = category_name_mapping.get(category_key, display_name)
            
            # Prepare category statistics
            category_stats[display_name] = {
                'name': display_name,
                'count': category_data.get('count', 0),
                'total_words': category_data.get('total_words', 0),
                'total_size': category_data.get('total_size', 0),
                'has_references': category_data.get('has_references', 0),
                'has_toc': category_data.get('has_toc', 0),
                'total_lines': category_data.get('total_lines', 0),
                'progress': category_data.get('progress', 0),
                'target': category_data.get('target', 50)
            }
            
            # Calculate total progress
            target = category_data.get('target', 50)
            total_target += target
            total_progress += category_data.get('progress', 0) * target
        
        # Calculate overall progress
        global_stats['total_progress'] = total_progress / max(total_target, 1)
        
        return category_stats, global_stats
    
    except Exception as e:
        print(f"Error calculating category stats: {e}")
        return {}, {}

def update_readme_new(stats, global_stats):
    """
    Update README.md with current progress and statistics while preserving markdown structure.
    
    Args:
        stats (dict): Category-level statistics
        global_stats (dict): Overall project statistics
    """
    try:
        # Read existing README
        with open('README.md', 'r', encoding='utf-8') as f:
            readme_content = f.readlines()
        
        # Prepare updated content
        updated_content = []
        in_progress_section = False
        in_category_details = False
        continue_skipping = False  # Initialize continue_skipping here
        
        # Current timestamp
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M UTC')
        
        # Predefined category order for progress bars
        category_order = [
            'Core Language', 
            'Libraries & Frameworks', 
            'Development Tools', 
            'Community & Culture', 
            'Applications'
        ]
        
        # Unique category rows tracking
        processed_category_rows = set()
        
        for line in readme_content:
            # Update progress bars section
            if '## 📊 Archive Progress' in line:
                in_progress_section = True
                updated_content.append(line)
                continue
            
            if in_progress_section:
                # Replace progress bars
                if line.startswith('```'):
                    updated_content.append(line)
                    
                    # Add overall progress bar first
                    overall_progress = global_stats.get('total_progress', 0)
                    progress_bar = create_progress_bar(overall_progress)
                    updated_content.append(f"{progress_bar} {overall_progress*100:.1f}% - Overall progress\n")
                    
                    # Add category progress bars
                    for category in category_order:
                        cat_stats = stats.get(category, {})
                        progress = cat_stats.get('progress', 0)
                        progress_bar = create_progress_bar(progress)
                        updated_content.append(f"{progress_bar} {progress*100:.1f}% - {category}\n")
                    
                    # Skip remaining lines in this block
                    continue_skipping = True
                    continue
                
                # Skip redundant lines if we're in progress section
                if continue_skipping:
                    if line.startswith('Python') or line.startswith('[░░░░░░░░░░]'):
                        continue
                    else:
                        continue_skipping = False
                
                # Update last update and statistics
                if line.startswith('Last Update:'):
                    updated_content.append(f"Last Update: {current_time}\n")
                    continue
                
                if line.startswith('- Total Articles:'):
                    updated_content.append(f"- Total Articles: {global_stats.get('total_articles', 0)}\n")
                    continue
                
                if line.startswith('- Total Content:'):
                    total_words = global_stats.get('total_words', 0)
                    total_size = global_stats.get('total_size', 0)
                    updated_content.append(f"- Total Content: {total_words:,} words ({format_size(total_size)})\n")
                    continue
                
                if line.startswith('- Articles with References:'):
                    updated_content.append(f"- Articles with References: {global_stats.get('articles_with_refs', 0)}\n")
                    continue
                
                if line.startswith('- Average Words per Article:'):
                    avg_words = global_stats.get('total_words', 0) / max(global_stats.get('total_articles', 1), 1)
                    updated_content.append(f"- Average Words per Article: {avg_words:.1f}\n")
                    continue
                
                if line.startswith('- Categories Processed:'):
                    updated_content.append(f"- Categories Processed: {len(stats)}\n")
                    continue
                
                if line.startswith('- Active Contributors:'):
                    # This might need to be dynamically tracked or hardcoded
                    updated_content.append(line)
                    continue
            
            # Update category details table
            if '### 📈 Category Details' in line:
                in_category_details = True
                updated_content.append(line)
                continue
            
            if in_category_details:
                if line.startswith('| Category |'):
                    updated_content.append(line)
                    continue
                
                if line.startswith('|----------'):
                    updated_content.append(line)
                    continue
                
                # Update category rows
                for category in category_order + ['Community & Culture', 'Applications']:
                    if f"| {category} |" in line:
                        cat_stats = stats.get(category, {})
                        
                        # Create a unique key for this row
                        row_key = f"{category}|{cat_stats.get('count', 0)}|{cat_stats.get('total_words', 0)}|{format_size(cat_stats.get('total_size', 0))}"
                        
                        if cat_stats and row_key not in processed_category_rows:
                            updated_line = f"| {category} | {cat_stats.get('count', 0)} | {cat_stats.get('total_words', 0):,} | {format_size(cat_stats.get('total_size', 0))} | {cat_stats.get('has_references', 0)} | {cat_stats.get('total_lines', 0)} | {cat_stats.get('has_toc', 0)} | 🔄 In Progress | {current_time} |\n"
                            updated_content.append(updated_line)
                            processed_category_rows.add(row_key)
                            break
            
            # Add other lines as is, but skip duplicate progress bars and configuration section progress bars
            if not (line.startswith('[░░░░░░░░░░]') and ('Overall progress' in line or 'LANGUAGE =' in line)):
                updated_content.append(line)
        
        # Write updated README
        with open('README.md', 'w', encoding='utf-8') as f:
            f.writelines(updated_content)
        
        print("README updated successfully.")
        return True
        
    except Exception as e:
        print(f"Error updating README: {e}")
        return False

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
    readme_updated = update_readme_new(category_stats, global_stats)
    
    # Update archive progress JSON
    update_archive_progress_new(category_stats, global_stats)
    
    print("Progress tracking updated successfully.")
    
    # Return a status that can be used by GitHub Actions
    return readme_updated

# Ensure this is run when imported or executed directly
if __name__ == "__main__":
    main()
