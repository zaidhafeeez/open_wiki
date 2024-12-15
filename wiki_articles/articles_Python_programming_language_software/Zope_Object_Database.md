# Zope Object Database

## Article Metadata

- **Last Updated:** 2024-12-15T04:22:27.605094+00:00
- **Original Article:** [Zope Object Database](https://en.wikipedia.org/wiki/Zope_Object_Database)
- **Language:** en
- **Page ID:** 2920295

## Summary

The Zope Object Database (ZODB) is an object-oriented database for transparently and persistently storing Python objects. It is included as part of the Zope web application server, but can also be used independently of Zope.
Features of the ZODB include: transactions, history/undo, transparently pluggable storage, built-in caching, multiversion concurrency control (MVCC), and scalability across a network (using ZEO).

## Categories

- Category:Cross-platform software
- Category:Free database management systems
- Category:ORDBMS software for Linux
- Category:Object-oriented database management systems
- Category:Python (programming language) software

## Table of Contents

- History
- Implementation
- ZEO
- References
- External links

## Content

The Zope Object Database (ZODB) is an object-oriented database for transparently and persistently storing Python objects. It is included as part of the Zope web application server, but can also be used independently of Zope.
Features of the ZODB include: transactions, history/undo, transparently pluggable storage, built-in caching, multiversion concurrency control (MVCC), and scalability across a network (using ZEO).

History
The Zope Object Database (ZODB) was created by Jim Fulton of Zope Corporation in the late 1990s. Initially, it began as a simple Persistent Object System (POS) during the development of Principia, which later evolved into Zope. A significant architectural change led to the renaming of the system to ZODB 3. Subsequently, ZODB 4 was introduced as a short-lived project aimed at re-implementing the entire ZODB 3 package using 100% Python.

Implementation
Basics
ZODB stores Python objects using an extended version of Python's built-in object persistence (pickle). A ZODB database has a single root object (normally a dictionary), which is the only object directly made accessible by the database. All other objects stored in the database are reached through the root object. Objects referenced by an object stored in the database are automatically stored in the database as well.
ZODB supports concurrent transactions using MVCC and tracks changes to objects on a per-object basis. Only changed objects are committed. Transactions are non-destructive by default and can be reverted.

Example
For example, say we have a car described using 3 classes Car, Wheel and Screw. In Python, this could be represented the following way:

If the variable mycar is the root of persistence, then:

This puts all of the object instances (car, wheel, screws etc.) into storage, which can be retrieved later. If another program gets a connection to the database through the mycar object, performing:

And retrieves all the objects, the pointer to the car being held in the car variable. Then at some later stage, this object can be altered with a Python code like:

The storage is altered to reflect the change of data (after a commit is ordered).
There is no declaration of the data structure in either Python or ZODB, so new fields can be freely added to any existing object.

Storage unit
For persistence to take place, the Python Car class must be derived from the Persistence.Persistent class — this class both holds the data necessary for the persistence machinery to work, such as the internal object id, state of the object, and so on, but also defines the boundary of the persistence in the following sense: every object whose class derives from Persistent is the atomic unit of storage (the whole object is copied to the storage when a field is modified).
In the example above, if Car is the only class deriving from Persistent, when wheel3 is added to car, all of the objects must be written to the storage. In contrast, if Wheel also derives from Persistent, then when carzz.wheel3 = Wheel is performed, a new record is written to the storage to hold the new value of the Car, but the existing Wheel are kept, and the new record for the Car points to the already existing Wheel record inside the storage.
The ZODB machinery doesn't chase modification down through the graph of pointers. In the example above, carzz.wheel3 = something is a modification automatically tracked down by the ZODB machinery, because carzz is of (Persistent) class Car. The ZODB machinery does this by marking the record as dirty. However, if there is a list, any change inside the list isn't noticed by the ZODB machinery, and the programmer must help by manually adding carzz._p_changed = 1, notifying ZODB that the record actually changed. Thus, to a certain extent the programmer must be aware of the working of the persistence machinery.

Atomicity
The storage unit (that is, an object whose class derives from Persistent) is also the atomicity unit. In the example above, if Cars is the only Persistent class, a thread modifies a Wheel (the Car record must be notified), and another thread modifies another Wheel inside another transaction, the second commit will fail. If Wheel is also Persistent, both Wheels can be modified independently by two different threads in two different transactions.

Class persistence
The class persistence—writing the class of a particular object into the storage—is obtained by writing a kind of "fully qualified" name of the class into each record on the disk. In Python, the name of the class involves the hierarchy of directory the source file of the class resides in. A consequence is that the source file of persisting object cannot be moved. If it is, the ZODB machinery is unable to locate the class of an object when retrieving it from the storage, resulting into a broken object.

ZEO
Zope Enterprise Objects (ZEO) is a ZODB storage implementation that allows multiple client processes to persist objects to a single ZEO server. This facilitates transparent scaling.

Pluggable storages
Network Storage (also known as ZEO) enables multiple Python processes to load and store persistent instances concurrently. File Storage allows a single Python process to interact with a file on disk. RelStorage enables the persistence backing store to be a RDBMS. Directory Storage stores each persistent data as a separate file on the filesystem, similar to FSFS in Subversion. Demo Storage serves as an in-memory backend for the persistent store. BDBStorage, now abandoned, used a Berkeley DB backend.

Failover technologies
Zope Replication Services (ZRS) is a commercial failover add-on, open-sourced since May 2013, that eliminates the single point of failure, providing hot backup for writes and load-balancing for reads. ZeoRAID is an open-source solution offering a proxy network server that distributes object stores and recovery across a series of network servers. RelStorage, by utilizing RDBMS technologies, eliminates the need for a ZEO server. NEO is a distributed storage implementation providing fault tolerance and load-balancing.

References
External links
ZODB Official Site
ZODB Book
ZODB programming guide
Introduction to the Zope Object Database

## Related Articles

### Internal Links

- [Apache Subversion](https://en.wikipedia.org/wiki/Apache_Subversion)
- [Application server](https://en.wikipedia.org/wiki/Application_server)
- [Atomicity (database systems)](https://en.wikipedia.org/wiki/Atomicity_(database_systems))
- [Berkeley DB](https://en.wikipedia.org/wiki/Berkeley_DB)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Failover](https://en.wikipedia.org/wiki/Failover)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Multiversion concurrency control](https://en.wikipedia.org/wiki/Multiversion_concurrency_control)
- [Object database](https://en.wikipedia.org/wiki/Object_database)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Relational database](https://en.wikipedia.org/wiki/Relational_database)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Zope](https://en.wikipedia.org/wiki/Zope)
- [Zope Public License](https://en.wikipedia.org/wiki/Zope_Public_License)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:22:27.605094+00:00_