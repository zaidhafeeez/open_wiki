# Method overriding

## Article Metadata

- **Last Updated:** 2024-12-15T04:35:43.233060+00:00
- **Original Article:** [Method overriding](https://en.wikipedia.org/wiki/Method_overriding)
- **Language:** en
- **Page ID:** 1010628

## Summary

Method overriding, in object-oriented programming, is a language feature that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its superclasses or parent classes. In addition to providing data-driven algorithm-determined parameters across virtual network interfaces, it also allows for a specific type of polymorphism (subtyping). The implementation in the subclass overrides (replaces) the implementation in the superclass by provi

## Categories

- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example Eiffel code
- Category:Articles with example Java code
- Category:Articles with example Python (programming language) code
- Category:Articles with example code
- Category:Articles with short description
- Category:Method (computer programming)
- Category:Short description matches Wikidata
- Category:Webarchive template wayback links

## Table of Contents

- Language-specific examples
- Notes
- See also
- References
- External links

## Content

Method overriding, in object-oriented programming, is a language feature that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its superclasses or parent classes. In addition to providing data-driven algorithm-determined parameters across virtual network interfaces, it also allows for a specific type of polymorphism (subtyping). The implementation in the subclass overrides (replaces) the implementation in the superclass by providing a method that has same name, same parameters or signature, and same return type as the method in the parent class. The version of a method that is executed will be determined by the object that is used to invoke it. If an object of a parent class is used to invoke the method, then the version in the parent class will be executed, but if an object of the subclass is used to invoke the method, then the version in the child class will be executed. This helps in preventing problems associated with differential relay analytics which would otherwise rely on a framework in which method overriding might be obviated. Some languages allow a programmer to prevent a method from being overridden.

Language-specific examples
Ada
Ada provides method overriding by default.
To favor early error detection (e.g. a misspelling),
it is possible to specify when a method
is expected to be actually overriding, or not. That will be checked by the compiler.

C#
C# does support method overriding, but only if explicitly requested using the modifiers override and virtual or abstract.

When overriding one method with another, the signatures of the two methods must be identical (and with same visibility). In C#, class methods, indexers, properties and events can all be overridden.
Non-virtual or static methods cannot be overridden. The overridden base method must be virtual, abstract, or override.
In addition to the modifiers that are used for method overriding, C# allows the hiding of an inherited property or method. This is done using the same signature of a property or method but adding the modifier new in front of it.
In the above example, hiding causes the following:

C++
C++ does not have the keyword super that a subclass can use in Java to invoke the superclass version of a method that it wants to override. Instead, the name of the parent or base class is used followed by the scope resolution operator. For example, the following code presents two classes, the base class Rectangle, and the derived class Box. Box overrides the Rectangle class's Print method, so as also to print its height.

The method Print in class Box, by invoking the parent version of method Print, is also able to output the private variables length and width of the base class. Otherwise, these variables are inaccessible to Box.
The following statements will instantiate objects of type Rectangle and Box, and call their respective Print methods:

In C++11, similar to Java, a method that is declared final in the super class cannot be overridden; also, a method can be declared override to make the compiler check that it overrides a method in the base class.

Delphi
In Delphi, method overriding is done with the directive override, but only if a method was marked with the dynamic or virtual directives.
The inherited reserved word must be called when you want to call super-class behavior

Eiffel
In Eiffel, feature redefinition is analogous to method overriding in C++ and Java. Redefinition is one of three forms of feature adaptation classified as redeclaration. Redeclaration also covers effecting, in which an implementation is provided for a feature which was deferred (abstract) in the parent class, and undefinition, in which a feature that was effective (concrete) in the parent becomes deferred again in the heir class. When a feature is redefined, the feature name is kept by the heir class, but properties of the feature such as its signature, contract (respecting restrictions for preconditions and postconditions), and/or implementation will be different in the heir. If the original feature in the parent class, called the heir feature's precursor, is effective, then the redefined feature in the heir will be effective. If the precursor is deferred, the feature in the heir will be deferred.
The intent to redefine a feature, as message in the example below, must be explicitly declared in the inherit clause of the heir class.

In class ADVICE the feature message is given an implementation that differs from that of its precursor in class THOUGHT.
Consider a class which uses instances for both THOUGHT and ADVICE:

When instantiated, class APPLICATION produces the following output:

Within a redefined feature, access to the feature's precursor can be gained by using the language keyword Precursor. Assume the implementation of {ADVICE}.message is altered as follows:

Invocation of the feature now includes the execution of {THOUGHT}.message, and produces the following output:

Java
In Java, when a subclass contains a method with the same signature (name and parameter types) as a method in its superclass, then the subclass's method overrides that of the superclass. 
For example:

Class Thought represents the superclass and implements a method call message(). The subclass called Advice inherits every method that could be in the Thought class. Class Advice overrides the method message(), replacing its functionality from Thought.

When a subclass contains a method that overrides a method of the superclass, then that (superclass's) overridden method can be explicitly invoked from within a subclass's method by using the keyword super. (It cannot be explicitly invoked from any method belongings to a class that is unrelated to the superclass.) 
The super reference can be 

There are methods that a subclass cannot override. For example, in Java, a method that is declared final in the super class cannot be overridden. Methods that are declared private or static cannot be overridden either because they are implicitly final. It is also impossible for a class that is declared final to become a super class.

Kotlin
In Kotlin we can simply override a function like this (note that the function must be open):

Python
In Python, when a subclass contains a method that overrides a method of the superclass, you can also call the superclass method by calling super(Subclass, self).method instead of self.method. 
Example:

Ruby
In Ruby when a subclass contains a method that overrides a method of the superclass, you can also call the superclass method by calling super in that overridden method.  You can use alias if you would like to keep the overridden method available outside of the overriding method as shown with 'super_message' below.
Example:

Notes
See also
Implementation inheritance
Inheritance semantics
Method overloading
Polymorphism in object-oriented programming
Template method pattern
Virtual inheritance
X-HTTP-Method-Override HTTP Header

References
Deitel, H. M & Deitel, P. J.(2001). Java How to Program (4th ed.). Upper Saddle River, NJ: Prentice Hall.
Lewis, J. & Loftus, W. (2008). Java: Software Solutions (6th ed.). Boston, MA: Pearson Addison Wesley.
Malik, D. S.(2006). C++ Programming: Program Design Including Data Structure. (3rd ed.). Washington, DC: Course Technology.
Flanagan, David.(2002).Java in a Nutshell.Retrieved from http://oreilly.com/catalog/9780596002831/preview#preview
Meyer, Bertrand (2009). Touch of Class: Learning to Program Well with Objects and Contracts. Springer.

External links
Introduction to O.O.P. Concepts and More by Nirosh L.w.C.
Overriding and Hiding Methods by Sun Microsystems

## Related Articles

### Internal Links

- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language))
- [Bertrand Meyer](https://en.wikipedia.org/wiki/Bertrand_Meyer)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C++11](https://en.wikipedia.org/wiki/C%2B%2B11)
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Delphi (software)](https://en.wikipedia.org/wiki/Delphi_(software))
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Eiffel (programming language)](https://en.wikipedia.org/wiki/Eiffel_(programming_language))
- [Function overloading](https://en.wikipedia.org/wiki/Function_overloading)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Inheritance (object-oriented programming)](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
- [Indexer (programming)](https://en.wikipedia.org/wiki/Indexer_(programming))
- [Behavioral subtyping](https://en.wikipedia.org/wiki/Behavioral_subtyping)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Reserved word](https://en.wikipedia.org/wiki/Reserved_word)
- [Kotlin (programming language)](https://en.wikipedia.org/wiki/Kotlin_(programming_language))
- [List of HTTP header fields](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Function overloading](https://en.wikipedia.org/wiki/Function_overloading)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Parameter (computer programming)](https://en.wikipedia.org/wiki/Parameter_(computer_programming))
- [Polymorphism (computer science)](https://en.wikipedia.org/wiki/Polymorphism_(computer_science))
- [Polymorphism (computer science)](https://en.wikipedia.org/wiki/Polymorphism_(computer_science))
- [Postcondition](https://en.wikipedia.org/wiki/Postcondition)
- [Precondition](https://en.wikipedia.org/wiki/Precondition)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Property (programming)](https://en.wikipedia.org/wiki/Property_(programming))
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Scope resolution operator](https://en.wikipedia.org/wiki/Scope_resolution_operator)
- [Statement (computer science)](https://en.wikipedia.org/wiki/Statement_(computer_science))
- [Inheritance (object-oriented programming)](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
- [Subtyping](https://en.wikipedia.org/wiki/Subtyping)
- [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems)
- [Inheritance (object-oriented programming)](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
- [Template method pattern](https://en.wikipedia.org/wiki/Template_method_pattern)
- [Type signature](https://en.wikipedia.org/wiki/Type_signature)
- [Variable (computer science)](https://en.wikipedia.org/wiki/Variable_(computer_science))
- [Virtual inheritance](https://en.wikipedia.org/wiki/Virtual_inheritance)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:35:43.233060+00:00_