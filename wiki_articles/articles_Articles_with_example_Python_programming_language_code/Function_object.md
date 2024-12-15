# Function object

## Metadata
- **Last Updated:** 2024-12-15 09:15:53 UTC
- **Original Article:** [Function object](https://en.wikipedia.org/wiki/Function_object)
- **Language:** en
- **Page ID:** 509999

## Summary
In computer programming, a function object is a construct allowing an object to be invoked or called as if it were an ordinary function, usually with the same syntax (a function parameter that can also be a function). In some languages, particularly C++, function objects are often called functors (not related to the functional programming concept).

## Categories
This article belongs to the following categories:

- Category:All articles needing additional references
- Category:Articles needing additional references from February 2009
- Category:Articles with example C++ code
- Category:Articles with example C code
- Category:Articles with example D code
- Category:Articles with example Eiffel code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example Julia code
- Category:Articles with example Lisp (programming language) code
- Category:Articles with example Objective-C code
- Category:Articles with example PHP code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Ruby code
- Category:Articles with short description
- Category:Object (computer science)
- Category:Short description is different from Wikidata
- Category:Subroutines
- Category:Webarchive template wayback links

## Table of Contents

- Description
- In C and C++
- In C#
- In D
- In Eiffel
- In Java
- In JavaScript
- In Julia
- In Lisp and Scheme
- In Objective-C
- In Perl
- In PHP
- In PowerShell
- In Python
- In Ruby
- Other meanings
- See also
- Notes
- References
- Further reading
- External links

## Content

In computer programming, a function object is a construct allowing an object to be invoked or called as if it were an ordinary function, usually with the same syntax (a function parameter that can also be a function). In some languages, particularly C++, function objects are often called functors (not related to the functional programming concept).

Description
A typical use of a function object is in writing callback functions. A callback in procedural languages, such as C, may be performed by using function pointers. However it can be difficult or awkward to pass a state into or out of the callback function. This restriction also inhibits more dynamic behavior of the function. A function object solves those problems since the function is really a façade for a full object, carrying its own state.
Many modern (and some older) languages, e.g. C++, Eiffel, Groovy, Lisp, Smalltalk, Perl, PHP, Python, Ruby, Scala, and many others, support first-class function objects and may even make significant use of them. Functional programming languages additionally support closures, i.e. first-class functions that can 'close over' variables in their surrounding environment at creation time. During compilation, a transformation known as lambda lifting converts the closures into function objects.

In C and C++
Consider the example of a sorting routine that uses a callback function to define an ordering relation between a pair of items. The following C/C++ program uses function pointers:

In C++, a function object may be used instead of an ordinary function by defining a class that overloads the function call operator by defining an operator() member function. In C++, this may appear as follows:

Notice that the syntax for providing the callback to the std::sort() function is identical, but an object is passed instead of a function pointer. When invoked, the callback function is executed just as any other member function, and therefore has full access to the other members (data or functions) of the object. Of course, this is just a trivial example. To understand what power a functor provides more than a regular function, consider the common use case of sorting objects by a particular field. In the following example, a functor is used to sort a simple employee database by each employee's ID number.

In C++11, the lambda expression provides a more succinct way to do the same thing.

        
It is possible to use function objects in situations other than as callback functions. In this case, the shortened term functor is normally not used about the function object. Continuing the example,

In addition to class type functors, other kinds of function objects are also possible in C++. They can take advantage of C++'s member-pointer or template facilities. The expressiveness of templates allows some functional programming techniques to be used, such as defining function objects in terms of other function objects (like function composition). Much of the C++ Standard Template Library (STL) makes heavy use of template-based function objects.
Another way to create a function object in C++ is to define a non-explicit conversion function to a function pointer type, a function reference type, or a reference to function pointer type. Assuming the conversion does not discard cv-qualifiers, this allows an object of that type to be used as a function with the same signature as the type it is converted to. Modifying an earlier example to use this we obtain the following class, whose instances can be called like function pointers:

Maintaining state
Another advantage of function objects is their ability to maintain a state that affects operator() between calls. For example, the following code defines a generator counting from 10 upwards and is invoked 11 times.

In C++14 or later, the example above could be rewritten as:

In C#
In C#, function objects are declared via delegates. A delegate can be declared using a named method or a lambda expression. Here is an example using a named method.

Here is an example using a lambda expression.

In D
D provides several ways to declare function objects: Lisp/Python-style via closures or C#-style via delegates, respectively:

The difference between a delegate and a closure in D is automatically and conservatively determined by the compiler. D also supports function literals, that allow a lambda-style definition:

To allow the compiler to inline the code (see above), function objects can also be specified C++-style via operator overloading:

In Eiffel
In the Eiffel software development method and language, operations and objects are seen always as separate concepts. However, the agent mechanism facilitates the modeling of operations as runtime objects. Agents satisfy the range of application attributed to function objects, such as being passed as arguments in procedural calls or specified as callback routines. The design of the agent mechanism in Eiffel attempts to reflect the object-oriented nature of the method and language. An agent is an object that generally is a direct instance of one of the two library classes, which model the two types of routines in Eiffel: PROCEDURE and FUNCTION. These two classes descend from the more abstract ROUTINE.
Within software text, the language keyword agent allows agents to be constructed in a compact form. In the following example, the goal is to add the action of stepping the gauge forward to the list of actions to be executed in the event that a button is clicked.

The routine extend referenced in the example above is a feature of a class in a graphical user interface (GUI) library to provide event-driven programming capabilities.
In other library classes, agents are seen to be used for different purposes. In a library supporting data structures, for example, a class modeling linear structures effects universal quantification with a function for_all of type BOOLEAN that accepts an agent, an instance of FUNCTION, as an argument. So, in the following example, my_action is executed only if all members of my_list contain the character '!':

When agents are created, the arguments to the routines they model and even the target object to which they are applied can be either closed or left open. Closed arguments and targets are given values at agent creation time. The assignment of values for open arguments and targets is deferred until some point after the agent is created. The routine for_all expects as an argument an agent representing a function with one open argument or target that conforms to actual generic parameter for the structure (STRING in this example.)
When the target of an agent is left open, the class name of the expected target, enclosed in braces, is substituted for an object reference as shown in the text agent {STRING}.has ('!') in the example above. When an argument is left open, the question mark character ('?') is coded as a placeholder for the open argument.
The ability to close or leave open targets and arguments is intended to improve the flexibility of the agent mechanism. Consider a class that contains the following procedure to print a string on standard output after a new line:

The following snippet, assumed to be in the same class, uses print_on_new_line to demonstrate the mixing of open arguments and open targets in agents used as arguments to the same routine.

This example uses the procedure do_all for linear structures, which executes the routine modeled by an agent for each item in the structure.
The sequence of three instructions prints the strings in my_list, converts the strings to lowercase, and then prints them again.
Procedure do_all iterates across the structure executing the routine substituting the current item for either the open argument (in the case of the agents based on print_on_new_line), or the open target (in the case of the agent based on to_lower).
Open and closed arguments and targets also allow the use of routines that call for more arguments than are required by closing all but the necessary number of arguments:

The Eiffel agent mechanism is detailed in the Eiffel ISO/ECMA standard document.

In Java
Java has no first-class functions, so function objects are usually expressed by an interface with a single method (most commonly the Callable interface), typically with the implementation being an anonymous inner class, or, starting in Java 8, a lambda.
For an example from Java's standard library, java.util.Collections.sort() takes a List and a functor whose role is to compare objects in the List. Without first-class functions, the function is part of the Comparator interface. This could be used as follows.

In Java 8+, this can be written as:

In JavaScript
In JavaScript, functions are first class objects. JavaScript also supports closures.
Compare the following with the subsequent Python example.

An example of this in use:

In Julia
In Julia, methods are associated with types, so it is possible to make any arbitrary Julia object "callable" by adding methods to its type. (Such "callable" objects are sometimes called "functors.")
An example is this accumulator mutable struct (based on Paul Graham's study on programming language syntax and clarity):

Such an accumulator can also be implemented using closure:

In Lisp and Scheme
In Lisp family languages such as Common Lisp, Scheme, and others, functions are objects, just like strings, vectors, lists, and numbers. A closure-constructing operator creates a function object from a part of the program: the part of code given as an argument to the operator is part of the function, and so is the lexical environment: the bindings of the lexically visible variables are captured and stored in the function object, which is more commonly called a closure. The captured bindings play the role of member variables, and the code part of the closure plays the role of the anonymous member function, just like operator () in C++.
The closure constructor has the syntax (lambda (parameters ...) code ...). The (parameters ...) part allows an interface to be declared, so that the function takes the declared parameters. The code ... part consists of expressions that are evaluated when the functor is called.
Many uses of functors in languages like C++ are simply emulations of the missing closure constructor. Since the programmer cannot directly construct a closure, they must define a class that has all of the necessary state variables, and also a member function. Then, construct an instance of that class instead, ensuring that all the member variables are initialized through its constructor. The values are derived precisely from those local variables that ought to be captured directly by a closure.
A function-object using the class system in Common Lisp, no use of closures:

Since there is no standard way to make funcallable objects in Common Lisp, we fake it by defining a generic function called FUNCTOR-CALL. This can be specialized for any class whatsoever. The standard FUNCALL function is not generic; it only takes function objects.
It is this FUNCTOR-CALL generic function that gives us function objects, which are a computer programming construct allowing an object to be invoked or called as if it were an ordinary function, usually with the same syntax. We have almost the same syntax: FUNCTOR-CALL instead of FUNCALL. Some Lisps provide funcallable objects as a simple extension. Making objects callable using the same syntax as functions is a fairly trivial business. Making a function call operator work with different kinds of function things, whether they be class objects or closures is no more complicated than making a + operator that works with different kinds of numbers, such as integers, reals or complex numbers.
Now, a counter implemented using a closure. This is much more brief and direct. The INITIAL-VALUE argument of the MAKE-COUNTER factory function is captured and used directly. It does not have to be copied into some auxiliary class object through a constructor. It is the counter. An auxiliary object is created, but that happens behind the scenes.

Scheme makes closures even simpler, and Scheme code tends to use such higher-order programming somewhat more idiomatically.

More than one closure can be created in the same lexical environment. A vector of closures, each implementing a specific kind of operation, can quite faithfully emulate an object that has a set of virtual operations. That type of single dispatch object-oriented programming can be done fully with closures.
Thus there exists a kind of tunnel being dug from both sides of the proverbial mountain. Programmers in OOP languages discover function objects by restricting objects to have one main function to do that object's functional purpose, and even eliminate its name so that it looks like the object is being called! While programmers who use closures are not surprised that an object is called like a function, they discover that multiple closures sharing the same environment can provide a complete set of abstract operations like a virtual table for single dispatch type OOP.

In Objective-C
In Objective-C, a function object can be created from the NSInvocation class. Construction of a function object requires a method signature, the target object, and the target selector. Here is an example for creating an invocation to the current object's myMethod:

An advantage of NSInvocation is that the target object can be modified after creation. A single NSInvocation can be created and then called for each of any number of targets, for instance from an observable object. An NSInvocation can be created from only a protocol, but it is not straightforward. See here.

In Perl
In Perl, a function object can be created either from a class's constructor returning a function closed over the object's instance data, blessed into the class:

or by overloading the &{} operator so that the object can be used as a function:

In both cases the function object can be used either using the dereferencing arrow syntax $ref->(@arguments):

or using the coderef dereferencing syntax &$ref(@arguments):

In PHP
PHP 5.3+ has first-class functions that can be used e.g. as parameter to the usort() function:

PHP 5.3+, supports also lambda functions and closures. 

An example of this in use:

It is also possible in PHP 5.3+ to make objects invokable by adding a magic __invoke() method to their class:

In PowerShell
In the Windows PowerShell language, a script block is a collection of statements or expressions that can be used as a single unit. A script block can accept arguments and return values. A script block is an instance of a Microsoft .NET Framework type System.Management.Automation.ScriptBlock.

In Python
In Python, functions are first-class objects, just like strings, numbers, lists etc. This feature eliminates the need to write a function object in many cases. Any object with a __call__() method can be called using function-call syntax.
An example is this accumulator class (based on Paul Graham's study on programming language syntax and clarity):

An example of this in use (using the interactive interpreter):

Since functions are objects, they can also be defined locally, given attributes, and  returned by other functions,  as demonstrated in the following example:

In Ruby
In Ruby, several objects can be considered function objects, in particular Method and Proc objects. Ruby also has two kinds of objects that can be thought of as semi-function objects: UnboundMethod and block. UnboundMethods must first be bound to an object (thus becoming a Method) before they can be used as a function object. Blocks can be called like function objects, but to be used in any other capacity as an object (e.g. passed as an argument) they must first be converted to a Proc. More recently, symbols (accessed via the literal unary indicator :) can also be converted to Procs. Using Ruby's unary & operator—equivalent to calling to_proc on an object, and assuming that method exists—the Ruby Extensions Project created a simple hack.

Now, method foo can be a function object, i.e. a Proc, via &:foo and used via takes_a_functor(&:foo). Symbol.to_proc was officially added to Ruby on June 11, 2006 during RubyKaigi2006. [1]
Because of the variety of forms, the term Functor is not generally used in Ruby to mean a Function object.
Just a type of dispatch delegation introduced by the Ruby Facets project is named as Functor. The most basic definition of which is:

This usage is more akin to that used by functional programming languages, like ML, and the original mathematical terminology.

Other meanings
In a more theoretical context a function object may be considered to be any instance of the class of functions, especially in languages such as Common Lisp in which functions are first-class objects.
The ML family of functional programming languages uses the term functor to represent a mapping from modules to modules, or from types to types and is a technique for reusing code. Functors used in this manner are analogous to the original mathematical meaning of functor in category theory, or to the use of generic programming in C++, Java or Ada.
In Haskell, the term functor is also used for a concept related to the meaning of functor in category theory.
In Prolog and related languages, functor is a synonym for function symbol.

See also
Callback (computer science)
Closure (computer science)
Function pointer
Higher-order function
Command pattern
Currying

Notes
References
Further reading
David Vandevoorde & Nicolai M Josuttis (2006). C++ Templates: The Complete Guide, ISBN 0-201-73484-2: Specifically, chapter 22 is devoted to function objects.

External links
Description from the Portland Pattern Repository
C++ Advanced Design Issues - Asynchronous C++ Archived 2020-09-22 at the Wayback Machine by Kevlin Henney
The Function Pointer Tutorials by Lars Haendel (2000/2001)
Article "Generalized Function Pointers" by Herb Sutter
Generic Algorithms for Java
PHP Functors - Function Objects in PHP
What the heck is a functionoid, and why would I use one? (C++ FAQ)

## Archive Info
- **Archived on:** 2024-12-15 21:04:30 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 18126 bytes
- **Word Count:** 2909 words
