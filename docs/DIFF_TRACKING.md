# Article Diff Tracking

## Overview

The Wikipedia Article Archiver provides a comprehensive article diff tracking mechanism to help you understand how Wikipedia articles change over time.

## Features

- Track changes between different versions of Wikipedia articles
- Save article versions for historical comparison
- Generate detailed change reports
- Support for multiple languages

## Installation

Ensure you have the Wikipedia Article Archiver installed in your Python environment.

## Basic Usage

### Track Changes for a Single Article

```python
from wiki_archiver.diff_tracker import track_wikipedia_article_changes

# Track changes for a specific article
diff_info = track_wikipedia_article_changes('Python (programming language)')

# Detailed change information
print(diff_info['changes'])
print(diff_info['change_summary'])
```

## Advanced Usage

### Using ArticleDiffTracker Class

```python
from wiki_archiver.diff_tracker import ArticleDiffTracker

# Create a diff tracker
tracker = ArticleDiffTracker(language='en')

# Get article history
history = tracker.get_article_history('Machine Learning')

# Track changes between versions
diff_result = tracker.track_article_changes(
    'Machine Learning', 
    previous_version_path=history[-1]  # Optional: compare with last saved version
)
```

## Configuration Options

- `language`: Wikipedia language (default: 'en')
- `output_dir`: Custom directory for storing article versions

## Change Tracking Details

The diff tracking provides:
- Current article version path
- Previous article version path (if available)
- Detailed line-by-line changes
- Summary of added and removed lines

## Best Practices

- Regularly track article changes to monitor Wikipedia updates
- Use language-specific tracking for non-English Wikipedia
- Store and analyze diff information for research or monitoring

## Troubleshooting

- Ensure network connectivity
- Check Wikipedia API access
- Verify sufficient disk space for storing article versions

## Contributing

Contributions to improve diff tracking are welcome. Please submit issues or pull requests to the project repository.
