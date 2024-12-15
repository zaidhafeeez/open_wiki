# Python (programming language)

## Article Metadata

- **Last Updated:** 2024-12-15T04:44:40.252691+00:00
- **Original Article:** [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- **Language:** en
- **Page ID:** 23862

## Summary

Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.
Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.
Guido van Rossum began working on Python in the late 

## Categories

- Category:All Wikipedia articles written in American English
- Category:All articles containing potentially dated statements
- Category:Articles containing potentially dated statements from 2008
- Category:Articles containing potentially dated statements from 2020
- Category:Articles containing potentially dated statements from December 2022
- Category:Articles containing potentially dated statements from March 2024
- Category:Articles containing potentially dated statements from October 2024
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Class-based programming languages
- Category:Computer science in the Netherlands
- Category:Concurrent programming languages
- Category:Cross-platform free software
- Category:Cross-platform software
- Category:Dutch inventions
- Category:Dynamically typed programming languages
- Category:Educational programming languages
- Category:High-level programming languages
- Category:Information technology in the Netherlands
- Category:Multi-paradigm programming languages
- Category:Notebook interface
- Category:Object-oriented programming languages
- Category:Pages using Sister project links with hidden wikidata
- Category:Pages using Sister project links with wikidata namespace mismatch
- Category:Pages with broken reference names
- Category:Pages with reference errors
- Category:Pattern matching programming languages
- Category:Programming languages
- Category:Programming languages created in 1991
- Category:Python (programming language)
- Category:Scripting languages
- Category:Short description matches Wikidata
- Category:Text-oriented programming languages
- Category:Use American English from December 2024
- Category:Use dmy dates from November 2021

## Table of Contents

- History
- Design philosophy and features
- Syntax and semantics
- Programming examples
- Libraries
- Development environments
- Implementations
- Development
- API documentation generators
- Naming
- Popularity
- Uses
- Languages influenced by Python
- See also
- References
- Further reading
- External links

## Content

Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.
Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.
Python consistently ranks as one of the most popular programming languages, and has gained widespread use in the machine learning community.

History
Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL, capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's "benevolent dictator for life" (BDFL), a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker (he has since come out of retirement and is self-titled "BDFL-emeritus"). In January 2019, active Python core developers elected a five-member Steering Council to lead the project.
The name Python is said to come from the British comedy series Monty Python's Flying Circus.
Python 2.0 was released on 16 October 2000, with many major new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 2.7's end-of-life was initially set for 2015, then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3. No further security patches or other improvements will be released for it. While Python 2.7 and older versions are officially unsupported, a different unofficial Python implementation, PyPy, continues to support Python 2, i.e. "2.7.18+" (plus 3.10), with the plus meaning (at least some) "backported security updates".
Python 3.0 was released on 3 December 2008, with some new semantics and changed syntax. At least every Python release since (now unsupported) 3.5 has added some syntax to the language, and a few later releases have dropped outdated modules, or changed semantics, at least in a minor way.
Since 7 October 2024, Python 3.13 is the latest stable release, and it and, for few more months, 3.12 are the only releases with active support including for bugfixes (as opposed to just for security) and Python 3.9, is the oldest supported version of Python (albeit in the 'security support' phase), due to Python 3.8 reaching end-of-life. Starting with 3.13, it and later versions have 2 years of full support (up from one and a half), followed by 3 years of security support (for same total support as before).
Security updates were expedited in 2021 (and again twice in 2022, and more fixed in 2023 and in September 2024 for Python 3.12.6 down to 3.8.20), since all Python versions were insecure (including 2.7) because of security issues leading to possible remote code execution and web-cache poisoning.   
Python 3.10 added the | union type operator and the match and case keywords (for structural pattern matching statements). 3.11 expanded exception handling functionality. Python 3.12 added the new keyword type. Notable changes in 3.11 from 3.10 include increased program execution speed and improved error reporting. Python 3.11 claims to be between 10 and 60% faster than Python 3.10, and Python 3.12 adds another 5% on top of that. It also has improved error messages (again improved in 3.14), and many other changes.
Python 3.13 introduces more syntax for types, a new and improved interactive interpreter (REPL), featuring multi-line editing and color support; an incremental garbage collector (producing shorter pauses for collection in programs with a lot of objects, and addition to the improved speed in 3.11 and 3.12),  and an experimental just-in-time (JIT) compiler (such features, can/needs to be enabled specifically for the increase in speed), and an experimental free-threaded build mode, which disables the global interpreter lock (GIL), allowing threads to run more concurrently, that latter feature enabled with python3.13t or python3.13t.exe.
Python 3.13 introduces some change in behavior, i.e. new "well-defined semantics", fixing bugs (plus many removals of deprecated classes, functions and methods, and removed some of the C API and outdated modules): "The  [old] implementation of locals() and frame.f_locals is slow, inconsistent and buggy [and it] has many corner cases and oddities. Code that works around those may need to be changed. Code that uses locals() for simple templating, or print debugging, will continue to work correctly."
Some (more) standard library modules and many deprecated classes, functions and methods, will be removed in Python 3.15 or 3.16.
Python 3.14 is now in alpha 2; regarding possible change to annotations: "In Python 3.14, from __future__ import annotations will continue to work as it did before, converting annotations into strings."  
PEP 711 proposes PyBI: a standard format for distributing Python Binaries.
Python 3.15 will "Make UTF-8 mode default", the mode exists in all current Python versions, but currently needs to be opted into. UTF-8 is already used, by default, on Windows (and elsewhere), for most things, but e.g. to open files it's not and enabling also makes code fully cross-platform, i.e. use UTF-8 for everything on all platforms.

Design philosophy and features
Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported, and many of their features support functional programming and aspect-oriented programming (including metaprogramming and metaobjects). Many other paradigms are supported via extensions, including design by contract and logic programming. Python is known as a glue language, able to work very well with many other languages with ease of access.
Python uses dynamic typing and a combination of reference counting and a cycle-detecting garbage collector for memory management. It uses dynamic name resolution (late binding), which binds method and variable names during program execution.
Its design offers some support for functional programming in the Lisp tradition. It has filter,mapandreduce functions; list comprehensions, dictionaries, sets, and generator expressions. The standard library has two modules (itertools and functools) that implement functional tools borrowed from Haskell and Standard ML.
Its core philosophy is summarized in the Zen of Python (PEP 20), which includes aphorisms such as:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Readability counts.
However, Python features regularly violate these principles and have received criticism for adding unnecessary language bloat. Responses to these criticisms are that the Zen of Python is a guideline rather than a rule. The addition of some new features had been so controversial that Guido van Rossum resigned as Benevolent Dictator for Life following vitriol over the addition of the assignment expression operator in Python 3.8.
Nevertheless, rather than building all of its functionality into its core, Python was designed to be highly extensible via modules. This compact modularity has made it particularly popular as a means of adding programmable interfaces to existing applications. Van Rossum's vision of a small core language with a large standard library and easily extensible interpreter stemmed from his frustrations with ABC, which espoused the opposite approach.
Python claims to strive for a simpler, less-cluttered syntax and grammar while giving developers a choice in their coding methodology. In contrast to Perl's "there is more than one way to do it" motto, Python embraces a "there should be one—and preferably only one—obvious way to do it." philosophy. In practice, however, Python provides many ways to achieve the same task. There are, for example, at least three ways to format a string literal, with no certainty as to which one a programmer should use. Alex Martelli, a Fellow at the Python Software Foundation and Python book author, wrote: "To describe something as 'clever' is not considered a compliment in the Python culture."
Python's developers usually strive to avoid premature optimization and reject patches to non-critical parts of the CPython reference implementation that would offer marginal increases in speed at the cost of clarity. Execution speed can be improved by moving speed-critical functions to extension modules written in languages such as C, or by using a just-in-time compiler like PyPy. It is also possible to cross-compile to other languages, but it either doesn't provide the full speed-up that might be expected, since Python is a very dynamic language, or a restricted subset of Python is compiled, and possibly semantics are slightly changed.
Python's developers aim for it to be fun to use. This is reflected in its name—a tribute to the British comedy group Monty Python—and in occasionally playful approaches to tutorials and reference materials, such as the use of the terms "spam" and "eggs" (a reference to a Monty Python sketch) in examples, instead of the often-used "foo" and "bar". A common neologism in the Python community is pythonic, which has a wide range of meanings related to program style. "Pythonic" code may use Python idioms well, be natural or show fluency in the language, or conform with Python's minimalist philosophy and emphasis on readability. Code that is difficult to understand or reads like a rough transcription from another programming language is called unpythonic.

Syntax and semantics
Python is meant to be an easily readable language. Its formatting is visually uncluttered and often uses English keywords where other languages use punctuation. Unlike many other languages, it does not use curly brackets to delimit blocks, and semicolons after statements are allowed but rarely used. It has fewer syntactic exceptions and special cases than C or Pascal.

Indentation
Python uses whitespace indentation, rather than curly brackets or keywords, to delimit blocks. An increase in indentation comes after certain statements; a decrease in indentation signifies the end of the current block. Thus, the program's visual structure accurately represents its semantic structure. This feature is sometimes termed the off-side rule. Some other languages use indentation this way; but in most, indentation has no semantic meaning. The recommended indent size is four spaces.

Statements and control flow
Python's statements include:

The assignment statement, using a single equals sign =
The if statement, which conditionally executes a block of code, along with else and elif (a contraction of else-if)
The for statement, which iterates over an iterable object, capturing each element to a local variable for use by the attached block
The while statement, which executes a block of code as long as its condition is true
The try statement, which allows exceptions raised in its attached code block to be caught and handled by except clauses (or new syntax except* in Python 3.11 for exception groups); it also ensures that clean-up code in a finally block is always run regardless of how the block exits
The raise statement, used to raise a specified exception or re-raise a caught exception
The class statement, which executes a block of code and attaches its local namespace to a class, for use in object-oriented programming
The def statement, which defines a function or method
The with statement, which encloses a code block within a context manager (for example, acquiring a lock before it is run, then releasing the lock; or opening and closing a file), allowing resource-acquisition-is-initialization (RAII)-like behavior and replacing a common try/finally idiom
The break statement, which exits a loop
The continue statement, which skips the rest of the current iteration and continues with the next
The del statement, which removes a variable—deleting the reference from the name to the value, and producing an error if the variable is referred to before it is redefined
The pass statement, serving as a NOP, syntactically needed to create an empty code block
The assert statement, used in debugging to check for conditions that should apply
The yield statement, which returns a value from a generator function (and also an operator); used to implement coroutines
The return statement, used to return a value from a function
The import and from statements, used to import modules whose functions or variables can be used in the current program
The match and case statements, an analog of the switch statement construct, that compares an expression against one or more cases as a control-of-flow measure.
The assignment statement (=) binds a name as a reference to a separate, dynamically allocated object. Variables may subsequently be rebound at any time to any object. In Python, a variable name is a generic reference holder without a fixed data type; however, it always refers to some object with a type. This is called dynamic typing—in contrast to statically-typed languages, where each variable may contain only a value of a certain type.
Python does not support tail call optimization or first-class continuations, and, according to Van Rossum, it never will. However, better support for coroutine-like functionality is provided by extending Python's generators. Before 2.5, generators were lazy iterators; data was passed unidirectionally out of the generator. From Python 2.5 on, it is possible to pass data back into a generator function; and from version 3.3, it can be passed through multiple stack levels.

Expressions
Python's expressions include:

The +, -, and * operators for mathematical addition, subtraction, and multiplication are similar to other languages, but the behavior of division differs. There are two types of divisions in Python: floor division (or integer division) // and floating-point/division. Python uses the ** operator for exponentiation.
Python uses the + operator for string concatenation. Python uses the * operator for duplicating a string a specified number of times.
The @ infix operator is intended to be used by libraries such as NumPy for matrix multiplication.
The syntax :=, called the "walrus operator", was introduced in Python 3.8. It assigns values to variables as part of a larger expression.
In Python, == compares by value. Python's is operator may be used to compare object identities (comparison by reference), and comparisons may be chained—for example, a <= b <= c.
Python uses and, or, and not as Boolean operators.
Python has a type of expression named a list comprehension, and a more general expression named a generator expression.
Anonymous functions are implemented using lambda expressions; however, there may be only one expression in each body.
Conditional expressions are written as x if c else y (different in order of operands from the c ? x : y operator common to many other languages).
Python makes a distinction between lists and tuples. Lists are written as [1, 2, 3], are mutable, and cannot be used as the keys of dictionaries (dictionary keys must be immutable in Python). Tuples, written as (1, 2, 3), are immutable and thus can be used as keys of dictionaries, provided all of the tuple's elements are immutable. The + operator can be used to concatenate two tuples, which does not directly modify their contents, but produces a new tuple containing the elements of both. Thus, given the variable t initially equal to (1, 2, 3), executing t = t + (4, 5) first evaluates t + (4, 5), which yields (1, 2, 3, 4, 5), which is then assigned back to t—thereby effectively "modifying the contents" of t while conforming to the immutable nature of tuple objects. Parentheses are optional for tuples in unambiguous contexts.
Python features sequence unpacking where multiple expressions, each evaluating to anything that can be assigned (to a variable, writable property, etc.) are associated in an identical manner to that forming tuple literals—and, as a whole, are put on the left-hand side of the equal sign in an assignment statement. The statement expects an iterable object on the right-hand side of the equal sign that produces the same number of values as the provided writable expressions; when iterated through them, it assigns each of the produced values to the corresponding expression on the left.
Python has a "string format" operator % that functions analogously to printf format strings in C—e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2". In Python 2.6+ and 3+, this was supplemented by the format() method of the str class, e.g. "spam={0} eggs={1}".format("blah", 2). Python 3.6 added "f-strings": spam = "blah"; eggs = 2; f'spam={spam} eggs={eggs}'.
Strings in Python can be concatenated by "adding" them (with the same operator as for adding integers and floats), e.g. "spam" + "eggs" returns "spameggs". If strings contain numbers, they are added as strings rather than integers, e.g. "2" + "2" returns "22".
Python has various string literals:
Delimited by single or double quotes; unlike in Unix shells, Perl, and Perl-influenced languages, single and double quotes work the same. Both use the backslash (\) as an escape character. String interpolation became available in Python 3.6 as "formatted string literals".
Triple-quoted (beginning and ending with three single or double quotes), which may span multiple lines and function like here documents in shells, Perl, and Ruby.
Raw string varieties, denoted by prefixing the string literal with r. Escape sequences are not interpreted; hence raw strings are useful where literal backslashes are common, such as regular expressions and Windows-style paths. (Compare "@-quoting" in C#.)
Python has array index and array slicing expressions in lists, denoted as a[key], a[start:stop] or a[start:stop:step]. Indexes are zero-based, and negative indexes are relative to the end. Slices take elements from the start index up to, but not including, the stop index. The third slice parameter, called step or stride, allows elements to be skipped and reversed. Slice indexes may be omitted—for example, a[:] returns a copy of the entire list. Each element of a slice is a shallow copy.
In Python, a distinction between expressions and statements is rigidly enforced, in contrast to languages such as Common Lisp, Scheme, or Ruby. This leads to duplicating some functionality. For example:

List comprehensions vs. for-loops
Conditional expressions vs. if blocks
The eval() vs. exec() built-in functions (in Python 2, exec is a statement); the former is for expressions, the latter is for statements
Statements cannot be a part of an expression—so list and other comprehensions or lambda expressions, all being expressions, cannot contain statements. A particular case is that an assignment statement such as a = 1 cannot form part of the conditional expression of a conditional statement.

Methods
Methods on objects are functions attached to the object's class; the syntax instance.method(argument) is, for normal methods and functions, syntactic sugar for Class.method(instance, argument). Python methods have an explicit self parameter to access instance data, in contrast to the implicit self (or this) in some other object-oriented programming languages (e.g., C++, Java, Objective-C, Ruby). Python also provides methods, often called dunder methods (due to their names beginning and ending with double-underscores), to allow user-defined classes to modify how they are handled by native operations including length, comparison, in arithmetic operations and type conversion.

Typing
Python uses duck typing and has typed objects but untyped variable names. Type constraints are not checked at compile time; rather, operations on an object may fail, signifying that it is not of a suitable type. Despite being dynamically typed, Python is strongly typed, forbidding operations that are not well-defined (for example, adding a number to a string) rather than silently attempting to make sense of them.
Python allows programmers to define their own types using classes, most often used for object-oriented programming. New instances of classes are constructed by calling the class (for example, SpamClass() or EggsClass()), and the classes are instances of the metaclass type (itself an instance of itself), allowing metaprogramming and reflection.
Before version 3.0, Python had two kinds of classes (both using the same syntax):  old-style and new-style; current Python versions only support the semantics of the new style.
Python supports optional type annotations. These annotations are not enforced by the language, but may be used by external tools such as mypy to catch errors. Mypy also supports a Python compiler called mypyc, which leverages type annotations for optimization.

Arithmetic operations
Python has the usual symbols for arithmetic operators (+, -, *, /), the floor division operator // and the modulo operation % (where the remainder can be negative, e.g. 4 % -3 == -2). It also has ** for exponentiation, e.g. 5**3 == 125 and 9**0.5 == 3.0, and a matrix‑multiplication operator @ . These operators work like in traditional math; with the same precedence rules, the operators infix (+ and - can also be unary to represent positive and negative numbers respectively).
The division between integers produces floating-point results. The behavior of division has changed significantly over time:

Current Python (i.e. since 3.0) changed / to always be floating-point division, e.g. 5/2 == 2.5.
The floor division // operator was introduced. So 7//3 == 2, -7//3 == -3, 7.5//3 == 2.0 and -7.5//3 == -3.0. Adding from __future__ import division causes a module used in Python 2.7 to use Python 3.0 rules for division (see above).
In Python terms, / is true division (or simply division), and // is floor division. / before version 3.0 is classic division.
Rounding towards negative infinity, though different from most languages, adds consistency. For instance, it means that the equation (a + b)//b == a//b + 1 is always true. It also means that the equation b*(a//b) + a%b == a is valid for both positive and negative values of a. However, maintaining the validity of this equation means that while the result of a%b is, as expected, in the half-open interval [0, b), where b is a positive integer, it has to lie in the interval (b, 0] when b is negative.
Python provides a round function for rounding a float to the nearest integer. For tie-breaking, Python 3 uses round to even: round(1.5) and round(2.5) both produce 2. Versions before 3 used round-away-from-zero: round(0.5) is 1.0, round(-0.5) is −1.0.
Python allows Boolean expressions with multiple equality relations in a manner that is consistent with general use in mathematics. For example, the expression a < b < c tests whether a is less than b and b is less than c. C-derived languages interpret this expression differently: in C, the expression would first evaluate a < b, resulting in 0 or 1, and that result would then be compared with c.
Python uses arbitrary-precision arithmetic for all integer operations. The Decimal type/class in the decimal module provides decimal floating-point numbers to a pre-defined arbitrary precision and several rounding modes. The Fraction class in the fractions module provides arbitrary precision for rational numbers.
Due to Python's extensive mathematics library, and the third-party library NumPy that further extends the native capabilities, it is frequently used as a scientific scripting language to aid in problems such as numerical data processing and manipulation.

Function syntax
Functions are created in Python using the def keyword. In Python, you define the function as if you were calling it, by typing the function name and then the attributes required. Here is an example of a function that will print whatever is given:If you want the attribute to have a set value if no value is given, use the variable-defining syntax inside the function definition.

Programming examples
"Hello, World!" program:

Program to calculate the factorial of a positive integer:

Libraries
Python's large standard library provides tools suited to many tasks and is commonly cited as one of its greatest strengths. For Internet-facing applications, many standard formats and protocols such as MIME and HTTP are supported. It includes modules for creating graphical user interfaces, connecting to relational databases, generating pseudorandom numbers, arithmetic with arbitrary-precision decimals, manipulating regular expressions, and unit testing.
Some parts of the standard library are covered by specifications—for example, the Web Server Gateway Interface (WSGI) implementation wsgiref follows PEP 333—but most are specified by their code, internal documentation, and test suites. However, because most of the standard library is cross-platform Python code, only a few modules need altering or rewriting for variant implementations.
As of 17 March 2024, the Python Package Index (PyPI), the official repository for third-party Python software, contains over 523,000 packages with a wide range of functionality, including:

Development environments
Most Python implementations (including CPython) include a read–eval–print loop (REPL), permitting them to function as a command line interpreter for which users enter statements sequentially and receive results immediately.
Python also comes with an Integrated development environment (IDE) called IDLE, which is more beginner-oriented.
Other shells, including IDLE and IPython, add further abilities such as improved auto-completion, session state retention, and syntax highlighting.
As well as standard desktop integrated development environments including PyCharm, IntelliJ Idea, Visual Studio Code etc, there are web browser-based IDEs, including SageMath, for developing science- and math-related programs; PythonAnywhere, a browser-based IDE and hosting environment; and Canopy IDE, a commercial IDE emphasizing scientific computing.

Implementations
Reference implementation
CPython is the reference implementation of Python. It is written in C, meeting the C89 standard (Python 3.11 uses C11) with several select C99 features. CPython includes its own C extensions, but third-party extensions are not limited to older C versions—e.g. they can be implemented with C11 or C++. CPython compiles Python programs into an intermediate bytecode which is then executed by its virtual machine. CPython is distributed with a large standard library written in a mixture of C and native Python, and is available for many platforms, including Windows (starting with Python 3.9, the Python installer deliberately fails to install on Windows 7 and 8; Windows XP was supported until Python 3.5) and most modern Unix-like systems, including macOS (and Apple M1 Macs, since Python 3.9.1, with experimental installer), with unofficial support for VMS. Platform portability was one of its earliest priorities. (During Python 1 and 2 development, even OS/2 and Solaris were supported, but support has since been dropped for many platforms.)
All current Python versions (i.e. since 3.7) only support operating systems with multi-threading support.

Other implementations
All alternative implementations have at least slightly different semantics (e.g. may have unordered dictionaries, unlike all current Python versions), e.g. with the larger Python ecosystem, such as with supporting the C Python API of with PyPy:

PyPy is a fast, compliant interpreter of Python 2.7 and  3.10. Its just-in-time compiler often brings a significant speed improvement over CPython, but some libraries written in C cannot be used with it. It has e.g. RISC-V support.
Codon is a language with an ahead-of-time (AOT) compiler, that (AOT) compiles a statically-typed Python-like language with "syntax and semantics are nearly identical to Python's, there are some notable differences" e.g. it uses 64-bit machine integers, for speed, not arbitrary like Python, and it claims speedups over CPython are usually on the order of 10–100x. It compiles to machine code (via LLVM) and supports native multithreading.  Codon can also compile to Python extension modules that can be imported and used from Python.
Stackless Python is a significant fork of CPython that implements microthreads; it does not use the call stack in the same way, thus allowing massively concurrent programs. PyPy also has a stackless version.
MicroPython and CircuitPython are Python 3 variants optimized for microcontrollers, including Lego Mindstorms EV3.
Pyston is a variant of the Python runtime that uses just-in-time compilation to speed up the execution of Python programs.
Cinder is a performance-oriented fork of CPython 3.8 that contains a number of optimizations, including bytecode inline caching, eager evaluation of coroutines, a method-at-a-time JIT, and an experimental bytecode compiler.
Snek Embedded Computing Language (compatible with e.g. 8-bit AVR microcontrollers such as ATmega 328P-based Arduino, as well as larger ones compatible with MicroPython) "is Python-inspired, but it is not Python. It is possible to write Snek programs that run under a full Python system, but most Python programs will not run under Snek." It is an imperative language not including OOP / classes, unlike Python, and simplifying to one number type with 32-bit single-precision (similar to JavaScript, except smaller).

No longer supported implementations
Other just-in-time Python compilers have been developed, but are now unsupported:

Google began a project named Unladen Swallow in 2009, with the aim of speeding up the Python interpreter five-fold by using the LLVM, and of improving its multithreading ability to scale to thousands of cores, while ordinary implementations suffer from the global interpreter lock.
Psyco is a discontinued just-in-time specializing compiler that integrates with CPython and transforms bytecode to machine code at runtime. The emitted code is specialized for certain data types and is faster than the standard Python code. Psyco does not support Python 2.7 or later.
PyS60 was a Python 2 interpreter for Series 60 mobile phones released by Nokia in 2005. It implemented many of the modules from the standard library and some additional modules for integrating with the Symbian operating system. The Nokia N900 also supports Python with GTK widget libraries, enabling programs to be written and run on the target device.

Cross-compilers to other languages
There are several compilers/transpilers to high-level object languages, with either unrestricted Python, a restricted subset of Python, or a language similar to Python as the source language:

Brython, Transcrypt and Pyjs (latest release in 2012) compile Python to JavaScript.
Cython compiles (a superset of) Python to C. The resulting code is also usable with Python via direct C-level API calls into the Python interpreter.
PyJL compiles/transpiles a subset of Python to "human-readable, maintainable, and high-performance Julia source code". Despite claiming high performance, no tool can claim to do that for arbitrary Python code; i.e. it's known not possible to compile to a faster language or machine code. Unless semantics of Python are changed, but in many cases speedup is possible with few or no changes in the Python code. The faster Julia source code can then be used from Python, or compiled to machine code, and based that way.
Nuitka compiles Python into C. It works with Python 3.4 to 3.12 (and 2.6 and 2.7), for Python's main supported platforms (and Windows 7 or even Windows XP) and for Android. It claims complete support for Python 3.10,  some support for 3.11 and 3.12  and experimental support for Python 3.13. It supports macOS including Apple Silicon-based.  It's a free compiler, though it also has commercial add-ons (e.g. for hiding source code).
Numba is used from Python, as a tool (enabled by adding a decorator to relevant Python code), a JIT compiler that translates a subset of Python and NumPy code into fast machine code.
Pythran compiles a subset of Python 3 to C++ (C++11).
RPython can be compiled to C, and is used to build the PyPy interpreter of Python.
The Python → 11l → C++ transpiler compiles a subset of Python 3 to C++ (C++17).
Specialized:

MyHDL is a Python-based hardware description language (HDL), that converts MyHDL code to Verilog or VHDL code.
Older projects (or not to be used with Python 3.x and latest syntax):

Google's Grumpy (latest release in 2017) transpiles Python 2 to Go.
IronPython allows running Python 2.7 programs (and an alpha, released in 2021, is also available for "Python 3.4, although features and behaviors from later versions may be included") on the .NET Common Language Runtime.
Jython compiles Python 2.7 to Java bytecode, allowing the use of the Java libraries from a Python program.
Pyrex (latest release in 2010) and Shed Skin (latest release in 2013) compile to C and C++ respectively.

Performance
Performance comparison of various Python implementations on a non-numerical (combinatorial) workload was presented at EuroSciPy '13. Python's performance compared to other programming languages is also benchmarked by The Computer Language Benchmarks Game.

Development
Python's development is conducted largely through the Python Enhancement Proposal (PEP) process, the primary mechanism for proposing major new features, collecting community input on issues, and documenting Python design decisions. Python coding style is covered in PEP 8. Outstanding PEPs are reviewed and commented on by the Python community and the steering council.
Enhancement of the language corresponds with the development of the CPython reference implementation. The mailing list python-dev is the primary forum for the language's development. Specific issues were originally discussed in the Roundup bug tracker hosted at by the foundation. In 2022, all issues and discussions were migrated to GitHub. Development originally took place on a self-hosted source-code repository running Mercurial, until Python moved to GitHub in January 2017.
CPython's public releases come in three types, distinguished by which part of the version number is incremented:

Backward-incompatible versions, where code is expected to break and needs to be manually ported. The first part of the version number is incremented. These releases happen infrequently—version 3.0 was released 8 years after 2.0. According to Guido van Rossum, a version 4.0 is very unlikely to ever happen.
Major or "feature" releases are largely compatible with the previous version but introduce new features. The second part of the version number is incremented. Starting with Python 3.9, these releases are expected to happen annually. Each major version is supported by bug fixes for several years after its release.
Bugfix releases, which introduce no new features, occur about every 3 months and are made when a sufficient number of bugs have been fixed upstream since the last release. Security vulnerabilities are also patched in these releases. The third and final part of the version number is incremented.
Many alpha, beta, and release-candidates are also released as previews and for testing before final releases. Although there is a rough schedule for each release, they are often delayed if the code is not ready. Python's development team monitors the state of the code by running the large unit test suite during development.
The major academic conference on Python is PyCon. There are also special Python mentoring programs, such as PyLadies.
Python 3.12 removed wstr meaning Python extensions need to be modified, and 3.10 added pattern matching to the language.
Python 3.12 dropped some outdated modules, and more will be dropped in the future, deprecated as of 3.13; already deprecated array 'u' format code will emit DeprecationWarning since 3.13 and will be removed in Python 3.16. The 'w' format code should be used instead. Part of ctypes is also deprecated and http.server.CGIHTTPRequestHandler will emit a DeprecationWarning, and will be removed in 3.15. Using that code already has a high potential for both security and functionality bugs. Parts of the typing module are deprecated, e.g. creating a typing.NamedTuple class using keyword arguments to denote the fields and such (and more) will be disallowed in Python 3.15.

API documentation generators
Tools that can generate documentation for Python API include pydoc (available as part of the standard library), Sphinx, Pdoc and its forks, Doxygen and Graphviz, among others.

Naming
Python's name is derived from the British comedy group Monty Python, whom Python creator Guido van Rossum enjoyed while developing the language. Monty Python references appear frequently in Python code and culture; for example, the metasyntactic variables often used in Python literature are spam and eggs instead of the traditional foo and bar. The official Python documentation also contains various references to Monty Python routines. Users of Python are sometimes referred to as "Pythonistas".
The prefix Py- is used to show that something is related to Python. Examples of the use of this prefix in names of Python applications or libraries include Pygame, a binding of Simple DirectMedia Layer to Python (commonly used to create games); PyQt and PyGTK, which bind Qt and GTK to Python respectively; and PyPy, a Python implementation originally written in Python.

Popularity
Since 2003, Python has consistently ranked in the top ten most popular programming languages in the TIOBE Programming Community Index where as of December 2022 it was the most popular language (ahead of C, C++, and Java). It was selected as Programming Language of the Year (for "the highest rise in ratings in a year") in 2007, 2010, 2018, and 2020 (the only language to have done so four times as of 2020).
Large organizations that use Python include Wikipedia, Google, Yahoo!, CERN, NASA, Facebook, Amazon, Instagram, Spotify, and some smaller entities like Industrial Light & Magic and ITA. The social news networking site Reddit was written mostly in Python. Organizations that partially use Python include Discord and Baidu.

Uses
Python can serve as a scripting language for web applications, e.g. via mod_wsgi for the Apache webserver. With Web Server Gateway Interface, a standard API has evolved to facilitate these applications. Web frameworks like Django, Pylons, Pyramid, TurboGears, web2py, Tornado, Flask, Bottle, and Zope support developers in the design and maintenance of complex applications. Pyjs and IronPython can be used to develop the client-side of Ajax-based applications. SQLAlchemy can be used as a data mapper to a relational database. Twisted is a framework to program communications between computers, and is used (for example) by Dropbox.
Libraries such as NumPy, SciPy and Matplotlib allow the effective use of Python in scientific computing, with specialized libraries such as Biopython and Astropy providing domain-specific functionality. SageMath is a computer algebra system with a notebook interface programmable in Python: its library covers many aspects of mathematics, including algebra, combinatorics, numerical mathematics, number theory, and calculus. OpenCV has Python bindings with a rich set of features for computer vision and image processing.
Python is commonly used in artificial intelligence projects and machine learning projects with the help of libraries like TensorFlow, Keras, Pytorch, scikit-learn and the Logic language ProbLog. As a scripting language with a modular architecture, simple syntax, and rich text processing tools, Python is often used for natural language processing.
The combination of Python and Prolog has proved to be particularly useful for AI applications, with Prolog providing knowledge representation and reasoning capabilities. The Janus system, in particular, exploits the similarities between these two languages,
in part because of their use of dynamic typing, and the simple recursive nature of their
data structures. Typical applications of this combination include  natural language processing, visual query
answering, geospatial reasoning, and handling of semantic web data.
The Natlog system, implemented in Python, uses Definite Clause Grammars (DCGs) as prompt generators for text-to-text generators like GPT3 and text-to-image generators like DALL-E or Stable Diffusion.
Python can also be used for graphical user interface (GUI) by using libraries like Tkinter.
Python has been successfully embedded in many software products as a scripting language, including in finite element method software such as Abaqus, 3D parametric modelers like FreeCAD, 3D animation packages such as 3ds Max, Blender, Cinema 4D, Lightwave, Houdini, Maya, modo, MotionBuilder, Softimage, the visual effects compositor Nuke, 2D imaging programs like GIMP, Inkscape, Scribus and Paint Shop Pro, and musical notation programs like scorewriter and capella. GNU Debugger uses Python as a pretty printer to show complex structures such as C++ containers. Esri promotes Python as the best choice for writing scripts in ArcGIS. It has also been used in several video games, and has been adopted as first of the three available programming languages in Google App Engine, the other two being Java and Go.
Many operating systems include Python as a standard component. It ships with most Linux distributions, AmigaOS 4 (using Python 2.7), FreeBSD (as a package), NetBSD, and OpenBSD (as a package) and can be used from the command line (terminal). Many Linux distributions use installers written in Python: Ubuntu uses the Ubiquity installer, while Red Hat Linux and Fedora Linux use the Anaconda installer. Gentoo Linux uses Python in its package management system, Portage.
Python is used extensively in the information security industry, including in exploit development.
Most of the Sugar software for the One Laptop per Child XO, developed at Sugar Labs as of 2008, is written in Python. The Raspberry Pi single-board computer project has adopted Python as its main user-programming language.
LibreOffice includes Python and intends to replace Java with Python. Its Python Scripting Provider is a core feature since Version 4.0 from 7 February 2013.

Languages influenced by Python
Python's design and philosophy have influenced many other programming languages:

Boo uses indentation, a similar syntax, and a similar object model.
Cobra uses indentation and a similar syntax, and its Acknowledgements document lists Python first among languages that influenced it.
CoffeeScript, a programming language that cross-compiles to JavaScript, has Python-inspired syntax.
ECMAScript–JavaScript borrowed iterators and generators from Python.
GDScript, a scripting language very similar to Python, built-in to the Godot game engine.
Go is designed for the "speed of working in a dynamic language like Python" and shares the same syntax for slicing arrays.
Groovy was motivated by the desire to bring the Python design philosophy to Java.
Julia was designed to be "as usable for general programming as Python".
Mojo is a non-strict superset of Python (e.g. still missing classes, and adding e.g. struct).
Nim uses indentation and similar syntax.
Ruby's creator, Yukihiro Matsumoto, has said: "I wanted a scripting language that was more powerful than Perl, and more object-oriented than Python. That's why I decided to design my own language."
Swift, a programming language developed by Apple, has some Python-inspired syntax.
Kotlin blends Python and Java features, minimizing boilerplate code for enhanced developer efficiency.
Python's development practices have also been emulated by other languages. For example, the practice of requiring a document describing the rationale for, and issues surrounding, a change to the language (in Python, a PEP) is also used in Tcl, Erlang, and Swift.

See also
Python syntax and semantics
pip (package manager)
List of programming languages
History of programming languages
Comparison of programming languages

References
Sources
"Python for Artificial Intelligence". Python Wiki. 19 July 2012. Archived from the original on 1 November 2012. Retrieved 3 December 2012.
Paine, Jocelyn, ed. (August 2005). "AI in Python". AI Expert Newsletter. Amzi!. Archived from the original on 26 March 2012. Retrieved 11 February 2012.
"PyAIML 0.8.5 : Python Package Index". Pypi.python.org. Retrieved 17 July 2013.
Russell, Stuart J. & Norvig, Peter (2009). Artificial Intelligence: A Modern Approach (3rd ed.). Upper Saddle River, NJ: Prentice Hall. ISBN 978-0-13-604259-4.

Further reading
Downey, Allen B. (May 2012). Think Python: How to Think Like a Computer Scientist (version 1.6.6 ed.). Cambridge University Press. ISBN 978-0-521-72596-5.
Hamilton, Naomi (5 August 2008). "The A-Z of Programming Languages: Python". Computerworld. Archived from the original on 29 December 2008. Retrieved 31 March 2010.
Lutz, Mark (2013). Learning Python (5th ed.). O'Reilly Media. ISBN 978-0-596-15806-4.
Summerfield, Mark (2009). Programming in Python 3 (2nd ed.). Addison-Wesley Professional. ISBN 978-0-321-68056-3.
Ramalho, Luciano (May 2022). Fluent Python. O'Reilly Media. ISBN 978-1-4920-5632-4.

External links

Official website

## Related Articles

### Internal Links

- ["Hello, World!" program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)
- [Autodesk 3ds Max](https://en.wikipedia.org/wiki/Autodesk_3ds_Max)
- [Ternary conditional operator](https://en.wikipedia.org/wiki/Ternary_conditional_operator)
- [ABC (programming language)](https://en.wikipedia.org/wiki/ABC_(programming_language))
- [ADMB](https://en.wikipedia.org/wiki/ADMB)
- [ALGOL](https://en.wikipedia.org/wiki/ALGOL)
- [ALGOL 68](https://en.wikipedia.org/wiki/ALGOL_68)
- [API](https://en.wikipedia.org/wiki/API)
- [APL (programming language)](https://en.wikipedia.org/wiki/APL_(programming_language))
- [AVR microcontrollers](https://en.wikipedia.org/wiki/AVR_microcontrollers)
- [AVR microcontrollers](https://en.wikipedia.org/wiki/AVR_microcontrollers)
- [Abaqus](https://en.wikipedia.org/wiki/Abaqus)
- [Academic Free License](https://en.wikipedia.org/wiki/Academic_Free_License)
- [Academic conference](https://en.wikipedia.org/wiki/Academic_conference)
- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language))
- [Advanced Simulation Library](https://en.wikipedia.org/wiki/Advanced_Simulation_Library)
- [Ahead-of-time compilation](https://en.wikipedia.org/wiki/Ahead-of-time_compilation)
- [Alex Martelli](https://en.wikipedia.org/wiki/Alex_Martelli)
- [Algebra](https://en.wikipedia.org/wiki/Algebra)
- [Alternative terms for free software](https://en.wikipedia.org/wiki/Alternative_terms_for_free_software)
- [Amazon (company)](https://en.wikipedia.org/wiki/Amazon_(company))
- [AmigaOS 4](https://en.wikipedia.org/wiki/AmigaOS_4)
- [Amoeba (operating system)](https://en.wikipedia.org/wiki/Amoeba_(operating_system))
- [Anaconda (installer)](https://en.wikipedia.org/wiki/Anaconda_(installer))
- [Analyse-it](https://en.wikipedia.org/wiki/Analyse-it)
- [Android (operating system)](https://en.wikipedia.org/wiki/Android_(operating_system))
- [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Apache License](https://en.wikipedia.org/wiki/Apache_License)
- [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server)
- [Aphorism](https://en.wikipedia.org/wiki/Aphorism)
- [Apple M1](https://en.wikipedia.org/wiki/Apple_M1)
- [Apple Public Source License](https://en.wikipedia.org/wiki/Apple_Public_Source_License)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Arbitrary-precision arithmetic](https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic)
- [ArcGIS](https://en.wikipedia.org/wiki/ArcGIS)
- [Arithmetic](https://en.wikipedia.org/wiki/Arithmetic)
- [Array (data structure)](https://en.wikipedia.org/wiki/Array_(data_structure))
- [Array slicing](https://en.wikipedia.org/wiki/Array_slicing)
- [Artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence)
- [Artistic License](https://en.wikipedia.org/wiki/Artistic_License)
- [Aspect-oriented programming](https://en.wikipedia.org/wiki/Aspect-oriented_programming)
- [Assembly language](https://en.wikipedia.org/wiki/Assembly_language)
- [Assertion (software development)](https://en.wikipedia.org/wiki/Assertion_(software_development))
- [Assignment (computer science)](https://en.wikipedia.org/wiki/Assignment_(computer_science))
- [Associative array](https://en.wikipedia.org/wiki/Associative_array)
- [Astropy](https://en.wikipedia.org/wiki/Astropy)
- [Asynchronous Server Gateway Interface](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface)
- [Automatic differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation)
- [Automation](https://en.wikipedia.org/wiki/Automation)
- [BASIC](https://en.wikipedia.org/wiki/BASIC)
- [BMDP](https://en.wikipedia.org/wiki/BMDP)
- [Berkeley Software Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution)
- [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses)
- [BV4.1 (software)](https://en.wikipedia.org/wiki/BV4.1_(software))
- [Backporting](https://en.wikipedia.org/wiki/Backporting)
- [Backward compatibility](https://en.wikipedia.org/wiki/Backward_compatibility)
- [Baidu](https://en.wikipedia.org/wiki/Baidu)
- [Bazel (software)](https://en.wikipedia.org/wiki/Bazel_(software))
- [Beerware](https://en.wikipedia.org/wiki/Beerware)
- [Benevolent dictator for life](https://en.wikipedia.org/wiki/Benevolent_dictator_for_life)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Biopython](https://en.wikipedia.org/wiki/Biopython)
- [Blender (software)](https://en.wikipedia.org/wiki/Blender_(software))
- [Block (programming)](https://en.wikipedia.org/wiki/Block_(programming))
- [Boo (programming language)](https://en.wikipedia.org/wiki/Boo_(programming_language))
- [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra)
- [Control flow](https://en.wikipedia.org/wiki/Control_flow)
- [Bug tracking system](https://en.wikipedia.org/wiki/Bug_tracking_system)
- [Byte](https://en.wikipedia.org/wiki/Byte)
- [Bytecode](https://en.wikipedia.org/wiki/Bytecode)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C++11](https://en.wikipedia.org/wiki/C%2B%2B11)
- [C++17](https://en.wikipedia.org/wiki/C%2B%2B17)
- [C11 (C standard revision)](https://en.wikipedia.org/wiki/C11_(C_standard_revision))
- [ANSI C](https://en.wikipedia.org/wiki/ANSI_C)
- [C99](https://en.wikipedia.org/wiki/C99)
- [CCP Games](https://en.wikipedia.org/wiki/CCP_Games)
- [CERN](https://en.wikipedia.org/wiki/CERN)
- [CLPython](https://en.wikipedia.org/wiki/CLPython)
- [CLU (programming language)](https://en.wikipedia.org/wiki/CLU_(programming_language))
- [COBOL](https://en.wikipedia.org/wiki/COBOL)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [CSPro](https://en.wikipedia.org/wiki/CSPro)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Cache poisoning](https://en.wikipedia.org/wiki/Cache_poisoning)
- [Calculus](https://en.wikipedia.org/wiki/Calculus)
- [Call stack](https://en.wikipedia.org/wiki/Call_stack)
- [Capella (notation program)](https://en.wikipedia.org/wiki/Capella_(notation_program))
- [Centrum Wiskunde & Informatica](https://en.wikipedia.org/wiki/Centrum_Wiskunde_%26_Informatica)
- [Chapel (programming language)](https://en.wikipedia.org/wiki/Chapel_(programming_language))
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [CherryPy](https://en.wikipedia.org/wiki/CherryPy)
- [Chris Lattner](https://en.wikipedia.org/wiki/Chris_Lattner)
- [Cinema 4D](https://en.wikipedia.org/wiki/Cinema_4D)
- [CircuitPython](https://en.wikipedia.org/wiki/CircuitPython)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Cobra (programming language)](https://en.wikipedia.org/wiki/Cobra_(programming_language))
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [CoffeeScript](https://en.wikipedia.org/wiki/CoffeeScript)
- [Combinatorics](https://en.wikipedia.org/wiki/Combinatorics)
- [Command-line interface](https://en.wikipedia.org/wiki/Command-line_interface)
- [Commercial software](https://en.wikipedia.org/wiki/Commercial_software)
- [Common Development and Distribution License](https://en.wikipedia.org/wiki/Common_Development_and_Distribution_License)
- [Common Language Runtime](https://en.wikipedia.org/wiki/Common_Language_Runtime)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Community of practice](https://en.wikipedia.org/wiki/Community_of_practice)
- [Comparison of free and open-source software licenses](https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses)
- [Comparison of free software for audio](https://en.wikipedia.org/wiki/Comparison_of_free_software_for_audio)
- [Comparison of integrated development environments](https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments)
- [Comparison of numerical-analysis software](https://en.wikipedia.org/wiki/Comparison_of_numerical-analysis_software)
- [Comparison of open-source and closed-source software](https://en.wikipedia.org/wiki/Comparison_of_open-source_and_closed-source_software)
- [Comparison of open-source configuration management software](https://en.wikipedia.org/wiki/Comparison_of_open-source_configuration_management_software)
- [Comparison of open-source operating systems](https://en.wikipedia.org/wiki/Comparison_of_open-source_operating_systems)
- [Comparison of open-source wireless drivers](https://en.wikipedia.org/wiki/Comparison_of_open-source_wireless_drivers)
- [Comparison of programming languages](https://en.wikipedia.org/wiki/Comparison_of_programming_languages)
- [Comparison of server-side web frameworks](https://en.wikipedia.org/wiki/Comparison_of_server-side_web_frameworks)
- [Comparison of shopping cart software](https://en.wikipedia.org/wiki/Comparison_of_shopping_cart_software)
- [Comparison of source-code-hosting facilities](https://en.wikipedia.org/wiki/Comparison_of_source-code-hosting_facilities)
- [Comparison of statistical packages](https://en.wikipedia.org/wiki/Comparison_of_statistical_packages)
- [Compile time](https://en.wikipedia.org/wiki/Compile_time)
- [Compiler](https://en.wikipedia.org/wiki/Compiler)
- [Complex number](https://en.wikipedia.org/wiki/Complex_number)
- [Computational learning theory](https://en.wikipedia.org/wiki/Computational_learning_theory)
- [Computer algebra system](https://en.wikipedia.org/wiki/Computer_algebra_system)
- [Computer file](https://en.wikipedia.org/wiki/Computer_file)
- [Computer network](https://en.wikipedia.org/wiki/Computer_network)
- [Computer vision](https://en.wikipedia.org/wiki/Computer_vision)
- [Concatenation](https://en.wikipedia.org/wiki/Concatenation)
- [Conditional (computer programming)](https://en.wikipedia.org/wiki/Conditional_(computer_programming))
- [Contributor License Agreement](https://en.wikipedia.org/wiki/Contributor_License_Agreement)
- [Copyleft](https://en.wikipedia.org/wiki/Copyleft)
- [Coroutine](https://en.wikipedia.org/wiki/Coroutine)
- [Creative Commons license](https://en.wikipedia.org/wiki/Creative_Commons_license)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [CubicWeb](https://en.wikipedia.org/wiki/CubicWeb)
- [CumFreq](https://en.wikipedia.org/wiki/CumFreq)
- [List of programming languages by type](https://en.wikipedia.org/wiki/List_of_programming_languages_by_type)
- [Cycle detection](https://en.wikipedia.org/wiki/Cycle_detection)
- [Cython](https://en.wikipedia.org/wiki/Cython)
- [DADiSP](https://en.wikipedia.org/wiki/DADiSP)
- [DAP (software)](https://en.wikipedia.org/wiki/DAP_(software))
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Data Desk](https://en.wikipedia.org/wiki/Data_Desk)
- [Analytics](https://en.wikipedia.org/wiki/Analytics)
- [Data mapper pattern](https://en.wikipedia.org/wiki/Data_mapper_pattern)
- [Data type](https://en.wikipedia.org/wiki/Data_type)
- [Database](https://en.wikipedia.org/wiki/Database)
- [Dataplot](https://en.wikipedia.org/wiki/Dataplot)
- [The Open Source Definition](https://en.wikipedia.org/wiki/The_Open_Source_Definition)
- [Decimal floating point](https://en.wikipedia.org/wiki/Decimal_floating_point)
- [Definite clause grammar](https://en.wikipedia.org/wiki/Definite_clause_grammar)
- [Definition of Free Cultural Works](https://en.wikipedia.org/wiki/Definition_of_Free_Cultural_Works)
- [Design by contract](https://en.wikipedia.org/wiki/Design_by_contract)
- [Device driver](https://en.wikipedia.org/wiki/Device_driver)
- [Differentiable function](https://en.wikipedia.org/wiki/Differentiable_function)
- [Differentiable programming](https://en.wikipedia.org/wiki/Differentiable_programming)
- [Digital rights management](https://en.wikipedia.org/wiki/Digital_rights_management)
- [Discord](https://en.wikipedia.org/wiki/Discord)
- [Dispose pattern](https://en.wikipedia.org/wiki/Dispose_pattern)
- [Django (web framework)](https://en.wikipedia.org/wiki/Django_(web_framework))
- [Documentation](https://en.wikipedia.org/wiki/Documentation)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Double-precision floating-point format](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)
- [Doxygen](https://en.wikipedia.org/wiki/Doxygen)
- [Dropbox](https://en.wikipedia.org/wiki/Dropbox)
- [Duck typing](https://en.wikipedia.org/wiki/Duck_typing)
- [Dylan (programming language)](https://en.wikipedia.org/wiki/Dylan_(programming_language))
- [Dynamic programming language](https://en.wikipedia.org/wiki/Dynamic_programming_language)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript)
- [EViews](https://en.wikipedia.org/wiki/EViews)
- [Eclipse Public License](https://en.wikipedia.org/wiki/Eclipse_Public_License)
- [Ellipsis (computer programming)](https://en.wikipedia.org/wiki/Ellipsis_(computer_programming))
- [End-of-life product](https://en.wikipedia.org/wiki/End-of-life_product)
- [Epi Info](https://en.wikipedia.org/wiki/Epi_Info)
- [Eric (software)](https://en.wikipedia.org/wiki/Eric_(software))
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Escape character](https://en.wikipedia.org/wiki/Escape_character)
- [Esri](https://en.wikipedia.org/wiki/Esri)
- [Euler Mathematical Toolbox](https://en.wikipedia.org/wiki/Euler_Mathematical_Toolbox)
- [Exception handling](https://en.wikipedia.org/wiki/Exception_handling)
- [Exception handling (programming)](https://en.wikipedia.org/wiki/Exception_handling_(programming))
- [Exception handling syntax](https://en.wikipedia.org/wiki/Exception_handling_syntax)
- [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)
- [Expression (computer science)](https://en.wikipedia.org/wiki/Expression_(computer_science))
- [Extensibility](https://en.wikipedia.org/wiki/Extensibility)
- [FEATool Multiphysics](https://en.wikipedia.org/wiki/FEATool_Multiphysics)
- [F Sharp (programming language)](https://en.wikipedia.org/wiki/F_Sharp_(programming_language))
- [Facebook](https://en.wikipedia.org/wiki/Facebook)
- [Factorial](https://en.wikipedia.org/wiki/Factorial)
- [FastAPI](https://en.wikipedia.org/wiki/FastAPI)
- [Fedora Linux](https://en.wikipedia.org/wiki/Fedora_Linux)
- [Fellow](https://en.wikipedia.org/wiki/Fellow)
- [Filename extension](https://en.wikipedia.org/wiki/Filename_extension)
- [Finite element method](https://en.wikipedia.org/wiki/Finite_element_method)
- [Firaxis Games](https://en.wikipedia.org/wiki/Firaxis_Games)
- [Continuation](https://en.wikipedia.org/wiki/Continuation)
- [Flask (web framework)](https://en.wikipedia.org/wiki/Flask_(web_framework))
- [Floating-point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic)
- [Division (mathematics)](https://en.wikipedia.org/wiki/Division_(mathematics))
- [Flux (machine-learning framework)](https://en.wikipedia.org/wiki/Flux_(machine-learning_framework))
- [Foobar](https://en.wikipedia.org/wiki/Foobar)
- [Foreach loop](https://en.wikipedia.org/wiki/Foreach_loop)
- [Fork (software development)](https://en.wikipedia.org/wiki/Fork_(software_development))
- [Forth (programming language)](https://en.wikipedia.org/wiki/Forth_(programming_language))
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Fortress (programming language)](https://en.wikipedia.org/wiki/Fortress_(programming_language))
- [Free-software license](https://en.wikipedia.org/wiki/Free-software_license)
- [FreeBSD](https://en.wikipedia.org/wiki/FreeBSD)
- [FreeCAD](https://en.wikipedia.org/wiki/FreeCAD)
- [FreeFem++](https://en.wikipedia.org/wiki/FreeFem%2B%2B)
- [FreeMat](https://en.wikipedia.org/wiki/FreeMat)
- [Free Software Foundation](https://en.wikipedia.org/wiki/Free_Software_Foundation)
- [Free Software Movement of India](https://en.wikipedia.org/wiki/Free_Software_Movement_of_India)
- [Free and open-source graphics device driver](https://en.wikipedia.org/wiki/Free_and_open-source_graphics_device_driver)
- [Free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software)
- [Free license](https://en.wikipedia.org/wiki/Free_license)
- [Free software](https://en.wikipedia.org/wiki/Free_software)
- [Free software movement](https://en.wikipedia.org/wiki/Free_software_movement)
- [Freeware](https://en.wikipedia.org/wiki/Freeware)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [GAUSS (software)](https://en.wikipedia.org/wiki/GAUSS_(software))
- [Godot (game engine)](https://en.wikipedia.org/wiki/Godot_(game_engine))
- [GIMP](https://en.wikipedia.org/wiki/GIMP)
- [GNU Affero General Public License](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License)
- [GNU Debugger](https://en.wikipedia.org/wiki/GNU_Debugger)
- [GNU General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License)
- [GNU Lesser General Public License](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)
- [GNU Manifesto](https://en.wikipedia.org/wiki/GNU_Manifesto)
- [GNU Octave](https://en.wikipedia.org/wiki/GNU_Octave)
- [GTK](https://en.wikipedia.org/wiki/GTK)
- [Garbage collection (computer science)](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science))
- [General-purpose programming language](https://en.wikipedia.org/wiki/General-purpose_programming_language)
- [Generational list of programming languages](https://en.wikipedia.org/wiki/Generational_list_of_programming_languages)
- [Generator (computer programming)](https://en.wikipedia.org/wiki/Generator_(computer_programming))
- [Generator (computer programming)](https://en.wikipedia.org/wiki/Generator_(computer_programming))
- [Genius (mathematics software)](https://en.wikipedia.org/wiki/Genius_(mathematics_software))
- [Genstat](https://en.wikipedia.org/wiki/Genstat)
- [Gentoo Linux](https://en.wikipedia.org/wiki/Gentoo_Linux)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Global interpreter lock](https://en.wikipedia.org/wiki/Global_interpreter_lock)
- [Scripting language](https://en.wikipedia.org/wiki/Scripting_language)
- [Gmsh](https://en.wikipedia.org/wiki/Gmsh)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Godot (game engine)](https://en.wikipedia.org/wiki/Godot_(game_engine))
- [Google](https://en.wikipedia.org/wiki/Google)
- [Google App Engine](https://en.wikipedia.org/wiki/Google_App_Engine)
- [Google JAX](https://en.wikipedia.org/wiki/Google_JAX)
- [GraphPad Software](https://en.wikipedia.org/wiki/GraphPad_Software)
- [GraphPad Software](https://en.wikipedia.org/wiki/GraphPad_Software)
- [Graphcore](https://en.wikipedia.org/wiki/Graphcore)
- [Graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface)
- [Graphviz](https://en.wikipedia.org/wiki/Graphviz)
- [Gratis versus libre](https://en.wikipedia.org/wiki/Gratis_versus_libre)
- [Gretl](https://en.wikipedia.org/wiki/Gretl)
- [Grok (web framework)](https://en.wikipedia.org/wiki/Grok_(web_framework))
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [Interval (mathematics)](https://en.wikipedia.org/wiki/Interval_(mathematics))
- [Hardware description language](https://en.wikipedia.org/wiki/Hardware_description_language)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Here document](https://en.wikipedia.org/wiki/Here_document)
- [High-level programming language](https://en.wikipedia.org/wiki/High-level_programming_language)
- [History of Python](https://en.wikipedia.org/wiki/History_of_Python)
- [History of free and open-source software](https://en.wikipedia.org/wiki/History_of_free_and_open-source_software)
- [History of programming languages](https://en.wikipedia.org/wiki/History_of_programming_languages)
- [Houdini (software)](https://en.wikipedia.org/wiki/Houdini_(software))
- [IDLE](https://en.wikipedia.org/wiki/IDLE)
- [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)
- [IOS](https://en.wikipedia.org/wiki/IOS)
- [IPython](https://en.wikipedia.org/wiki/IPython)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISC license](https://en.wikipedia.org/wiki/ISC_license)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [ITA Software](https://en.wikipedia.org/wiki/ITA_Software)
- [Icon (programming language)](https://en.wikipedia.org/wiki/Icon_(programming_language))
- [Conditional (computer programming)](https://en.wikipedia.org/wiki/Conditional_(computer_programming))
- [Digital image processing](https://en.wikipedia.org/wiki/Digital_image_processing)
- [Immutable object](https://en.wikipedia.org/wiki/Immutable_object)
- [Immutable object](https://en.wikipedia.org/wiki/Immutable_object)
- [Imperative programming](https://en.wikipedia.org/wiki/Imperative_programming)
- [Include directive](https://en.wikipedia.org/wiki/Include_directive)
- [Inductive bias](https://en.wikipedia.org/wiki/Inductive_bias)
- [Industrial Light & Magic](https://en.wikipedia.org/wiki/Industrial_Light_%26_Magic)
- [Infix notation](https://en.wikipedia.org/wiki/Infix_notation)
- [InfoWorld](https://en.wikipedia.org/wiki/InfoWorld)
- [Information geometry](https://en.wikipedia.org/wiki/Information_geometry)
- [Information security](https://en.wikipedia.org/wiki/Information_security)
- [Inkscape](https://en.wikipedia.org/wiki/Inkscape)
- [Instagram](https://en.wikipedia.org/wiki/Instagram)
- [Field (computer science)](https://en.wikipedia.org/wiki/Field_(computer_science))
- [Integer (computer science)](https://en.wikipedia.org/wiki/Integer_(computer_science))
- [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment)
- [IronPython](https://en.wikipedia.org/wiki/IronPython)
- [Iterator](https://en.wikipedia.org/wiki/Iterator)
- [JASP](https://en.wikipedia.org/wiki/JASP)
- [JMP (statistical software)](https://en.wikipedia.org/wiki/JMP_(statistical_software))
- [JMulTi](https://en.wikipedia.org/wiki/JMulTi)
- [Jamovi](https://en.wikipedia.org/wiki/Jamovi)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Java (software platform)](https://en.wikipedia.org/wiki/Java_(software_platform))
- [Jeff Dean](https://en.wikipedia.org/wiki/Jeff_Dean)
- [Julia (programming language)](https://en.wikipedia.org/wiki/Julia_(programming_language))
- [Just-in-time compilation](https://en.wikipedia.org/wiki/Just-in-time_compilation)
- [Just-in-time compilation](https://en.wikipedia.org/wiki/Just-in-time_compilation)
- [Just another Gibbs sampler](https://en.wikipedia.org/wiki/Just_another_Gibbs_sampler)
- [Jython](https://en.wikipedia.org/wiki/Jython)
- [Keras](https://en.wikipedia.org/wiki/Keras)
- [Kotlin (programming language)](https://en.wikipedia.org/wiki/Kotlin_(programming_language))
- [LIMDEP](https://en.wikipedia.org/wiki/LIMDEP)
- [LISREL](https://en.wikipedia.org/wiki/LISREL)
- [LLVM](https://en.wikipedia.org/wiki/LLVM)
- [LabVIEW](https://en.wikipedia.org/wiki/LabVIEW)
- [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- [Language binding](https://en.wikipedia.org/wiki/Language_binding)
- [Late binding](https://en.wikipedia.org/wiki/Late_binding)
- [Lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation)
- [Lego Mindstorms EV3](https://en.wikipedia.org/wiki/Lego_Mindstorms_EV3)
- [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice)
- [License proliferation](https://en.wikipedia.org/wiki/License_proliferation)
- [LightWave 3D](https://en.wikipedia.org/wiki/LightWave_3D)
- [Linux](https://en.wikipedia.org/wiki/Linux)
- [Linux distribution](https://en.wikipedia.org/wiki/Linux_distribution)
- [Lisp (programming language)](https://en.wikipedia.org/wiki/Lisp_(programming_language))
- [List (abstract data type)](https://en.wikipedia.org/wiki/List_(abstract_data_type))
- [List comprehension](https://en.wikipedia.org/wiki/List_comprehension)
- [List comprehension](https://en.wikipedia.org/wiki/List_comprehension)
- [List of Python software](https://en.wikipedia.org/wiki/List_of_Python_software)
- [List of commercial open-source applications and services](https://en.wikipedia.org/wiki/List_of_commercial_open-source_applications_and_services)
- [List of formerly open-source or free software](https://en.wikipedia.org/wiki/List_of_formerly_open-source_or_free_software)
- [List of formerly proprietary software](https://en.wikipedia.org/wiki/List_of_formerly_proprietary_software)
- [List of free-software events](https://en.wikipedia.org/wiki/List_of_free-software_events)
- [List of free and open-source Android applications](https://en.wikipedia.org/wiki/List_of_free_and_open-source_Android_applications)
- [List of free and open-source iOS applications](https://en.wikipedia.org/wiki/List_of_free_and_open-source_iOS_applications)
- [List of free and open-source software organizations](https://en.wikipedia.org/wiki/List_of_free_and_open-source_software_organizations)
- [List of free and open-source software packages](https://en.wikipedia.org/wiki/List_of_free_and_open-source_software_packages)
- [List of free and open-source web applications](https://en.wikipedia.org/wiki/List_of_free_and_open-source_web_applications)
- [List of free software project directories](https://en.wikipedia.org/wiki/List_of_free_software_project_directories)
- [List of free television software](https://en.wikipedia.org/wiki/List_of_free_television_software)
- [Comparison of integrated development environments](https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments)
- [List of numerical-analysis software](https://en.wikipedia.org/wiki/List_of_numerical-analysis_software)
- [List of office suites](https://en.wikipedia.org/wiki/List_of_office_suites)
- [List of open-source bioinformatics software](https://en.wikipedia.org/wiki/List_of_open-source_bioinformatics_software)
- [List of open-source codecs](https://en.wikipedia.org/wiki/List_of_open-source_codecs)
- [List of open-source health software](https://en.wikipedia.org/wiki/List_of_open-source_health_software)
- [List of open-source routing platforms](https://en.wikipedia.org/wiki/List_of_open-source_routing_platforms)
- [List of open-source software for mathematics](https://en.wikipedia.org/wiki/List_of_open-source_software_for_mathematics)
- [List of open-source video games](https://en.wikipedia.org/wiki/List_of_open-source_video_games)
- [List of programming languages](https://en.wikipedia.org/wiki/List_of_programming_languages)
- [List of programming languages by type](https://en.wikipedia.org/wiki/List_of_programming_languages_by_type)
- [List of statistical software](https://en.wikipedia.org/wiki/List_of_statistical_software)
- [Lock (computer science)](https://en.wikipedia.org/wiki/Lock_(computer_science))
- [Logic programming](https://en.wikipedia.org/wiki/Logic_programming)
- [Long-term support](https://en.wikipedia.org/wiki/Long-term_support)
- [Lua (programming language)](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [MFEM](https://en.wikipedia.org/wiki/MFEM)
- [MIME](https://en.wikipedia.org/wiki/MIME)
- [MIT License](https://en.wikipedia.org/wiki/MIT_License)
- [ML (programming language)](https://en.wikipedia.org/wiki/ML_(programming_language))
- [MLwiN](https://en.wikipedia.org/wiki/MLwiN)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
- [Maple (software)](https://en.wikipedia.org/wiki/Maple_(software))
- [Mathcad](https://en.wikipedia.org/wiki/Mathcad)
- [Mathematics](https://en.wikipedia.org/wiki/Mathematics)
- [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
- [Matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication)
- [Autodesk Maya](https://en.wikipedia.org/wiki/Autodesk_Maya)
- [MedCalc](https://en.wikipedia.org/wiki/MedCalc)
- [Memory management](https://en.wikipedia.org/wiki/Memory_management)
- [Memristor](https://en.wikipedia.org/wiki/Memristor)
- [Mercurial](https://en.wikipedia.org/wiki/Mercurial)
- [Metaclass](https://en.wikipedia.org/wiki/Metaclass)
- [Metaobject](https://en.wikipedia.org/wiki/Metaobject)
- [Metaprogramming](https://en.wikipedia.org/wiki/Metaprogramming)
- [Metasyntactic variable](https://en.wikipedia.org/wiki/Metasyntactic_variable)
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [MicroPython](https://en.wikipedia.org/wiki/MicroPython)
- [Microcontroller](https://en.wikipedia.org/wiki/Microcontroller)
- [Microfit](https://en.wikipedia.org/wiki/Microfit)
- [Microsoft Excel](https://en.wikipedia.org/wiki/Microsoft_Excel)
- [Microsoft Open Specification Promise](https://en.wikipedia.org/wiki/Microsoft_Open_Specification_Promise)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Microthread](https://en.wikipedia.org/wiki/Microthread)
- [MindSpore](https://en.wikipedia.org/wiki/MindSpore)
- [Minitab](https://en.wikipedia.org/wiki/Minitab)
- [Mobile app](https://en.wikipedia.org/wiki/Mobile_app)
- [Mod wsgi](https://en.wikipedia.org/wiki/Mod_wsgi)
- [Modo (software)](https://en.wikipedia.org/wiki/Modo_(software))
- [Modula-3](https://en.wikipedia.org/wiki/Modula-3)
- [Modular programming](https://en.wikipedia.org/wiki/Modular_programming)
- [Modulo](https://en.wikipedia.org/wiki/Modulo)
- [Mojo (programming language)](https://en.wikipedia.org/wiki/Mojo_(programming_language))
- [Monty Python](https://en.wikipedia.org/wiki/Monty_Python)
- [Monty Python's Flying Circus](https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus)
- [Autodesk MotionBuilder](https://en.wikipedia.org/wiki/Autodesk_MotionBuilder)
- [Mozilla Public License](https://en.wikipedia.org/wiki/Mozilla_Public_License)
- [Debian–Mozilla trademark dispute](https://en.wikipedia.org/wiki/Debian%E2%80%93Mozilla_trademark_dispute)
- [Comparison of multi-paradigm programming languages](https://en.wikipedia.org/wiki/Comparison_of_multi-paradigm_programming_languages)
- [Comparison of multi-paradigm programming languages](https://en.wikipedia.org/wiki/Comparison_of_multi-paradigm_programming_languages)
- [Multimedia](https://en.wikipedia.org/wiki/Multimedia)
- [Multithreading (computer architecture)](https://en.wikipedia.org/wiki/Multithreading_(computer_architecture))
- [Musical notation](https://en.wikipedia.org/wiki/Musical_notation)
- [MyHDL](https://en.wikipedia.org/wiki/MyHDL)
- [Nokia N900](https://en.wikipedia.org/wiki/Nokia_N900)
- [NASA](https://en.wikipedia.org/wiki/NASA)
- [NCSS (statistical software)](https://en.wikipedia.org/wiki/NCSS_(statistical_software))
- [NOP (code)](https://en.wikipedia.org/wiki/NOP_(code))
- [Name resolution (programming languages)](https://en.wikipedia.org/wiki/Name_resolution_(programming_languages))
- [Natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing)
- [Neologism](https://en.wikipedia.org/wiki/Neologism)
- [NetBSD](https://en.wikipedia.org/wiki/NetBSD)
- [Netherlands](https://en.wikipedia.org/wiki/Netherlands)
- [Neuromorphic computing](https://en.wikipedia.org/wiki/Neuromorphic_computing)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Nim (programming language)](https://en.wikipedia.org/wiki/Nim_(programming_language))
- [Ninja-IDE](https://en.wikipedia.org/wiki/Ninja-IDE)
- [Nokia](https://en.wikipedia.org/wiki/Nokia)
- [Non-English-based programming languages](https://en.wikipedia.org/wiki/Non-English-based_programming_languages)
- [Norman Jouppi](https://en.wikipedia.org/wiki/Norman_Jouppi)
- [Notebook interface](https://en.wikipedia.org/wiki/Notebook_interface)
- [Nuitka](https://en.wikipedia.org/wiki/Nuitka)
- [Nuke (software)](https://en.wikipedia.org/wiki/Nuke_(software))
- [Null pointer](https://en.wikipedia.org/wiki/Null_pointer)
- [NumPy](https://en.wikipedia.org/wiki/NumPy)
- [Numba](https://en.wikipedia.org/wiki/Numba)
- [Number theory](https://en.wikipedia.org/wiki/Number_theory)
- [Numerical analysis](https://en.wikipedia.org/wiki/Numerical_analysis)
- [O'Reilly Media](https://en.wikipedia.org/wiki/O%27Reilly_Media)
- [O'Reilly Open Source Convention](https://en.wikipedia.org/wiki/O%27Reilly_Open_Source_Convention)
- [OS/2](https://en.wikipedia.org/wiki/OS/2)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Object Pascal](https://en.wikipedia.org/wiki/Object_Pascal)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [Off-side rule](https://en.wikipedia.org/wiki/Off-side_rule)
- [One Laptop per Child](https://en.wikipedia.org/wiki/One_Laptop_per_Child)
- [Open-core model](https://en.wikipedia.org/wiki/Open-core_model)
- [Open-source software movement](https://en.wikipedia.org/wiki/Open-source_software_movement)
- [Open-source hardware](https://en.wikipedia.org/wiki/Open-source_hardware)
- [Open-source license](https://en.wikipedia.org/wiki/Open-source_license)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [Open-source software advocacy](https://en.wikipedia.org/wiki/Open-source_software_advocacy)
- [Open-source software development](https://en.wikipedia.org/wiki/Open-source_software_development)
- [Open-source software security](https://en.wikipedia.org/wiki/Open-source_software_security)
- [OpenBSD](https://en.wikipedia.org/wiki/OpenBSD)
- [OpenBUGS](https://en.wikipedia.org/wiki/OpenBUGS)
- [OpenCV](https://en.wikipedia.org/wiki/OpenCV)
- [OpenFOAM](https://en.wikipedia.org/wiki/OpenFOAM)
- [OpenVMS](https://en.wikipedia.org/wiki/OpenVMS)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Operator overloading](https://en.wikipedia.org/wiki/Operator_overloading)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Orange (software)](https://en.wikipedia.org/wiki/Orange_(software))
- [Order of operations](https://en.wikipedia.org/wiki/Order_of_operations)
- [Outline of free software](https://en.wikipedia.org/wiki/Outline_of_free_software)
- [OxMetrics](https://en.wikipedia.org/wiki/OxMetrics)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PSPP](https://en.wikipedia.org/wiki/PSPP)
- [Package manager](https://en.wikipedia.org/wiki/Package_manager)
- [PaintShop Pro](https://en.wikipedia.org/wiki/PaintShop_Pro)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching)
- [Pattern recognition](https://en.wikipedia.org/wiki/Pattern_recognition)
- [Pdoc](https://en.wikipedia.org/wiki/Pdoc)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Permissive software license](https://en.wikipedia.org/wiki/Permissive_software_license)
- [Peter Norvig](https://en.wikipedia.org/wiki/Peter_Norvig)
- [Pip (package manager)](https://en.wikipedia.org/wiki/Pip_(package_manager))
- [Pointer (computer programming)](https://en.wikipedia.org/wiki/Pointer_(computer_programming))
- [Portage (software)](https://en.wikipedia.org/wiki/Portage_(software))
- [Porting](https://en.wikipedia.org/wiki/Porting)
- [Program optimization](https://en.wikipedia.org/wiki/Program_optimization)
- [Prettyprint](https://en.wikipedia.org/wiki/Prettyprint)
- [Printf](https://en.wikipedia.org/wiki/Printf)
- [ProbLog](https://en.wikipedia.org/wiki/ProbLog)
- [Procedural programming](https://en.wikipedia.org/wiki/Procedural_programming)
- [Programming idiom](https://en.wikipedia.org/wiki/Programming_idiom)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Programming language implementation](https://en.wikipedia.org/wiki/Programming_language_implementation)
- [Programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)
- [Project Jupyter](https://en.wikipedia.org/wiki/Project_Jupyter)
- [Prolog](https://en.wikipedia.org/wiki/Prolog)
- [Binary blob](https://en.wikipedia.org/wiki/Binary_blob)
- [Proprietary firmware](https://en.wikipedia.org/wiki/Proprietary_firmware)
- [Proprietary software](https://en.wikipedia.org/wiki/Proprietary_software)
- [Pseudorandom number generator](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)
- [Psyco](https://en.wikipedia.org/wiki/Psyco)
- [Public-domain software](https://en.wikipedia.org/wiki/Public-domain_software)
- [Public domain](https://en.wikipedia.org/wiki/Public_domain)
- [PyCharm](https://en.wikipedia.org/wiki/PyCharm)
- [Python Conference](https://en.wikipedia.org/wiki/Python_Conference)
- [PyDev](https://en.wikipedia.org/wiki/PyDev)
- [PyGTK](https://en.wikipedia.org/wiki/PyGTK)
- [PyLadies](https://en.wikipedia.org/wiki/PyLadies)
- [PyMC](https://en.wikipedia.org/wiki/PyMC)
- [PyPy](https://en.wikipedia.org/wiki/PyPy)
- [PyQt](https://en.wikipedia.org/wiki/PyQt)
- [Python for S60](https://en.wikipedia.org/wiki/Python_for_S60)
- [PyTorch](https://en.wikipedia.org/wiki/PyTorch)
- [Pydoc](https://en.wikipedia.org/wiki/Pydoc)
- [Pygame](https://en.wikipedia.org/wiki/Pygame)
- [Pyjs](https://en.wikipedia.org/wiki/Pyjs)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Pyrex (programming language)](https://en.wikipedia.org/wiki/Pyrex_(programming_language))
- [PythonAnywhere](https://en.wikipedia.org/wiki/PythonAnywhere)
- [Python (genus)](https://en.wikipedia.org/wiki/Python_(genus))
- [Python Conference](https://en.wikipedia.org/wiki/Python_Conference)
- [Python License](https://en.wikipedia.org/wiki/Python_License)
- [Python Package Index](https://en.wikipedia.org/wiki/Python_Package_Index)
- [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation)
- [Python Software Foundation License](https://en.wikipedia.org/wiki/Python_Software_Foundation_License)
- [Python for S60](https://en.wikipedia.org/wiki/Python_for_S60)
- [Python syntax and semantics](https://en.wikipedia.org/wiki/Python_syntax_and_semantics)
- [PyTorch](https://en.wikipedia.org/wiki/PyTorch)
- [Qt (software)](https://en.wikipedia.org/wiki/Qt_(software))
- [Quixote (web framework)](https://en.wikipedia.org/wiki/Quixote_(web_framework))
- [RATS (software)](https://en.wikipedia.org/wiki/RATS_(software))
- [RExcel](https://en.wikipedia.org/wiki/RExcel)
- [RISC-V](https://en.wikipedia.org/wiki/RISC-V)
- [PyPy](https://en.wikipedia.org/wiki/PyPy)
- [RStudio](https://en.wikipedia.org/wiki/RStudio)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi)
- [Raspberry Pi OS](https://en.wikipedia.org/wiki/Raspberry_Pi_OS)
- [Rational number](https://en.wikipedia.org/wiki/Rational_number)
- [String literal](https://en.wikipedia.org/wiki/String_literal)
- [Read–eval–print loop](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)
- [Red Hat Linux](https://en.wikipedia.org/wiki/Red_Hat_Linux)
- [Reddit](https://en.wikipedia.org/wiki/Reddit)
- [Reference counting](https://en.wikipedia.org/wiki/Reference_counting)
- [Reference implementation](https://en.wikipedia.org/wiki/Reference_implementation)
- [Reflective programming](https://en.wikipedia.org/wiki/Reflective_programming)
- [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Relational database](https://en.wikipedia.org/wiki/Relational_database)
- [Arbitrary code execution](https://en.wikipedia.org/wiki/Arbitrary_code_execution)
- [Resource acquisition is initialization](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization)
- [Revolution Analytics](https://en.wikipedia.org/wiki/Revolution_Analytics)
- [Revolution OS](https://en.wikipedia.org/wiki/Revolution_OS)
- [Ricci calculus](https://en.wikipedia.org/wiki/Ricci_calculus)
- [Ring (programming language)](https://en.wikipedia.org/wiki/Ring_(programming_language))
- [Rounding](https://en.wikipedia.org/wiki/Rounding)
- [Rounding](https://en.wikipedia.org/wiki/Rounding)
- [Roundup (issue tracker)](https://en.wikipedia.org/wiki/Roundup_(issue_tracker))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Run-time algorithm specialization](https://en.wikipedia.org/wiki/Run-time_algorithm_specialization)
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [S-PLUS](https://en.wikipedia.org/wiki/S-PLUS)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [SAS (software)](https://en.wikipedia.org/wiki/SAS_(software))
- [SCO–Linux disputes](https://en.wikipedia.org/wiki/SCO%E2%80%93Linux_disputes)
- [SETL](https://en.wikipedia.org/wiki/SETL)
- [Shazam (econometrics software)](https://en.wikipedia.org/wiki/Shazam_(econometrics_software))
- [SOFA Statistics](https://en.wikipedia.org/wiki/SOFA_Statistics)
- [SPSS](https://en.wikipedia.org/wiki/SPSS)
- [SPSS Modeler](https://en.wikipedia.org/wiki/SPSS_Modeler)
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [SQLAlchemy](https://en.wikipedia.org/wiki/SQLAlchemy)
- [SUDAAN](https://en.wikipedia.org/wiki/SUDAAN)
- [SYSTAT (statistics package)](https://en.wikipedia.org/wiki/SYSTAT_(statistics_package))
- [SageMath](https://en.wikipedia.org/wiki/SageMath)
- [Salome (software)](https://en.wikipedia.org/wiki/Salome_(software))
- [Scheme (programming language)](https://en.wikipedia.org/wiki/Scheme_(programming_language))
- [SciPy](https://en.wikipedia.org/wiki/SciPy)
- [ScicosLab](https://en.wikipedia.org/wiki/ScicosLab)
- [Computational science](https://en.wikipedia.org/wiki/Computational_science)
- [Scikit-learn](https://en.wikipedia.org/wiki/Scikit-learn)
- [Scilab](https://en.wikipedia.org/wiki/Scilab)
- [Scorewriter](https://en.wikipedia.org/wiki/Scorewriter)
- [Scratch (programming language)](https://en.wikipedia.org/wiki/Scratch_(programming_language))
- [Scribus](https://en.wikipedia.org/wiki/Scribus)
- [Scripting language](https://en.wikipedia.org/wiki/Scripting_language)
- [SegReg](https://en.wikipedia.org/wiki/SegReg)
- [Self-hosting (web services)](https://en.wikipedia.org/wiki/Self-hosting_(web_services))
- [S60 (software platform)](https://en.wikipedia.org/wiki/S60_(software_platform))
- [Set (abstract data type)](https://en.wikipedia.org/wiki/Set_(abstract_data_type))
- [Object copying](https://en.wikipedia.org/wiki/Object_copying)
- [Shared Source Initiative](https://en.wikipedia.org/wiki/Shared_Source_Initiative)
- [Shed Skin](https://en.wikipedia.org/wiki/Shed_Skin)
- [Shell script](https://en.wikipedia.org/wiki/Shell_script)
- [SigmaStat](https://en.wikipedia.org/wiki/SigmaStat)
- [Off-side rule](https://en.wikipedia.org/wiki/Off-side_rule)
- [SimFiT](https://en.wikipedia.org/wiki/SimFiT)
- [Simple DirectMedia Layer](https://en.wikipedia.org/wiki/Simple_DirectMedia_Layer)
- [Simula](https://en.wikipedia.org/wiki/Simula)
- [Single-board computer](https://en.wikipedia.org/wiki/Single-board_computer)
- [Single-precision floating-point format](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)
- [Sleepycat Software](https://en.wikipedia.org/wiki/Sleepycat_Software)
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [SmartPLS](https://en.wikipedia.org/wiki/SmartPLS)
- [Softimage](https://en.wikipedia.org/wiki/Softimage)
- [Software design](https://en.wikipedia.org/wiki/Software_design)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software patents and free software](https://en.wikipedia.org/wiki/Software_patents_and_free_software)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Oracle Solaris](https://en.wikipedia.org/wiki/Oracle_Solaris)
- [Source-available software](https://en.wikipedia.org/wiki/Source-available_software)
- [Spam (Monty Python sketch)](https://en.wikipedia.org/wiki/Spam_(Monty_Python_sketch))
- [Speakeasy (computational environment)](https://en.wikipedia.org/wiki/Speakeasy_(computational_environment))
- [Sphinx (documentation generator)](https://en.wikipedia.org/wiki/Sphinx_(documentation_generator))
- [SpiNNaker](https://en.wikipedia.org/wiki/SpiNNaker)
- [Spotify](https://en.wikipedia.org/wiki/Spotify)
- [Spyder (software)](https://en.wikipedia.org/wiki/Spyder_(software))
- [Stack Overflow](https://en.wikipedia.org/wiki/Stack_Overflow)
- [Stackless Python](https://en.wikipedia.org/wiki/Stackless_Python)
- [Stan (software)](https://en.wikipedia.org/wiki/Stan_(software))
- [Standard ML](https://en.wikipedia.org/wiki/Standard_ML)
- [Standard library](https://en.wikipedia.org/wiki/Standard_library)
- [StatView](https://en.wikipedia.org/wiki/StatView)
- [StatXact](https://en.wikipedia.org/wiki/StatXact)
- [Stata](https://en.wikipedia.org/wiki/Stata)
- [Statement (computer science)](https://en.wikipedia.org/wiki/Statement_(computer_science))
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Statistica](https://en.wikipedia.org/wiki/Statistica)
- [Statistical manifold](https://en.wikipedia.org/wiki/Statistical_manifold)
- [StatsDirect](https://en.wikipedia.org/wiki/StatsDirect)
- [String interpolation](https://en.wikipedia.org/wiki/String_interpolation)
- [String literal](https://en.wikipedia.org/wiki/String_literal)
- [Strong and weak typing](https://en.wikipedia.org/wiki/Strong_and_weak_typing)
- [Strong and weak typing](https://en.wikipedia.org/wiki/Strong_and_weak_typing)
- [Record (computer science)](https://en.wikipedia.org/wiki/Record_(computer_science))
- [Structured programming](https://en.wikipedia.org/wiki/Structured_programming)
- [Stuart J. Russell](https://en.wikipedia.org/wiki/Stuart_J._Russell)
- [Sugar (desktop environment)](https://en.wikipedia.org/wiki/Sugar_(desktop_environment))
- [Sugar Labs](https://en.wikipedia.org/wiki/Sugar_Labs)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Switch statement](https://en.wikipedia.org/wiki/Switch_statement)
- [Symbian](https://en.wikipedia.org/wiki/Symbian)
- [Syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar)
- [Syntax highlighting](https://en.wikipedia.org/wiki/Syntax_highlighting)
- [System administrator](https://en.wikipedia.org/wiki/System_administrator)
- [TACTIC (web framework)](https://en.wikipedia.org/wiki/TACTIC_(web_framework))
- [TIOBE index](https://en.wikipedia.org/wiki/TIOBE_index)
- [TSP (econometrics software)](https://en.wikipedia.org/wiki/TSP_(econometrics_software))
- [Tail call](https://en.wikipedia.org/wiki/Tail_call)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow)
- [Tensor Processing Unit](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)
- [Test automation](https://en.wikipedia.org/wiki/Test_automation)
- [Test suite](https://en.wikipedia.org/wiki/Test_suite)
- [Text processing](https://en.wikipedia.org/wiki/Text_processing)
- [The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language)
- [The Cathedral and the Bazaar](https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar)
- [The Computer Language Benchmarks Game](https://en.wikipedia.org/wiki/The_Computer_Language_Benchmarks_Game)
- [The Document Foundation](https://en.wikipedia.org/wiki/The_Document_Foundation)
- [The Free Software Definition](https://en.wikipedia.org/wiki/The_Free_Software_Definition)
- [The Open Source Definition](https://en.wikipedia.org/wiki/The_Open_Source_Definition)
- [The Unscrambler](https://en.wikipedia.org/wiki/The_Unscrambler)
- [Theano (software)](https://en.wikipedia.org/wiki/Theano_(software))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [This (computer programming)](https://en.wikipedia.org/wiki/This_(computer_programming))
- [Timeline of free and open-source software](https://en.wikipedia.org/wiki/Timeline_of_free_and_open-source_software)
- [Timeline of programming languages](https://en.wikipedia.org/wiki/Timeline_of_programming_languages)
- [Tivoization](https://en.wikipedia.org/wiki/Tivoization)
- [Tkinter](https://en.wikipedia.org/wiki/Tkinter)
- [Tornado (web server)](https://en.wikipedia.org/wiki/Tornado_(web_server))
- [Source-to-source compiler](https://en.wikipedia.org/wiki/Source-to-source_compiler)
- [Source-to-source compiler](https://en.wikipedia.org/wiki/Source-to-source_compiler)
- [Trusted Computing](https://en.wikipedia.org/wiki/Trusted_Computing)
- [Tuple](https://en.wikipedia.org/wiki/Tuple)
- [TurboGears](https://en.wikipedia.org/wiki/TurboGears)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
- [Ubiquity (software)](https://en.wikipedia.org/wiki/Ubiquity_(software))
- [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu)
- [Unary operation](https://en.wikipedia.org/wiki/Unary_operation)
- [Unicode](https://en.wikipedia.org/wiki/Unicode)
- [Unit testing](https://en.wikipedia.org/wiki/Unit_testing)
- [Unit testing](https://en.wikipedia.org/wiki/Unit_testing)
- [Unix-like](https://en.wikipedia.org/wiki/Unix-like)
- [Unix shell](https://en.wikipedia.org/wiki/Unix_shell)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [Unlicense](https://en.wikipedia.org/wiki/Unlicense)
- [VHDL](https://en.wikipedia.org/wiki/VHDL)
- [Verilog](https://en.wikipedia.org/wiki/Verilog)
- [Virtual machine](https://en.wikipedia.org/wiki/Virtual_machine)
- [VisSim](https://en.wikipedia.org/wiki/VisSim)
- [Vision processing unit](https://en.wikipedia.org/wiki/Vision_processing_unit)
- [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic)
- [Visual Basic (.NET)](https://en.wikipedia.org/wiki/Visual_Basic_(.NET))
- [Visual Basic (classic)](https://en.wikipedia.org/wiki/Visual_Basic_(classic))
- [WTFPL](https://en.wikipedia.org/wiki/WTFPL)
- [Web2py](https://en.wikipedia.org/wiki/Web2py)
- [WebAssembly](https://en.wikipedia.org/wiki/WebAssembly)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [Web application](https://en.wikipedia.org/wiki/Web_application)
- [Web browser](https://en.wikipedia.org/wiki/Web_browser)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [Web scraping](https://en.wikipedia.org/wiki/Web_scraping)
- [Weka (software)](https://en.wikipedia.org/wiki/Weka_(software))
- [While loop](https://en.wikipedia.org/wiki/While_loop)
- [Whitespace character](https://en.wikipedia.org/wiki/Whitespace_character)
- [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia)
- [WinBUGS](https://en.wikipedia.org/wiki/WinBUGS)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Windows 7](https://en.wikipedia.org/wiki/Windows_7)
- [Windows XP](https://en.wikipedia.org/wiki/Windows_XP)
- [Wolfram Mathematica](https://en.wikipedia.org/wiki/Wolfram_Mathematica)
- [World Programming System](https://en.wikipedia.org/wiki/World_Programming_System)
- [X-13ARIMA-SEATS](https://en.wikipedia.org/wiki/X-13ARIMA-SEATS)
- [X10 (programming language)](https://en.wikipedia.org/wiki/X10_(programming_language))
- [XLfit](https://en.wikipedia.org/wiki/XLfit)
- [XLispStat](https://en.wikipedia.org/wiki/XLispStat)
- [XploRe](https://en.wikipedia.org/wiki/XploRe)
- [Yahoo](https://en.wikipedia.org/wiki/Yahoo)
- [Yukihiro Matsumoto](https://en.wikipedia.org/wiki/Yukihiro_Matsumoto)
- [Zen of Python](https://en.wikipedia.org/wiki/Zen_of_Python)
- [Zero-based numbering](https://en.wikipedia.org/wiki/Zero-based_numbering)
- [Zlib License](https://en.wikipedia.org/wiki/Zlib_License)
- [Zope](https://en.wikipedia.org/wiki/Zope)
- [Wikipedia:Wikimedia sister projects](https://en.wikipedia.org/wiki/Wikipedia:Wikimedia_sister_projects)
- [Template:Differentiable computing](https://en.wikipedia.org/wiki/Template:Differentiable_computing)
- [Template:FOSS](https://en.wikipedia.org/wiki/Template:FOSS)
- [Template:Numerical analysis software](https://en.wikipedia.org/wiki/Template:Numerical_analysis_software)
- [Template:Programming languages](https://en.wikipedia.org/wiki/Template:Programming_languages)
- [Template:Python (programming language)](https://en.wikipedia.org/wiki/Template:Python_(programming_language))
- [Template:Python web frameworks](https://en.wikipedia.org/wiki/Template:Python_web_frameworks)
- [Template:Statistical software](https://en.wikipedia.org/wiki/Template:Statistical_software)
- [Template talk:Differentiable computing](https://en.wikipedia.org/wiki/Template_talk:Differentiable_computing)
- [Template talk:FOSS](https://en.wikipedia.org/wiki/Template_talk:FOSS)
- [Template talk:Numerical analysis software](https://en.wikipedia.org/wiki/Template_talk:Numerical_analysis_software)
- [Template talk:Programming languages](https://en.wikipedia.org/wiki/Template_talk:Programming_languages)
- [Template talk:Python (programming language)](https://en.wikipedia.org/wiki/Template_talk:Python_(programming_language))
- [Template talk:Python web frameworks](https://en.wikipedia.org/wiki/Template_talk:Python_web_frameworks)
- [Template talk:Statistical software](https://en.wikipedia.org/wiki/Template_talk:Statistical_software)
- [Help:Authority control](https://en.wikipedia.org/wiki/Help:Authority_control)
- [Help:Cite errors/Cite error references no text](https://en.wikipedia.org/wiki/Help:Cite_errors/Cite_error_references_no_text)
- [Category:Articles containing potentially dated statements from 2008](https://en.wikipedia.org/wiki/Category:Articles_containing_potentially_dated_statements_from_2008)
- [Category:Articles containing potentially dated statements from 2020](https://en.wikipedia.org/wiki/Category:Articles_containing_potentially_dated_statements_from_2020)
- [Category:Articles containing potentially dated statements from December 2022](https://en.wikipedia.org/wiki/Category:Articles_containing_potentially_dated_statements_from_December_2022)
- [Category:Articles containing potentially dated statements from March 2024](https://en.wikipedia.org/wiki/Category:Articles_containing_potentially_dated_statements_from_March_2024)
- [Category:Articles containing potentially dated statements from October 2024](https://en.wikipedia.org/wiki/Category:Articles_containing_potentially_dated_statements_from_October_2024)
- [Category:Free software](https://en.wikipedia.org/wiki/Category:Free_software)
- [Category:Programming languages](https://en.wikipedia.org/wiki/Category:Programming_languages)
- [Category:Python (programming language) web frameworks](https://en.wikipedia.org/wiki/Category:Python_(programming_language)_web_frameworks)
- [Category:Statistical software](https://en.wikipedia.org/wiki/Category:Statistical_software)
- [Category:Use American English from December 2024](https://en.wikipedia.org/wiki/Category:Use_American_English_from_December_2024)
- [Category:Use dmy dates from November 2021](https://en.wikipedia.org/wiki/Category:Use_dmy_dates_from_November_2021)
- [Portal:Computer programming](https://en.wikipedia.org/wiki/Portal:Computer_programming)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)
- [Portal:Technology](https://en.wikipedia.org/wiki/Portal:Technology)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:44:40.252691+00:00_