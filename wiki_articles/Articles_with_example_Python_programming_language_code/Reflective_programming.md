---
title: Reflective programming
url: https://en.wikipedia.org/wiki/Reflective_programming
language: en
categories: ["Category:All articles needing additional references", "Category:All articles with unsourced statements", "Category:Articles needing additional references from January 2008", "Category:Articles with example BASIC code", "Category:Articles with example C Sharp code", "Category:Articles with example C code", "Category:Articles with example JavaScript code", "Category:Articles with example Java code", "Category:Articles with example Julia code", "Category:Articles with example Lisp (programming language) code", "Category:Articles with example Objective-C code", "Category:Articles with example PHP code", "Category:Articles with example Pascal code", "Category:Articles with example Perl code", "Category:Articles with example Python (programming language) code", "Category:Articles with example R code", "Category:Articles with example Ruby code", "Category:Articles with short description", "Category:Articles with unsourced statements from July 2015", "Category:Programming constructs", "Category:Programming language comparisons", "Category:Short description is different from Wikidata", "Category:Webarchive template wayback links"]
references: 0
last_modified: 2024-12-19T13:43:53Z
---

# Reflective programming

## Summary

In computer science, reflective programming or reflection is the ability of a process to examine, introspect, and modify its own structure and behavior.

## Full Content

In computer science, reflective programming or reflection is the ability of a process to examine, introspect, and modify its own structure and behavior.

Historical background
The earliest computers were programmed in their native assembly languages, which were inherently reflective, as these original architectures could be programmed by defining instructions as data and using self-modifying code. As the bulk of programming moved to higher-level compiled languages such as Algol, Cobol, Fortran, Pascal, and C, this reflective ability largely disappeared until new programming languages with reflection built into their type systems appeared.
Brian Cantwell Smith's 1982 doctoral dissertation introduced the notion of computational reflection in procedural programming languages and the notion of the meta-circular interpreter as a component of 3-Lisp.

Uses
Reflection helps programmers make generic software libraries to display data, process different formats of data, perform serialization and deserialization of data for communication, or do bundling and unbundling of data for containers or bursts of communication.
Effective use of reflection almost always requires a plan: A design framework, encoding description, object library, a map of a database or entity relations.
Reflection makes a language more suited to network-oriented code. For example, it assists languages such as Java to operate well in networks by enabling libraries for serialization, bundling and varying data formats. Languages without reflection such as C are required to use auxiliary compilers for tasks like Abstract Syntax Notation to produce code for serialization and bundling.
Reflection can be used for observing and modifying program execution at runtime. A reflection-oriented program component can monitor the execution of an enclosure of code and can modify itself according to a desired goal of that enclosure. This is typically accomplished by dynamically assigning program code at runtime.
In object-oriented programming languages such as Java, reflection allows inspection of classes, interfaces, fields and methods at runtime without knowing the names of the interfaces, fields, methods at compile time. It also allows instantiation of new objects and invocation of methods.
Reflection is often used as part of software testing, such as for the runtime creation/instantiation of mock objects.
Reflection is also a key strategy for metaprogramming.
In some object-oriented programming languages such as C# and Java, reflection can be used to bypass member accessibility rules. For C#-properties this can be achieved by writing directly onto the (usually invisible) backing field of a non-public property. It is also possible to find non-public methods of classes and types and manually invoke them. This works for project-internal files as well as external libraries such as .NET's assemblies and Java's archives.

Implementation
A language that supports reflection provides a number of features available at runtime that would otherwise be difficult to accomplish in a lower-level language. Some of these features are the abilities to:

Discover and modify source-code constructions (such as code blocks, classes, methods, protocols, etc.) as first-class objects at runtime.
Convert a string matching the symbolic name of a class or function into a reference to or invocation of that class or function.
Evaluate a string as if it were a source-code statement at runtime.
Create a new interpreter for the language's bytecode to give a new meaning or purpose for a programming construct.
These features can be implemented in different ways. In MOO, reflection forms a natural part of everyday programming idiom. When verbs (methods) are called, various variables such as verb (the name of the verb being called) and this (the object on which the verb is called) are populated to give the context of the call. Security is typically managed by accessing the caller stack programmatically: Since callers() is a list of the methods by which the current verb was eventually called, performing tests on callers()[0] (the command invoked by the original user) allows the verb to protect itself against unauthorised use.
Compiled languages rely on their runtime system to provide information about the source code. A compiled Objective-C executable, for example, records the names of all methods in a block of the executable, providing a table to correspond these with the underlying methods (or selectors for these methods) compiled into the program. In a compiled language that supports runtime creation of functions, such as Common Lisp, the runtime environment must include a compiler or an interpreter.
Reflection can be implemented for languages without built-in reflection by using a program transformation system to define automated source-code changes.

Security considerations
Reflection may allow a user to create unexpected control flow paths through an application, potentially bypassing security measures. This may be exploited by attackers. Historical vulnerabilities in Java caused by unsafe reflection allowed code retrieved from potentially untrusted remote machines to break out of the Java sandbox security mechanism. A large scale study of 120 Java vulnerabilities in 2013 concluded that unsafe reflection is the most common vulnerability in Java, though not the most exploited.

Examples
The following code snippets create an instance foo of class Foo and invoke its method PrintHello. For each programming language, normal and reflection-based call sequences are shown.

Common Lisp
The following is an example in Common Lisp using the Common Lisp Object System:

C#
The following is an example in C#:

Delphi, Object Pascal
This Delphi and Object Pascal example assumes that a TFoo class has been declared in a unit called Unit1:

eC
The following is an example in eC:

Go
The following is an example in Go:

Java
The following is an example in Java:

JavaScript
The following is an example in JavaScript:

Julia
The following is an example in Julia:

Objective-C
The following is an example in Objective-C, implying either the OpenStep or Foundation Kit framework is used:

Perl
The following is an example in Perl:

PHP
The following is an example in PHP:

Python
The following is an example in Python:

R
The following is an example in R:

Ruby
The following is an example in Ruby:

Xojo
The following is an example using Xojo:

See also
List of reflective programming languages and platforms
Mirror (programming)
Programming paradigms
Self-hosting (compilers)
Self-modifying code
Type introspection
typeof

References
Citations
Sources
Further reading
Ira R. Forman and Nate Forman, Java Reflection in Action (2005), ISBN 1-932394-18-4
Ira R. Forman and Scott Danforth, Putting Metaclasses to Work (1999), ISBN 0-201-43305-2

External links
Reflection in logic, functional and object-oriented programming: a short comparative study
An Introduction to Reflection-Oriented Programming
Brian Foote's pages on Reflection in Smalltalk
Java Reflection API Tutorial from Oracle
