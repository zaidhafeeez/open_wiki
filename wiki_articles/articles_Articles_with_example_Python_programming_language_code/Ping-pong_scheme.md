# Ping-pong scheme

## Metadata
- **Last Updated:** 2024-12-03 07:10:39 UTC
- **Original Article:** [Ping-pong scheme](https://en.wikipedia.org/wiki/Ping-pong_scheme)
- **Language:** en
- **Page ID:** 12242679

## Summary
Algorithms said to employ a ping-pong scheme exist in different fields of software engineering. They are characterized by an alternation between two entities. In the examples described below, these entities are communication partners, network paths or file blocks.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 21:05:41 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2228 bytes
- **Word Count:** 377 words
