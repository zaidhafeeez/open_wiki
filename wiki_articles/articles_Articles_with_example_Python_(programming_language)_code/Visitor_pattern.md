# Visitor pattern

## Article Metadata

- **Last Updated:** 2024-12-14T19:46:56.448501+00:00
- **Original Article:** [Visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern)
- **Language:** en
- **Page ID:** 38689

## Summary

A visitor pattern is a software design pattern that separates the algorithm from the object structure. Because of this separation, new operations can be added to existing object structures without modifying the structures. It is one way to follow the open/closed principle in object-oriented programming and software engineering. 
In essence, the visitor allows adding new virtual functions to a family of classes, without modifying the classes. Instead, a visitor class is created that implements al

## Categories

- Category:All articles needing additional references
- Category:Articles needing additional references from January 2022
- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example Java code
- Category:Articles with example Lisp (programming language) code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Smalltalk code
- Category:Articles with short description
- Category:CS1 maint: multiple names: authors list
- Category:Commons category link from Wikidata
- Category:Programming language comparisons
- Category:Short description is different from Wikidata
- Category:Software design patterns
- Category:Webarchive template wayback links

## Table of Contents

- Overview
- Definition
- Advantages
- Application
- Structure
- Details
- C# example
- Smalltalk example
- Go
- Java example
- Common Lisp example
- Python example
- Related design patterns
- See also
- References
- External links

## Content

A visitor pattern is a software design pattern that separates the algorithm from the object structure. Because of this separation, new operations can be added to existing object structures without modifying the structures. It is one way to follow the open/closed principle in object-oriented programming and software engineering. 
In essence, the visitor allows adding new virtual functions to a family of classes, without modifying the classes. Instead, a visitor class is created that implements all of the appropriate specializations of the virtual function. The visitor takes the instance reference as input, and implements the goal through double dispatch.
Programming languages with sum types and pattern matching obviate many of the benefits of the visitor pattern, as the visitor class is able to both easily branch on the type of the object and generate a compiler error if a new object type is defined which the visitor does not yet handle.

Overview
The Visitor  

design pattern is one of the twenty-three well-known Gang of Four design patterns 
that describe how to solve recurring design problems to design flexible and reusable object-oriented software, that is, 
objects that are easier to implement, change, test, and reuse.

What problems can the Visitor design pattern solve?
It should be possible to define a new operation for (some) classes of an object structure without changing the classes.
When new operations are needed frequently and the object structure consists of many unrelated classes,
it's inflexible to add new subclasses each time a new operation is required
because "[..] distributing all these operations across the various node classes leads to a system that's hard to understand, maintain, and change."

What solution does the Visitor design pattern describe?
Define a separate (visitor) object that implements an operation to be performed on elements of an object structure.
Clients traverse the object structure and call a dispatching operation accept (visitor) on an element — that "dispatches" (delegates) the request to the "accepted visitor object". The visitor object then performs the operation on the element ("visits the element").
This makes it possible to create new operations independently from the classes of an object structure
by adding new visitor objects.
See also the UML class and sequence diagram below.

Definition
The Gang of Four defines the Visitor as:

Represent[ing] an operation to be performed on elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.
The nature of the Visitor makes it an ideal pattern to plug into public APIs, thus allowing its clients to perform operations on a class using a "visiting" class without having to modify the source.

Advantages
Moving operations into visitor classes is beneficial when

many unrelated operations on an object structure are required,
the classes that make up the object structure are known and not expected to change,
new operations need to be added frequently,
an algorithm involves several classes of the object structure, but it is desired to manage it in one single location,
an algorithm needs to work across several independent class hierarchies.
A drawback to this pattern, however, is that it makes extensions to the class hierarchy more difficult, as new classes typically require a new visit method to be added to each visitor.

