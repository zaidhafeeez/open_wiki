# SymPy

## Article Metadata

- **Last Updated:** 2024-12-14T19:45:49.322427+00:00
- **Original Article:** [SymPy](https://en.wikipedia.org/wiki/SymPy)
- **Language:** en
- **Page ID:** 12168252

## Summary

SymPy is an open-source Python library for symbolic computation. It provides computer algebra capabilities either as a standalone application, as a library to other applications, or live on the web as SymPy Live or SymPy Gamma. SymPy is simple to install and to inspect because it is written entirely in Python with few dependencies. This ease of access combined with a simple and extensible code base in a well known language make SymPy a computer algebra system with a relatively low barrier to ent

## Categories

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

## Related Articles

### Internal Links

- [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses)
- [ALTRAN](https://en.wikipedia.org/wiki/ALTRAN)
- [ASCII](https://en.wikipedia.org/wiki/ASCII)
- [Absolute value](https://en.wikipedia.org/wiki/Absolute_value)
- [Algebra](https://en.wikipedia.org/wiki/Algebra)
- [Algebraic equation](https://en.wikipedia.org/wiki/Algebraic_equation)
- [Animation](https://en.wikipedia.org/wiki/Animation)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Arbitrary-precision arithmetic](https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic)
- [Arithmetic](https://en.wikipedia.org/wiki/Arithmetic)
- [Axiom (computer algebra system)](https://en.wikipedia.org/wiki/Axiom_(computer_algebra_system))
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Binomial coefficient](https://en.wikipedia.org/wiki/Binomial_coefficient)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [Cadabra (computer program)](https://en.wikipedia.org/wiki/Cadabra_(computer_program))
- [Calculus](https://en.wikipedia.org/wiki/Calculus)
- [Cambridge Algebra System](https://en.wikipedia.org/wiki/Cambridge_Algebra_System)
- [Casio ClassPad 300](https://en.wikipedia.org/wiki/Casio_ClassPad_300)
- [Characteristic polynomial](https://en.wikipedia.org/wiki/Characteristic_polynomial)
- [Circle](https://en.wikipedia.org/wiki/Circle)
- [Classical mechanics](https://en.wikipedia.org/wiki/Classical_mechanics)
- [CoCoA](https://en.wikipedia.org/wiki/CoCoA)
- [Code generation (compiler)](https://en.wikipedia.org/wiki/Code_generation_(compiler))
- [Combination](https://en.wikipedia.org/wiki/Combination)
- [List of computer algebra systems](https://en.wikipedia.org/wiki/List_of_computer_algebra_systems)
- [Computer algebra system](https://en.wikipedia.org/wiki/Computer_algebra_system)
- [Continuum mechanics](https://en.wikipedia.org/wiki/Continuum_mechanics)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Derive (computer algebra system)](https://en.wikipedia.org/wiki/Derive_(computer_algebra_system))
- [Determinant](https://en.wikipedia.org/wiki/Determinant)
- [Recurrence relation](https://en.wikipedia.org/wiki/Recurrence_relation)
- [Differential equation](https://en.wikipedia.org/wiki/Differential_equation)
- [Derivative](https://en.wikipedia.org/wiki/Derivative)
- [Discrete mathematics](https://en.wikipedia.org/wiki/Discrete_mathematics)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Eigenvalues and eigenvectors](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)
- [Eigenvalues and eigenvectors](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)
- [Ellipse](https://en.wikipedia.org/wiki/Ellipse)
- [Engineering Equation Solver](https://en.wikipedia.org/wiki/Engineering_Equation_Solver)
- [Erable](https://en.wikipedia.org/wiki/Erable)
- [Exponential function](https://en.wikipedia.org/wiki/Exponential_function)
- [FORM (symbolic manipulation system)](https://en.wikipedia.org/wiki/FORM_(symbolic_manipulation_system))
- [Factorial](https://en.wikipedia.org/wiki/Factorial)
- [Factorization](https://en.wikipedia.org/wiki/Factorization)
- [Fermat (computer algebra system)](https://en.wikipedia.org/wiki/Fermat_(computer_algebra_system))
- [Floating-point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Free software](https://en.wikipedia.org/wiki/Free_software)
- [FriCAS](https://en.wikipedia.org/wiki/FriCAS)
- [Function (mathematics)](https://en.wikipedia.org/wiki/Function_(mathematics))
- [GAP (computer algebra system)](https://en.wikipedia.org/wiki/GAP_(computer_algebra_system))
- [Gamma function](https://en.wikipedia.org/wiki/Gamma_function)
- [Gaussian optics](https://en.wikipedia.org/wiki/Gaussian_optics)
- [Geometric algebra](https://en.wikipedia.org/wiki/Geometric_algebra)
- [GiNaC](https://en.wikipedia.org/wiki/GiNaC)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Gray code](https://en.wikipedia.org/wiki/Gray_code)
- [Greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor)
- [Gröbner basis](https://en.wikipedia.org/wiki/Gr%C3%B6bner_basis)
- [Hyperbolic functions](https://en.wikipedia.org/wiki/Hyperbolic_functions)
- [Hypergeometric function](https://en.wikipedia.org/wiki/Hypergeometric_function)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Infinitary combinatorics](https://en.wikipedia.org/wiki/Infinitary_combinatorics)
- [Integer](https://en.wikipedia.org/wiki/Integer)
- [Integer factorization](https://en.wikipedia.org/wiki/Integer_factorization)
- [Integral](https://en.wikipedia.org/wiki/Integral)
- [Intersection](https://en.wikipedia.org/wiki/Intersection)
- [Inversion (discrete mathematics)](https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics))
- [KANT (software)](https://en.wikipedia.org/wiki/KANT_(software))
- [LaTeX](https://en.wikipedia.org/wiki/LaTeX)
- [Laurent series](https://en.wikipedia.org/wiki/Laurent_series)
- [Library (computing)](https://en.wikipedia.org/wiki/Library_(computing))
- [Line (geometry)](https://en.wikipedia.org/wiki/Line_(geometry))
- [Line coordinates](https://en.wikipedia.org/wiki/Line_coordinates)
- [Linear control](https://en.wikipedia.org/wiki/Linear_control)
- [List of computer algebra systems](https://en.wikipedia.org/wiki/List_of_computer_algebra_systems)
- [LiveMath](https://en.wikipedia.org/wiki/LiveMath)
- [Logarithm](https://en.wikipedia.org/wiki/Logarithm)
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [Macaulay2](https://en.wikipedia.org/wiki/Macaulay2)
- [Macsyma](https://en.wikipedia.org/wiki/Macsyma)
- [Magma (computer algebra system)](https://en.wikipedia.org/wiki/Magma_(computer_algebra_system))
- [Maple (software)](https://en.wikipedia.org/wiki/Maple_(software))
- [Mathcad](https://en.wikipedia.org/wiki/Mathcad)
- [Limit (mathematics)](https://en.wikipedia.org/wiki/Limit_(mathematics))
- [Mathomatic](https://en.wikipedia.org/wiki/Mathomatic)
- [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
- [Maxima (software)](https://en.wikipedia.org/wiki/Maxima_(software))
- [MuMATH](https://en.wikipedia.org/wiki/MuMATH)
- [MuPAD](https://en.wikipedia.org/wiki/MuPAD)
- [Network analysis (electrical circuits)](https://en.wikipedia.org/wiki/Network_analysis_(electrical_circuits))
- [Noncommutative logic](https://en.wikipedia.org/wiki/Noncommutative_logic)
- [Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)
- [Normaliz](https://en.wikipedia.org/wiki/Normaliz)
- [Number theory](https://en.wikipedia.org/wiki/Number_theory)
- [Open source](https://en.wikipedia.org/wiki/Open_source)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [PARI/GP](https://en.wikipedia.org/wiki/PARI/GP)
- [Partial fraction decomposition](https://en.wikipedia.org/wiki/Partial_fraction_decomposition)
- [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching)
- [Permutation group](https://en.wikipedia.org/wiki/Permutation_group)
- [Permutation](https://en.wikipedia.org/wiki/Permutation)
- [Point (geometry)](https://en.wikipedia.org/wiki/Point_(geometry))
- [Polygon](https://en.wikipedia.org/wiki/Polygon)
- [Polyhedral combinatorics](https://en.wikipedia.org/wiki/Polyhedral_combinatorics)
- [Polynomial](https://en.wikipedia.org/wiki/Polynomial)
- [Polynomial long division](https://en.wikipedia.org/wiki/Polynomial_long_division)
- [Prettyprint](https://en.wikipedia.org/wiki/Prettyprint)
- [Prime number](https://en.wikipedia.org/wiki/Prime_number)
- [Probability](https://en.wikipedia.org/wiki/Probability)
- [Product (mathematics)](https://en.wikipedia.org/wiki/Product_(mathematics))
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Proprietary software](https://en.wikipedia.org/wiki/Proprietary_software)
- [Prüfer sequence](https://en.wikipedia.org/wiki/Pr%C3%BCfer_sequence)
- [Pyglet](https://en.wikipedia.org/wiki/Pyglet)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quantum Monte Carlo](https://en.wikipedia.org/wiki/Quantum_Monte_Carlo)
- [Quantum mechanics](https://en.wikipedia.org/wiki/Quantum_mechanics)
- [Quantum mechanics](https://en.wikipedia.org/wiki/Quantum_mechanics)
- [Rational number](https://en.wikipedia.org/wiki/Rational_number)
- [Reduce (computer algebra system)](https://en.wikipedia.org/wiki/Reduce_(computer_algebra_system))
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Resultant](https://en.wikipedia.org/wiki/Resultant)
- [Risch algorithm](https://en.wikipedia.org/wiki/Risch_algorithm)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [SMath Studio](https://en.wikipedia.org/wiki/SMath_Studio)
- [SageMath](https://en.wikipedia.org/wiki/SageMath)
- [SimPy](https://en.wikipedia.org/wiki/SimPy)
- [Similarity (geometry)](https://en.wikipedia.org/wiki/Similarity_(geometry))
- [Singular (software)](https://en.wikipedia.org/wiki/Singular_(software))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Galois theory](https://en.wikipedia.org/wiki/Galois_theory)
- [Spherical harmonics](https://en.wikipedia.org/wiki/Spherical_harmonics)
- [Square-free polynomial](https://en.wikipedia.org/wiki/Square-free_polynomial)
- [Subset](https://en.wikipedia.org/wiki/Subset)
- [Substitution (logic)](https://en.wikipedia.org/wiki/Substitution_(logic))
- [Summation](https://en.wikipedia.org/wiki/Summation)
- [Computer algebra](https://en.wikipedia.org/wiki/Computer_algebra)
- [Symmetric group](https://en.wikipedia.org/wiki/Symmetric_group)
- [System of equations](https://en.wikipedia.org/wiki/System_of_equations)
- [TI InterActive!](https://en.wikipedia.org/wiki/TI_InterActive!)
- [Tangent](https://en.wikipedia.org/wiki/Tangent)
- [Taylor series](https://en.wikipedia.org/wiki/Taylor_series)
- [Trigonometric functions](https://en.wikipedia.org/wiki/Trigonometric_functions)
- [Unicode](https://en.wikipedia.org/wiki/Unicode)
- [Continuous uniform distribution](https://en.wikipedia.org/wiki/Continuous_uniform_distribution)
- [Wolfram Mathematica](https://en.wikipedia.org/wiki/Wolfram_Mathematica)
- [Xcas](https://en.wikipedia.org/wiki/Xcas)
- [Yacas](https://en.wikipedia.org/wiki/Yacas)
- [Zero of a function](https://en.wikipedia.org/wiki/Zero_of_a_function)
- [Zeta function (operator)](https://en.wikipedia.org/wiki/Zeta_function_(operator))
- [Wikipedia:Manual of Style/Dates and numbers](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Dates_and_numbers)
- [Template:Computer algebra systems](https://en.wikipedia.org/wiki/Template:Computer_algebra_systems)
- [Template talk:Computer algebra systems](https://en.wikipedia.org/wiki/Template_talk:Computer_algebra_systems)
- [Category:Computer algebra systems](https://en.wikipedia.org/wiki/Category:Computer_algebra_systems)
- [Category:Vague or ambiguous time from August 2021](https://en.wikipedia.org/wiki/Category:Vague_or_ambiguous_time_from_August_2021)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)
- [Portal:Mathematics](https://en.wikipedia.org/wiki/Portal:Mathematics)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:45:49.322427+00:00_