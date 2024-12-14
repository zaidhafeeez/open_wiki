# Higher-order function

## Article Metadata

- **Last Updated:** 2024-12-14T19:38:24.827606+00:00
- **Original Article:** [Higher-order function](https://en.wikipedia.org/wiki/Higher-order_function)
- **Language:** en
- **Page ID:** 244689

## Summary

In mathematics and computer science, a higher-order function (HOF) is a function that does at least one of the following:
takes one or more functions as arguments (i.e. a procedural parameter, which is a parameter of a procedure that is itself a procedure),
returns a function or value as its result.
All other functions are first-order functions. In mathematics higher-order functions are also termed operators or functionals. The differential operator in calculus is a common example, since it maps

## Categories

- Category:All articles needing additional references
- Category:Articles needing additional references from November 2024
- Category:Articles with example C++ code
- Category:Articles with example C code
- Category:Articles with example D code
- Category:Articles with example Haskell code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example Julia code
- Category:Articles with example Lisp (programming language) code
- Category:Articles with example MATLAB/Octave code
- Category:Articles with example PHP code
- Category:Articles with example Pascal code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with example Scala code
- Category:Articles with example Scheme (programming language) code
- Category:Articles with example Swift code
- Category:Articles with example Tcl code
- Category:Articles with short description
- Category:Functional programming
- Category:Higher-order functions
- Category:Lambda calculus
- Category:Short description is different from Wikidata
- Category:Subroutines

## Table of Contents

- General examples
- Support in programming languages
- See also

## Content

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

## Related Articles

### Internal Links

- [APL (programming language)](https://en.wikipedia.org/wiki/APL_(programming_language))
- [Algebraic function](https://en.wikipedia.org/wiki/Algebraic_function)
- [Analytic function](https://en.wikipedia.org/wiki/Analytic_function)
- [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- [Apply](https://en.wikipedia.org/wiki/Apply)
- [Bijection](https://en.wikipedia.org/wiki/Bijection)
- [Binary relation](https://en.wikipedia.org/wiki/Binary_relation)
- [Boilerplate code](https://en.wikipedia.org/wiki/Boilerplate_code)
- [Boolean-valued function](https://en.wikipedia.org/wiki/Boolean-valued_function)
- [Boolean function](https://en.wikipedia.org/wiki/Boolean_function)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C++11](https://en.wikipedia.org/wiki/C%2B%2B11)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Calculus](https://en.wikipedia.org/wiki/Calculus)
- [Callback (computer programming)](https://en.wikipedia.org/wiki/Callback_(computer_programming))
- [Clojure](https://en.wikipedia.org/wiki/Clojure)
- [ColdFusion Markup Language](https://en.wikipedia.org/wiki/ColdFusion_Markup_Language)
- [Combinatory logic](https://en.wikipedia.org/wiki/Combinatory_logic)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Complex analysis](https://en.wikipedia.org/wiki/Complex_analysis)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Constant function](https://en.wikipedia.org/wiki/Constant_function)
- [Continuous function](https://en.wikipedia.org/wiki/Continuous_function)
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Dart (programming language)](https://en.wikipedia.org/wiki/Dart_(programming_language))
- [Defunctionalization](https://en.wikipedia.org/wiki/Defunctionalization)
- [Derivative](https://en.wikipedia.org/wiki/Derivative)
- [Differential operator](https://en.wikipedia.org/wiki/Differential_operator)
- [Don't repeat yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
- [Memory management](https://en.wikipedia.org/wiki/Memory_management)
- [Elixir (programming language)](https://en.wikipedia.org/wiki/Elixir_(programming_language))
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [F Sharp (programming language)](https://en.wikipedia.org/wiki/F_Sharp_(programming_language))
- [Filter (higher-order function)](https://en.wikipedia.org/wiki/Filter_(higher-order_function))
- [First-class function](https://en.wikipedia.org/wiki/First-class_function)
- [First-class function](https://en.wikipedia.org/wiki/First-class_function)
- [Fold (higher-order function)](https://en.wikipedia.org/wiki/Fold_(higher-order_function))
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Free Pascal](https://en.wikipedia.org/wiki/Free_Pascal)
- [Function-level programming](https://en.wikipedia.org/wiki/Function-level_programming)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Function (mathematics)](https://en.wikipedia.org/wiki/Function_(mathematics))
- [Function composition](https://en.wikipedia.org/wiki/Function_composition)
- [Function composition (computer science)](https://en.wikipedia.org/wiki/Function_composition_(computer_science))
- [Complex analysis](https://en.wikipedia.org/wiki/Complex_analysis)
- [Function of a real variable](https://en.wikipedia.org/wiki/Function_of_a_real_variable)
- [Function of several complex variables](https://en.wikipedia.org/wiki/Function_of_several_complex_variables)
- [Function of several real variables](https://en.wikipedia.org/wiki/Function_of_several_real_variables)
- [Function overloading](https://en.wikipedia.org/wiki/Function_overloading)
- [Function pointer](https://en.wikipedia.org/wiki/Function_pointer)
- [Function space](https://en.wikipedia.org/wiki/Function_space)
- [Functional (mathematics)](https://en.wikipedia.org/wiki/Functional_(mathematics))
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [Functor](https://en.wikipedia.org/wiki/Functor)
- [Functor (disambiguation)](https://en.wikipedia.org/wiki/Functor_(disambiguation))
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Higher order message](https://en.wikipedia.org/wiki/Higher_order_message)
- [History of the function concept](https://en.wikipedia.org/wiki/History_of_the_function_concept)
- [Identity function](https://en.wikipedia.org/wiki/Identity_function)
- [Imperative programming](https://en.wikipedia.org/wiki/Imperative_programming)
- [Implicit function](https://en.wikipedia.org/wiki/Implicit_function)
- [Injective function](https://en.wikipedia.org/wiki/Injective_function)
- [Integer-valued function](https://en.wikipedia.org/wiki/Integer-valued_function)
- [Integral](https://en.wikipedia.org/wiki/Integral)
- [Interpreter (computing)](https://en.wikipedia.org/wiki/Interpreter_(computing))
- [Inverse function](https://en.wikipedia.org/wiki/Inverse_function)
- [J (programming language)](https://en.wikipedia.org/wiki/J_(programming_language))
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Java version history](https://en.wikipedia.org/wiki/Java_version_history)
- [Julia (programming language)](https://en.wikipedia.org/wiki/Julia_(programming_language))
- [Just-in-time compilation](https://en.wikipedia.org/wiki/Just-in-time_compilation)
- [Kappa calculus](https://en.wikipedia.org/wiki/Kappa_calculus)
- [Kotlin (programming language)](https://en.wikipedia.org/wiki/Kotlin_(programming_language))
- [Lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus)
- [Linear map](https://en.wikipedia.org/wiki/Linear_map)
- [List of mathematical functions](https://en.wikipedia.org/wiki/List_of_mathematical_functions)
- [Lua (programming language)](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [Macro (computer science)](https://en.wikipedia.org/wiki/Macro_(computer_science))
- [Map (higher-order function)](https://en.wikipedia.org/wiki/Map_(higher-order_function))
- [Mathematics](https://en.wikipedia.org/wiki/Mathematics)
- [Measurable function](https://en.wikipedia.org/wiki/Measurable_function)
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Montague grammar](https://en.wikipedia.org/wiki/Montague_grammar)
- [Morphism](https://en.wikipedia.org/wiki/Morphism)
- [Multivalued function](https://en.wikipedia.org/wiki/Multivalued_function)
- [OCaml](https://en.wikipedia.org/wiki/OCaml)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Operator (mathematics)](https://en.wikipedia.org/wiki/Operator_(mathematics))
- [Ordered pair](https://en.wikipedia.org/wiki/Ordered_pair)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Parameter (computer programming)](https://en.wikipedia.org/wiki/Parameter_(computer_programming))
- [Partial function](https://en.wikipedia.org/wiki/Partial_function)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Polynomial](https://en.wikipedia.org/wiki/Polynomial)
- [Procedural parameter](https://en.wikipedia.org/wiki/Procedural_parameter)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Qsort](https://en.wikipedia.org/wiki/Qsort)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Raku (programming language)](https://en.wikipedia.org/wiki/Raku_(programming_language))
- [Rational function](https://en.wikipedia.org/wiki/Rational_function)
- [Real-valued function](https://en.wikipedia.org/wiki/Real-valued_function)
- [Record (computer science)](https://en.wikipedia.org/wiki/Record_(computer_science))
- [Relation (mathematics)](https://en.wikipedia.org/wiki/Relation_(mathematics))
- [Restriction (mathematics)](https://en.wikipedia.org/wiki/Restriction_(mathematics))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scheme (programming language)](https://en.wikipedia.org/wiki/Scheme_(programming_language))
- [Sequence](https://en.wikipedia.org/wiki/Sequence)
- [Set-valued function](https://en.wikipedia.org/wiki/Set-valued_function)
- [Smoothness](https://en.wikipedia.org/wiki/Smoothness)
- [Stack-based memory allocation](https://en.wikipedia.org/wiki/Stack-based_memory_allocation)
- [Strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Surjective function](https://en.wikipedia.org/wiki/Surjective_function)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Tree traversal](https://en.wikipedia.org/wiki/Tree_traversal)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Typed lambda calculus](https://en.wikipedia.org/wiki/Typed_lambda_calculus)
- [XACML](https://en.wikipedia.org/wiki/XACML)
- [XQuery](https://en.wikipedia.org/wiki/XQuery)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Functions navbox](https://en.wikipedia.org/wiki/Template:Functions_navbox)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from November 2024](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_November_2024)
- [Category:Functions](https://en.wikipedia.org/wiki/Category:Functions)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:38:24.827606+00:00_