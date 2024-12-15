# Comparison of programming languages (list comprehension)

## Article Metadata

- **Last Updated:** 2024-12-15T04:08:22.888734+00:00
- **Original Article:** [Comparison of programming languages (list comprehension)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(list_comprehension))
- **Language:** en
- **Page ID:** 18519593

## Summary

List comprehension is a syntactic construct available in some programming languages for creating a list based on existing lists.  It follows the form of the mathematical set-builder notation (set comprehension) as distinct from the use of map and filter functions.

## Categories

- Category:All articles needing additional references
- Category:Articles needing additional references from February 2009
- Category:Articles with example C Sharp code
- Category:Articles with example Haskell code
- Category:Articles with example Julia code
- Category:Articles with example Lisp (programming language) code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Racket code
- Category:Articles with hatnote templates targeting a nonexistent page
- Category:Programming language comparisons

## Table of Contents

- Examples of list comprehension
- References
- External links

## Content

List comprehension is a syntactic construct available in some programming languages for creating a list based on existing lists.  It follows the form of the mathematical set-builder notation (set comprehension) as distinct from the use of map and filter functions.

Examples of list comprehension
Boo
List with all the doubles from 0 to 10 (exclusive)

List with the names of the customers based in Rio de Janeiro

C#
The previous code is syntactic sugar for the following code written using lambda expressions:

Ceylon
Filtering numbers divisible by 3:

Multiple "generators":

Clojure
An infinite lazy sequence:

A list comprehension using multiple generators:

CoffeeScript
Common Lisp
List comprehensions can be expressed with the loop macro's collect keyword. Conditionals are expressed with if, as follows:

Cobra
List the names of customers:

List the customers with balances:

List the names of customers with balances:

The general forms:

Note that by putting the condition and expression after the variable name and enumerable object, editors and IDEs can provide autocompletion on the members of the variable.

Dart
Elixir
Erlang
F#
Lazily-evaluated sequences:

Or, for floating point values

Lists and arrays:

List comprehensions are the part of a greater family of language constructs called computation expressions.

Haskell
An example of a list comprehension using multiple generators:

Io
By using Range object, Io language can create list as easy as in other languages:

ISLISP
List comprehensions can be expressed with the for special form. Conditionals are expressed with if, as follows:

Julia
Julia supports comprehensions using the syntax:

and multidimensional comprehensions like:

It is also possible to add a condition:

And just changing square brackets to the round one, we get a generator:

Mythryl
s = [ 2*i for i in 1..100 where i*i > 3 ];

Multiple generators:

 pyth = [ (x,y,z) for x in 1..20 for y in x..20 for z in y..20 where x*x + y*y == z*z ];

Nemerle
Nim
Nim has built-in seq, set, table and object comprehensions on the sugar standard library module:

The comprehension is implemented as a macro that is expanded at compile time, 
you can see the expanded code using the expandMacro compiler option:

The comprehensions can be nested and multi-line:

OCaml
OCaml supports List comprehension through OCaml Batteries.

Perl
Array with all the doubles from 1 to 9 inclusive:

Array with the names of the customers based in Rio de Janeiro (from array of hashes):

Filtering numbers divisible by 3:

PowerShell
which is short-hand notation of:

Python
Python uses the following syntax to express list comprehensions over finite lists:

A generator expression may be used in Python versions >= 2.4 which gives lazy evaluation over its input, and can be used with generators to iterate over 'infinite' input such as the count generator function which returns successive integers:

(Subsequent use of the generator expression will determine when to stop generating values).

R
Racket
An example with multiple generators:

Raku
Scala
Using the for-comprehension:

Scheme
List comprehensions are supported in Scheme through the use of the SRFI-42 library.

An example of a list comprehension using multiple generators:

SETL
Smalltalk
Visual Prolog
S = [ 2*X || X = list::getMember_nd(L), X*X > 3 ]

References
External links
Comparison of list comprehensions on rosettacode.org

## Related Articles

### Internal Links

