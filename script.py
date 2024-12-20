#!/usr/bin/env python3
"""
Main script for Wikipedia Article Archiver.

This script archives Wikipedia articles from specified categories.
"""

import sys
import os
import argparse
from datetime import datetime

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from wiki_archiver.config import *
from wiki_archiver.core import WikiArchiver
from wiki_archiver.logging import logger

def parse_arguments():
    """
    Parse command-line arguments.
    
    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(description="Wikipedia Article Archiver")
    parser.add_argument(
        "-c", "--categories", 
        nargs='+',  # Allow multiple categories
        default=CATEGORIES, 
        help="Wikipedia categories to archive (space-separated)"
    )
    parser.add_argument(
        "-l", "--language", 
        default=LANGUAGE, 
        help="Wikipedia language"
    )
    parser.add_argument(
        "-d", "--depth", 
        type=int, 
        default=MAX_DEPTH, 
        help="Maximum category recursion depth"
    )
    parser.add_argument(
        "-o", "--output", 
        default=OUTPUT_DIR, 
        help="Output directory for archived articles"
    )
    
    return parser.parse_args()

def main():
    """
    Main function to orchestrate Wikipedia article archiving.
    """
    try:
        # Parse arguments
        args = parse_arguments()
        
        # Validate configuration
        from wiki_archiver.config import validate_config
        if not validate_config():
            logger.error("Invalid configuration. Exiting.")
            sys.exit(1)
        
        # Initialize archiver
        archiver = WikiArchiver(
            language=args.language, 
            categories=args.categories, 
            max_depth=args.depth
        )
        
        # Load previous progress
        previous_progress = archiver.load_progress()
        logger.info(f"Loaded previous progress: {previous_progress}")
        
        # Start archiving
        start_time = datetime.now()
        logger.info(f"Starting archive for categories: {args.categories}")
        
        archiver.scrape_categories()  # Use new method for multiple categories
        
        # Save progress
        archiver.save_progress()
        
        # Log completion
        end_time = datetime.now()
        duration = end_time - start_time
        logger.info(f"Archiving completed in {duration}")
        
    except KeyboardInterrupt:
        logger.warning("Archiving interrupted by user.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)
    finally:
        # Cleanup and final logging
        logger.info("Wikipedia Article Archiver finished.")

if __name__ == "__main__":
    main()
