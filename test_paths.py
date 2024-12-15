#!/usr/bin/env python3
"""
Test suite for the path handling functionality in the Wikipedia article archiving script.
Tests various scenarios including special characters, Unicode, and edge cases.
"""

from script import get_safe_path
import unittest
from typing import List, Tuple

# Test cases with expected results
test_cases: List[Tuple[str, str]] = [
    # Basic cases
    ("Hello World", "Hello_World"),
    ("Python/Programming", "Python_Programming"),
    ("C:\\Windows\\Path", "C_Windows_Path"),
    
    # Special characters
    ("Article: Title!", "Article_Title"),
    ("Question? & Answer", "Question_Answer"),
    ("File (version 2.0)", "File_version_2.0"),
    ("Test [beta]", "Test_beta"),
    ("File{with}braces", "File_with_braces"),
    ("Path/with\\slashes", "Path_with_slashes"),
    
    # Complex cases
    ("C++ Programming", "C_Programming"),
    ("Python/C#/Java", "Python_C_Java"),
    ("Article with <tags> & {braces}", "Article_with_tags_braces"),
    ("File with: many! special@ characters#", "File_with_many_special_characters"),
    
    # Unicode and special characters
    ("Café & Restaurant", "Cafe_Restaurant"),
    ("Python – Programming", "Python-Programming"),
    ("File@Home/Test#1", "File_Home_Test_1"),
    ("Über Python", "Uber_Python"),
    ("Python—Advanced—Guide", "Python-Advanced-Guide"),
    ("Python'Quote'Test", "Python_Quote_Test"),
    
    # Edge cases
    ("", "unnamed"),
    ("   ", "unnamed"),
    ("___test___", "test"),
    ("Multiple___underscores", "Multiple_underscores"),
    (".", "unnamed"),
    ("a" * 300, "a" * 252 + "..."),  # Very long filename
    
    # Real-world examples from Wikipedia
    ("Category:Python (programming language)", "Category_Python_programming_language"),
    ("Python/Libraries & Frameworks", "Python_Libraries_Frameworks"),
    ("Article: How to use C++ in Python?", "Article_How_to_use_C_in_Python"),
    ("Python – The Programming Language", "Python-The_Programming_Language"),
    ("Python/C++/Integration", "Python_C_Integration"),
    
    # Smart quotes and special dashes
    ("Python's Guide", "Python_s_Guide"),
    ('Python\'s "Advanced" Guide', "Python_s_Advanced_Guide"),
    ("Python—A Guide", "Python-A_Guide"),
    
    # Mixed cases
    ("UPPER_lower_Mixed", "UPPER_lower_Mixed"),
    ("Mixed Case File.txt", "Mixed_Case_File.txt"),
    ("  Spaces  Everywhere  ", "Spaces_Everywhere"),
    
    # Numbers and special characters
    ("Version 1.0.0-beta.1", "Version_1.0.0-beta.1"),
    ("File (2023)", "File_2023"),
    ("Test v2.0 [Beta]", "Test_v2.0_Beta"),
]

class TestPathHandling(unittest.TestCase):
    """Test cases for the get_safe_path function"""
    
    def test_basic_path_conversion(self):
        """Test basic path conversion functionality"""
        for input_path, expected in test_cases:
            with self.subTest(input_path=input_path):
                result = get_safe_path(input_path)
                self.assertEqual(result, expected)
    
    def test_idempotency(self):
        """Test that running get_safe_path multiple times produces the same result"""
        for input_path, _ in test_cases:
            with self.subTest(input_path=input_path):
                first_pass = get_safe_path(input_path)
                second_pass = get_safe_path(first_pass)
                self.assertEqual(first_pass, second_pass)
    
    def test_non_string_input(self):
        """Test handling of non-string inputs"""
        test_inputs = [
            (123, "123"),
            (3.14, "3.14"),
            (None, "None"),
            ([], "[]"),
            ({}, "{}"),
        ]
        for input_val, expected in test_inputs:
            with self.subTest(input_val=input_val):
                result = get_safe_path(input_val)
                self.assertTrue(isinstance(result, str))
                self.assertEqual(result, expected)
    
    def test_length_limits(self):
        """Test that very long paths are truncated appropriately"""
        very_long_input = "a" * 1000
        result = get_safe_path(very_long_input)
        self.assertLessEqual(len(result), 255)
        self.assertTrue(result.endswith("..."))
    
    def test_special_cases(self):
        """Test special edge cases"""
        special_cases = [
            (" ", "unnamed"),
            (".", "unnamed"),
            ("__", "unnamed"),
            ("___", "unnamed"),
            ("...", "unnamed"),
        ]
        for input_path, expected in special_cases:
            with self.subTest(input_path=input_path):
                result = get_safe_path(input_path)
                self.assertEqual(result, expected)

def run_visual_tests():
    """Run visual tests with formatted output"""
    print("Running path safety tests...\n")
    passed = 0
    failed = 0
    
    for input_path, expected in test_cases:
        result = get_safe_path(input_path)
        status = "PASS" if result == expected else "FAIL"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"[{status}] Input: {input_path}")
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")
        print()
    
    total = passed + failed
    print(f"Results: {passed}/{total} tests passed ({(passed/total)*100:.1f}%)")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

if __name__ == "__main__":
    print("Running unit tests...\n")
    unittest.main(verbosity=2, exit=False)
    print("\nRunning visual tests...\n")
    run_visual_tests()
