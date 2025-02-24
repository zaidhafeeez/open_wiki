# Cython

## Article Metadata

- **Last Updated:** 2024-12-14T19:48:39.446556+00:00
- **Original Article:** [Cython](https://en.wikipedia.org/wiki/Cython)
- **Language:** en
- **Page ID:** 18384111

## Summary

Cython () is a superset of the programming language Python, which allows developers to write Python code (with optional, C-inspired syntax extensions) that yields performance comparable to that of C.
Cython is a compiled language that is typically used to generate CPython extension modules. Annotated Python-like code is compiled to C and then automatically wrapped in interface code, producing extension modules that can be loaded and used by regular Python code using the import statement, but wit

## Categories

- Category:All articles lacking reliable references
- Category:All articles needing expert attention
- Category:All articles that are too technical
- Category:Articles lacking reliable references from October 2018
- Category:Articles needing expert attention from May 2024
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:CS1 errors: periodical ignored
- Category:CS1 maint: numeric names: authors list
- Category:Python (programming language)
- Category:Python (programming language) implementations
- Category:Short description is different from Wikidata
- Category:Software using the Apache license
- Category:Source-to-source compilers
- Category:Use dmy dates from February 2014
- Category:Wikipedia articles that are too technical from May 2024

## Table of Contents

- Design
- History
- Example
- Using in IPython/Jupyter notebook
- Uses
- See also
- References
- External links

## Content

Cython () is a superset of the programming language Python, which allows developers to write Python code (with optional, C-inspired syntax extensions) that yields performance comparable to that of C.
Cython is a compiled language that is typically used to generate CPython extension modules. Annotated Python-like code is compiled to C and then automatically wrapped in interface code, producing extension modules that can be loaded and used by regular Python code using the import statement, but with significantly less computational overhead at run time. Cython also facilitates wrapping independent C or C++ code into python-importable modules.
Cython is written in Python and C and works on Windows, macOS, and Linux, producing C source files compatible with CPython 2.6, 2.7, and 3.3 and later versions. The Cython source code that Cython compiles (to C) can use both Python 2 and Python 3 syntax, defaulting to Python 2 syntax in Cython 0.x and Python 3 syntax in Cython 3.x. The default can be overridden (e.g. in source code comment) to Python 3 (or 2) syntax. Since Python 3 syntax has changed in recent versions, Cython may not be up to date with the latest additions. Cython has "native support for most of the C++ language" and "compiles almost all existing Python code".
Cython 3.0.0 was released on 17 July 2023.

Design
Cython works by producing a standard Python module. However, the behavior differs from standard Python in that the module code, originally written in Python, is translated into C. While the resulting code is fast, it makes many calls into the CPython interpreter and CPython standard libraries to perform actual work. Choosing this arrangement saved considerably on Cython's development time, but modules have a dependency on the Python interpreter and standard library.
Although most of the code is C-based, a small stub loader written in interpreted Python is usually required (unless the goal is to create a loader written entirely in C, which may involve work with the undocumented internals of CPython). However, this is not a major problem due to the presence of the Python interpreter.
Cython has a foreign function interface for invoking C/C++ routines and the ability to declare the static type of subroutine parameters and results, local variables, and class attributes.
A Cython program that implements the same algorithm as a corresponding Python program may consume fewer computing resources such as core memory and processing cycles due to differences between the CPython and Cython execution models. A basic Python program is loaded and executed by the CPython virtual machine, so both the runtime and the program itself consume computing resources. A Cython program is compiled to C code, which is further compiled to machine code, so the virtual machine is used only briefly when the program is loaded.
Cython employs:

Optimistic optimizations
Type inference (optional)
Low overhead in control structures
Low function call overhead
Performance depends both on what C code is generated by Cython and how that code is compiled by the C compiler.

History
Cython is a derivative of the Pyrex language, but it supports more features and optimizations than Pyrex. Cython was forked from Pyrex in 2007 by developers of the Sage computer algebra package, because they were unhappy with Pyrex's limitations and could not get patches accepted by Pyrex's maintainer Greg Ewing, who envisioned a much smaller scope for his tool than the Sage developers had in mind. They then forked Pyrex as SageX. When they found people were downloading Sage just to get SageX, and developers of other packages (including Stefan Behnel, who maintains the XML library LXML) were also maintaining forks of Pyrex, SageX was split off the Sage project and merged with cython-lxml to become Cython.
Cython files have a .pyx extension. At its most basic, Cython code looks exactly like Python code. However, whereas standard Python is dynamically typed, in Cython, types can optionally be provided, allowing for improved performance, allowing loops to be converted into C loops where possible. For example:

Example
A sample hello world program for Cython is more complex than in most languages because it interfaces with the Python C API and setuptools or other PEP517-compliant extension building facilities. At least three files are required for a basic project:

A setup.py file to invoke the setuptools build process that generates the extension module
A main python program to load the extension module
Cython source file(s)
The following code listings demonstrate the build and launch process:

These commands build and launch the program:

Using in IPython/Jupyter notebook
A more straightforward way to start with Cython is through command-line IPython (or through in-browser python console called Jupyter notebook):

which gives a 95 times improvement over the pure-python version. More details on the subject in the official quickstart page.

Uses
Cython is particularly popular among scientific users of Python, where it has "the perfect audience" according to Python creator Guido van Rossum. Of particular note:

The free software SageMath computer algebra system depends on Cython, both for performance and to interface with other libraries.
Significant parts of the scientific computing libraries SciPy, pandas and scikit-learn are written in Cython.
Some high-traffic websites such as Quora use Cython.
Cython's domain is not limited to just numerical computing. For example, the lxml XML toolkit is written mostly in Cython, and like its predecessor Pyrex, Cython is used to provide Python bindings for many C and C++ libraries such as the messaging library ZeroMQ. Cython can also be used to develop parallel programs for multi-core processor machines; this feature makes use of the OpenMP library.

See also
PyPy
Numba

References
External links
Official website 
Cython on GitHub

## Related Articles

### Internal Links

- ["Hello, World!" program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)
- [Apache License](https://en.wikipedia.org/wiki/Apache_License)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Asynchronous Server Gateway Interface](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CLPython](https://en.wikipedia.org/wiki/CLPython)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [CircuitPython](https://en.wikipedia.org/wiki/CircuitPython)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Compiled language](https://en.wikipedia.org/wiki/Compiled_language)
- [Computing in Science & Engineering](https://en.wikipedia.org/wiki/Computing_in_Science_%26_Engineering)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Eric (software)](https://en.wikipedia.org/wiki/Eric_(software))
- [Filename extension](https://en.wikipedia.org/wiki/Filename_extension)
- [Foreign function interface](https://en.wikipedia.org/wiki/Foreign_function_interface)
- [Fork (software development)](https://en.wikipedia.org/wiki/Fork_(software_development))
- [Free software](https://en.wikipedia.org/wiki/Free_software)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
- [Handle System](https://en.wikipedia.org/wiki/Handle_System)
- [IDLE](https://en.wikipedia.org/wiki/IDLE)
- [IPython](https://en.wikipedia.org/wiki/IPython)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment)
- [IronPython](https://en.wikipedia.org/wiki/IronPython)
- [Journal of Machine Learning Research](https://en.wikipedia.org/wiki/Journal_of_Machine_Learning_Research)
- [Jython](https://en.wikipedia.org/wiki/Jython)
- [Linux](https://en.wikipedia.org/wiki/Linux)
- [List of Python software](https://en.wikipedia.org/wiki/List_of_Python_software)
- [Comparison of integrated development environments](https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [MicroPython](https://en.wikipedia.org/wiki/MicroPython)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Multi-core processor](https://en.wikipedia.org/wiki/Multi-core_processor)
- [Ninja-IDE](https://en.wikipedia.org/wiki/Ninja-IDE)
- [Notebook interface](https://en.wikipedia.org/wiki/Notebook_interface)
- [Numba](https://en.wikipedia.org/wiki/Numba)
- [O'Reilly Media](https://en.wikipedia.org/wiki/O%27Reilly_Media)
- [OpenMP](https://en.wikipedia.org/wiki/OpenMP)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Pandas (software)](https://en.wikipedia.org/wiki/Pandas_(software))
- [Parallel computing](https://en.wikipedia.org/wiki/Parallel_computing)
- [Programming language implementation](https://en.wikipedia.org/wiki/Programming_language_implementation)
- [Psyco](https://en.wikipedia.org/wiki/Psyco)
- [PyCharm](https://en.wikipedia.org/wiki/PyCharm)
- [PyDev](https://en.wikipedia.org/wiki/PyDev)
- [PyPy](https://en.wikipedia.org/wiki/PyPy)
- [Pyrex (programming language)](https://en.wikipedia.org/wiki/Pyrex_(programming_language))
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Conference](https://en.wikipedia.org/wiki/Python_Conference)
- [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation)
- [Python for S60](https://en.wikipedia.org/wiki/Python_for_S60)
- [Quora](https://en.wikipedia.org/wiki/Quora)
- [Execution (computing)](https://en.wikipedia.org/wiki/Execution_(computing))
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [SageMath](https://en.wikipedia.org/wiki/SageMath)
- [SciPy](https://en.wikipedia.org/wiki/SciPy)
- [Scikit-learn](https://en.wikipedia.org/wiki/Scikit-learn)
- [Shed Skin](https://en.wikipedia.org/wiki/Shed_Skin)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Spyder (software)](https://en.wikipedia.org/wiki/Spyder_(software))
- [Stackless Python](https://en.wikipedia.org/wiki/Stackless_Python)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Subset](https://en.wikipedia.org/wiki/Subset)
- [Type inference](https://en.wikipedia.org/wiki/Type_inference)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [Virtual machine](https://en.wikipedia.org/wiki/Virtual_machine)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Wrapper library](https://en.wikipedia.org/wiki/Wrapper_library)
- [XML](https://en.wikipedia.org/wiki/XML)
- [YouTube](https://en.wikipedia.org/wiki/YouTube)
- [ZeroMQ](https://en.wikipedia.org/wiki/ZeroMQ)
- [Wikipedia:Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Cite book](https://en.wikipedia.org/wiki/Template:Cite_book)
- [Template:Cite web](https://en.wikipedia.org/wiki/Template:Cite_web)
- [Template:Latest preview software release/Cython](https://en.wikipedia.org/wiki/Template:Latest_preview_software_release/Cython)
- [Template:Latest stable software release/Cython](https://en.wikipedia.org/wiki/Template:Latest_stable_software_release/Cython)
- [Template:Python (programming language)](https://en.wikipedia.org/wiki/Template:Python_(programming_language))
- [Template talk:Python (programming language)](https://en.wikipedia.org/wiki/Template_talk:Python_(programming_language))
- [Help:CS1 errors](https://en.wikipedia.org/wiki/Help:CS1_errors)
- [Help:IPA/English](https://en.wikipedia.org/wiki/Help:IPA/English)
- [Category:Articles lacking reliable references from October 2018](https://en.wikipedia.org/wiki/Category:Articles_lacking_reliable_references_from_October_2018)
- [Category:Articles needing expert attention from May 2024](https://en.wikipedia.org/wiki/Category:Articles_needing_expert_attention_from_May_2024)
- [Category:CS1 maint: numeric names: authors list](https://en.wikipedia.org/wiki/Category:CS1_maint:_numeric_names:_authors_list)
- [Category:Use dmy dates from February 2014](https://en.wikipedia.org/wiki/Category:Use_dmy_dates_from_February_2014)
- [Category:Wikipedia articles that are too technical from May 2024](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_that_are_too_technical_from_May_2024)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:48:39.446556+00:00_