Application
Consider the design of a 2D computer-aided design (CAD) system. At its core, there are several types to represent basic geometric shapes like circles, lines, and arcs. The entities are ordered into layers, and at the top of the type hierarchy is the drawing, which is simply a list of layers, plus some added properties.
A fundamental operation on this type hierarchy is saving a drawing to the system's native file format. At first glance, it may seem acceptable to add local save methods to all types in the hierarchy. But it is also useful to be able to save drawings to other file formats. Adding ever more methods for saving into many different file formats soon clutters the relatively pure original geometric data structure.
A naive way to solve this would be to maintain separate functions for each file format. Such a save function would take a drawing as input, traverse it, and encode into that specific file format. As this is done for each added different format, duplication between the functions accumulates. For example, saving a circle shape in a raster format requires very similar code no matter what specific raster form is used, and is different from other primitive shapes. The case for other primitive shapes like lines and polygons is similar. Thus, the code becomes a large outer loop traversing through the objects, with a large decision tree inside the loop querying the type of the object. Another problem with this approach is that it is very easy to miss a shape in one or more savers, or a new primitive shape is introduced, but the save routine is implemented only for one file type and not others, leading to code extension and maintenance problems. As the versions of the same file grows it becomes more complicated to maintain it.
Instead, the visitor pattern can be applied. It encodes the logical operation (i.e. save(image_tree)) on the whole hierarchy into one class (i.e. Saver) that implements the common methods for traversing the tree and describes virtual helper methods (i.e. save_circle, save_square, etc.) to be implemented for format specific behaviors. In the case of the CAD example, such format specific behaviors would be implemented by a subclass of Visitor (i.e. SaverPNG). As such, all duplication of type checks and traversal steps is removed. Additionally, the compiler now complains if a shape is omitted since it is now expected by the common base traversal/save function.

Iteration loops
The visitor pattern may be used for iteration over container-like data structures just like Iterator pattern but with limited functionality.: 288  For example, iteration over a directory structure could be implemented by a function class instead of more conventional loop pattern. This would allow deriving various useful information from directories content by implementing a visitor functionality for every item while reusing the iteration code. It's widely employed in Smalltalk systems and can be found in C++ as well.: 289  A drawback of this approach, however, is that you can't break out of the loop easily or iterate concurrently (in parallel i.e. traversing two containers at the same time by a single i variable).: 289  The latter would require writing additional functionality for a visitor to support these features.: 289

Structure
UML class and sequence diagram
In the UML class diagram above, the ElementA class doesn't implement a new operation directly.
Instead, ElementA implements a dispatching operation  accept(visitor) that "dispatches" (delegates) a request to the "accepted visitor object" (visitor.visitElementA(this)). The Visitor1 class implements the operation (visitElementA(e:ElementA)).

ElementB then implements accept(visitor) by dispatching to visitor.visitElementB(this). The Visitor1 class implements the operation (visitElementB(e:ElementB)).
The UML sequence diagram
shows the run-time interactions: The Client object traverses the elements of an object structure (ElementA,ElementB) and calls accept(visitor) on each element.

First, the Client calls accept(visitor) on
ElementA, which calls visitElementA(this) on the accepted visitor object.
The element itself (this) is passed to the visitor so that 
it can "visit" ElementA (call operationA()).

Thereafter, the Client calls accept(visitor) on
ElementB, which calls visitElementB(this) on the visitor that "visits" ElementB (calls operationB()).

