# Stackless Python

## Metadata
- **Last Updated:** 2024-12-03 06:57:40 UTC
- **Original Article:** [Stackless Python](https://en.wikipedia.org/wiki/Stackless_Python)
- **Language:** en
- **Page ID:** 2009536

## Summary
Stackless Python, or Stackless, is a Python programming language interpreter, so named because it avoids depending on the C call stack for its own stack. In practice, Stackless Python uses the C stack, but the stack is cleared between function calls. The most prominent feature of Stackless is microthreads, which avoid much of the overhead associated with usual operating system threads. In addition to Python features, Stackless also adds support for coroutines, communication channels, and task serialization.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 20:27:21 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2846 bytes
- **Word Count:** 426 words
