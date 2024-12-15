# SymPy

## Metadata
- **Last Updated:** 2024-12-03 07:10:31 UTC
- **Original Article:** [SymPy](https://en.wikipedia.org/wiki/SymPy)
- **Language:** en
- **Page ID:** 12168252

## Summary
SymPy is an open-source Python library for symbolic computation. It provides computer algebra capabilities either as a standalone application, as a library to other applications, or live on the web as SymPy Live or SymPy Gamma. SymPy is simple to install and to inspect because it is written entirely in Python with few dependencies. This ease of access combined with a simple and extensible code base in a well known language make SymPy a computer algebra system with a relatively low barrier to entry.
SymPy includes features ranging from basic symbolic arithmetic to calculus, algebra, discrete mathematics, and quantum physics. It is capable of formatting the result of the computations as LaTeX code.
SymPy is free software and is licensed under the 3-clause BSD. The lead developers are Ondřej Čertík and Aaron Meurer. It was started in 2005 by Ondřej Čertík.

## Categories
This article belongs to the following categories:

- Category:All articles with vague or ambiguous time
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Computer algebra system software for Linux
- Category:Computer algebra system software for Windows
- Category:Computer algebra system software for macOS
- Category:Free computer algebra systems
- Category:Free mathematics software
- Category:Free software programmed in Python
- Category:Python (programming language) scientific libraries
- Category:Short description is different from Wikidata
- Category:Vague or ambiguous time from August 2021

## Table of Contents

- Features
- Related projects
- Dependencies
- Usage examples
- See also
- References
- External links

## Content

SymPy is an open-source Python library for symbolic computation. It provides computer algebra capabilities either as a standalone application, as a library to other applications, or live on the web as SymPy Live or SymPy Gamma. SymPy is simple to install and to inspect because it is written entirely in Python with few dependencies. This ease of access combined with a simple and extensible code base in a well known language make SymPy a computer algebra system with a relatively low barrier to entry.
SymPy includes features ranging from basic symbolic arithmetic to calculus, algebra, discrete mathematics, and quantum physics. It is capable of formatting the result of the computations as LaTeX code.
SymPy is free software and is licensed under the 3-clause BSD. The lead developers are Ondřej Čertík and Aaron Meurer. It was started in 2005 by Ondřej Čertík.

Features
The SymPy library is split into a core with many optional modules.
Currently, the core of SymPy has around 260,000 lines of code (it also includes a comprehensive set of self-tests: over 100,000 lines in 350 files as of version 0.7.5), and its capabilities include:

Core capabilities
Basic arithmetic: *, /, +, -, **
Simplification
Expansion
Functions: trigonometric, hyperbolic, exponential, roots, logarithms, absolute value, spherical harmonics, factorials and gamma functions, zeta functions, polynomials, hypergeometric, special functions, etc.
Substitution
Arbitrary precision integers, rationals and floats
Noncommutative symbols
Pattern matching

Polynomials
Basic arithmetic: division, gcd, etc.
Factorization
Square-free factorization
Gröbner bases
Partial fraction decomposition
Resultants

Calculus
Limits
Differentiation
Integration: Implemented Risch–Norman heuristic
Taylor series (Laurent series)

Solving equations
Systems of linear equations
Systems of algebraic equations that are solvable by radicals
Differential equations
Difference equations

Discrete math
Binomial coefficients
Summations
Products
Number theory: generating Prime numbers, primality testing, integer factorization, etc.
Logic expressions

Matrices
Basic arithmetic
Eigenvalues and their eigenvectors when the characteristic polynomial is solvable by radicals
Determinants
Inversion
Solving

Geometry
Points, lines, rays, ellipses, circles, polygons, etc.
Intersections
Tangency
Similarity

Plotting
Note, plotting requires the external Matplotlib or Pyglet module.

Coordinate models
Plotting Geometric Entities
2D and 3D
Interactive interface
Colors
Animations

Physics
Units
Classical mechanics
Continuum mechanics
Quantum mechanics
Gaussian optics
Linear control

Statistics
Normal distributions
Uniform distributions
Probability

Combinatorics
Permutations
Combinations
Partitions
Subsets
Permutation group: Polyhedral, Rubik, Symmetric, etc.
Prufer sequence and Gray codes

Printing
Pretty-printing: ASCII/Unicode pretty-printing, LaTeX
Code generation: C, Fortran, Python

Related projects
SageMath: an open source alternative to Mathematica, Maple, MATLAB, and Magma (SymPy is included in Sage)
SymEngine: a rewriting of SymPy's core in C++, in order to increase its performance. Work is currently in progress to make SymEngine the underlying engine of Sage too.
mpmath: a Python library for arbitrary-precision floating-point arithmetic
SympyCore: another Python computer algebra system
SfePy: Software for solving systems of coupled partial differential equations (PDEs) by the finite element method in 1D, 2D and 3D.
GAlgebra: Geometric algebra module (previously sympy.galgebra).
Quameon: Quantum Monte Carlo in Python.
Lcapy: Experimental Python package for teaching linear circuit analysis.
LaTeX Expression project: Easy LaTeX typesetting of algebraic expressions in symbolic form with automatic substitution and result computation.
Symbolic statistical modeling: Adding statistical operations to complex physical models.
Diofant: a fork of SymPy, started by Sergey B Kirpichev

Dependencies
Since version 1.0, SymPy has the mpmath package as a dependency.
There are several optional dependencies that can enhance its capabilities:

gmpy: If gmpy is installed, SymPy's polynomial module will automatically use it for faster ground types. This can provide a several times boost in performance of certain operations.
matplotlib: If matplotlib is installed, SymPy can use it for plotting.
Pyglet: Alternative plotting package.

Usage examples
Pretty-printing
Sympy allows outputs to be formatted into a more appealing format through the pprint function. Alternatively, the init_printing() method will enable pretty-printing, so pprint need not be called. Pretty-printing will use unicode symbols when available in the current environment, otherwise it will fall back to ASCII characters.

Expansion
Arbitrary-precision example
Differentiation
Plotting
Limits
Differential equations
Integration
Series
Logical reasoning
Example 1
Example 2
See also
Comparison of computer algebra systems

References
External links
Official website 
Planet SymPy
SymPy Tutorials Collection
Code Repository on GitHub
Support and development forum
Gitter chat room

## Archive Info
- **Archived on:** 2024-12-15 20:38:50 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 5131 bytes
- **Word Count:** 687 words
