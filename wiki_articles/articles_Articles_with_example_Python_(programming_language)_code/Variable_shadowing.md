# Variable shadowing

## Article Metadata

- **Last Updated:** 2024-12-14T19:46:44.448890+00:00
- **Original Article:** [Variable shadowing](https://en.wikipedia.org/wiki/Variable_shadowing)
- **Language:** en
- **Page ID:** 19792997

## Summary

In computer programming, variable shadowing occurs when a variable declared within a certain scope (decision block, method, or inner class) has the same name as a variable declared in an outer scope. At the level of identifiers (names, rather than variables), this is known as name masking. This outer variable is said to be shadowed by the inner variable, while the inner identifier is said to mask the outer identifier. This can lead to confusion, as it may be unclear which variable subsequent use

## Categories

- Category:Articles with example C++ code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Short description is different from Wikidata
- Category:Variable (computer science)

## Table of Contents

- Example
- See also

## Content

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

## Related Articles

### Internal Links

- [ALGOL](https://en.wikipedia.org/wiki/ALGOL)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [CoffeeScript](https://en.wikipedia.org/wiki/CoffeeScript)
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [ECMAScript version history](https://en.wikipedia.org/wiki/ECMAScript_version_history)
- [Function overloading](https://en.wikipedia.org/wiki/Function_overloading)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Identifier (computer languages)](https://en.wikipedia.org/wiki/Identifier_(computer_languages))
- [Inner class](https://en.wikipedia.org/wiki/Inner_class)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Kotlin (programming language)](https://en.wikipedia.org/wiki/Kotlin_(programming_language))
- [Lua (programming language)](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [Name binding](https://en.wikipedia.org/wiki/Name_binding)
- [Name resolution (programming languages)](https://en.wikipedia.org/wiki/Name_resolution_(programming_languages))
- [Name resolution (programming languages)](https://en.wikipedia.org/wiki/Name_resolution_(programming_languages))
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Scope (computer science)](https://en.wikipedia.org/wiki/Scope_(computer_science))
- [Switch statement](https://en.wikipedia.org/wiki/Switch_statement)
- [Polymorphism (computer science)](https://en.wikipedia.org/wiki/Polymorphism_(computer_science))
- [V (programming language)](https://en.wikipedia.org/wiki/V_(programming_language))

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:46:44.448890+00:00_