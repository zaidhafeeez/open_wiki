# Memento pattern

## Metadata
- **Last Updated:** 2024-12-03 06:51:50 UTC
- **Original Article:** [Memento pattern](https://en.wikipedia.org/wiki/Memento_pattern)
- **Language:** en
- **Page ID:** 140542

## Summary
The memento pattern is a software design pattern that exposes the private internal state of an object.
One example of how this can be used is to restore an object to its previous state (undo via rollback), another is versioning, another is custom serialization.
The memento pattern is implemented with three objects: the originator, a caretaker and a memento. The originator is some object that has an internal state. The caretaker is going to do something to the originator, but wants to be able to undo the change. The caretaker first asks the originator for a memento object. Then it does whatever operation (or sequence of operations) it was going to do. To roll back to the state before the operations, it returns the memento object to the originator. The memento object itself is an opaque object (one which the caretaker cannot, or should not, change). When using this pattern, care should be taken if the originator may change other objects or resources—the memento pattern operates on a single object.
Classic examples of the memento pattern include a pseudorandom number generator (each consumer of the PRNG serves as a caretaker who can initialize the PRNG (the originator) with the same seed (the memento) to produce an identical sequence of pseudorandom numbers) and the state in a finite state machine.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 20:26:37 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 3777 bytes
- **Word Count:** 592 words
