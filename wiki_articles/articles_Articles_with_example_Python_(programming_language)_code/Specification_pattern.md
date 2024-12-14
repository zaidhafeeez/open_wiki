# Specification pattern

## Article Metadata

- **Last Updated:** 2024-12-14T19:45:14.095624+00:00
- **Original Article:** [Specification pattern](https://en.wikipedia.org/wiki/Specification_pattern)
- **Language:** en
- **Page ID:** 12088522

## Summary

In computer programming, the specification pattern is a particular software design pattern, whereby business rules can be recombined by chaining the business rules together using boolean logic. The pattern is frequently used in the context of domain-driven design.
A specification pattern outlines a business rule that is combinable with other business rules. In this pattern, a unit of business logic inherits its functionality from the abstract aggregate Composite Specification class. The Composit

## Categories

- Category:Architectural pattern (computer science)
- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example JavaScript code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Programming language comparisons
- Category:Short description is different from Wikidata
- Category:Software design patterns

## Table of Contents

- Code examples
- Example of use
- References
- External links

## Content

In computer programming, the specification pattern is a particular software design pattern, whereby business rules can be recombined by chaining the business rules together using boolean logic. The pattern is frequently used in the context of domain-driven design.
A specification pattern outlines a business rule that is combinable with other business rules. In this pattern, a unit of business logic inherits its functionality from the abstract aggregate Composite Specification class. The Composite Specification class has one function called IsSatisfiedBy that returns a boolean value. After instantiation, the specification is "chained" with other specifications, making new specifications easily maintainable, yet highly customizable business logic. Furthermore, upon instantiation the business logic may, through method invocation or inversion of control, have its state altered in order to become a delegate of other classes such as a persistence repository.
As a consequence of performing runtime composition of high-level business/domain logic, the Specification pattern is a convenient tool for converting ad-hoc user search criteria into low level logic to be processed by repositories.
Since a specification is an encapsulation of logic in a reusable form it is very simple to thoroughly unit test, and when used in this context is also an implementation of the humble object pattern.

Code examples
C#
C# 6.0 with generics
Python
C++
TypeScript
Example of use
In the next example, invoices are retrieved and sent to a collection agency if:

they are overdue,
notices have been sent, and
they are not already with the collection agency.
This example is meant to show the result of how the logic is 'chained' together.
This usage example assumes a previously defined OverdueSpecification class that is satisfied when an invoice's due date is 30 days or older, a NoticeSentSpecification class that is satisfied when three notices have been sent to the customer, and an InCollectionSpecification class that is satisfied when an invoice has already been sent to the collection agency. The implementation of these classes isn't important here.
Using these three specifications, we created a new specification called SendToCollection which will be satisfied when an invoice is overdue, when notices have been sent to the customer, and are not already with the collection agency.

References
Evans, Eric (2004). Domain Driven Design. Addison-Wesley. p. 224.

External links
Specifications by Eric Evans and Martin Fowler
The Specification Pattern: A Primer by Matt Berther
The Specification Pattern: A Four Part Introduction using VB.Net  by Richard Dalton
The Specification Pattern in PHP by Moshe Brevda
Happyr Doctrine Specification in PHP by Happyr
The Specification Pattern in Swift by Simon Strandgaard
The Specification Pattern in TypeScript and JavaScript by Thiago Delgado Pinto
specification pattern in flash actionscript 3 by Rolf Vreijdenberger

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
- [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra)
- [Bridge pattern](https://en.wikipedia.org/wiki/Bridge_pattern)
- [Broker pattern](https://en.wikipedia.org/wiki/Broker_pattern)
- [Builder pattern](https://en.wikipedia.org/wiki/Builder_pattern)
- [Business delegate pattern](https://en.wikipedia.org/wiki/Business_delegate_pattern)
- [Business rule](https://en.wikipedia.org/wiki/Business_rule)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
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
- [Domain-driven design](https://en.wikipedia.org/wiki/Domain-driven_design)
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
- [Memento pattern](https://en.wikipedia.org/wiki/Memento_pattern)
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
- [Publish–subscribe pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
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
- [State pattern](https://en.wikipedia.org/wiki/State_pattern)
- [Strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern)
- [Structural pattern](https://en.wikipedia.org/wiki/Structural_pattern)
- [Template method pattern](https://en.wikipedia.org/wiki/Template_method_pattern)
- [The Hillside Group](https://en.wikipedia.org/wiki/The_Hillside_Group)
- [Thread-local storage](https://en.wikipedia.org/wiki/Thread-local_storage)
- [Thread pool](https://en.wikipedia.org/wiki/Thread_pool)
- [Twin pattern](https://en.wikipedia.org/wiki/Twin_pattern)
- [TypeScript](https://en.wikipedia.org/wiki/TypeScript)
- [Shim (computing)](https://en.wikipedia.org/wiki/Shim_(computing))
- [Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)
- [Visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern)
- [Ward Cunningham](https://en.wikipedia.org/wiki/Ward_Cunningham)
- [Template:Design patterns](https://en.wikipedia.org/wiki/Template:Design_patterns)
- [Template talk:Design patterns](https://en.wikipedia.org/wiki/Template_talk:Design_patterns)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:45:14.095624+00:00_