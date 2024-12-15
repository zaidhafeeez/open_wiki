# Pyrex (programming language)

## Article Metadata

- **Last Updated:** 2024-12-15T03:19:26.722324+00:00
- **Original Article:** [Pyrex (programming language)](https://en.wikipedia.org/wiki/Pyrex_(programming_language))
- **Language:** en
- **Page ID:** 3274540

## Summary

Pyrex is a programming language for creating Python modules. Its syntax is very close to Python and it makes it easy for Python programmers to write non-Python supporting code for interfacing modules in a language which is as close to Python as possible.
Python itself only provides a C API to write extension modules, which allows writing of functions and datatypes in C. These can then be accessed from Python. It is possible to wrap the functions and datatypes of existing C libraries as Python ob

## Categories

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

## Related Articles

### Internal Links

- [API](https://en.wikipedia.org/wiki/API)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Cython](https://en.wikipedia.org/wiki/Cython)
- [Data type](https://en.wikipedia.org/wiki/Data_type)
- [Enumerated type](https://en.wikipedia.org/wiki/Enumerated_type)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Library (computing)](https://en.wikipedia.org/wiki/Library_(computing))
- [Modular programming](https://en.wikipedia.org/wiki/Modular_programming)
- [O'Reilly Media](https://en.wikipedia.org/wiki/O%27Reilly_Media)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Prentice Hall](https://en.wikipedia.org/wiki/Prentice_Hall)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [SWIG](https://en.wikipedia.org/wiki/SWIG)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Springer Science+Business Media](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Talk:Pyrex (programming language)](https://en.wikipedia.org/wiki/Talk:Pyrex_(programming_language))
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Stub](https://en.wikipedia.org/wiki/Wikipedia:Stub)
- [Template:Compu-prog-stub](https://en.wikipedia.org/wiki/Template:Compu-prog-stub)
- [Template talk:Compu-prog-stub](https://en.wikipedia.org/wiki/Template_talk:Compu-prog-stub)
- [Category:Articles with unsourced statements from June 2021](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_June_2021)
- [Category:Use dmy dates from July 2023](https://en.wikipedia.org/wiki/Category:Use_dmy_dates_from_July_2023)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:19:26.722324+00:00_