# Comparison of programming languages (string functions)

## Article Metadata

- **Last Updated:** 2024-12-15T04:08:28.385294+00:00
- **Original Article:** [Comparison of programming languages (string functions)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(string_functions))
- **Language:** en
- **Page ID:** 3681422

## Summary

String functions are used in computer programming languages to manipulate a string or query information about a string (some do both).
Most programming languages that have a string datatype will have some string functions although there may be other low-level ways within each language to handle strings directly. In object-oriented languages, string functions are often implemented as properties and methods of string objects. In functional and list-based languages a string is represented as a list

## Categories

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

## Related Articles

### Internal Links

- [.NET](https://en.wikipedia.org/wiki/.NET)
- [ALGOL 58](https://en.wikipedia.org/wiki/ALGOL_58)
- [ALGOL 60](https://en.wikipedia.org/wiki/ALGOL_60)
- [ALGOL 68](https://en.wikipedia.org/wiki/ALGOL_68)
- [APL (programming language)](https://en.wikipedia.org/wiki/APL_(programming_language))
- [AWK](https://en.wikipedia.org/wiki/AWK)
- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language))
- [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- [Assignment (computer science)](https://en.wikipedia.org/wiki/Assignment_(computer_science))
- [BASIC](https://en.wikipedia.org/wiki/BASIC)
- [Bash (Unix shell)](https://en.wikipedia.org/wiki/Bash_(Unix_shell))
- [Boost (C++ libraries)](https://en.wikipedia.org/wiki/Boost_(C%2B%2B_libraries))
- [Bourne shell](https://en.wikipedia.org/wiki/Bourne_shell)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C++20](https://en.wikipedia.org/wiki/C%2B%2B20)
- [C++23](https://en.wikipedia.org/wiki/C%2B%2B23)
- [COBOL](https://en.wikipedia.org/wiki/COBOL)
- [CPAN](https://en.wikipedia.org/wiki/CPAN)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Character (computing)](https://en.wikipedia.org/wiki/Character_(computing))
- [Clojure](https://en.wikipedia.org/wiki/Clojure)
- [Cobra (programming language)](https://en.wikipedia.org/wiki/Cobra_(programming_language))
- [Cocoa (API)](https://en.wikipedia.org/wiki/Cocoa_(API))
- [Character encoding](https://en.wikipedia.org/wiki/Character_encoding)
- [Adobe ColdFusion](https://en.wikipedia.org/wiki/Adobe_ColdFusion)
- [Comment (computer programming)](https://en.wikipedia.org/wiki/Comment_(computer_programming))
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Comparison of ALGOL 68 and C++](https://en.wikipedia.org/wiki/Comparison_of_ALGOL_68_and_C%2B%2B)
- [Comparison of C Sharp and Java](https://en.wikipedia.org/wiki/Comparison_of_C_Sharp_and_Java)
- [Comparison of C Sharp and Visual Basic .NET](https://en.wikipedia.org/wiki/Comparison_of_C_Sharp_and_Visual_Basic_.NET)
- [Comparison of Java and C++](https://en.wikipedia.org/wiki/Comparison_of_Java_and_C%2B%2B)
- [Comparison of Pascal and C](https://en.wikipedia.org/wiki/Comparison_of_Pascal_and_C)
- [Comparison of Pascal and C](https://en.wikipedia.org/wiki/Comparison_of_Pascal_and_C)
- [Comparison of Pascal and Delphi](https://en.wikipedia.org/wiki/Comparison_of_Pascal_and_Delphi)
- [Comparison of Visual Basic and Visual Basic .NET](https://en.wikipedia.org/wiki/Comparison_of_Visual_Basic_and_Visual_Basic_.NET)
- [Comparison of programming languages](https://en.wikipedia.org/wiki/Comparison_of_programming_languages)
- [Comparison of programming languages (algebraic data type)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(algebraic_data_type))
- [Comparison of programming languages (array)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(array))
- [Comparison of programming languages (associative array)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(associative_array))
- [Comparison of programming languages (basic instructions)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(basic_instructions))
- [Comparison of programming languages (functional programming)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(functional_programming))
- [Higher-order function](https://en.wikipedia.org/wiki/Higher-order_function)
- [Comparison of programming languages (list comprehension)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(list_comprehension))
- [Comparison of programming languages (object-oriented programming)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(object-oriented_programming))
- [Operator (computer programming)](https://en.wikipedia.org/wiki/Operator_(computer_programming))
- [Comparison of programming languages (strings)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(strings))
- [Comparison of programming languages (syntax)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(syntax))
- [Comparison of programming languages by type system](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_by_type_system)
- [Dependent type](https://en.wikipedia.org/wiki/Dependent_type)
- [Compatibility of C and C++](https://en.wikipedia.org/wiki/Compatibility_of_C_and_C%2B%2B)
- [Concatenation](https://en.wikipedia.org/wiki/Concatenation)
- [Constructor (object-oriented programming)](https://en.wikipedia.org/wiki/Constructor_(object-oriented_programming))
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Data type](https://en.wikipedia.org/wiki/Data_type)
- [Delphi (software)](https://en.wikipedia.org/wiki/Delphi_(software))
- [Do while loop](https://en.wikipedia.org/wiki/Do_while_loop)
- [Echo (command)](https://en.wikipedia.org/wiki/Echo_(command))
- [Eiffel (programming language)](https://en.wikipedia.org/wiki/Eiffel_(programming_language))
- [Enumerated type](https://en.wikipedia.org/wiki/Enumerated_type)
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Evaluation strategy](https://en.wikipedia.org/wiki/Evaluation_strategy)
- [Exception handling syntax](https://en.wikipedia.org/wiki/Exception_handling_syntax)
- [F Sharp (programming language)](https://en.wikipedia.org/wiki/F_Sharp_(programming_language))
- [Factor (programming language)](https://en.wikipedia.org/wiki/Factor_(programming_language))
- [Filter (higher-order function)](https://en.wikipedia.org/wiki/Filter_(higher-order_function))
- [Fold (higher-order function)](https://en.wikipedia.org/wiki/Fold_(higher-order_function))
- [For loop](https://en.wikipedia.org/wiki/For_loop)
- [Foreach loop](https://en.wikipedia.org/wiki/Foreach_loop)
- [Format (Common Lisp)](https://en.wikipedia.org/wiki/Format_(Common_Lisp))
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [FreeBASIC](https://en.wikipedia.org/wiki/FreeBASIC)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [Generator (computer programming)](https://en.wikipedia.org/wiki/Generator_(computer_programming))
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Guillemet](https://en.wikipedia.org/wiki/Guillemet)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [ISLISP](https://en.wikipedia.org/wiki/ISLISP)
- [Ingres (database)](https://en.wikipedia.org/wiki/Ingres_(database))
- [J (programming language)](https://en.wikipedia.org/wiki/J_(programming_language))
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Julia (programming language)](https://en.wikipedia.org/wiki/Julia_(programming_language))
- [Kotlin (programming language)](https://en.wikipedia.org/wiki/Kotlin_(programming_language))
- [Lexicographic order](https://en.wikipedia.org/wiki/Lexicographic_order)
- [Linux kernel](https://en.wikipedia.org/wiki/Linux_kernel)
- [Lua (programming language)](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [Map (higher-order function)](https://en.wikipedia.org/wiki/Map_(higher-order_function))
- [Wolfram Mathematica](https://en.wikipedia.org/wiki/Wolfram_Mathematica)
- [Modulo](https://en.wikipedia.org/wiki/Modulo)
- [Null character](https://en.wikipedia.org/wiki/Null_character)
- [Null coalescing operator](https://en.wikipedia.org/wiki/Null_coalescing_operator)
- [OCaml](https://en.wikipedia.org/wiki/OCaml)
- [Object Pascal](https://en.wikipedia.org/wiki/Object_Pascal)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [Option type](https://en.wikipedia.org/wiki/Option_type)
- [Oracle Corporation](https://en.wikipedia.org/wiki/Oracle_Corporation)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PL/I](https://en.wikipedia.org/wiki/PL/I)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Pharo](https://en.wikipedia.org/wiki/Pharo)
- [Pick operating system](https://en.wikipedia.org/wiki/Pick_operating_system)
- [Pointer (computer programming)](https://en.wikipedia.org/wiki/Pointer_(computer_programming))
- [Printf (Unix)](https://en.wikipedia.org/wiki/Printf_(Unix))
- [Printf](https://en.wikipedia.org/wiki/Printf)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [History of Python](https://en.wikipedia.org/wiki/History_of_Python)
- [History of Python](https://en.wikipedia.org/wiki/History_of_Python)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [QBasic](https://en.wikipedia.org/wiki/QBasic)
- [Qt (software)](https://en.wikipedia.org/wiki/Qt_(software))
- [Rexx](https://en.wikipedia.org/wiki/Rexx)
- [Raku (programming language)](https://en.wikipedia.org/wiki/Raku_(programming_language))
- [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Rexx](https://en.wikipedia.org/wiki/Rexx)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [SAS (software)](https://en.wikipedia.org/wiki/SAS_(software))
- [SNOBOL](https://en.wikipedia.org/wiki/SNOBOL)
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [Safe navigation operator](https://en.wikipedia.org/wiki/Safe_navigation_operator)
- [Scheme (programming language)](https://en.wikipedia.org/wiki/Scheme_(programming_language))
- [Scope (computer science)](https://en.wikipedia.org/wiki/Scope_(computer_science))
- [Sed](https://en.wikipedia.org/wiki/Sed)
- [Seed7](https://en.wikipedia.org/wiki/Seed7)
- [Shift JIS](https://en.wikipedia.org/wiki/Shift_JIS)
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [C file input/output](https://en.wikipedia.org/wiki/C_file_input/output)
- [Squeak](https://en.wikipedia.org/wiki/Squeak)
- [Standard ML](https://en.wikipedia.org/wiki/Standard_ML)
- [C++ string handling](https://en.wikipedia.org/wiki/C%2B%2B_string_handling)
- [C string handling](https://en.wikipedia.org/wiki/C_string_handling)
- [C string handling](https://en.wikipedia.org/wiki/C_string_handling)
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [Comparison of programming languages (string functions)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(string_functions))
- [String literal](https://en.wikipedia.org/wiki/String_literal)
- [String operations](https://en.wikipedia.org/wiki/String_operations)
- [C string handling](https://en.wikipedia.org/wiki/C_string_handling)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Transact-SQL](https://en.wikipedia.org/wiki/Transact-SQL)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Ternary conditional operator](https://en.wikipedia.org/wiki/Ternary_conditional_operator)
- [Tr (Unix)](https://en.wikipedia.org/wiki/Tr_(Unix))
- [Trimming (computer programming)](https://en.wikipedia.org/wiki/Trimming_(computer_programming))
- [Turbo Pascal](https://en.wikipedia.org/wiki/Turbo_Pascal)
- [Turing (programming language)](https://en.wikipedia.org/wiki/Turing_(programming_language))
- [UTF-16](https://en.wikipedia.org/wiki/UTF-16)
- [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
- [Unix](https://en.wikipedia.org/wiki/Unix)
- [Unspecified behavior](https://en.wikipedia.org/wiki/Unspecified_behavior)
- [Visual Basic (.NET)](https://en.wikipedia.org/wiki/Visual_Basic_(.NET))
- [Visual Basic (classic)](https://en.wikipedia.org/wiki/Visual_Basic_(classic))
- [Visual Basic (.NET)](https://en.wikipedia.org/wiki/Visual_Basic_(.NET))
- [Visual Basic (.NET)](https://en.wikipedia.org/wiki/Visual_Basic_(.NET))
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [While loop](https://en.wikipedia.org/wiki/While_loop)
- [PowerShell](https://en.wikipedia.org/wiki/PowerShell)
- [Wolfram Language](https://en.wikipedia.org/wiki/Wolfram_Language)
- [XSLT](https://en.wikipedia.org/wiki/XSLT)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Comparison of programming languages](https://en.wikipedia.org/wiki/Template:Comparison_of_programming_languages)
- [Template talk:Comparison of programming languages](https://en.wikipedia.org/wiki/Template_talk:Comparison_of_programming_languages)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from July 2013](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_July_2013)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:08:28.385294+00:00_