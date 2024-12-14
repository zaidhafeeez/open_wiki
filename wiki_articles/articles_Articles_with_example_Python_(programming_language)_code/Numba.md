# Numba

## Article Metadata

- **Last Updated:** 2024-12-14T19:41:46.169768+00:00
- **Original Article:** [Numba](https://en.wikipedia.org/wiki/Numba)
- **Language:** en
- **Page ID:** 41170321

## Summary

Numba is an open-source JIT compiler that translates a subset of Python and NumPy into fast machine code using LLVM, via the llvmlite Python package. It offers a range of options for parallelising Python code for CPUs and GPUs, often with only minor code changes.
Numba was started by Travis Oliphant in 2012 and has since been under active development at its repository in GitHub with frequent releases. The project is driven by developers at Anaconda, Inc., with support by DARPA, the Gordon and Be

## Categories

- Category:All articles lacking reliable references
- Category:Articles lacking reliable references from November 2024
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Python (programming language)
- Category:Python (programming language) implementations
- Category:Short description is different from Wikidata

## Table of Contents

- Example
- GPU support
- Alternative approaches

## Content

Numba is an open-source JIT compiler that translates a subset of Python and NumPy into fast machine code using LLVM, via the llvmlite Python package. It offers a range of options for parallelising Python code for CPUs and GPUs, often with only minor code changes.
Numba was started by Travis Oliphant in 2012 and has since been under active development at its repository in GitHub with frequent releases. The project is driven by developers at Anaconda, Inc., with support by DARPA, the Gordon and Betty Moore Foundation, Intel, Nvidia and AMD, and a community of contributors on GitHub.

Example
Numba can be used by simply applying the numba.jit decorator to a Python function that does numerical computations:

The just-in-time compilation happens transparently when the function is called:

Numba's website  contains many more examples, as well as information on how to get good performance from Numba.

GPU support
Numba can compile Python functions to GPU code. Initially two backends are available:

Nvidia CUDA, see numba.pydata.org/numba-doc/dev/cuda
AMD ROCm HSA, see numba.pydata.org/numba-doc/dev/roc
Since release 0.56.4, AMD ROCm HSA has been officially moved to unmaintained status and a separate repository stub has been created for it.

Alternative approaches
Numba is one approach to make Python fast, by compiling specific functions that contain
Python and NumPy code. Many alternative approaches for fast numeric computing with Python exist, such as Cython, Pythran, and PyPy.


== References ==

## Related Articles

### Internal Links

- [AMD](https://en.wikipedia.org/wiki/AMD)
- [AMD](https://en.wikipedia.org/wiki/AMD)
- [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses)
- [CUDA](https://en.wikipedia.org/wiki/CUDA)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Cython](https://en.wikipedia.org/wiki/Cython)
- [DARPA](https://en.wikipedia.org/wiki/DARPA)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Gordon and Betty Moore Foundation](https://en.wikipedia.org/wiki/Gordon_and_Betty_Moore_Foundation)
- [Heterogeneous System Architecture](https://en.wikipedia.org/wiki/Heterogeneous_System_Architecture)
- [Intel](https://en.wikipedia.org/wiki/Intel)
- [Just-in-time compilation](https://en.wikipedia.org/wiki/Just-in-time_compilation)
- [LLVM](https://en.wikipedia.org/wiki/LLVM)
- [List of numerical-analysis software](https://en.wikipedia.org/wiki/List_of_numerical-analysis_software)
- [NumPy](https://en.wikipedia.org/wiki/NumPy)
- [Nvidia](https://en.wikipedia.org/wiki/Nvidia)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [PyPy](https://en.wikipedia.org/wiki/PyPy)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [ROCm](https://en.wikipedia.org/wiki/ROCm)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Travis Oliphant](https://en.wikipedia.org/wiki/Travis_Oliphant)
- [Wikipedia:No original research](https://en.wikipedia.org/wiki/Wikipedia:No_original_research)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles lacking reliable references from November 2024](https://en.wikipedia.org/wiki/Category:Articles_lacking_reliable_references_from_November_2024)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:41:46.169768+00:00_