---
title: Strongly typed identifier
url: https://en.wikipedia.org/wiki/Strongly_typed_identifier
language: en
categories: ["Category:Articles with example C++ code", "Category:Articles with example C Sharp code", "Category:Articles with example D code", "Category:Articles with example Haskell code", "Category:Articles with example JavaScript code", "Category:Articles with example Java code", "Category:Articles with example Julia code", "Category:Articles with example PHP code", "Category:Articles with example Python (programming language) code", "Category:Articles with example Ruby code", "Category:Articles with example Rust code", "Category:Articles with example Scala code", "Category:Articles with example Swift code", "Category:Data types", "Category:Software design patterns"]
references: 0
last_modified: 2024-10-30T13:34:56Z
---

# Strongly typed identifier

## Summary

A strongly typed identifier is user-defined data type which serves as an identifier or key that is strongly typed. This is a solution to the "primitive obsession" code smell as mentioned by Martin Fowler. The data type should preferably be immutable if possible. It is common for implementations to handle equality testing, serialization and model binding.
The strongly typed identifier commonly wraps the data type used as the primary key in the database, such as a string, an integer or universally

## Full Content

A strongly typed identifier is user-defined data type which serves as an identifier or key that is strongly typed. This is a solution to the "primitive obsession" code smell as mentioned by Martin Fowler. The data type should preferably be immutable if possible. It is common for implementations to handle equality testing, serialization and model binding.
The strongly typed identifier commonly wraps the data type used as the primary key in the database, such as a string, an integer or universally unique identifier (UUID).
Web frameworks can often be configured to model bind properties on view models that are strongly typed identifiers. Object–relational mappers can often be configured with value converters to map data between the properties on a model using strongly typed identifier data types and database columns.

Examples
Passing a strongly typed identifier throughout the layers of an example application.

C#
C# have records which provide immutability and equality testing. The record is sealed to prevent inheritance. It overrides the built-in ToString() method.
This example implementation includes a static method which can be used to initialize a new instance with a randomly generated globally unique identifier (GUID).

C++
C++ have structs but not immutability so here the id field is marked as private with a method named value() to get the value.

Crystal
Crystal's standard library provides the record macro for creating records which are immutable structs and lets you create override the built-in to_s method.

D
D have immutable structs.

Dart
Dart have classes with operator overloading.

F#
F# lets you create override the Equals, GetHashCode and ToString methods.

Go
Go have structs which provide equality testing. Go however does not provide immutability.

Groovy
Groovy have record classes which provide immutability and equality testing.

Haskell
Haskell can create user-defined custom data types using the newtype keyword. It provides equality testing using the Eq standard class and printing using the Read and Show standard classes.

Java
Java have records which provide equality testing.
The record is declared using the final modifier keyword to prevent inheritance. It overrides the built-in toString() method.

JavaScript
This JavaScript example implementation provides the toJSON method used by the JSON.stringify() function to serialize the class into a simple string instead of a composite data type.
It calls Object.freeze() to make the instance immutable.
It overrides the built-in toString() method and the valueOf() method.

Julia
Julia have immutable composite data types.

Kotlin
Kotlin have "inline classes".

Nim
Nim have "distinct types".

PHP
This PHP example implementation implements the __toString() magic method.
Furthermore, it implements the JsonSerializable interface which is used by the built-in json_encode function to serialize the class into a simple string instead of a composite data type.
The class is declared using the final modifier keyword to prevent inheritance.
PHP has traits as a way to re-use code.

Python
Python has data classes which provides equality testing and can be made immutable using the frozen parameter. It overrides the __str__ dunder method.
This example implementation includes a static method which can be used to initialize a new instance with a randomly generated universally unique identifier (UUID).

Python also has NewType which can be used to create new data types.

Ruby
Ruby have data classes which provides equality testing and are immutable. It overrides the built-in to_s method.
This example implementation includes a static method which can be used to initialize a new instance with a randomly generated universally unique identifier (UUID).

Rust
In Rust this can be done using a tuple struct containing a single value. This example implementation implements the Debug and the PartialEq traits. The PartialEq trait provides equality testing.

Scala
Scala have case classes which provide immutability and equality testing. The case class is sealed to prevent inheritance.

Swift
Swift have the CustomStringConvertible protocol which can be used to provide its own representation to be used when converting an instance to a string, and the Equatable protocol which provides equality testing.

Zig
Zig have structs with constants but by design does not have operator overloading and method overriding.

See also
Domain-driven design
Type safety
Value object

References
External links
https://wiki.c2.com/?PrimitiveObsession
