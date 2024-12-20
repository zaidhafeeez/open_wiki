---
title: Variable shadowing
url: https://en.wikipedia.org/wiki/Variable_shadowing
language: en
categories: ["Category:Articles with example C++ code", "Category:Articles with example JavaScript code", "Category:Articles with example Java code", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Short description is different from Wikidata", "Category:Variable (computer science)"]
references: 0
last_modified: 2024-12-19T14:13:40Z
---

# Variable shadowing

## Summary

In computer programming, variable shadowing occurs when a variable declared within a certain scope (decision block, method, or inner class) has the same name as a variable declared in an outer scope. At the level of identifiers (names, rather than variables), this is known as name masking. This outer variable is said to be shadowed by the inner variable, while the inner identifier is said to mask the outer identifier. This can lead to confusion, as it may be unclear which variable subsequent use

## Full Content

In computer programming, variable shadowing occurs when a variable declared within a certain scope (decision block, method, or inner class) has the same name as a variable declared in an outer scope. At the level of identifiers (names, rather than variables), this is known as name masking. This outer variable is said to be shadowed by the inner variable, while the inner identifier is said to mask the outer identifier. This can lead to confusion, as it may be unclear which variable subsequent uses of the shadowed variable name refer to, which depends on the name resolution rules of the language.
One of the first languages to introduce variable shadowing was ALGOL, which first introduced blocks to establish scopes. It was also permitted by many of the derivative programming languages including C, C++ and Java.  
The C# language breaks this tradition, allowing variable shadowing between an inner and an outer class, and between a method and its containing class, but not between an if-block and its containing method, or between case statements in a switch block.
Some languages allow variable shadowing in more cases than others. For example Kotlin allows an inner variable in a function to shadow a passed argument and a variable in an inner block to shadow another in an outer block, while Java does not allow these. Both languages allow a passed argument to a function/Method to shadow a Class Field.
Some languages disallow variable shadowing completely such as CoffeeScript and V (Vlang).

Example
Lua
The following Lua code provides an example of variable shadowing, in multiple blocks.

Python
The following Python code provides another example of variable shadowing:

As there is no variable declaration but only variable assignment in Python, the keyword nonlocal introduced in Python 3 is used to avoid variable shadowing and assign to non-local variables:

The keyword global is used to avoid variable shadowing and assign to global variables:

Rust
C++
Java
JavaScript
ECMAScript 6 introduction of let and const with block scoping allow variable shadowing.

See also
Overloading
Type polymorphism
Name binding


== References ==
