# Ping-pong scheme

## Article Metadata

- **Last Updated:** 2024-12-14T19:42:54.188357+00:00
- **Original Article:** [Ping-pong scheme](https://en.wikipedia.org/wiki/Ping-pong_scheme)
- **Language:** en
- **Page ID:** 12242679

## Summary

Algorithms said to employ a ping-pong scheme exist in different fields of software engineering. They are characterized by an alternation between two entities. In the examples described below, these entities are communication partners, network paths or file blocks.

## Categories

- Category:Algorithms
- Category:All articles needing additional references
- Category:All articles with unsourced statements
- Category:Articles needing additional references from June 2010
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from October 2024
- Category:Short description matches Wikidata

## Table of Contents

- Databases
- Networking

## Content

Algorithms said to employ a ping-pong scheme exist in different fields of software engineering. They are characterized by an alternation between two entities. In the examples described below, these entities are communication partners, network paths or file blocks.

Databases
In most database management systems durable database transactions are supported through a log file. However, multiple writes to the same page of that file can produce a slim chance of data loss. Assuming for simplicity that the log file is organized in pages whose size matches the block size of its underlying medium, the following problem can occur:
If the very last page of the log file is only partially filled with data and has to be written to permanent storage in this state, the very same page will have to be overwritten during the next write operation. If a crash happens during that later write operation, previously stored log data may be lost.
The ping-pong scheme described in Transaction Processing eliminates this problem by alternately writing the contents of said (logical) last page to two different physical pages inside the log file (the actual last page i and its empty successor i+1). Once said logical log page is no longer the last page (i.e. it is completely filled with log data), it is written one last time to the regular physical position (i) inside the log file.
This scheme requires the usage of time stamps for each page in order to distinguish the most recent version of the logical last page one from its predecessor.

Networking
Internet
A functionality which lets a computer A find out whether a computer B is reachable and responding is built into the Internet Control Message Protocol (ICMP). Through an "Echo Request" Computer A asks B to send back an "Echo Reply". These two messages are also sometimes called "ping" and "pong" for historical purposes.

Routing
In routing, a Ping-Pong scheme is a simple algorithm for distributing data packets across two paths. If you had two paths A and B, then the algorithm would randomly start with one of the paths and then switch back and forth between the two.
If you were to get the next path from a function call, it would look like this in Python:


== References ==

## Related Articles

### Internal Links

- [Block (data storage)](https://en.wikipedia.org/wiki/Block_(data_storage))
- [Crash (computing)](https://en.wikipedia.org/wiki/Crash_(computing))
- [Database](https://en.wikipedia.org/wiki/Database)
- [Database transaction](https://en.wikipedia.org/wiki/Database_transaction)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Durability (database systems)](https://en.wikipedia.org/wiki/Durability_(database_systems))
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Internet Control Message Protocol](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol)
- [Ping (networking utility)](https://en.wikipedia.org/wiki/Ping_(networking_utility))
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Routing](https://en.wikipedia.org/wiki/Routing)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Software engineering](https://en.wikipedia.org/wiki/Software_engineering)
- [Transaction log](https://en.wikipedia.org/wiki/Transaction_log)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from June 2010](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_June_2010)
- [Category:Articles with unsourced statements from October 2024](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_October_2024)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:42:54.188357+00:00_