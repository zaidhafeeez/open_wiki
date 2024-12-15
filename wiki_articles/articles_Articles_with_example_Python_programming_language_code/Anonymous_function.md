# Anonymous function

## Metadata
- **Last Updated:** 2024-12-10 08:12:38 UTC
- **Original Article:** [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- **Language:** en
- **Page ID:** 7018181

## Summary
In computer programming, an anonymous function (function literal, expression or block) is a function definition that is not bound to an identifier. Anonymous functions are often arguments being passed to higher-order functions or used for constructing the result of a higher-order function that needs to return a function.
If the function is only used once, or a limited number of times, an anonymous function may be syntactically lighter than using a named function. Anonymous functions are ubiquitous in functional programming languages and other languages with first-class functions, where they fulfil the same role for the function type as literals do for other data types.
Anonymous functions originate in the work of Alonzo Church in his invention of the lambda calculus, in which all functions are anonymous, in 1936, before electronic computers. In several programming languages, anonymous functions are introduced using the keyword lambda, and anonymous functions are often referred to as lambdas or lambda abstractions. Anonymous functions have been a feature of programming languages since Lisp in 1958, and a growing number of modern programming languages support anonymous functions.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 21:03:25 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 8868 bytes
- **Word Count:** 1348 words
