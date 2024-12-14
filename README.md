# Wikipedia Article Archive Script

A Python script that automatically archives Wikipedia articles related to Python programming language, maintaining a structured and searchable knowledge base.

## Features

- **Automated Article Archiving**: Daily updates via GitHub Actions
- **Parallel Processing**: Fast article retrieval with multi-threading
- **Smart Caching**: Caches dependencies and progress for faster runs
- **Rich Metadata**: Includes categories, links, references, and more
- **Markdown Format**: Articles stored in clean, readable Markdown
- **Progress Tracking**: Resumes from last state if interrupted
- **Category Support**: Archives main category and subcategories

## Directory Structure

```
wiki_articles/
├── articles/
│   └── Python_(programming_language)/
│       ├── README.md              # Category overview
│       ├── Python.md             # Main Python article
│       ├── Python_syntax.md      # Python syntax article
│       └── ...                   # Other related articles
└── ...
```

## Article Format

Each archived article includes:
- Article metadata (last updated, URL, language, page ID)
- Summary
- Categories
- Table of contents
- Main content
- Related articles
- References

## Quick Navigation

To find specific articles:
1. Browse the `wiki_articles/articles` directory
2. Each category has its own subdirectory with a README
3. Articles are named using underscores (e.g., `Python_syntax.md`)
4. Use GitHub's search to find specific topics

## Setup and Usage

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Locally**:
   ```bash
   python script.py
   ```

3. **GitHub Actions** (automatic):
   - Runs daily at midnight UTC
   - Caches dependencies and progress
   - Updates articles automatically
   - Commits changes to repository

## Configuration

Edit these variables in `script.py`:
```python
LANGUAGE = "en"                        # Article language
CATEGORY = "Python (programming language)"  # Main category
MAX_DEPTH = 1                         # Category depth
MAX_WORKERS = 10                      # Parallel threads
```

## Performance Features

- **Parallel Processing**: Uses ThreadPoolExecutor for concurrent downloads
- **Progress Caching**: Saves and resumes from last state
- **Rate Limiting**: Smart API request management
- **Efficient Storage**: Deduplicates articles across categories
- **GitHub Actions Optimization**: Caches dependencies and article data

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Future Plans

- [ ] Support for additional programming language categories
- [ ] Full-text search capabilities
- [ ] Article diff tracking
- [ ] Custom category configuration
- [ ] API for programmatic access

## License

This project is licensed under the MIT License - see the LICENSE file for details.
