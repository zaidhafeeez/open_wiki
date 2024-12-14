# Foreach loop

## Article Metadata

- **Last Updated:** 2024-12-14T19:37:21.201619+00:00
- **Original Article:** [Foreach loop](https://en.wikipedia.org/wiki/Foreach_loop)
- **Language:** en
- **Page ID:** 623068

## Summary

In computer programming, foreach loop (or for-each loop) is a control flow statement for traversing items in a collection. foreach is usually used in place of a standard for loop statement. Unlike other for loop constructs, however, foreach loops usually maintain no explicit counter: they essentially say "do this to everything in this set", rather than "do this x times". This avoids potential off-by-one errors and makes code simpler to read. In object-oriented languages, an iterator, even if imp

## Categories

- Category:Articles with example Ada code
- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example C code
- Category:Articles with example D code
- Category:Articles with example Eiffel code
- Category:Articles with example Haskell code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example Lisp (programming language) code
- Category:Articles with example MATLAB/Octave code
- Category:Articles with example OCaml code
- Category:Articles with example Objective-C code
- Category:Articles with example PHP code
- Category:Articles with example Pascal code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with example Racket code
- Category:Articles with example Ruby code
- Category:Articles with example Rust code
- Category:Articles with example Scala code
- Category:Articles with example Scheme (programming language) code
- Category:Articles with example Smalltalk code
- Category:Articles with example Swift code
- Category:Articles with example Tcl code
- Category:Articles with short description
- Category:Control flow
- Category:Iteration in programming
- Category:Programming language comparisons
- Category:Short description is different from Wikidata

## Table of Contents

- Syntax
- Language support
- See also

## Content

In computer programming, foreach loop (or for-each loop) is a control flow statement for traversing items in a collection. foreach is usually used in place of a standard for loop statement. Unlike other for loop constructs, however, foreach loops usually maintain no explicit counter: they essentially say "do this to everything in this set", rather than "do this x times". This avoids potential off-by-one errors and makes code simpler to read. In object-oriented languages, an iterator, even if implicit, is often used as the means of traversal.
The foreach statement in some languages has some defined order, processing each item in the collection from the first to the last.
The foreach statement in many other languages, especially array programming languages, does not have any particular order. This simplifies loop optimization in general and in particular allows vector processing of items in the collection concurrently.

Syntax
Syntax varies among languages. Most use the simple word for, although other use the more logical word foreach, roughly as follows:

foreach(key, value) in collection {
  # Do something to value #
}

Language support
Programming languages which support foreach loops include ABC, ActionScript, Ada, C++ (since C++11), C#, ColdFusion Markup Language (CFML), Cobra, D, Daplex (query language), Delphi, ECMAScript, Erlang, Java (since 1.5), JavaScript, Lua, Objective-C (since 2.0), ParaSail, Perl, PHP, Prolog, Python, R, REALbasic, Rebol, Red, Ruby, Scala, Smalltalk, Swift, Tcl, tcsh, Unix shells, Visual Basic (.NET), and Windows PowerShell. Notable languages without foreach are C, and C++ pre-C++11.

ActionScript 3.0
ActionScript supports the ECMAScript 4.0 Standard for for each .. in which pulls the value at each index.

It also supports for .. in which pulls the key at each index.

Ada
Ada supports foreach loops as part of the normal for loop. Say X is an array:

This syntax is used on mostly arrays, but will also work with other types when a full iteration is needed.
Ada 2012 has generalized loops to foreach loops on any kind of container (array, lists, maps...):

C
The C language does not have collections or a foreach construct. However, it has several standard data structures that can be used as collections, and foreach can be made easily with a macro.
However, two obvious problems occur:

The macro is unhygienic: it declares a new variable in the existing scope which remains after the loop.
One foreach macro cannot be defined that works with different collection types (e.g., array and linked list) or that is extensible to user types.
C string as a collection of char

C int array as a collection of int (array size known at compile-time)

Most general: string or array as collection (collection size known at run-time)

idxtype can be removed and typeof(col[0]) used in its place with GCC

C#
In C#, assuming that myArray is an array of integers:

Language Integrated Query (LINQ) provides the following syntax, accepting a delegate or lambda expression:

C++
C++11 provides a foreach loop. The syntax is similar to that of Java:

C++11 range-based for statements have been implemented in GNU Compiler Collection (GCC) (since version 4.6), Clang (since version 3.0) and Visual C++ 2012 (version 11 )
The range-based for is syntactic sugar equivalent to:

The compiler uses argument-dependent lookup to resolve the begin and end functions.
The C++ Standard Library also supports for_each, that applies each element to a function, which can be any predefined function or a lambda expression. While range-based for is only from the start to the end, the range or direction can be changed by altering the first two parameters.

Qt, a C++ framework, offers a macro providing foreach loops using the STL iterator interface:

Boost, a set of free peer-reviewed portable C++ libraries also provides foreach loops:

C++/CLI
The C++/CLI language proposes a construct similar to C#.
Assuming that myArray is an array of integers:

ColdFusion Markup Language (CFML)
Script syntax
Tag syntax
CFML incorrectly identifies the value as "index" in this construct; the index variable does receive the actual value of the array element, not its index.

Common Lisp
Common Lisp provides foreach ability either with the dolist macro:

or the powerful loop macro to iterate on more data types

and even with the mapcar function:

D
or

Dart
Object Pascal, Delphi
Foreach support was added in Delphi 2005, and uses an enumerator variable that must be declared in the var section.

Eiffel
The iteration (foreach) form of the Eiffel loop construct is introduced by the keyword across.
In this example, every element of the structure my_list is printed:

The local entity ic is an instance of the library class ITERATION_CURSOR. The cursor's feature item provides access to each structure element. Descendants of class ITERATION_CURSOR can be created to handle specialized iteration algorithms. The types of objects that can be iterated across (my_list in the example) are based on classes that inherit from the library class ITERABLE.
The iteration form of the Eiffel loop can also be used as a boolean expression when the keyword loop is replaced by either all (effecting universal quantification) or some (effecting existential quantification).
This iteration is a boolean expression which is true if all items in my_list have counts greater than three:

The following is true if at least one item has a count greater than three:

Go
Go's foreach loop can be used to loop over an array, slice, string, map, or channel.
Using the two-value form gets the index/key (first element) and the value (second element):

Using the one-value form gets the index/key (first element):

Groovy
Groovy supports for loops over collections like arrays, lists and ranges:

Groovy also supports a C-style for loop with an array index:

Collections in Groovy can also be iterated over using the each keyword
and a closure. By default, the loop dummy is named it

Haskell
Haskell allows looping over lists with monadic actions using mapM_ and forM_ (mapM_ with its arguments flipped) from Control.Monad:

It's also possible to generalize those functions to work on applicative functors rather than monads and any data structure that is traversable using traverse (for with its arguments flipped) and mapM (forM with its arguments flipped) from Data.Traversable.

Haxe
Java
In Java, a foreach-construct was introduced in Java Development Kit (JDK) 1.5.0.
Official sources use several names for the construct. It is referred to as the "Enhanced for Loop", the "For-Each Loop", and the "foreach statement".: 264 

Java also provides the stream api since java 8:: 294–203

JavaScript
In ECMAScript 5, a callback-based forEach() method was added to the array prototype:The ECMAScript 6 standard introduced a more conventional for..of syntax that works on all iterables rather than operating on only array instances. However, no index variable is available with the syntax.

For unordered iteration over the keys in an object, JavaScript features the for..in loop:

To limit the iteration to the object's own properties, excluding those inherited through the prototype chain, it's often useful to add a hasOwnProperty() test (or a hasOwn() test if supported).

Alternatively, the Object.keys() method combined with the for..of loop can be used for a less verbose way to iterate over the keys of an object.

Lua
Source:

Iterate only through numerical index values:Iterate through all index values:

Mathematica
In Mathematica, Do will simply evaluate an expression for each element of a list, without returning any value.

It is more common to use Table, which returns the result of each evaluation in a new list.

MATLAB
Mint
For each loops are supported in Mint, possessing the following syntax:

The for (;;) or while (true) infinite loop
in Mint can be written using a for each loop and an infinitely long list.

Objective-C
Foreach loops, called Fast enumeration, are supported starting in Objective-C 2.0. They can be used to iterate over any object that implements the NSFastEnumeration protocol, including NSArray, NSDictionary (iterates over keys), NSSet, etc.

NSArrays can also broadcast a message to their members:

Where blocks are available, an NSArray can automatically perform a block on every contained item:

The type of collection being iterated will dictate the item returned with each iteration.
For example:

OCaml
OCaml is a functional programming language. Thus, the equivalent of a foreach loop can be achieved as a library function over lists and arrays.
For lists:

or in short way:

For arrays:

or in short way:

ParaSail
The ParaSail parallel programming language supports several kinds of iterators, including a general "for each" iterator over a container:

ParaSail also supports filters on iterators, and the ability to refer to both the key and the value of a map. Here is a forward iteration over the elements of "My_Map" selecting only elements where the keys are in "My_Set":

Pascal
In Pascal, ISO standard 10206:1990 introduced iteration over set types, thus:

Perl
In Perl, foreach (which is equivalent to the shorter for) can be used to traverse elements of a list.  The expression which denotes the collection to loop over is evaluated in list-context and each item of the resulting list is, in turn, aliased to the loop variable.
List literal example:

Array examples:

Hash example:

Direct modification of collection members:

PHP
It is also possible to extract both keys and values using the alternate syntax:

Direct modification of collection members:

More information

Python
Python's tuple assignment, fully available in its foreach loop, also makes it trivial to iterate on (key, value) pairs in dictionaries:

As for ... in is the only kind of for loop in Python, the equivalent to the "counter" loop found in other languages is...

... although using the enumerate function is considered more "Pythonic":

R
As for ... in is the only kind of for loop in R, the equivalent to the "counter" loop found in other languages is...

Racket
or using the conventional Scheme for-each function:

do-something-with is a one-argument function.

Raku
In Raku, a sister language to Perl, for must be used to traverse elements of a list (foreach is not allowed). The expression which denotes the collection to loop over is evaluated in list-context, but not flattened by default, and each item of the resulting list is, in turn, aliased to the loop variable(s).
List literal example:

Array examples:

The for loop in its statement modifier form:

Hash example:

or

or

Direct modification of collection members with a doubly pointy block, <->:

Ruby
or

This can also be used with a hash.

Rust
The for loop has the structure for <pattern> in <expression> { /* optional statements */ }. It implicitly calls the IntoIterator::into_iter method on the expression, and uses the resulting value, which must implement the Iterator trait. If the expression is itself an iterator, it is used directly by the for loop through an implementation of IntoIterator for all Iterators that returns the iterator unchanged. The loop calls the Iterator::next method on the iterator before executing the loop body. If Iterator::next returns Some(_), the value inside is assigned to the pattern and the loop body is executed; if it returns None, the loop is terminated.

Scala
Scheme
do-something-with is a one-argument function.

Smalltalk
Swift
Swift uses the for…in construct to iterate over members of a collection.

The for…in loop is often used with the closed and half-open range constructs to iterate over the loop body a certain number of times.

SystemVerilog
SystemVerilog supports iteration over any vector or array type of any dimensionality using the foreach keyword.
A trivial example iterates over an array of integers:

A more complex example iterates over an associative array of arrays of integers:

Tcl
Tcl uses foreach to iterate over lists. It is possible to specify more than one iterator variable, in which case they are assigned sequential values from the list. 

It is also possible to iterate over more than one list simultaneously. In the following i assumes sequential values of the first list, j sequential values of the second list:

Visual Basic (.NET)
or without type inference

Windows
Conventional command processor
Invoke a hypothetical frob command three times, giving it a color name each time.

Windows PowerShell
From a pipeline

XSLT
See also
Do while loop
For loop
While loop
Map (higher-order function)


== References ==

## Related Articles

### Internal Links

- [ABC (programming language)](https://en.wikipedia.org/wiki/ABC_(programming_language))
- [ActionScript](https://en.wikipedia.org/wiki/ActionScript)
- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language))
- [Argument-dependent name lookup](https://en.wikipedia.org/wiki/Argument-dependent_name_lookup)
- [Array (data structure)](https://en.wikipedia.org/wiki/Array_(data_structure))
- [Array programming](https://en.wikipedia.org/wiki/Array_programming)
- [Associative array](https://en.wikipedia.org/wiki/Associative_array)
- [Blocks (C language extension)](https://en.wikipedia.org/wiki/Blocks_(C_language_extension))
- [Boost (C++ libraries)](https://en.wikipedia.org/wiki/Boost_(C%2B%2B_libraries))
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C++/CLI](https://en.wikipedia.org/wiki/C%2B%2B/CLI)
- [C++11](https://en.wikipedia.org/wiki/C%2B%2B11)
- [C++ Standard Library](https://en.wikipedia.org/wiki/C%2B%2B_Standard_Library)
- [COMMAND.COM](https://en.wikipedia.org/wiki/COMMAND.COM)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [C preprocessor](https://en.wikipedia.org/wiki/C_preprocessor)
- [Clang](https://en.wikipedia.org/wiki/Clang)
- [Cmd.exe](https://en.wikipedia.org/wiki/Cmd.exe)
- [Cobra (programming language)](https://en.wikipedia.org/wiki/Cobra_(programming_language))
- [ColdFusion Markup Language](https://en.wikipedia.org/wiki/ColdFusion_Markup_Language)
- [Container (abstract data type)](https://en.wikipedia.org/wiki/Container_(abstract_data_type))
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [Control flow](https://en.wikipedia.org/wiki/Control_flow)
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Daplex](https://en.wikipedia.org/wiki/Daplex)
- [Dart (programming language)](https://en.wikipedia.org/wiki/Dart_(programming_language))
- [Delegate (CLI)](https://en.wikipedia.org/wiki/Delegate_(CLI))
- [Delphi (software)](https://en.wikipedia.org/wiki/Delphi_(software))
- [Do while loop](https://en.wikipedia.org/wiki/Do_while_loop)
- [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript)
- [ECMAScript version history](https://en.wikipedia.org/wiki/ECMAScript_version_history)
- [ECMAScript version history](https://en.wikipedia.org/wiki/ECMAScript_version_history)
- [Eiffel (programming language)](https://en.wikipedia.org/wiki/Eiffel_(programming_language))
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Existential quantification](https://en.wikipedia.org/wiki/Existential_quantification)
- [For loop](https://en.wikipedia.org/wiki/For_loop)
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [GNU Compiler Collection](https://en.wikipedia.org/wiki/GNU_Compiler_Collection)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Haxe](https://en.wikipedia.org/wiki/Haxe)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Infinite loop](https://en.wikipedia.org/wiki/Infinite_loop)
- [Infinite set](https://en.wikipedia.org/wiki/Infinite_set)
- [Iterator](https://en.wikipedia.org/wiki/Iterator)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Java Development Kit](https://en.wikipedia.org/wiki/Java_Development_Kit)
- [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- [Language Integrated Query](https://en.wikipedia.org/wiki/Language_Integrated_Query)
- [Loop optimization](https://en.wikipedia.org/wiki/Loop_optimization)
- [Lua (programming language)](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [Map (higher-order function)](https://en.wikipedia.org/wiki/Map_(higher-order_function))
- [Wolfram Mathematica](https://en.wikipedia.org/wiki/Wolfram_Mathematica)
- [Monad (functional programming)](https://en.wikipedia.org/wiki/Monad_(functional_programming))
- [OCaml](https://en.wikipedia.org/wiki/OCaml)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object Pascal](https://en.wikipedia.org/wiki/Object_Pascal)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [Off-by-one error](https://en.wikipedia.org/wiki/Off-by-one_error)
- [Option type](https://en.wikipedia.org/wiki/Option_type)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PHP syntax and semantics](https://en.wikipedia.org/wiki/PHP_syntax_and_semantics)
- [ParaSail (programming language)](https://en.wikipedia.org/wiki/ParaSail_(programming_language))
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Prolog](https://en.wikipedia.org/wiki/Prolog)
- [Prototype-based programming](https://en.wikipedia.org/wiki/Prototype-based_programming)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Qt (software)](https://en.wikipedia.org/wiki/Qt_(software))
- [Xojo](https://en.wikipedia.org/wiki/Xojo)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Racket (programming language)](https://en.wikipedia.org/wiki/Racket_(programming_language))
- [Raku (programming language)](https://en.wikipedia.org/wiki/Raku_(programming_language))
- [Rebol](https://en.wikipedia.org/wiki/Rebol)
- [Red (programming language)](https://en.wikipedia.org/wiki/Red_(programming_language))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scheme (programming language)](https://en.wikipedia.org/wiki/Scheme_(programming_language))
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Statement (computer science)](https://en.wikipedia.org/wiki/Statement_(computer_science))
- [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar)
- [SystemVerilog](https://en.wikipedia.org/wiki/SystemVerilog)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Tcsh](https://en.wikipedia.org/wiki/Tcsh)
- [Type inference](https://en.wikipedia.org/wiki/Type_inference)
- [Typeof](https://en.wikipedia.org/wiki/Typeof)
- [Universal quantification](https://en.wikipedia.org/wiki/Universal_quantification)
- [Unix shell](https://en.wikipedia.org/wiki/Unix_shell)
- [Vector processor](https://en.wikipedia.org/wiki/Vector_processor)
- [Visual Basic (.NET)](https://en.wikipedia.org/wiki/Visual_Basic_(.NET))
- [Microsoft Visual C++](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B)
- [While loop](https://en.wikipedia.org/wiki/While_loop)
- [PowerShell](https://en.wikipedia.org/wiki/PowerShell)
- [XSLT](https://en.wikipedia.org/wiki/XSLT)
- [Template:Loop constructs](https://en.wikipedia.org/wiki/Template:Loop_constructs)
- [Template talk:Loop constructs](https://en.wikipedia.org/wiki/Template_talk:Loop_constructs)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:37:21.201619+00:00_