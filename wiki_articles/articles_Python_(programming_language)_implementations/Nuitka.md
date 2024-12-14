# Nuitka

## Article Metadata

- **Last Updated:** 2024-12-14T19:49:10.140462+00:00
- **Original Article:** [Nuitka](https://en.wikipedia.org/wiki/Nuitka)
- **Language:** en
- **Page ID:** 56115363

## Summary

Nuitka (pronounced as ) is a source-to-source compiler which compiles Python code to C source code, applying some compile-time optimizations in the process such as constant folding and propagation, built-in call prediction, type inference, and conditional statement execution. Nuitka initially was designed to produce C++ code, but current versions produce C source code using only those features of C11 that are shared by C++03, enabling further compilation to a binary executable format by modern C

## Categories

- Category:All articles needing additional references
- Category:All articles with topics of unclear notability
- Category:Articles needing additional references from December 2017
- Category:Articles with multiple maintenance issues
- Category:Articles with short description
- Category:Articles with topics of unclear notability from December 2017
- Category:Official website different in Wikidata and Wikipedia
- Category:Products articles with topics of unclear notability
- Category:Python (programming language) implementations
- Category:Short description is different from Wikidata
- Category:Software using the Apache license
- Category:Source-to-source compilers

## Table of Contents

- Limitations
- Usage
- References
- External links

## Content

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

## Related Articles

### Internal Links

- [Apache License](https://en.wikipedia.org/wiki/Apache_License)
- [C++03](https://en.wikipedia.org/wiki/C%2B%2B03)
- [C11 (C standard revision)](https://en.wikipedia.org/wiki/C11_(C_standard_revision))
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Clang](https://en.wikipedia.org/wiki/Clang)
- [Constant folding](https://en.wikipedia.org/wiki/Constant_folding)
- [Cross compiler](https://en.wikipedia.org/wiki/Cross_compiler)
- [Duck typing](https://en.wikipedia.org/wiki/Duck_typing)
- [Exception handling](https://en.wikipedia.org/wiki/Exception_handling)
- [GNU Compiler Collection](https://en.wikipedia.org/wiki/GNU_Compiler_Collection)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [IronPython](https://en.wikipedia.org/wiki/IronPython)
- [Jython](https://en.wikipedia.org/wiki/Jython)
- [Microsoft Visual C++](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B)
- [MinGW](https://en.wikipedia.org/wiki/MinGW)
- [Pip (package manager)](https://en.wikipedia.org/wiki/Pip_(package_manager))
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [PyPy](https://en.wikipedia.org/wiki/PyPy)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Source-to-source compiler](https://en.wikipedia.org/wiki/Source-to-source_compiler)
- [Type inference](https://en.wikipedia.org/wiki/Type_inference)
- [Talk:Nuitka](https://en.wikipedia.org/wiki/Talk:Nuitka)
- [Wikipedia:Deletion policy](https://en.wikipedia.org/wiki/Wikipedia:Deletion_policy)
- [Wikipedia:Independent sources](https://en.wikipedia.org/wiki/Wikipedia:Independent_sources)
- [Wikipedia:Merging](https://en.wikipedia.org/wiki/Wikipedia:Merging)
- [Wikipedia:Notability (organizations and companies)](https://en.wikipedia.org/wiki/Wikipedia:Notability_(organizations_and_companies))
- [Wikipedia:Redirect](https://en.wikipedia.org/wiki/Wikipedia:Redirect)
- [Wikipedia:Reliable sources](https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Help:IPA/English](https://en.wikipedia.org/wiki/Help:IPA/English)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from December 2017](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_December_2017)
- [Category:Articles with topics of unclear notability from December 2017](https://en.wikipedia.org/wiki/Category:Articles_with_topics_of_unclear_notability_from_December_2017)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:49:10.140462+00:00_