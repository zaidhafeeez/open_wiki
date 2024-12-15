# Named parameter

## Article Metadata

- **Last Updated:** 2024-12-15T04:37:37.916294+00:00
- **Original Article:** [Named parameter](https://en.wikipedia.org/wiki/Named_parameter)
- **Language:** en
- **Page ID:** 495104

## Summary

In computer programming, named parameters, named-parameter arguments, named arguments or keyword arguments refer to a computer language's support for function calls to clearly associate each argument with a given parameter within the function call.

## Categories

- Category:All articles needing additional references
- Category:All articles with dead external links
- Category:All articles with unsourced statements
- Category:Articles needing additional references from August 2014
- Category:Articles with dead external links from December 2023
- Category:Articles with example C code
- Category:Articles with example JavaScript code
- Category:Articles with example PHP code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from July 2021
- Category:Short description matches Wikidata
- Category:Subroutines

## Table of Contents

- Overview
- Use in programming languages
- Order of parameters
- Optional parameters and positional parameters
- Emulating
- See also
- References
- External links

## Content

In computer programming, named parameters, named-parameter arguments, named arguments or keyword arguments refer to a computer language's support for function calls to clearly associate each argument with a given parameter within the function call.

Overview
A function call using named parameters differs from a regular function call in that the arguments are passed by associating each one with a parameter name, instead of providing an ordered list of arguments.
For example, consider this Java or C# method call that doesn't use named parameters:

Using named parameters in Python, the call can be written as:

Using named parameters in PHP, the call can be written as:

The version with positional arguments is more implicit. The versions that name parameters are more explicit. Depending on circumstance, a programmer may find one or the other to be easier to read.

Use in programming languages
Named parameters are supported explicitly in many languages. A non-exhaustive selection of examples includes Ada, C# 4.0+, Ceylon, ColdFusion Markup Language (CFML), Common Lisp, Fortran, IDL, Kotlin, Mathematica, PL/SQL, PowerShell, Python, R, PHP, Ruby, Scala, Smalltalk, Swift and Visual Basic. Objective-C does not have named parameters (even though parts of the method name may look like named parameters).
In C++, you can achieve named parameters by using designated initializers since C++20, like so:

Order of parameters
In languages that do not support named parameters, the order of arguments in a function call is necessarily fixed, since it is the only way that the language can identify which argument is intended to be used for which parameter.
With named parameters, it is usually possible to provide the arguments in any order, since the parameter name attached to each argument identifies its purpose. This reduces the connascence between parts of the program. A few languages support named parameters but still require the arguments to be provided in a specific order.

Optional parameters and positional parameters
Named parameters are often used in conjunction with optional parameters.  Without named parameters, optional parameters can only appear at the end of the parameter list, since there is no other way to determine which values have been omitted.  In languages that support named optional parameters, however, programs may supply any subset of the available parameters, and the names are used to determine which values have been provided.
An added complication arises in languages such as OCaml that support both optional named parameters and partial application. It is impossible in general to distinguish between a function partly applied, and a function to which a subset of parameters have been provided.  OCaml resolves this ambiguity by requiring a positional argument after all optional named-parameter arguments: its presence or absence is used to decide if the function has been fully or partly applied. If all parameters are optional, the implementor may solve the issue by adding a dummy positional parameter of type unit.

Emulating
In languages that do not support named parameters, some of the same benefits can be achieved in other ways.

With documentation
Their value as documentation can be replicated by tooltips in integrated development environments (IDEs) for languages such as Java, or with comments (in C):

Such comments are not checked for correctness and the order of arguments remains important.

With data structures
Removing the argument order restriction, and the ability to leave some values unspecified, can be achieved by passing a record or associative array.
For example, in JavaScript, these two calls are equivalent:

Compare to C99:

Special Support
In Perl and pre-2.0 Ruby a similar convention exists (generally called a hash or options hash), with special support for omitting the delimiters within function calls. As an example, the core module's Net::FTP new function accepts a hash of optional arguments.

With chained method calls
In object-oriented programming languages, it is possible to use method chaining to simulate named parameters, as a form of fluent interface. Each named-parameter argument is replaced with a method on an "arguments" object that modifies and then returns the object. In C++, this is termed the named parameter idiom. The object may then be passed to a function that uses the arguments it contains.
Method chaining is often used in conjunction with the builder pattern as a way to override default values provided by the builder class.

See also
Help:Template for named and positional parameters.
Fluent interface
Tag (programming)

References
External links
https://web.archive.org/web/20070502112455/http://plg.uwaterloo.ca/~rgesteve/cforall/named_pars.html
In C++ this paradigm can be easily implemented: Boost Parameter Library
Named Parameters in various programming languages at Rosetta Code

## Related Articles

### Internal Links

- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language))
- [Associative array](https://en.wikipedia.org/wiki/Associative_array)
- [Builder pattern](https://en.wikipedia.org/wiki/Builder_pattern)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C++20](https://en.wikipedia.org/wiki/C%2B%2B20)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [C Sharp 4.0](https://en.wikipedia.org/wiki/C_Sharp_4.0)
- [Ceylon (programming language)](https://en.wikipedia.org/wiki/Ceylon_(programming_language))
- [ColdFusion Markup Language](https://en.wikipedia.org/wiki/ColdFusion_Markup_Language)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [Connascence](https://en.wikipedia.org/wiki/Connascence)
- [Default argument](https://en.wikipedia.org/wiki/Default_argument)
- [Fluent interface](https://en.wikipedia.org/wiki/Fluent_interface)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [IDL (programming language)](https://en.wikipedia.org/wiki/IDL_(programming_language))
- [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Kotlin (programming language)](https://en.wikipedia.org/wiki/Kotlin_(programming_language))
- [Wolfram Mathematica](https://en.wikipedia.org/wiki/Wolfram_Mathematica)
- [Method chaining](https://en.wikipedia.org/wiki/Method_chaining)
- [OCaml](https://en.wikipedia.org/wiki/OCaml)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PL/SQL](https://en.wikipedia.org/wiki/PL/SQL)
- [Parameter (computer programming)](https://en.wikipedia.org/wiki/Parameter_(computer_programming))
- [Parameter (computer programming)](https://en.wikipedia.org/wiki/Parameter_(computer_programming))
- [Partial application](https://en.wikipedia.org/wiki/Partial_application)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [PowerShell](https://en.wikipedia.org/wiki/PowerShell)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Record (computer science)](https://en.wikipedia.org/wiki/Record_(computer_science))
- [Rosetta Code](https://en.wikipedia.org/wiki/Rosetta_Code)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Tag (programming)](https://en.wikipedia.org/wiki/Tag_(programming))
- [Unit type](https://en.wikipedia.org/wiki/Unit_type)
- [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Link rot](https://en.wikipedia.org/wiki/Wikipedia:Link_rot)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Help:Template](https://en.wikipedia.org/wiki/Help:Template)
- [Category:Articles needing additional references from August 2014](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_August_2014)
- [Category:Articles with dead external links from December 2023](https://en.wikipedia.org/wiki/Category:Articles_with_dead_external_links_from_December_2023)
- [Category:Articles with unsourced statements from July 2021](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_July_2021)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:37:37.916294+00:00_