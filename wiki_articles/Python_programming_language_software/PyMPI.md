---
title: PyMPI
url: https://en.wikipedia.org/wiki/PyMPI
language: en
categories: ["Category:All articles needing additional references", "Category:All articles with topics of unclear notability", "Category:Articles needing additional references from February 2015", "Category:Articles with topics of unclear notability from February 2015", "Category:Products articles with topics of unclear notability", "Category:Python (programming language) software"]
references: 0
last_modified: 2024-11-26T12:58:12Z
---

# PyMPI

## Summary

pyMPI is a software project that integrates the Message Passing Interface (MPI) into the Python interpreter.
It allows one to write parallel programs using the Python language.
It has not been updated since 2013-04-17.

## Full Content

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
