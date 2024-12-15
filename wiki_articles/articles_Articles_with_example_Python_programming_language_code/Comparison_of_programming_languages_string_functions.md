# Comparison of programming languages (string functions)

## Metadata
- **Last Updated:** 2024-12-03 07:00:59 UTC
- **Original Article:** [Comparison of programming languages (string functions)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(string_functions))
- **Language:** en
- **Page ID:** 3681422

## Summary
String functions are used in computer programming languages to manipulate a string or query information about a string (some do both).
Most programming languages that have a string datatype will have some string functions although there may be other low-level ways within each language to handle strings directly. In object-oriented languages, string functions are often implemented as properties and methods of string objects. In functional and list-based languages a string is represented as a list (of character codes), therefore all list-manipulation procedures could be considered string functions. However such languages may implement a subset of explicit string-specific functions as well.
For function that manipulate strings, modern object-oriented languages, like C# and Java have immutable strings and return a copy (in newly allocated dynamic memory), while others, like C manipulate the original string unless the programmer copies data to a new string. See for example Concatenation below.
The most basic example of a string function is the length(string) function. This function returns the length of a string literal.

e.g. length("hello world") would return 11.
Other languages may have string functions with similar or exactly the same syntax or parameters or outcomes. For example, in many languages the length function is usually represented as len(string).  The below list of common functions aims to help limit this confusion.

## Categories
This article belongs to the following categories:

- Category:All articles needing additional references
- Category:Articles needing additional references from July 2013
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Programming language comparisons
- Category:Short description is different from Wikidata
- Category:String (computer science)
- Category:Webarchive template wayback links

## Table of Contents

- Common string functions (multi language reference)

## Content

String functions are used in computer programming languages to manipulate a string or query information about a string (some do both).
Most programming languages that have a string datatype will have some string functions although there may be other low-level ways within each language to handle strings directly. In object-oriented languages, string functions are often implemented as properties and methods of string objects. In functional and list-based languages a string is represented as a list (of character codes), therefore all list-manipulation procedures could be considered string functions. However such languages may implement a subset of explicit string-specific functions as well.
For function that manipulate strings, modern object-oriented languages, like C# and Java have immutable strings and return a copy (in newly allocated dynamic memory), while others, like C manipulate the original string unless the programmer copies data to a new string. See for example Concatenation below.
The most basic example of a string function is the length(string) function. This function returns the length of a string literal.

e.g. length("hello world") would return 11.
Other languages may have string functions with similar or exactly the same syntax or parameters or outcomes. For example, in many languages the length function is usually represented as len(string).  The below list of common functions aims to help limit this confusion.

Common string functions (multi language reference)
String functions common to many languages are listed below, including the different names used.  The below list of common functions aims to help programmers find the equivalent function in a language. Note, string concatenation and regular expressions are handled in separate pages. Statements in guillemets (« … ») are optional.

CharAt
# Example in ALGOL 68 #
"Hello, World"[2];             // 'e'

Compare (integer result)
Compare (relational operator-based, Boolean result)
Concatenation
Contains
¢ Example in ALGOL 68 ¢
string in string("e", loc int, "Hello mate");      ¢ returns true ¢
string in string("z", loc int, "word");            ¢ returns false ¢

Equality
Tests if two strings are equal. See also #Compare and #Compare. Note that doing equality checks via a generic Compare with integer result is not only confusing for the programmer but is often a significantly more expensive operation; this is especially true when using "C-strings".

Find
Examples

Common Lisp

C#

Raku

Scheme

Visual Basic

Smalltalk

Find character
^a  Given a set of characters, SCAN returns the position of the first character found, while VERIFY returns the position of the first character that does not belong to the set.

Format
Inequality
Tests if two strings are not equal. See also #Equality.

index
see #Find

indexof
see #Find

instr
see #Find

instrrev
see #rfind

join
lastindexof
see #rfind

left
len
see #length

length
locate
see #Find

Lowercase
mid
see #substring

partition
replace
reverse
rfind
right
rpartition
slice
see #substring

split
sprintf
see #Format

strip
see #trim

strcmp
see #Compare (integer result)

substring
Uppercase
trim
trim or strip is used to remove whitespace from the beginning, end, or both beginning and end, of a string.

Other languages
In languages without a built-in trim function, it is usually simple to create a custom function which accomplishes the same task.

APL
APL can use regular expressions directly:

Alternatively, a functional approach combining Boolean masks that filter away leading and trailing spaces:

Or reverse and remove leading spaces, twice:

AWK
In AWK, one can use regular expressions to trim:

or:

C/C++
There is no standard trim function in C or C++. Most of the available string libraries for C contain code which implements trimming, or functions that significantly ease an efficient implementation. The function has also often been called EatWhitespace in some non-standard C libraries.
In C, programmers often combine a ltrim and rtrim to implement trim:

The open source C++ library Boost has several trim variants, including a standard one:

With boost's function named simply trim the input sequence is modified in-place, and returns no result.
Another open source C++ library Qt, has several trim variants, including a standard one:

The Linux kernel also includes a strip function, strstrip(), since 2.6.18-rc1, which trims the string "in place". Since 2.6.33-rc1, the kernel uses strim() instead of strstrip() to avoid false warnings.

Haskell
A trim algorithm in Haskell:

may be interpreted as follows: f drops the preceding whitespace, and reverses the string. f is then again applied to its own output. Note that the type signature (the second line) is optional.

J
The trim algorithm in J is a functional description:

That is: filter (#~) for non-space characters (' '&~:) between leading (+./\) and (*.) trailing (+./\.) spaces.

JavaScript
There is a built-in trim function in JavaScript 1.8.1 (Firefox 3.5 and later), and the ECMAScript 5 standard. In earlier versions it can be added to the String object's prototype as follows:

Perl
Perl 5 has no built-in trim function. However, the functionality is commonly achieved using regular expressions.
Example:

 
or:

 
These examples modify the value of the original variable $string.
Also available for Perl is StripLTSpace in String::Strip from CPAN.
There are, however, two functions that are commonly used to strip whitespace from the end of strings, chomp and chop:

chop removes the last character from a string and returns it.
chomp removes the trailing newline character(s) from a string if present. (What constitutes a newline is $INPUT_RECORD_SEPARATOR dependent).
In Raku, the upcoming sister language of Perl, strings have a trim method.
Example:

Tcl
The Tcl string command has three relevant subcommands:  trim, trimright and trimleft.  For each of those commands, an additional argument may be specified:  a string that represents a set of characters to remove—the default is whitespace (space, tab, newline, carriage return).
Example of trimming vowels:

XSLT
XSLT includes the function normalize-space(string) which strips leading and trailing whitespace, in addition to replacing any whitespace sequence (including line breaks) with a single space.
Example:

XSLT 2.0 includes regular expressions, providing another mechanism to perform string trimming.
Another XSLT technique for trimming is to utilize the XPath 2.0 substring() function.


== References ==

## Archive Info
- **Archived on:** 2024-12-15 21:04:01 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 6528 bytes
- **Word Count:** 987 words
