---
title: While loop
url: https://en.wikipedia.org/wiki/While_loop
language: en
categories: ["Category:All articles needing additional references", "Category:Articles needing additional references from October 2016", "Category:Articles with example Ada code", "Category:Articles with example BASIC code", "Category:Articles with example C++ code", "Category:Articles with example C Sharp code", "Category:Articles with example C code", "Category:Articles with example D code", "Category:Articles with example Fortran code", "Category:Articles with example JavaScript code", "Category:Articles with example Java code", "Category:Articles with example MATLAB/Octave code", "Category:Articles with example PHP code", "Category:Articles with example Pascal code", "Category:Articles with example Perl code", "Category:Articles with example Python (programming language) code", "Category:Articles with example Racket code", "Category:Articles with example Ruby code", "Category:Articles with example Rust code", "Category:Articles with example Smalltalk code", "Category:Articles with example Swift code", "Category:Articles with example Tcl code", "Category:Articles with short description", "Category:Control flow", "Category:Iteration in programming", "Category:Programming language comparisons", "Category:Short description is different from Wikidata"]
references: 0
last_modified: 2024-12-19T13:44:28Z
---

# While loop

## Summary

In most computer programming languages, a while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The while loop can be thought of as a repeating if statement.

## Full Content

In most computer programming languages, a while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The while loop can be thought of as a repeating if statement.

Overview
The while construct consists of a block of code and a condition/expression. The condition/expression is evaluated, and if the condition/expression is true, the code within all of their following in the block is executed. This repeats until the condition/expression becomes false. Because the while loop checks the condition/expression before the block is executed, the control structure is often also known as a pre-test loop. Compare this with the do while loop, which tests the condition/expression after the loop has executed.
For example, in the languages C, Java, C#, Objective-C, and C++, (which use the same syntax in this case), the code fragment

first checks whether x is less than 5, which it is, so then the {loop body} is entered, where the printf function is run and x is incremented by 1. After completing all the statements in the loop body, the condition, (x < 5), is checked again, and the loop is executed again, this process repeating until the variable x has the value 5.
It is possible, and in some cases desirable, for the condition to always evaluate to true, creating an infinite loop. When such a loop is created intentionally, there is usually another control structure (such as a break statement) that controls termination of the loop.
For example:

Demonstrating while loops
These while loops will calculate the factorial of the number 5:

ActionScript 3
Ada
APL
or simply

AutoHotkey
Small Basic
Visual Basic
Bourne (Unix) shell
C, C++
ColdFusion Markup Language (CFML)
Script syntax
Tag syntax
Fortran
Go
Go has no while statement, but it has the function of a for statement when omitting some elements of the for statement.

Java, C#, D
The code for the loop is the same for Java, C# and D:

JavaScript
Lua
MATLAB, Octave
Mathematica
Oberon, Oberon-2, Oberon-07, Component Pascal
Maya Embedded Language
Nim
Non-terminating while loop:

Pascal
Pascal has two forms of the while loop, while and repeat. While repeats one statement (unless enclosed in a begin-end block) as long as the condition is true. The repeat statement repetitively executes a block of one or more statements through an until statement and continues repeating unless the condition is false. The main difference between the two is the while loop may execute zero times if the condition is initially false, the repeat-until loop always executes at least once.

Perl
While loops are frequently used for reading data line by line (as defined by the $/ line separator) from open filehandles:

PHP
PL/I
Python
Non-terminating while loop:

Racket
In Racket, as in other Scheme implementations, a named-let is a popular way to implement loops:

Using a macro system, implementing a while loop is a trivial exercise (commonly used to introduce macros):

However, an imperative programming style is often discouraged in Scheme and Racket.

Ruby
Rust
Smalltalk
Contrary to other languages, in Smalltalk a while loop is not a language construct but defined in the class BlockClosure as a method with one parameter, the body as a closure, using self as the condition.
Smalltalk also has a corresponding whileFalse: method.

Swift
Tcl
VEX
PowerShell
While (language)
While is a simple programming language constructed from assignments, sequential composition, conditionals, and while statements, used in the theoretical analysis of imperative programming language semantics.

See also
Do while loop
For loop
Foreach
Primitive recursive function
General recursive function
LOOP (programming language) – a programming language with the property that the functions it can compute are exactly the primitive recursive functions


== References ==
