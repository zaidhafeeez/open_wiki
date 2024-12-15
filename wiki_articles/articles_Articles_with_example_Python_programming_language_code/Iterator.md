# Iterator

## Metadata
- **Last Updated:** 2024-12-10 17:03:47 UTC
- **Original Article:** [Iterator](https://en.wikipedia.org/wiki/Iterator)
- **Language:** en
- **Page ID:** 172640

## Summary
In computer programming, an iterator is an object that progressively provides access to each item of a collection, in order. 
A collection may provide multiple iterators via its interface that provide items in different orders, such as forwards and backwards.
An iterator is often implemented in terms of the structure underlying a collection implementation and is often tightly coupled to the collection to enable the operational semantics of the iterator.
An iterator is behaviorally similar to a database cursor. 
Iterators date to the CLU programming language in 1974.

## Categories
This article belongs to the following categories:

- Category:Abstract data types
- Category:All articles needing additional references
- Category:Articles needing additional references from June 2010
- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example Java code
- Category:Articles with example PHP code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Ruby code
- Category:Articles with short description
- Category:CS1 German-language sources (de)
- Category:CS1 maint: bot: original URL status unknown
- Category:Iteration in programming
- Category:Object (computer science)
- Category:Pages displaying short descriptions of redirect targets via Module:Annotated link
- Category:Pages displaying wikidata descriptions as a fallback via Module:Annotated link
- Category:Short description is different from Wikidata

## Table of Contents

- Pattern
- Generator
- Internal Iterator
- Implicit iterator
- Stream
- Contrast with indexing
- In different programming languages
- See also
- References
- External links

## Content

In computer programming, an iterator is an object that progressively provides access to each item of a collection, in order. 
A collection may provide multiple iterators via its interface that provide items in different orders, such as forwards and backwards.
An iterator is often implemented in terms of the structure underlying a collection implementation and is often tightly coupled to the collection to enable the operational semantics of the iterator.
An iterator is behaviorally similar to a database cursor. 
Iterators date to the CLU programming language in 1974.

Pattern
An iterator provides access to an element of a collection (element access) and can change its internal state to provide access to the next element (element traversal). It also provides for creation and initialization to a first element and indicates whether all elements have been traversed. In some programming contexts, an iterator provides additional functionality.
An iterator allows a consumer to process each element of a collection while isolating the consumer from the internal structure of the collection. The collection can store elements in any manner while the consumer can access them as a sequence.
In object-oriented programming, an iterator class is usually designed in tight coordination with the corresponding collection class. Usually, the collection provides the methods for creating iterators.
A loop counter is sometimes also referred to as a loop iterator. A loop counter, however, only provides the traversal functionality and not the element access functionality.

Generator
One way of implementing an iterator is via a restricted form of coroutine, known as a generator. By contrast with a subroutine, a generator coroutine can yield values to its caller multiple times, instead of returning just once. Most iterators are naturally expressible as generators, but because generators preserve their local state between invocations, they're particularly well-suited for complicated, stateful iterators, such as tree traversers. There are subtle differences and distinctions in the use of the terms "generator" and "iterator", which vary between authors and languages. In Python, a generator is an iterator constructor: a function that returns an iterator. An example of a Python generator returning an iterator for the Fibonacci numbers using Python's yield statement follows:

Internal Iterator
An internal iterator is a higher order function (often taking anonymous functions) that traverses a collection while applying a function to each element. For example, Python's map function applies a caller-defined function to each element:

Implicit iterator
Some object-oriented languages such as C#, C++ (later versions), Delphi (later versions), Go, Java (later versions), Lua, Perl, Python, Ruby provide an intrinsic way of iterating through the elements of a collection without an explicit iterator. An iterator object may exist, but is not   represented in the source code.
An implicit iterator is often manifest in language syntax as foreach.
In Python, a collection object can be iterated directly:

In Ruby, iteration requires accessing an iterator property:

This iteration style is sometimes called "internal iteration" because its code fully executes within the context of the iterable object (that controls all aspects of iteration), and the programmer only provides the operation to execute at each step (using an anonymous function).
Languages that support list comprehensions or similar constructs may also make use of implicit iterators during the construction of the result list, as in Python:

Sometimes the implicit hidden nature is only partial. The C++ language has a few function templates for implicit iteration, such as for_each(). These functions still require explicit iterator objects as their initial input, but the subsequent iteration does not expose an iterator object to the user.

Stream
Iterators are a useful abstraction of input streams – they provide a potentially infinite iterable (but not necessarily indexable) object. Several languages, such as Perl and Python, implement streams as iterators. In Python, iterators are objects representing streams of data. Alternative implementations of stream include data-driven languages, such as AWK and sed.

Contrast with indexing
Instead of using an iterator, many languages allow the use of a subscript operator and a loop counter to access each element. Although indexing may be used with collections, the use of iterators may have advantages such as:

Counting loops are not suitable to all data structures, in particular to data structures with no or slow random access, like lists or trees.
Iterators can provide a consistent way to iterate on data structures of all kinds, and therefore make the code more readable, reusable, and less sensitive to a change in the data structure.
An iterator can enforce additional restrictions on access, such as ensuring that elements cannot be skipped or that a previously visited element cannot be accessed a second time.
An iterator may allow the collection object to be modified without invalidating the iterator. For instance, once an iterator has advanced beyond the first element it may be possible to insert additional elements into the beginning of the collection with predictable results. With indexing this is problematic since the index numbers must change.
The ability of a collection to be modified while iterating through its elements has become necessary in modern object-oriented programming, where the interrelationships between objects and the effects of operations may not be obvious. By using an iterator one is isolated from these sorts of consequences. This assertion must however be taken with a grain of salt, because more often than not, for efficiency reasons, the iterator implementation is so tightly bound to the collection that it does preclude modification of the underlying collection without invalidating itself.
For collections that may move around their data in memory, the only way to not invalidate the iterator is, for the collection, to somehow keep track of all the currently alive iterators and update them on the fly. Since the number of iterators at a given time may be arbitrarily large in comparison to the size of the tied collection, updating them all will drastically impair the complexity guarantee on the collection's operations.
An alternative way to keep the number of updates bound relatively to the collection size would be to use a kind of handle mechanism, that is a collection of indirect pointers to the collection's elements that must be updated with the collection, and let the iterators point to these handles instead of directly to the data elements. But this approach will negatively impact the iterator performance, since it must effectuate a double pointer following to access the actual data element. This is usually not desirable, because many algorithms using the iterators invoke the iterators data access operation more often than the advance method. It is therefore especially important to have iterators with very efficient data access.
All in all, this is always a trade-off between security (iterators remain always valid) and efficiency. Most of the time, the added security is not worth the efficiency price to pay for it. Using an alternative collection (for example a singly linked list instead of a vector) would be a better choice (globally more efficient) if the stability of the iterators is needed.

Classification
Categories
Iterators can be categorised according to their functionality. Here is a (non-exhaustive) list of iterator categories:

Types
Different languages or libraries used with these languages define iterator types. Some of them are

In different programming languages
.NET
Iterators in the .NET Framework (i.e. C#) are called "enumerators" and represented by the IEnumerator interface.: 189–190, 344 : 53–54 IEnumerator provides a MoveNext() method, which advances to the next element and indicates whether the end of the collection has been reached;: 344 : 55–56 : 89  a Current property, to obtain the value of the element currently being pointed at.: 344 : 56 : 89  and an optional Reset() method,: 344  to rewind the enumerator back to its initial position. The enumerator initially points to a special value before the first element, so a call to MoveNext() is required to begin iterating.
Enumerators are typically obtained by calling the GetEnumerator() method of an object implementing the IEnumerable interface.: 54–56 : 54–56  a Current property, to obtain the value of the element currently being pointed at;: 344 : 56 : 89 Container classes typically implement this interface. However, the foreach statement in C# can operate on any object providing such a method, even if it does not implement IEnumerable (duck typing).: 89  Both interfaces were expanded into generic versions in .NET 2.0.
The following shows a simple use of iterators in C# 2.0:

C# 2.0 also supports generators: a method that is declared as returning IEnumerator (or IEnumerable), but uses the "yield return" statement to produce a sequence of elements instead of returning an object instance, will be transformed by the compiler into a new class implementing the appropriate interface.

C++
The C++ language makes wide use of iterators in its Standard Library and describes several categories of iterators differing in the repertoire of operations they allow. These include forward iterators, bidirectional iterators, and random access iterators, in order of increasing possibilities. All of the standard container template types provide iterators of one of these categories. Iterators generalize pointers to elements of an array (which indeed can be used as iterators), and their syntax is designed to resemble that of C pointer arithmetic, where the * and -> operators are used to reference the element to which the iterator points and pointer arithmetic operators like ++ are used to modify iterators in the traversal of a container.
Traversal using iterators usually involves a single varying iterator, and two fixed iterators that serve to delimit a range to be traversed. The distance between the limiting iterators, in terms of the number of applications of the operator ++ needed to transform the lower limit into the upper one, equals the number of items in the designated range; the number of distinct iterator values involved is one more than that. By convention, the lower limiting iterator "points to" the first element in the range, while the upper limiting iterator does not point to any element in the range, but rather just beyond the end of the range.
For traversal of an entire container, the begin() method provides the lower limit, and end() the upper limit. The latter does not reference any element of the container at all but is a valid iterator value that can be compared against.
The following example shows a typical use of an iterator.

Iterator types are separate from the container types they are used with, though the two are often used in concert. The category of the iterator (and thus the operations defined for it) usually depends on the type of container, with for instance arrays or vectors providing random access iterators, but sets (which use a linked structure as implementation) only providing bidirectional iterators. One same container type can have more than one associated iterator type; for instance the std::vector<T> container type allows traversal either using (raw) pointers to its elements (of type *<T>), or values of a special type std::vector<T>::iterator, and yet another type is provided for "reverse iterators", whose operations are defined in such a way that an algorithm performing a usual (forward) traversal will actually do traversal in reverse order when called with reverse iterators. Most containers also provide a separate const_iterator type, for which operations that would allow changing the values pointed to are intentionally not defined.
Simple traversal of a container object or a range of its elements (including modification of those elements unless a const_iterator is used) can be done using iterators alone. But container types may also provide methods like insert or erase that modify the structure of the container itself; these are methods of the container class, but in addition require one or more iterator values to specify the desired operation. While it is possible to have multiple iterators pointing into the same container simultaneously, structure-modifying operations may invalidate certain iterator values (the standard specifies for each case whether this may be so); using an invalidated iterator is an error that will lead to undefined behavior, and such errors need not be signaled by the run time system.
Implicit iteration is also partially supported by C++ through the use of standard function templates, such as std::for_each(),
std::copy()
and
std::accumulate().
When used they must be initialized with existing iterators, usually begin and end, that define the range over which iteration occurs. But no explicit iterator object is subsequently exposed as the iteration proceeds. This example shows the use of for_each.

The same can be achieved using std::copy, passing a std::ostream_iterator value as third iterator:

Since C++11, lambda function syntax can be used to specify to operation to be iterated inline, avoiding the need to define a named function. Here is an example of for-each iteration using a lambda function:

Java
Introduced in the Java JDK 1.2 release, the java.util.Iterator interface allows the iteration of container classes. Each Iterator provides a next() and hasNext() method,: 294–295  and may optionally support a remove(): 262, 266  method. Iterators are created by the corresponding container class, typically by a method named iterator().: 99 : 217 
The next() method advances the iterator and returns the value pointed to by the iterator. The first element is obtained upon the first call to next().: 294–295  To determine when all the elements in the container have been visited the hasNext() test method is used.: 262  The following example shows a simple use of iterators:

To show that hasNext() can be called repeatedly, we use it to insert commas between the elements but not after the last element.
This approach does not properly separate the advance operation from the actual data access. If the data element must be used more than once for each advance, it needs to be stored in a temporary variable. When an advance is needed without data access (i.e. to skip a given data element), the access is nonetheless performed, though the returned value is ignored in this case.
For collection types that support it, the remove() method of the iterator removes the most recently visited element from the container while keeping the iterator usable. Adding or removing elements by calling the methods of the container (also from the same thread) makes the iterator unusable. An attempt to get the next element throws the exception. An exception is also thrown if there are no more elements remaining (hasNext() has previously returned false).
Additionally, for java.util.List there is a java.util.ListIterator with a similar API but that allows forward and backward iteration, provides its current index in the list and allows setting of the list element at its position.
The J2SE 5.0 release of Java introduced the Iterable interface to support an enhanced for (foreach) loop for iterating over collections and arrays. Iterable defines the iterator() method that returns an Iterator.: 266  Using the enhanced for loop, the preceding example can be rewritten as

Some containers also use the older (since 1.0) Enumeration class. It provides hasMoreElements() and nextElement() methods but has no methods to modify the container.

Scala
In Scala, iterators have a rich set of methods similar to collections, and can be used directly in for loops. Indeed, both iterators and collections inherit from a common base trait - scala.collection.TraversableOnce. However, because of the rich set of methods available in the Scala collections library, such as map, collect, filter etc., it is often not necessary to deal with iterators directly when programming in Scala.
Java iterators and collections can be automatically converted into Scala iterators and collections, respectively, simply by adding the single line

to the file. The JavaConversions object provides implicit conversions to do this. Implicit conversions are a feature of Scala: methods that, when visible in the current scope, automatically insert calls to themselves into relevant expressions at the appropriate place to make them typecheck when they otherwise would not.

MATLAB
MATLAB supports both external and internal implicit iteration using either "native" arrays or cell arrays. In the case of external iteration where the onus is on the user to advance the traversal and request next elements, one can define a set of elements within an array storage structure and traverse the elements using the for-loop construct. For example,

traverses an array of integers using the for keyword.
In the case of internal iteration where the user can supply an operation to the iterator to perform over every element of a collection, many built-in operators and MATLAB functions are overloaded to execute over every element of an array and return a corresponding output array implicitly. Furthermore, the arrayfun and cellfun functions can be leveraged for performing custom or user defined operations over "native" arrays and cell arrays respectively. For example,

defines a primary function simpleFun that implicitly applies custom subfunction myCustomFun to each element of an array using built-in function arrayfun.
Alternatively, it may be desirable to abstract the mechanisms of the array storage container from the user by defining a custom object-oriented MATLAB implementation of the Iterator Pattern. Such an implementation supporting external iteration is demonstrated in MATLAB Central File Exchange item Design Pattern: Iterator (Behavioral). This is written in the new class-definition syntax introduced with MATLAB software version 7.6 (R2008a) and features a one-dimensional cell array realization of the List Abstract Data Type (ADT) as the mechanism for storing a heterogeneous (in data type) set of elements. It provides the functionality for explicit forward List traversal with the hasNext(), next() and reset() methods for use in a while-loop.

PHP
PHP's foreach loop was introduced in version 4.0 and made compatible with objects as values in 4.0 Beta 4. However, support for iterators was added in PHP 5 through the introduction of the internal Traversable interface. The two main interfaces for implementation in PHP scripts that enable objects to be iterated via the foreach loop are Iterator and IteratorAggregate. The latter does not require the implementing class to declare all required methods, instead it implements an accessor method (getIterator) that returns an instance of Traversable. The Standard PHP Library provides several classes to work with special iterators. PHP also supports Generators since 5.5.
The simplest implementation is by wrapping an array, this can be useful for type hinting and information hiding.

All methods of the example class are used during the execution of a complete foreach loop (foreach ($iterator as $key => $current) {}). The iterator's methods are executed in the following order:

$iterator->rewind() ensures that the internal structure starts from the beginning.
$iterator->valid() returns true in this example.
$iterator->current() returned value is stored in $value.
$iterator->key() returned value is stored in $key.
$iterator->next() advances to the next element in the internal structure.
$iterator->valid() returns false and the loop is aborted.
The next example illustrates a PHP class that implements the Traversable interface, which could be wrapped in an IteratorIterator class to act upon the data before it is returned to the foreach loop. The usage together with the MYSQLI_USE_RESULT constant allows PHP scripts to iterate result sets with billions of rows with very little memory usage. These features are not exclusive to PHP nor to its MySQL class implementations (e.g. the PDOStatement class implements the Traversable interface as well).

Python
Iterators in Python are a fundamental part of the language and in many cases go unseen as they are implicitly used in the for (foreach) statement, in list comprehensions, and in generator expressions. All of Python's standard built-in collection types support iteration, as well as many classes that are part of the standard library. The following example shows typical implicit iteration over a sequence:

Python dictionaries (a form of associative array) can also be directly iterated over, when the dictionary keys are returned; or the items() method of a dictionary can be iterated over where it yields corresponding key,value pairs as a tuple:

Iterators however can be used and defined explicitly. For any iterable sequence type or class, the built-in function iter() is used to create an iterator object. The iterator object can then be iterated with the next() function, which uses the __next__() method internally, which returns the next element in the container. (The previous statement applies to Python 3.x. In Python 2.x, the next() method is equivalent.) A StopIteration exception will be raised when no more elements are left. The following example shows an equivalent iteration over a sequence using explicit iterators:

Any user-defined class can support standard iteration (either implicit or explicit) by defining an __iter__() method that returns an iterator object. The iterator object then needs to define a __next__() method that returns the next element.
Python's generators implement this iteration protocol.

Raku
Iterators in Raku are a fundamental part of the language, although usually users do not have to care about iterators. Their usage is hidden behind iteration APIs such as the for statement, map, grep, list indexing with .[$idx], etc.
The following example shows typical implicit iteration over a collection of values:

Raku hashes can also be directly iterated over; this yields key-value Pair objects. The kv method can be invoked on the hash to iterate over the key and values; the keys method to iterate over the hash's keys; and the values method to iterate over the hash's values.

Iterators however can be used and defined explicitly. For any iterable type, there are several methods that control different aspects of the iteration process. For example, the iterator method is supposed to return an Iterator object, and the pull-one method is supposed to produce and return the next value if possible, or return the sentinel value IterationEnd if no more values could be produced. The following example shows an equivalent iteration over a collection using explicit iterators:

All iterable types in Raku compose the Iterable role, Iterator role, or both. The Iterable is quite simple and only requires the iterator to be implemented by the composing class. The Iterator is more complex and provides a series of methods such as pull-one, which allows for a finer operation of iteration in several contexts such as adding or eliminating items, or skipping over them to access other items. Thus, any user-defined class can support standard iteration by composing these roles and implementing the iterator and/or pull-one methods.
The DNA class represents a DNA strand and implements the iterator by composing the Iterable role. The DNA strand is split into a group of trinucleotides when iterated over:

The Repeater class composes both the Iterable and Iterator roles:

Ruby
Ruby implements iterators quite differently; all iterations are done by means of passing callback closures to container methods - this way Ruby not only implements basic iteration but also several patterns of iteration like function mapping, filters and reducing. Ruby also supports an alternative syntax for the basic iterating method each, the following three examples are equivalent:

...and...

or even shorter

Ruby can also iterate over fixed lists by using Enumerators and either calling their #next method or doing a for each on them, as above.

Rust
Rust makes use of external iterators throughout the standard library, including in its for loop, which implicitly calls the next() method of an iterator until it is consumed. The most basic for loop for example iterates over a Range type:

Specifically, the for loop will call a value's into_iter() method, which returns an iterator that in turn yields the elements to the loop. The for loop (or indeed, any method that consumes the iterator), proceeds until the next() method returns a None value (iterations yielding elements return a Some(T) value, where T is the element type).
All collections provided by the standard library implement the IntoIterator trait (meaning they define the into_iter() method). Iterators themselves implement the Iterator trait, which requires defining the next() method. Furthermore, any type implementing Iterator is automatically provided an implementation for IntoIterator that returns itself.
Iterators support various adapters (map(), filter(), skip(), take(), etc.) as methods provided automatically by the Iterator trait.
Users can create custom iterators by creating a type implementing the Iterator trait. Custom collections can implement the IntoIterator trait and return an associated iterator type for their elements, enabling their use directly in for loops. Below, the Fibonacci type implements a custom, unbounded iterator:

See also
Iteratee
Design pattern (computer science) – Reusable solution to a commonly occurring software problemPages displaying short descriptions of redirect targets
Range (computer science) – concept in computer programmingPages displaying wikidata descriptions as a fallback
Visitor pattern – Software design pattern

References
External links

Java's Iterator, Iterable and ListIterator Explained
.NET interface
Article "Understanding and Using Iterators" by Joshua Gatcomb
Article "A Technique for Generic Iteration and Its Optimization" (217 KB) by Stephen M. Watt
Iterators
Boost C++ Iterator Library
Java interface
PHP: Object Iteration
STL Iterators
What are iterators? - Reference description

## Archive Info
- **Archived on:** 2024-12-15 15:19:05 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 26615 bytes
- **Word Count:** 4087 words
