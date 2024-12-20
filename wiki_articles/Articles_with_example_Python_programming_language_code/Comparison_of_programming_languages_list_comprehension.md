---
title: Comparison of programming languages (list comprehension)
url: https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(list_comprehension)
language: en
categories: ["Category:All articles needing additional references", "Category:Articles needing additional references from February 2009", "Category:Articles with example C Sharp code", "Category:Articles with example Haskell code", "Category:Articles with example Julia code", "Category:Articles with example Lisp (programming language) code", "Category:Articles with example Python (programming language) code", "Category:Articles with example Racket code", "Category:Articles with hatnote templates targeting a nonexistent page", "Category:Programming language comparisons"]
references: 0
last_modified: 2024-11-28T10:33:37Z
---

# Comparison of programming languages (list comprehension)

## Summary

List comprehension is a syntactic construct available in some programming languages for creating a list based on existing lists.  It follows the form of the mathematical set-builder notation (set comprehension) as distinct from the use of map and filter functions.

## Full Content

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
