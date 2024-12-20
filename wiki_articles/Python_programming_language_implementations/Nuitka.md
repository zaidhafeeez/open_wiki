---
title: Nuitka
url: https://en.wikipedia.org/wiki/Nuitka
language: en
categories: ["Category:All articles needing additional references", "Category:All articles with topics of unclear notability", "Category:Articles needing additional references from December 2017", "Category:Articles with multiple maintenance issues", "Category:Articles with short description", "Category:Articles with topics of unclear notability from December 2017", "Category:Official website different in Wikidata and Wikipedia", "Category:Products articles with topics of unclear notability", "Category:Python (programming language) implementations", "Category:Short description is different from Wikidata", "Category:Software using the Apache license", "Category:Source-to-source compilers"]
references: 0
last_modified: 2024-12-20T19:28:45Z
---

# Nuitka

## Summary

Nuitka (pronounced as ) is a source-to-source compiler which compiles Python code to C source code, applying some compile-time optimizations in the process such as constant folding and propagation, built-in call prediction, type inference, and conditional statement execution. Nuitka initially was designed to produce C++ code, but current versions produce C source code using only those features of C11 that are shared by C++03, enabling further compilation to a binary executable format by modern C

## Full Content

Nuitka (pronounced as ) is a source-to-source compiler which compiles Python code to C source code, applying some compile-time optimizations in the process such as constant folding and propagation, built-in call prediction, type inference, and conditional statement execution. Nuitka initially was designed to produce C++ code, but current versions produce C source code using only those features of C11 that are shared by C++03, enabling further compilation to a binary executable format by modern C and C++ compilers including gcc, clang, MinGW, or Microsoft Visual C++. It accepts Python code compatible with several different Python versions (currently supporting versions 2.6, 2.7, and 3.3–3.12) and optionally allows for the creation of standalone programs that do not require Python to be installed on the target computer.
Nuitka was discussed at the 2012 EuroPython conference, and serious development began at the end of the same year. It now supports virtually all of the features of the Python language. Additional compile-time optimizations are planned for future releases, including avoiding the use of Python objects for additional variables whose type can be inferred at compile time, particularly when using iterators, which is expected to result in a large performance increase.

Limitations
Currently it is not possible to cross-compile binaries (e.g. building the executable on Windows and shipping it to macOS).
Standalone binaries built using the --standalone command line option include an embedded CPython interpreter to handle aspects of the language that are not determined when the program is compiled and must be interpreted at runtime, such as duck typing, exception handling, and dynamic code execution (the eval function and exec function or statement), along with those Python and native libraries that are needed for execution, leading to rather large file sizes.
Nuitka's design heavily relies on the internals of the CPython interpreter, and as a result other implementations of the Python language such as PyPy, Jython, and IronPython cannot be used instead of CPython for the runtime interpreter and library.

Usage
Nuitka can be installed from the repositories of many Linux distributions. It can also be installed through pip and pip3, respectively. Compilation is done either with nuitka program.py or by calling Python itself and afterwards defining which module to run, which in this case is Nuitka (python -m nuitka program.py).

References
External links
Official website
Nuitka on GitHub - Source code and manual
