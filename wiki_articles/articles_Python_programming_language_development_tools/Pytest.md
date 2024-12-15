# Pytest

## Metadata
- **Last Updated:** 2024-12-06 06:18:25 UTC
- **Original Article:** [Pytest](https://en.wikipedia.org/wiki/Pytest)
- **Language:** en
- **Page ID:** 69852359

## Summary
Pytest is a Python testing framework that originated from the PyPy project. It can be used to write various types of software tests, including unit tests, integration tests, end-to-end tests, and functional tests. Its features include parametrized testing, fixtures, and assert re-writing.
Pytest fixtures provide the contexts for tests by passing in parameter names in test cases; its parametrization eliminates duplicate code for testing multiple sets of input and output; and its rewritten assert statements provide detailed output for causes of failures.

## Categories
This article belongs to the following categories:

- Category:Articles with short description
- Category:Free software testing tools
- Category:Good articles
- Category:Python (programming language) development tools
- Category:Short description is different from Wikidata
- Category:Unit testing frameworks

## Table of Contents

- History
- Features
- See also
- References
- External links

## Content

Pytest is a Python testing framework that originated from the PyPy project. It can be used to write various types of software tests, including unit tests, integration tests, end-to-end tests, and functional tests. Its features include parametrized testing, fixtures, and assert re-writing.
Pytest fixtures provide the contexts for tests by passing in parameter names in test cases; its parametrization eliminates duplicate code for testing multiple sets of input and output; and its rewritten assert statements provide detailed output for causes of failures.

History
Pytest was developed as part of an effort by third-party packages to address Python's built-in module unittest's shortcomings. It originated as part of PyPy, an alternative implementation of Python to the standard CPython. Since its creation in early 2003, PyPy has had a heavy emphasis on testing. PyPy had unit tests for newly written code, regression tests for bugs, and integration tests using CPython's test suite.
In mid 2004, a testing framework called utest emerged and contributors to PyPy began converting existing test cases to utest. Meanwhile, at EuroPython 2004 a complementary standard library for testing, named std, was invented. This package laid out the principles, such as assert rewriting, of what would later become pytest. In late 2004, the std project was renamed to py, std.utest became py.test, and the py library was separated from PyPy. In November 2010, pytest 2.0.0 was released as a package separate from py. It was still called py.test until August 2016, but following the release of pytest 3.0.0 the recommended command line entry point became pytest.
Pytest has been classified by developer security platform Snyk as one of the key ecosystem projects in Python due to its popularity. Some well-known projects who switched to pytest from unittest and nose (another testing package) include those of Mozilla and Dropbox.

Features
Parametrized testing
It is a common pattern in software testing to send values through test functions and check for correct output. In many cases, in order to thoroughly test functionalities, one needs to test multiple sets of input/output, and writing such cases separately would cause duplicate code as most of the actions would remain the same, only differing in input/output values. Pytest's parametrized testing feature eliminates such duplicate code by combining different iterations into one test case, then running these iterations and displaying each test's result separately.
Parametrized tests in pytest are marked by the @pytest.mark.parametrize(argnames, argvalues) decorator, where the first parameter, argnames, is a string of comma-separated names, and argvalues is a list of values to pass into argnames. When there are multiple names in argnames, argvalues would be a list of tuples where values in each tuple corresponds to the names in argnames by index. The names in argnames are then passed into the test function marked by the decorator as parameters. When pytest runs such decorated tests, each pair of argnames and argvalues would constitute a separate run with its own test output and unique identifier. The identifier can then be used to run individual data pairs.: 52–58

Assert rewriting
When writing software tests, the assert statement is a primary means for communicating test failure, where expected values are compared to actual values.: 32–34  While Python's built-in assert keyword would only raise AssertionError with no details in cases of failure, pytest rewrites Python's assert keyword and provides detailed output for the causes of failures, such as what expressions in the assert statement evaluate to. A comparison can be made with unittest (Python's built-in module for testing)'s assert statements:: 32 

unittest adheres to a more verbose syntax because it is inspired by the Java programming language's JUnit, as are most unit testing libraries; pytest achieves the same while intercepting Python's built-in assert calls, making the approach more concise.: 32

Pytest fixtures
Pytest's tests verify that computer code performs as expected using tests that are structured in an arrange, act and assert sequence known as AAA. Its fixtures provide the context for tests. They can be used to put a system into a known state and to pass data into test functions. Fixtures practically constitute the arrange phase in the anatomy of a test (AAA, short for arrange, act, assert). Pytest fixtures can run before test cases as setup or after test cases for clean up, but are different from unittest and nose (another third-party Python testing framework)'s setups and teardowns. Functions declared as pytest fixtures are marked by the @pytest.fixture decorator, whose names can then be passed into test functions as parameters. When pytest finds the fixtures' names in test functions' parameters, it first searches in the same module for such fixtures, and if not found, it searches for such fixtures in the conftest.py file.: 61 
For example:

In the above example, pytest fixture dataset returns a dictionary, which is then passed into test function test_dataset for assertion. In addition to fixture detection within the same file as test cases, pytest fixtures can also be placed in the conftest.py file in the tests directory. There can be multiple conftest.py files, each placed within a tests directory for fixtures to be detected for each subset of tests.: 63

Fixture scopes
In pytest, fixture scopes let the user define when a fixture should be called. There are four fixture scopes: function scope, class scope, module scope, and session scope. Function-scoped fixtures are default for all pytest fixtures, which are called every time a function having the fixture as a parameter runs.  The goal of specifying a broader fixture scope is to eliminate repeated fixture calls, which could slow down test execution. Class-scoped fixtures are called once per test class, regardless of the number of times they are called, and the same logic goes for all other scopes. When changing fixture scope, one need only add the scope parameter to fixture decorators, for example, @pytest.fixture(scope="class").: 72

Test filtering
Another feature of pytest is its ability to filter through tests, where only desired tests are selected to run, or behave in a certain way as desired by the developer. With the "k" option (e.g. pytest -k some_name), pytest would only run tests whose names include some_name. The opposite is true, where one can run pytest -k "not some_name", and pytest will run all tests whose names do not include some_name.
Pytest's markers can, in addition to altering test behaviour, also filter tests. Pytest's markers are Python decorators starting with the @pytest.mark.<markername> syntax placed on top of test functions. With different arbitrarily named markers, running pytest -m <markername> on the command line will only run those tests decorated with such markers.: 13  All available markers can be listed by the pytest --markers along with their descriptions; custom markers can also be defined by users and registered in pytest.ini, in which case pytest --markers will also list those custom markers along with builtin markers.: 147

See also
JUnit, well-known software testing framework based on Java
Doctest, well-known testing framework in Python for docstrings
List of unit testing frameworks

References
External links
Official website 
https://pypi.org/project/pytest/
https://docs.pytest.org

## Archive Info
- **Archived on:** 2024-12-15 20:39:02 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 7525 bytes
- **Word Count:** 1160 words
