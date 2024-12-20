"""
Test suite for Wikipedia Article Archiver
"""

import os
import pytest
import wikipedia_api as wikipediaapi

from wiki_archiver.core import WikiArchiver
from wiki_archiver.config import LANGUAGE, CATEGORY, MAX_DEPTH
from wiki_archiver.utils import get_safe_path, ensure_directory

def test_safe_path_generation():
    """Test safe path generation for file names"""
    test_cases = [
        ("Python (programming language)", "Python_programming_language"),
        ("C++ Programming", "C++_Programming"),
        ("Special Characters !@#$%^", "Special_Characters"),
    ]
    
    for input_path, expected_path in test_cases:
        assert get_safe_path(input_path) == expected_path

def test_ensure_directory():
    """Test directory creation utility"""
    test_dir = "test_temp_dir"
    ensure_directory(test_dir)
    assert os.path.exists(test_dir)
    os.rmdir(test_dir)

def test_wiki_archiver_initialization():
    """Test WikiArchiver class initialization"""
    archiver = WikiArchiver(
        language=LANGUAGE, 
        category=CATEGORY, 
        max_depth=MAX_DEPTH
    )
    
    assert archiver.language == LANGUAGE
    assert archiver.category == CATEGORY
    assert archiver.max_depth == MAX_DEPTH
    assert hasattr(archiver, 'wiki_wiki')

def test_article_metadata_extraction():
    """Test article metadata extraction"""
    archiver = WikiArchiver()
    wiki_wiki = wikipediaapi.Wikipedia(
        language=LANGUAGE,
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    
    test_page = wiki_wiki.page("Python (programming language)")
    
    metadata = archiver.get_article_metadata(test_page)
    
    assert 'title' in metadata
    assert 'url' in metadata
    assert 'summary' in metadata
    assert 'categories' in metadata
    assert metadata['title'] == "Python (programming language)"

def test_category_processing():
    """Test category processing method"""
    archiver = WikiArchiver(max_depth=1)
    
    articles, subcategories = archiver.process_category(CATEGORY)
    
    assert isinstance(articles, set)
    assert isinstance(subcategories, set)
    assert len(articles) > 0 or len(subcategories) > 0

def test_article_content_formatting():
    """Test article content formatting"""
    archiver = WikiArchiver()
    wiki_wiki = wikipediaapi.Wikipedia(
        language=LANGUAGE,
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    
    test_page = wiki_wiki.page("Python (programming language)")
    metadata = archiver.get_article_metadata(test_page)
    
    content = archiver.format_article_content(test_page, metadata)
    
    assert "---" in content  # Front matter
    assert metadata['title'] in content
    assert len(content) > 0

def test_error_handling():
    """Test error handling in article processing"""
    archiver = WikiArchiver()
    
    # Test non-existent article
    success, title = archiver.process_article("Non-Existent Article", CATEGORY, 0)
    
    assert not success
    assert title == "Non-Existent Article"

# Performance and stress tests
def test_parallel_processing():
    """Test parallel processing capabilities"""
    archiver = WikiArchiver(max_depth=1)
    
    # This will test the scrape_category method's parallel processing
    archiver.scrape_category(CATEGORY)
    
    # Check that some articles were processed
    assert len(archiver.processed_articles) > 0
