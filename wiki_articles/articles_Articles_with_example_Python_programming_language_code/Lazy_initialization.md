# Lazy initialization

## Metadata
- **Last Updated:** 2024-12-15 10:08:27 UTC
- **Original Article:** [Lazy initialization](https://en.wikipedia.org/wiki/Lazy_initialization)
- **Language:** en
- **Page ID:** 93427

## Summary
In computer programming, lazy initialization is the tactic of delaying the creation of an object, the calculation of a value, or some other expensive process until the first time it is needed. It is a kind of lazy evaluation that refers specifically to the instantiation of objects or other resources.
This is typically accomplished by augmenting an accessor method (or property getter) to check whether a private member, acting as a cache, has already been initialized.  If it has, it is returned straight away. If not, a new instance is created, placed into the member variable, and returned to the caller just-in-time for its first use. 
If objects have properties that are rarely used, this can improve startup speed. Mean average program performance may be slightly worse in terms of memory (for the condition variables) and execution cycles (to check them), but the impact of object instantiation is spread in time ("amortized") rather than concentrated in the startup phase of a system, and thus median response times can be greatly improved.
In multithreaded code, access to lazy-initialized objects/state must be synchronized to guard against race conditions.

## Categories
This article belongs to the following categories:

- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example C code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example PHP code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Ruby code
- Category:Articles with example Smalltalk code
- Category:Programming language comparisons
- Category:Software design patterns

## Table of Contents

- The "lazy factory"
- Examples
- Theoretical computer science
- See also
- References
- External links

## Content

In computer programming, lazy initialization is the tactic of delaying the creation of an object, the calculation of a value, or some other expensive process until the first time it is needed. It is a kind of lazy evaluation that refers specifically to the instantiation of objects or other resources.
This is typically accomplished by augmenting an accessor method (or property getter) to check whether a private member, acting as a cache, has already been initialized.  If it has, it is returned straight away. If not, a new instance is created, placed into the member variable, and returned to the caller just-in-time for its first use. 
If objects have properties that are rarely used, this can improve startup speed. Mean average program performance may be slightly worse in terms of memory (for the condition variables) and execution cycles (to check them), but the impact of object instantiation is spread in time ("amortized") rather than concentrated in the startup phase of a system, and thus median response times can be greatly improved.
In multithreaded code, access to lazy-initialized objects/state must be synchronized to guard against race conditions.

The "lazy factory"
In a software design pattern view, lazy initialization is often used together with a factory method pattern. This combines three ideas:

Using a factory method to create instances of a class (factory method pattern)
Storing the instances in a map, and returning the same instance to each request for an instance with same parameters (multiton pattern)
Using lazy initialization to instantiate the object the first time it is requested (lazy initialization pattern)

Examples
ActionScript 3
The following is an example of a class with lazy initialization implemented in ActionScript:

Basic use:

C
In C, lazy evaluation would normally be implemented inside one function, or one source file, using static variables.
In a function:

Using one source file instead allows the state to be shared between multiple functions, while still hiding it from non-related functions.
fruit.h:

fruit.c:

main.c:

C#
In .NET Framework 4.0 Microsoft has included a Lazy class that can be used to do lazy loading.
Below is some dummy code that does lazy loading of Class Fruit

Here is a dummy example in C#.
The Fruit class itself doesn't do anything here, The class variable _typesDictionary is a Dictionary/Map used to store Fruit instances by typeName.

A fairly straightforward 'fill-in-the-blanks' example of a Lazy Initialization design pattern, except that this uses an enumeration for the type

C++
This example is in C++.

Crystal
Output:

Number of instances made: 1
Banana

Number of instances made: 2
Banana
Apple

Number of instances made: 2
Banana
Apple

Haxe
This example is in Haxe.

Usage

Java
This example is in Java.

Output

Number of instances made = 1
Banana

Number of instances made = 2
Banana
Apple

Number of instances made = 2
Banana
Apple

JavaScript
This example is in JavaScript.

Output

Number of instances made: 1
Apple

Number of instances made: 2
Apple
Banana

Number of instances made: 2
Apple
Banana

PHP
Here is an example of lazy initialization in PHP 7.4:

Python
This example is in Python.

Ruby
This example is in Ruby, of lazily initializing an authentication token from a remote service like Google. The way that @auth_token is cached is also an example of memoization.

Scala
Scala has built-in support for lazy variable initiation.

Smalltalk
This example is in Smalltalk, of a typical accessor method to return the value of a variable using lazy initialization.

The 'non-lazy' alternative is to use an initialization method that is run when the object is created and then use a simpler accessor method to fetch the value.

Note that lazy initialization can also be used in non-object-oriented languages.

Theoretical computer science
In the field of theoretical computer science, lazy initialization (also called a lazy array) is a technique to design data structures that can work with memory that does not need to be initialized. Specifically, assume that we have access to a table T of n uninitialized memory cells (numbered from 1 to n), and want to assign m cells of this array, e.g., we want to assign T[ki] := vi for pairs (k1, v1), ..., (km, vm) with all ki being different. The lazy initialization technique allows us to do this in just O(m) operations, rather than spending O(m+n) operations to first initialize all array cells. The technique is simply to allocate a table V storing the pairs (ki, vi) in some arbitrary order, and to write for each i in the cell T[ki] the position in V where key ki is stored, leaving the other cells of T uninitialized. This can be used to handle queries in the following fashion: when we look up cell T[k] for some k, we can check if k is in the range {1, ..., m}: if it is not, then T[k] is uninitialized. Otherwise, we check V[T[k]], and verify that the first component of this pair is equal to k. If it is not, then T[k] is uninitialized (and just happened by accident to fall in the range {1, ..., m}). Otherwise, we know that T[k] is indeed one of the initialized cells, and the corresponding value is the second component of the pair.

See also
Double-checked locking
Lazy loading
Proxy pattern
Singleton pattern

References
External links
Article "Java Tip 67: Lazy instantiation - Balancing performance and resource usage" by Philip Bishop and Nigel Warren
Java code examples
Use Lazy Initialization to Conserve Resources
Description from the Portland Pattern Repository
Lazy Initialization of Application Server Services
Lazy Inheritance in JavaScript
Lazy Inheritance in C#

## Archive Info
- **Archived on:** 2024-12-15 20:38:23 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 5650 bytes
- **Word Count:** 928 words
