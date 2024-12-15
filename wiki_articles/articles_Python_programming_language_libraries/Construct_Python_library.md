# Construct (Python library)

## Article Metadata

- **Last Updated:** 2024-12-15T03:25:37.561938+00:00
- **Original Article:** [Construct (Python library)](https://en.wikipedia.org/wiki/Construct_(Python_library))
- **Language:** en
- **Page ID:** 8583006

## Summary

Construct is a Python library for the construction and deconstruction of data structures in a declarative fashion. In this context, construction, or building, refers to the process of converting (serializing) a programmatic object into a binary representation. 
Deconstruction, or parsing, refers to the opposite process of converting (deserializing) binary data into a programmatic object. Being declarative means that user code defines the data structure, instead of the convention of writing proce

## Categories

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

## Related Articles

### Internal Links

- [Bit](https://en.wikipedia.org/wiki/Bit)
- [Byte](https://en.wikipedia.org/wiki/Byte)
- [CPAN](https://en.wikipedia.org/wiki/CPAN)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Data structure](https://en.wikipedia.org/wiki/Data_structure)
- [Declarative programming](https://en.wikipedia.org/wiki/Declarative_programming)
- [Endianness](https://en.wikipedia.org/wiki/Endianness)
- [Ethernet](https://en.wikipedia.org/wiki/Ethernet)
- [Ethernet frame](https://en.wikipedia.org/wiki/Ethernet_frame)
- [Internet Protocol](https://en.wikipedia.org/wiki/Internet_Protocol)
- [Natural Language Toolkit](https://en.wikipedia.org/wiki/Natural_Language_Toolkit)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Procedural programming](https://en.wikipedia.org/wiki/Procedural_programming)
- [Protocol stack](https://en.wikipedia.org/wiki/Protocol_stack)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Serialization](https://en.wikipedia.org/wiki/Serialization)
- [Internet protocol suite](https://en.wikipedia.org/wiki/Internet_protocol_suite)
- [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
- [Type conversion](https://en.wikipedia.org/wiki/Type_conversion)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Category:Articles with unsourced statements from August 2023](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_August_2023)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:25:37.561938+00:00_