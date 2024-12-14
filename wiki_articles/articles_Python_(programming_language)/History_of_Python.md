# History of Python

## Article Metadata

- **Last Updated:** 2024-12-14T19:29:45.303832+00:00
- **Original Article:** [History of Python](https://en.wikipedia.org/wiki/History_of_Python)
- **Language:** en
- **Page ID:** 21356332

## Summary

The programming language Python was conceived in the late 1980s, and its implementation was started in December 1989 by Guido van Rossum at CWI in the Netherlands as a successor to ABC capable of exception handling and interfacing with the Amoeba operating system. Van Rossum is Python's principal author, and his continuing central role in deciding the direction of Python is reflected in the title given to him by the Python community, Benevolent Dictator for Life (BDFL). (However, Van Rossum step

## Categories

- Category:All Wikipedia articles written in American English
- Category:All articles containing potentially dated statements
- Category:Articles containing potentially dated statements from 2007
- Category:Articles to be expanded from March 2024
- Category:Articles with short description
- Category:History of software
- Category:Pages using multiple image with auto scaled images
- Category:Pages using the EasyTimeline extension
- Category:Python (programming language)
- Category:Short description is different from Wikidata
- Category:Software version histories
- Category:Use American English from May 2024
- Category:Use mdy dates from September 2015
- Category:Wikipedia articles scheduled for update tagging

## Table of Contents

- Early history
- Version 1
- Version 2
- Version 3
- Table of versions
- See also
- References
- External links

## Content

The programming language Python was conceived in the late 1980s, and its implementation was started in December 1989 by Guido van Rossum at CWI in the Netherlands as a successor to ABC capable of exception handling and interfacing with the Amoeba operating system. Van Rossum is Python's principal author, and his continuing central role in deciding the direction of Python is reflected in the title given to him by the Python community, Benevolent Dictator for Life (BDFL). (However, Van Rossum stepped down as leader on July 12, 2018.). Python was named after the BBC TV show Monty Python's Flying Circus.
Python 2.0 was released on October 16, 2000, with many major new features, such as list comprehensions, cycle-detecting garbage collector (in addition to reference counting) and reference counting, for memory management and support for Unicode, along with a change to the development process itself, with a shift to a more transparent and community-backed process.
Python 3.0, a major, backwards-incompatible release, was released on December 3, 2008 after a long period of testing. Many of its major features have also been backported to the backwards-compatible, though now-unsupported, Python 2.6 and 2.7. Releases of Python 3 include the 2to3 utility, which automates the translation of Python 2 code to Python 3.

Early history
In February 1991, Van Rossum published the code (labeled version 0.9.0) to alt.sources. Already present at this stage in development were classes with inheritance, exception handling, functions, and the core datatypes of list, dict, str and so on. Also in this initial release was a module system borrowed from Modula-3; Van Rossum describes the module as "one of Python's major programming units". Python's exception model also resembles Modula-3's, with the addition of an else clause. In 1994 comp.lang.python, the primary discussion forum for Python, was formed, marking a milestone in the growth of Python's userbase and popularity.

Version 1
Python reached version 1.0 in January 1994. The major new features included in this release were the functional programming tools lambda, map, filter and reduce. Van Rossum stated that "Python acquired lambda, reduce(), filter() and map(), courtesy of a Lisp hacker who missed them and submitted working patches".
The last version released while Van Rossum was at CWI was Python 1.2.  In 1995, Van Rossum continued his work on Python at the Corporation for National Research Initiatives (CNRI) in Reston, Virginia from where he released several versions.
By version 1.4, Python had acquired several new features. Notable among these are the Modula-3 inspired keyword arguments (which are also similar to Common Lisp's keyword arguments) and built-in support for complex numbers. Also included is a basic form of data hiding by name mangling, though this is easily bypassed.
During Van Rossum's stay at CNRI, he launched the Computer Programming for Everybody (CP4E) initiative, intending to make programming more accessible to more people, with a basic "literacy" in programming languages, similar to the basic English literacy and mathematics skills required by most employers. Python served a central role in this: because of its focus on clean syntax, it was already suitable, and CP4E's goals bore similarities to its predecessor, ABC. The project was funded by DARPA. As of 2007, the CP4E project is inactive, and while Python attempts to be easily learnable and not too arcane in its syntax and semantics, outreach to non-programmers is not an active concern.

BeOpen
In 2000, the Python core development team moved to BeOpen.com to form the BeOpen PythonLabs team. CNRI requested that a version 1.6 be released, summarizing Python's development up to the point at which the development team left CNRI. Consequently, the release schedules for 1.6 and 2.0 had a significant amount of overlap. Python 2.0 was the only release from BeOpen.com. After Python 2.0 was released by BeOpen.com, Guido van Rossum and the other PythonLabs developers joined Digital Creations.
The Python 1.6 release included a new CNRI license that was substantially longer than the CWI license that had been used for earlier releases.  The new license included a clause stating that the license was governed by the laws of the State of Virginia.  The Free Software Foundation argued that the choice-of-law clause was incompatible with the GNU General Public License.  BeOpen, CNRI and the FSF negotiated a change to Python's free-software license that would make it GPL-compatible.  Python 1.6.1 is essentially the same as Python 1.6, with a few minor bug fixes, and with the new GPL-compatible license.

Version 2
Python 2.0, released October 2000, introduced list comprehensions, a feature borrowed from the functional programming languages SETL and Haskell. Python's syntax for this construct is very similar to Haskell's, apart from Haskell's preference for punctuation characters and Python's preference for alphabetic keywords. Python 2.0 also introduced a garbage collector able to collect reference cycles.
Python 2.1 was close to Python 1.6.1, as well as Python 2.0. Its license was renamed Python Software Foundation License. All code, documentation and specifications added, from the time of Python 2.1's alpha release on, is owned by the Python Software Foundation (PSF), a nonprofit organization formed in 2001, modeled after the Apache Software Foundation. The release included a change to the language specification to support nested scopes, like other statically scoped languages. (The feature was turned off by default, and not required, until Python 2.2.)
Python 2.2 was released in December 2001; a major innovation was the unification of Python's types (types written in C) and classes (types written in Python) into one hierarchy. This single unification made Python's object model purely and consistently object oriented. Also added were generators which were inspired by Icon.

Python 2.5 was released in September 2006 and introduced the with statement, which encloses a code block within a context manager (for example, acquiring a lock before the block of code is run and releasing the lock afterwards, or opening a file and then closing it), allowing resource acquisition is initialization (RAII)-like behavior and replacing a common try/finally idiom.
Python 2.6 was released to coincide with Python 3.0, and included some features from that release, as well as a "warnings" mode that highlighted the use of features that were removed in Python 3.0. Similarly, Python 2.7 coincided with and included features from Python 3.1, which was released on June 26, 2009.
Parallel 2.x and 3.x releases then ceased, and Python 2.7 was the last release in the 2.x series. In November 2014, it was announced that Python 2.7 would be supported until 2020, but users were encouraged to move to Python 3 as soon as possible. Python 2.7 support ended on January 1, 2020, along with code freeze of 2.7 development branch. A final release, 2.7.18, occurred on April 20, 2020, and included fixes for critical bugs and release blockers. This marked the end-of-life of Python 2.

Version 3
Python 3.0 (also called "Python 3000" or "Py3K") was released on December 3, 2008. It was designed to rectify fundamental design flaws in the language – the changes required could not be implemented while retaining full backwards compatibility with the 2.x series, which necessitated a new major version number.  The guiding principle of Python 3 was: "reduce feature duplication by removing old ways of doing things".
Python 3.0 was developed with the same philosophy as in prior versions.  However, as Python had accumulated new and redundant ways to program the same task, Python 3.0 had an emphasis on removing duplicative constructs and modules, in keeping with the Zen of Python: "There should be one— and preferably only one —obvious way to do it".
Nonetheless, Python 3.0 remained a multi-paradigm language.  Coders could still follow object-oriented, structured, and functional programming paradigms, among others, but within such broad choices, the details were intended to be more obvious in Python 3.0 than they were in Python 2.x.

Compatibility
Python 3.0 broke backward compatibility, and much Python 2 code does not run unmodified on Python 3. Python's dynamic typing combined with the plans to change the semantics of certain methods of dictionaries, for example, made perfect mechanical translation from Python 2.x to Python 3.0 very difficult. A tool called "2to3" does the parts of translation that can be done automatically.  At this, 2to3 appeared to be fairly successful, though an early review noted that there were aspects of translation that such a tool would never be able to handle. Prior to the roll-out of Python 3, projects requiring compatibility with both the 2.x and 3.x series were recommended to have one source (for the 2.x series), and produce releases for the Python 3.x platform using 2to3. Edits to the Python 3.x code were discouraged for so long as the code needed to run on Python 2.x.  This is no longer recommended; as of 2012 the preferred approach was to create a single code base that can run under both Python 2 and 3 using compatibility modules.

Features
Some of the major changes included for Python 3.0 were:

Changing print so that it is a built-in function, not a statement.  This made it easier to change a module to use a different print function, as well as making the syntax more regular.  In Python 2.6 and 2.7 print() is available as a built-in but is masked by the print statement syntax, which can be disabled by entering from __future__ import print_function at the top of the file
Removal of the Python 2 input function, and the renaming of the raw_input function to input. Python 3's input function behaves like Python 2's raw_input function, in that the input is always returned as a string rather than being evaluated as an expression
Moving reduce (but not map or filter) out of the built-in namespace and into functools (the rationale being code that uses reduce is less readable than code that uses a for loop and accumulator variable)
Adding support for optional function annotations that can be used for informal type declarations or other purposes
Unifying the str/unicode types, representing text, and introducing a separate immutable bytes type; and a mostly corresponding mutable bytearray type, both of which represent arrays of bytes
Removing backward-compatibility features, including old-style classes, string exceptions, and implicit relative imports
A change in integer division functionality: in Python 2, integer division always returns an integer. For example 5 / 2 is 2; whereas in Python 3, 5 / 2 is 2.5. (In both Python 2 – 2.2 onwards – and Python 3, a separate operator exists to provide the old behavior: 5 // 2 is 2)
Allowing non-ASCII letters to be used in identifiers, such as in smörgåsbord
Subsequent releases in the Python 3.x series have included additional, substantial new features; all ongoing development of the language is done in the 3.x series.

Table of versions
Releases before numbered versions:

Implementation started – December, 1989
Internal releases at Centrum Wiskunde & Informatica – 1990

Table notes:

Support
See also
History of software engineering

References
External links
Guido Van Rossum blog on Python's History

## Related Articles

### Internal Links

- [ABC (programming language)](https://en.wikipedia.org/wiki/ABC_(programming_language))
- [Amoeba (operating system)](https://en.wikipedia.org/wiki/Amoeba_(operating_system))
- [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- [The Apache Software Foundation](https://en.wikipedia.org/wiki/The_Apache_Software_Foundation)
- [BBC Television](https://en.wikipedia.org/wiki/BBC_Television)
- [Backporting](https://en.wikipedia.org/wiki/Backporting)
- [Benevolent dictator for life](https://en.wikipedia.org/wiki/Benevolent_dictator_for_life)
- [Byte](https://en.wikipedia.org/wiki/Byte)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Centrum Wiskunde & Informatica](https://en.wikipedia.org/wiki/Centrum_Wiskunde_%26_Informatica)
- [Freeze (software engineering)](https://en.wikipedia.org/wiki/Freeze_(software_engineering))
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Complex number](https://en.wikipedia.org/wiki/Complex_number)
- [Computer file](https://en.wikipedia.org/wiki/Computer_file)
- [Corporation for National Research Initiatives](https://en.wikipedia.org/wiki/Corporation_for_National_Research_Initiatives)
- [Cycle detection](https://en.wikipedia.org/wiki/Cycle_detection)
- [DARPA](https://en.wikipedia.org/wiki/DARPA)
- [Information hiding](https://en.wikipedia.org/wiki/Information_hiding)
- [Data type](https://en.wikipedia.org/wiki/Data_type)
- [Internet forum](https://en.wikipedia.org/wiki/Internet_forum)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [End-of-life product](https://en.wikipedia.org/wiki/End-of-life_product)
- [Exception handling](https://en.wikipedia.org/wiki/Exception_handling)
- [Filter (higher-order function)](https://en.wikipedia.org/wiki/Filter_(higher-order_function))
- [Fold (higher-order function)](https://en.wikipedia.org/wiki/Fold_(higher-order_function))
- [Free-software license](https://en.wikipedia.org/wiki/Free-software_license)
- [Free Software Foundation](https://en.wikipedia.org/wiki/Free_Software_Foundation)
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [GNU General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License)
- [Garbage collection (computer science)](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science))
- [Generator (computer programming)](https://en.wikipedia.org/wiki/Generator_(computer_programming))
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Gradual typing](https://en.wikipedia.org/wiki/Gradual_typing)
- [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [History of software engineering](https://en.wikipedia.org/wiki/History_of_software_engineering)
- [Icon (programming language)](https://en.wikipedia.org/wiki/Icon_(programming_language))
- [Inheritance (object-oriented programming)](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
- [Division (mathematics)](https://en.wikipedia.org/wiki/Division_(mathematics))
- [Intrinsic function](https://en.wikipedia.org/wiki/Intrinsic_function)
- [Named parameter](https://en.wikipedia.org/wiki/Named_parameter)
- [Law](https://en.wikipedia.org/wiki/Law)
- [Lisp (programming language)](https://en.wikipedia.org/wiki/Lisp_(programming_language))
- [List comprehension](https://en.wikipedia.org/wiki/List_comprehension)
- [Lock (computer science)](https://en.wikipedia.org/wiki/Lock_(computer_science))
- [Map (higher-order function)](https://en.wikipedia.org/wiki/Map_(higher-order_function))
- [Memory management](https://en.wikipedia.org/wiki/Memory_management)
- [Modula-3](https://en.wikipedia.org/wiki/Modula-3)
- [Modular programming](https://en.wikipedia.org/wiki/Modular_programming)
- [Monty Python's Flying Circus](https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus)
- [Comparison of multi-paradigm programming languages](https://en.wikipedia.org/wiki/Comparison_of_multi-paradigm_programming_languages)
- [Name mangling](https://en.wikipedia.org/wiki/Name_mangling)
- [Nonprofit organization](https://en.wikipedia.org/wiki/Nonprofit_organization)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Patch (computing)](https://en.wikipedia.org/wiki/Patch_(computing))
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Punctuation](https://en.wikipedia.org/wiki/Punctuation)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation)
- [Python Software Foundation License](https://en.wikipedia.org/wiki/Python_Software_Foundation_License)
- [Reference counting](https://en.wikipedia.org/wiki/Reference_counting)
- [Resource acquisition is initialization](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization)
- [Reston, Virginia](https://en.wikipedia.org/wiki/Reston,_Virginia)
- [SETL](https://en.wikipedia.org/wiki/SETL)
- [Source-to-source compiler](https://en.wikipedia.org/wiki/Source-to-source_compiler)
- [Virginia](https://en.wikipedia.org/wiki/Virginia)
- [Scope (computer science)](https://en.wikipedia.org/wiki/Scope_(computer_science))
- [Structured programming](https://en.wikipedia.org/wiki/Structured_programming)
- [Netherlands](https://en.wikipedia.org/wiki/Netherlands)
- [Unicode](https://en.wikipedia.org/wiki/Unicode)
- [Virginia](https://en.wikipedia.org/wiki/Virginia)
- [Zen of Python](https://en.wikipedia.org/wiki/Zen_of_Python)
- [Zope](https://en.wikipedia.org/wiki/Zope)
- [Talk:History of Python](https://en.wikipedia.org/wiki/Talk:History_of_Python)
- [Category:Articles containing potentially dated statements from 2007](https://en.wikipedia.org/wiki/Category:Articles_containing_potentially_dated_statements_from_2007)
- [Category:Articles to be expanded from March 2024](https://en.wikipedia.org/wiki/Category:Articles_to_be_expanded_from_March_2024)
- [Category:Use American English from May 2024](https://en.wikipedia.org/wiki/Category:Use_American_English_from_May_2024)
- [Category:Use mdy dates from September 2015](https://en.wikipedia.org/wiki/Category:Use_mdy_dates_from_September_2015)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:29:45.303832+00:00_