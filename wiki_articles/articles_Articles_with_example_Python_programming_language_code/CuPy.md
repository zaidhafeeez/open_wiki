# CuPy

## Metadata
- **Last Updated:** 2024-12-03 08:01:27 UTC
- **Original Article:** [CuPy](https://en.wikipedia.org/wiki/CuPy)
- **Language:** en
- **Page ID:** 71062349

## Summary
CuPy is an open source library for GPU-accelerated computing with Python programming language, providing support for multi-dimensional arrays, sparse matrices, and a variety of numerical algorithms implemented on top of them.
CuPy shares the same API set as NumPy and SciPy, allowing it to be a drop-in replacement to run NumPy/SciPy code on GPU. CuPy supports Nvidia CUDA GPU platform, and AMD ROCm GPU platform starting in v9.0.
CuPy has been initially developed as a backend of Chainer deep learning framework, and later established as an independent project in 2017.
CuPy is a part of the NumPy ecosystem array libraries and is widely adopted to utilize GPU with Python, especially in high-performance computing environments such as Summit, Perlmutter, EULER, and ABCI.
CuPy is a NumFOCUS sponsored project.

## Categories
This article belongs to the following categories:

- Category:Array programming languages
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Free mathematics software
- Category:Free science software
- Category:Numerical analysis software for Linux
- Category:Numerical analysis software for Windows
- Category:Numerical programming languages
- Category:Official website not in Wikidata
- Category:Python (programming language) scientific libraries
- Category:Short description matches Wikidata
- Category:Software using the MIT license

## Table of Contents

- Features
- Examples
- Applications
- See also
- References
- External links

## Content

CuPy is an open source library for GPU-accelerated computing with Python programming language, providing support for multi-dimensional arrays, sparse matrices, and a variety of numerical algorithms implemented on top of them.
CuPy shares the same API set as NumPy and SciPy, allowing it to be a drop-in replacement to run NumPy/SciPy code on GPU. CuPy supports Nvidia CUDA GPU platform, and AMD ROCm GPU platform starting in v9.0.
CuPy has been initially developed as a backend of Chainer deep learning framework, and later established as an independent project in 2017.
CuPy is a part of the NumPy ecosystem array libraries and is widely adopted to utilize GPU with Python, especially in high-performance computing environments such as Summit, Perlmutter, EULER, and ABCI.
CuPy is a NumFOCUS sponsored project.

Features
CuPy implements NumPy/SciPy-compatible APIs, as well as features to write user-defined GPU kernels or access low-level APIs.

NumPy-compatible APIs
The same set of APIs defined in the NumPy package (numpy.*) are available under cupy.* package.

Multi-dimensional array (cupy.ndarray) for boolean, integer, float, and complex data types
Module-level functions
Linear algebra functions
Fast Fourier transform
Random number generator

SciPy-compatible APIs
The same set of APIs defined in the SciPy package (scipy.*) are available under cupyx.scipy.* package.

Sparse matrices (cupyx.scipy.sparse.*_matrix) of CSR, COO, CSC, and DIA format
Discrete Fourier transform
Advanced linear algebra
Multidimensional image processing
Sparse linear algebra
Special functions
Signal processing
Statistical functions

User-defined GPU kernels
Kernel templates for element-wise and reduction operations
Raw kernel (CUDA C/C++)
Just-in-time transpiler (JIT)
Kernel fusion

Distributed computing
Distributed communication package (cupyx.distributed), providing collective and peer-to-peer primitives

Low-level CUDA features
Stream and event
Memory pool
Profiler
Host API binding
CUDA Python support

Interoperability
DLPack
CUDA Array Interface
NEP 13 (__array_ufunc__)
NEP 18 (__array_function__)
Array API Standard

Examples
Array creation
Basic operations
Raw CUDA C/C++ kernel
Applications
spaCy
XGBoost
turboSETI (Berkeley SETI)
NVIDIA RAPIDS
einops
scikit-learn
MONAI
Chainer

See also
Array programming
List of numerical-analysis software
Dask

References
External links
Official website
cupy on GitHub

## Archive Info
- **Archived on:** 2024-12-15 21:04:07 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2414 bytes
- **Word Count:** 328 words
