# Callable object

## Metadata
- **Last Updated:** 2024-11-28 07:42:04 UTC
- **Original Article:** [Callable object](https://en.wikipedia.org/wiki/Callable_object)
- **Language:** en
- **Page ID:** 48516945

## Summary
A callable object, in computer programming, is any object that can be called like a function.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 21:03:47 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 967 bytes
- **Word Count:** 152 words
