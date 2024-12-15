# Callable object

## Article Metadata

- **Last Updated:** 2024-12-15T03:59:24.001589+00:00
- **Original Article:** [Callable object](https://en.wikipedia.org/wiki/Callable_object)
- **Language:** en
- **Page ID:** 48516945

## Summary

A callable object, in computer programming, is any object that can be called like a function.

## Categories

- Category:All articles needing additional references
- Category:All stub articles
- Category:Articles needing additional references from May 2017
- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example PHP code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Swift code
- Category:Computer programming stubs
- Category:Object (computer science)
- Category:Subroutines

## Table of Contents

- In different languages
- References
- External links

## Content

A callable object, in computer programming, is any object that can be called like a function.

In different languages
In C++
pointer to function;
pointer to member function;
functor;
lambda expression.
std::function is a template class that can hold any callable object that matches its signature.
In C++, any class that overloads the function call operator operator() may be called using function-call syntax.

In C#
delegate;
lambda expression.

In PHP
PHP 5.3+ has first-class functions that can be used e.g. as parameter to the usort() function:

It is also possible in PHP 5.3+ to make objects invokable by adding a magic __invoke() method to their class:

In Python
In Python any object with a __call__() method can be called using function-call syntax.

Another example:

In Dart
Callable objects are defined in Dart using the call() method.

In Swift
In Swift, callable objects are defined using callAsFunction.

References
External links
C++ Callable concept

## Related Articles

### Internal Links

- [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [Dart (programming language)](https://en.wikipedia.org/wiki/Dart_(programming_language))
- [Delegate (CLI)](https://en.wikipedia.org/wiki/Delegate_(CLI))
- [First-class function](https://en.wikipedia.org/wiki/First-class_function)
- [Function object](https://en.wikipedia.org/wiki/Function_object)
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Operator overloading](https://en.wikipedia.org/wiki/Operator_overloading)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Function pointer](https://en.wikipedia.org/wiki/Function_pointer)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Generic programming](https://en.wikipedia.org/wiki/Generic_programming)
- [Wikipedia:Stub](https://en.wikipedia.org/wiki/Wikipedia:Stub)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Compu-prog-stub](https://en.wikipedia.org/wiki/Template:Compu-prog-stub)
- [Template talk:Compu-prog-stub](https://en.wikipedia.org/wiki/Template_talk:Compu-prog-stub)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from May 2017](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_May_2017)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:59:24.001589+00:00_