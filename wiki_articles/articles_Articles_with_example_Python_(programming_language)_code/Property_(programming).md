# Property (programming)

## Article Metadata

- **Last Updated:** 2024-12-14T19:43:15.061351+00:00
- **Original Article:** [Property (programming)](https://en.wikipedia.org/wiki/Property_(programming))
- **Language:** en
- **Page ID:** 5999262

## Summary

A property, in some object-oriented programming languages, is a special sort of class member, intermediate in functionality between a field (or data member) and a method. The syntax for reading and writing of properties is like for fields, but property reads and writes are (usually) translated to 'getter' and 'setter' method calls. The field-like syntax is easier to read and write than many method calls, yet the interposition of method calls "under the hood" allows for data validation, active up

## Categories

- Category:All Wikipedia articles needing clarification
- Category:All articles needing additional references
- Category:All articles with unsourced statements
- Category:Articles needing additional references from January 2022
- Category:Articles needing additional references from October 2016
- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example D code
- Category:Articles with example JavaScript code
- Category:Articles with example PHP code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Ruby code
- Category:Articles with short description
- Category:Articles with unsourced statements from March 2020
- Category:Object-oriented programming
- Category:Short description is different from Wikidata
- Category:Wikipedia articles needing clarification from October 2016

## Table of Contents

- Support in languages
- Syntax variants
- Example syntax
- See also

## Content

A property, in some object-oriented programming languages, is a special sort of class member, intermediate in functionality between a field (or data member) and a method. The syntax for reading and writing of properties is like for fields, but property reads and writes are (usually) translated to 'getter' and 'setter' method calls. The field-like syntax is easier to read and write than many method calls, yet the interposition of method calls "under the hood" allows for data validation, active updating (e.g., of GUI elements), or implementation of what may be called "read-only fields".

Support in languages
Programming languages that support properties include ActionScript 3, C#, D, Delphi/Free Pascal, eC, F#, Kotlin, JavaScript, Objective-C 2.0, Python, Scala, Swift, Lua, and Visual Basic.
Some object-oriented languages, such as Java and C++, do not support properties, requiring the programmer to define a pair of accessor and mutator methods instead.
Oberon-2 provides an alternative mechanism using object variable visibility flags.
Other languages designed for the Java Virtual Machine, such as Groovy, natively support properties.
While C++ does not have first class properties, they can be emulated with operator overloading.
Also note that some C++ compilers support first class properties as language extensions.

In Microsoft Visual Studio, GCC, and llvm/clang, the __declspec(property) creates properties similar to C#.
Borland C++ and Borland/CodeGear/Embarcadero C++Builder use the __property keyword.
In many object oriented languages properties are implemented as a pair of accessor/mutator methods, but accessed using the same syntax as for public fields. Omitting a method from the pair yields a read-only or an uncommon write-only property.
In some languages with no built-in support for properties, a similar construct can be implemented as a single method that either returns or changes the underlying data, depending on the context of its invocation. Such techniques are used e.g. in Perl. 
Some languages (Ruby, Smalltalk) achieve property-like syntax using normal methods, sometimes with a limited amount of syntactic sugar.

Syntax variants
Some languages follow well-established syntax conventions for formally specifying and utilizing properties and methods.
Among these conventions:

Dot notation
Bracket notation

Dot notation
The following example demonstrates dot notation in JavaScript.

Bracket notation
The following example demonstrates bracket notation in JavaScript.

Example syntax
C#
Recent C# versions also allow "auto-implemented properties" where the backing field for the property is generated by the compiler during compilation. This means that the property must have a setter. However, it can be private.

C++
C++ does not have first class properties, but there exist several ways to emulate properties to a limited degree. Two of which follow:

Using Standard C++
Also see Stack Overflow for a more detailed example.

C++, Microsoft, GCC, LLVM/clang and C++Builder-specific
An example taken from the MSDN documentation page.

D
In D version 2, each property accessor or mutator must be marked with @property:

Delphi/Free Pascal
eC
F#
JavaScript
ActionScript 3.0
Objective-C 2.0
The above example could be used in an arbitrary method like this:

PHP
Python
Properties only work correctly for new-style classes (classes that have object as a superclass), and are only available in Python 2.2 and newer (see the relevant section of the tutorial Unifying types and classes in Python 2.2). Python 2.6 added a new syntax involving decorators for defining properties.

Ruby
Ruby also provides automatic getter/setter synthesizers defined as instance methods of Class.

Visual Basic
Visual Basic (.NET 2003–2010)
Visual Basic (only .NET 2010)
Visual Basic 6
See also
Attribute (computing)
Bound property
Field (computer science)
Indexer (programming)
Method (computer programming)
Mutator method
Uniform access principle


== References ==

## Related Articles

### Internal Links

- [Mutator method](https://en.wikipedia.org/wiki/Mutator_method)
- [ActionScript](https://en.wikipedia.org/wiki/ActionScript)
- [Active updating](https://en.wikipedia.org/wiki/Active_updating)
- [Attribute (computing)](https://en.wikipedia.org/wiki/Attribute_(computing))
- [Borland C++](https://en.wikipedia.org/wiki/Borland_C%2B%2B)
- [Data binding](https://en.wikipedia.org/wiki/Data_binding)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C++Builder](https://en.wikipedia.org/wiki/C%2B%2BBuilder)
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Data validation](https://en.wikipedia.org/wiki/Data_validation)
- [F Sharp (programming language)](https://en.wikipedia.org/wiki/F_Sharp_(programming_language))
- [Field (computer science)](https://en.wikipedia.org/wiki/Field_(computer_science))
- [Free Pascal](https://en.wikipedia.org/wiki/Free_Pascal)
- [GNU Compiler Collection](https://en.wikipedia.org/wiki/GNU_Compiler_Collection)
- [Graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface)
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Indexer (programming)](https://en.wikipedia.org/wiki/Indexer_(programming))
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Java virtual machine](https://en.wikipedia.org/wiki/Java_virtual_machine)
- [Kotlin (programming language)](https://en.wikipedia.org/wiki/Kotlin_(programming_language))
- [LLVM](https://en.wikipedia.org/wiki/LLVM)
- [Lua (programming language)](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Visual Studio](https://en.wikipedia.org/wiki/Visual_Studio)
- [Mutator method](https://en.wikipedia.org/wiki/Mutator_method)
- [Oberon-2](https://en.wikipedia.org/wiki/Oberon-2)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object Pascal](https://en.wikipedia.org/wiki/Object_Pascal)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [Operator overloading](https://en.wikipedia.org/wiki/Operator_overloading)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Inheritance (object-oriented programming)](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar)
- [Uniform access principle](https://en.wikipedia.org/wiki/Uniform_access_principle)
- [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic)
- [Talk:Property (programming)](https://en.wikipedia.org/wiki/Talk:Property_(programming))
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:Please clarify](https://en.wikipedia.org/wiki/Wikipedia:Please_clarify)
- [Wikipedia:Vagueness](https://en.wikipedia.org/wiki/Wikipedia:Vagueness)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Help:Authority control](https://en.wikipedia.org/wiki/Help:Authority_control)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from January 2022](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_January_2022)
- [Category:Articles needing additional references from October 2016](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_October_2016)
- [Category:Articles with unsourced statements from March 2020](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_March_2020)
- [Category:Wikipedia articles needing clarification from October 2016](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_needing_clarification_from_October_2016)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:43:15.061351+00:00_