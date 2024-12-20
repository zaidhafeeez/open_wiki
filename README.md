# 📚 Wikipedia Article Archiver

A Python script that automatically archives Wikipedia articles related to Python programming language, maintaining a structured and searchable knowledge base. 🐍

## 🌟 Project Structure

```
open_wiki/
├── script.py             # Main entry point for archiving
├── wiki_archiver/        # Modular package
│   ├── config/           # Configuration settings
│   ├── core/             # Core archiving logic
│   ├── logging/          # Thread-safe logging
│   └── utils/            # Utility functions
├── wiki_articles/        # Archived article storage
└── requirements.txt      # Project dependencies
```

## ✨ Features

- 🌐 Wikipedia article archiving
- 🔍 Category-based article discovery
- 💾 Progress tracking and resuming
- 🚀 Parallel processing
- 📝 Markdown content generation

## 🚀 Setup and Usage

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Locally**:
   ```bash
   python script.py [OPTIONS]
   ```

   Options:
   - `-c, --category`: Wikipedia category to archive (default: Python (programming language))
   - `-l, --language`: Wikipedia language (default: en)
   - `-d, --depth`: Maximum category recursion depth (default: 1)
   - `-o, --output`: Output directory for archived articles

3. **GitHub Actions** (automatic):
   - ⏰ Runs daily at midnight UTC
   - 💾 Caches dependencies and progress
   - 🔄 Updates articles automatically
   - 📤 Commits changes to repository

## ⚙️ Configuration

Edit these variables in `wiki_archiver/config/__init__.py`:
```python
LANGUAGE = "en"                        # Article language
CATEGORY = "Python (programming language)"  # Main category
MAX_DEPTH = 1                          # Category depth
MAX_WORKERS = 10                       # Parallel threads
```

## 🚄 Performance Features

- ⚡ **Parallel Processing**: Uses ThreadPoolExecutor for concurrent downloads
- 💾 **Progress Caching**: Saves and resumes from last state
- 🔄 **Rate Limiting**: Smart API request management
- 📦 **Efficient Storage**: Deduplicates articles across categories
- ⚡ **GitHub Actions Optimization**: Caches dependencies and article data

## 📊 Archive Progress

Current archiving progress by category:

```
[░░░░░░░░░░] 1% 61.0% - Overall progress
[░░░░░░░░░░] 0% 0.0% - Core Language
[░░░░░░░░░░] 1% 100.0% - Libraries & Frameworks
[░░░░░░░░░░] 0% 0.0% - Development Tools
[░░░░░░░░░░] 0% 0.0% - Community & Culture
[░░░░░░░░░░] 0% 0.0% - Applications
```

## 🤝 Contributing

1. 🔱 Fork the repository
2. 🌿 Create your feature branch
3. 💾 Commit your changes
4. 🚀 Push to the branch
5. 📬 Create a Pull Request

## 🔮 Future Plans

- [ ] 📚 Support for additional programming language categories
- [ ] 🔍 Full-text search capabilities
- [x] 📊 Article diff tracking
- [ ] ⚙️ Custom category configuration
- [x] 🔌 API for programmatic access

## Project Roadmap

Check out our [TODO list](TODO.md) for upcoming features, improvements, and project goals. We welcome contributions and suggestions!

## Article Diff Tracking

Track changes in Wikipedia articles over time with our built-in diff tracking feature. 

Quick example:

```python
from wiki_archiver.diff_tracker import track_wikipedia_article_changes

# Track changes for a specific article
diff_info = track_wikipedia_article_changes('Python (programming language)')
print(diff_info['change_summary'])
```

For detailed documentation, see the [Diff Tracking Guide](docs/DIFF_TRACKING.md).

## Programmatic Access

For detailed information about programmatically using the Wikipedia Article Archiver, please refer to the [API Documentation](docs/API.md).

Quick example:

```python
from wiki_archiver.api import archive_wikipedia

# Archive Wikipedia articles
results = archive_wikipedia(
    categories=['Python (programming language)']
)
```

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🐛 Troubleshooting

- Ensure you have the latest version of Python
- Check network connectivity
- Verify API rate limits
- Review logs in `wiki_archiver.log`

## 📞 Contact

For issues or suggestions, please [open an issue](https://github.com/zaidhafeeez/open_wiki/issues) on GitHub.
