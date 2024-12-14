# Global interpreter lock

_Last updated: 2024-12-14T15:03:11.681031_

**Original Article:** [Global interpreter lock](https://en.wikipedia.org/wiki/Global_interpreter_lock)

**Summary:** A global interpreter lock (GIL) is a mechanism used in computer-language interpreters to synchronize the execution of threads so that only one native thread (per process) can execute basic operations (such as memory allocation and reference counting) at a time. As a general rule, an interpreter that uses GIL will see only one thread to execute at a time, even if it runs on a multi-core processor, although some implementations provide for CPU intensive code to release the GIL, allowing multiple t

## Categories
- Category:All articles with unsourced statements
- Category:Articles with short description
- Category:Articles with unsourced statements from March 2023
- Category:Concurrency control
- Category:Python (programming language)
- Category:Short description is different from Wikidata

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