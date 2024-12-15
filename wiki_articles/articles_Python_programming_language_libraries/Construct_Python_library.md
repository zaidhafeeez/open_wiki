# Construct (Python library)

## Metadata
- **Last Updated:** 2024-11-22 02:59:11 UTC
- **Original Article:** [Construct (Python library)](https://en.wikipedia.org/wiki/Construct_(Python_library))
- **Language:** en
- **Page ID:** 8583006

## Summary
Construct is a Python library for the construction and deconstruction of data structures in a declarative fashion. In this context, construction, or building, refers to the process of converting (serializing) a programmatic object into a binary representation. 
Deconstruction, or parsing, refers to the opposite process of converting (deserializing) binary data into a programmatic object. Being declarative means that user code defines the data structure, instead of the convention of writing procedural code to accomplish the goal. Construct can work seamlessly with bit- and byte-level data granularity and various byte-ordering.

## Categories
This article belongs to the following categories:

- Category:All articles with unsourced statements
- Category:Articles with unsourced statements from August 2023
- Category:Parser generators
- Category:Python (programming language) libraries

## Table of Contents

- Benefits
- Example
- Ports and spin-offs
- See also
- References
- External links

## Content

Construct is a Python library for the construction and deconstruction of data structures in a declarative fashion. In this context, construction, or building, refers to the process of converting (serializing) a programmatic object into a binary representation. 
Deconstruction, or parsing, refers to the opposite process of converting (deserializing) binary data into a programmatic object. Being declarative means that user code defines the data structure, instead of the convention of writing procedural code to accomplish the goal. Construct can work seamlessly with bit- and byte-level data granularity and various byte-ordering.

Benefits
Using declarative code has many benefits. For example, the same code that can parse can also build (symmetrical), debugging and testing are much simpler (provable to some extent), creating new constructs is easy (wrapping components), and many more. If one is familiar with the C (programming language), one can think of constructs as casting from char * to struct foo * and vice versa, rather than writing code that unpacks the data.

Example
The following example show how a TCP/IP protocol stack might be defined using Construct. Some code is omitted for brevity and simplicity. Also note that the following code is just Python code that creates objects.
First, the Ethernet header (layer 2):

Next, the IP header (layer 3):

And finally, the TCP header (layer 4):

Now define the hierarchy of the protocol stack. The following code "binds" each pair of adjacent protocols into a separate unit. Each such unit will "select" the proper next layer based on its contained protocol.

At this point, the code can parse captured TCP/IP frames into "packet" objects and build these packet objects back into binary representation.

Ports and spin-offs
Perl
Data::ParseBinary is a CPAN module that originated as a port of Construct to the Perl programming language. (see its main POD document for its inspiration). Since the initial version, some parts of the original API have been deprecated.

Java
A port to Java is available on GitHub. Examples in Java, the Ethernet header (layer 2):

See also
Natural Language Toolkit

References
External links
Construct's Documentation
Construct's Repository
Python Training

## Archive Info
- **Archived on:** 2024-12-15 20:39:13 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2253 bytes
- **Word Count:** 347 words
