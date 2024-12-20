"""
Configuration module for Wikipedia Article Archiver.

This module manages global configuration settings and constants.
"""

import os

# Core Configuration
LANGUAGE = "en"
CATEGORIES = [
    "Python (programming language)",
    "Python programming language",
    "Python software",
    "Python programming language topics"
]
MAX_DEPTH = 1
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "wiki_articles")

# Progress Tracking
PROGRESS_FILE = "archive_progress.json"

# Performance and Rate Limiting
MAX_WORKERS = 10  # Number of parallel threads
RATE_LIMIT_DELAY = 0.1  # Delay between API calls in seconds
MAX_RETRIES = 3  # Maximum number of retries for failed API calls
BACKOFF_FACTOR = 2  # Exponential backoff factor for retries

# Error Handling
MAX_ERRORS = 50  # Maximum number of errors before stopping

# User Agent for Wikipedia API
USER_AGENT = "WikiArchiveScript/1.0 (https://github.com/zaidhafeeez/open_wiki)"

def validate_config():
    """
    Validate and potentially adjust configuration settings.
    
    Returns:
        bool: Whether the configuration is valid
    """
    # Add validation logic here
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    return True
