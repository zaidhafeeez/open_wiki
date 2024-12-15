# Stackless Python

## Article Metadata

- **Last Updated:** 2024-12-15T03:43:34.279131+00:00
- **Original Article:** [Stackless Python](https://en.wikipedia.org/wiki/Stackless_Python)
- **Language:** en
- **Page ID:** 2009536

## Summary

Stackless Python, or Stackless, is a Python programming language interpreter, so named because it avoids depending on the C call stack for its own stack. In practice, Stackless Python uses the C stack, but the stack is cleared between function calls. The most prominent feature of Stackless is microthreads, which avoid much of the overhead associated with usual operating system threads. In addition to Python features, Stackless also adds support for coroutines, communication channels, and task se

## Categories

- Category:All articles lacking reliable references
- Category:All articles needing additional references
- Category:Articles lacking reliable references from December 2017
- Category:Articles needing additional references from March 2013
- Category:Articles with multiple maintenance issues
- Category:Articles with short description
- Category:Concurrent computing
- Category:Python (programming language) implementations
- Category:Short description matches Wikidata
- Category:Software using the PSF license

## Table of Contents

- Design
- Use
- See also
- References
- External links

## Content

Stackless Python, or Stackless, is a Python programming language interpreter, so named because it avoids depending on the C call stack for its own stack. In practice, Stackless Python uses the C stack, but the stack is cleared between function calls. The most prominent feature of Stackless is microthreads, which avoid much of the overhead associated with usual operating system threads. In addition to Python features, Stackless also adds support for coroutines, communication channels, and task serialization.

Design
With Stackless Python, a running program is split into microthreads that are managed by the language interpreter itself, not the operating system kernel—context switching and task scheduling is done purely in the interpreter (these are thus also regarded as a form of green thread). Microthreads manage the execution of different subtasks in a program on the same CPU core. Thus, they are an alternative to event-based asynchronous programming and also avoid the overhead of using separate threads for single-core programs (because no mode switching between user mode and kernel mode needs to be done, so CPU usage can be reduced).
Although microthreads make it easier to deal with running subtasks on a single core, Stackless Python does not remove CPython's global interpreter lock (GIL), nor does it use multiple threads and/or processes. So it allows only cooperative multitasking on a shared CPU and not parallelism (preemption was originally not available but is now in some form). To use multiple CPU cores, one would still need to build an interprocess communication system on top of Stackless Python processes.
Due to the considerable number of changes in the source, Stackless Python cannot be installed on a preexisting Python installation as an extension or library. It is instead a complete Python distribution in itself. The majority of Stackless's features have also been implemented in PyPy, a self-hosting Python interpreter and JIT compiler.

Use
Although the whole Stackless is a separate distribution, its switching functionality has been successfully packaged as a CPython extension called greenlet. It is used by a number of libraries (e.g. gevent) to provide a green threading solution for CPython. Python since has received a native solution for green threads: await/async.
Stackless is used extensively in the implementation of the Eve Online massively multiplayer online game as well as in IronPort's mail platform.

See also
Erlang (programming language)
Limbo (programming language)
Go (programming language)
SCOOP (software)

References
External links
Official website 
Stackless Python Documentation for: 3.7-slp, 3.6-slp, 3.5-slp, 3.4-slp, 2.7-slp
stackless on GitHub
Multithreaded Game Scripting with Stackless Python by Harry Kalogirou
Continuations and Stackless Python by Christian Tismer

## Related Articles

### Internal Links

- [Async/await](https://en.wikipedia.org/wiki/Async/await)
- [Asynchronous Server Gateway Interface](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface)
- [CLPython](https://en.wikipedia.org/wiki/CLPython)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Call stack](https://en.wikipedia.org/wiki/Call_stack)
- [Channel (programming)](https://en.wikipedia.org/wiki/Channel_(programming))
- [CircuitPython](https://en.wikipedia.org/wiki/CircuitPython)
- [Context switch](https://en.wikipedia.org/wiki/Context_switch)
- [Cooperative multitasking](https://en.wikipedia.org/wiki/Cooperative_multitasking)
- [Coroutine](https://en.wikipedia.org/wiki/Coroutine)
- [Cython](https://en.wikipedia.org/wiki/Cython)
- [Eric (software)](https://en.wikipedia.org/wiki/Eric_(software))
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Eve Online](https://en.wikipedia.org/wiki/Eve_Online)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Global interpreter lock](https://en.wikipedia.org/wiki/Global_interpreter_lock)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Green thread](https://en.wikipedia.org/wiki/Green_thread)
- [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
- [IDLE](https://en.wikipedia.org/wiki/IDLE)
- [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment)
- [Interpreter (computing)](https://en.wikipedia.org/wiki/Interpreter_(computing))
- [List of acquisitions by Cisco](https://en.wikipedia.org/wiki/List_of_acquisitions_by_Cisco)
- [IronPython](https://en.wikipedia.org/wiki/IronPython)
- [Just-in-time compilation](https://en.wikipedia.org/wiki/Just-in-time_compilation)
- [Jython](https://en.wikipedia.org/wiki/Jython)
- [Kernel (operating system)](https://en.wikipedia.org/wiki/Kernel_(operating_system))
- [Library (computing)](https://en.wikipedia.org/wiki/Library_(computing))
- [Limbo (programming language)](https://en.wikipedia.org/wiki/Limbo_(programming_language))
- [Linux](https://en.wikipedia.org/wiki/Linux)
- [List of Python software](https://en.wikipedia.org/wiki/List_of_Python_software)
- [Comparison of integrated development environments](https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [MicroPython](https://en.wikipedia.org/wiki/MicroPython)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Microthread](https://en.wikipedia.org/wiki/Microthread)
- [Ninja-IDE](https://en.wikipedia.org/wiki/Ninja-IDE)
- [Numba](https://en.wikipedia.org/wiki/Numba)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Parallel computing](https://en.wikipedia.org/wiki/Parallel_computing)
- [Plug-in (computing)](https://en.wikipedia.org/wiki/Plug-in_(computing))
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Programming language implementation](https://en.wikipedia.org/wiki/Programming_language_implementation)
- [Psyco](https://en.wikipedia.org/wiki/Psyco)
- [PyCharm](https://en.wikipedia.org/wiki/PyCharm)
- [PyDev](https://en.wikipedia.org/wiki/PyDev)
- [PyPy](https://en.wikipedia.org/wiki/PyPy)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Conference](https://en.wikipedia.org/wiki/Python_Conference)
- [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation)
- [Python Software Foundation License](https://en.wikipedia.org/wiki/Python_Software_Foundation_License)
- [Python for S60](https://en.wikipedia.org/wiki/Python_for_S60)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [SCOOP (software)](https://en.wikipedia.org/wiki/SCOOP_(software))
- [Scheduling (computing)](https://en.wikipedia.org/wiki/Scheduling_(computing))
- [Self-hosting (compilers)](https://en.wikipedia.org/wiki/Self-hosting_(compilers))
- [Serialization](https://en.wikipedia.org/wiki/Serialization)
- [Shed Skin](https://en.wikipedia.org/wiki/Shed_Skin)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Spyder (software)](https://en.wikipedia.org/wiki/Spyder_(software))
- [Thread (computing)](https://en.wikipedia.org/wiki/Thread_(computing))
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [YouTube](https://en.wikipedia.org/wiki/YouTube)
- [Talk:Stackless Python](https://en.wikipedia.org/wiki/Talk:Stackless_Python)
- [Wikipedia:No original research](https://en.wikipedia.org/wiki/Wikipedia:No_original_research)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Python (programming language)](https://en.wikipedia.org/wiki/Template:Python_(programming_language))
- [Template talk:Python (programming language)](https://en.wikipedia.org/wiki/Template_talk:Python_(programming_language))
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles lacking reliable references from December 2017](https://en.wikipedia.org/wiki/Category:Articles_lacking_reliable_references_from_December_2017)
- [Category:Articles needing additional references from March 2013](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_March_2013)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:43:34.279131+00:00_