"""
Logging module for Wikipedia Article Archiver.

Provides thread-safe logging mechanisms with different log levels.
"""

import queue
import threading
from datetime import datetime
import sys

class ThreadSafeLogger:
    def __init__(self, log_file=None):
        """
        Initialize a thread-safe logger.
        
        Args:
            log_file (str, optional): Path to log file. Defaults to None.
        """
        self._log_queue = queue.Queue()
        self._log_lock = threading.Lock()
        
    def _log(self, message, level='INFO'):
        """
        Internal method to log messages.
        
        Args:
            message (str): Log message
            level (str): Log level (INFO, WARNING, ERROR)
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_msg = f"[{timestamp}] {level}: {message}"
        
        with self._log_lock:
            # Console output only
            print(formatted_msg, file=sys.stderr)
    
    def info(self, message):
        """Log an informational message."""
        self._log(message, 'INFO')
    
    def warning(self, message):
        """Log a warning message."""
        self._log(message, 'WARNING')
    
    def error(self, message):
        """Log an error message."""
        self._log(message, 'ERROR')
    
    def close(self):
        """Close the log file handler."""
        pass

# Global logger instance
logger = ThreadSafeLogger()
