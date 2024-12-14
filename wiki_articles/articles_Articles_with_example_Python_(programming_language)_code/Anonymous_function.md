# Anonymous function

## Article Metadata

- **Last Updated:** 2024-12-14T19:32:26.564257+00:00
- **Original Article:** [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- **Language:** en
- **Page ID:** 7018181

## Summary

In computer programming, an anonymous function (function literal, expression or block) is a function definition that is not bound to an identifier. Anonymous functions are often arguments being passed to higher-order functions or used for constructing the result of a higher-order function that needs to return a function.
If the function is only used once, or a limited number of times, an anonymous function may be syntactically lighter than using a named function. Anonymous functions are ubiquito

## Categories

- Category:All articles needing additional references
- Category:Articles needing additional references from February 2018
- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example C code
- Category:Articles with example D code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example Julia code
- Category:Articles with example Lisp (programming language) code
- Category:Articles with example MATLAB/Octave code
- Category:Articles with example PHP code
- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with example Ruby code
- Category:Articles with example Scala code
- Category:Articles with example Smalltalk code
- Category:Articles with example Tcl code
- Category:Articles with example code
- Category:Articles with short description
- Category:Data types
- Category:Functional programming
- Category:Incomplete lists from August 2008
- Category:Lambda calculus
- Category:Short description matches Wikidata
- Category:Subroutines

## Table of Contents

- Names
- Uses
- List of languages
- Examples of anonymous functions
- See also
- References
- External links

## Content

In computer programming, an anonymous function (function literal, expression or block) is a function definition that is not bound to an identifier. Anonymous functions are often arguments being passed to higher-order functions or used for constructing the result of a higher-order function that needs to return a function.
If the function is only used once, or a limited number of times, an anonymous function may be syntactically lighter than using a named function. Anonymous functions are ubiquitous in functional programming languages and other languages with first-class functions, where they fulfil the same role for the function type as literals do for other data types.
Anonymous functions originate in the work of Alonzo Church in his invention of the lambda calculus, in which all functions are anonymous, in 1936, before electronic computers. In several programming languages, anonymous functions are introduced using the keyword lambda, and anonymous functions are often referred to as lambdas or lambda abstractions. Anonymous functions have been a feature of programming languages since Lisp in 1958, and a growing number of modern programming languages support anonymous functions.

Names
The names "lambda abstraction", "lambda function", and "lambda expression" refer to the notation of function abstraction in lambda calculus, where the usual function f(x) = M would be written (λx.M), and where M is an expression that uses x. Compare to the Python syntax of lambda x: M.
The name "arrow function" refers to the mathematical "maps to" symbol, x ↦ M. Compare to the JavaScript syntax of x => M.

Uses
Anonymous functions can be used for containing functionality that need not be named and possibly for short-term use. Some notable examples include closures and currying.
The use of anonymous functions is a matter of style. Using them is never the only way to solve a problem; each anonymous function could instead be defined as a named function and called by name. Anonymous functions often provide a briefer notation than defining named functions. In languages that do not permit the definition of named functions in local scopes, anonymous functions may provide encapsulation via localized scope, however the code in the body of such anonymous function may not be re-usable, or amenable to separate testing. Short/simple anonymous functions used in expressions may be easier to read and understand than separately defined named functions, though without a descriptive name they may be more difficult to understand.
In some programming languages, anonymous functions are commonly implemented for very specific purposes such as binding events to callbacks or instantiating the function for particular values, which may be more efficient in a Dynamic programming language, more readable, and less error-prone than calling a named function.
The following examples are written in Python 3.

Sorting
When attempting to sort in a non-standard way, it may be easier to contain the sorting logic as an anonymous function instead of creating a named function.
Most languages provide a generic sort function that implements a sort algorithm that will sort arbitrary objects.
This function usually accepts an arbitrary function that determines how to compare whether two elements are equal or if one is greater or less than the other.
Consider this Python code sorting a list of strings by length of the string:

The anonymous function in this example is the lambda expression:

The anonymous function accepts one argument, x, and returns the length of its argument, which is then used by the sort() method as the criteria for sorting.
Basic syntax of a lambda function in Python is 

The expression returned by the lambda function can be assigned to a variable and used in the code at multiple places.

Another example would be sorting items in a list by the name of their class (in Python, everything has a class):

Note that 11.2 has class name "float", 10 has class name "int", and 'number' has class name "str". The sorted order is "float", "int", then "str".

Closures
Closures are functions evaluated in an environment containing bound variables. The following example binds the variable "threshold" in an anonymous function that compares the input to the threshold.

This can be used as a sort of generator of comparison functions:

It would be impractical to create a function for every possible comparison function and may be too inconvenient to keep the threshold around for further use. Regardless of the reason why a closure is used, the anonymous function is the entity that contains the functionality that does the comparing.

Currying
Currying is the process of changing a function so that rather than taking multiple inputs, it takes a single input and returns a function which accepts the second input, and so forth. In this example, a function that performs division by any integer is transformed into one that performs division by a set integer.

While the use of anonymous functions is perhaps not common with currying, it still can be used. In the above example, the function divisor generates functions with a specified divisor. The functions half and third curry the divide function with a fixed divisor.
The divisor function also forms a closure by binding the variable d.

Higher-order functions
A higher-order function is a function that takes a function as an argument or returns one as a result. This is commonly used to customize the behavior of a generically defined function, often a looping construct or recursion scheme. Anonymous functions are a convenient way to specify such function arguments. The following examples are in Python 3.

Map
The map function performs a function call on each element of a list. The following example squares every element in an array with an anonymous function.

The anonymous function accepts an argument and multiplies it by itself (squares it). The above form is discouraged by the creators of the language, who maintain that the form presented below has the same meaning and is more aligned with the philosophy of the language:

Filter
The filter function returns all elements from a list that evaluate True when passed to a certain function.

The anonymous function checks if the argument passed to it is even. The same as with map, the form below is considered more appropriate:

Fold
A fold function runs over all elements in a structure (for lists usually left-to-right, a "left fold", called reduce in Python), accumulating a value as it goes. This can be used to combine all elements of a structure into one value, for example:

This performs

  
    
      
        
          (
          
            
              (
              
                
                  (
                  
                    1
                    ×
                    2
                  
                  )
                
                ×
                3
              
              )
            
            ×
            4
          
          )
        
        ×
        5
        =
        120.
      
    
    {\displaystyle \left(\left(\left(1\times 2\right)\times 3\right)\times 4\right)\times 5=120.}
  

The anonymous function here is the multiplication of the two arguments.
The result of a fold need not be one value. Instead, both map and filter can be created using fold. In map, the value that is accumulated is a new list, containing the results of applying a function to each element of the original list. In filter, the value that is accumulated is a new list containing only those elements that match the given condition.

List of languages
The following is a list of programming languages that support unnamed anonymous functions fully, or partly as some variant, or not at all.
This table shows some general trends. First, the languages that do not support anonymous functions (C, Pascal, Object Pascal) are all statically typed languages. However, statically typed languages can support anonymous functions. For example, the ML languages are statically typed and fundamentally include anonymous functions, and Delphi, a dialect of Object Pascal, has been extended to support anonymous functions, as has C++ (by the C++11 standard). Second, the languages that treat functions as first-class functions (Dylan, Haskell, JavaScript, Lisp, ML, Perl, Python, Ruby, Scheme) generally have anonymous function support so that functions can be defined and passed around as easily as other data types.

Examples of anonymous functions
See also
First-class function
Lambda calculus definition

References
External links
Anonymous Methods - When Should They Be Used? (blog about anonymous function in Delphi)
Compiling Lambda Expressions: Scala vs. Java 8
php anonymous functions php anonymous functions
Lambda functions in various programming languages
Functions in Go

## Related Articles

### Internal Links

- [ALGOL 68](https://en.wikipedia.org/wiki/ALGOL_68)
- [APL (programming language)](https://en.wikipedia.org/wiki/APL_(programming_language))
- [ActionScript](https://en.wikipedia.org/wiki/ActionScript)
- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language))
- [Alonzo Church](https://en.wikipedia.org/wiki/Alonzo_Church)
- [Assembly language](https://en.wikipedia.org/wiki/Assembly_language)
- [AutoHotkey](https://en.wikipedia.org/wiki/AutoHotkey)
- [Bash (Unix shell)](https://en.wikipedia.org/wiki/Bash_(Unix_shell))
- [Blocks (C language extension)](https://en.wikipedia.org/wiki/Blocks_(C_language_extension))
- [Free variables and bound variables](https://en.wikipedia.org/wiki/Free_variables_and_bound_variables)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C++11](https://en.wikipedia.org/wiki/C%2B%2B11)
- [COBOL](https://en.wikipedia.org/wiki/COBOL)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Clang](https://en.wikipedia.org/wiki/Clang)
- [Clojure](https://en.wikipedia.org/wiki/Clojure)
- [Closure (computer programming)](https://en.wikipedia.org/wiki/Closure_(computer_programming))
- [Closure (computer programming)](https://en.wikipedia.org/wiki/Closure_(computer_programming))
- [Adobe ColdFusion](https://en.wikipedia.org/wiki/Adobe_ColdFusion)
- [ColdFusion Markup Language](https://en.wikipedia.org/wiki/ColdFusion_Markup_Language)
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [Curl (programming language)](https://en.wikipedia.org/wiki/Curl_(programming_language))
- [Currying](https://en.wikipedia.org/wiki/Currying)
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Dart (programming language)](https://en.wikipedia.org/wiki/Dart_(programming_language))
- [Data type](https://en.wikipedia.org/wiki/Data_type)
- [Delphi (software)](https://en.wikipedia.org/wiki/Delphi_(software))
- [Dylan (programming language)](https://en.wikipedia.org/wiki/Dylan_(programming_language))
- [Dynamic programming language](https://en.wikipedia.org/wiki/Dynamic_programming_language)
- [Eiffel (programming language)](https://en.wikipedia.org/wiki/Eiffel_(programming_language))
- [Elixir (programming language)](https://en.wikipedia.org/wiki/Elixir_(programming_language))
- [Elm (programming language)](https://en.wikipedia.org/wiki/Elm_(programming_language))
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Examples of anonymous functions](https://en.wikipedia.org/wiki/Examples_of_anonymous_functions)
- [F Sharp (programming language)](https://en.wikipedia.org/wiki/F_Sharp_(programming_language))
- [Factor (programming language)](https://en.wikipedia.org/wiki/Factor_(programming_language))
- [Filter (higher-order function)](https://en.wikipedia.org/wiki/Filter_(higher-order_function))
- [First-class function](https://en.wikipedia.org/wiki/First-class_function)
- [Fold (higher-order function)](https://en.wikipedia.org/wiki/Fold_(higher-order_function))
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Frink (programming language)](https://en.wikipedia.org/wiki/Frink_(programming_language))
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Function type](https://en.wikipedia.org/wiki/Function_type)
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [GNU Octave](https://en.wikipedia.org/wiki/GNU_Octave)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Gosu (programming language)](https://en.wikipedia.org/wiki/Gosu_(programming_language))
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Haxe](https://en.wikipedia.org/wiki/Haxe)
- [Higher-order function](https://en.wikipedia.org/wiki/Higher-order_function)
- [IBM RPG](https://en.wikipedia.org/wiki/IBM_RPG)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Division (mathematics)](https://en.wikipedia.org/wiki/Division_(mathematics))
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Java version history](https://en.wikipedia.org/wiki/Java_version_history)
- [Julia (programming language)](https://en.wikipedia.org/wiki/Julia_(programming_language))
- [Kotlin (programming language)](https://en.wikipedia.org/wiki/Kotlin_(programming_language))
- [LLVM](https://en.wikipedia.org/wiki/LLVM)
- [Lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus)
- [Lambda calculus definition](https://en.wikipedia.org/wiki/Lambda_calculus_definition)
- [Lisp (programming language)](https://en.wikipedia.org/wiki/Lisp_(programming_language))
- [Literal (computer programming)](https://en.wikipedia.org/wiki/Literal_(computer_programming))
- [Logtalk](https://en.wikipedia.org/wiki/Logtalk)
- [Lua (programming language)](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [ML (programming language)](https://en.wikipedia.org/wiki/ML_(programming_language))
- [MUMPS](https://en.wikipedia.org/wiki/MUMPS)
- [Map (higher-order function)](https://en.wikipedia.org/wiki/Map_(higher-order_function))
- [Maple (software)](https://en.wikipedia.org/wiki/Maple_(software))
- [Maps to](https://en.wikipedia.org/wiki/Maps_to)
- [Maxima (software)](https://en.wikipedia.org/wiki/Maxima_(software))
- [Micro Focus](https://en.wikipedia.org/wiki/Micro_Focus)
- [Microsoft Excel](https://en.wikipedia.org/wiki/Microsoft_Excel)
- [Identifier](https://en.wikipedia.org/wiki/Identifier)
- [Name binding](https://en.wikipedia.org/wiki/Name_binding)
- [Naming convention (programming)](https://en.wikipedia.org/wiki/Naming_convention_(programming))
- [Nim (programming language)](https://en.wikipedia.org/wiki/Nim_(programming_language))
- [OCaml](https://en.wikipedia.org/wiki/OCaml)
- [Object Pascal](https://en.wikipedia.org/wiki/Object_Pascal)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [OpenSCAD](https://en.wikipedia.org/wiki/OpenSCAD)
- [Oxygene (programming language)](https://en.wikipedia.org/wiki/Oxygene_(programming_language))
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PL/I](https://en.wikipedia.org/wiki/PL/I)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Racket (programming language)](https://en.wikipedia.org/wiki/Racket_(programming_language))
- [Railo](https://en.wikipedia.org/wiki/Railo)
- [Raku (programming language)](https://en.wikipedia.org/wiki/Raku_(programming_language))
- [Rexx](https://en.wikipedia.org/wiki/Rexx)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scheme (programming language)](https://en.wikipedia.org/wiki/Scheme_(programming_language))
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)
- [Square (algebra)](https://en.wikipedia.org/wiki/Square_(algebra))
- [Standard ML](https://en.wikipedia.org/wiki/Standard_ML)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [TypeScript](https://en.wikipedia.org/wiki/TypeScript)
- [Vala (programming language)](https://en.wikipedia.org/wiki/Vala_(programming_language))
- [Visual Basic (.NET)](https://en.wikipedia.org/wiki/Visual_Basic_(.NET))
- [Visual Prolog](https://en.wikipedia.org/wiki/Visual_Prolog)
- [Wolfram Language](https://en.wikipedia.org/wiki/Wolfram_Language)
- [Zig (programming language)](https://en.wikipedia.org/wiki/Zig_(programming_language))
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Wikipedia:WikiProject Lists](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Lists)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from February 2018](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_February_2018)
- [Category:Incomplete lists from August 2008](https://en.wikipedia.org/wiki/Category:Incomplete_lists_from_August_2008)
- [Portal:Computer programming](https://en.wikipedia.org/wiki/Portal:Computer_programming)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:32:26.564257+00:00_