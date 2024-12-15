# Irish logarithm

## Metadata
- **Last Updated:** 2024-12-07 14:46:39 UTC
- **Original Article:** [Irish logarithm](https://en.wikipedia.org/wiki/Irish_logarithm)
- **Language:** en
- **Page ID:** 31818344

## Summary
The Irish logarithm was a system of number manipulation invented by Percy Ludgate for machine multiplication. The system used a combination of mechanical cams as lookup tables and mechanical addition to sum pseudo-logarithmic indices to produce partial products, which were then added to produce results.
The technique is similar to Zech logarithms (also known as Jacobi logarithms), but uses a system of indices original to Ludgate.

## Categories
This article belongs to the following categories:

- Category:Algorithms
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:CS1 maint: others
- Category:Irish inventions
- Category:Mechanical calculators
- Category:Multiplication
- Category:Pages displaying short descriptions of redirect targets via Module:Annotated link
- Category:Short description is different from Wikidata

## Table of Contents

- Concept
- Pseudocode
- See also
- References
- Further reading
- External links

## Content

The Irish logarithm was a system of number manipulation invented by Percy Ludgate for machine multiplication. The system used a combination of mechanical cams as lookup tables and mechanical addition to sum pseudo-logarithmic indices to produce partial products, which were then added to produce results.
The technique is similar to Zech logarithms (also known as Jacobi logarithms), but uses a system of indices original to Ludgate.

Concept
Ludgate's algorithm compresses the multiplication of two single decimal numbers into two table lookups (to convert the digits into indices), the addition of the two indices to create a new index which is input to a second lookup table that generates the output product. Because both lookup tables are one-dimensional, and the addition of linear movements is simple to implement mechanically, this allows a less complex mechanism than would be needed to implement a two-dimensional 10×10 multiplication lookup table.
Ludgate stated that he deliberately chose the values in his tables to be as small as he could make them; given this, Ludgate's tables can be simply constructed from first principles, either via pen-and-paper methods, or a systematic search using only a few tens of lines of program code. They do not correspond to either Zech logarithms, Remak indexes or Korn indexes.

Pseudocode
The following is an implementation of Ludgate's Irish logarithm algorithm in the Python programming language:

Table 1 is taken from Ludgate's original paper; given the first table, the contents of Table 2 can be trivially derived from Table 1 and the definition of the algorithm. Note since that the last third of the second table is entirely zeros, this could be exploited to further simplify a mechanical implementation of the algorithm.

See also
Faber-Castell Model 366 – Unusual slide rule using a system similar to discrete logarithmsPages displaying short descriptions of redirect targets
Canon arithmeticus – Book by Carl Jacobi

References
Further reading
Boys, C.V., "A New Analytical Engine," Nature, Vol. 81, No. 2070, July 1, 1904, pp. 14–15.
Randell, B., "Ludgate's analytical machine of 1909", The Computer Journal, Volume 14, Issue 3, 1971, Pages 317–326, https://doi.org/10.1093/comjnl/14.3.317 Includes the text of Ludgate's original paper.

External links
A detailed treatment of Ludgate's Irish Logarithms, Brian Coghlan, 2019 (Archived from original link)
Transcript of "On a Proposed Analytical Machine" by Percy Ludgate (first published in Scientific Proceedings of the Royal Dublin Society 1909 vol 12 pages 77–91), containing Ludgate's own description of the Irish logarithm tables
A reproduction of Ludgate's original 1909 paper, from The origins of digital computers : selected papers. Randell, Brian, 1936-. Berlin: Springer-Verlag. 1973. p. 71. ISBN 978-3-642-96145-8. OCLC 858931618.{{cite book}}:  CS1 maint: others (link)
Method for deriving Ludgate's Irish Logarithms from first principles, Brian Coghlan, 2022)

## Archive Info
- **Archived on:** 2024-12-15 21:04:51 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2996 bytes
- **Word Count:** 448 words
