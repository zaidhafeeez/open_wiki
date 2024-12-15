# Variadic function

## Metadata
- **Last Updated:** 2024-12-03 06:56:34 UTC
- **Original Article:** [Variadic function](https://en.wikipedia.org/wiki/Variadic_function)
- **Language:** en
- **Page ID:** 1576209

## Summary
In mathematics and in computer programming, a variadic function is a function of indefinite arity, i.e., one which accepts a variable number of arguments. Support for variadic functions differs widely among programming languages.
The term variadic is a neologism, dating back to 1936–1937.  The term was not widely used until the 1970s.

## Categories
This article belongs to the following categories:

- Category:All articles with unsourced statements
- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example C code
- Category:Articles with example Haskell code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example Pascal code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Ruby code
- Category:Articles with example Rust code
- Category:Articles with example Swift code
- Category:Articles with example Tcl code
- Category:Articles with short description
- Category:Articles with unsourced statements from February 2018
- Category:Programming language comparisons
- Category:Short description is different from Wikidata
- Category:Subroutines
- Category:Wikipedia articles needing clarification from May 2018

## Table of Contents

- Overview
- Examples
- See also
- Notes
- References
- External links

## Content

In mathematics and in computer programming, a variadic function is a function of indefinite arity, i.e., one which accepts a variable number of arguments. Support for variadic functions differs widely among programming languages.
The term variadic is a neologism, dating back to 1936–1937.  The term was not widely used until the 1970s.

Overview
There are many mathematical and logical operations that come across naturally as variadic functions. For instance, the summing of numbers or the concatenation of strings or other sequences are operations that can be thought of as applicable to any number of operands (even though formally in these cases the associative property is applied).
Another operation that has been implemented as a variadic function in many languages is output formatting. The C function printf and the Common Lisp function format are two such examples. Both take one argument that specifies the formatting of the output, and any number of arguments that provide the values to be formatted.
Variadic functions can expose type-safety problems in some languages. For instance, C's printf, if used incautiously, can give rise to a class of security holes known as format string attacks. The attack is possible because the language support for variadic functions is not type-safe: it permits the function to attempt to pop more arguments off the stack than were placed there, corrupting the stack and leading to unexpected behavior. As a consequence of this, the CERT Coordination Center considers variadic functions in C to be a high-severity security risk.
In functional programming languages, variadics can be considered complementary to the apply function, which takes a function and a list/sequence/array as arguments, and calls the function with the arguments supplied in that list, thus passing a variable number of arguments to the function. In the functional language Haskell, variadic functions can be implemented by returning a value of a type class T; if instances of T are a final return value r and a function (T t) => x -> t, this allows for any number of additional arguments x.
A related subject in term rewriting research is called hedges, or hedge variables. Unlike variadics, which are functions with arguments, hedges are sequences of arguments themselves. They also can have constraints ('take no more than 4 arguments', for example) to the point where they are not variable-length (such as 'take exactly 4 arguments') - thus calling them variadics can be misleading. However they are referring to the same phenomenon, and sometimes the phrasing is mixed, resulting in names such as variadic variable (synonymous to hedge). Note the double meaning of the word variable and the difference between arguments and variables in functional programming and term rewriting. For example, a term (function) can have three variables, one of them a hedge, thus allowing the term to take three or more arguments (or two or more if the hedge is allowed to be empty).

Examples
In C
To portably implement variadic functions in the C language, the standard stdarg.h header file is used. The older varargs.h header has been deprecated in favor of stdarg.h. In C++, the header file cstdarg is used.

This will compute the average of an arbitrary number of arguments. Note that the function does not know the number of arguments or their types. The above function expects that the types will be int, and that the number of arguments is passed in the first argument (this is a frequent usage but by no means enforced by the language or compiler). In some other cases, for example printf, the number and types of arguments are figured out from a format string. In both cases, this depends on the programmer to supply the correct information. (Alternatively, a sentinel value like NULL or nullptr may be used to indicate the end of the parameter list.) If fewer arguments are passed in than the function believes, or the types of arguments are incorrect, this could cause it to read into invalid areas of memory and can lead to vulnerabilities like the format string attack. Depending on the system, even using NULL as a sentinel may encounter such problems; nullptr or a dedicated null pointer of the correct target type may be used to avoid them. 
stdarg.h declares a type, va_list, and defines four macros: va_start, va_arg, va_copy, and va_end. Each invocation of va_start and va_copy must be matched by a corresponding invocation of va_end. When working with variable arguments, a function normally declares a variable of type va_list (ap in the example) that will be manipulated by the macros.

va_start takes two arguments, a va_list object and a reference to the function's last parameter (the one before the ellipsis; the macro uses this to get its bearings). In C23, the second argument will no longer be required and variadic functions will no longer need a named parameter before the ellipsis. It initialises the va_list object for use by va_arg or va_copy. The compiler will normally issue a warning if the reference is incorrect (e.g. a reference to a different parameter than the last one, or a reference to a wholly different object), but will not prevent compilation from completing normally.
va_arg takes two arguments, a va_list object (previously initialised) and a type descriptor. It expands to the next variable argument, and has the specified type. Successive invocations of va_arg allow processing each of the variable arguments in turn. Unspecified behavior occurs if the type is incorrect or there is no next variable argument.
va_end takes one argument, a va_list object. It serves to clean up. If one wanted to, for instance, scan the variable arguments more than once, the programmer would re-initialise your va_list object by invoking va_end and then va_start again on it.
va_copy takes two arguments, both of them va_list objects. It clones the second (which must have been initialised) into the first. Going back to the "scan the variable arguments more than once" example, this could be achieved by invoking va_start on a first va_list, then using va_copy to clone it into a second va_list. After scanning the variable arguments a first time with va_arg and the first va_list (disposing of it with va_end), the programmer could scan the variable arguments a second time with va_arg and the second va_list. va_end needs to also be called on the cloned va_list before the containing function returns.

In C#
C# describes variadic functions using the params keyword. A type must be provided for the arguments, although object[] can be used as a catch-all. At the calling site, you can either list the arguments one by one, or hand over a pre-existing array having the required element type. Using the variadic form is Syntactic sugar for the latter.

In C++
The basic variadic facility in C++ is largely identical to that in C. The only difference is in the syntax, where the comma before the ellipsis can be omitted. C++ allows variadic functions without named parameters but provides no way to access those arguments since va_start requires the name of the last fixed argument of the function. 

Variadic templates (parameter pack) can also be used in C++ with language built-in fold expressions.

The CERT Coding Standards for C++ strongly prefers the use of variadic templates (parameter pack) in C++ over the C-style variadic function due to a lower risk of misuse.

In Go
Variadic functions in Go can be called with any number of trailing arguments. fmt.Println is a common variadic function; it uses an empty interface as a catch-all type.

Output:

The sum of [1 2] is 3 
The sum of [1 2 3] is 6 
The sum of [1 2 3 4] is 10

In Java
As with C#, the Object type in Java is available as a catch-all.

In JavaScript
JavaScript does not care about types of variadic arguments.

It's also possible to create a variadic function using the arguments object, although it is only usable with functions created with the function keyword.

In Lua
Lua functions may pass varargs to other functions the same way as other values using the return keyword. tables can be passed into variadic functions by using, in Lua version 5.2 or higher table.unpack, or Lua 5.1 or lower unpack. Varargs can be used as a table by constructing a table with the vararg as a value.

In Pascal
Pascal is standardized by ISO standards 7185 (“Standard Pascal”) and 10206 (“Extended Pascal”).
Neither standardized form of Pascal supports variadic routines, except for certain built-in routines (read/readLn and write/writeLn, and additionally in EP readStr/writeStr).
Nonetheless, dialects of Pascal implement mechanisms resembling variadic routines.
Delphi defines an array of const data type that may be associated with the last formal parameter.
Within the routine definition the array of const is an array of TVarRec, an array of variant records.
The VType member of the aforementioned record data type allows inspection of the argument’s data type and subsequent appropriate handling.
The Free Pascal Compiler supports Delphi’s variadic routines, too.
This implementation, however, technically requires a single argument, that is an array.
Pascal imposes the restriction that arrays need to be homogenous.
This requirement is circumvented by utilizing a variant record.
The GNU Pascal defines a real variadic formal parameter specification using an ellipsis (...), but as of 2022 no portable mechanism to use such has been defined.
Both GNU Pascal and FreePascal allow externally declared functions to use a variadic formal parameter specification using an ellipsis (...).

In PHP
PHP does not care about types of variadic arguments unless the argument is typed.

And typed variadic arguments:

In Python
Python does not care about types of variadic arguments.

Keyword arguments can be stored in a dictionary, e.g. def bar(*args, **kwargs).

In Raku
In Raku, the type of parameters that create variadic functions are known as slurpy array parameters and they're classified into three groups:

Flattened slurpy
These parameters are declared with a single asterisk (*) and they flatten arguments by dissolving one or more layers of elements that can be iterated over (i.e, Iterables).

Unflattened slurpy
These parameters are declared with two asterisks (**) and they do not flatten any iterable arguments within the list, but keep the arguments more or less as-is:

Contextual slurpy
These parameters are declared with a plus (+) sign and they apply the "single argument rule", which decides how to handle the slurpy argument based upon context. Simply put, if only a single argument is passed and that argument is iterable, that argument is used to fill the slurpy parameter array. In any other case, +@ works like **@ (i.e., unflattened slurpy).

In Ruby
Ruby does not care about types of variadic arguments.

In Rust
Rust does not support variadic arguments in functions. Instead, it uses macros.

Rust is able to interact with C's variadic system via a c_variadic feature switch. As with other C interfaces, the system is considered unsafe to Rust.

In Scala
In Swift
Swift cares about the type of variadic arguments, but the catch-all Any type is available.

In Tcl
A Tcl procedure or lambda is variadic when its last argument is args: this will contain a list (possibly empty) of all the remaining arguments. This pattern is common in many other procedure-like methods.

See also
Varargs in Java programming language
Variadic macro (C programming language)
Variadic template

Notes
References
External links
Variadic function. Rosetta Code task showing the implementation of variadic functions in over 120 programming languages.
Variable Argument Functions — A tutorial on Variable Argument Functions for C++
GNU libc manual

## Archive Info
- **Archived on:** 2024-12-15 20:38:55 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 11773 bytes
- **Word Count:** 1913 words
