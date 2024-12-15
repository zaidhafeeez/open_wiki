# CPython

## Metadata
- **Last Updated:** 2024-12-10 14:27:49 UTC
- **Original Article:** [CPython](https://en.wikipedia.org/wiki/CPython)
- **Language:** en
- **Page ID:** 1984246

## Summary
CPython is the reference implementation of the Python programming language. Written in C and Python, CPython is the default and most widely used implementation of the Python language.
CPython can be defined as both an interpreter and a compiler as it compiles Python code into bytecode before interpreting it. It has a foreign function interface with several languages, including C, in which one must explicitly write bindings in a language other than Python.

## Categories
This article belongs to the following categories:

- Category:All Wikipedia articles in need of updating
- Category:All articles covered by WikiProject Wikify
- Category:All articles lacking reliable references
- Category:All articles needing rewrite
- Category:All articles with bare URLs for citations
- Category:All articles with unsourced statements
- Category:Articles covered by WikiProject Wikify from September 2022
- Category:Articles lacking reliable references from November 2010
- Category:Articles needing cleanup from September 2022
- Category:Articles with bare URLs for citations from September 2022
- Category:Articles with multiple maintenance issues
- Category:Articles with short description
- Category:Articles with unsourced statements from August 2019
- Category:CS1 errors: bare URL
- Category:CS1 errors: missing title
- Category:Free and open source compilers
- Category:Free and open source interpreters
- Category:Free software programmed in C
- Category:Free software programmed in Python
- Category:Python (programming language) implementations
- Category:Short description matches Wikidata
- Category:Software using the PSF license
- Category:Stack-based virtual machines
- Category:Wikipedia articles in need of updating from April 2021
- Category:Wikipedia articles in need of updating from June 2022
- Category:Wikipedia articles in need of updating from June 2023
- Category:Wikipedia articles in need of updating from June 2024
- Category:Wikipedia articles in need of updating from March 2022
- Category:Wikipedia articles in need of updating from November 2024
- Category:Wikipedia articles in need of updating from October 2024
- Category:Wikipedia articles needing rewrite from January 2020
- Category:Wikipedia articles scheduled for update tagging

## Table of Contents

- Design
- History
- Distribution
- Alternatives
- References
- Further reading
- External links

## Content

CPython is the reference implementation of the Python programming language. Written in C and Python, CPython is the default and most widely used implementation of the Python language.
CPython can be defined as both an interpreter and a compiler as it compiles Python code into bytecode before interpreting it. It has a foreign function interface with several languages, including C, in which one must explicitly write bindings in a language other than Python.

Design
A particular feature of CPython is that it makes use of a global interpreter lock (GIL) on each CPython interpreter process, which means that within a single process, only one thread may be processing Python bytecode at any one time. This does not mean that there is no point in multithreading; the most common multithreading scenario is where threads are mostly waiting on external processes to complete.
This can happen when multiple threads are servicing separate clients. One thread may be waiting for a client to reply, and another may be waiting for a database query to execute, while the third thread is actually processing Python code.
However, the GIL does mean that CPython is not suitable for processes that implement CPU-intensive algorithms in Python code that could potentially be distributed across multiple cores.
In real-world applications, situations where the GIL is a significant bottleneck are quite rare. This is because Python is an inherently slow language and is generally not used for CPU-intensive or time-sensitive operations. Python is typically used at the top level and calls functions in libraries to perform specialized tasks. These libraries are generally not written in Python, and Python code in another thread can be executed while a call to one of these underlying processes takes place. The non-Python library being called to perform the CPU-intensive task is not subject to the GIL and may concurrently execute many threads on multiple processors without restriction.
Concurrency of Python code can only be achieved with separate CPython interpreter processes managed by a multitasking operating system. This complicates communication between concurrent Python processes, though the multiprocessing module mitigates this somewhat; it means that applications that really can benefit from concurrent Python-code execution can be implemented with limited overhead.
The presence of the GIL simplifies the implementation of CPython, and makes it easier to implement multi-threaded applications that do not benefit from concurrent Python code execution. However, without a GIL, multiprocessing apps must make sure all common code is thread safe.
Although many proposals have been made to eliminate the GIL, the general consensus has been that in most cases, the advantages of the GIL outweigh the disadvantages; in the few cases where the GIL is a bottleneck, the application should be built around the multiprocessing structure. To help allow more parallelism, an improvement was released in October 2023 to allow a separate GIL per subinterpreter in a single Python process and have been described as "threads with opt-in sharing".
After several debates, a project was launched in 2023 to propose making the GIL optional from version 3.13 of Python, which is scheduled for release in October 2024.

History
Unladen Swallow
Unladen Swallow was an optimization branch of CPython, intended to be fully compatible and significantly faster. It aimed to achieve its goals by supplementing CPython's custom virtual machine with a just-in-time compiler built using LLVM.
The project had stated a goal of a speed improvement by a factor of five over CPython; this goal was not met.
The project was sponsored by Google, and the project owners, Thomas Wouters, Jeffrey Yasskin, and Collin Winter, are full-time Google employees; however, most project contributors were not Google employees. Unladen Swallow was hosted on Google Code.
Like many things regarding the Python language, the name Unladen Swallow is a Monty Python reference, specifically to the joke about the airspeed velocity of unladen swallows in Monty Python and the Holy Grail.
Although it fell short of all published goals, Unladen Swallow did produce some code that got added to the main Python implementation, such as improvements to the cPickle module.
In July 2010, some observers speculated on whether the project was dead or dying since the 2009 Q4 milestone had not yet been released. The traffic on Unladen's mailing list had decreased from 500 messages in January 2010 to fewer than 10 in September 2010. It has also been reported that Unladen lost Google's funding. In November 2010, one of the main developers announced that "Jeffrey and I have been pulled on to other projects of higher importance to Google."
The 2009 Q4 development branch was created on 26 January 2010, but no advertising was made on the website. Further, regarding the long-term plans, and as the project missed the Python 2.7 release, a Python Enhancement Proposal (PEP) was accepted, which proposed a merge of Unladen Swallow into a special py3k-jit branch of Python's official repository. As of July 2010, this work was ongoing. This merging would have taken some time, since Unladen Swallow was originally based on Python 2.6 with which Python 3 broke compatibility (see Python 3000 for more details). However, the PEP was subsequently withdrawn.
In early 2011, it became clear that the project was stopped.

Unladen Swallow release history
2009 Q1
2009 Q2
2009 Q3: reduce memory use, improve speed

Distribution
Officially supported tier-1 platforms are Linux for 64-bit Intel using a GCC toolchain, macOS for 64-bit Intel and ARM, and Microsoft Windows for 32- and 64-bit Intel. Official tier-2 support exists for Linux for 64-bit ARM, wasm32 (Web Assembly) with WASI runtime support, and Linux for 64-bit Intel using a clang toolchain. Official supported tier-3 systems include 64-bit ARM Windows, 64-bit iOS, Raspberry Pi OS (Linux for armv7 with hard float), Linux for 64-bit PowerPC in little-endian mode, and Linux for s390x.
More platforms have working implementations, including:

Unix-like

Special and embedded

Other

PEP 11 lists platforms which are not supported in CPython by the Python Software Foundation. These platforms can still be supported by external ports. These ports include:

External ports not integrated to Python Software Foundation's official version of CPython, with links to its main development site, often include additional modules for platform-specific functionalities, like graphics and sound API for PSP and SMS and camera API for S60. These ports include:

Enterprise Linux
These Python versions are distributed with currently-supported enterprise Linux distributions. The support status of Python in the table refers to support from the Python core team, and not from the distribution maintainer.

Alternatives
CPython is one of several "production-quality" Python implementations including: Jython, written in Java for the Java virtual machine (JVM); PyPy, written in RPython and translated into C; and IronPython, written in C# for the Common Language Infrastructure. There are also several experimental implementations.

References
Further reading
Shaw, Anthony (2021). CPython Internals: Your Guide to the Python 3 Interpreter. Real Python. ISBN 9781775093343.

External links
CPython on GitHub

## Archive Info
- **Archived on:** 2024-12-15 20:39:06 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 7387 bytes
- **Word Count:** 1142 words
