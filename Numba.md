# Numba

_Last updated: 2024-12-14T15:07:14.816984_

**Original Article:** [Numba](https://en.wikipedia.org/wiki/Numba)

**Summary:** Numba is an open-source JIT compiler that translates a subset of Python and NumPy into fast machine code using LLVM, via the llvmlite Python package. It offers a range of options for parallelising Python code for CPUs and GPUs, often with only minor code changes.
Numba was started by Travis Oliphant in 2012 and has since been under active development at its repository in GitHub with frequent releases. The project is driven by developers at Anaconda, Inc., with support by DARPA, the Gordon and Be

## Categories
- Category:All articles lacking reliable references
- Category:Articles lacking reliable references from November 2024
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Python (programming language)
- Category:Python (programming language) implementations
- Category:Short description is different from Wikidata

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