---
title: Mutator method
url: https://en.wikipedia.org/wiki/Mutator_method
language: en
categories: ["Category:Articles with example BASIC code", "Category:Articles with example C++ code", "Category:Articles with example C Sharp code", "Category:Articles with example Java code", "Category:Articles with example Lisp (programming language) code", "Category:Articles with example PHP code", "Category:Articles with example Pascal code", "Category:Articles with example Perl code", "Category:Articles with example Python (programming language) code", "Category:Articles with example Racket code", "Category:Articles with example Ruby code", "Category:Articles with example Smalltalk code", "Category:Articles with short description", "Category:Method (computer programming)", "Category:Short description is different from Wikidata"]
references: 0
last_modified: 2024-12-19T13:46:33Z
---

# Mutator method

## Summary

In computer science, a mutator method is a method used to control changes to a variable. They are also widely known as setter methods. Often a setter is accompanied by a getter, which returns the value of the private member variable. They are also known collectively as accessors.
The mutator method is most often used in object-oriented programming, in keeping with the principle of encapsulation. According to this principle, member variables of a class are made private to hide and protect them fr

## Full Content

In computer science, a mutator method is a method used to control changes to a variable. They are also widely known as setter methods. Often a setter is accompanied by a getter, which returns the value of the private member variable. They are also known collectively as accessors.
The mutator method is most often used in object-oriented programming, in keeping with the principle of encapsulation. According to this principle, member variables of a class are made private to hide and protect them from other code, and can only be modified by a public member function (the mutator method), which takes the desired new value as a parameter, optionally validates it, and modifies the private member variable. Mutator methods can be compared to assignment operator overloading but they typically appear at different levels of the object hierarchy.
Mutator methods may also be used in non-object-oriented environments. In this case, a reference to the variable to be modified is passed to the mutator, along with the new value. In this scenario, the compiler cannot restrict code from bypassing the mutator method and changing the variable directly. The responsibility falls to the developers to ensure the variable is only modified through the mutator method and not modified directly.
In programming languages that support them, properties offer a convenient alternative without giving up the utility of encapsulation.
In the examples below, a fully implemented mutator method can also validate the input data or take further action such as triggering an event.

Implications
The alternative to defining mutator and accessor methods, or property blocks, is to give the instance variable some visibility other than private and access it directly from outside the objects. Much finer control of access rights can be defined using mutators and accessors. For example, a parameter may be made read-only simply by defining an accessor but not a mutator. The visibility of the two methods may be different; it is often useful for the accessor to be public while the mutator remains protected, package-private or internal.
The block where the mutator is defined provides an opportunity for validation or preprocessing of incoming data. If all external access is guaranteed to come through the mutator, then these steps cannot be bypassed. For example, if a date is represented by separate private year, month and day variables, then incoming dates can be split by the setDate mutator while for consistency the same private instance variables are accessed by setYear and setMonth. In all cases month values outside of 1 - 12 can be rejected by the same code.
Accessors conversely allow for synthesis of useful data representations from internal variables while keeping their structure encapsulated and hidden from outside modules. A monetary getAmount accessor may build a string from a numeric variable with the number of decimal places defined by a hidden currency parameter.
Modern programming languages often offer the ability to generate the boilerplate for mutators and accessors in a single line—as for example C#'s public string Name { get; set; } and Ruby's attr_accessor :name. In these cases, no code blocks are created for validation, preprocessing or synthesis. These simplified accessors still retain the advantage of encapsulation over simple public instance variables, but it is common that, as system designs progress, the software is maintained and requirements change, the demands on the data become more sophisticated. Many automatic mutators and accessors eventually get replaced by separate blocks of code. The benefit of automatically creating them in the early days of the implementation is that the public interface of the class remains identical whether or not greater sophistication is added, requiring no extensive refactoring if it is. 
Manipulation of parameters that have mutators and accessors from inside the class where they are defined often requires some additional thought. In the early days of an implementation, when there is little or no additional code in these blocks, it makes no difference if the private instance variable is accessed directly or not. As validation, cross-validation, data integrity checks, preprocessing or other sophistication is added, subtle bugs may appear where some internal access makes use of the newer code while in other places it is bypassed.
Accessor functions can be less efficient than directly fetching or storing data fields due to the extra steps involved, however such functions are often inlined which eliminates the overhead of a function call.

