# Output-sensitive algorithm

## Article Metadata

- **Last Updated:** 2024-12-14T19:42:35.266236+00:00
- **Original Article:** [Output-sensitive algorithm](https://en.wikipedia.org/wiki/Output-sensitive_algorithm)
- **Language:** en
- **Page ID:** 12127990

## Summary

In computer science, an output-sensitive algorithm is an algorithm whose running time depends on the size of the output, instead of, or in addition to, the size of the input. For certain problems where the output size varies widely, for example from linear in the size of the input to quadratic in the size of the input, analyses that take the output size explicitly into account can produce better runtime bounds that differentiate algorithms that would otherwise have identical asymptotic complexit

## Categories

- Category:Analysis of algorithms
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Short description matches Wikidata

## Table of Contents

- Examples
- Generalizations
- See also

## Content

In computer science, an output-sensitive algorithm is an algorithm whose running time depends on the size of the output, instead of, or in addition to, the size of the input. For certain problems where the output size varies widely, for example from linear in the size of the input to quadratic in the size of the input, analyses that take the output size explicitly into account can produce better runtime bounds that differentiate algorithms that would otherwise have identical asymptotic complexity.

Examples
Division by subtraction
A simple example of an output-sensitive algorithm is given by the division algorithm division by subtraction which computes the quotient and remainder of dividing two positive integers using only addition, subtraction, and comparisons:

Example output:

This algorithm takes Θ(Q) time, and so can be fast in scenarios where the quotient Q is known to be small. In cases where Q is large however, it is outperformed by more complex algorithms such as long division.

Computational geometry
Convex hull algorithms for finding the convex hull of a finite set of points in the plane require Ω(n log n) time for n points; even relatively simple algorithms like the Graham scan achieve this lower bound. If the convex hull uses all n points, this is the best we can do; however, for many practical sets of points, and in particular for random sets of points, the number of points h in the convex hull is typically much smaller than n. Consequently, output-sensitive algorithms such as the ultimate convex hull algorithm and Chan's algorithm which require only O(n log h) time are considerably faster for such point sets.
Output-sensitive algorithms arise frequently in computational geometry applications and have been described for problems such as hidden surface removal and resolving range filter conflicts in router tables.
Frank Nielsen describes a general paradigm of output-sensitive algorithms known as grouping and querying and gives such an algorithm for computing cells of a Voronoi diagram. Nielsen breaks these algorithms into two stages: estimating the output size, and then building data structures based on that estimate which are queried to construct the final solution.

Generalizations
A more general kind of output-sensitive algorithms are enumeration algorithms, which enumerate the set of solutions to a problem. In this context, the performance of algorithms is also measured in an output-sensitive way, in addition to more sensitive measures, e.g., bounded the delay between any two successive solutions.

See also
Lazy evaluation


== References ==

## Related Articles

### Internal Links

- [ACM Transactions on Graphics](https://en.wikipedia.org/wiki/ACM_Transactions_on_Graphics)
- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Chan's algorithm](https://en.wikipedia.org/wiki/Chan%27s_algorithm)
- [Computational geometry](https://en.wikipedia.org/wiki/Computational_geometry)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Convex hull](https://en.wikipedia.org/wiki/Convex_hull)
- [Convex hull algorithms](https://en.wikipedia.org/wiki/Convex_hull_algorithms)
- [Division algorithm](https://en.wikipedia.org/wiki/Division_algorithm)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Enumeration algorithm](https://en.wikipedia.org/wiki/Enumeration_algorithm)
- [Graham scan](https://en.wikipedia.org/wiki/Graham_scan)
- [Handle System](https://en.wikipedia.org/wiki/Handle_System)
- [Hidden-surface determination](https://en.wikipedia.org/wiki/Hidden-surface_determination)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation)
- [Long division](https://en.wikipedia.org/wiki/Long_division)
- [Mark Overmars](https://en.wikipedia.org/wiki/Mark_Overmars)
- [Micha Sharir](https://en.wikipedia.org/wiki/Micha_Sharir)
- [Kirkpatrick–Seidel algorithm](https://en.wikipedia.org/wiki/Kirkpatrick%E2%80%93Seidel_algorithm)
- [Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:42:35.266236+00:00_