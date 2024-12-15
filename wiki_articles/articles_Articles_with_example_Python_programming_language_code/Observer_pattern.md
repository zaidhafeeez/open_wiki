# Observer pattern

## Article Metadata

- **Last Updated:** 2024-12-15T04:40:27.217701+00:00
- **Original Article:** [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern)
- **Language:** en
- **Page ID:** 164863

## Summary

In software design and engineering, the observer pattern is a software design pattern in which an object, named the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.
It is often used for implementing distributed event-handling systems in event-driven software. In such systems, the subject is usually named a "stream of events" or "stream source of events" while the observers are called "sin

## Categories

- Category:Articles with example C Sharp code
- Category:Articles with example Java code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Short description is different from Wikidata
- Category:Software design patterns

## Table of Contents

- Overview
- Strong vs. weak reference
- Coupling and typical publish-subscribe implementations
- Structure
- Example
- See also
- References
- External links

## Content

In software design and engineering, the observer pattern is a software design pattern in which an object, named the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.
It is often used for implementing distributed event-handling systems in event-driven software. In such systems, the subject is usually named a "stream of events" or "stream source of events" while the observers are called "sinks of events." The stream nomenclature alludes to a physical setup in which the observers are physically separated and have no control over the emitted events from the subject/stream source. This pattern thus suits any process by which data arrives from some input that is not available to the CPU at startup, but instead may arrive at arbitrary or indeterminate times (HTTP requests, GPIO data, user input from peripherals and distributed databases, etc.).

Overview
The observer design pattern is a behavioural pattern listed among the 23 well-known "Gang of Four" design patterns that address recurring design challenges in order to design flexible and reusable object-oriented software, yielding objects that are easier to implement, change, test and reuse.
The observer pattern addresses the following problems:

A one-to-many dependency between objects should be defined without making the objects tightly coupled.
When one object changes state, an open-ended number of dependent objects should be updated automatically.
An object can notify multiple other objects.
Defining a one-to-many dependency between objects by defining one object (subject) that updates the state of dependent objects directly is inflexible because it couples the subject to particular dependent objects. However, it might be applicable from a performance point of view or if the object implementation is tightly coupled (such as low-level kernel structures that execute thousands of times per second). Tightly coupled objects can be difficult to implement in some scenarios and are not easily reused because they refer to and are aware of many objects with different interfaces. In other scenarios, tightly coupled objects can be a better option because the compiler is able to detect errors at compile time and optimize the code at the CPU instruction level.

