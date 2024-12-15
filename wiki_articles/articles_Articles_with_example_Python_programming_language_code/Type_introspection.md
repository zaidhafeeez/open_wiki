# Type introspection

## Metadata
- **Last Updated:** 2024-12-10 19:54:29 UTC
- **Original Article:** [Type introspection](https://en.wikipedia.org/wiki/Type_introspection)
- **Language:** en
- **Page ID:** 390415

## Summary
In computing, type introspection is the ability of a program to examine the type or properties of an object
at runtime.
Some programming languages possess this capability.
Introspection should not be confused with reflection, which goes a step further and is the ability for a program to manipulate the metadata, properties, and functions of an object at runtime.  Some programming languages also possess that capability  (e.g.,
Java,
Python,
Julia,
and
Go).

## Categories
This article belongs to the following categories:

- Category:All articles with style issues
- Category:All articles with too many examples
- Category:Articles with example C++ code
- Category:Articles with example Java code
- Category:Articles with example Objective-C code
- Category:Articles with example PHP code
- Category:Articles with example Pascal code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Ruby code
- Category:Articles with multiple maintenance issues
- Category:Articles with too many examples from December 2011
- Category:Object-oriented programming
- Category:Programming language comparisons
- Category:Wikipedia articles with style issues from December 2011

## Table of Contents

- Examples
- See also
- References
- External links

## Content

In computing, type introspection is the ability of a program to examine the type or properties of an object
at runtime.
Some programming languages possess this capability.
Introspection should not be confused with reflection, which goes a step further and is the ability for a program to manipulate the metadata, properties, and functions of an object at runtime.  Some programming languages also possess that capability  (e.g.,
Java,
Python,
Julia,
and
Go).

Examples
Objective-C
In Objective-C, for example, both the generic Object and NSObject (in Cocoa/OpenStep) provide the method isMemberOfClass: which returns true if the argument to the method is an instance of the specified class. The method isKindOfClass: analogously returns true if the argument inherits from the specified class.
For example, say we have an Apple and an Orange class inheriting from Fruit.
Now, in the eat method we can write

Now, when eat is called with a generic object (an id), the function will behave correctly depending on the type of the generic object.

C++
C++ supports type introspection via the run-time type information (RTTI) typeid and dynamic_cast keywords.
The dynamic_cast expression can be used to determine whether a particular object is of a particular derived class. For instance:

The typeid operator retrieves a std::type_info object describing the most derived type of an object:

Object Pascal
Type introspection has been a part of Object Pascal since the original release of Delphi, which uses RTTI heavily for visual form design. In Object Pascal, all classes descend from the base TObject class, which implements basic RTTI functionality.  Every class's name can be referenced in code for RTTI purposes; the class name identifier is implemented as a pointer to the class's metadata, which can be declared and used as a variable of type TClass.
The language includes an is operator, to determine if an object is or descends from a given class, an as operator, providing a type-checked typecast, and several TObject methods. Deeper introspection (enumerating fields and methods) is traditionally only supported for objects declared in the $M+ (a pragma) state, typically TPersistent, and only for symbols defined in the published section. Delphi 2010 increased this to nearly all symbols.

Java
The simplest example of type introspection in Java is the instanceof operator.  The instanceof operator determines whether a particular object belongs to a particular class (or a subclass of that class, or a class that implements that interface).  For instance:

The java.lang.Class class is the basis of more advanced introspection.
For instance, if it is desirable to determine the actual class of an object (rather than whether it is a member of a particular class), Object.getClass() and Class.getName() can be used:

PHP
In PHP introspection can be done using instanceof operator. For instance:

Perl
Introspection can be achieved using the ref and isa functions in Perl.
We can introspect the following classes and their corresponding instances:

using:

Meta-Object Protocol
Much more powerful introspection in Perl can be achieved using the Moose object system and the Class::MOP meta-object protocol; for example, you can check if a given object does a role X:

This is how you can list fully qualified names of all of the methods that can be invoked on the object, together with the classes in which they were defined:

Python
The most common method of introspection in Python is using the dir function to detail the attributes of an object. For example:

Also, the built-in functions type and isinstance can be used to determine what an object is while hasattr can determine what an object does. For example:

Ruby
Type introspection is a core feature of Ruby. In Ruby, the Object class (ancestor of every class) provides Object#instance_of? and Object#kind_of? methods for checking the instance's class. The latter returns true when the particular instance the message was sent to is an instance of a descendant of the class in question. For example, consider the following example code (you can immediately try this with the Interactive Ruby Shell):

In the example above, the Class class is used as any other class in Ruby. Two classes are created, A and B, the former is being a superclass of the latter, then one instance of each class is checked. The last expression gives true because A is a superclass of the class of b.
Further, you can directly ask for the class of any object, and "compare" them (code below assumes having executed the code above):

ActionScript
In ActionScript (as3), the function flash.utils.getQualifiedClassName can be used to retrieve the class/type name of an arbitrary object.

Alternatively, the operator is can be used to determine if an object is of a specific type:

This second function can be used to test class inheritance parents as well:

Meta-type introspection
Like Perl, ActionScript can go further than getting the class name, but all the metadata, functions and other elements that make up an object using the flash.utils.describeType function; this is used when implementing reflection in ActionScript.

See also
Reification (computer science)
typeof

References
External links
Introspection on Rosetta Code

## Archive Info
- **Archived on:** 2024-12-15 20:38:53 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 5270 bytes
- **Word Count:** 835 words
