# Range (computer programming)

## Metadata
- **Last Updated:** 2024-11-26 13:36:02 UTC
- **Original Article:** [Range (computer programming)](https://en.wikipedia.org/wiki/Range_(computer_programming))
- **Language:** en
- **Page ID:** 8508082

## Summary
In computer science, the term range may refer to one of three things:

The possible values that may be stored in a variable.
The upper and lower bounds of an array.
An alternative to iterator.

## Categories
This article belongs to the following categories:

- Category:All articles needing additional references
- Category:All stub articles
- Category:Arrays
- Category:Articles needing additional references from December 2006
- Category:Articles with example C Sharp code
- Category:Articles with example PHP code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Rust code
- Category:Computer programming stubs
- Category:Programming constructs

## Table of Contents

- Range of a variable
- Range of an array
- Range as an alternative to iterator
- Range as a data type
- Range as a operator
- See also

## Content

In computer science, the term range may refer to one of three things:

The possible values that may be stored in a variable.
The upper and lower bounds of an array.
An alternative to iterator.

Range of a variable
The range of a variable is given as the set of possible values that that variable can hold. In the case of an integer, the variable definition is restricted to whole numbers only, and the range will cover every number within its range (including the maximum and minimum). For example, the range of a signed 16-bit integer variable is all the integers from −32,768 to +32,767.

Range of an array
When an array is numerically indexed, its range is the upper and lower bound of the array. Depending on the environment, a warning, a fatal exception, or unpredictable behavior will occur if the program attempts to access an array element that is outside the range. In some programming languages, such as C, arrays have a fixed lower bound (zero) and will contain data at each position up to the upper bound (so an array with 5 elements will have a range of 0 to 4). In others, such as PHP, an array may have holes where no element is defined, and therefore an array with a range of 0 to 4 will have up to 5 elements (and a minimum of 2).

Range as an alternative to iterator
Another meaning of range in computer science is an alternative to iterator. When used in this sense, range is defined as "a pair of begin/end iterators packed together". It is argued  that "Ranges are a superior abstraction" (compared to iterators) for several reasons, including better safety.
In particular, such ranges are supported in C++20, Boost C++ Libraries and the D standard library.

Range as a data type
A data type for ranges can be implemented using generics.
Example in C#.

Example in Kotlin.

Example in PHP.

Example in Python.

Rust has a built-in range struct in the standard library in std::ops::Range.

Range as a operator
Rust has the .. and ..= operators.

Zig also has the .. operator.

See also
Interval


== References ==

## Archive Info
- **Archived on:** 2024-12-15 20:38:42 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2035 bytes
- **Word Count:** 361 words
