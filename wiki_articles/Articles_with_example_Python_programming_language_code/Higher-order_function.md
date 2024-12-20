---
title: Higher-order function
url: https://en.wikipedia.org/wiki/Higher-order_function
language: en
categories: ["Category:All articles needing additional references", "Category:Articles needing additional references from November 2024", "Category:Articles with example C++ code", "Category:Articles with example C code", "Category:Articles with example D code", "Category:Articles with example Haskell code", "Category:Articles with example JavaScript code", "Category:Articles with example Java code", "Category:Articles with example Julia code", "Category:Articles with example Lisp (programming language) code", "Category:Articles with example MATLAB/Octave code", "Category:Articles with example PHP code", "Category:Articles with example Pascal code", "Category:Articles with example Perl code", "Category:Articles with example Python (programming language) code", "Category:Articles with example R code", "Category:Articles with example Scala code", "Category:Articles with example Scheme (programming language) code", "Category:Articles with example Swift code", "Category:Articles with example Tcl code", "Category:Articles with short description", "Category:Functional programming", "Category:Higher-order functions", "Category:Lambda calculus", "Category:Short description is different from Wikidata", "Category:Subroutines"]
references: 0
last_modified: 2024-12-19T13:43:36Z
---

# Higher-order function

## Summary

In mathematics and computer science, a higher-order function (HOF) is a function that does at least one of the following:
takes one or more functions as arguments (i.e. a procedural parameter, which is a parameter of a procedure that is itself a procedure),
returns a function or value as its result.
All other functions are first-order functions. In mathematics higher-order functions are also termed operators or functionals. The differential operator in calculus is a common example, since it maps

## Full Content

In mathematics and computer science, a higher-order function (HOF) is a function that does at least one of the following:
takes one or more functions as arguments (i.e. a procedural parameter, which is a parameter of a procedure that is itself a procedure),
returns a function or value as its result.
All other functions are first-order functions. In mathematics higher-order functions are also termed operators or functionals. The differential operator in calculus is a common example, since it maps a function to its derivative, also a function. Higher-order functions should not be confused with other uses of the word "functor" throughout mathematics, see Functor (disambiguation).
In the untyped lambda calculus, all functions are higher-order; in a typed lambda calculus, from which most functional programming languages are derived, higher-order functions that take one function as argument are values with types of the form 
  
    
      
        (
        
          τ
          
            1
          
        
        →
        
          τ
          
            2
          
        
        )
        →
        
          τ
          
            3
          
        
      
    
    {\displaystyle (\tau _{1}\to \tau _{2})\to \tau _{3}}
  
.

General examples
map function, found in many functional programming languages, is one example of a higher-order function. It takes as arguments a function f and a collection of elements, and as the result, returns a new collection with f applied to each element from the collection.
Sorting functions, which take a comparison function as a parameter, allowing the programmer to separate the sorting algorithm from the comparisons of the items being sorted. The C standard function qsort is an example of this.
 filter
fold
apply
Function composition
Integration
 Callback
Tree traversal
Montague grammar, a semantic theory of natural language, uses higher-order functions

Support in programming languages
Direct support
The examples are not intended to compare and contrast programming languages, but to serve as examples of higher-order function syntax
In the following examples, the higher-order function twice takes a function, and applies the function to some value twice. If twice has to be applied several times for the same f it preferably should return a function rather than a value. This is in line with the "don't repeat yourself" principle.

APL
Or in a tacit manner:

C++
Using std::function in C++11:

Or, with generic lambdas provided by C++14:

C#
Using just delegates:

Or equivalently, with static methods:

Clojure
ColdFusion Markup Language (CFML)
Common Lisp
D
Dart
Elixir
In Elixir, you can mix module definitions and anonymous functions

Alternatively, we can also compose using pure anonymous functions.

Erlang
In this Erlang example, the higher-order function or_else/2 takes a list of functions (Fs) and argument (X). It evaluates the function F with the argument X as argument. If the function F returns false then the next function in Fs will be evaluated. If the function F returns {false, Y} then the next function in Fs with argument Y will be evaluated. If the function F returns R the higher-order function or_else/2 will return R. Note that X, Y, and R can be functions. The example returns false.

F#
Go
Notice a function literal can be defined either with an identifier (twice) or anonymously (assigned to variable plusThree).

Groovy
Haskell
J
Explicitly,

or tacitly,

Java (1.8+)
Using just functional interfaces:

Or equivalently, with static methods:

JavaScript
With arrow functions:

Or with classical syntax:

Julia
Kotlin
Lua
MATLAB
OCaml
PHP
or with all functions in variables:

Note that arrow functions implicitly capture any variables that come from the parent scope, whereas anonymous functions require the use keyword to do the same.

Perl
or with all functions in variables:

Python
Python decorator syntax is often used to replace a function with the result of passing that function through a higher-order function. E.g., the function g could be implemented equivalently:

R
Raku
In Raku, all code objects are closures and therefore can reference inner "lexical" variables from an outer scope because the lexical variable is "closed" inside of the function. Raku also supports "pointy block" syntax for lambda expressions which can be assigned to a variable or invoked anonymously.

Ruby
Rust
Scala
Scheme
Swift
Tcl
Tcl uses apply command to apply an anonymous function (since 8.6).

XACML
The XACML standard defines higher-order functions in the standard to apply a function to multiple values of attribute bags.

The list of higher-order functions in XACML can be found here.

XQuery
Alternatives
Function pointers
Function pointers in languages such as C, C++, Fortran, and Pascal allow programmers to pass around references to functions. The following C code computes an approximation of the integral of an arbitrary function:

The qsort function from the C standard library uses a function pointer to emulate the behavior of a higher-order function.

Macros
Macros can also be used to achieve some of the effects of higher-order functions. However, macros cannot easily avoid the problem of variable capture; they may also result in large amounts of duplicated code, which can be more difficult for a compiler to optimize. Macros are generally not strongly typed, although they may produce strongly typed code.

Dynamic code evaluation
In other imperative programming languages, it is possible to achieve some of the same algorithmic results as are obtained via higher-order functions by dynamically executing code (sometimes called Eval or Execute operations) in the scope of evaluation. There can be significant drawbacks to this approach:

The argument code to be executed is usually not statically typed; these languages generally rely on dynamic typing to determine the well-formedness and safety of the code to be executed.
The argument is usually provided as a string, the value of which may not be known until run-time. This string must either be compiled during program execution (using just-in-time compilation) or evaluated by interpretation, causing some added overhead at run-time, and usually generating less efficient code.

Objects
In object-oriented programming languages that do not support higher-order functions, objects can be an effective substitute. An object's methods act in essence like functions, and a method may accept objects as parameters and produce objects as return values. Objects often carry added run-time overhead compared to pure functions, however, and added boilerplate code for defining and instantiating an object and its method(s). Languages that permit stack-based (versus heap-based) objects or structs can provide more flexibility with this method.
An example of using a simple stack based record in Free Pascal with a function that returns a function:

The function a() takes a Txy record as input and returns the integer value of the sum of the record's x and y fields (3 + 7).

Defunctionalization
Defunctionalization can be used to implement higher-order functions in languages that lack  first-class functions:

In this case, different types are used to trigger different functions via function overloading. The overloaded function in this example has the signature auto apply.

See also
First-class function
Combinatory logic
Function-level programming
Functional programming
Kappa calculus - a formalism for functions which excludes higher-order functions
Strategy pattern
Higher order messages


== References ==
