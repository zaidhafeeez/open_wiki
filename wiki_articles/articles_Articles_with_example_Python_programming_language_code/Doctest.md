# Doctest

## Metadata
- **Last Updated:** 2024-12-03 07:00:28 UTC
- **Original Article:** [Doctest](https://en.wikipedia.org/wiki/Doctest)
- **Language:** en
- **Page ID:** 3415737

## Summary
doctest is a module included in the Python programming language's standard library that allows the easy generation of tests based on output from the standard Python interpreter shell, cut and pasted into docstrings.

## Categories
This article belongs to the following categories:

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Short description matches Wikidata
- Category:Software testing tools
- Category:Technical communication

## Table of Contents

- Implementation specifics
- Literate programming and doctests
- Documenting libraries by example
- Examples
- Doctest and documentation generators
- Implementation in other programming languages
- References
- External links

## Content

doctest is a module included in the Python programming language's standard library that allows the easy generation of tests based on output from the standard Python interpreter shell, cut and pasted into docstrings.

Implementation specifics
Doctest makes innovative use of the following Python capabilities:

docstrings
The Python interactive shell (both command line and the included idle application)
Python introspection
When using the Python shell, the primary prompt: >>> , is followed by new commands. The secondary prompt: ... , is used when continuing commands on multiple lines; and the result of executing the command is expected on following lines.
A blank line, or another line starting with the primary prompt is seen as the end of the output from the command.
The doctest module looks for such sequences of prompts in a docstring, re-executes the extracted command and checks the output against the output of the command given in the docstrings test example.
The default action when running doctests is for no output to be shown when tests pass. This can be modified by options to the doctest runner. In addition, doctest has been integrated with the Python unit test module allowing doctests to be run as standard unittest testcases. Unittest testcase runners allow more options when running tests such as the reporting of test statistics such as tests passed, and failed.

Literate programming and doctests
Although doctest does not allow a Python program to be embedded in narrative text, it does allow for verifiable examples to be embedded in docstrings, where the docstrings can contain other text. Docstrings can in turn be extracted from program files to generate documentation in other formats such as HTML or PDF. 
A program file can be made to contain the documentation, tests, as well as the code and the tests easily verified against the code. This allows code, tests, and documentation to evolve together.

Documenting libraries by example
Doctests are well suited to provide an introduction to a library by demonstrating how the API is used.
On the basis of the output of Python's interactive interpreter, text can be mixed with tests that exercise the library, showing expected results.

Examples
Example one shows how narrative text can be interspersed with testable examples in a docstring. 
In the second example, more features of doctest are shown, together with their explanation. 
Example three is set up to run all doctests in a file when the file is run, but when imported as a module, the tests will not be run.

Example 1: A doctest embedded in the docstring of a function
Example 2: doctests embedded in a README.txt file
Example 3: unique_words.py
This example also simulates input to the function from a file by using the Python StringIO module

Doctest and documentation generators
Both the EpyText format of Epydoc and Docutils' reStructuredText format support the markup of doctest sections within docstrings.

Implementation in other programming languages
In C++, the doctest framework is the closest possible implementation of the concept – tests can be written directly in the production code with minimal overhead and the option to strip them from the binary.
The ExUnit.DocTest Elixir library implements functionality similar to Doctest.
An implementation of Doctest for Haskell.
Writing documentation tests in Elm.
Writing documentation tests in Rust.
Writing documentation tests in Elixir.
byexample supports writing doctests for several popular programming languages (e.g. Python, Ruby, Shell, JavaScript, C/C++, Java, Go, Rust) inside Markdown, reStructuredText and other text documents.

References
External links
doctest — Test interactive Python examples

## Archive Info
- **Archived on:** 2024-12-15 15:18:26 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 3717 bytes
- **Word Count:** 580 words
