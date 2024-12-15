# Mojo (programming language)

## Metadata
- **Last Updated:** 2024-12-12 23:00:36 UTC
- **Original Article:** [Mojo (programming language)](https://en.wikipedia.org/wiki/Mojo_(programming_language))
- **Language:** en
- **Page ID:** 73729965

## Summary
Mojo is a programming language in the Python family that is currently under development. It is available both in browsers via Jupyter notebooks, and locally on Linux and macOS. Mojo aims to combine the usability of a high-level programming language, specifically Python, with the performance of a system programming language such as C++, Rust, and Zig. As of 2024, the Mojo compiler is opensource software (closed source) with an open source standard library. Modular, the company behind Mojo, has stated an intent to eventually open source the Mojo language, as it matures.
Mojo builds on the Multi-Level Intermediate Representation (MLIR) compiler software framework instead of directly on the lower level LLVM compiler framework, as do many languages such as Julia, Swift, Clang, and Rust. MLIR is a newer compiler framework that allows Mojo to exploit higher level compiler passes unavailable in LLVM alone, and allows Mojo to compile down and target more than only central processing units (CPUs), including producing code that can run on graphics  processing units (GPUs), Tensor Processing Units (TPUs), application-specific integrated circuits (ASICs) and other accelerators. It can also often more effectively use certain types of CPU optimizations directly, like single instruction, multiple data (SIMD) with no direct intervention by a developer, as occurs in many other languages. According to Jeremy Howard of fast.ai, Mojo can be seen as "syntax sugar for MLIR" and for that reason Mojo is well optimized for applications like artificial intelligence (AI).

## Categories
This article belongs to the following categories:

- Category:AI software
- Category:All articles containing potentially dated statements
- Category:All articles with unsourced statements
- Category:Articles containing potentially dated statements from 2024
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from October 2023
- Category:Cross-platform software
- Category:High-level programming languages
- Category:Multi-paradigm programming languages
- Category:Notebook interface
- Category:Official website different in Wikidata and Wikipedia
- Category:Programming languages
- Category:Programming languages created in 2023
- Category:Python (programming language)
- Category:Python (programming language) implementations
- Category:Short description is different from Wikidata
- Category:Software using the Apache license
- Category:Text-oriented programming languages

## Table of Contents

- Origin and development history
- Features
- Programming examples
- Usage
- See also
- References
- External links

## Content

Mojo is a programming language in the Python family that is currently under development. It is available both in browsers via Jupyter notebooks, and locally on Linux and macOS. Mojo aims to combine the usability of a high-level programming language, specifically Python, with the performance of a system programming language such as C++, Rust, and Zig. As of 2024, the Mojo compiler is opensource software (closed source) with an open source standard library. Modular, the company behind Mojo, has stated an intent to eventually open source the Mojo language, as it matures.
Mojo builds on the Multi-Level Intermediate Representation (MLIR) compiler software framework instead of directly on the lower level LLVM compiler framework, as do many languages such as Julia, Swift, Clang, and Rust. MLIR is a newer compiler framework that allows Mojo to exploit higher level compiler passes unavailable in LLVM alone, and allows Mojo to compile down and target more than only central processing units (CPUs), including producing code that can run on graphics  processing units (GPUs), Tensor Processing Units (TPUs), application-specific integrated circuits (ASICs) and other accelerators. It can also often more effectively use certain types of CPU optimizations directly, like single instruction, multiple data (SIMD) with no direct intervention by a developer, as occurs in many other languages. According to Jeremy Howard of fast.ai, Mojo can be seen as "syntax sugar for MLIR" and for that reason Mojo is well optimized for applications like artificial intelligence (AI).

Origin and development history
The Mojo programming language was created by Modular Inc, which was founded by Chris Lattner, the original architect of the Swift programming language and LLVM, and Tim Davis, a former Google employee. Intention behind Mojo is to bridge the gap between Python’s ease of use and the fast performance required for cutting-edge AI applications.
According to public change logs, Mojo development goes back to 2022. In May of 2023, the first publicly testable version was made available online via a hosted playground. By September 2023 Mojo was available for local download for Linux and by October 2023 it was also made available for download on Apple's macOS.
In March of 2024, Modular open sourced the Mojo standard library and started accepting community contributions under the Apache 2.0 license.

Features
Mojo was created for an easy transition from Python. The language has syntax similar to Python's, with inferred static typing, and allows users to import Python modules. It uses LLVM and MLIR as its compilation backend. The language also intends to add a foreign function interface to call C/C++ and Python code. The language is not source-compatible with Python 3, only providing a subset of its syntax, e.g. missing the global keyword, list and dictionary comprehensions, and support for classes. Further, Mojo also adds features that enable performant low-level programming: fn for creating typed, compiled functions and "struct" for memory-optimized alternatives to classes. Mojo structs support methods, fields, operator overloading, and decorators.
The language also provides a borrow checker, an influence from Rust. Mojo def functions use value semantics by default (functions receive a copy of all arguments and any modifications are not visible outside the function), while Python functions use reference semantics (functions receive a reference on their arguments and any modification of a mutable argument inside the function is visible outside).
The language is not open source, but it is planned to be made open source in the future.

Programming examples
In Mojo, functions can be declared using both fn (for performant functions) or def (for Python compatibility).
Basic arithmetic operations in Mojo with a def function:

and with an fn function:

The manner in which Mojo employs var and let for mutable and immutable variable declarations respectively mirrors the syntax found in Swift. In Swift, var is used for mutable variables, while let is designated for constants or immutable variables.
Variable declaration and usage in Mojo:

Usage
The Mojo SDK allows Mojo programmers to compile and execute Mojo source files locally from a command-line interface and currently supports Ubuntu and macOS. Additionally, there is a Mojo extension for Visual Studio Code which provides code completion and tooltips.
In January 2024, an inference model of LLaMA2 written in Mojo was released to the public.

See also
List of programming languages for artificial intelligence

References
External links
Official website
Mojo manual
mojo on GitHub
All about mojo programming language
Mojo may be the biggest programming language advance in decades
Mojo: The Future of AI Programming

## Archive Info
- **Archived on:** 2024-12-15 21:03:04 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 4802 bytes
- **Word Count:** 740 words