Examples
Assembly
C
In file student.h:

In file student.c:

In file main.c:

In file Makefile:

C++
In file Student.h:

In file Student.cpp:

C#
This example illustrates the C# idea of properties, which are a special type of class member. Unlike Java, no explicit methods are defined; a public 'property' contains the logic to handle the actions. Note use of the built-in (undeclared) variable value. 

In later C# versions (.NET Framework 3.5 and above), this example may be abbreviated as follows, without declaring the private variable name.

Using the abbreviated syntax means that the underlying variable is no longer available from inside the class. As a result, the set portion of the property must be present for assignment. Access can be restricted with a set-specific access modifier.

Common Lisp
In Common Lisp Object System, slot specifications within class definitions may specify any of the :reader, :writer and :accessor options (even multiple times) to define reader methods, setter methods and accessor methods (a reader method and the respective setf method). Slots are always directly accessible through their names with the use of with-slots and slot-value, and the slot accessor options define specialized methods that use slot-value.
CLOS itself has no notion of properties, although the MetaObject Protocol extension specifies means to access a slot's reader and writer function names, including the ones generated with the :accessor option.
The following example shows a definition of a student class using these slot options and direct slot access:

D
D supports a getter and setter function syntax. In version 2 of the language getter and setter class/struct methods should have the @property attribute.

A Student instance can be used like this:

Delphi
This is a simple class in Delphi language which illustrates the concept of public property for accessing a private field.

Java
In this example of a simple class representing a student with only the name stored, one can see the variable name is private, i.e. only visible from the Student class, and the "setter" and "getter" are public, namely the "getName()" and "setName(name)" methods.

JavaScript
In this example constructor-function Student is used to create objects representing a student with only the name stored.

Or (using a deprecated way to define accessors in Web browsers):

Or (using prototypes for inheritance and ES6 accessor syntax):

Or (without using prototypes):

Or (using defineProperty):

ActionScript 3.0
Objective-C
Using traditional Objective-C 1.0 syntax, with manual reference counting as the one working on GNUstep on Ubuntu 12.04:

Using newer Objective-C 2.0 syntax as used in Mac OS X 10.6, iOS 4 and Xcode 3.2, generating the same code as described above:

And starting with OS X 10.8 and iOS 6, while using Xcode 4.4 and up, syntax can be even simplified:

Perl
Or, using Class::Accessor

Or, using the Moose Object System:

PHP
PHP defines the "magic methods" __getand__set for properties of objects.
In this example of a simple class representing a student with only the name stored, one can see the variable name is private, i.e. only visible from the Student class, and the "setter" and "getter" is public, namely the getName() and setName('name') methods.

Python
This example uses a Python class with one variable, a getter, and a setter.

Racket
In Racket, the object system is a way to organize code that comes in addition to modules and units.  As in the rest of the language, the object system has first-class values and lexical scope is used to control access to objects and methods.

Struct definitions are an alternative way to define new types of values, with mutators being present when explicitly required:

Ruby
In Ruby, individual accessor and mutator methods may be defined, or the metaprogramming constructs attr_reader or attr_accessor may be used both to declare a private variable in a class and to provide either read-only or read-write public access to it respectively.
Defining individual accessor and mutator methods creates space for pre-processing or validation of the data

Read-only simple public access to implied @name variable

Read-write simple public access to implied @name variable

Rust
Smalltalk
Swift
Visual Basic .NET
This example illustrates the VB.NET idea of properties, which are used in classes. Similar to C#, there is an explicit use of the Get and Set methods. 

In VB.NET 2010, Auto Implemented properties can be utilized to create a property without having to use the Get and Set syntax. Note that a hidden variable is created by the compiler, called _name, to correspond with the Property name. Using another variable within the class named _name would result in an error. Privileged access to the underlying variable is available from within the class.

See also
Property (programming)
Indexer (programming)
Immutable object


== References ==
