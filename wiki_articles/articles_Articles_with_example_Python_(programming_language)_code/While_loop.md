# While loop

## Article Metadata

- **Last Updated:** 2024-12-14T19:47:14.734062+00:00
- **Original Article:** [While loop](https://en.wikipedia.org/wiki/While_loop)
- **Language:** en
- **Page ID:** 468915

## Summary

In most computer programming languages, a while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The while loop can be thought of as a repeating if statement.

## Categories

- Category:All articles needing additional references
- Category:Articles needing additional references from October 2016
- Category:Articles with example Ada code
- Category:Articles with example BASIC code
- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example C code
- Category:Articles with example D code
- Category:Articles with example Fortran code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example MATLAB/Octave code
- Category:Articles with example PHP code
- Category:Articles with example Pascal code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Racket code
- Category:Articles with example Ruby code
- Category:Articles with example Rust code
- Category:Articles with example Smalltalk code
- Category:Articles with example Swift code
- Category:Articles with example Tcl code
- Category:Articles with short description
- Category:Control flow
- Category:Iteration in programming
- Category:Programming language comparisons
- Category:Short description is different from Wikidata

## Table of Contents

- Overview
- Demonstrating while loops
- See also

## Content

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

## Related Articles

### Internal Links

- [APL (programming language)](https://en.wikipedia.org/wiki/APL_(programming_language))
- [ActionScript](https://en.wikipedia.org/wiki/ActionScript)
- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language))
- [AutoHotkey](https://en.wikipedia.org/wiki/AutoHotkey)
- [Boolean data type](https://en.wikipedia.org/wiki/Boolean_data_type)
- [Bourne shell](https://en.wikipedia.org/wiki/Bourne_shell)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Closure (computer programming)](https://en.wikipedia.org/wiki/Closure_(computer_programming))
- [ColdFusion Markup Language](https://en.wikipedia.org/wiki/ColdFusion_Markup_Language)
- [Component Pascal](https://en.wikipedia.org/wiki/Component_Pascal)
- [Conditional (computer programming)](https://en.wikipedia.org/wiki/Conditional_(computer_programming))
- [Control flow](https://en.wikipedia.org/wiki/Control_flow)
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Do while loop](https://en.wikipedia.org/wiki/Do_while_loop)
- [Factorial](https://en.wikipedia.org/wiki/Factorial)
- [False (logic)](https://en.wikipedia.org/wiki/False_(logic))
- [For loop](https://en.wikipedia.org/wiki/For_loop)
- [Foreach loop](https://en.wikipedia.org/wiki/Foreach_loop)
- [Foreach loop](https://en.wikipedia.org/wiki/Foreach_loop)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [GNU Octave](https://en.wikipedia.org/wiki/GNU_Octave)
- [General recursive function](https://en.wikipedia.org/wiki/General_recursive_function)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Infinite loop](https://en.wikipedia.org/wiki/Infinite_loop)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [LOOP (programming language)](https://en.wikipedia.org/wiki/LOOP_(programming_language))
- [Language construct](https://en.wikipedia.org/wiki/Language_construct)
- [Lua (programming language)](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [Maya Embedded Language](https://en.wikipedia.org/wiki/Maya_Embedded_Language)
- [Microsoft Small Basic](https://en.wikipedia.org/wiki/Microsoft_Small_Basic)
- [Nim (programming language)](https://en.wikipedia.org/wiki/Nim_(programming_language))
- [Oberon (programming language)](https://en.wikipedia.org/wiki/Oberon_(programming_language))
- [Oberon-2](https://en.wikipedia.org/wiki/Oberon-2)
- [Oberon (programming language)](https://en.wikipedia.org/wiki/Oberon_(programming_language))
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PL/I](https://en.wikipedia.org/wiki/PL/I)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Polyglot (computing)](https://en.wikipedia.org/wiki/Polyglot_(computing))
- [PowerShell](https://en.wikipedia.org/wiki/PowerShell)
- [Primitive recursive function](https://en.wikipedia.org/wiki/Primitive_recursive_function)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Racket (programming language)](https://en.wikipedia.org/wiki/Racket_(programming_language))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [Scheme (programming language)](https://en.wikipedia.org/wiki/Scheme_(programming_language))
- [Semantics (computer science)](https://en.wikipedia.org/wiki/Semantics_(computer_science))
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Statement (computer science)](https://en.wikipedia.org/wiki/Statement_(computer_science))
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Tag (programming)](https://en.wikipedia.org/wiki/Tag_(programming))
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [VEX prefix](https://en.wikipedia.org/wiki/VEX_prefix)
- [Variable (computer science)](https://en.wikipedia.org/wiki/Variable_(computer_science))
- [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic)
- [Wolfram Language](https://en.wikipedia.org/wiki/Wolfram_Language)
- [Wolfram Mathematica](https://en.wikipedia.org/wiki/Wolfram_Mathematica)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Loop constructs](https://en.wikipedia.org/wiki/Template:Loop_constructs)
- [Template talk:Loop constructs](https://en.wikipedia.org/wiki/Template_talk:Loop_constructs)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from October 2016](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_October_2016)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:47:14.734062+00:00_