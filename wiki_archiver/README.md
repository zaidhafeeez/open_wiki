# Wikipedia Article Archiver

## Project Structure

```
wiki_archiver/
├── config/
│   └── __init__.py      # Configuration settings and constants
├── core/
│   └── __init__.py      # Core archiving logic and WikiArchiver class
├── logging/
│   └── __init__.py      # Thread-safe logging mechanisms
└── utils/
    └── __init__.py      # Utility functions for file handling, retries, etc.
```

## Features

- 🌐 Wikipedia article archiving
- 🔍 Category-based article discovery
- 💾 Progress tracking and resuming
- 🚀 Parallel processing
- 📝 Markdown content generation

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python script.py [OPTIONS]

Options:
  -c, --category   Wikipedia category to archive (default: Python (programming language))
  -l, --language   Wikipedia language (default: en)
  -d, --depth      Maximum category recursion depth (default: 1)
  -o, --output     Output directory for archived articles
```

## Configuration

Modify settings in `wiki_archiver/config/__init__.py`:
- `LANGUAGE`: Wikipedia language
- `CATEGORY`: Starting category
- `MAX_DEPTH`: Category recursion depth
- `MAX_WORKERS`: Parallel processing threads

## Logging

Logs are saved to `wiki_archiver.log` with timestamps and log levels.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License
