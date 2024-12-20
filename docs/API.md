# Wikipedia Article Archiver API

## Overview

The Wikipedia Article Archiver provides a flexible programmatic API for archiving Wikipedia articles. This document explains how to use the API for various archiving tasks.

## Installation

Ensure you have the Wikipedia Article Archiver installed in your Python environment.

## Basic Usage

### Quick Archiving

```python
from wiki_archiver.api import archive_wikipedia, WikiArchiveAPI

# Quick archiving of default categories
results = archive_wikipedia()

# More detailed archiving with specific parameters
api = WikiArchiveAPI(language='en', max_depth=2)
results = api.archive_categories(
    categories=['Python (programming language)', 'Machine Learning']
)
```

## Advanced API Methods

### Retrieving Progress and Archived Articles

```python
# Get current archiving progress
progress = api.get_archive_progress()

# List archived articles
archived_articles = api.list_archived_articles(
    category='Python (programming language)'
)
```

## API Methods Overview

### `archive_wikipedia()`
- Quick archiving function
- Parameters:
  - `categories`: List of categories to archive (optional)
  - `language`: Wikipedia language (default: 'en')
  - `max_depth`: Maximum category recursion depth (default: 1)

### `WikiArchiveAPI` Class

#### Constructor
```python
WikiArchiveAPI(
    language='en', 
    categories=None, 
    max_depth=1,
    output_dir=OUTPUT_DIR
)
```

#### Methods
- `archive_categories()`: Archive articles from specified categories
- `get_archive_progress()`: Retrieve current archiving progress
- `list_archived_articles()`: List archived article files

## Configuration Options

- `language`: Wikipedia language (default: 'en')
- `categories`: List of categories to archive
- `max_depth`: Maximum category recursion depth
- `output_dir`: Custom output directory for archived articles

## Error Handling

The API includes basic error handling:
- Logging of warnings and errors
- Graceful handling of missing progress files
- Validation of input parameters

## Best Practices

- Always specify a reasonable `max_depth` to prevent excessive recursion
- Use specific categories for more focused archiving
- Check the returned results for processed articles

## Examples

### Archiving Multiple Categories

```python
api = WikiArchiveAPI(max_depth=2)
results = api.archive_categories([
    'Machine Learning',
    'Artificial Intelligence',
    'Data Science'
])
```

### Custom Language and Output Directory

```python
api = WikiArchiveAPI(
    language='es',  # Spanish Wikipedia
    output_dir='/path/to/custom/archive'
)
results = api.archive_categories()
```

## Troubleshooting

- Ensure you have the required dependencies installed
- Check network connectivity
- Verify Wikipedia API access
- Review logs for detailed error information

## Contributing

Contributions to improve the API are welcome. Please submit issues or pull requests to the project repository.
