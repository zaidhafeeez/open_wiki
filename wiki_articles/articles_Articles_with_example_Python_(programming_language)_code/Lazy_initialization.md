# Lazy initialization

## Article Metadata

- **Last Updated:** 2024-12-14T19:39:35.587601+00:00
- **Original Article:** [Lazy initialization](https://en.wikipedia.org/wiki/Lazy_initialization)
- **Language:** en
- **Page ID:** 93427

## Summary

In computer programming, lazy initialization is the tactic of delaying the creation of an object, the calculation of a value, or some other expensive process until the first time it is needed. It is a kind of lazy evaluation that refers specifically to the instantiation of objects or other resources.
This is typically accomplished by augmenting an accessor method (or property getter) to check whether a private member, acting as a cache, has already been initialized.  If it has, it is returned st

## Categories

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

## Related Articles

### Internal Links

- [Abstract factory pattern](https://en.wikipedia.org/wiki/Abstract_factory_pattern)
- [Mutator method](https://en.wikipedia.org/wiki/Mutator_method)
- [ActionScript](https://en.wikipedia.org/wiki/ActionScript)
- [Action–domain–responder](https://en.wikipedia.org/wiki/Action%E2%80%93domain%E2%80%93responder)
- [Active object](https://en.wikipedia.org/wiki/Active_object)
- [Active record pattern](https://en.wikipedia.org/wiki/Active_record_pattern)
- [Adapter pattern](https://en.wikipedia.org/wiki/Adapter_pattern)
- [Anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern)
- [Architectural pattern](https://en.wikipedia.org/wiki/Architectural_pattern)
- [Associative array](https://en.wikipedia.org/wiki/Associative_array)
- [Asynchronous method invocation](https://en.wikipedia.org/wiki/Asynchronous_method_invocation)
- [Balking pattern](https://en.wikipedia.org/wiki/Balking_pattern)
- [Behavioral pattern](https://en.wikipedia.org/wiki/Behavioral_pattern)
- [Binding properties pattern](https://en.wikipedia.org/wiki/Binding_properties_pattern)
- [Blackboard (design pattern)](https://en.wikipedia.org/wiki/Blackboard_(design_pattern))
- [Bridge pattern](https://en.wikipedia.org/wiki/Bridge_pattern)
- [Broker pattern](https://en.wikipedia.org/wiki/Broker_pattern)
- [Builder pattern](https://en.wikipedia.org/wiki/Builder_pattern)
- [Business delegate pattern](https://en.wikipedia.org/wiki/Business_delegate_pattern)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Chain-of-responsibility pattern](https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern)
- [Christopher Alexander](https://en.wikipedia.org/wiki/Christopher_Alexander)
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Class variable](https://en.wikipedia.org/wiki/Class_variable)
- [Command pattern](https://en.wikipedia.org/wiki/Command_pattern)
- [Composite entity pattern](https://en.wikipedia.org/wiki/Composite_entity_pattern)
- [Composite pattern](https://en.wikipedia.org/wiki/Composite_pattern)
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [Concurrency pattern](https://en.wikipedia.org/wiki/Concurrency_pattern)
- [Creational pattern](https://en.wikipedia.org/wiki/Creational_pattern)
- [Data access object](https://en.wikipedia.org/wiki/Data_access_object)
- [Data structure](https://en.wikipedia.org/wiki/Data_structure)
- [Data transfer object](https://en.wikipedia.org/wiki/Data_transfer_object)
- [Decorator pattern](https://en.wikipedia.org/wiki/Decorator_pattern)
- [Delegation pattern](https://en.wikipedia.org/wiki/Delegation_pattern)
- [Dependency injection](https://en.wikipedia.org/wiki/Dependency_injection)
- [Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns)
- [Double-checked locking](https://en.wikipedia.org/wiki/Double-checked_locking)
- [Douglas C. Schmidt](https://en.wikipedia.org/wiki/Douglas_C._Schmidt)
- [Enterprise Integration Patterns](https://en.wikipedia.org/wiki/Enterprise_Integration_Patterns)
- [Entity component system](https://en.wikipedia.org/wiki/Entity_component_system)
- [Enumerated type](https://en.wikipedia.org/wiki/Enumerated_type)
- [Erich Gamma](https://en.wikipedia.org/wiki/Erich_Gamma)
- [Facade pattern](https://en.wikipedia.org/wiki/Facade_pattern)
- [Factory method pattern](https://en.wikipedia.org/wiki/Factory_method_pattern)
- [Flyweight pattern](https://en.wikipedia.org/wiki/Flyweight_pattern)
- [Front controller](https://en.wikipedia.org/wiki/Front_controller)
- [Grady Booch](https://en.wikipedia.org/wiki/Grady_Booch)
- [Guarded suspension](https://en.wikipedia.org/wiki/Guarded_suspension)
- [Haxe](https://en.wikipedia.org/wiki/Haxe)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Identity map pattern](https://en.wikipedia.org/wiki/Identity_map_pattern)
- [Intercepting filter pattern](https://en.wikipedia.org/wiki/Intercepting_filter_pattern)
- [Interceptor pattern](https://en.wikipedia.org/wiki/Interceptor_pattern)
- [Interpreter pattern](https://en.wikipedia.org/wiki/Interpreter_pattern)
- [Inversion of control](https://en.wikipedia.org/wiki/Inversion_of_control)
- [Iterator pattern](https://en.wikipedia.org/wiki/Iterator_pattern)
- [JSP model 2 architecture](https://en.wikipedia.org/wiki/JSP_model_2_architecture)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Jim Coplien](https://en.wikipedia.org/wiki/Jim_Coplien)
- [John Vlissides](https://en.wikipedia.org/wiki/John_Vlissides)
- [Join-pattern](https://en.wikipedia.org/wiki/Join-pattern)
- [Kent Beck](https://en.wikipedia.org/wiki/Kent_Beck)
- [Lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation)
- [Lazy loading](https://en.wikipedia.org/wiki/Lazy_loading)
- [Linda Rising](https://en.wikipedia.org/wiki/Linda_Rising)
- [Lock (computer science)](https://en.wikipedia.org/wiki/Lock_(computer_science))
- [Martin Fowler (software engineer)](https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer))
- [Mediator pattern](https://en.wikipedia.org/wiki/Mediator_pattern)
- [Memento pattern](https://en.wikipedia.org/wiki/Memento_pattern)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)
- [Method chaining](https://en.wikipedia.org/wiki/Method_chaining)
- [Mock object](https://en.wikipedia.org/wiki/Mock_object)
- [Model–view–controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
- [Model–view–presenter](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter)
- [Model–view–viewmodel](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)
- [Monitor (synchronization)](https://en.wikipedia.org/wiki/Monitor_(synchronization))
- [Multithreading (computer architecture)](https://en.wikipedia.org/wiki/Multithreading_(computer_architecture))
- [Multitier architecture](https://en.wikipedia.org/wiki/Multitier_architecture)
- [Multiton pattern](https://en.wikipedia.org/wiki/Multiton_pattern)
- [Mutual exclusion](https://en.wikipedia.org/wiki/Mutual_exclusion)
- [Naked objects](https://en.wikipedia.org/wiki/Naked_objects)
- [Null object pattern](https://en.wikipedia.org/wiki/Null_object_pattern)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Object pool pattern](https://en.wikipedia.org/wiki/Object_pool_pattern)
- [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Portland Pattern Repository](https://en.wikipedia.org/wiki/Portland_Pattern_Repository)
- [Proactor pattern](https://en.wikipedia.org/wiki/Proactor_pattern)
- [Prototype pattern](https://en.wikipedia.org/wiki/Prototype_pattern)
- [Proxy pattern](https://en.wikipedia.org/wiki/Proxy_pattern)
- [Publish–subscribe pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Race condition](https://en.wikipedia.org/wiki/Race_condition)
- [Ralph Johnson (computer scientist)](https://en.wikipedia.org/wiki/Ralph_Johnson_(computer_scientist))
- [Reactor pattern](https://en.wikipedia.org/wiki/Reactor_pattern)
- [Readers–writer lock](https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock)
- [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scheduled-task pattern](https://en.wikipedia.org/wiki/Scheduled-task_pattern)
- [Scheduling (computing)](https://en.wikipedia.org/wiki/Scheduling_(computing))
- [Semaphore (programming)](https://en.wikipedia.org/wiki/Semaphore_(programming))
- [Servant (design pattern)](https://en.wikipedia.org/wiki/Servant_(design_pattern))
- [Service locator pattern](https://en.wikipedia.org/wiki/Service_locator_pattern)
- [Singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern)
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Software design pattern](https://en.wikipedia.org/wiki/Software_design_pattern)
- [Specification pattern](https://en.wikipedia.org/wiki/Specification_pattern)
- [State pattern](https://en.wikipedia.org/wiki/State_pattern)
- [Static variable](https://en.wikipedia.org/wiki/Static_variable)
- [Strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern)
- [Structural pattern](https://en.wikipedia.org/wiki/Structural_pattern)
- [Template method pattern](https://en.wikipedia.org/wiki/Template_method_pattern)
- [The Hillside Group](https://en.wikipedia.org/wiki/The_Hillside_Group)
- [Theoretical computer science](https://en.wikipedia.org/wiki/Theoretical_computer_science)
- [Thread-local storage](https://en.wikipedia.org/wiki/Thread-local_storage)
- [Thread pool](https://en.wikipedia.org/wiki/Thread_pool)
- [Twin pattern](https://en.wikipedia.org/wiki/Twin_pattern)
- [Shim (computing)](https://en.wikipedia.org/wiki/Shim_(computing))
- [Value (computer science)](https://en.wikipedia.org/wiki/Value_(computer_science))
- [Visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern)
- [Ward Cunningham](https://en.wikipedia.org/wiki/Ward_Cunningham)
- [Talk:Lazy initialization](https://en.wikipedia.org/wiki/Talk:Lazy_initialization)
- [Template:Design patterns](https://en.wikipedia.org/wiki/Template:Design_patterns)
- [Template talk:Design patterns](https://en.wikipedia.org/wiki/Template_talk:Design_patterns)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:39:35.587601+00:00_