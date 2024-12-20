#!/usr/bin/env python3
"""
Demonstration script for Wikipedia Article Diff Tracking.

This script showcases the capabilities of the ArticleDiffTracker 
in tracking changes in Wikipedia articles.
"""

import os
import sys
import time

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wiki_archiver.diff_tracker import ArticleDiffTracker, track_wikipedia_article_changes

def main():
    # Demonstrate different tracking scenarios
    print("Wikipedia Article Diff Tracking Demonstration")
    print("=" * 50)

    # Articles to track
    articles = [
        'Python (programming language)', 
        'Machine Learning', 
        'Artificial Intelligence'
    ]

    # Create diff tracker
    tracker = ArticleDiffTracker()

    for article in articles:
        print(f"\nTracking Article: {article}")
        print("-" * 30)

        # Get previous versions if they exist
        history = tracker.get_article_history(article)
        
        # Track changes
        if history:
            print(f"Previous versions found: {len(history)}")
            previous_version = history[-1]  # Use the most recent previous version
            
            diff_result = tracker.track_article_changes(article, previous_version)
            
            # Display change summary
            print("\nChange Summary:")
            if 'change_summary' in diff_result:
                added = diff_result['change_summary']['added_lines']
                removed = diff_result['change_summary']['removed_lines']
                print(f"  Lines Added: {added}")
                print(f"  Lines Removed: {removed}")
            else:
                print("  No significant changes detected.")
        else:
            print("No previous versions found. Creating initial version.")
            diff_result = tracker.track_article_changes(article)
        
        # Display version paths
        print("\nVersion Paths:")
        print(f"  Current Version: {diff_result.get('current_version', 'N/A')}")
        print(f"  Previous Version: {diff_result.get('previous_version', 'N/A')}")
        
        # Optional: Display detailed changes (limited to first 10 for brevity)
        if diff_result.get('changes'):
            print("\nDetailed Changes (first 10 lines):")
            for change in diff_result['changes'][:10]:
                print(change)

    # Convenience function demonstration
    print("\nConvenience Function Demonstration")
    print("-" * 30)
    
    try:
        quick_diff = track_wikipedia_article_changes('Deep Learning')
        print("Quick Diff Result:")
        print(f"  Added Lines: {quick_diff.get('change_summary', {}).get('added_lines', 'N/A')}")
        print(f"  Removed Lines: {quick_diff.get('change_summary', {}).get('removed_lines', 'N/A')}")
    except Exception as e:
        print(f"Error in quick diff tracking: {e}")

if __name__ == "__main__":
    main()
