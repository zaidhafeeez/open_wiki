# Array slicing

## Metadata
- **Last Updated:** 2024-12-03 06:54:05 UTC
- **Original Article:** [Array slicing](https://en.wikipedia.org/wiki/Array_slicing)
- **Language:** en
- **Page ID:** 683334

## Summary
In computer programming, array slicing is an operation that extracts a subset of elements from an array and packages them as another array, possibly in a different dimension from the original. 
Common examples of array slicing are extracting a substring from a string of characters, the "ell" in "hello", extracting a row or column from a two-dimensional array, or extracting a vector from a matrix.
Depending on the programming language, an array slice can be made out of non-consecutive elements.  Also depending on the language, the elements of the new array may be aliased to (i.e., share memory with) those of the original array.

## Categories
This article belongs to the following categories:

- Category:Arrays
- Category:Articles with example ALGOL 68 code
- Category:Articles with example Ada code
- Category:Articles with example BASIC code
- Category:Articles with example D code
- Category:Articles with example Fortran code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Programming constructs
- Category:Short description is different from Wikidata

## Table of Contents

- Details
- History
- Timeline of slicing in various programming languages
- See also

## Content

In computer programming, array slicing is an operation that extracts a subset of elements from an array and packages them as another array, possibly in a different dimension from the original. 
Common examples of array slicing are extracting a substring from a string of characters, the "ell" in "hello", extracting a row or column from a two-dimensional array, or extracting a vector from a matrix.
Depending on the programming language, an array slice can be made out of non-consecutive elements.  Also depending on the language, the elements of the new array may be aliased to (i.e., share memory with) those of the original array.

Details
For "one-dimensional" (single-indexed) arrays –  vectors, sequence, strings etc. –  the most common slicing operation is extraction of zero or more consecutive elements. Thus, if we have a vector containing elements (2, 5, 7, 3, 8, 6, 4, 1), and we want to create an array slice from the 3rd to the 6th items, we get (7, 3, 8, 6). In programming languages that use a 0-based indexing scheme, the slice would be from index 2 to 5.
Reducing the range of any index to a single value effectively eliminates that index. This feature can be used, for example, to extract one-dimensional slices (vectors: in 3D, rows, columns, and tubes) or two-dimensional slices (rectangular matrices) from a  three-dimensional array. However, since the range can be specified at run-time, type-checked languages may require an explicit (compile-time) notation to actually eliminate the trivial indices.
General array slicing can be implemented (whether or not built into the language) by referencing every array through a dope vector or descriptor –  a record that contains the address of the first array element, and then the range of each index and the corresponding coefficient in the indexing formula. This technique also allows immediate array transposition, index reversal, subsampling, etc. For languages like C, where the indices always start at zero, the dope vector of an array with d indices has at least 1 + 2d parameters. For languages that allow arbitrary lower bounds for indices, like Pascal, the dope vector needs 1 + 3d entries.
If the array abstraction does not support true negative indices (as for example the arrays of Ada and Pascal do), then negative indices for the bounds of the slice for a given dimension are sometimes used to specify an offset from the end of the array in that dimension. In 1-based schemes, -1 generally would indicate the second-to-last item, while in a 0-based system, it would mean the very last item.

History
The concept of slicing was surely known even before the invention of compilers. Slicing as a language feature probably started with FORTRAN (1957), more as a consequence of non-existent type and range checking than by design. The concept was also alluded to in the preliminary report for the IAL (ALGOL 58) in that the syntax allowed one or more indices of an array element (or, for that matter, of a procedure call) to be omitted when used as an actual parameter.
Kenneth Iverson's APL (1957) had very flexible multi-dimensional array slicing, which contributed much to the language's expressive power and popularity.
ALGOL 68 (1968) introduced comprehensive multi-dimension array slicing and trimming features.
Array slicing facilities have been incorporated in several modern languages, such as Ada 2005, Cobra, D, Fortran 90, Go, Rust, Julia, MATLAB, Perl, Python, S-Lang, Windows PowerShell and the mathematical/statistical languages GNU Octave, S and R.

Timeline of slicing in various programming languages
1964: PL/I
PL/I provides two facilities for array slicing.

Using iSub DEFINING, an array slice can be declared using iSUB variables to map specific elements in a "base array" onto elements of the "defined array". iSUBs can define rows, columns, diagonals, or many-to-one mappings.: pp.212–213  The following example defines Y as a one-dimensional slice consisting of the diagonal elements of the two-dimensional array X.
DECLARE X(5,5);
DECLARE Y(5) DEFINED(X(1SUB,1SUB));
A reference to Y(2) is a reference to X(2,2), and so on.

A slice, called a cross-section, of an array can be referred to by using asterisk as the subscript for one or more dimensions. The following code sets all the elements in the first column of X to zero. One or more subscripts can be specified by asterisks in an expression.: p.43 
DECLARE X(5,5);
X(*,1)=0;

1966: Fortran 66
The Fortran 66 programmers were only able to take advantage of slicing matrices by row, and then only when passing that row to a subroutine:

Result:

   2.000000       4.000000       8.000000

Note that there is no dope vector in FORTRAN 66 hence the length of the slice must also be passed as an argument - or some other means - to the SUBROUTINE. 1970s Pascal and C had similar restrictions.

1968: Algol 68
Algol68 final report contains an early example of slicing, slices are specified in the form:

[lower bound:upper bound] ¢ for computers with extended character sets ¢

or:

(LOWER BOUND..UPPER BOUND) # FOR COMPUTERS WITH ONLY 6 BIT CHARACTERS. #

Both bounds are inclusive and can be omitted, in which case they default to the declared array bounds. Neither the stride facility, nor diagonal slice aliases are part of the revised report.
Examples:

[3, 3]real a := ((1, 1, 1), (2, 4, 8), (3, 9, 27)); # declaration of a variable matrix #
[,]  real c = ((1, 1, 1), (2, 4, 8), (3, 9, 27));   # constant matrix, the size is implied #

ref[]real row := a[2,];                    # alias/ref to a row slice #
ref[]real col2 = a[, 2];                   # permanent alias/ref to second column #

print ((a[:, 2], newline));                # second column slice #
print ((a[1⌈a, :], newline));              # last row slice #
print ((a[:, 2⌈a], newline));              # last column slice #
print ((a[:2, :2], newline));              # leading 2-by-2 submatrix "slice" #

+1.000010+0 +4.000010+0 +9.000010+0
+3.000010+0 +9.000010+0 +2.700010+1
+1.000010+0 +8.000010+0 +2.700010+1
+1.000010+0 +1.000010+0 +2.000010+0 +4.000010+0

1968: BASIC
HP's HP 2000 systems, introduced in November 1968, used HP Time-Shared BASIC as their primary interface and programming language. This version of BASIC used slicing for most string manipulation operations. One oddity of the language was that it allowed round or square braces interchangeably, and which was used in practice was typically a function of the computer terminal being used.
Example:

Will produce:

HELLO
WORLD

The HP systems were widely used in the early 1970s, especially in technical high schools and many small industrial and scientific settings. As the first microcomputers emerged in the mid-1970s, HP was often used as the pattern for their BASIC dialects as well. Notable examples include 1977's Apple BASIC, 1978's Atari BASIC, and 1979's Sinclair BASIC. This style of manipulation generally offers advantages in terms of memory use, and was often chosen on systems that shipped with small amounts of memory. Only Sinclair's dialect differed in any meaningful way, using the TO keyword instead of a comma-separated list:

Slicing was also selected as the basis for the ANSI Full BASIC standard, using the colon as the separator and thus differentiating between slicing and array access:

While this style of access offered a number of advantages, especially for the small machines of the era, sometime after 1970 Digital Equipment Corporation introduced their own variation of BASIC that used the LEFT$, RIGHT$ and MID$ string functions. Microsoft BASIC was written on the PDP-10 and its BASIC was used as the pattern. Through the late 1970s the two styles were both widely used, but by the early 1980s the DEC-style functions were the de facto standard.

1970s: MATLAB
The : operator implements the stride syntax (lower_bound:upper_bound[:stride]) by generating a vector. 1:5 evaluates as [1, 2, 3, 4, 5]. 1:9:2 evaluates as [1, 3, 5, 7, 9]. A bare : evaluates the same as 1:end, with end determined by context.

1976: S/R
Arrays in S and GNU R are always one-based, thus the indices of a new slice will begin with one for each dimension, regardless of the previous indices. Dimensions with length of one will be dropped (unless drop = FALSE). Dimension names (where present) will be preserved.

1977: Fortran 77
The Fortran 77 standard introduced the ability to slice and concatenate strings:

Produces:

BCD

Such strings could be passed by reference to another subroutine, the length would also be passed transparently to the subroutine as a kind of short dope vector.

Again produces:

BCD

1983: Ada 83 and above
Ada 83 supports slices for all array types. Like Fortran 77 such arrays could be passed by reference to another subroutine, the length would also be passed transparently to the subroutine as a kind of short dope vector.

Produces:

BCD

Note: Since in Ada indices are n-based the term Text (2 .. 4) will result in an Array with the base index of 2.
The definition for Text_IO.Put_Line is:

The definition for String is:

As Ada supports true negative indices as in type History_Data_Array is array (-6000 .. 2010) of History_Data; it places no special meaning on negative indices. In the example above the term  Some_History_Data (-30 .. 30) would slice the History_Data from 31 BC to 30 AD (since there was no year zero, the year number 0 actually refers to 1 BC).

1987: Perl
If we have

as above, then the first 3 elements, middle 3 elements and last 3 elements would be:

Perl supports negative list indices. The -1 index is the last element, -2 the penultimate element, etc.
In addition, Perl supports slicing based on expressions, for example:

1991: Python
If you have the following list:

Then it is possible to slice by using a notation similar to element retrieval:

Note that Python allows negative list indices. The index -1 represents the last element, -2 the penultimate element, etc.
Python also allows a step property by appending an extra colon and a value. For example:

The stride syntax (nums[1:5:2]) was introduced in the second half of the 1990s, as a result of requests put forward by scientific users in the Python "matrix-SIG" (special interest group).
Slice semantics potentially differ per object; new semantics can be introduced when operator overloading the indexing operator. With Python standard lists (which are dynamic arrays), every slice is a copy. Slices of NumPy arrays, by contrast, are views onto the same underlying buffer.

1992: Fortran 90 and above
In Fortran 90, slices are specified in the form

Both bounds are inclusive and can be omitted, in which case they default to the declared
array bounds. Stride defaults to 1. Example:

1994: Analytica
Each dimension of an array value in Analytica is identified by an Index variable. When slicing or subscripting, the syntax identifies the dimension(s) over which you are slicing or subscripting by naming the dimension. Such as:

Index I := 1..5   { Definition of a numerical Index }
Index J := ['A', 'B', 'C'] { Definition of a text-valued Index }
Variable X := Array(I, J, [[10, 20, 30], [1, 2, 3], ....]) { Definition of a 2D value }
X[I = 1, J = 'B']  -> 20  { Subscript to obtain a single value }
X[I = 1] ->  Array(J, [10, 20, 30])  { Slice out a 1D array. }
X[J = 2] -> Array(I, [20, 2, ....]) { Slice out a 1D array over the other dimension. }
X[I = 1..3]  {Slice out first four elements over I with all elements over J}

Naming indexes in slicing and subscripting is similar to naming parameters in function calls instead of relying on a fixed sequence of parameters. One advantage of naming indexes in slicing is that the programmer does not have to remember the sequence of Indexes, in a multidimensional array. A deeper advantage is that expressions generalize automatically and safely without requiring a rewrite when the number of dimensions of X changes.

1998: S-Lang
Array slicing was introduced in version 1.0. Earlier versions did not
support this feature.
Suppose that A is a 1-d array such as

    A = [1:50];           % A = [1, 2, 3, ...49, 50]

Then an array B of first 5 elements of A may be created using

    B = A[[:4]];

Similarly, B may be assigned to an array of the last 5 elements of A via:

    B = A[[-5:]];

Other examples of 1-d slicing include:

    A[-1]                 % The last element of A
    A[*]                  % All elements of A
    A[[::2]]              % All even elements of A
    A[[1::2]]             % All odd elements of A
    A[[-1::-2]]           % All even elements in the reversed order
    A[[[0:3], [10:14]]]   % Elements 0-3 and 10-14

Slicing of higher-dimensional arrays works similarly:

    A[-1, *]              % The last row of A
    A[[1:5], [2:7]]       % 2d array using rows 1-5 and columns 2-7
    A[[5:1:-1], [2:7]]    % Same as above except the rows are reversed

Array indices can also be arrays of integers. For example, suppose
that I = [0:9] is an array of 10 integers. Then
A[I] is equivalent to an array of the first 10 elements
of A. A practical example of this is a sorting
operation such as:

    I = array_sort(A);    % Obtain a list of sort indices
    B = A[I];             % B is the sorted version of A
    C = A[array_sort(A)]; % Same as above but more concise.

1999: D
Consider the array:

Take a slice out of it:

and the contents of b will be [7, 3, 8]. The first index of the slice is inclusive, the second is exclusive.

means that the dynamic array c now contains [8, 6] because inside the [] the $ symbol refers to the length of the array.
D array slices are aliased to the original array, so:

means that a now has the contents [2, 5, 7, 3, 10, 6, 4, 1]. To create a copy of the array data, instead of only an alias, do:

Unlike Python, D slice bounds don't saturate, so code equivalent to this Python code is an error in D:

2004: SuperCollider
The programming language SuperCollider implements some concepts from J/APL. Slicing looks as follows:

2005: fish
Arrays in fish are always one-based, thus the indices of a new slice will begin with one, regardless of the previous indices.

2006: Cobra
Cobra supports Python-style slicing. If you have a list

then the first 3 elements, middle 3 elements, and last 3 elements would be:

Cobra also supports slicing-style syntax for 'numeric for loops':

2006: Windows PowerShell
Arrays are zero-based in PowerShell and can be defined using the comma operator:

2009: Go
Go supports Python-style syntax for slicing (except negative indices are not supported). Arrays and slices can be sliced. If you have a slice

then the first 3 elements, middle 3 elements, last 3 elements, and a copy of the entire slice would be:

Slices in Go are reference types, which means that different slices may refer to the same underlying array.

2010: Cilk Plus
Cilk Plus supports syntax for array slicing as an extension to C and C++.

Cilk Plus slicing looks as follows:

Cilk Plus's array slicing differs from Fortran's in two ways:

the second parameter is the length (number of elements in the slice) instead of the upper bound, in order to be consistent with standard C libraries;
slicing never produces a temporary, and thus never needs to allocate memory. Assignments are required to be either non-overlapping or perfectly overlapping, otherwise the result is undefined.

2012: Julia
Julia array slicing is like that of MATLAB, but uses square brackets.  Example:

See also
Comparison of programming languages (array) § Slicing


== References ==

## Archive Info
- **Archived on:** 2024-12-15 21:03:28 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 15536 bytes
- **Word Count:** 2568 words
