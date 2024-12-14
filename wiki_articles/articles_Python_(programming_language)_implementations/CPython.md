# CPython

## Article Metadata

- **Last Updated:** 2024-12-14T19:48:39.454458+00:00
- **Original Article:** [CPython](https://en.wikipedia.org/wiki/CPython)
- **Language:** en
- **Page ID:** 1984246

## Summary

CPython is the reference implementation of the Python programming language. Written in C and Python, CPython is the default and most widely used implementation of the Python language.
CPython can be defined as both an interpreter and a compiler as it compiles Python code into bytecode before interpreting it. It has a foreign function interface with several languages, including C, in which one must explicitly write bindings in a language other than Python.

## Categories

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

## Related Articles

### Internal Links

- [AROS Research Operating System](https://en.wikipedia.org/wiki/AROS_Research_Operating_System)
- [Alex Martelli](https://en.wikipedia.org/wiki/Alex_Martelli)
- [Amiga](https://en.wikipedia.org/wiki/Amiga)
- [Android (operating system)](https://en.wikipedia.org/wiki/Android_(operating_system))
- [IOS](https://en.wikipedia.org/wiki/IOS)
- [Asynchronous Server Gateway Interface](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface)
- [Syllable Desktop](https://en.wikipedia.org/wiki/Syllable_Desktop)
- [BeOS](https://en.wikipedia.org/wiki/BeOS)
- [Berkeley Software Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution)
- [BlackBerry 10](https://en.wikipedia.org/wiki/BlackBerry_10)
- [Bytecode](https://en.wikipedia.org/wiki/Bytecode)
- [CLPython](https://en.wikipedia.org/wiki/CLPython)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [CentOS](https://en.wikipedia.org/wiki/CentOS)
- [CircuitPython](https://en.wikipedia.org/wiki/CircuitPython)
- [Common Language Infrastructure](https://en.wikipedia.org/wiki/Common_Language_Infrastructure)
- [Compiler](https://en.wikipedia.org/wiki/Compiler)
- [Computing platform](https://en.wikipedia.org/wiki/Computing_platform)
- [Cython](https://en.wikipedia.org/wiki/Cython)
- [DJGPP](https://en.wikipedia.org/wiki/DJGPP)
- [DOS](https://en.wikipedia.org/wiki/DOS)
- [Darwin (operating system)](https://en.wikipedia.org/wiki/Darwin_(operating_system))
- [Database](https://en.wikipedia.org/wiki/Database)
- [Debian](https://en.wikipedia.org/wiki/Debian)
- [End-of-life product](https://en.wikipedia.org/wiki/End-of-life_product)
- [English language](https://en.wikipedia.org/wiki/English_language)
- [Eric (software)](https://en.wikipedia.org/wiki/Eric_(software))
- [Foreign function interface](https://en.wikipedia.org/wiki/Foreign_function_interface)
- [FreeBSD](https://en.wikipedia.org/wiki/FreeBSD)
- [GP2X](https://en.wikipedia.org/wiki/GP2X)
- [GameCube](https://en.wikipedia.org/wiki/GameCube)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Global interpreter lock](https://en.wikipedia.org/wiki/Global_interpreter_lock)
- [Google](https://en.wikipedia.org/wiki/Google)
- [Google Developers](https://en.wikipedia.org/wiki/Google_Developers)
- [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
- [HP-UX](https://en.wikipedia.org/wiki/HP-UX)
- [History of Python](https://en.wikipedia.org/wiki/History_of_Python)
- [IBM AIX](https://en.wikipedia.org/wiki/IBM_AIX)
- [IBM i](https://en.wikipedia.org/wiki/IBM_i)
- [IDLE](https://en.wikipedia.org/wiki/IDLE)
- [IPodLinux](https://en.wikipedia.org/wiki/IPodLinux)
- [IRIX](https://en.wikipedia.org/wiki/IRIX)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Illumos](https://en.wikipedia.org/wiki/Illumos)
- [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment)
- [Interpreter (computing)](https://en.wikipedia.org/wiki/Interpreter_(computing))
- [IronPython](https://en.wikipedia.org/wiki/IronPython)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Java virtual machine](https://en.wikipedia.org/wiki/Java_virtual_machine)
- [Just-in-time compilation](https://en.wikipedia.org/wiki/Just-in-time_compilation)
- [Jython](https://en.wikipedia.org/wiki/Jython)
- [LLVM](https://en.wikipedia.org/wiki/LLVM)
- [Language binding](https://en.wikipedia.org/wiki/Language_binding)
- [Linux](https://en.wikipedia.org/wiki/Linux)
- [List of Python software](https://en.wikipedia.org/wiki/List_of_Python_software)
- [Comparison of integrated development environments](https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments)
- [Minix](https://en.wikipedia.org/wiki/Minix)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [Mac OS 9](https://en.wikipedia.org/wiki/Mac_OS_9)
- [MicroPython](https://en.wikipedia.org/wiki/MicroPython)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Monty Python](https://en.wikipedia.org/wiki/Monty_Python)
- [Monty Python and the Holy Grail](https://en.wikipedia.org/wiki/Monty_Python_and_the_Holy_Grail)
- [MorphOS](https://en.wikipedia.org/wiki/MorphOS)
- [Computer multitasking](https://en.wikipedia.org/wiki/Computer_multitasking)
- [Multithreading (computer architecture)](https://en.wikipedia.org/wiki/Multithreading_(computer_architecture))
- [NetBSD](https://en.wikipedia.org/wiki/NetBSD)
- [Ninja-IDE](https://en.wikipedia.org/wiki/Ninja-IDE)
- [Nintendo DS](https://en.wikipedia.org/wiki/Nintendo_DS)
- [Nokia 770 Internet Tablet](https://en.wikipedia.org/wiki/Nokia_770_Internet_Tablet)
- [Nokia N800](https://en.wikipedia.org/wiki/Nokia_N800)
- [Nokia N810](https://en.wikipedia.org/wiki/Nokia_N810)
- [Nokia N900](https://en.wikipedia.org/wiki/Nokia_N900)
- [Numba](https://en.wikipedia.org/wiki/Numba)
- [O'Reilly Media](https://en.wikipedia.org/wiki/O%27Reilly_Media)
- [OS/2](https://en.wikipedia.org/wiki/OS/2)
- [OS/390](https://en.wikipedia.org/wiki/OS/390)
- [OpenBSD](https://en.wikipedia.org/wiki/OpenBSD)
- [OpenVMS](https://en.wikipedia.org/wiki/OpenVMS)
- [Openmoko](https://en.wikipedia.org/wiki/Openmoko)
- [Overhead (computing)](https://en.wikipedia.org/wiki/Overhead_(computing))
- [Palm OS](https://en.wikipedia.org/wiki/Palm_OS)
- [Parallel computing](https://en.wikipedia.org/wiki/Parallel_computing)
- [Plan 9 from Bell Labs](https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs)
- [PlayStation 2](https://en.wikipedia.org/wiki/PlayStation_2)
- [PlayStation 3](https://en.wikipedia.org/wiki/PlayStation_3)
- [PlayStation Portable](https://en.wikipedia.org/wiki/PlayStation_Portable)
- [Pocket PC](https://en.wikipedia.org/wiki/Pocket_PC)
- [Process (computing)](https://en.wikipedia.org/wiki/Process_(computing))
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Programming language implementation](https://en.wikipedia.org/wiki/Programming_language_implementation)
- [Psion (company)](https://en.wikipedia.org/wiki/Psion_(company))
- [Psyco](https://en.wikipedia.org/wiki/Psyco)
- [PyCharm](https://en.wikipedia.org/wiki/PyCharm)
- [PyDev](https://en.wikipedia.org/wiki/PyDev)
- [PyPy](https://en.wikipedia.org/wiki/PyPy)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [History of Python](https://en.wikipedia.org/wiki/History_of_Python)
- [Python Conference](https://en.wikipedia.org/wiki/Python_Conference)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation)
- [Python Software Foundation License](https://en.wikipedia.org/wiki/Python_Software_Foundation_License)
- [Python for S60](https://en.wikipedia.org/wiki/Python_for_S60)
- [QNX](https://en.wikipedia.org/wiki/QNX)
- [RISC OS](https://en.wikipedia.org/wiki/RISC_OS)
- [Raspberry Pi OS](https://en.wikipedia.org/wiki/Raspberry_Pi_OS)
- [Red Hat Enterprise Linux](https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux)
- [Reference implementation](https://en.wikipedia.org/wiki/Reference_implementation)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Linux on IBM Z](https://en.wikipedia.org/wiki/Linux_on_IBM_Z)
- [S60 (software platform)](https://en.wikipedia.org/wiki/S60_(software_platform))
- [Sharp Zaurus](https://en.wikipedia.org/wiki/Sharp_Zaurus)
- [Shed Skin](https://en.wikipedia.org/wiki/Shed_Skin)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Oracle Solaris](https://en.wikipedia.org/wiki/Oracle_Solaris)
- [Spyder (software)](https://en.wikipedia.org/wiki/Spyder_(software))
- [Stackless Python](https://en.wikipedia.org/wiki/Stackless_Python)
- [SUSE Linux Enterprise](https://en.wikipedia.org/wiki/SUSE_Linux_Enterprise)
- [Swallow](https://en.wikipedia.org/wiki/Swallow)
- [Symbian](https://en.wikipedia.org/wiki/Symbian)
- [Thread (computing)](https://en.wikipedia.org/wiki/Thread_(computing))
- [Tru64 UNIX](https://en.wikipedia.org/wiki/Tru64_UNIX)
- [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [Virtual machine](https://en.wikipedia.org/wiki/Virtual_machine)
- [VxWorks](https://en.wikipedia.org/wiki/VxWorks)
- [WebAssembly](https://en.wikipedia.org/wiki/WebAssembly)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [Windows 2000](https://en.wikipedia.org/wiki/Windows_2000)
- [Windows 3.x](https://en.wikipedia.org/wiki/Windows_3.x)
- [Windows 7](https://en.wikipedia.org/wiki/Windows_7)
- [Windows 8](https://en.wikipedia.org/wiki/Windows_8)
- [Windows 9x](https://en.wikipedia.org/wiki/Windows_9x)
- [Windows CE](https://en.wikipedia.org/wiki/Windows_CE)
- [Windows NT 4.0](https://en.wikipedia.org/wiki/Windows_NT_4.0)
- [Windows Vista](https://en.wikipedia.org/wiki/Windows_Vista)
- [Windows XP](https://en.wikipedia.org/wiki/Windows_XP)
- [Kodi (software)](https://en.wikipedia.org/wiki/Kodi_(software))
- [Xbox (console)](https://en.wikipedia.org/wiki/Xbox_(console))
- [Z/OS](https://en.wikipedia.org/wiki/Z/OS)
- [Talk:CPython](https://en.wikipedia.org/wiki/Talk:CPython)
- [User:Citation bot](https://en.wikipedia.org/wiki/User:Citation_bot)
- [Wikipedia:Bare URLs](https://en.wikipedia.org/wiki/Wikipedia:Bare_URLs)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:Link rot](https://en.wikipedia.org/wiki/Wikipedia:Link_rot)
- [Wikipedia:Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style)
- [Wikipedia:Manual of Style/Dates and numbers](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Dates_and_numbers)
- [Wikipedia:No original research](https://en.wikipedia.org/wiki/Wikipedia:No_original_research)
- [Wikipedia:ReFill](https://en.wikipedia.org/wiki/Wikipedia:ReFill)
- [Wikipedia:Template index/Sources of articles](https://en.wikipedia.org/wiki/Wikipedia:Template_index/Sources_of_articles)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Cite web](https://en.wikipedia.org/wiki/Template:Cite_web)
- [Template:Python (programming language)](https://en.wikipedia.org/wiki/Template:Python_(programming_language))
- [Template talk:Python (programming language)](https://en.wikipedia.org/wiki/Template_talk:Python_(programming_language))
- [Help:CS1 errors](https://en.wikipedia.org/wiki/Help:CS1_errors)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles covered by WikiProject Wikify from September 2022](https://en.wikipedia.org/wiki/Category:Articles_covered_by_WikiProject_Wikify_from_September_2022)
- [Category:Articles lacking reliable references from November 2010](https://en.wikipedia.org/wiki/Category:Articles_lacking_reliable_references_from_November_2010)
- [Category:Articles needing cleanup from September 2022](https://en.wikipedia.org/wiki/Category:Articles_needing_cleanup_from_September_2022)
- [Category:Articles with bare URLs for citations from September 2022](https://en.wikipedia.org/wiki/Category:Articles_with_bare_URLs_for_citations_from_September_2022)
- [Category:Articles with unsourced statements from August 2019](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_August_2019)
- [Category:Wikipedia articles in need of updating from April 2021](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_in_need_of_updating_from_April_2021)
- [Category:Wikipedia articles in need of updating from June 2022](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_in_need_of_updating_from_June_2022)
- [Category:Wikipedia articles in need of updating from June 2023](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_in_need_of_updating_from_June_2023)
- [Category:Wikipedia articles in need of updating from June 2024](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_in_need_of_updating_from_June_2024)
- [Category:Wikipedia articles in need of updating from March 2022](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_in_need_of_updating_from_March_2022)
- [Category:Wikipedia articles in need of updating from November 2024](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_in_need_of_updating_from_November_2024)
- [Category:Wikipedia articles in need of updating from October 2024](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_in_need_of_updating_from_October_2024)
- [Category:Wikipedia articles needing rewrite from January 2020](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_needing_rewrite_from_January_2020)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:48:39.454458+00:00_