Define Subject and Observer objects.
When a subject changes state, all registered observers are notified and updated automatically (and probably asynchronously).
The sole responsibility of a subject is to maintain a list of observers and to notify them of state changes by calling their update() operation. The responsibility of observers is to register and unregister themselves with a subject (in order to be notified of state changes) and to update their state (to synchronize their state with the subject's state) when they are notified. This makes subject and observers loosely coupled. Subject and observers have no explicit knowledge of each other. Observers can be added and removed independently at run time. This notification-registration interaction is also known as publish-subscribe.

Strong vs. weak reference
The observer pattern can cause memory leaks, known as the lapsed listener problem, because in a basic implementation, it requires both explicit registration and explicit deregistration, as in the dispose pattern, because the subject holds strong references to the observers, keeping them alive. This can be prevented if the subject holds weak references to the observers.

Coupling and typical publish-subscribe implementations
Typically, the observer pattern is implemented so that the subject being observed is part of the object for which state changes are being observed (and communicated to the observers). This type of implementation is considered tightly coupled, forcing both the observers and the subject to be aware of each other and have access to their internal parts, creating possible issues of scalability, speed, message recovery and maintenance (also called event or notification loss), the lack of flexibility in conditional dispersion and possible hindrance to desired security measures. In some (non-polling) implementations of the publish-subscribe pattern, this is solved by creating a dedicated message queue server (and sometimes an extra message handler object) as an extra stage between the observer and the object being observed, thus decoupling the components. In these cases, the message queue server is accessed by the observers with the observer pattern, subscribing to certain messages and knowing (or not knowing, in some cases) about only the expected message, while knowing nothing about the message sender itself; the sender may also know nothing about the observers. Other implementations of the publish-subscribe pattern, which achieve a similar effect of notification and communication to interested parties, do not use the observer pattern. 
In early implementations of multi-window operating systems such as OS/2 and Windows, the terms "publish-subscribe pattern" and "event-driven software development" were used as synonyms for the observer pattern. 
The observer pattern, as described in the Design Patterns book, is a very basic concept and does not address removing interest in changes to the observed subject or special logic to be performed by the observed subject before or after notifying the observers. The pattern also does not deal with recording change notifications or guaranteeing that they are received. These concerns are typically handled in message-queueing systems, in which the observer pattern plays only a small part. 
Related patterns include publish–subscribe, mediator and singleton.

Uncoupled
The observer pattern may be used in the absence of publish-subscribe, as when model status is frequently updated. Frequent updates may cause the view to become unresponsive (e.g., by invoking many repaint calls); such observers should instead use a timer. Instead of becoming overloaded by change message, the observer will cause the view to represent the approximate state of the model at a regular interval. This mode of observer is particularly useful for progress bars, in which the underlying operation's progress changes frequently.

Structure
UML class and sequence diagram
In this UML class diagram, the Subject class does not update the state of dependent objects directly. Instead, Subject refers to the Observer interface (update()) for updating state, which makes the Subject independent of how the state of dependent objects is updated. The Observer1 and Observer2 classes implement the Observer interface by synchronizing their state with subject's state.
The UML sequence diagram shows the runtime interactions: The Observer1 and Observer2 objects call attach(this) on Subject1 to register themselves. Assuming that the state of Subject1 changes, Subject1 calls notify() on itself. notify() calls update() on the registered Observer1 and Observer2objects, which request the changed data (getState()) from Subject1 to update (synchronize) their state.

UML class diagram
Example
While the library classes java.util.Observer and java.util.Observable exist, they have been deprecated in Java 9 because the model implemented was quite limited.
Below is an example written in Java that takes keyboard input and handles each input line as an event. When a string is supplied from System.in, the method notifyObservers() is then called in order to notify all observers of the event's occurrence, in the form of an invocation of their update methods.

Java
C++
This is a C++11 implementation.

The program output is like

Groovy
Kotlin
Delphi
Output

Husband listener received notification: Someone is knocking on the door
Wife listener received notification: Someone is knocking on the door

Python
A similar example in Python:

C#
C# provides the IObservable. and IObserver interfaces as well as documentation on how to implement the design pattern.

JavaScript
JavaScript has a deprecated Object.observe function that was a more accurate implementation of the observer pattern. This would fire events upon change to the observed object. Without the deprecated Object.observe function, the pattern may be implemented with more explicit code:

See also
Implicit invocation
Client–server model
The observer pattern is often used in the entity–component–system pattern

References
External links
 Observer implementations in various languages at Wikibooks

## Related Articles

### Internal Links

- [Abstract factory pattern](https://en.wikipedia.org/wiki/Abstract_factory_pattern)
- [Action–domain–responder](https://en.wikipedia.org/wiki/Action%E2%80%93domain%E2%80%93responder)
- [Active object](https://en.wikipedia.org/wiki/Active_object)
- [Active record pattern](https://en.wikipedia.org/wiki/Active_record_pattern)
- [Adapter pattern](https://en.wikipedia.org/wiki/Adapter_pattern)
- [Anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern)
- [Architectural pattern](https://en.wikipedia.org/wiki/Architectural_pattern)
- [Asynchronous method invocation](https://en.wikipedia.org/wiki/Asynchronous_method_invocation)
- [Balking pattern](https://en.wikipedia.org/wiki/Balking_pattern)
- [Behavioral pattern](https://en.wikipedia.org/wiki/Behavioral_pattern)
- [Binding properties pattern](https://en.wikipedia.org/wiki/Binding_properties_pattern)
- [Blackboard (design pattern)](https://en.wikipedia.org/wiki/Blackboard_(design_pattern))
- [Booting](https://en.wikipedia.org/wiki/Booting)
- [Bridge pattern](https://en.wikipedia.org/wiki/Bridge_pattern)
- [Broker pattern](https://en.wikipedia.org/wiki/Broker_pattern)
- [Builder pattern](https://en.wikipedia.org/wiki/Builder_pattern)
- [Business delegate pattern](https://en.wikipedia.org/wiki/Business_delegate_pattern)
- [Central processing unit](https://en.wikipedia.org/wiki/Central_processing_unit)
- [Chain-of-responsibility pattern](https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern)
- [Charles Petzold](https://en.wikipedia.org/wiki/Charles_Petzold)
- [Christopher Alexander](https://en.wikipedia.org/wiki/Christopher_Alexander)
- [Class diagram](https://en.wikipedia.org/wiki/Class_diagram)
- [Client–server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
- [Command pattern](https://en.wikipedia.org/wiki/Command_pattern)
- [Composite entity pattern](https://en.wikipedia.org/wiki/Composite_entity_pattern)
- [Composite pattern](https://en.wikipedia.org/wiki/Composite_pattern)
- [Concurrency pattern](https://en.wikipedia.org/wiki/Concurrency_pattern)
- [Coupling (computer programming)](https://en.wikipedia.org/wiki/Coupling_(computer_programming))
- [Creational pattern](https://en.wikipedia.org/wiki/Creational_pattern)
- [Data access object](https://en.wikipedia.org/wiki/Data_access_object)
- [Data transfer object](https://en.wikipedia.org/wiki/Data_transfer_object)
- [Decorator pattern](https://en.wikipedia.org/wiki/Decorator_pattern)
- [Delegation pattern](https://en.wikipedia.org/wiki/Delegation_pattern)
- [Dependency injection](https://en.wikipedia.org/wiki/Dependency_injection)
- [Deprecation](https://en.wikipedia.org/wiki/Deprecation)
- [Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns)
- [Dispose pattern](https://en.wikipedia.org/wiki/Dispose_pattern)
- [Distributed database](https://en.wikipedia.org/wiki/Distributed_database)
- [Double-checked locking](https://en.wikipedia.org/wiki/Double-checked_locking)
- [Douglas C. Schmidt](https://en.wikipedia.org/wiki/Douglas_C._Schmidt)
- [Enterprise Integration Patterns](https://en.wikipedia.org/wiki/Enterprise_Integration_Patterns)
- [Entity component system](https://en.wikipedia.org/wiki/Entity_component_system)
- [Entity component system](https://en.wikipedia.org/wiki/Entity_component_system)
- [Erich Gamma](https://en.wikipedia.org/wiki/Erich_Gamma)
- [Event-driven programming](https://en.wikipedia.org/wiki/Event-driven_programming)
- [Event (computing)](https://en.wikipedia.org/wiki/Event_(computing))
- [Event (computing)](https://en.wikipedia.org/wiki/Event_(computing))
- [Facade pattern](https://en.wikipedia.org/wiki/Facade_pattern)
- [Factory method pattern](https://en.wikipedia.org/wiki/Factory_method_pattern)
- [Flyweight pattern](https://en.wikipedia.org/wiki/Flyweight_pattern)
- [Front controller](https://en.wikipedia.org/wiki/Front_controller)
- [General-purpose input/output](https://en.wikipedia.org/wiki/General-purpose_input/output)
- [Google Books](https://en.wikipedia.org/wiki/Google_Books)
- [Grady Booch](https://en.wikipedia.org/wiki/Grady_Booch)
- [Guarded suspension](https://en.wikipedia.org/wiki/Guarded_suspension)
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Identity map pattern](https://en.wikipedia.org/wiki/Identity_map_pattern)
- [Implicit invocation](https://en.wikipedia.org/wiki/Implicit_invocation)
- [Intercepting filter pattern](https://en.wikipedia.org/wiki/Intercepting_filter_pattern)
- [Interceptor pattern](https://en.wikipedia.org/wiki/Interceptor_pattern)
- [Interpreter pattern](https://en.wikipedia.org/wiki/Interpreter_pattern)
- [Inversion of control](https://en.wikipedia.org/wiki/Inversion_of_control)
- [Iterator pattern](https://en.wikipedia.org/wiki/Iterator_pattern)
- [JSP model 2 architecture](https://en.wikipedia.org/wiki/JSP_model_2_architecture)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Jim Coplien](https://en.wikipedia.org/wiki/Jim_Coplien)
- [John Vlissides](https://en.wikipedia.org/wiki/John_Vlissides)
- [Join-pattern](https://en.wikipedia.org/wiki/Join-pattern)
- [Kent Beck](https://en.wikipedia.org/wiki/Kent_Beck)
- [Lapsed listener problem](https://en.wikipedia.org/wiki/Lapsed_listener_problem)
- [Lazy loading](https://en.wikipedia.org/wiki/Lazy_loading)
- [Linda Rising](https://en.wikipedia.org/wiki/Linda_Rising)
- [Lock (computer science)](https://en.wikipedia.org/wiki/Lock_(computer_science))
- [Martin Fowler (software engineer)](https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer))
- [Mediator pattern](https://en.wikipedia.org/wiki/Mediator_pattern)
- [Memento pattern](https://en.wikipedia.org/wiki/Memento_pattern)
- [Memory leak](https://en.wikipedia.org/wiki/Memory_leak)
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Method chaining](https://en.wikipedia.org/wiki/Method_chaining)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Mock object](https://en.wikipedia.org/wiki/Mock_object)
- [Model–view–controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
- [Model–view–presenter](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter)
- [Model–view–viewmodel](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)
- [Monitor (synchronization)](https://en.wikipedia.org/wiki/Monitor_(synchronization))
- [Multitier architecture](https://en.wikipedia.org/wiki/Multitier_architecture)
- [Naked objects](https://en.wikipedia.org/wiki/Naked_objects)
- [Null object pattern](https://en.wikipedia.org/wiki/Null_object_pattern)
- [OS/2](https://en.wikipedia.org/wiki/OS/2)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Object pool pattern](https://en.wikipedia.org/wiki/Object_pool_pattern)
- [PCMag](https://en.wikipedia.org/wiki/PCMag)
- [Painter's algorithm](https://en.wikipedia.org/wiki/Painter%27s_algorithm)
- [Peripheral](https://en.wikipedia.org/wiki/Peripheral)
- [Polling (computer science)](https://en.wikipedia.org/wiki/Polling_(computer_science))
- [Portland Pattern Repository](https://en.wikipedia.org/wiki/Portland_Pattern_Repository)
- [Proactor pattern](https://en.wikipedia.org/wiki/Proactor_pattern)
- [Progress bar](https://en.wikipedia.org/wiki/Progress_bar)
- [Prototype pattern](https://en.wikipedia.org/wiki/Prototype_pattern)
- [Proxy pattern](https://en.wikipedia.org/wiki/Proxy_pattern)
- [Publish–subscribe pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
- [Publish–subscribe pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
- [Publish–subscribe pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Ralph Johnson (computer scientist)](https://en.wikipedia.org/wiki/Ralph_Johnson_(computer_scientist))
- [Reactor pattern](https://en.wikipedia.org/wiki/Reactor_pattern)
- [Readers–writer lock](https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock)
- [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin)
- [Scalability](https://en.wikipedia.org/wiki/Scalability)
- [Scheduled-task pattern](https://en.wikipedia.org/wiki/Scheduled-task_pattern)
- [Scheduling (computing)](https://en.wikipedia.org/wiki/Scheduling_(computing))
- [Semaphore (programming)](https://en.wikipedia.org/wiki/Semaphore_(programming))
- [Sequence diagram](https://en.wikipedia.org/wiki/Sequence_diagram)
- [Servant (design pattern)](https://en.wikipedia.org/wiki/Servant_(design_pattern))
- [Service locator pattern](https://en.wikipedia.org/wiki/Service_locator_pattern)
- [Singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern)
- [Software design](https://en.wikipedia.org/wiki/Software_design)
- [Software design pattern](https://en.wikipedia.org/wiki/Software_design_pattern)
- [Software engineering](https://en.wikipedia.org/wiki/Software_engineering)
- [Specification pattern](https://en.wikipedia.org/wiki/Specification_pattern)
- [State pattern](https://en.wikipedia.org/wiki/State_pattern)
- [Strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern)
- [Structural pattern](https://en.wikipedia.org/wiki/Structural_pattern)
- [Template method pattern](https://en.wikipedia.org/wiki/Template_method_pattern)
- [The Hillside Group](https://en.wikipedia.org/wiki/The_Hillside_Group)
- [Thread-local storage](https://en.wikipedia.org/wiki/Thread-local_storage)
- [Thread pool](https://en.wikipedia.org/wiki/Thread_pool)
- [Twin pattern](https://en.wikipedia.org/wiki/Twin_pattern)
- [Shim (computing)](https://en.wikipedia.org/wiki/Shim_(computing))
- [Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)
- [Input/output](https://en.wikipedia.org/wiki/Input/output)
- [Visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern)
- [Ward Cunningham](https://en.wikipedia.org/wiki/Ward_Cunningham)
- [Weak reference](https://en.wikipedia.org/wiki/Weak_reference)
- [Template:Design patterns](https://en.wikipedia.org/wiki/Template:Design_patterns)
- [Template talk:Design patterns](https://en.wikipedia.org/wiki/Template_talk:Design_patterns)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:40:27.217701+00:00_