"""
Utility functions for Wikipedia Article Archiver.

Provides helper functions for file handling, path sanitization, and retries.
"""

import os
import re
import time
import unicodedata
from functools import wraps

def get_safe_path(name):
    """
    Convert a string into a safe file path.
    
    Args:
        name (str): The original file name
    
    Returns:
        str: A safe file path string
    """
    # Normalize Unicode characters
    normalized_name = unicodedata.normalize('NFKD', name)
    
    # Remove non-ASCII characters
    ascii_name = normalized_name.encode('ascii', 'ignore').decode('ascii')
    
    # Replace spaces and special characters
    safe_name = re.sub(r'[^\w\-_\.]', '_', ascii_name)
    
    # Remove consecutive underscores
    safe_name = re.sub(r'_+', '_', safe_name)
    
    # Trim leading/trailing underscores
    safe_name = safe_name.strip('_')
    
    # Limit length to prevent overly long filenames
    return safe_name[:255]

def ensure_directory(directory):
    """
    Create directory if it doesn't exist.
    
    Args:
        directory (str): Path to the directory
    """
    os.makedirs(directory, exist_ok=True)

def retry_with_backoff(func, max_retries=3, backoff_factor=2):
    """
    Retry a function with exponential backoff.
    
    Args:
        func (callable): Function to retry
        max_retries (int): Maximum number of retries
        backoff_factor (int): Factor to increase delay between retries
    
    Returns:
        callable: Decorated function with retry mechanism
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        retries = 0
        while retries < max_retries:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                retries += 1
                if retries == max_retries:
                    raise
                
                # Exponential backoff
                wait_time = backoff_factor ** retries
                time.sleep(wait_time)
        
        return None
    return wrapper
