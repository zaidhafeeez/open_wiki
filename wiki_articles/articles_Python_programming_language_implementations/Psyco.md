# Psyco

## Metadata
- **Last Updated:** 2024-12-03 06:56:31 UTC
- **Original Article:** [Psyco](https://en.wikipedia.org/wiki/Psyco)
- **Language:** en
- **Page ID:** 1561564

## Summary
Psyco is an unmaintained specializing just-in-time compiler for pre-2.7 Python originally developed by Armin Rigo and further maintained and developed by Christian Tismer. Development ceased in December, 2011.
Psyco ran on BSD-derived operating systems, Linux, Mac OS X and Microsoft Windows using 32-bit Intel-compatible processors. Psyco was written in C and generated only 32-bit x86-based code.
Although Tismer announced on 17 July 2009 that work was being done on a second version of Psyco, a further announcement declared the project "unmaintained and dead" on 12 March 2012 and pointed visitors to PyPy instead. Unlike Psyco, PyPy incorporates an interpreter and a compiler that can generate C, improving its cross-platform compatibility over Psyco.

## Categories
This article belongs to the following categories:

- Category:All Wikipedia articles in need of updating
- Category:All stub articles
- Category:Articles with obsolete information from September 2018
- Category:Articles with short description
- Category:Free and open-source software stubs
- Category:Free software programmed in Python
- Category:Python (programming language) implementations
- Category:Python (programming language) software
- Category:Short description matches Wikidata
- Category:Software using the MIT license

## Table of Contents

- Speed enhancement
- See also
- References
- External links

## Content

Psyco is an unmaintained specializing just-in-time compiler for pre-2.7 Python originally developed by Armin Rigo and further maintained and developed by Christian Tismer. Development ceased in December, 2011.
Psyco ran on BSD-derived operating systems, Linux, Mac OS X and Microsoft Windows using 32-bit Intel-compatible processors. Psyco was written in C and generated only 32-bit x86-based code.
Although Tismer announced on 17 July 2009 that work was being done on a second version of Psyco, a further announcement declared the project "unmaintained and dead" on 12 March 2012 and pointed visitors to PyPy instead. Unlike Psyco, PyPy incorporates an interpreter and a compiler that can generate C, improving its cross-platform compatibility over Psyco.

Speed enhancement
Psyco can noticeably speed up CPU-bound applications. The actual performance depends greatly on the application and varies from a slight slowdown to a 100x speedup.
The average speed improvement is typically in the 1.5-4x range, making Python performance close to languages such as Smalltalk and Scheme, but still slower than compiled languages such as Fortran, C or some other JIT languages like C# and Java.
Psyco also advertises its ease of use: the simplest Psyco optimization involves adding only two lines to the top of a script:

These commands will import the psyco module, and have Psyco optimize the entire script. This approach is best suited to shorter scripts, but demonstrates the minimal amount of work needed to begin applying Psyco optimizations to an existing program.

See also
PyPy
Unladen Swallow
Cython
YARV (Yet another Ruby VM)

References
External links
Psyco on SourceForge
David Mertz's IBM developerWorks article: Make Python run as fast as C with Psyco
psyco notes, Poor Yorick

## Archive Info
- **Archived on:** 2024-12-15 20:39:08 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 1782 bytes
- **Word Count:** 275 words
