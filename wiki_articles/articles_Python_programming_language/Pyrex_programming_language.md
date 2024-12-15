# Pyrex (programming language)

## Metadata
- **Last Updated:** 2024-11-24 06:40:49 UTC
- **Original Article:** [Pyrex (programming language)](https://en.wikipedia.org/wiki/Pyrex_(programming_language))
- **Language:** en
- **Page ID:** 3274540

## Summary
Pyrex is a programming language for creating Python modules. Its syntax is very close to Python and it makes it easy for Python programmers to write non-Python supporting code for interfacing modules in a language which is as close to Python as possible.
Python itself only provides a C API to write extension modules, which allows writing of functions and datatypes in C. These can then be accessed from Python. It is possible to wrap the functions and datatypes of existing C libraries as Python objects and therefore make them available to Python.
Pyrex allows the user to write extension modules in a Python-like language which may directly access the external C code. The similarity of Pyrex's syntax to Python's makes it easy to write Python modules, but there are some functional limitations. The programmer must specify the name of C-header files, enumerations, datatypes and functions needing to be accessed in the module, then they can be used as if they were Python objects. The Pyrex compiler will generate the necessary glue code automatically and compile the Pyrex code into a working Python module.
There are tools like SWIG or Python's foreign function library ctypes which can be used for this task without requiring much additional code, but this is limited to making an external library available in Python code. If adjustments to the API are needed, glue code must again be written manually.

## Categories
This article belongs to the following categories:

- Category:All articles with unsourced statements
- Category:All stub articles
- Category:Articles with unsourced statements from June 2021
- Category:Computer programming stubs
- Category:Free and open source compilers
- Category:Python (programming language)
- Category:Use dmy dates from July 2023

## Table of Contents

- See also
- References
- External links

## Content

Pyrex is a programming language for creating Python modules. Its syntax is very close to Python and it makes it easy for Python programmers to write non-Python supporting code for interfacing modules in a language which is as close to Python as possible.
Python itself only provides a C API to write extension modules, which allows writing of functions and datatypes in C. These can then be accessed from Python. It is possible to wrap the functions and datatypes of existing C libraries as Python objects and therefore make them available to Python.
Pyrex allows the user to write extension modules in a Python-like language which may directly access the external C code. The similarity of Pyrex's syntax to Python's makes it easy to write Python modules, but there are some functional limitations. The programmer must specify the name of C-header files, enumerations, datatypes and functions needing to be accessed in the module, then they can be used as if they were Python objects. The Pyrex compiler will generate the necessary glue code automatically and compile the Pyrex code into a working Python module.
There are tools like SWIG or Python's foreign function library ctypes which can be used for this task without requiring much additional code, but this is limited to making an external library available in Python code. If adjustments to the API are needed, glue code must again be written manually.

See also
Cython

References
External links
Official website

## Archive Info
- **Archived on:** 2024-12-15 21:03:06 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 1472 bytes
- **Word Count:** 242 words
