# Command pattern

## Article Metadata

- **Last Updated:** 2024-12-15T04:08:18.468948+00:00
- **Original Article:** [Command pattern](https://en.wikipedia.org/wiki/Command_pattern)
- **Language:** en
- **Page ID:** 164858

## Summary

In object-oriented programming, the command pattern is a behavioral design pattern in which an object is used to encapsulate all information needed to perform an action or trigger an event at a later time. This information includes the method name, the object that owns the method and values for the method parameters.
Four terms always associated with the command pattern are command, receiver, invoker and client. A command object knows about receiver and invokes a method of the receiver. Values f

## Categories

- Category:All articles lacking in-text citations
- Category:All articles with dead external links
- Category:Articles lacking in-text citations from December 2012
- Category:Articles with dead external links from September 2023
- Category:Articles with example C Sharp code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Ruby code
- Category:Articles with example Scala code
- Category:Articles with short description
- Category:Commons category link from Wikidata
- Category:Short description matches Wikidata
- Category:Software design patterns

## Table of Contents

- Overview
- Structure
- Uses
- Terminology
- Example
- See also
- History
- References
- External links

## Content

In object-oriented programming, the command pattern is a behavioral design pattern in which an object is used to encapsulate all information needed to perform an action or trigger an event at a later time. This information includes the method name, the object that owns the method and values for the method parameters.
Four terms always associated with the command pattern are command, receiver, invoker and client. A command object knows about receiver and invokes a method of the receiver. Values for parameters of the receiver method are stored in the command.  The receiver object to execute these methods is also stored in the command object by aggregation. The receiver then does the work when the execute() method in command is called. An invoker object knows how to execute a command, and optionally does bookkeeping about the command execution. The invoker does not know anything about a concrete command, it knows only about the command interface. Invoker object(s), command objects and receiver objects are held by a client object. The client decides which receiver objects it assigns to the command objects, and which commands it assigns to the invoker. The client decides which commands to execute at which points. To execute a command, it passes the command object to the invoker object.
Using command objects makes it easier to construct general components that need to delegate, sequence or execute method calls at a time of their choosing without the need to know the class of the method or the method parameters. Using an invoker object allows bookkeeping about command executions to be conveniently performed, as well as implementing different modes for commands, which are managed by the invoker object, without the need for the client to be aware of the existence of bookkeeping or modes.
The central ideas of this design pattern closely mirror the semantics of first-class functions and higher-order functions in functional programming languages.  Specifically, the invoker object is a higher-order function of which the command object is a first-class argument.

Overview
The command
design pattern is one of the twenty-three well-known GoF design patterns that describe how to solve recurring design problems to design flexible and reusable object-oriented software, that is, objects that are easier to implement, change, test, and reuse.
Using the command design pattern can solve these problems:

Coupling the invoker of a request to a particular request should be avoided. That is, hard-wired requests should be avoided.
It should be possible to configure an object (that invokes a request) with a request.
Implementing (hard-wiring) a request directly into a class is inflexible because it couples the class to a particular request at compile-time, which makes it impossible to specify a request at run-time.
Using the command design pattern describes the following solution:

Define separate (command) objects that encapsulate a request.
A class delegates a request to a command object instead of implementing a particular request directly.
This enables one to configure a class with a command object that is used to perform a request. The class is no longer coupled to a particular request and has no knowledge (is independent) of how the request is carried out.
See also the UML class and sequence diagram below.

Structure
UML class and sequence diagram
In the above UML class diagram, the Invoker class doesn't implement a request directly.
Instead, Invoker refers to the Command interface to perform a request (command.execute()), which makes the Invoker independent of how the request is performed.
The Command1 class implements the Command interface by performing an action on a receiver (receiver1.action1()).
The UML sequence diagram
shows the run-time interactions: The Invoker object calls execute() on a Command1 object.
Command1 calls action1() on a Receiver1 object,
which performs the request.

UML class diagram
Uses
GUI buttons and menu items
In Swing and Borland Delphi programming, an Action is a command object. In addition to the ability to perform the desired command, an Action may have an associated icon, keyboard shortcut, tooltip text, and so on. A toolbar button or menu item component may be completely initialized using only the Action object.
Macro recording
If all user actions are represented by command objects, a program can record a sequence of actions simply by keeping a list of the command objects as they are executed. It can then "play back" the same actions by executing the same command objects again in sequence. If the program embeds a scripting engine, each command object can implement a toScript() method, and user actions can then be easily recorded as scripts.
Mobile code
Using languages such as Java where code can be streamed/slurped from one location to another via URLClassloaders and Codebases the commands can enable new behavior to be delivered to remote locations (EJB Command, Master Worker).
Multi-level undo
If all user actions in a program are implemented as command objects, the program can keep a stack of the most recently executed commands. When the user wants to undo a command, the program simply pops the most recent command object and executes its undo() method.
Networking
It is possible to send whole command objects across the network to be executed on the other machines, for example player actions in computer games.
Parallel processing
Where the commands are written as tasks to a shared resource and executed by many threads in parallel (possibly on remote machines; this variant is often referred to as the Master/Worker pattern)
Progress bars
Suppose a program has a sequence of commands that it executes in order. If each command object has a getEstimatedDuration() method, the program can easily estimate the total duration. It can show a progress bar that meaningfully reflects how close the program is to completing all the tasks.
Thread pools
A typical, general-purpose thread pool class might have a public addTask() method that adds a work item to an internal queue of tasks waiting to be done. It maintains a pool of threads that execute commands from the queue. The items in the queue are command objects. Typically these objects implement a common interface such as java.lang.Runnable that allows the thread pool to execute the command even though the thread pool class itself was written without any knowledge of the specific tasks for which it would be used.
Transactional behavior
Similar to undo, a database engine or software installer may keep a list of operations that have been or will be performed. Should one of them fail, all others can be reversed or discarded (usually called rollback). For example, if two database tables that refer to each other must be updated, and the second update fails, the transaction can be rolled back, so that the first table does not now contain an invalid reference.
Wizards
Often a wizard presents several pages of configuration for a single action that happens only when the user clicks the "Finish" button on the last page. In these cases, a natural way to separate user interface code from application code is to implement the wizard using a command object. The command object is created when the wizard is first displayed. Each wizard page stores its GUI changes in the command object, so the object is populated as the user progresses. "Finish" simply triggers a call to execute(). This way, the command class will work.

Terminology
The terminology used to describe command pattern implementations is not consistent and can therefore be confusing.
This is the result of ambiguity, the use of synonyms, and implementations that may obscure the original pattern by going well beyond it.

Ambiguity.
The term command is ambiguous. For example, move up, move up may refer to a single (move up) command that should be executed twice, or it may refer to two commands, each of which happens to do the same thing (move up). If the former command is added twice to an undo stack, both items on the stack refer to the same command instance. This may be appropriate when a command can always be undone the same way (e.g. move down). Both the Gang of Four and the Java example below use this interpretation of the term command. On the other hand, if the latter commands are added to an undo stack, the stack refers to two separate objects. This may be appropriate when each object on the stack must contain information that allows the command to be undone. For example, to undo a delete selection command, the object may contain a copy of the deleted text so that it can be re-inserted, if the delete selection command must be undone. Note that using a separate object for each invocation of a command is also an example of the chain of responsibility pattern.
The term execute is also ambiguous. It may refer to running the code identified by the command object's execute method. However, in Microsoft's Windows Presentation Foundation a command is considered to have been executed when the command's execute method has been invoked, but that does not necessarily mean that the application code has run. That occurs only after some further event processing.
Synonyms and homonyms.
Client, Source, Invoker: the button, toolbar button, or menu item clicked, the shortcut key pressed by the user.
Command Object, Routed Command Object, Action Object: a singleton object (e.g. there is only one CopyCommand object), which knows about shortcut keys, button images, command text, etc. related to the command. A source or invoker object calls the Command or Action object's execute or performAction method. The Command/Action object notifies the appropriate source/invoker objects when the availability of a command/action has changed. This allows buttons and menu items to become inactive (grayed out) when a command/action cannot be executed/performed.
Receiver, Target Object: the object that is about to be copied, pasted, moved, etc. The receiver object owns the method that is called by the command's execute method. The receiver is typically also the target object. For example, if the receiver object is a cursor and the method is called moveUp, then one would expect that the cursor is the target of the moveUp action. On the other hand, if the code is defined by the command object itself, the target object will be a different object entirely.
Command Object, routed event arguments, event object: the object that is passed from the source to the Command/Action object, to the Target object to the code that does the work. Each button click or shortcut key results in a new command/event object. Some implementations add more information to the command/event object as it is being passed from one object (e.g. CopyCommand) to another (e.g. document section). Other implementations put command/event objects in other event objects (like a box inside a bigger box) as they move along the line, to avoid naming conflicts. (See also chain of responsibility pattern.)
Handler, ExecutedRoutedEventHandler, method, function: the actual code that does the copying, pasting, moving, etc. In some implementations the handler code is part of the command/action object. In other implementations the code is part of the Receiver/Target Object, and in yet other implementations the handler code is kept separate from the other objects.
Command Manager, Undo Manager, Scheduler, Queue, Dispatcher, Invoker: an object that puts command/event objects on an undo stack or redo stack, or that holds on to command/event objects until other objects are ready to act on them, or that routes the command/event objects to the appropriate receiver/target object or handler code.
Implementations that go well beyond the original command pattern.
Microsoft's Windows Presentation Foundation (WPF), introduces routed commands, which combine the command pattern with event processing. As a result, the command object no longer contains a reference to the target object nor a reference to the application code. Instead, invoking the command object's execute command results in a so-called Executed Routed Event that during the event's tunneling or bubbling may encounter a so-called binding object that identifies the target and the application code, which is executed at that point.

Example
This C++14 implementation is based on the pre C++98 implementation in the book.

The program output is

See also
Batch queue
Closure
Command queue
Function object
Job scheduler
Model–view–controller
Priority queue
Software design pattern
Design Patterns (book)

History
The first published mention of using a Command class to implement interactive systems seems to be a 1985 article by Henry Lieberman. The first published description of a (multiple-level) undo-redo mechanism, using a Command class with execute and undo methods, and a history list, appears to be the first (1988) edition of Bertrand Meyer's book Object-oriented Software Construction, section 12.2.

References
External links

Command Pattern
Java Tip 68: Learn how to implement the Command pattern in Java

## Related Articles

### Internal Links

- [Abstract factory pattern](https://en.wikipedia.org/wiki/Abstract_factory_pattern)
- [Action–domain–responder](https://en.wikipedia.org/wiki/Action%E2%80%93domain%E2%80%93responder)
- [Active object](https://en.wikipedia.org/wiki/Active_object)
- [Active record pattern](https://en.wikipedia.org/wiki/Active_record_pattern)
- [Adapter pattern](https://en.wikipedia.org/wiki/Adapter_pattern)
- [Ambiguity](https://en.wikipedia.org/wiki/Ambiguity)
- [Anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern)
- [Architectural pattern](https://en.wikipedia.org/wiki/Architectural_pattern)
- [Asynchronous method invocation](https://en.wikipedia.org/wiki/Asynchronous_method_invocation)
- [Balking pattern](https://en.wikipedia.org/wiki/Balking_pattern)
- [Job queue](https://en.wikipedia.org/wiki/Job_queue)
- [Behavioral pattern](https://en.wikipedia.org/wiki/Behavioral_pattern)
- [Bertrand Meyer](https://en.wikipedia.org/wiki/Bertrand_Meyer)
- [Binding properties pattern](https://en.wikipedia.org/wiki/Binding_properties_pattern)
- [Blackboard (design pattern)](https://en.wikipedia.org/wiki/Blackboard_(design_pattern))
- [Borland](https://en.wikipedia.org/wiki/Borland)
- [Bridge pattern](https://en.wikipedia.org/wiki/Bridge_pattern)
- [Broker pattern](https://en.wikipedia.org/wiki/Broker_pattern)
- [Builder pattern](https://en.wikipedia.org/wiki/Builder_pattern)
- [Business delegate pattern](https://en.wikipedia.org/wiki/Business_delegate_pattern)
- [Chain-of-responsibility pattern](https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern)
- [Chain-of-responsibility pattern](https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern)
- [Christopher Alexander](https://en.wikipedia.org/wiki/Christopher_Alexander)
- [Class diagram](https://en.wikipedia.org/wiki/Class_diagram)
- [Closure (computer programming)](https://en.wikipedia.org/wiki/Closure_(computer_programming))
- [Code mobility](https://en.wikipedia.org/wiki/Code_mobility)
- [Command queue](https://en.wikipedia.org/wiki/Command_queue)
- [Composite entity pattern](https://en.wikipedia.org/wiki/Composite_entity_pattern)
- [Composite pattern](https://en.wikipedia.org/wiki/Composite_pattern)
- [Concurrency pattern](https://en.wikipedia.org/wiki/Concurrency_pattern)
- [Creational pattern](https://en.wikipedia.org/wiki/Creational_pattern)
- [Data access object](https://en.wikipedia.org/wiki/Data_access_object)
- [Data transfer object](https://en.wikipedia.org/wiki/Data_transfer_object)
- [Database transaction](https://en.wikipedia.org/wiki/Database_transaction)
- [Decorator pattern](https://en.wikipedia.org/wiki/Decorator_pattern)
- [Delegation pattern](https://en.wikipedia.org/wiki/Delegation_pattern)
- [Delphi (software)](https://en.wikipedia.org/wiki/Delphi_(software))
- [Dependency injection](https://en.wikipedia.org/wiki/Dependency_injection)
- [Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns)
- [Software design pattern](https://en.wikipedia.org/wiki/Software_design_pattern)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Double-checked locking](https://en.wikipedia.org/wiki/Double-checked_locking)
- [Douglas C. Schmidt](https://en.wikipedia.org/wiki/Douglas_C._Schmidt)
- [Enterprise Integration Patterns](https://en.wikipedia.org/wiki/Enterprise_Integration_Patterns)
- [Entity component system](https://en.wikipedia.org/wiki/Entity_component_system)
- [Erich Gamma](https://en.wikipedia.org/wiki/Erich_Gamma)
- [Facade pattern](https://en.wikipedia.org/wiki/Facade_pattern)
- [Factory method pattern](https://en.wikipedia.org/wiki/Factory_method_pattern)
- [First-class function](https://en.wikipedia.org/wiki/First-class_function)
- [Flyweight pattern](https://en.wikipedia.org/wiki/Flyweight_pattern)
- [Front controller](https://en.wikipedia.org/wiki/Front_controller)
- [Function object](https://en.wikipedia.org/wiki/Function_object)
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns)
- [Grady Booch](https://en.wikipedia.org/wiki/Grady_Booch)
- [Guarded suspension](https://en.wikipedia.org/wiki/Guarded_suspension)
- [Higher-order function](https://en.wikipedia.org/wiki/Higher-order_function)
- [Homonym](https://en.wikipedia.org/wiki/Homonym)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Identity map pattern](https://en.wikipedia.org/wiki/Identity_map_pattern)
- [Information hiding](https://en.wikipedia.org/wiki/Information_hiding)
- [Intercepting filter pattern](https://en.wikipedia.org/wiki/Intercepting_filter_pattern)
- [Interceptor pattern](https://en.wikipedia.org/wiki/Interceptor_pattern)
- [Interpreter pattern](https://en.wikipedia.org/wiki/Interpreter_pattern)
- [Inversion of control](https://en.wikipedia.org/wiki/Inversion_of_control)
- [Iterator pattern](https://en.wikipedia.org/wiki/Iterator_pattern)
- [JSP model 2 architecture](https://en.wikipedia.org/wiki/JSP_model_2_architecture)
- [Jim Coplien](https://en.wikipedia.org/wiki/Jim_Coplien)
- [Job scheduler](https://en.wikipedia.org/wiki/Job_scheduler)
- [John Vlissides](https://en.wikipedia.org/wiki/John_Vlissides)
- [Join-pattern](https://en.wikipedia.org/wiki/Join-pattern)
- [Kent Beck](https://en.wikipedia.org/wiki/Kent_Beck)
- [Lazy loading](https://en.wikipedia.org/wiki/Lazy_loading)
- [Linda Rising](https://en.wikipedia.org/wiki/Linda_Rising)
- [Lock (computer science)](https://en.wikipedia.org/wiki/Lock_(computer_science))
- [Macro (computer science)](https://en.wikipedia.org/wiki/Macro_(computer_science))
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
- [Object-Oriented Software Construction](https://en.wikipedia.org/wiki/Object-Oriented_Software_Construction)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object composition](https://en.wikipedia.org/wiki/Object_composition)
- [Object pool pattern](https://en.wikipedia.org/wiki/Object_pool_pattern)
- [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern)
- [Portland Pattern Repository](https://en.wikipedia.org/wiki/Portland_Pattern_Repository)
- [Priority queue](https://en.wikipedia.org/wiki/Priority_queue)
- [Proactor pattern](https://en.wikipedia.org/wiki/Proactor_pattern)
- [Progress bar](https://en.wikipedia.org/wiki/Progress_bar)
- [Prototype pattern](https://en.wikipedia.org/wiki/Prototype_pattern)
- [Proxy pattern](https://en.wikipedia.org/wiki/Proxy_pattern)
- [Publish–subscribe pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
- [Ralph Johnson (computer scientist)](https://en.wikipedia.org/wiki/Ralph_Johnson_(computer_scientist))
- [Reactor pattern](https://en.wikipedia.org/wiki/Reactor_pattern)
- [Readers–writer lock](https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock)
- [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin)
- [Scheduled-task pattern](https://en.wikipedia.org/wiki/Scheduled-task_pattern)
- [Scheduling (computing)](https://en.wikipedia.org/wiki/Scheduling_(computing))
- [Semaphore (programming)](https://en.wikipedia.org/wiki/Semaphore_(programming))
- [Sequence diagram](https://en.wikipedia.org/wiki/Sequence_diagram)
- [Servant (design pattern)](https://en.wikipedia.org/wiki/Servant_(design_pattern))
- [Service locator pattern](https://en.wikipedia.org/wiki/Service_locator_pattern)
- [Singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern)
- [Software design pattern](https://en.wikipedia.org/wiki/Software_design_pattern)
- [Specification pattern](https://en.wikipedia.org/wiki/Specification_pattern)
- [State pattern](https://en.wikipedia.org/wiki/State_pattern)
- [Strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern)
- [Structural pattern](https://en.wikipedia.org/wiki/Structural_pattern)
- [Swing (Java)](https://en.wikipedia.org/wiki/Swing_(Java))
- [Synonym](https://en.wikipedia.org/wiki/Synonym)
- [Template method pattern](https://en.wikipedia.org/wiki/Template_method_pattern)
- [The Hillside Group](https://en.wikipedia.org/wiki/The_Hillside_Group)
- [Thread-local storage](https://en.wikipedia.org/wiki/Thread-local_storage)
- [Thread pool](https://en.wikipedia.org/wiki/Thread_pool)
- [Twin pattern](https://en.wikipedia.org/wiki/Twin_pattern)
- [Shim (computing)](https://en.wikipedia.org/wiki/Shim_(computing))
- [Undo](https://en.wikipedia.org/wiki/Undo)
- [Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)
- [Visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern)
- [Ward Cunningham](https://en.wikipedia.org/wiki/Ward_Cunningham)
- [Windows Presentation Foundation](https://en.wikipedia.org/wiki/Windows_Presentation_Foundation)
- [Wizard (software)](https://en.wikipedia.org/wiki/Wizard_(software))
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:External links](https://en.wikipedia.org/wiki/Wikipedia:External_links)
- [Wikipedia:Further reading](https://en.wikipedia.org/wiki/Wikipedia:Further_reading)
- [Wikipedia:Link rot](https://en.wikipedia.org/wiki/Wikipedia:Link_rot)
- [Wikipedia:When to cite](https://en.wikipedia.org/wiki/Wikipedia:When_to_cite)
- [Wikipedia:WikiProject Reliability](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Reliability)
- [Template:Design patterns](https://en.wikipedia.org/wiki/Template:Design_patterns)
- [Template talk:Design patterns](https://en.wikipedia.org/wiki/Template_talk:Design_patterns)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles lacking in-text citations from December 2012](https://en.wikipedia.org/wiki/Category:Articles_lacking_in-text_citations_from_December_2012)
- [Category:Articles with dead external links from September 2023](https://en.wikipedia.org/wiki/Category:Articles_with_dead_external_links_from_September_2023)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:08:18.468948+00:00_