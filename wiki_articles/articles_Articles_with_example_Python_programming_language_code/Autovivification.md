# Autovivification

## Article Metadata

- **Last Updated:** 2024-12-15T03:25:46.380372+00:00
- **Original Article:** [Autovivification](https://en.wikipedia.org/wiki/Autovivification)
- **Language:** en
- **Page ID:** 1176875

## Summary

In the Perl programming language, autovivification is the automatic creation of new arrays and hashes as required every time an undefined value is dereferenced. Perl autovivification allows a programmer to refer to a structured variable, and arbitrary sub-elements of that structured variable, without expressly declaring the existence of the variable and its complete structure beforehand.
In contrast, other programming languages either:

Require a programmer to expressly declare an entire variabl

## Categories

- Category:All articles lacking reliable references
- Category:All articles with failed verification
- Category:Articles lacking reliable references from August 2024
- Category:Articles with example C++ code
- Category:Articles with example Java code
- Category:Articles with example PHP code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Ruby code
- Category:Articles with failed verification from August 2024
- Category:Evaluation strategy
- Category:Management cybernetics
- Category:Perl

## Table of Contents

- Hashes
- File and directory handles
- Emulation in other programming languages
- See also
- Notes
- References
- External links

## Content

In the Perl programming language, autovivification is the automatic creation of new arrays and hashes as required every time an undefined value is dereferenced. Perl autovivification allows a programmer to refer to a structured variable, and arbitrary sub-elements of that structured variable, without expressly declaring the existence of the variable and its complete structure beforehand.
In contrast, other programming languages either:

Require a programmer to expressly declare an entire variable structure before using or referring to any part of it; or
Require a programmer to declare a part of a variable structure before referring to any part of it; or
Create an assignment to a part of a variable before referring, assigning to or composing an expression that refers to any part of it.
Perl autovivification can be contrasted against languages such as Python, PHP, Ruby, and many of the C style languages, where dereferencing null or undefined values is not generally permitted. It can be compared to the HTML standard's "named access on the window object" which results in corresponding globally scoped variables being automatically accessible to browser-based JavaScript.

Hashes
It is important to remember that autovivification happens when an undefined value is dereferenced.  An assignment is not necessary.  The debugger session below illustrates autovivification of a hash just from examining it:

The debugger session below illustrates autovivification of a hash from assigning to an inner hash:

Hashes several layers deep were created automatically without any declarations. Autovivification can prevent excessive typing. If Perl did not support autovivification, the structure above would have to be created as follows:

File and directory handles
Perl 5.6.1 and newer support autovivification of file and directory handles. Calling open() on an undefined variable will set it to a filehandle. According to perl561delta, "[t]his largely eliminates the need for typeglobs when opening filehandles that must be passed around, as in the following example:

Emulation in other programming languages
C++
The C++ Standard Library's associative containers (std::unordered_map and std::map) use operator[] to get the value associated to a key. If there is nothing associated to this key, it will construct it and value initialize

the value. For simple types like int or float, the value initialization will be zero initialization.

Another example of counting occurrences of strings:

A similar trick can be achieved with the insert() method, which returns an iterator to the element associated to the key, even if it already exists.

Python
Python's built-in dict class can be subclassed to implement autovivificious dictionaries simply by overriding the __missing__() method that was added to the class in Python v2.5. There are other ways of implementing the behavior, but the following is one of the simplest and instances of the class print just like normal Python dictionary objects.

Ruby
Ruby hashes can take a block specifying an object to be returned for non-existing indexes. These can be used to implement autovivificious maps.

Java
Java Map has a method computeIfAbsent that can be used to emulate autovivificous maps.

PHP
PHP arrays are natively autovivificious.

However, this only applies to assignment, and not array access.

JavaScript
ES6 introduces a new Proxy class that can be used to implement autovivification. With other features of JavaScript, this can be reduced to a single line of code:

C#
C#, using indexers and C# 4.0 dynamics,

DynamicObject can be used for implementing different syntaxes also,

See also
Evaluation strategy
Variable
Vivification

Notes
References
External links
perl561delta: File and directory handles can be autovivified
Autovivification in Perl: An In-Depth Tutorial
Autovivification in Ruby - emulate Perl's autovivification
A Use of the Y Combinator in Ruby - Implements autovivification in Ruby with the Y Combinator.
Hash#autonew in the Ruby gem "facets" adds autovivification on hash reads
The Ruby gem "xkeys" facilitates nested structure traversal and autovivifies on array or hash writes

## Related Articles

### Internal Links

- [Array (data structure)](https://en.wikipedia.org/wiki/Array_(data_structure))
- [C++ Standard Library](https://en.wikipedia.org/wiki/C%2B%2B_Standard_Library)
- [Pointer (computer programming)](https://en.wikipedia.org/wiki/Pointer_(computer_programming))
- [ECMAScript version history](https://en.wikipedia.org/wiki/ECMAScript_version_history)
- [Evaluation strategy](https://en.wikipedia.org/wiki/Evaluation_strategy)
- [Hash table](https://en.wikipedia.org/wiki/Hash_table)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Null pointer](https://en.wikipedia.org/wiki/Null_pointer)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Segmentation fault](https://en.wikipedia.org/wiki/Segmentation_fault)
- [Inheritance (object-oriented programming)](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
- [Perl language structure](https://en.wikipedia.org/wiki/Perl_language_structure)
- [Variable (computer science)](https://en.wikipedia.org/wiki/Variable_(computer_science))
- [Vivification](https://en.wikipedia.org/wiki/Vivification)
- [Wikipedia:Reliable sources](https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Category:Articles lacking reliable references from August 2024](https://en.wikipedia.org/wiki/Category:Articles_lacking_reliable_references_from_August_2024)
- [Category:Articles with failed verification from August 2024](https://en.wikipedia.org/wiki/Category:Articles_with_failed_verification_from_August_2024)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:25:46.380372+00:00_