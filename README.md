# Wiki Archive Script

A Python script that archives Wikipedia articles related to Python programming language, organizing them into category-based directories with enhanced metadata and formatting.

## Features

- **Category-Based Organization**: Articles are organized into directories based on their categories
- **Rich Metadata**: Each article includes:
  - Last updated timestamp
  - Original article link
  - Language and Page ID
  - Categories and sections
  - Related articles and references
  - Disambiguation information
- **Parallel Processing**: Uses multi-threading for faster article processing
- **Progress Tracking**: Saves progress and can resume from where it left off
- **GitHub Integration**: Automated workflow for daily updates
- **Local Storage**: Saves articles locally for review before committing

## Requirements

```
wikipediaapi
tqdm
python-dotenv
```

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd wiki-archive-script
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the script:
```bash
python script.py
```

## Directory Structure

```
wiki_articles/
├── articles/
│   ├── Python_(programming_language)/
│   │   ├── README.md
│   │   ├── Python_syntax_and_semantics.md
│   │   ├── Python_Software_Foundation.md
│   │   └── ...
│   └── Articles_with_example_Python_(programming_language)_code/
│       ├── README.md
│       └── ...
```

## Article Format

Each article is saved as a Markdown file with the following sections:

1. **Article Metadata**
   - Last Updated timestamp
   - Original article link
   - Language and Page ID
   - Disambiguation status (if applicable)

2. **Summary**
   - Brief overview of the article

3. **Categories**
   - List of Wikipedia categories

4. **Table of Contents**
   - Hierarchical structure of article sections

5. **Content**
   - Full article text

6. **Related Articles**
   - Links to related Wikipedia articles

7. **References**
   - Citations and external links

## Configuration

The script can be configured by modifying these variables in `script.py`:

- `LANGUAGE`: Wikipedia language code (default: "en")
- `CATEGORY`: Root category to archive (default: "Python (programming language)")
- `MAX_DEPTH`: Maximum depth for subcategory traversal (default: 1)
- `MAX_WORKERS`: Number of concurrent article processing threads (default: 3)

## GitHub Actions Workflow

The repository includes a GitHub Actions workflow that:
1. Runs daily at midnight UTC
2. Updates all articles with the latest content
3. Commits changes only if articles were updated
4. Can be manually triggered through the Actions tab

## Progress Tracking

- Progress is saved in `archive_progress.json`
- Tracks processed articles and last processed category
- Automatically resumes from last position if interrupted
- Cleans up progress file after successful completion

## Error Handling

- Graceful handling of network issues
- Thread-safe operations
- Progress saving on interruption
- Detailed error logging

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the MIT License.
