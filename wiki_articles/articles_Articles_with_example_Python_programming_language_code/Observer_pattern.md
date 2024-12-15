# Observer pattern

## Metadata
- **Last Updated:** 2024-12-03 06:51:58 UTC
- **Original Article:** [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern)
- **Language:** en
- **Page ID:** 164863

## Summary
In software design and engineering, the observer pattern is a software design pattern in which an object, named the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.
It is often used for implementing distributed event-handling systems in event-driven software. In such systems, the subject is usually named a "stream of events" or "stream source of events" while the observers are called "sinks of events." The stream nomenclature alludes to a physical setup in which the observers are physically separated and have no control over the emitted events from the subject/stream source. This pattern thus suits any process by which data arrives from some input that is not available to the CPU at startup, but instead may arrive at arbitrary or indeterminate times (HTTP requests, GPIO data, user input from peripherals and distributed databases, etc.).

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 20:38:35 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 8498 bytes
- **Word Count:** 1264 words
