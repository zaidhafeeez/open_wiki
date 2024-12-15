# PyMPI

## Metadata
- **Last Updated:** 2024-11-26 12:58:12 UTC
- **Original Article:** [PyMPI](https://en.wikipedia.org/wiki/PyMPI)
- **Language:** en
- **Page ID:** 3761499

## Summary
pyMPI is a software project that integrates the Message Passing Interface (MPI) into the Python interpreter.
It allows one to write parallel programs using the Python language.
It has not been updated since 2013-04-17.

## Categories
This article belongs to the following categories:

- Category:All articles needing additional references
- Category:All articles with topics of unclear notability
- Category:Articles needing additional references from February 2015
- Category:Articles with topics of unclear notability from February 2015
- Category:Products articles with topics of unclear notability
- Category:Python (programming language) software

## Table of Contents

- Example of usage
- References
- External links

## Content

pyMPI is a software project that integrates the Message Passing Interface (MPI) into the Python interpreter.
It allows one to write parallel programs using the Python language.
It has not been updated since 2013-04-17.

Example of usage
This python program:

$ mpirun -np 3 pyMPI
> import mpi
> print "Hi, I'm process #%d" % mpi.rank

will print this output:

Hi, I'm process #0
Hi, I'm process #1
Hi, I'm process #2

The -np parameter given to mpirun tells mpi to use 3 processes, and each process in its turn prints its output on the screen.

References
External links
PyMPI on SourceForge

## Archive Info
- **Archived on:** 2024-12-15 20:28:01 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 591 bytes
- **Word Count:** 102 words
