# Mojo (programming language)

## Article Metadata

- **Last Updated:** 2024-12-15T03:19:27.908356+00:00
- **Original Article:** [Mojo (programming language)](https://en.wikipedia.org/wiki/Mojo_(programming_language))
- **Language:** en
- **Page ID:** 73729965

## Summary

Mojo is a programming language in the Python family that is currently under development. It is available both in browsers via Jupyter notebooks, and locally on Linux and macOS. Mojo aims to combine the usability of a high-level programming language, specifically Python, with the performance of a system programming language such as C++, Rust, and Zig. As of 2024, the Mojo compiler is opensource software (closed source) with an open source standard library. Modular, the company behind Mojo, has st

## Categories

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

## Related Articles

### Internal Links

- [ADMB](https://en.wikipedia.org/wiki/ADMB)
- [ALGOL](https://en.wikipedia.org/wiki/ALGOL)
- [APL (programming language)](https://en.wikipedia.org/wiki/APL_(programming_language))
- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language))
- [Advanced Simulation Library](https://en.wikipedia.org/wiki/Advanced_Simulation_Library)
- [Substructural type system](https://en.wikipedia.org/wiki/Substructural_type_system)
- [Analyse-it](https://en.wikipedia.org/wiki/Analyse-it)
- [Apache License](https://en.wikipedia.org/wiki/Apache_License)
- [Apple Inc.](https://en.wikipedia.org/wiki/Apple_Inc.)
- [Application-specific integrated circuit](https://en.wikipedia.org/wiki/Application-specific_integrated_circuit)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence)
- [Assembly language](https://en.wikipedia.org/wiki/Assembly_language)
- [BASIC](https://en.wikipedia.org/wiki/BASIC)
- [BMDP](https://en.wikipedia.org/wiki/BMDP)
- [BV4.1 (software)](https://en.wikipedia.org/wiki/BV4.1_(software))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [COBOL](https://en.wikipedia.org/wiki/COBOL)
- [CSPro](https://en.wikipedia.org/wiki/CSPro)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Central processing unit](https://en.wikipedia.org/wiki/Central_processing_unit)
- [Chapel (programming language)](https://en.wikipedia.org/wiki/Chapel_(programming_language))
- [Chris Lattner](https://en.wikipedia.org/wiki/Chris_Lattner)
- [Clang](https://en.wikipedia.org/wiki/Clang)
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Command-line interface](https://en.wikipedia.org/wiki/Command-line_interface)
- [Commercial software](https://en.wikipedia.org/wiki/Commercial_software)
- [Comparison of numerical-analysis software](https://en.wikipedia.org/wiki/Comparison_of_numerical-analysis_software)
- [Comparison of programming languages](https://en.wikipedia.org/wiki/Comparison_of_programming_languages)
- [Comparison of statistical packages](https://en.wikipedia.org/wiki/Comparison_of_statistical_packages)
- [Compiled language](https://en.wikipedia.org/wiki/Compiled_language)
- [Compiler](https://en.wikipedia.org/wiki/Compiler)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [CumFreq](https://en.wikipedia.org/wiki/CumFreq)
- [Cython](https://en.wikipedia.org/wiki/Cython)
- [DADiSP](https://en.wikipedia.org/wiki/DADiSP)
- [DAP (software)](https://en.wikipedia.org/wiki/DAP_(software))
- [Data Desk](https://en.wikipedia.org/wiki/Data_Desk)
- [Dataplot](https://en.wikipedia.org/wiki/Dataplot)
- [Duck typing](https://en.wikipedia.org/wiki/Duck_typing)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [EViews](https://en.wikipedia.org/wiki/EViews)
- [Emoji](https://en.wikipedia.org/wiki/Emoji)
- [Epi Info](https://en.wikipedia.org/wiki/Epi_Info)
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Euler Mathematical Toolbox](https://en.wikipedia.org/wiki/Euler_Mathematical_Toolbox)
- [FEATool Multiphysics](https://en.wikipedia.org/wiki/FEATool_Multiphysics)
- [Field (computer science)](https://en.wikipedia.org/wiki/Field_(computer_science))
- [Filename extension](https://en.wikipedia.org/wiki/Filename_extension)
- [Foreign function interface](https://en.wikipedia.org/wiki/Foreign_function_interface)
- [Forth (programming language)](https://en.wikipedia.org/wiki/Forth_(programming_language))
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Fortress (programming language)](https://en.wikipedia.org/wiki/Fortress_(programming_language))
- [FreeFem++](https://en.wikipedia.org/wiki/FreeFem%2B%2B)
- [FreeMat](https://en.wikipedia.org/wiki/FreeMat)
- [Freeware](https://en.wikipedia.org/wiki/Freeware)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [GAUSS (software)](https://en.wikipedia.org/wiki/GAUSS_(software))
- [GNU Octave](https://en.wikipedia.org/wiki/GNU_Octave)
- [Generational list of programming languages](https://en.wikipedia.org/wiki/Generational_list_of_programming_languages)
- [Generic programming](https://en.wikipedia.org/wiki/Generic_programming)
- [Genius (mathematics software)](https://en.wikipedia.org/wiki/Genius_(mathematics_software))
- [Genstat](https://en.wikipedia.org/wiki/Genstat)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Gmsh](https://en.wikipedia.org/wiki/Gmsh)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Google](https://en.wikipedia.org/wiki/Google)
- [GraphPad Software](https://en.wikipedia.org/wiki/GraphPad_Software)
- [GraphPad Software](https://en.wikipedia.org/wiki/GraphPad_Software)
- [Graphics processing unit](https://en.wikipedia.org/wiki/Graphics_processing_unit)
- [Gretl](https://en.wikipedia.org/wiki/Gretl)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [High-level programming language](https://en.wikipedia.org/wiki/High-level_programming_language)
- [History of programming languages](https://en.wikipedia.org/wiki/History_of_programming_languages)
- [IDLE](https://en.wikipedia.org/wiki/IDLE)
- [IPython](https://en.wikipedia.org/wiki/IPython)
- [Imperative programming](https://en.wikipedia.org/wiki/Imperative_programming)
- [JASP](https://en.wikipedia.org/wiki/JASP)
- [JMP (statistical software)](https://en.wikipedia.org/wiki/JMP_(statistical_software))
- [JMulTi](https://en.wikipedia.org/wiki/JMulTi)
- [Jamovi](https://en.wikipedia.org/wiki/Jamovi)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Jeremy Howard (entrepreneur)](https://en.wikipedia.org/wiki/Jeremy_Howard_(entrepreneur))
- [Julia (programming language)](https://en.wikipedia.org/wiki/Julia_(programming_language))
- [Just another Gibbs sampler](https://en.wikipedia.org/wiki/Just_another_Gibbs_sampler)
- [Kotlin (programming language)](https://en.wikipedia.org/wiki/Kotlin_(programming_language))
- [LIMDEP](https://en.wikipedia.org/wiki/LIMDEP)
- [LISREL](https://en.wikipedia.org/wiki/LISREL)
- [LLVM](https://en.wikipedia.org/wiki/LLVM)
- [Llama (language model)](https://en.wikipedia.org/wiki/Llama_(language_model))
- [LabVIEW](https://en.wikipedia.org/wiki/LabVIEW)
- [Linux](https://en.wikipedia.org/wiki/Linux)
- [Lisp (programming language)](https://en.wikipedia.org/wiki/Lisp_(programming_language))
- [List of numerical-analysis software](https://en.wikipedia.org/wiki/List_of_numerical-analysis_software)
- [List of programming languages](https://en.wikipedia.org/wiki/List_of_programming_languages)
- [List of programming languages by type](https://en.wikipedia.org/wiki/List_of_programming_languages_by_type)
- [List of programming languages for artificial intelligence](https://en.wikipedia.org/wiki/List_of_programming_languages_for_artificial_intelligence)
- [List of statistical software](https://en.wikipedia.org/wiki/List_of_statistical_software)
- [Lua (programming language)](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [MFEM](https://en.wikipedia.org/wiki/MFEM)
- [MLIR (software)](https://en.wikipedia.org/wiki/MLIR_(software))
- [ML (programming language)](https://en.wikipedia.org/wiki/ML_(programming_language))
- [MLwiN](https://en.wikipedia.org/wiki/MLwiN)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [Maple (software)](https://en.wikipedia.org/wiki/Maple_(software))
- [Mathcad](https://en.wikipedia.org/wiki/Mathcad)
- [MedCalc](https://en.wikipedia.org/wiki/MedCalc)
- [Memory model (programming)](https://en.wikipedia.org/wiki/Memory_model_(programming))
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Microfit](https://en.wikipedia.org/wiki/Microfit)
- [Microsoft Excel](https://en.wikipedia.org/wiki/Microsoft_Excel)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Minitab](https://en.wikipedia.org/wiki/Minitab)
- [Modular programming](https://en.wikipedia.org/wiki/Modular_programming)
- [NCSS (statistical software)](https://en.wikipedia.org/wiki/NCSS_(statistical_software))
- [Nominal type system](https://en.wikipedia.org/wiki/Nominal_type_system)
- [Non-English-based programming languages](https://en.wikipedia.org/wiki/Non-English-based_programming_languages)
- [Object Pascal](https://en.wikipedia.org/wiki/Object_Pascal)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [OpenBUGS](https://en.wikipedia.org/wiki/OpenBUGS)
- [OpenFOAM](https://en.wikipedia.org/wiki/OpenFOAM)
- [Open source](https://en.wikipedia.org/wiki/Open_source)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Operator overloading](https://en.wikipedia.org/wiki/Operator_overloading)
- [Orange (software)](https://en.wikipedia.org/wiki/Orange_(software))
- [OxMetrics](https://en.wikipedia.org/wiki/OxMetrics)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PSPP](https://en.wikipedia.org/wiki/PSPP)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)
- [Project Jupyter](https://en.wikipedia.org/wiki/Project_Jupyter)
- [Prolog](https://en.wikipedia.org/wiki/Prolog)
- [Public-domain software](https://en.wikipedia.org/wiki/Public-domain_software)
- [PyMC](https://en.wikipedia.org/wiki/PyMC)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python syntax and semantics](https://en.wikipedia.org/wiki/Python_syntax_and_semantics)
- [RATS (software)](https://en.wikipedia.org/wiki/RATS_(software))
- [RExcel](https://en.wikipedia.org/wiki/RExcel)
- [RStudio](https://en.wikipedia.org/wiki/RStudio)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Revolution Analytics](https://en.wikipedia.org/wiki/Revolution_Analytics)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [S-PLUS](https://en.wikipedia.org/wiki/S-PLUS)
- [SAS (software)](https://en.wikipedia.org/wiki/SAS_(software))
- [Shazam (econometrics software)](https://en.wikipedia.org/wiki/Shazam_(econometrics_software))
- [SOFA Statistics](https://en.wikipedia.org/wiki/SOFA_Statistics)
- [SPSS](https://en.wikipedia.org/wiki/SPSS)
- [SPSS Modeler](https://en.wikipedia.org/wiki/SPSS_Modeler)
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [SUDAAN](https://en.wikipedia.org/wiki/SUDAAN)
- [SYSTAT (statistics package)](https://en.wikipedia.org/wiki/SYSTAT_(statistics_package))
- [SageMath](https://en.wikipedia.org/wiki/SageMath)
- [Salome (software)](https://en.wikipedia.org/wiki/Salome_(software))
- [ScicosLab](https://en.wikipedia.org/wiki/ScicosLab)
- [Scilab](https://en.wikipedia.org/wiki/Scilab)
- [Scratch (programming language)](https://en.wikipedia.org/wiki/Scratch_(programming_language))
- [SegReg](https://en.wikipedia.org/wiki/SegReg)
- [Shell script](https://en.wikipedia.org/wiki/Shell_script)
- [SigmaStat](https://en.wikipedia.org/wiki/SigmaStat)
- [SimFiT](https://en.wikipedia.org/wiki/SimFiT)
- [Simula](https://en.wikipedia.org/wiki/Simula)
- [Single instruction, multiple data](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data)
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [SmartPLS](https://en.wikipedia.org/wiki/SmartPLS)
- [Software architect](https://en.wikipedia.org/wiki/Software_architect)
- [Software design](https://en.wikipedia.org/wiki/Software_design)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software framework](https://en.wikipedia.org/wiki/Software_framework)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Source-code compatibility](https://en.wikipedia.org/wiki/Source-code_compatibility)
- [Speakeasy (computational environment)](https://en.wikipedia.org/wiki/Speakeasy_(computational_environment))
- [Stan (software)](https://en.wikipedia.org/wiki/Stan_(software))
- [Standard library](https://en.wikipedia.org/wiki/Standard_library)
- [StatView](https://en.wikipedia.org/wiki/StatView)
- [StatXact](https://en.wikipedia.org/wiki/StatXact)
- [Stata](https://en.wikipedia.org/wiki/Stata)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Statistica](https://en.wikipedia.org/wiki/Statistica)
- [StatsDirect](https://en.wikipedia.org/wiki/StatsDirect)
- [Strong and weak typing](https://en.wikipedia.org/wiki/Strong_and_weak_typing)
- [Subset](https://en.wikipedia.org/wiki/Subset)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar)
- [Syntax (programming languages)](https://en.wikipedia.org/wiki/Syntax_(programming_languages))
- [System programming language](https://en.wikipedia.org/wiki/System_programming_language)
- [TSP (econometrics software)](https://en.wikipedia.org/wiki/TSP_(econometrics_software))
- [Tensor Processing Unit](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)
- [The Unscrambler](https://en.wikipedia.org/wiki/The_Unscrambler)
- [Timeline of programming languages](https://en.wikipedia.org/wiki/Timeline_of_programming_languages)
- [Type inference](https://en.wikipedia.org/wiki/Type_inference)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu)
- [Unicode](https://en.wikipedia.org/wiki/Unicode)
- [VisSim](https://en.wikipedia.org/wiki/VisSim)
- [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic)
- [Visual Basic (.NET)](https://en.wikipedia.org/wiki/Visual_Basic_(.NET))
- [Visual Basic (classic)](https://en.wikipedia.org/wiki/Visual_Basic_(classic))
- [Weka (software)](https://en.wikipedia.org/wiki/Weka_(software))
- [WinBUGS](https://en.wikipedia.org/wiki/WinBUGS)
- [Wolfram Mathematica](https://en.wikipedia.org/wiki/Wolfram_Mathematica)
- [World Programming System](https://en.wikipedia.org/wiki/World_Programming_System)
- [X-13ARIMA-SEATS](https://en.wikipedia.org/wiki/X-13ARIMA-SEATS)
- [X10 (programming language)](https://en.wikipedia.org/wiki/X10_(programming_language))
- [XLfit](https://en.wikipedia.org/wiki/XLfit)
- [XLispStat](https://en.wikipedia.org/wiki/XLispStat)
- [XploRe](https://en.wikipedia.org/wiki/XploRe)
- [Zig (programming language)](https://en.wikipedia.org/wiki/Zig_(programming_language))
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Template:Numerical analysis software](https://en.wikipedia.org/wiki/Template:Numerical_analysis_software)
- [Template:Programming languages](https://en.wikipedia.org/wiki/Template:Programming_languages)
- [Template:Statistical software](https://en.wikipedia.org/wiki/Template:Statistical_software)
- [Template talk:Numerical analysis software](https://en.wikipedia.org/wiki/Template_talk:Numerical_analysis_software)
- [Template talk:Programming languages](https://en.wikipedia.org/wiki/Template_talk:Programming_languages)
- [Template talk:Statistical software](https://en.wikipedia.org/wiki/Template_talk:Statistical_software)
- [Category:Articles containing potentially dated statements from 2024](https://en.wikipedia.org/wiki/Category:Articles_containing_potentially_dated_statements_from_2024)
- [Category:Articles with unsourced statements from October 2023](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_October_2023)
- [Category:Programming languages](https://en.wikipedia.org/wiki/Category:Programming_languages)
- [Category:Statistical software](https://en.wikipedia.org/wiki/Category:Statistical_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:19:27.908356+00:00_