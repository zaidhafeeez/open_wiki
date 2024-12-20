---
title: Command pattern
url: https://en.wikipedia.org/wiki/Command_pattern
language: en
categories: ["Category:All articles lacking in-text citations", "Category:All articles with dead external links", "Category:Articles lacking in-text citations from December 2012", "Category:Articles with dead external links from September 2023", "Category:Articles with example C Sharp code", "Category:Articles with example JavaScript code", "Category:Articles with example Java code", "Category:Articles with example Python (programming language) code", "Category:Articles with example Ruby code", "Category:Articles with example Scala code", "Category:Articles with short description", "Category:Commons category link from Wikidata", "Category:Short description matches Wikidata", "Category:Software design patterns"]
references: 0
last_modified: 2024-12-19T13:43:13Z
---

# Command pattern

## Summary

In object-oriented programming, the command pattern is a behavioral design pattern in which an object is used to encapsulate all information needed to perform an action or trigger an event at a later time. This information includes the method name, the object that owns the method and values for the method parameters.
Four terms always associated with the command pattern are command, receiver, invoker and client. A command object knows about receiver and invokes a method of the receiver. Values f

## Full Content

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