Class diagram
Details
The visitor pattern requires a programming language that supports single dispatch, as common object-oriented languages (such as C++, Java, Smalltalk, Objective-C, Swift, JavaScript, Python and C#) do. Under this condition, consider two objects, each of some class type; one is termed the element, and the other is visitor.
The visitor declares a visit method, which takes the element as an argument, for each class of element. Concrete visitors are derived from the visitor class and implement these visit methods, each of which implements part of the algorithm operating on the object structure. The state of the algorithm is maintained locally by the concrete visitor class.
The element declares an accept method to accept a visitor, taking the visitor as an argument. Concrete elements, derived from the element class, implement the accept method. In its simplest form, this is no more than a call to the visitor's visit method. Composite elements, which maintain a list of child objects, typically iterate over these, calling each child's accept method.
The client creates the object structure, directly or indirectly, and instantiates the concrete visitors. When an operation is to be performed which is implemented using the Visitor pattern, it calls the accept method of the top-level element(s).
When the accept method is called in the program, its implementation is chosen based on both the dynamic type of the element and the static type of the visitor. When the associated visit method is called, its implementation is chosen based on both the dynamic type of the visitor and the static type of the element, as known from within the implementation of the accept method, which is the same as the dynamic type of the element. (As a bonus, if the visitor can't handle an argument of the given element's type, then the compiler will catch the error.)
Thus, the implementation of the visit method is chosen based on both the dynamic type of the element and the dynamic type of the visitor. This effectively implements double dispatch. For languages whose object systems support multiple dispatch, not only single dispatch, such as Common Lisp or C# via the Dynamic Language Runtime (DLR), implementation of the visitor pattern is greatly simplified (a.k.a. Dynamic Visitor) by allowing use of simple function overloading to cover all the cases being visited. A dynamic visitor, provided it operates on public data only, conforms to the open/closed principle (since it does not modify extant structures) and to the single responsibility principle (since it implements the Visitor pattern in a separate component).
In this way, one algorithm can be written to traverse a graph of elements, and many different kinds of operations can be performed during that traversal by supplying different kinds of visitors to interact with the elements based on the dynamic types of both the elements and the visitors.

C# example
This example declares a separate ExpressionPrintingVisitor class that takes care of the printing. If the introduction of a new concrete visitor is desired, a new class will be created to implement the Visitor interface, and new implementations for the Visit methods will be provided. The existing classes (Literal and Addition) will remain unchanged.

Smalltalk example
In this case, it is the object's responsibility to know how to print itself on a stream. The visitor here is then the object, not the stream.

Go
Go does not support method overloading, so the visit methods need different names. A typical visitor interface might be

Java example
The following example is in the language Java, and shows how the contents of a tree of nodes (in this case describing the components of a car) can be printed. Instead of creating print methods for each node subclass (Wheel, Engine, Body, and Car), one visitor class (CarElementPrintVisitor) performs the required printing action. Because different node subclasses require slightly different actions to print properly, CarElementPrintVisitor dispatches actions based on the class of the argument passed to its visit method. CarElementDoVisitor, which is analogous to a save operation for a different file format, does likewise.

Diagram
Sources
Output
Visiting front left wheel
Visiting front right wheel
Visiting back left wheel
Visiting back right wheel
Visiting body
Visiting engine
Visiting car
Kicking my front left wheel
Kicking my front right wheel
Kicking my back left wheel
Kicking my back right wheel
Moving my body
Starting my engine
Starting my car

Common Lisp example
Sources
Output
"front-left-wheel"
"front-right-wheel"
"rear-left-wheel"
"rear-right-wheel"
"body"
"engine"
kicking wheel "front-left-wheel" 42 times
kicking wheel "front-right-wheel" 42 times
kicking wheel "rear-left-wheel" 42 times
kicking wheel "rear-right-wheel" 42 times
don't know how "body" and 42 should interact
starting engine "engine" 42 times
kicking wheel "front-left-wheel" symbolically using symbol ABC
kicking wheel "front-right-wheel" symbolically using symbol ABC
kicking wheel "rear-left-wheel" symbolically using symbol ABC
kicking wheel "rear-right-wheel" symbolically using symbol ABC
don't know how "body" and ABC should interact
starting engine "engine" symbolically using symbol ABC

Notes
The other-object parameter is superfluous in traverse. The reason is that it is possible to use an anonymous function that calls the desired target method with a lexically captured object:

Now, the multiple dispatch occurs in the call issued from the body of the anonymous function, and so traverse is just a mapping function that distributes a function application over the elements of an object. Thus all traces of the Visitor Pattern disappear, except for the mapping function, in which there is no evidence of two objects being involved. All knowledge of there being two objects and a dispatch on their types is in the lambda function.

Python example
Python does not support method overloading in the classical sense (polymorphic behavior according to type of passed parameters), so the "visit" methods for the different model types need to have different names.

Sources
Output
Abstraction
Using Python 3 or above allows to make a general implementation of the accept method:

One could extend this to iterate over the class's method resolution order if they would like to fall back on already-implemented classes. They could also use the subclass hook feature to define the lookup in advance.

Related design patterns
Iterator pattern – defines a traversal principle like the visitor pattern, without making a type differentiation within the traversed objects
Church encoding – a related concept from functional programming, in which tagged union/sum types may be modeled using the behaviors of "visitors" on such types, and which enables the visitor pattern to emulate variants and patterns.

See also
Algebraic data type
Double dispatch
Multiple dispatch
Function object

References
External links

The Visitor Family of Design Patterns at the Wayback Machine (archived October 22, 2015). Additional archives: April 12, 2004, March 5, 2002. A rough chapter from The Principles, Patterns, and Practices of Agile Software Development, Robert C. Martin, Prentice Hall
Visitor pattern in UML and in LePUS3 (a Design Description Language)
Article "Componentization: the Visitor Example by Bertrand Meyer and Karine Arnout, Computer (IEEE), vol. 39, no. 7, July 2006, pages 23-30.
Article A Type-theoretic Reconstruction of the Visitor Pattern
Article "The Essence of the Visitor Pattern" by Jens Palsberg and C. Barry Jay. 1997 IEEE-CS COMPSAC paper showing that accept() methods are unnecessary when reflection is available; introduces term 'Walkabout' for the technique.
Article "A Time for Reflection" by Bruce Wallace – subtitled "Java 1.2's reflection capabilities eliminate burdensome accept() methods from your Visitor pattern"
Visitor Pattern using reflection(java).
PerfectJPattern Open Source Project, Provides a context-free and type-safe implementation of the Visitor Pattern in Java based on Delegates.
Visitor Design Pattern

## Related Articles

### Internal Links

- [Abstract factory pattern](https://en.wikipedia.org/wiki/Abstract_factory_pattern)
- [Action–domain–responder](https://en.wikipedia.org/wiki/Action%E2%80%93domain%E2%80%93responder)
- [Active object](https://en.wikipedia.org/wiki/Active_object)
- [Active record pattern](https://en.wikipedia.org/wiki/Active_record_pattern)
- [Adapter pattern](https://en.wikipedia.org/wiki/Adapter_pattern)
- [Algebraic data type](https://en.wikipedia.org/wiki/Algebraic_data_type)
- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [Anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern)
- [Architectural pattern](https://en.wikipedia.org/wiki/Architectural_pattern)
- [Asynchronous method invocation](https://en.wikipedia.org/wiki/Asynchronous_method_invocation)
- [Balking pattern](https://en.wikipedia.org/wiki/Balking_pattern)
- [Behavioral pattern](https://en.wikipedia.org/wiki/Behavioral_pattern)
- [Bertrand Meyer](https://en.wikipedia.org/wiki/Bertrand_Meyer)
- [Binding properties pattern](https://en.wikipedia.org/wiki/Binding_properties_pattern)
- [Blackboard (design pattern)](https://en.wikipedia.org/wiki/Blackboard_(design_pattern))
- [Bridge pattern](https://en.wikipedia.org/wiki/Bridge_pattern)
- [Broker pattern](https://en.wikipedia.org/wiki/Broker_pattern)
- [Builder pattern](https://en.wikipedia.org/wiki/Builder_pattern)
- [Business delegate pattern](https://en.wikipedia.org/wiki/Business_delegate_pattern)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Chain-of-responsibility pattern](https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern)
- [Christopher Alexander](https://en.wikipedia.org/wiki/Christopher_Alexander)
- [Church encoding](https://en.wikipedia.org/wiki/Church_encoding)
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Class diagram](https://en.wikipedia.org/wiki/Class_diagram)
- [Code reuse](https://en.wikipedia.org/wiki/Code_reuse)
- [Command pattern](https://en.wikipedia.org/wiki/Command_pattern)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Composite entity pattern](https://en.wikipedia.org/wiki/Composite_entity_pattern)
- [Composite pattern](https://en.wikipedia.org/wiki/Composite_pattern)
- [Computer-aided design](https://en.wikipedia.org/wiki/Computer-aided_design)
- [Concurrency pattern](https://en.wikipedia.org/wiki/Concurrency_pattern)
- [Container (abstract data type)](https://en.wikipedia.org/wiki/Container_(abstract_data_type))
- [Creational pattern](https://en.wikipedia.org/wiki/Creational_pattern)
- [Data access object](https://en.wikipedia.org/wiki/Data_access_object)
- [Data transfer object](https://en.wikipedia.org/wiki/Data_transfer_object)
- [Decorator pattern](https://en.wikipedia.org/wiki/Decorator_pattern)
- [Delegation pattern](https://en.wikipedia.org/wiki/Delegation_pattern)
- [Dependency injection](https://en.wikipedia.org/wiki/Dependency_injection)
- [Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns)
- [Double-checked locking](https://en.wikipedia.org/wiki/Double-checked_locking)
- [Double dispatch](https://en.wikipedia.org/wiki/Double_dispatch)
- [Douglas C. Schmidt](https://en.wikipedia.org/wiki/Douglas_C._Schmidt)
- [Dynamic Language Runtime](https://en.wikipedia.org/wiki/Dynamic_Language_Runtime)
- [Enterprise Integration Patterns](https://en.wikipedia.org/wiki/Enterprise_Integration_Patterns)
- [Entity component system](https://en.wikipedia.org/wiki/Entity_component_system)
- [Erich Gamma](https://en.wikipedia.org/wiki/Erich_Gamma)
- [Facade pattern](https://en.wikipedia.org/wiki/Facade_pattern)
- [Factory method pattern](https://en.wikipedia.org/wiki/Factory_method_pattern)
- [Flyweight pattern](https://en.wikipedia.org/wiki/Flyweight_pattern)
- [Front controller](https://en.wikipedia.org/wiki/Front_controller)
- [Function object](https://en.wikipedia.org/wiki/Function_object)
- [Grady Booch](https://en.wikipedia.org/wiki/Grady_Booch)
- [Guarded suspension](https://en.wikipedia.org/wiki/Guarded_suspension)
- [IEEE Computer Society](https://en.wikipedia.org/wiki/IEEE_Computer_Society)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Identity map pattern](https://en.wikipedia.org/wiki/Identity_map_pattern)
- [Intercepting filter pattern](https://en.wikipedia.org/wiki/Intercepting_filter_pattern)
- [Interceptor pattern](https://en.wikipedia.org/wiki/Interceptor_pattern)
- [Interpreter pattern](https://en.wikipedia.org/wiki/Interpreter_pattern)
- [Inversion of control](https://en.wikipedia.org/wiki/Inversion_of_control)
- [Iteration](https://en.wikipedia.org/wiki/Iteration)
- [Iterator pattern](https://en.wikipedia.org/wiki/Iterator_pattern)
- [JSP model 2 architecture](https://en.wikipedia.org/wiki/JSP_model_2_architecture)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Jim Coplien](https://en.wikipedia.org/wiki/Jim_Coplien)
- [John Vlissides](https://en.wikipedia.org/wiki/John_Vlissides)
- [Join-pattern](https://en.wikipedia.org/wiki/Join-pattern)
- [Kent Beck](https://en.wikipedia.org/wiki/Kent_Beck)
- [Lazy loading](https://en.wikipedia.org/wiki/Lazy_loading)
- [Linda Rising](https://en.wikipedia.org/wiki/Linda_Rising)
- [Lock (computer science)](https://en.wikipedia.org/wiki/Lock_(computer_science))
- [Control flow](https://en.wikipedia.org/wiki/Control_flow)
- [Martin Fowler (software engineer)](https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer))
- [Mediator pattern](https://en.wikipedia.org/wiki/Mediator_pattern)
- [Memento pattern](https://en.wikipedia.org/wiki/Memento_pattern)
- [Method chaining](https://en.wikipedia.org/wiki/Method_chaining)
- [Mock object](https://en.wikipedia.org/wiki/Mock_object)
- [Model–view–controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
- [Model–view–presenter](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter)
- [Model–view–viewmodel](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)
- [Monitor (synchronization)](https://en.wikipedia.org/wiki/Monitor_(synchronization))
- [Multiple dispatch](https://en.wikipedia.org/wiki/Multiple_dispatch)
- [Multitier architecture](https://en.wikipedia.org/wiki/Multitier_architecture)
- [Naked objects](https://en.wikipedia.org/wiki/Naked_objects)
- [Null object pattern](https://en.wikipedia.org/wiki/Null_object_pattern)
- [OCLC](https://en.wikipedia.org/wiki/OCLC)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Object pool pattern](https://en.wikipedia.org/wiki/Object_pool_pattern)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern)
- [Open–closed principle](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)
- [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching)
- [Portland Pattern Repository](https://en.wikipedia.org/wiki/Portland_Pattern_Repository)
- [Proactor pattern](https://en.wikipedia.org/wiki/Proactor_pattern)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Prototype pattern](https://en.wikipedia.org/wiki/Prototype_pattern)
- [Proxy pattern](https://en.wikipedia.org/wiki/Proxy_pattern)
- [Publish–subscribe pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Ralph Johnson (computer scientist)](https://en.wikipedia.org/wiki/Ralph_Johnson_(computer_scientist))
- [Reactor pattern](https://en.wikipedia.org/wiki/Reactor_pattern)
- [Readers–writer lock](https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock)
- [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin)
- [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin)
- [Scheduled-task pattern](https://en.wikipedia.org/wiki/Scheduled-task_pattern)
- [Scheduling (computing)](https://en.wikipedia.org/wiki/Scheduling_(computing))
- [Semaphore (programming)](https://en.wikipedia.org/wiki/Semaphore_(programming))
- [Sequence diagram](https://en.wikipedia.org/wiki/Sequence_diagram)
- [Servant (design pattern)](https://en.wikipedia.org/wiki/Servant_(design_pattern))
- [Service locator pattern](https://en.wikipedia.org/wiki/Service_locator_pattern)
- [Dynamic dispatch](https://en.wikipedia.org/wiki/Dynamic_dispatch)
- [Single-responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle)
- [Singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern)
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Software design pattern](https://en.wikipedia.org/wiki/Software_design_pattern)
- [Software engineering](https://en.wikipedia.org/wiki/Software_engineering)
- [Specification pattern](https://en.wikipedia.org/wiki/Specification_pattern)
- [State pattern](https://en.wikipedia.org/wiki/State_pattern)
- [Strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern)
- [Structural pattern](https://en.wikipedia.org/wiki/Structural_pattern)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Tagged union](https://en.wikipedia.org/wiki/Tagged_union)
- [Template method pattern](https://en.wikipedia.org/wiki/Template_method_pattern)
- [The Hillside Group](https://en.wikipedia.org/wiki/The_Hillside_Group)
- [Thread-local storage](https://en.wikipedia.org/wiki/Thread-local_storage)
- [Thread pool](https://en.wikipedia.org/wiki/Thread_pool)
- [Twin pattern](https://en.wikipedia.org/wiki/Twin_pattern)
- [Shim (computing)](https://en.wikipedia.org/wiki/Shim_(computing))
- [Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)
- [Virtual function](https://en.wikipedia.org/wiki/Virtual_function)
- [Ward Cunningham](https://en.wikipedia.org/wiki/Ward_Cunningham)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Cite book](https://en.wikipedia.org/wiki/Template:Cite_book)
- [Template:Design patterns](https://en.wikipedia.org/wiki/Template:Design_patterns)
- [Template talk:Design patterns](https://en.wikipedia.org/wiki/Template_talk:Design_patterns)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from January 2022](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_January_2022)
- [Category:CS1 maint: multiple names: authors list](https://en.wikipedia.org/wiki/Category:CS1_maint:_multiple_names:_authors_list)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:46:56.448501+00:00_