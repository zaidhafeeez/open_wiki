from script import get_safe_path

# Test cases with expected results
test_cases = [
    # Basic cases
    ("Hello World", "Hello_World"),
    ("Python/Programming", "Python_Programming"),
    ("C:\\Windows\\Path", "C_Windows_Path"),
    
    # Special characters
    ("Article: Title!", "Article_Title"),
    ("Question? & Answer", "Question_Answer"),
    ("File (version 2.0)", "File_version_2.0"),
    ("Test [beta]", "Test_beta"),
    
    # Complex cases
    ("C++ Programming", "C_Programming"),
    ("Python/C#/Java", "Python_C_Java"),
    ("Article with <tags> & {braces}", "Article_with_tags_braces"),
    
    # Unicode and special characters
    ("Café & Restaurant", "Cafe_Restaurant"),
    ("Python – Programming", "Python_Programming"),
    ("File@Home/Test#1", "File_Home_Test_1"),
    
    # Edge cases
    ("", "unnamed"),
    ("   ", "unnamed"),
    ("___test___", "test"),
    ("Multiple___underscores", "Multiple_underscores"),
    
    # Real-world examples
    ("Category:Python (programming language)", "Category_Python_programming_language"),
    ("Python/Libraries & Frameworks", "Python_Libraries_Frameworks"),
    ("Article: How to use C++ in Python?", "Article_How_to_use_C_in_Python"),
]

def run_tests():
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
    run_tests()
