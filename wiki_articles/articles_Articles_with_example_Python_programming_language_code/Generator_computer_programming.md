# Generator (computer programming)

## Metadata
- **Last Updated:** 2024-12-10 16:05:10 UTC
- **Original Article:** [Generator (computer programming)](https://en.wikipedia.org/wiki/Generator_(computer_programming))
- **Language:** en
- **Page ID:** 572997

## Summary
In computer science, a generator is a routine that can be used to control the iteration behaviour of a loop. All generators are also iterators. A generator is very similar to a function that returns an array, in that a generator has parameters, can be called, and generates a sequence of values. However, instead of building an array containing all the values and returning them all at once, a generator yields the values one at a time, which requires less memory and allows the caller to get started processing the first few values immediately. In short, a generator looks like a function but behaves like an iterator.
Generators can be implemented in terms of more expressive control flow constructs, such as coroutines or first-class continuations. Generators, also known as semicoroutines, are a special case of (and weaker than) coroutines, in that they always yield control back to the caller (when passing a value back), rather than specifying a coroutine to jump to; see comparison of coroutines with generators.

## Categories
This article belongs to the following categories:

- Category:All articles needing additional references
- Category:Articles needing additional references from July 2007
- Category:Articles with example C Sharp code
- Category:Articles with example Haskell code
- Category:Articles with example Java code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with example Racket code
- Category:Articles with example Ruby code
- Category:Articles with example Tcl code
- Category:Iteration in programming
- Category:Programming constructs

## Table of Contents

- Uses
- Timeline
- See also
- Notes
- References

## Content

In computer science, a generator is a routine that can be used to control the iteration behaviour of a loop. All generators are also iterators. A generator is very similar to a function that returns an array, in that a generator has parameters, can be called, and generates a sequence of values. However, instead of building an array containing all the values and returning them all at once, a generator yields the values one at a time, which requires less memory and allows the caller to get started processing the first few values immediately. In short, a generator looks like a function but behaves like an iterator.
Generators can be implemented in terms of more expressive control flow constructs, such as coroutines or first-class continuations. Generators, also known as semicoroutines, are a special case of (and weaker than) coroutines, in that they always yield control back to the caller (when passing a value back), rather than specifying a coroutine to jump to; see comparison of coroutines with generators.

Uses
Generators are usually invoked inside loops.  The first time that a generator invocation is reached in a loop, an iterator object is created that encapsulates the state of the generator routine at its beginning, with arguments bound to the corresponding parameters.  The generator's body is then executed in the context of that iterator until a special yield action is encountered; at that time, the value provided with the yield action is used as the value of the invocation expression.  The next time the same generator invocation is reached in a subsequent iteration, the execution of the generator's body is resumed after the yield action, until yet another yield action is encountered.  In addition to the yield action, execution of the generator body can also be terminated by a finish action, at which time the innermost loop enclosing the generator invocation is terminated. In more complicated situations, a generator may be used manually outside of a loop to create an iterator, which can then be used in various ways.
Because generators compute their yielded values only on demand, they are useful for representing streams, such as sequences that would be expensive or impossible to compute at once. These include e.g. infinite sequences and live data streams.
When eager evaluation is desirable (primarily when the sequence is finite, as otherwise evaluation will never terminate), one can either convert to a list, or use a parallel construction that creates a list instead of a generator. For example, in Python a generator g can be evaluated to a list l via l = list(g), while in F# the sequence expression seq { ... } evaluates lazily (a generator or sequence) but [ ... ] evaluates eagerly (a list).
In the presence of generators, loop constructs of a language – such as for and while – can be reduced into a single loop ... end loop construct; all the usual loop constructs can then be comfortably simulated by using suitable generators in the right way. For example, a ranged loop like for x = 1 to 10 can be implemented as iteration through a generator, as in Python's for x in range(1, 10). Further, break can be implemented as sending finish to the generator and then using continue in the loop.

Timeline
Generators first appeared in CLU (1975), were a prominent feature in the string manipulation language Icon (1977) and are now available in Python (2001), C#, Ruby, PHP, ECMAScript (as of ES6/ES2015), and other languages.  In CLU and C#, generators are called iterators, and in Ruby, enumerators.

Lisp
The final Common Lisp standard does not natively provide generators, yet various library implementations exist, such as SERIES documented in CLtL2 or pygen.

CLU
A yield statement is used to implement iterators over user-defined data abstractions.

Icon
Every expression (including loops) is a generator. The language has many generators built-in and even implements some of the logic semantics using the generator mechanism (logical disjunction or "OR" is done this way).
Printing squares from 0 to 20 can be achieved using a co-routine by writing:

However, most of the time custom generators are implemented with the "suspend" keyword which functions exactly like the "yield" keyword in CLU.

C
C does not have generator functions as a language construct, but, as they are a subset of coroutines, it is simple to implement them using any framework that implements stackful coroutines, such as libdill. On POSIX platforms, when the cost of context switching per iteration is not a concern, or full parallelism rather than merely concurrency is desired, a very simple generator function framework can be implemented using pthreads and pipes.

C++
It is possible to introduce generators into C++ using pre-processor macros. The resulting code might have aspects that are very different from native C++, but the generator syntax can be very uncluttered. The set of pre-processor macros defined in this source allow generators defined with the syntax as in the following example:

This can then be iterated using:

Moreover, C++11 allows foreach loops to be applied to any class that provides the begin and end functions. It's then possible to write generator-like classes by defining both the iterable methods (begin and end) and the iterator methods (operator!=, operator++ and operator*) in the same class. For example, it is possible to write the following program:

A basic range implementation would look like that:

Perl
Perl does not natively provide generators, but support is provided by the Coro::Generator module which uses the Coro co-routine framework.  Example usage:

Raku
Example parallel to Icon uses Raku (formerly/aka Perl 6) Range class as one of several ways to achieve generators with the language.
Printing squares from 0 to 20 can be achieved by writing:

However, most of the time custom generators are implemented with "gather" and "take" keywords in a lazy context.

Tcl
In Tcl 8.6, the generator mechanism is founded on named coroutines.

Haskell
In Haskell, with its lazy evaluation model, every datum created with a non-strict data constructor is generated on demand. For example,

where (:) is a non-strict list constructor, cons, and $ is just a "called-with" operator, used for parenthesization. This uses the standard adaptor function,

which walks down the list and stops on the first element that doesn't satisfy the predicate. If the list has been walked before until that point, it is just a strict data structure, but if any part hadn't been walked through before, it will be generated on demand. List comprehensions can be freely used:

Racket
Racket provides several related facilities for generators.  First, its for-loop forms work with sequences, which are a kind of a producer:

and these sequences are also first-class values:

Some sequences are implemented imperatively (with private state variables) and some are implemented as (possibly infinite) lazy lists.  Also, new struct definitions can have a property that specifies how they can be used as sequences.
But more directly, Racket comes with a generator library for a more traditional generator specification.  For example,

Note that the Racket core implements powerful continuation features, providing general (re-entrant) continuations that are composable, and also delimited continuations.  Using this, the generator library is implemented in Racket.

PHP
The community of PHP implemented generators in PHP 5.5. Details can be found in the original Request for Comments: Generators.
Infinite Fibonacci sequence:

Fibonacci sequence with limit:

Any function which contains a yield statement is automatically a generator function.

Ruby
Ruby supports generators (starting from version 1.9) in the form of the built-in Enumerator class.

Java
Java has had a standard interface for implementing iterators since its early days, and since Java 5, the "foreach" construction makes it easy to loop over objects that provide the java.lang.Iterable interface. (The Java collections framework and other collections frameworks, typically provide iterators for all collections.)

Or get an Iterator from the Java 8 super-interface BaseStream of Stream interface.

Output:

C#
An example C# 2.0 generator (the yield is available since C# version 2.0):
Both of these examples utilize generics, but this is not required. yield keyword also helps in implementing custom stateful iterations over a collection as discussed in this discussion.

It is possible to use multiple yield return statements and they are applied in sequence on each iteration:

XL
In XL, iterators are the basis of 'for' loops:

F#
F# provides generators via sequence expressions, since version 1.9.1. These can define a sequence (lazily evaluated, sequential access) via seq { ... }, a list (eagerly evaluated, sequential access) via [ ... ] or an array (eagerly evaluated, indexed access) via [| ... |] that contain code that generates values. For example,

forms a sequence of squares of numbers from 0 to 14 by filtering out numbers from the range of numbers from 0 to 25.

Python
Generators were added to Python in version 2.2 in 2001. An example generator:

In Python, a generator can be thought of as an iterator that contains a frozen stack frame. Whenever next() is called on the iterator, Python resumes the frozen frame, which executes normally until the next yield statement is reached. The generator's frame is then frozen again, and the yielded value is returned to the caller.
PEP 380 (implemented in Python 3.3) adds the yield from expression, allowing a generator to delegate part of its operations to another generator or iterable.

Generator expressions
Python has a syntax modeled on that of list comprehensions, called a generator expression that aids in the creation of generators.
The following extends the first example above by using a generator expression to compute squares from the countfrom generator function:

ECMAScript
ECMAScript 6 (a.k.a. Harmony) introduced generator functions.
An infinite Fibonacci sequence can be written using a function generator:

R
The iterators package can be used for this purpose.

Smalltalk
Example in Pharo Smalltalk:
The Golden ratio generator below returns to each invocation 'goldenRatio next' a better approximation to the Golden Ratio. 

The expression below returns the next 10 approximations.

See more in A hidden gem in Pharo: Generator.

See also
List comprehension for another construct that generates a sequence of values
Iterator for the concept of producing a list one element at a time
Iteratee for an alternative
Lazy evaluation for producing values when needed
Corecursion for potentially infinite data by recursion instead of yield
Coroutine for even more generalization from subroutine
Continuation for generalization of control flow

Notes
References
Stephan Murer, Stephen Omohundro, David Stoutamire and Clemens Szyperski: Iteration abstraction in Sather.  ACM Transactions on Programming Languages and Systems, 18(1):1-15 (1996) [1]

## Archive Info
- **Archived on:** 2024-12-15 15:18:46 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 11043 bytes
- **Word Count:** 1746 words
