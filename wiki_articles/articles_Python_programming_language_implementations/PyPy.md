# PyPy

## Metadata
- **Last Updated:** 2024-12-04 11:57:53 UTC
- **Original Article:** [PyPy](https://en.wikipedia.org/wiki/PyPy)
- **Language:** en
- **Page ID:** 2564605

## Summary
PyPy () is an implementation of the Python programming language. PyPy often runs faster than the standard implementation CPython because PyPy uses a just-in-time compiler. Most Python code runs well on PyPy except for code that depends on CPython extensions, which either does not work or incurs some overhead when run in PyPy.
PyPy itself is built using a technique known as meta-tracing, which is a mostly automatic transformation that takes an interpreter as input and produces a tracing just-in-time compiler as output. Since interpreters are usually easier to write than compilers, but run slower, this technique can make it easier to produce efficient implementations of programming languages. PyPy's meta-tracing toolchain is called RPython.
PyPy does not have full compatibility with more recent versions of the CPython ecosystem. While it claims compatibility with Python 2.7, 3.7, 3.8 and 3.9 ("a drop-in replacement for CPython"), it lacks some of the newer features and syntax in Python 3.10, such as syntax for pattern matching.

## Categories
This article belongs to the following categories:

- Category:2007 software
- Category:Articles with short description
- Category:FP6 projects
- Category:Free software programmed in Python
- Category:Python (programming language) implementations
- Category:Python (programming language) software
- Category:Short description is different from Wikidata
- Category:Software using the MIT license
- Category:Stack-based virtual machines
- Category:Wikipedia articles needing clarification from May 2013

## Table of Contents

- Details and motivation
- Project status
- History
- See also
- Notes
- References
- External links

## Content

PyPy () is an implementation of the Python programming language. PyPy often runs faster than the standard implementation CPython because PyPy uses a just-in-time compiler. Most Python code runs well on PyPy except for code that depends on CPython extensions, which either does not work or incurs some overhead when run in PyPy.
PyPy itself is built using a technique known as meta-tracing, which is a mostly automatic transformation that takes an interpreter as input and produces a tracing just-in-time compiler as output. Since interpreters are usually easier to write than compilers, but run slower, this technique can make it easier to produce efficient implementations of programming languages. PyPy's meta-tracing toolchain is called RPython.
PyPy does not have full compatibility with more recent versions of the CPython ecosystem. While it claims compatibility with Python 2.7, 3.7, 3.8 and 3.9 ("a drop-in replacement for CPython"), it lacks some of the newer features and syntax in Python 3.10, such as syntax for pattern matching.

Details and motivation
PyPy aims to provide a common translation and support framework for producing implementations of dynamic languages, emphasizing a clean separation between language specification and implementation aspects. It also aims to provide a compliant, flexible and fast implementation of the Python programming language using the above framework to enable new advanced features without having to encode low-level details into it.

RPython
The PyPy interpreter itself is written in a restricted subset of Python called RPython (Restricted Python). RPython puts some constraints on the Python language such that a variable's type can be inferred at compile time.
The PyPy project has developed a toolchain that analyzes RPython code and translates it into a form of byte code, which can be lowered into C. There used to be other backends in addition to C (Java, C#, and JavaScript), but those suffered from bitrot and have been removed. Thus, the recursive logo of PyPy is a snake swallowing itself since the RPython is translated by a Python interpreter. The code can also be run untranslated for testing and analysis, which provides a nice test-bed for research into dynamic languages.
It allows for pluggable garbage collectors, as well as optionally enabling Stackless Python features. Finally, it includes a just-in-time (JIT) generator that builds a just-in-time compiler into the interpreter, given a few annotations in the interpreter source code. The generated JIT compiler is a tracing JIT.
RPython is now also used to write non-Python language implementations, such as Pixie.

Project status
PyPy as of version 7.3.17 is compatible with two CPython versions: 2.7 and 3.10. The first PyPy version compatible with CPython v3 is PyPy v2.3.1 (2014). The PyPy interpreter compatible with CPython v3 is also known as PyPy3.
PyPy has JIT compilation support on 32-bit/64-bit x86 and 32-bit/64-bit ARM processors. It is tested nightly on Windows, Linux, OpenBSD and Mac OS X. PyPy is able to run pure Python software that does not rely on implementation-specific features.
There is a compatibility layer for CPython C API extensions called CPyExt, but it is incomplete and experimental. The preferred way of interfacing with C shared libraries is through the built-in C foreign function interface (CFFI) or ctypes libraries.

History
PyPy is a followup to the Psyco project, a just-in-time specializing compiler for Python, developed by Armin Rigo between 2002 and 2010. PyPy's aim is to have a just-in-time specializing compiler with scope, which was not available for Psyco. Initially, the RPython could also be compiled into Java bytecode, CIL and JavaScript, but these backends were removed due to lack of interest.
PyPy was initially a research and development-oriented project. Reaching a mature state of development and an official 1.0 release in mid-2007, its next focus was on releasing a production-ready version with more CPython compatibility. Many of PyPy's changes have been made during coding sprints.

In August 2008, PyPy was able to run some popular Python libraries like Pylons, Pyglet, Nevow and Django.
On 12 March 2010, PyPy 1.2 was released, focusing on speed. It included a working, though not yet stable, just-in-time compiler.
On 30 April 2011, PyPy version 1.5 was released, which reached compatibility with CPython 2.7.
On 9 May 2013, PyPy 2.0 was released, which introduced alpha-quality support for JIT compilation on ARMv6 and ARMv7 JIT, and included CFFI in the standard library.
On 20 June 2014, PyPy3 was declared stable and introduced compatibility with the more modern Python 3. It was released alongside PyPy 2.3.1 and bears the same version number.
On 21 March 2017, the PyPy project released version 5.7 of both PyPy and PyPy3, with the latter introducing beta-quality support for Python 3.5.
On 26 April 2018, version 6.0 was released, with support for Python 2.7 and 3.5 (still beta-quality on Windows).
On 11 February 2019, version 7.0 was released, with support for Python 2.7 and 3.5.
On 14 October 2019, version 7.2 was released, with support for Python 3.6.9.
On 24 December 2019, version 7.3 was released, with support for Python 3.6.9.
On 16 February 2020, the PyPy team announced the move of the source code hosting from Bitbucket to heptapod.net with the repositories of the CFFI (C Foreign Function Interface) project. A new logo and website design are also published. However, the author and the license of the new logo are unknown.
On 29 December 2023, PyPy announced hosting has moved to GitHub and development will now be tracked with git.

Funding
PyPy was funded by the European Union being a Specific Targeted Research Project between December 2004 and March 2007. In June 2008, PyPy announced funding being part of the Google Open Source programs and has agreed to focus on making PyPy more compatible with CPython. In 2009 Eurostars, a European Union funding agency specially focused on SMEs, accepted a proposal from PyPy project members titled "PYJIT – a fast and flexible toolkit for dynamic programming languages based on PyPy". Eurostars funding lasted until August 2011.
At PyCon US 2011, the Python Software Foundation provided a $10,000 grant for PyPy to continue work on performance and compatibility with newer versions of the language.
The port to ARM architecture was sponsored in part by the Raspberry Pi Foundation.
The PyPy project also accepts donations through its status blog pages. As of 2013, a variety of sub-projects had funding: Python 3 version compatibility, built-in optimized NumPy support for numerical calculations and software transactional memory support to allow better parallelism.

See also
Bootstrapping (compilers)
Cython
GraalVM
Partial evaluation
Psyco
Self-hosting
Self-interpreter
Unladen Swallow

Notes
References
External links
Official website

## Archive Info
- **Archived on:** 2024-12-15 21:07:09 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 6906 bytes
- **Word Count:** 1084 words
