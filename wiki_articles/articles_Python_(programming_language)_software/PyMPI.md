# PyMPI

## Article Metadata

- **Last Updated:** 2024-12-14T19:56:08.951979+00:00
- **Original Article:** [PyMPI](https://en.wikipedia.org/wiki/PyMPI)
- **Language:** en
- **Page ID:** 3761499

## Summary

pyMPI is a software project that integrates the Message Passing Interface (MPI) into the Python interpreter.
It allows one to write parallel programs using the Python language.
It has not been updated since 2013-04-17.

## Categories

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

## Related Articles

### Internal Links

- [Message Passing Interface](https://en.wikipedia.org/wiki/Message_Passing_Interface)
- [Parallel computing](https://en.wikipedia.org/wiki/Parallel_computing)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [SourceForge](https://en.wikipedia.org/wiki/SourceForge)
- [Wikipedia:Deletion policy](https://en.wikipedia.org/wiki/Wikipedia:Deletion_policy)
- [Wikipedia:Independent sources](https://en.wikipedia.org/wiki/Wikipedia:Independent_sources)
- [Wikipedia:Merging](https://en.wikipedia.org/wiki/Wikipedia:Merging)
- [Wikipedia:Notability (organizations and companies)](https://en.wikipedia.org/wiki/Wikipedia:Notability_(organizations_and_companies))
- [Wikipedia:Redirect](https://en.wikipedia.org/wiki/Wikipedia:Redirect)
- [Wikipedia:Reliable sources](https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from February 2015](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_February_2015)
- [Category:Articles with topics of unclear notability from February 2015](https://en.wikipedia.org/wiki/Category:Articles_with_topics_of_unclear_notability_from_February_2015)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:56:08.951979+00:00_