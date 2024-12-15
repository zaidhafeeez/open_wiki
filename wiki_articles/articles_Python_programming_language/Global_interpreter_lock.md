# Global interpreter lock

## Article Metadata

- **Last Updated:** 2024-12-15T03:19:25.242674+00:00
- **Original Article:** [Global interpreter lock](https://en.wikipedia.org/wiki/Global_interpreter_lock)
- **Language:** en
- **Page ID:** 13338864

## Summary

A global interpreter lock (GIL) is a mechanism used in computer-language interpreters to synchronize the execution of threads so that only one native thread (per process) can execute basic operations (such as memory allocation and reference counting) at a time. As a general rule, an interpreter that uses GIL will see only one thread to execute at a time, even if it runs on a multi-core processor, although some implementations provide for CPU intensive code to release the GIL, allowing multiple t

## Categories

- Category:All articles with unsourced statements
- Category:Articles with short description
- Category:Articles with unsourced statements from March 2023
- Category:Concurrency control
- Category:Python (programming language)
- Category:Short description is different from Wikidata

## Table of Contents

- Technical background concepts
- Advantages
- Drawbacks
- Examples
- See also

## Content

A global interpreter lock (GIL) is a mechanism used in computer-language interpreters to synchronize the execution of threads so that only one native thread (per process) can execute basic operations (such as memory allocation and reference counting) at a time. As a general rule, an interpreter that uses GIL will see only one thread to execute at a time, even if it runs on a multi-core processor, although some implementations provide for CPU intensive code to release the GIL, allowing multiple threads to use multiple cores. Some popular interpreters that have GIL are CPython and Ruby MRI.

Technical background concepts
A global interpreter lock (GIL) is a mutual-exclusion lock held by a programming language interpreter thread to avoid sharing code that is not thread-safe with other threads. In implementations with a GIL, there is always one GIL for each interpreter process.
Applications running on implementations with a GIL can be designed to use separate processes to achieve full parallelism, as each process has its own interpreter and in turn has its own GIL. Otherwise, the GIL can be a significant barrier to parallelism.

Advantages
Reasons for employing a global interpreter lock include:

increased speed of single-threaded programs (no necessity to acquire or release locks on all data structures separately),
easy integration of C libraries that usually are not thread-safe,
ease of implementation (having a single GIL is much simpler to implement than a lock-free interpreter or one using fine-grained locks).
A way to get around a GIL is creating a separate interpreter per thread, which is too expensive with most languages.

Drawbacks
Use of a global interpreter lock in a language effectively limits the amount of parallelism reachable through concurrency of a single interpreter process with multiple threads. If the process is almost purely made up of interpreted code and does not make calls outside of the interpreter which block for long periods of time (allowing the GIL to be released by that thread while they process), there is likely to be very little increase in speed when running the process on a multiprocessor machine.  Due to signaling with a CPU-bound thread, it can cause a significant slowdown, even on single processors.  More seriously, when the single native thread calls a blocking OS process (such as disk access), the entire process is blocked, even though other application threads may be waiting.

Examples
Some language implementations that implement a global interpreter lock are CPython, the most widely-used implementation of Python, and Ruby MRI, the reference implementation of Ruby (where it is called Global VM Lock).
JVM-based equivalents of these languages (Jython and JRuby) do not use global interpreter locks. IronPython and IronRuby are implemented on top of Microsoft's Dynamic Language Runtime and also avoid using a GIL.
An example of an interpreted language without a GIL is Tcl, which is used in the benchmarking tool HammerDB.

See also
Green threads
Giant lock


== References ==

## Related Articles

### Internal Links

- [CPU-bound](https://en.wikipedia.org/wiki/CPU-bound)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Concurrency (computer science)](https://en.wikipedia.org/wiki/Concurrency_(computer_science))
- [David M. Beazley](https://en.wikipedia.org/wiki/David_M._Beazley)
- [Dr. Dobb's Journal](https://en.wikipedia.org/wiki/Dr._Dobb%27s_Journal)
- [Dynamic Language Runtime](https://en.wikipedia.org/wiki/Dynamic_Language_Runtime)
- [Giant lock](https://en.wikipedia.org/wiki/Giant_lock)
- [Green thread](https://en.wikipedia.org/wiki/Green_thread)
- [HammerDB](https://en.wikipedia.org/wiki/HammerDB)
- [Interpreter (computing)](https://en.wikipedia.org/wiki/Interpreter_(computing))
- [IronPython](https://en.wikipedia.org/wiki/IronPython)
- [IronRuby](https://en.wikipedia.org/wiki/IronRuby)
- [JRuby](https://en.wikipedia.org/wiki/JRuby)
- [Java virtual machine](https://en.wikipedia.org/wiki/Java_virtual_machine)
- [Jython](https://en.wikipedia.org/wiki/Jython)
- [Lock (computer science)](https://en.wikipedia.org/wiki/Lock_(computer_science))
- [Memory management](https://en.wikipedia.org/wiki/Memory_management)
- [Microsoft](https://en.wikipedia.org/wiki/Microsoft)
- [Multi-core processor](https://en.wikipedia.org/wiki/Multi-core_processor)
- [Multiprocessing](https://en.wikipedia.org/wiki/Multiprocessing)
- [Mutual exclusion](https://en.wikipedia.org/wiki/Mutual_exclusion)
- [Parallel computing](https://en.wikipedia.org/wiki/Parallel_computing)
- [Process (computing)](https://en.wikipedia.org/wiki/Process_(computing))
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Reference counting](https://en.wikipedia.org/wiki/Reference_counting)
- [Reference implementation](https://en.wikipedia.org/wiki/Reference_implementation)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Ruby MRI](https://en.wikipedia.org/wiki/Ruby_MRI)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Thread safety](https://en.wikipedia.org/wiki/Thread_safety)
- [Thread (computing)](https://en.wikipedia.org/wiki/Thread_(computing))
- [Thread (computing)](https://en.wikipedia.org/wiki/Thread_(computing))
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Category:Articles with unsourced statements from March 2023](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_March_2023)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:19:25.242674+00:00_