- [.NET](https://en.wikipedia.org/wiki/.NET)
- [ALGOL 58](https://en.wikipedia.org/wiki/ALGOL_58)
- [ALGOL 60](https://en.wikipedia.org/wiki/ALGOL_60)
- [ALGOL 68](https://en.wikipedia.org/wiki/ALGOL_68)
- [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- [Assignment (computer science)](https://en.wikipedia.org/wiki/Assignment_(computer_science))
- [Autocomplete](https://en.wikipedia.org/wiki/Autocomplete)
- [Boo (programming language)](https://en.wikipedia.org/wiki/Boo_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Ceylon (programming language)](https://en.wikipedia.org/wiki/Ceylon_(programming_language))
- [Cobra (programming language)](https://en.wikipedia.org/wiki/Cobra_(programming_language))
- [CoffeeScript](https://en.wikipedia.org/wiki/CoffeeScript)
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
- [Comparison of programming languages (object-oriented programming)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(object-oriented_programming))
- [Operator (computer programming)](https://en.wikipedia.org/wiki/Operator_(computer_programming))
- [Comparison of programming languages (string functions)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(string_functions))
- [Comparison of programming languages (strings)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(strings))
- [Comparison of programming languages (syntax)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(syntax))
- [Comparison of programming languages by type system](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_by_type_system)
- [Dependent type](https://en.wikipedia.org/wiki/Dependent_type)
- [Compatibility of C and C++](https://en.wikipedia.org/wiki/Compatibility_of_C_and_C%2B%2B)
- [Constructor (object-oriented programming)](https://en.wikipedia.org/wiki/Constructor_(object-oriented_programming))
- [Dart (programming language)](https://en.wikipedia.org/wiki/Dart_(programming_language))
- [Do while loop](https://en.wikipedia.org/wiki/Do_while_loop)
- [Elixir (programming language)](https://en.wikipedia.org/wiki/Elixir_(programming_language))
- [Enumerated type](https://en.wikipedia.org/wiki/Enumerated_type)
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Evaluation strategy](https://en.wikipedia.org/wiki/Evaluation_strategy)
- [Exception handling syntax](https://en.wikipedia.org/wiki/Exception_handling_syntax)
- [F Sharp (programming language)](https://en.wikipedia.org/wiki/F_Sharp_(programming_language))
- [Filter (higher-order function)](https://en.wikipedia.org/wiki/Filter_(higher-order_function))
- [Fold (higher-order function)](https://en.wikipedia.org/wiki/Fold_(higher-order_function))
- [For loop](https://en.wikipedia.org/wiki/For_loop)
- [Foreach loop](https://en.wikipedia.org/wiki/Foreach_loop)
- [Generator (computer programming)](https://en.wikipedia.org/wiki/Generator_(computer_programming))
- [Generator (computer programming)](https://en.wikipedia.org/wiki/Generator_(computer_programming))
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [ISLISP](https://en.wikipedia.org/wiki/ISLISP)
- [Io (programming language)](https://en.wikipedia.org/wiki/Io_(programming_language))
- [Julia (programming language)](https://en.wikipedia.org/wiki/Julia_(programming_language))
- [Lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation)
- [List comprehension](https://en.wikipedia.org/wiki/List_comprehension)
- [Map (higher-order function)](https://en.wikipedia.org/wiki/Map_(higher-order_function))
- [Modulo](https://en.wikipedia.org/wiki/Modulo)
- [Mono (software)](https://en.wikipedia.org/wiki/Mono_(software))
- [Nemerle](https://en.wikipedia.org/wiki/Nemerle)
- [Nim (programming language)](https://en.wikipedia.org/wiki/Nim_(programming_language))
- [Null coalescing operator](https://en.wikipedia.org/wiki/Null_coalescing_operator)
- [OCaml](https://en.wikipedia.org/wiki/OCaml)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [PowerShell](https://en.wikipedia.org/wiki/PowerShell)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python syntax and semantics](https://en.wikipedia.org/wiki/Python_syntax_and_semantics)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Racket (programming language)](https://en.wikipedia.org/wiki/Racket_(programming_language))
- [Raku (programming language)](https://en.wikipedia.org/wiki/Raku_(programming_language))
- [Rio de Janeiro](https://en.wikipedia.org/wiki/Rio_de_Janeiro)
- [SETL](https://en.wikipedia.org/wiki/SETL)
- [Safe navigation operator](https://en.wikipedia.org/wiki/Safe_navigation_operator)
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scheme (programming language)](https://en.wikipedia.org/wiki/Scheme_(programming_language))
- [Scheme Requests for Implementation](https://en.wikipedia.org/wiki/Scheme_Requests_for_Implementation)
- [Scope (computer science)](https://en.wikipedia.org/wiki/Scope_(computer_science))
- [Set-builder notation](https://en.wikipedia.org/wiki/Set-builder_notation)
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar)
- [Syntax (programming languages)](https://en.wikipedia.org/wiki/Syntax_(programming_languages))
- [Ternary conditional operator](https://en.wikipedia.org/wiki/Ternary_conditional_operator)
- [Visual Prolog](https://en.wikipedia.org/wiki/Visual_Prolog)
- [While loop](https://en.wikipedia.org/wiki/While_loop)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Comparison of programming languages](https://en.wikipedia.org/wiki/Template:Comparison_of_programming_languages)
- [Template talk:Comparison of programming languages](https://en.wikipedia.org/wiki/Template_talk:Comparison_of_programming_languages)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from February 2009](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_February_2009)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:08:22.888734+00:00_