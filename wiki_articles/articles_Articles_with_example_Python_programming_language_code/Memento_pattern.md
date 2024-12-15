# Memento pattern

## Article Metadata

- **Last Updated:** 2024-12-15T04:35:42.862809+00:00
- **Original Article:** [Memento pattern](https://en.wikipedia.org/wiki/Memento_pattern)
- **Language:** en
- **Page ID:** 140542

## Summary

The memento pattern is a software design pattern that exposes the private internal state of an object.
One example of how this can be used is to restore an object to its previous state (undo via rollback), another is versioning, another is custom serialization.
The memento pattern is implemented with three objects: the originator, a caretaker and a memento. The originator is some object that has an internal state. The caretaker is going to do something to the originator, but wants to be able to 

## Categories

- Category:Articles with example C Sharp code
- Category:Articles with example Java code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Short description is different from Wikidata
- Category:Software design patterns

## Table of Contents

- Structure
- Java example
- C# example
- Python example
- Javascript example
- References
- External links

## Content

The memento pattern is a software design pattern that exposes the private internal state of an object.
One example of how this can be used is to restore an object to its previous state (undo via rollback), another is versioning, another is custom serialization.
The memento pattern is implemented with three objects: the originator, a caretaker and a memento. The originator is some object that has an internal state. The caretaker is going to do something to the originator, but wants to be able to undo the change. The caretaker first asks the originator for a memento object. Then it does whatever operation (or sequence of operations) it was going to do. To roll back to the state before the operations, it returns the memento object to the originator. The memento object itself is an opaque object (one which the caretaker cannot, or should not, change). When using this pattern, care should be taken if the originator may change other objects or resources—the memento pattern operates on a single object.
Classic examples of the memento pattern include a pseudorandom number generator (each consumer of the PRNG serves as a caretaker who can initialize the PRNG (the originator) with the same seed (the memento) to produce an identical sequence of pseudorandom numbers) and the state in a finite state machine.

Structure
UML class and sequence diagram
In the above UML class diagram, 
the Caretaker class refers to the Originator class 
for saving (createMemento()) and restoring (restore(memento)) originator's internal state.

The Originator class implements 

(1) createMemento() by creating and returning a Memento object that stores originator's current internal state
and 

(2) restore(memento) by restoring state from the passed in Memento object.

The UML sequence diagram
shows the run-time interactions: 

(1) Saving originator's internal state: The Caretaker object calls createMemento() on the Originator object,
which creates a Memento object, saves 
its current internal state (setState()), and returns the Memento to the Caretaker.

(2) Restoring originator's internal state: The Caretaker calls restore(memento) on the Originator object and specifies the Memento object that stores the state that should be restored. The Originator gets the state (getState()) from the Memento to set its own state.

Java example
The following Java program illustrates the "undo" usage of the memento pattern.

The output is:

Originator: Setting state to State1
Originator: Setting state to State2
Originator: Saving to Memento.
Originator: Setting state to State3
Originator: Saving to Memento.
Originator: Setting state to State4
Originator: State after restoring from Memento: State3

This example uses a String as the state, which is an immutable object in Java. In real-life scenarios the state will
almost always be a mutable object, in which case a copy of the state must be made.
It must be said that the implementation shown has a drawback: it declares an internal class. It would be better if this memento strategy could apply to more than one originator.
There are mainly three other ways to achieve Memento:

Serialization.
A class declared in the same package.
The object can also be accessed via a proxy, which can achieve any save/restore operation on the object.

C# example
The memento pattern allows one to capture the internal state of an object without violating encapsulation such that later one can undo/revert the changes if required. Here one can see that the memento object is actually used to revert the changes made in the object.

Python example
Javascript example
References
External links
Description of Memento Pattern in Ada
Memento UML Class Diagram with C# and .NET code samples
SourceMaking Tutorial
Memento Design Pattern using Java

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
- [Bridge pattern](https://en.wikipedia.org/wiki/Bridge_pattern)
- [Broker pattern](https://en.wikipedia.org/wiki/Broker_pattern)
- [Builder pattern](https://en.wikipedia.org/wiki/Builder_pattern)
- [Business delegate pattern](https://en.wikipedia.org/wiki/Business_delegate_pattern)
- [Chain-of-responsibility pattern](https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern)
- [Christopher Alexander](https://en.wikipedia.org/wiki/Christopher_Alexander)
- [Command pattern](https://en.wikipedia.org/wiki/Command_pattern)
- [Composite entity pattern](https://en.wikipedia.org/wiki/Composite_entity_pattern)
- [Composite pattern](https://en.wikipedia.org/wiki/Composite_pattern)
- [Concurrency pattern](https://en.wikipedia.org/wiki/Concurrency_pattern)
- [Creational pattern](https://en.wikipedia.org/wiki/Creational_pattern)
- [Data access object](https://en.wikipedia.org/wiki/Data_access_object)
- [Data transfer object](https://en.wikipedia.org/wiki/Data_transfer_object)
- [Decorator pattern](https://en.wikipedia.org/wiki/Decorator_pattern)
- [Delegation pattern](https://en.wikipedia.org/wiki/Delegation_pattern)
- [Dependency injection](https://en.wikipedia.org/wiki/Dependency_injection)
- [Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns)
- [Double-checked locking](https://en.wikipedia.org/wiki/Double-checked_locking)
- [Douglas C. Schmidt](https://en.wikipedia.org/wiki/Douglas_C._Schmidt)
- [Enterprise Integration Patterns](https://en.wikipedia.org/wiki/Enterprise_Integration_Patterns)
- [Entity component system](https://en.wikipedia.org/wiki/Entity_component_system)
- [Erich Gamma](https://en.wikipedia.org/wiki/Erich_Gamma)
- [Facade pattern](https://en.wikipedia.org/wiki/Facade_pattern)
- [Factory method pattern](https://en.wikipedia.org/wiki/Factory_method_pattern)
- [Flyweight pattern](https://en.wikipedia.org/wiki/Flyweight_pattern)
- [Front controller](https://en.wikipedia.org/wiki/Front_controller)
- [Grady Booch](https://en.wikipedia.org/wiki/Grady_Booch)
- [Guarded suspension](https://en.wikipedia.org/wiki/Guarded_suspension)
- [Identity map pattern](https://en.wikipedia.org/wiki/Identity_map_pattern)
- [Intercepting filter pattern](https://en.wikipedia.org/wiki/Intercepting_filter_pattern)
- [Interceptor pattern](https://en.wikipedia.org/wiki/Interceptor_pattern)
- [Interpreter pattern](https://en.wikipedia.org/wiki/Interpreter_pattern)
- [Inversion of control](https://en.wikipedia.org/wiki/Inversion_of_control)
- [Iterator pattern](https://en.wikipedia.org/wiki/Iterator_pattern)
- [JSP model 2 architecture](https://en.wikipedia.org/wiki/JSP_model_2_architecture)
- [Jim Coplien](https://en.wikipedia.org/wiki/Jim_Coplien)
- [John Vlissides](https://en.wikipedia.org/wiki/John_Vlissides)
- [Join-pattern](https://en.wikipedia.org/wiki/Join-pattern)
- [Kent Beck](https://en.wikipedia.org/wiki/Kent_Beck)
- [Lazy loading](https://en.wikipedia.org/wiki/Lazy_loading)
- [Linda Rising](https://en.wikipedia.org/wiki/Linda_Rising)
- [Lock (computer science)](https://en.wikipedia.org/wiki/Lock_(computer_science))
- [Martin Fowler (software engineer)](https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer))
- [Mediator pattern](https://en.wikipedia.org/wiki/Mediator_pattern)
- [Method chaining](https://en.wikipedia.org/wiki/Method_chaining)
- [Mock object](https://en.wikipedia.org/wiki/Mock_object)
- [Model–view–controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
- [Model–view–presenter](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter)
- [Model–view–viewmodel](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)
- [Monitor (synchronization)](https://en.wikipedia.org/wiki/Monitor_(synchronization))
- [Multitier architecture](https://en.wikipedia.org/wiki/Multitier_architecture)
- [Naked objects](https://en.wikipedia.org/wiki/Naked_objects)
- [Null object pattern](https://en.wikipedia.org/wiki/Null_object_pattern)
- [Object pool pattern](https://en.wikipedia.org/wiki/Object_pool_pattern)
- [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern)
- [Portland Pattern Repository](https://en.wikipedia.org/wiki/Portland_Pattern_Repository)
- [Proactor pattern](https://en.wikipedia.org/wiki/Proactor_pattern)
- [Prototype pattern](https://en.wikipedia.org/wiki/Prototype_pattern)
- [Proxy pattern](https://en.wikipedia.org/wiki/Proxy_pattern)
- [Pseudorandom number generator](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)
- [Publish–subscribe pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
- [Ralph Johnson (computer scientist)](https://en.wikipedia.org/wiki/Ralph_Johnson_(computer_scientist))
- [Reactor pattern](https://en.wikipedia.org/wiki/Reactor_pattern)
- [Readers–writer lock](https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock)
- [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin)
- [Scheduled-task pattern](https://en.wikipedia.org/wiki/Scheduled-task_pattern)
- [Scheduling (computing)](https://en.wikipedia.org/wiki/Scheduling_(computing))
- [Semaphore (programming)](https://en.wikipedia.org/wiki/Semaphore_(programming))
- [Servant (design pattern)](https://en.wikipedia.org/wiki/Servant_(design_pattern))
- [Service locator pattern](https://en.wikipedia.org/wiki/Service_locator_pattern)
- [Singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern)
- [Software design pattern](https://en.wikipedia.org/wiki/Software_design_pattern)
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
- [Visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern)
- [Ward Cunningham](https://en.wikipedia.org/wiki/Ward_Cunningham)
- [Template:Design patterns](https://en.wikipedia.org/wiki/Template:Design_patterns)
- [Template talk:Design patterns](https://en.wikipedia.org/wiki/Template_talk:Design_patterns)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:35:42.862809+00:00_