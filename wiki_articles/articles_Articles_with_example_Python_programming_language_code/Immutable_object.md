# Immutable object

## Article Metadata

- **Last Updated:** 2024-12-15T04:29:34.507785+00:00
- **Original Article:** [Immutable object](https://en.wikipedia.org/wiki/Immutable_object)
- **Language:** en
- **Page ID:** 197824

## Summary

In object-oriented (OO) and functional programming, an immutable object (unchangeable object) is an object whose state cannot be modified after it is created. This is in contrast to a mutable object (changeable object), which can be modified after it is created. In some cases, an object is considered immutable even if some internally used attributes change, but the object's state appears unchanging from an external point of view. For example, an object that uses memoization to cache the results 

## Categories

- Category:All articles lacking reliable references
- Category:Articles lacking reliable references from July 2017
- Category:Articles with example Ada code
- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example D code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Racket code
- Category:Articles with example Scala code
- Category:Articles with short description
- Category:Functional data structures
- Category:Functional programming
- Category:Object (computer science)
- Category:Short description matches Wikidata
- Category:Webarchive template wayback links

## Table of Contents

- Concepts
- Language-specific details
- See also
- References
- External links

## Content

In object-oriented (OO) and functional programming, an immutable object (unchangeable object) is an object whose state cannot be modified after it is created. This is in contrast to a mutable object (changeable object), which can be modified after it is created. In some cases, an object is considered immutable even if some internally used attributes change, but the object's state appears unchanging from an external point of view. For example, an object that uses memoization to cache the results of expensive computations could still be considered an immutable object.
Strings and other concrete objects are typically expressed as immutable objects to improve readability and runtime efficiency in OO programming. Immutable objects are also useful because they are inherently thread-safe. Other benefits are that they are simpler to understand and reason about and offer higher security than mutable objects.

Concepts
Immutable variables
In imperative programming, values held in program variables whose content never changes are known as constants to differentiate them from variables that could be altered during execution. Examples include conversion factors from meters to feet, or the value of pi to several decimal places.
Read-only fields may be calculated when the program runs (unlike constants, which are known beforehand), but never change after they are initialized.

Weak vs strong immutability
Sometimes, one talks of certain fields of an object being immutable. This means that there is no way to change those parts of the object state, even though other parts of the object may be changeable (weakly immutable). If all fields are immutable, then the object is immutable. If the whole object cannot be extended by another class, the object is called strongly immutable. This might, for example, help to explicitly enforce certain invariants about certain data in the object staying the same through the lifetime of the object. In some languages, this is done with a keyword (e.g. const in C++, final in Java) that designates the field as immutable. Some languages reverse it: in OCaml, fields of an object or record are by default immutable, and must be explicitly marked with mutable to be so.

References to objects
In most object-oriented languages, objects can be referred to using references. Some examples of such languages are Java, C++, C#, VB.NET, and many scripting languages, such as Perl, Python, and Ruby. In this case, it matters whether the state of an object can vary when objects are shared via references.

Referencing vs copying objects
If an object is known to be immutable, it is preferred to create a reference of it instead of copying the entire object. This is done to conserve memory by preventing data duplication and avoid calls to constructors and destructors; it also results in a potential boost in execution speed.
The reference copying technique is much more difficult to use for mutable objects, because if any user of a mutable object reference changes it, all other users of that reference see the change. If this is not the intended effect, it can be difficult to notify the other users to have them respond correctly. In these situations, defensive copying of the entire object rather than the reference is usually an easy but costly solution. The observer pattern is an alternative technique for handling changes to mutable objects.

Copy-on-write
A technique that blends the advantages of mutable and immutable objects, and is supported directly in almost all modern hardware, is copy-on-write (COW). Using this technique, when a user asks the system to copy an object, it instead merely creates a new reference that still points to the same object. As soon as a user attempts to modify the object through a particular reference, the system makes a real copy, applies the modification to that, and sets the reference to refer to the new copy. The other users are unaffected, because they still refer to the original object. Therefore, under COW, all users appear to have a mutable version of their objects, although in the case that users do not modify their objects, the space-saving and speed advantages of immutable objects are preserved. Copy-on-write is popular in virtual memory systems because it allows them to save memory space while still correctly handling anything an application program might do.

Interning
The practice of always using references in place of copies of equal objects is known as interning. If interning is used, two objects are considered equal if and only if their references, typically represented as pointers or integers, are equal. Some languages do this automatically: for example, Python automatically interns short strings. If the algorithm that implements interning is guaranteed to do so in every case that it is possible, then comparing objects for equality is reduced to comparing their pointers – a substantial gain in speed in most applications. (Even if the algorithm is not guaranteed to be comprehensive, there still exists the possibility of a fast path case improvement when the objects are equal and use the same reference.) Interning is generally only useful for immutable objects.

Thread safety
Immutable objects can be useful in multi-threaded applications. Multiple threads can act on data represented by immutable objects without concern of the data being changed by other threads. Immutable objects are therefore considered more thread-safe than mutable objects.

Violating immutability
Immutability does not imply that the object as stored in the computer's memory is unwriteable. Rather, immutability is a compile-time construct that indicates what a programmer can do through the normal interface of the object, not necessarily what they can absolutely do (for instance, by circumventing the type system or violating const correctness in C or C++).

Language-specific details
In Python, Java: 80  and the .NET Framework, strings are immutable objects. Both Java and the .NET Framework have mutable versions of string. In Java: 84  these are StringBuffer and StringBuilder (mutable versions of Java String) and in .NET this is StringBuilder (mutable version of .Net String). Python 3 has a mutable string (bytes) variant, named bytearray.
Additionally, all of the primitive wrapper classes in Java are immutable.
Similar patterns are the Immutable Interface and Immutable Wrapper.
In pure functional programming languages it is not possible to create mutable objects without extending the language (e.g. via a mutable references library or a foreign function interface), so all objects are immutable.

Ada
In Ada, any object is declared either variable (i.e. mutable; typically the implicit default), or constant (i.e. immutable) via the constant keyword.

Subprogram parameters are immutable in the in mode, and mutable in the in out and out modes.

C#
In C# you can enforce immutability of the fields of a class with the readonly statement.: 239 
By enforcing all the fields as immutable, you obtain an immutable type.

C# have records which are immutable.

C++
In C++, a const-correct implementation of Cart would allow the user to create instances of the class and then use them as either const (immutable) or mutable, as desired, by providing two different versions of the items() method. (Notice that in C++ it is not necessary — and in fact impossible — to provide a specialized constructor for const instances.)

Note that, when there is a data member that is a pointer or reference to another object, then it is possible to mutate the object pointed to or referenced only within a non-const method.
C++ also provides abstract (as opposed to bitwise) immutability via the mutable keyword, which lets a member variable be changed from within a const method.

D
In D, there exist two type qualifiers, const and immutable, for variables that cannot be changed. Unlike C++'s const, Java's final, and C#'s readonly, they are transitive and recursively apply to anything reachable through references of such a variable. The difference between const and immutable is what they apply to: const is a property of the variable: there might legally exist mutable references to referred value, i.e. the value can actually change. In contrast, immutable is a property of the referred value: the value and anything transitively reachable from it cannot change (without breaking the type system, leading to undefined behavior). Any reference of that value must be marked const or immutable. Basically for any unqualified type T, const(T) is the disjoint union of T (mutable) and immutable(T).

For a mutable C object, its mField can be written to. For a const(C) object, mField cannot be modified, it inherits const; iField is still immutable as it is the stronger guarantee. For an immutable(C), all fields are immutable.
In a function like this:

Inside the braces, c might refer to the same object as m, so mutations to m could indirectly change c as well. Also, 
c might refer to the same object as i, but since the value then is immutable, there are no changes. However, m and i cannot legally refer to the same object.
In the language of guarantees, mutable has no guarantees (the function might change the object), const is an outward-only guarantee that the function will not change anything, and 
immutable is a bidirectional guarantee (the function will not change the value and the caller must not change it).
Values that are const or immutable must be initialized by direct assignment at the point of declaration or by a constructor.
Because const parameters forget if the value was mutable or not, a similar construct, inout, acts, in a sense, as a variable for mutability information.
A function of type const(S) function(const(T)) returns const(S) typed values for mutable, const and immutable arguments. In contrast, a function of type inout(S) function(inout(T)) returns S for mutable T arguments, const(S) for const(T) values, and immutable(S) for immutable(T) values.
Casting immutable values to mutable inflicts undefined behavior upon change, even if the original value comes from a mutable origin. Casting mutable values to immutable can be legal when there remain no mutable references afterward. "An expression may be converted from mutable (...) to immutable if the expression is unique and all expressions it transitively refers to are either unique or immutable." If the compiler cannot prove uniqueness, the casting can be done explicitly and it is up to the programmer to ensure that no mutable references exist.
The type string is an alias for immutable(char)[], i.e. a typed slice of memory of immutable characters. Making substrings is cheap, as it just copies and modifies a pointer and a length filed, and safe, as the underlying data cannot be changed. Objects of type const(char)[] can refer to strings, but also to mutable buffers.
Making a shallow copy of a const or immutable value removes the outer layer of immutability: Copying an immutable string (immutable(char[])) returns a string (immutable(char)[]). The immutable pointer and length are being copied and the copies are mutable. The referred data has not been copied and keeps its qualifier, in the example immutable. It can be stripped by making a depper copy, e.g. using the dup function.

Java
A classic example of an immutable object is an instance of the Java String class

The method toLowerCase() does not change the data "ABC" that s contains. Instead, a new String object is instantiated and given the data "abc" during its construction. A reference to this String object is returned by the toLowerCase() method. To make the String s contain the data "abc", a different approach is needed:

Now the String s references a new String object that contains "abc". There is nothing in the syntax of the declaration of the class String that enforces it as immutable; rather, none of the String class's methods ever affect the data that a String object contains, thus making it immutable.
The keyword final (detailed article) is used in implementing immutable primitive types and object references, but it cannot, by itself, make the objects themselves immutable.  See below examples:
Primitive type variables (int, long, short, etc.) can be reassigned after being defined. This can be prevented by using final.

Reference types cannot be made immutable just by using the final keyword. final only prevents reassignment.

Primitive wrappers (Integer, Long, Short, Double, Float, Character, Byte, Boolean) are also all immutable. Immutable classes can be implemented by following a few simple guidelines.

JavaScript
In JavaScript, all primitive types (Undefined, Null, Boolean, Number, BigInt, String, Symbol) are immutable, but custom objects are generally mutable.

To simulate immutability in an object, one may define properties as read-only (writable: false).

However, the approach above still lets new properties be added. Alternatively, one may use Object.freeze to make existing objects immutable.

With the implementation of ECMA262, JavaScript has the ability to create immutable references that cannot be reassigned. However, using a const declaration doesn't mean that value of the read-only reference is immutable, just that the name cannot be assigned to a new value.

The use of immutable state has become a rising trend in JavaScript since the introduction of React, which favours Flux-like state management patterns such as Redux.

Perl
In Perl, one can create an immutable class with the Moo library by simply declaring all the attributes read only:

Creating an immutable class used to require two steps:  first, creating accessors (either automatically or manually) that prevent modification of object attributes, and secondly, preventing direct modification of the instance data of instances of that class (this was usually stored in a hash reference, and could be locked with Hash::Util's lock_hash function):

Or, with a manually written accessor:

Python
In Python, some built-in types (numbers, Booleans, strings, tuples, frozensets) are immutable, but custom classes are generally mutable. To simulate immutability in a class, one could override attribute setting and deletion to raise exceptions:

The standard library helpers collections.namedtuple and typing.NamedTuple, available from Python 3.6 onward, create simple immutable classes. The following example is roughly equivalent to the above, plus some tuple-like features:

Introduced in Python 3.7, dataclasses allow developers to emulate immutability with frozen instances.  If a frozen dataclass is built, dataclasses will override __setattr__() and __delattr__() to raise FrozenInstanceError if invoked.

Racket
Racket substantially diverges from other Scheme implementations by making its core pair type ("cons cells") immutable. Instead, it provides a parallel mutable pair type, via mcons, mcar, set-mcar! etc. In addition, many immutable types are supported, for example, immutable strings and vectors, and these are used extensively. New structs are immutable by default, unless a field is specifically declared mutable, or the whole struct:

The language also supports immutable hash tables, implemented functionally, and immutable dictionaries.

Rust
Rust's ownership system allows developers to declare immutable variables, and pass immutable references. By default, all variables and references are immutable. Mutable variables and references are explicitly created with the mut keyword.
Constant items in Rust are always immutable.

Scala
In Scala, any entity (narrowly, a binding) can be defined as mutable or immutable: in the declaration, one can use val (value) for immutable entities and var (variable) for mutable ones. Note that even though an immutable binding can not be reassigned, it may still refer to a mutable object and it is still possible to call mutating methods on that object: the binding is immutable, but the underlying object may be mutable.
For example, the following code snippet:

defines an immutable entity maxValue (the integer type is inferred at compile-time) and a mutable entity named currentValue.
By default, collection classes such as List and Map are immutable, so update-methods return a new instance rather than mutating an existing one. While this may sound inefficient, the implementation of these classes and their guarantees of immutability mean that the new instance can re-use existing nodes, which, especially in the case of creating copies, is very efficient.

See also
Clojure
Erlang
F#
Haskell
Mutator method
Prolog
Scala
Tcl

References
This article contains some material from the Perl Design Patterns Book

External links

Immutable objects in C# using 3 simple steps.
Article Java theory and practice: To mutate or not to mutate? by Brian Goetz, from IBM DeveloperWorks – saved copy at Internet Archive by Brian Goetz, from IBM DeveloperWorks – saved copy at Internet Archive
Immutable objects from JavaPractices.com
Immutable objects from Portland Pattern Repository
Immutable.js by Facebook
Immutable structures in C# Archived 2017-12-21 at the Wayback Machine opensource project in Codeplex
Immutable collections in .NET official library by Microsoft
Immutable objects in C# by Tutlane.com

## Related Articles

### Internal Links

- [.NET Framework](https://en.wikipedia.org/wiki/.NET_Framework)
- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language))
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Clojure](https://en.wikipedia.org/wiki/Clojure)
- [Compile time](https://en.wikipedia.org/wiki/Compile_time)
- [Computer data storage](https://en.wikipedia.org/wiki/Computer_data_storage)
- [Const (computer programming)](https://en.wikipedia.org/wiki/Const_(computer_programming))
- [Const (computer programming)](https://en.wikipedia.org/wiki/Const_(computer_programming))
- [Constant (computer programming)](https://en.wikipedia.org/wiki/Constant_(computer_programming))
- [Constructor (object-oriented programming)](https://en.wikipedia.org/wiki/Constructor_(object-oriented_programming))
- [Copy-on-write](https://en.wikipedia.org/wiki/Copy-on-write)
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Declaration (computer programming)](https://en.wikipedia.org/wiki/Declaration_(computer_programming))
- [Object copying](https://en.wikipedia.org/wiki/Object_copying)
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [F Sharp (programming language)](https://en.wikipedia.org/wiki/F_Sharp_(programming_language))
- [Fast path](https://en.wikipedia.org/wiki/Fast_path)
- [Final (Java)](https://en.wikipedia.org/wiki/Final_(Java))
- [Foreign function interface](https://en.wikipedia.org/wiki/Foreign_function_interface)
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Immutable object](https://en.wikipedia.org/wiki/Immutable_object)
- [Immutability (theology)](https://en.wikipedia.org/wiki/Immutability_(theology))
- [Immutable object](https://en.wikipedia.org/wiki/Immutable_object)
- [Immutable (album)](https://en.wikipedia.org/wiki/Immutable_(album))
- [Immutable (company)](https://en.wikipedia.org/wiki/Immutable_(company))
- [Immutable interface](https://en.wikipedia.org/wiki/Immutable_interface)
- [Imperative programming](https://en.wikipedia.org/wiki/Imperative_programming)
- [String interning](https://en.wikipedia.org/wiki/String_interning)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Member variable](https://en.wikipedia.org/wiki/Member_variable)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)
- [Mutator method](https://en.wikipedia.org/wiki/Mutator_method)
- [OCaml](https://en.wikipedia.org/wiki/OCaml)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Perl Design Patterns Book](https://en.wikipedia.org/wiki/Perl_Design_Patterns_Book)
- [Pi](https://en.wikipedia.org/wiki/Pi)
- [Portland Pattern Repository](https://en.wikipedia.org/wiki/Portland_Pattern_Repository)
- [Primitive wrapper class in Java](https://en.wikipedia.org/wiki/Primitive_wrapper_class_in_Java)
- [Variable (computer science)](https://en.wikipedia.org/wiki/Variable_(computer_science))
- [Prolog](https://en.wikipedia.org/wiki/Prolog)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [History of Python](https://en.wikipedia.org/wiki/History_of_Python)
- [Racket (programming language)](https://en.wikipedia.org/wiki/Racket_(programming_language))
- [React (software)](https://en.wikipedia.org/wiki/React_(software))
- [Redux (JavaScript library)](https://en.wikipedia.org/wiki/Redux_(JavaScript_library))
- [Reference (computer science)](https://en.wikipedia.org/wiki/Reference_(computer_science))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scheme (programming language)](https://en.wikipedia.org/wiki/Scheme_(programming_language))
- [Scripting language](https://en.wikipedia.org/wiki/Scripting_language)
- [State (computer science)](https://en.wikipedia.org/wiki/State_(computer_science))
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [String interning](https://en.wikipedia.org/wiki/String_interning)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Thread safety](https://en.wikipedia.org/wiki/Thread_safety)
- [Thread safety](https://en.wikipedia.org/wiki/Thread_safety)
- [Type qualifier](https://en.wikipedia.org/wiki/Type_qualifier)
- [Undefined behavior](https://en.wikipedia.org/wiki/Undefined_behavior)
- [Visual Basic (.NET)](https://en.wikipedia.org/wiki/Visual_Basic_(.NET))
- [Virtual memory](https://en.wikipedia.org/wiki/Virtual_memory)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Category:Articles lacking reliable references from July 2017](https://en.wikipedia.org/wiki/Category:Articles_lacking_reliable_references_from_July_2017)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:29:34.507785+00:00_