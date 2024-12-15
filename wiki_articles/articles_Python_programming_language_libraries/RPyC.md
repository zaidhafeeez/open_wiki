# RPyC

## Metadata
- **Last Updated:** 2024-12-03 07:02:08 UTC
- **Original Article:** [RPyC](https://en.wikipedia.org/wiki/RPyC)
- **Language:** en
- **Page ID:** 4379735

## Summary
RPyC (pronounced are-pie-see), or Remote Python Call, is a Python library for remote procedure calls (RPC), as well as distributed computing. Unlike regular RPC mechanisms, such as ONC RPC, CORBA or Java RMI, RPyC is transparent, symmetric, and requires no special decoration or definition languages. Moreover, it provides programmatic access to any pythonic element, be it functions, classes, instances or modules.

## Categories
This article belongs to the following categories:

- Category:All articles lacking reliable references
- Category:Articles lacking reliable references from November 2009
- Category:Articles with short description
- Category:Python (programming language) libraries
- Category:Remote procedure call
- Category:Short description is different from Wikidata
- Category:Software using the MIT license

## Table of Contents

- Features
- Architecture
- Usage
- Demo
- History
- References
- External links

## Content

RPyC (pronounced are-pie-see), or Remote Python Call, is a Python library for remote procedure calls (RPC), as well as distributed computing. Unlike regular RPC mechanisms, such as ONC RPC, CORBA or Java RMI, RPyC is transparent, symmetric, and requires no special decoration or definition languages. Moreover, it provides programmatic access to any pythonic element, be it functions, classes, instances or modules.

Features
Symmetric—there is no difference between the client and the server—both can serve. The only different aspect is that the client is usually the side that initiates the action. Being symmetric, for example, allows the client to pass callback functions to the server.
Transparent—remote objects look and behave the same as local objects would.
Exceptions propagate like local ones
Allows for synchronous and asynchronous operation:
Synchronous operations return a NetProxy (see below)
Asynchronous operations return an AsyncResult, which is like promise objects
AsyncResults can be used as events
Threads are supported (though not recommended)
UNIX specific: server integration with inetd

Architecture
RPyC gives the programmer a slave python interpreter at his or her control. In this essence, RPyC is different from other RPCs, that require registration of resources prior to accessing them. As a result, using RPyC is much more straightforward, but this comes at the expense of security (you cannot limit access). RPyC is intended to be used within a trusted network, there are various schemes including VPN for achieving this.
Once a client is connected to the server, it has one of two ways to perform remote operations:

The modules property, that exposes the server's modules namespace: doc = conn.modules.sys.path or conn.modules["xml.dom.minidom"].parseString("<some>xml</some>").
The execute function, that executes the given code on the server: conn.execute("print 'hello world'")
Remote operations return something called a NetProxy, which is an intermediate object that reflects any operation performed locally on it to the remote object. For example, conn.modules.sys.path is a NetProxy for the sys.path object of the server. Any local changes done to conn.modules.sys.path are reflected immediately on the remote object.
Note: NetProxies are not used for simple objects, such as numbers and strings, which are immutable.
Async is a proxy wrapper, meaning, it takes a NetProxy and returns another that wraps it with asynchronous functionality. Operations done to an AsyncNetProxy return something called AsyncResult. These objects have a '.is_ready' predicate, '.result' property that holds the result (or blocks until it arrives), and '.on_ready' callback, which will be called when the result arrives.

Usage
Originally, RPyC was developed for managing distributed testing of products over a range of different platforms (all capable of running python). However, RPyC has evolved since then, and now its use cases include:

Distributed computing (splitting workload between machines)
Distributed testing (running tests that connect multiple platforms and abstracting hardware resources)
Remote administration (tweaking config files from one central place, etc.)
Tunneling or chaining (crossing over routable network boundaries)

Demo
History
RPyC is based on the work of Eyal Lotem (aka Lotex) on PyInvoke, which is no longer maintained. The first public release was 1.20, which allowed for symmetric and transparent RPC, but not for asynchronous operation. Version 1.6, while never publicly released, added the concept of 'events', as a means for the server to inform the client. Version 2.X, the first release of which was 2.2, added thread synchronization and the Async concept, which can be used as a superset of events. Version 2.40 adds the execute method, that can be used to execute code on the other side of the connection directly.
RPyC 3 is a complete rewrite of the library, adding a capability-based security model, explicit services, and various other improvements.

References
External links
Official website

## Archive Info
- **Archived on:** 2024-12-15 21:07:40 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 4069 bytes
- **Word Count:** 601 words
