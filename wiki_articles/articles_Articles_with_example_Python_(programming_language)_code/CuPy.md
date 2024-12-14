# CuPy

## Article Metadata

- **Last Updated:** 2024-12-14T19:36:06.497589+00:00
- **Original Article:** [CuPy](https://en.wikipedia.org/wiki/CuPy)
- **Language:** en
- **Page ID:** 71062349

## Summary

CuPy is an open source library for GPU-accelerated computing with Python programming language, providing support for multi-dimensional arrays, sparse matrices, and a variety of numerical algorithms implemented on top of them.
CuPy shares the same API set as NumPy and SciPy, allowing it to be a drop-in replacement to run NumPy/SciPy code on GPU. CuPy supports Nvidia CUDA GPU platform, and AMD ROCm GPU platform starting in v9.0.
CuPy has been initially developed as a backend of Chainer deep learni

## Categories

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

## Related Articles

### Internal Links

- [AI Bridging Cloud Infrastructure](https://en.wikipedia.org/wiki/AI_Bridging_Cloud_Infrastructure)
- [AMD](https://en.wikipedia.org/wiki/AMD)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Array (data type)](https://en.wikipedia.org/wiki/Array_(data_type))
- [Array programming](https://en.wikipedia.org/wiki/Array_programming)
- [Berkeley SETI Research Center](https://en.wikipedia.org/wiki/Berkeley_SETI_Research_Center)
- [Brutus cluster](https://en.wikipedia.org/wiki/Brutus_cluster)
- [CUDA](https://en.wikipedia.org/wiki/CUDA)
- [Chainer](https://en.wikipedia.org/wiki/Chainer)
- [Computing platform](https://en.wikipedia.org/wiki/Computing_platform)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Cython](https://en.wikipedia.org/wiki/Cython)
- [Dask (software)](https://en.wikipedia.org/wiki/Dask_(software))
- [Digital image processing](https://en.wikipedia.org/wiki/Digital_image_processing)
- [Discrete Fourier transform](https://en.wikipedia.org/wiki/Discrete_Fourier_transform)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [ETH Zurich](https://en.wikipedia.org/wiki/ETH_Zurich)
- [Fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Linear algebra](https://en.wikipedia.org/wiki/Linear_algebra)
- [List of numerical-analysis software](https://en.wikipedia.org/wiki/List_of_numerical-analysis_software)
- [MIT License](https://en.wikipedia.org/wiki/MIT_License)
- [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
- [MayaVi](https://en.wikipedia.org/wiki/MayaVi)
- [Medical open network for AI](https://en.wikipedia.org/wiki/Medical_open_network_for_AI)
- [National Energy Research Scientific Computing Center](https://en.wikipedia.org/wiki/National_Energy_Research_Scientific_Computing_Center)
- [National Institute of Advanced Industrial Science and Technology](https://en.wikipedia.org/wiki/National_Institute_of_Advanced_Industrial_Science_and_Technology)
- [Nature (journal)](https://en.wikipedia.org/wiki/Nature_(journal))
- [NumPy](https://en.wikipedia.org/wiki/NumPy)
- [Numerical analysis](https://en.wikipedia.org/wiki/Numerical_analysis)
- [Nvidia](https://en.wikipedia.org/wiki/Nvidia)
- [Oak Ridge Leadership Computing Facility](https://en.wikipedia.org/wiki/Oak_Ridge_Leadership_Computing_Facility)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [PubMed Central](https://en.wikipedia.org/wiki/PubMed_Central)
- [PubMed](https://en.wikipedia.org/wiki/PubMed)
- [Pandas (software)](https://en.wikipedia.org/wiki/Pandas_(software))
- [Perlmutter (supercomputer)](https://en.wikipedia.org/wiki/Perlmutter_(supercomputer))
- [Phoronix Test Suite](https://en.wikipedia.org/wiki/Phoronix_Test_Suite)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [ROCm](https://en.wikipedia.org/wiki/ROCm)
- [Random number generation](https://en.wikipedia.org/wiki/Random_number_generation)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [SciPy](https://en.wikipedia.org/wiki/SciPy)
- [Scikit-image](https://en.wikipedia.org/wiki/Scikit-image)
- [Scikit-learn](https://en.wikipedia.org/wiki/Scikit-learn)
- [Signal processing](https://en.wikipedia.org/wiki/Signal_processing)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [SpaCy](https://en.wikipedia.org/wiki/SpaCy)
- [Sparse matrix](https://en.wikipedia.org/wiki/Sparse_matrix)
- [Statistics](https://en.wikipedia.org/wiki/Statistics)
- [Summit (supercomputer)](https://en.wikipedia.org/wiki/Summit_(supercomputer))
- [Wikidata](https://en.wikipedia.org/wiki/Wikidata)
- [XGBoost](https://en.wikipedia.org/wiki/XGBoost)
- [Template:SciPy ecosystem](https://en.wikipedia.org/wiki/Template:SciPy_ecosystem)
- [Template talk:SciPy ecosystem](https://en.wikipedia.org/wiki/Template_talk:SciPy_ecosystem)
- [Category:Python (programming language) scientific libraries](https://en.wikipedia.org/wiki/Category:Python_(programming_language)_scientific_libraries)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:36:06.497589+00:00_