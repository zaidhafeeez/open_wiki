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
        self._log_file = log_file
        self._file_handler = None
        
        if log_file:
            try:
                self._file_handler = open(log_file, 'a', encoding='utf-8')
            except IOError as e:
                self.error(f"Could not open log file: {e}")
    
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
            # Console output
            print(formatted_msg, file=sys.stderr)
            
            # File logging if file handler exists
            if self._file_handler:
                try:
                    print(formatted_msg, file=self._file_handler)
                    self._file_handler.flush()
                except Exception as e:
                    print(f"Error writing to log file: {e}", file=sys.stderr)
    
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
        if self._file_handler:
            self._file_handler.close()

# Global logger instance
logger = ThreadSafeLogger(log_file='wiki_archiver.log')
