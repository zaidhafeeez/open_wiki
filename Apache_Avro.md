# Apache Avro

_Last updated: 2024-12-14T15:09:07.797593_

**Original Article:** [Apache Avro](https://en.wikipedia.org/wiki/Apache_Avro)

**Summary:** Avro is a row-oriented remote procedure call and data serialization framework developed within Apache's Hadoop project. It uses JSON for defining data types and protocols, and serializes data in a compact binary format. Its primary use is in Apache Hadoop, where it can provide both a serialization format for persistent data, and a wire format for communication between Hadoop nodes, and from client programs to the Hadoop services.
Avro uses a schema to structure the data that is being encoded. It

## Categories
- Category:Apache Software Foundation projects
- Category:Application layer protocols
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Data serialization formats
- Category:Inter-process communication
- Category:Remote procedure call
- Category:Short description is different from Wikidata
- Category:Use mdy dates from April 2016

## Content

Avro is a row-oriented remote procedure call and data serialization framework developed within Apache's Hadoop project. It uses JSON for defining data types and protocols, and serializes data in a compact binary format. Its primary use is in Apache Hadoop, where it can provide both a serialization format for persistent data, and a wire format for communication between Hadoop nodes, and from client programs to the Hadoop services.
Avro uses a schema to structure the data that is being encoded. It has two different types of schema languages: one for human editing (Avro IDL) and another which is more machine-readable based on JSON.
It is similar to Thrift and Protocol Buffers, but does not require running a code-generation program when a schema changes (unless desired for statically-typed languages).
Apache Spark SQL can access Avro as a data source.

Avro Object Container File
An Avro Object Container File consists of: 

A file header, followed by
one or more file data blocks.
A file header consists of:

Four bytes, ASCII 'O', 'b', 'j', followed by the Avro version number which is 1 (0x01) (Binary values 0x4F 0x62 0x6A 0x01).
File metadata, including the schema definition.
The 16-byte, randomly-generated sync marker for this file.
For data blocks Avro specifies two serialization encodings: binary and JSON. Most applications will use the binary encoding, as it is smaller and faster.  For debugging and web-based applications, the JSON encoding may sometimes be appropriate.

Schema definition
Avro schemas are defined using JSON.  Schemas are composed of primitive types (null, boolean, int, long, float, double, bytes, and string) and complex types (record, enum, array, map, union, and fixed).
Simple schema example:

Serializing and deserializing
Data in Avro might be stored with its corresponding schema, meaning a serialized item can be read without knowing the schema ahead of time.

Example serialization and deserialization code in Python
Serialization:

File "users.avro" will contain the schema in JSON and a compact binary representation of the data:

Deserialization:

This outputs:

Languages with APIs
Though theoretically any language could use Avro, the following languages have APIs written for them:

C
C++
C#
Elixir
Go
Haskell
Java
Javascript
Perl
PHP
Python
Ruby
Rust
Scala

Avro IDL
In addition to supporting JSON for type and protocol definitions, Avro includes experimental support for an alternative interface description language (IDL) syntax known as Avro IDL.  Previously known as GenAvro, this format is designed to ease adoption by users familiar with more traditional IDLs and programming languages, with a syntax similar to C/C++, Protocol Buffers and others.

Logo
The original Apache Avro logo was from the defunct British aircraft manufacturer Avro (originally A.V. Roe and Company).
The Apache Avro logo was updated to an original design in late 2023.

See also
Comparison of data serialization formats
Apache Thrift
Protocol Buffers
Etch (protocol)
Internet Communications Engine
MessagePack
CBOR

References
Further reading
White, Tom (November 2010). Hadoop: The Definitive Guide. ISBN 978-1-4493-8973-4.