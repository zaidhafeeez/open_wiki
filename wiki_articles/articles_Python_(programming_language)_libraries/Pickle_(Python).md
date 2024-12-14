# Serialization

## Article Metadata

- **Last Updated:** 2024-12-14T19:50:54.470402+00:00
- **Original Article:** [Serialization](https://en.wikipedia.org/wiki/Serialization)
- **Language:** en
- **Page ID:** 28555

## Summary

In computing, serialization (or serialisation, also referred to as pickling in Python) is the process of translating a data structure or object state into a format that can be stored (e.g. files in secondary storage devices, data buffers in primary storage devices) or transmitted (e.g. data streams over computer networks) and reconstructed later (possibly in a different computer environment). When the resulting series of bits is reread according to the serialization format, it can be used to cre

## Categories

- Category:Articles with short description
- Category:Data serialization formats
- Category:Persistence
- Category:Short description is different from Wikidata
- Category:Webarchive template wayback links
- Category:Wikipedia external links cleanup from August 2024

## Table of Contents

- Uses
- Drawbacks
- Serialization formats
- Programming language support
- See also
- References
- External links

## Content

In computing, serialization (or serialisation, also referred to as pickling in Python) is the process of translating a data structure or object state into a format that can be stored (e.g. files in secondary storage devices, data buffers in primary storage devices) or transmitted (e.g. data streams over computer networks) and reconstructed later (possibly in a different computer environment). When the resulting series of bits is reread according to the serialization format, it can be used to create a semantically identical clone of the original object. For many complex objects, such as those that make extensive use of references, this process is not straightforward. Serialization of objects does not include any of their associated methods with which they were previously linked.
This process of serializing an object is also called marshalling an object in some situations. The opposite operation, extracting a data structure from a series of bytes, is deserialization, (also called unserialization or unmarshalling).
In networking equipment hardware, the part that is responsible for serialization and deserialization is commonly called SerDes.

Uses
Uses of serialization include:

serializing data for transfer across wires and networks (messaging).
storing data (in databases, on hard disk drives).
remote procedure calls, e.g., as in SOAP.
distributing objects, especially in component-based software engineering such as COM, CORBA, etc.
detecting changes in time-varying data.
For some of these features to be useful, architecture independence must be maintained. For example, for maximal use of distribution, a computer running on a different hardware architecture should be able to reliably reconstruct a serialized data stream, regardless of endianness. This means that the simpler and faster procedure of directly copying the memory layout of the data structure cannot work reliably for all architectures. Serializing the data structure in an architecture-independent format means preventing the problems of byte ordering, memory layout, or simply different ways of representing data structures in different programming languages.
Inherent to any serialization scheme is that, because the encoding of the data is by definition serial, extracting one part of the serialized data structure requires that the entire object be read from start to end, and reconstructed. In many applications, this linearity is an asset, because it enables simple, common I/O interfaces to be utilized to hold and pass on the state of an object. In applications where higher performance is an issue, it can make sense to expend more effort to deal with a more complex, non-linear storage organization.
Even on a single machine, primitive pointer objects are too fragile to save because the objects to which they point may be reloaded to a different location in memory. To deal with this, the serialization process includes a step called unswizzling or pointer unswizzling, where direct pointer references are converted to references based on name or position. The deserialization process includes an inverse step called pointer swizzling.
Since both serializing and deserializing can be driven from common code (for example, the Serialize function in Microsoft Foundation Classes), it is possible for the common code to do both at the same time, and thus, 1) detect differences between the objects being serialized and their prior copies, and 2) provide the input for the next such detection.  It is not necessary to actually build the prior copy because differences can be detected on the fly, a technique called differential execution. This is useful in the programming of user interfaces whose contents are time-varying — graphical objects can be created, removed, altered, or made to handle input events without necessarily having to write separate code to do those things.

Drawbacks
Serialization breaks the opacity of an abstract data type by potentially exposing private implementation details. Trivial implementations which serialize all data members may violate encapsulation.
To discourage competitors from making compatible products, publishers of proprietary software often keep the details of their programs' serialization formats a trade secret. Some deliberately obfuscate or even encrypt the serialized data. Yet, interoperability requires that applications be able to understand each other's serialization formats. Therefore, remote method call architectures such as CORBA define their serialization formats in detail.
Many institutions, such as archives and libraries, attempt to future proof their backup archives—in particular, database dumps—by storing them in some relatively human-readable serialized format.

Serialization formats
The Xerox Network Systems Courier technology in the early 1980s influenced the first widely adopted standard. Sun Microsystems published the External Data Representation (XDR) in 1987. XDR is an open format, and standardized as STD 67 (RFC 4506).
In the late 1990s, a push to provide an alternative to the standard serialization protocols started: XML, an SGML subset, was used to produce a human-readable text-based encoding. Such an encoding can be useful for persistent objects that may be read and understood by humans, or communicated to other systems regardless of programming language. It has the disadvantage of losing the more compact, byte-stream-based encoding, but by this point larger storage and transmission capacities made file size less of a concern than in the early days of computing. In the 2000s, XML was often used for asynchronous transfer of structured data between client and server in Ajax web applications. XML is an open format, and standardized as a W3C recommendation.
JSON is a lightweight plain-text alternative to XML, and is also commonly used for client-server communication in web applications. JSON is based on JavaScript syntax, but is independent of JavaScript and supported in many other programming languages. JSON is an open format, standardized as STD 90 (RFC 8259), ECMA-404, and ISO/IEC 21778:2017.
YAML is a strict superset of JSON and includes additional features such as a data type tags, support for cyclic data structures, indentation-sensitive syntax, and multiple forms of scalar data quoting. YAML is an open format.
Property lists are used for serialization by NeXTSTEP, GNUstep, macOS, and iOS frameworks. Property list, or p-list for short, doesn't refer to a single serialization format but instead several different variants, some human-readable and one binary.
For large volume scientific datasets, such as satellite data and output of numerical climate, weather, or ocean models, specific binary serialization standards have been developed, e.g. HDF, netCDF and the older GRIB.

Programming language support
Several object-oriented programming languages directly support object serialization (or object archival), either by syntactic sugar elements or providing a standard interface for doing so. The languages which do so include Ruby, Smalltalk, Python, PHP, Objective-C, Delphi, Java, and the .NET family of languages. There are also libraries available that add serialization support to languages that lack native support for it.

C and C++
C and C++ do not provide serialization as any sort of high-level construct, but both languages support writing any of the built-in data types, as well as plain old data structs, as binary data. As such, it is usually trivial to write custom serialization functions. Moreover, compiler-based solutions, such as the ODB ORM system for C++ and the gSOAP toolkit for C and C++, are capable of automatically producing serialization code with few or no modifications to class declarations. Other popular serialization frameworks are Boost.Serialization from the Boost Framework, the S11n framework, and Cereal. MFC framework (Microsoft) also provides serialization methodology as part of its Document-View architecture.

CFML
CFML allows data structures to be serialized to WDDX with the <cfwddx> tag and to JSON with the SerializeJSON() function.

Delphi
Delphi provides a built-in mechanism for serialization of components (also called persistent objects), which is fully integrated with its IDE. The component's contents are saved to a DFM file and reloaded on-the-fly.

Go
Go natively supports unmarshalling/marshalling of JSON and XML data. There are also third-party modules that support YAML and Protocol Buffers. Go also supports Gobs.

Haskell
In Haskell, serialization is supported for types that are members of the Read and Show type classes. Every type that is a member of the Read type class defines a function that will extract the data from the string representation of the dumped data. The Show type class, in turn, contains the show function from which a string representation of the object can be generated. The programmer need not define the functions explicitly—merely declaring a type to be deriving Read or deriving Show, or both, can make the compiler generate the appropriate functions for many cases (but not all: function types, for example, cannot automatically derive Show or Read). The auto-generated instance for Show also produces valid source code, so the same Haskell value can be generated by running the code produced by show in, for example, a Haskell interpreter. For more efficient serialization, there are haskell libraries that allow high-speed serialization in binary format, e.g. binary.

Java
Java provides automatic serialization which requires that the object be marked by implementing the java.io.Serializable interface. Implementing the interface marks the class as "okay to serialize", and Java then handles serialization internally. There are no serialization methods defined on the Serializable interface, but a serializable class can optionally define methods with certain special names and signatures that if defined, will be called as part of the serialization/deserialization process. The language also allows the developer to override the serialization process more thoroughly by implementing another interface, the Externalizable interface, which includes two special methods that are used to save and restore the object's state. There are three primary reasons why objects are not serializable by default and must implement the Serializable interface to access Java's serialization mechanism.Firstly, not all objects capture useful semantics in a serialized state. For example, a Thread object is tied to the state of the current JVM. There is no context in which a deserialized Thread object would maintain useful semantics.Secondly, the serialized state of an object forms part of its class' compatibility contract. Maintaining compatibility between versions of serializable classes requires additional effort and consideration. Therefore, making a class serializable needs to be a deliberate design decision and not a default condition.Lastly, serialization allows access to non-transient private members of a class that are not otherwise accessible. Classes containing sensitive information (for example, a password) should not be serializable nor externalizable.: 339–345  The standard encoding method uses a recursive graph-based translation of the object's class descriptor and serializable fields into a byte stream. Primitives as well as non-transient, non-static referenced objects are encoded into the stream. Each object that is referenced by the serialized object via a field that is not marked as transient must also be serialized; and if any object in the complete graph of non-transient object references is not serializable, then serialization will fail. The developer can influence this behavior by marking objects as transient, or by redefining the serialization for an object so that some portion of the reference graph is truncated and not serialized. Java does not use constructor to serialize objects. It is possible to serialize Java objects through JDBC and store them into a database. While Swing components do implement the Serializable interface, they are not guaranteed to be portable between different versions of the Java Virtual Machine. As such, a Swing component, or any component which inherits it, may be serialized to a byte stream, but it is not guaranteed that this will be re-constitutable on another machine.

JavaScript
Since ECMAScript 5.1, JavaScript has included the built-in JSON object and its methods JSON.parse() and JSON.stringify(). Although JSON is originally based on a subset of JavaScript, there are boundary cases where JSON is not valid JavaScript. Specifically, JSON allows the Unicode line terminators U+2028  LINE SEPARATOR and U+2029  PARAGRAPH SEPARATOR to appear unescaped in quoted strings, while ECMAScript 2018 and older does not. See the main article on JSON.

Julia
Julia implements serialization through the serialize() / deserialize() modules, intended to work within the same version of Julia, and/or instance of the same system image. The HDF5.jl package offers a more stable alternative, using a documented format and common library with wrappers for different languages, while the default serialization format is suggested to have been designed rather with maximal performance for network communication in mind.

Lisp
Generally a Lisp data structure can be serialized with the functions "read" and "print". A variable foo containing, for example, a list of arrays would be printed by (print foo). Similarly an object can be read from a stream named s by (read s). These two parts of the Lisp implementation are called the Printer and the Reader. The output of "print" is human readable; it uses lists demarked by parentheses, for example: (4 2.9 "x" y). In many types of Lisp, including Common Lisp, the printer cannot represent every type of data because it is not clear how to do so. In Common Lisp for example the printer cannot print CLOS objects. Instead the programmer may write a method on the generic function print-object, this will be invoked when the object is printed. This is somewhat similar to the method used in Ruby. Lisp code itself is written in the syntax of the reader, called read syntax. Most languages use separate and different parsers to deal with code and data, Lisp only uses one. A file containing lisp code may be read into memory as a data structure, transformed by another program, then possibly executed or written out, such as in a read–eval–print loop. Not all readers/writers support cyclic, recursive or shared structures.

.NET
.NET has several serializers designed by Microsoft. There are also many serializers by third parties. More than a dozen serializers are discussed and tested here. and here

OCaml
OCaml's standard library provides marshalling through the Marshal module and the Pervasives functions output_value and input_value. While OCaml programming is statically type-checked, uses of the Marshal module may break type guarantees, as there is no way to check whether an unmarshalled stream represents objects of the expected type. In OCaml it is difficult to marshal a function or a data structure which contains a function (e.g. an object which contains a method), because executable code in functions cannot be transmitted across different programs. (There is a flag to marshal the code position of a function but it can only be unmarshalled in exactly the same program). The standard marshalling functions can preserve sharing and handle cyclic data, which can be configured by a flag.

Perl
Several Perl modules available from CPAN provide serialization mechanisms, including Storable , JSON::XS and FreezeThaw. Storable includes functions to serialize and deserialize Perl data structures to and from files or Perl scalars. In addition to serializing directly to files, Storable includes the freeze function to return a serialized copy of the data packed into a scalar, and thaw to deserialize such a scalar. This is useful for sending a complex data structure over a network socket or storing it in a database. When serializing structures with Storable, there are network safe functions that always store their data in a format that is readable on any computer at a small cost of speed. These functions are named nstore, nfreeze, etc. There are no "n" functions for deserializing these structures — the regular thaw and retrieve deserialize structures serialized with the "n" functions and their machine-specific equivalents.

PHP
PHP originally implemented serialization through the built-in serialize() and unserialize() functions. PHP can serialize any of its data types except resources (file pointers, sockets, etc.). The built-in unserialize() function is often dangerous when used on completely untrusted data. For objects, there are two "magic methods" that can be implemented within a class — __sleep() and __wakeup() — that are called from within serialize() and unserialize(), respectively, that can clean up and restore an object. For example, it may be desirable to close a database connection on serialization and restore the connection on deserialization; this functionality would be handled in these two magic methods. They also permit the object to pick which properties are serialized. Since PHP 5.1, there is an object-oriented serialization mechanism for objects, the Serializable interface.

Prolog
Prolog's term structure, which is the only data structure of the language, can be serialized out through the built-in predicate write_term/3 and serialized-in through the built-in predicates read/1 and read_term/2. The resulting stream is uncompressed text (in some encoding determined by configuration of the target stream), with any free variables in the term represented by placeholder variable names. The predicate write_term/3 is standardized in the ISO Specification for Prolog (ISO/IEC 13211-1) on pages 59 ff. ("Writing a term, § 7.10.5"). Therefore it is expected that terms serialized-out by one implementation can be serialized-in by another without ambiguity or surprises. In practice, implementation-specific extensions (e.g. SWI-Prolog's dictionaries) may use non-standard term structures, so interoperability may break in edge cases. As examples, see the corresponding manual pages for SWI-Prolog, SICStus Prolog, GNU Prolog. Whether and how serialized terms received over the network are checked against a specification (after deserialization from the character stream has happened) is left to the implementer. Prolog's built-in Definite Clause Grammars can be applied at that stage.

Python
The core general serialization mechanism is the pickle standard library module, alluding to the database systems term pickling to describe data serialization (unpickling for deserializing). Pickle uses a simple stack-based virtual machine that records the instructions used to reconstruct the object. It is a cross-version customisable but unsafe (not secure against erroneous or malicious data) serialization format. Malformed or maliciously constructed data, may cause the deserializer to import arbitrary modules and instantiate any object. The standard library also includes modules serializing to standard data formats: json (with built-in support for basic scalar and collection types and able to support arbitrary types via encoding and decoding hooks). plistlib (with support for both binary and XML property list formats). xdrlib (with support for the External Data Representation (XDR) standard as described in RFC 1014). Finally, it is recommended that an object's __repr__ be evaluable in the right environment, making it a rough match for Common Lisp's print-object. Not all object types can be pickled automatically, especially ones that hold operating system resources like file handles, but users can register custom "reduction" and construction functions to support the pickling and unpickling of arbitrary types. Pickle was originally implemented as the pure Python pickle module, but, in versions of Python prior to 3.0, the cPickle module (also a built-in) offers improved performance (up to 1000 times faster). The cPickle was adapted from the Unladen Swallow project. In Python 3, users should always import the standard version, which attempts to import the accelerated version and falls back to the pure Python version.

R
R has the function dput which writes an ASCII text representation of an R object to a file or connection. A representation can be read from a file using dget. More specific, the function serialize serializes an R object to a connection, the output being a raw vector coded in hexadecimal format. The unserialize function allows to read an object from a connection or a raw vector.

REBOL
REBOL will serialize to file (save/all) or to a string! (mold/all). Strings and files can be deserialized using the polymorphic load function. RProtoBuf provides cross-language data serialization in R, using Protocol Buffers.

Ruby
Ruby includes the standard module Marshal with 2 methods dump and load, akin to the standard Unix utilities dump and restore. These methods serialize to the standard class String, that is, they effectively become a sequence of bytes. Some objects cannot be serialized (doing so would raise a TypeError exception): bindings, procedure objects, instances of class IO, singleton objects and interfaces. If a class requires custom serialization (for example, it requires certain cleanup actions done on dumping / restoring), it can be done by implementing 2 methods: _dump and _load. The instance method _dump should return a String object containing all the information necessary to reconstitute objects of this class and all referenced objects up to a maximum depth given as an integer parameter (a value of -1 implies that depth checking should be disabled). The class method _load should take a String and return an object of this class.

Rust
Serde is the most widely used library, or crate, for serialization in Rust.

Smalltalk
In general, non-recursive and non-sharing objects can be stored and retrieved in a human readable form using the storeOn:/readFrom: protocol. The storeOn: method generates the text of a Smalltalk expression which – when evaluated using readFrom: – recreates the original object. This scheme is special, in that it uses a procedural description of the object, not the data itself. It is therefore very flexible, allowing for classes to define more compact representations. However, in its original form, it does not handle cyclic data structures or preserve the identity of shared references (i.e. two references a single object will be restored as references to two equal, but not identical copies). For this, various portable and non-portable alternatives exist. Some of them are specific to a particular Smalltalk implementation or class library. There are several ways in Squeak Smalltalk to serialize and store objects. The easiest and most used are storeOn:/readFrom: and binary storage formats based on SmartRefStream serializers. In addition, bundled objects can be stored and retrieved using ImageSegments. Both provide a so-called "binary-object storage framework", which support serialization into and retrieval from a compact binary form. Both handle cyclic, recursive and shared structures, storage/retrieval of class and metaclass info and include mechanisms for "on the fly" object migration (i.e. to convert instances which were written by an older version of a class with a different object layout). The APIs are similar (storeBinary/readBinary), but the encoding details are different, making these two formats incompatible. However, the Smalltalk/X code is open source and free and can be loaded into other Smalltalks to allow for cross-dialect object interchange. Object serialization is not part of the ANSI Smalltalk specification. As a result, the code to serialize an object varies by Smalltalk implementation. The resulting binary data also varies. For instance, a serialized object created in Squeak Smalltalk cannot be restored in Ambrai Smalltalk. Consequently, various applications that do work on multiple Smalltalk implementations that rely on object serialization cannot share data between these different implementations. These applications include the MinneStore object database and some RPC packages. A solution to this problem is SIXX, which is a package for multiple Smalltalks that uses an XML-based format for serialization.

Swift
The Swift standard library provides two protocols, Encodable and Decodable (composed together as Codable), which allow instances of conforming types to be serialized to or deserialized from JSON, property lists, or other formats. Default implementations of these protocols can be generated by the compiler for types whose stored properties are also Decodable or Encodable.

PowerShell
PowerShell implements serialization through the built-in cmdlet Export-CliXML. Export-CliXML serializes .NET objects and stores the resulting XML in a file. To reconstitute the objects, use the Import-CliXML cmdlet, which generates a deserialized object from the XML in the exported file. Deserialized objects, often known as "property bags" are not live objects; they are snapshots that have properties, but no methods. Two dimensional data structures can also be (de)serialized in CSV format using the built-in cmdlets Import-CSV and Export-CSV.

See also
Commutation (telemetry)
Comparison of data serialization formats
Container format
Hibernate (Java)
XML Schema
Basic Encoding Rules
Google Protocol Buffers
Wikibase
Apache Avro

References
External links
Java Object Serialization documentation
Java 1.4 Object Serialization documentation.
Durable Java: Serialization Archived 25 November 2005 at the Wayback Machine
XML Data Binding Resources
Databoard - Binary serialization with partial and random access, type system, RPC, type adaption, and text format

## Related Articles

### Internal Links

- [.NET](https://en.wikipedia.org/wiki/.NET)
- [.NET Framework](https://en.wikipedia.org/wiki/.NET_Framework)
- [ACM Transactions on Programming Languages and Systems](https://en.wikipedia.org/wiki/ACM_Transactions_on_Programming_Languages_and_Systems)
- [ASN.1](https://en.wikipedia.org/wiki/ASN.1)
- [Abstract data type](https://en.wikipedia.org/wiki/Abstract_data_type)
- [Action Message Format](https://en.wikipedia.org/wiki/Action_Message_Format)
- [Ajax (programming)](https://en.wikipedia.org/wiki/Ajax_(programming))
- [Apache Avro](https://en.wikipedia.org/wiki/Apache_Avro)
- [Apache Thrift](https://en.wikipedia.org/wiki/Apache_Thrift)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Ascii85](https://en.wikipedia.org/wiki/Ascii85)
- [Atom (web standard)](https://en.wikipedia.org/wiki/Atom_(web_standard))
- [BSON](https://en.wikipedia.org/wiki/BSON)
- [Backup](https://en.wikipedia.org/wiki/Backup)
- [Barbara Liskov](https://en.wikipedia.org/wiki/Barbara_Liskov)
- [Base32](https://en.wikipedia.org/wiki/Base32)
- [Base64](https://en.wikipedia.org/wiki/Base64)
- [X.690](https://en.wikipedia.org/wiki/X.690)
- [Bencode](https://en.wikipedia.org/wiki/Bencode)
- [Binary-to-text encoding](https://en.wikipedia.org/wiki/Binary-to-text_encoding)
- [Binary file](https://en.wikipedia.org/wiki/Binary_file)
- [Boost (C++ libraries)](https://en.wikipedia.org/wiki/Boost_(C%2B%2B_libraries))
- [Endianness](https://en.wikipedia.org/wiki/Endianness)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CBOR](https://en.wikipedia.org/wiki/CBOR)
- [ColdFusion Markup Language](https://en.wikipedia.org/wiki/ColdFusion_Markup_Language)
- [Common Object Request Broker Architecture](https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture)
- [CPAN](https://en.wikipedia.org/wiki/CPAN)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C data types](https://en.wikipedia.org/wiki/C_data_types)
- [Cap'n Proto](https://en.wikipedia.org/wiki/Cap%27n_Proto)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Comma-separated values](https://en.wikipedia.org/wiki/Comma-separated_values)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Commutation (telemetry)](https://en.wikipedia.org/wiki/Commutation_(telemetry))
- [Comparison of data-serialization formats](https://en.wikipedia.org/wiki/Comparison_of_data-serialization_formats)
- [Comparison of data-serialization formats](https://en.wikipedia.org/wiki/Comparison_of_data-serialization_formats)
- [Component-based software engineering](https://en.wikipedia.org/wiki/Component-based_software_engineering)
- [Component Object Model](https://en.wikipedia.org/wiki/Component_Object_Model)
- [Computer file](https://en.wikipedia.org/wiki/Computer_file)
- [Computer network](https://en.wikipedia.org/wiki/Computer_network)
- [Concurrent computing](https://en.wikipedia.org/wiki/Concurrent_computing)
- [Container format](https://en.wikipedia.org/wiki/Container_format)
- [Cyphal](https://en.wikipedia.org/wiki/Cyphal)
- [Data buffer](https://en.wikipedia.org/wiki/Data_buffer)
- [Data exchange](https://en.wikipedia.org/wiki/Data_exchange)
- [Data stream](https://en.wikipedia.org/wiki/Data_stream)
- [Data structure](https://en.wikipedia.org/wiki/Data_structure)
- [Database](https://en.wikipedia.org/wiki/Database)
- [Database dump](https://en.wikipedia.org/wiki/Database_dump)
- [Delaware](https://en.wikipedia.org/wiki/Delaware)
- [Delphi (software)](https://en.wikipedia.org/wiki/Delphi_(software))
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Dump (Unix)](https://en.wikipedia.org/wiki/Dump_(Unix))
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [EDIFACT](https://en.wikipedia.org/wiki/EDIFACT)
- [Encapsulation (computer programming)](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming))
- [Encryption](https://en.wikipedia.org/wiki/Encryption)
- [Endianness](https://en.wikipedia.org/wiki/Endianness)
- [External Data Representation](https://en.wikipedia.org/wiki/External_Data_Representation)
- [File descriptor](https://en.wikipedia.org/wiki/File_descriptor)
- [FlatBuffers](https://en.wikipedia.org/wiki/FlatBuffers)
- [Future-proof](https://en.wikipedia.org/wiki/Future-proof)
- [GNUstep](https://en.wikipedia.org/wiki/GNUstep)
- [GRIB](https://en.wikipedia.org/wiki/GRIB)
- [GSOAP](https://en.wikipedia.org/wiki/GSOAP)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Protocol Buffers](https://en.wikipedia.org/wiki/Protocol_Buffers)
- [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
- [Hard disk drive](https://en.wikipedia.org/wiki/Hard_disk_drive)
- [Hardware architecture](https://en.wikipedia.org/wiki/Hardware_architecture)
- [Hibernate (framework)](https://en.wikipedia.org/wiki/Hibernate_(framework))
- [Hierarchical Data Format](https://en.wikipedia.org/wiki/Hierarchical_Data_Format)
- [Human-readable medium and data](https://en.wikipedia.org/wiki/Human-readable_medium_and_data)
- [Human-readable medium and data](https://en.wikipedia.org/wiki/Human-readable_medium_and_data)
- [IOS](https://en.wikipedia.org/wiki/IOS)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment)
- [Interface (Java)](https://en.wikipedia.org/wiki/Interface_(Java))
- [Interface (computing)](https://en.wikipedia.org/wiki/Interface_(computing))
- [Java Database Connectivity](https://en.wikipedia.org/wiki/Java_Database_Connectivity)
- [JSON](https://en.wikipedia.org/wiki/JSON)
- [JSON Web Encryption](https://en.wikipedia.org/wiki/JSON_Web_Encryption)
- [JSON Web Signature](https://en.wikipedia.org/wiki/JSON_Web_Signature)
- [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token)
- [Java virtual machine](https://en.wikipedia.org/wiki/Java_virtual_machine)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [JavaScript syntax](https://en.wikipedia.org/wiki/JavaScript_syntax)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Julia (programming language)](https://en.wikipedia.org/wiki/Julia_(programming_language))
- [Lisp (programming language)](https://en.wikipedia.org/wiki/Lisp_(programming_language))
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [Magic (programming)](https://en.wikipedia.org/wiki/Magic_(programming))
- [Marker interface pattern](https://en.wikipedia.org/wiki/Marker_interface_pattern)
- [Marshalling (computer science)](https://en.wikipedia.org/wiki/Marshalling_(computer_science))
- [Maurice Herlihy](https://en.wikipedia.org/wiki/Maurice_Herlihy)
- [MessagePack](https://en.wikipedia.org/wiki/MessagePack)
- [Message](https://en.wikipedia.org/wiki/Message)
- [Metaclass](https://en.wikipedia.org/wiki/Metaclass)
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Microsoft](https://en.wikipedia.org/wiki/Microsoft)
- [Microsoft Foundation Class Library](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library)
- [Microsoft Foundation Class Library](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library)
- [NeXTSTEP](https://en.wikipedia.org/wiki/NeXTSTEP)
- [NetCDF](https://en.wikipedia.org/wiki/NetCDF)
- [Network socket](https://en.wikipedia.org/wiki/Network_socket)
- [OCLC](https://en.wikipedia.org/wiki/OCLC)
- [OCaml](https://en.wikipedia.org/wiki/OCaml)
- [Obfuscation (software)](https://en.wikipedia.org/wiki/Obfuscation_(software))
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
- [Open file format](https://en.wikipedia.org/wiki/Open_file_format)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Pickling](https://en.wikipedia.org/wiki/Pickling)
- [Passive data structure](https://en.wikipedia.org/wiki/Passive_data_structure)
- [Pointer (computer programming)](https://en.wikipedia.org/wiki/Pointer_(computer_programming))
- [Pointer swizzling](https://en.wikipedia.org/wiki/Pointer_swizzling)
- [PowerShell](https://en.wikipedia.org/wiki/PowerShell)
- [Primitive data type](https://en.wikipedia.org/wiki/Primitive_data_type)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Prolog](https://en.wikipedia.org/wiki/Prolog)
- [Prolog syntax and semantics](https://en.wikipedia.org/wiki/Prolog_syntax_and_semantics)
- [Property list](https://en.wikipedia.org/wiki/Property_list)
- [Proprietary software](https://en.wikipedia.org/wiki/Proprietary_software)
- [Protocol Buffers](https://en.wikipedia.org/wiki/Protocol_Buffers)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation)
- [Rebol](https://en.wikipedia.org/wiki/Rebol)
- [Request for Comments](https://en.wikipedia.org/wiki/Request_for_Comments)
- [RMI-IIOP](https://en.wikipedia.org/wiki/RMI-IIOP)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Read–eval–print loop](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)
- [Rebol](https://en.wikipedia.org/wiki/Rebol)
- [Reference (computer science)](https://en.wikipedia.org/wiki/Reference_(computer_science))
- [Remote procedure call](https://en.wikipedia.org/wiki/Remote_procedure_call)
- [Resource Description Framework](https://en.wikipedia.org/wiki/Resource_Description_Framework)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Standard Generalized Markup Language](https://en.wikipedia.org/wiki/Standard_Generalized_Markup_Language)
- [SOAP](https://en.wikipedia.org/wiki/SOAP)
- [Computer data storage](https://en.wikipedia.org/wiki/Computer_data_storage)
- [SerDes](https://en.wikipedia.org/wiki/SerDes)
- [Serialization (disambiguation)](https://en.wikipedia.org/wiki/Serialization_(disambiguation))
- [Shell builtin](https://en.wikipedia.org/wiki/Shell_builtin)
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Software framework](https://en.wikipedia.org/wiki/Software_framework)
- [Squeak](https://en.wikipedia.org/wiki/Squeak)
- [Stack (abstract data type)](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
- [Struct (C programming language)](https://en.wikipedia.org/wiki/Struct_(C_programming_language))
- [Structure of Management Information](https://en.wikipedia.org/wiki/Structure_of_Management_Information)
- [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Swing (Java)](https://en.wikipedia.org/wiki/Swing_(Java))
- [Syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar)
- [TOML](https://en.wikipedia.org/wiki/TOML)
- [Trade secret](https://en.wikipedia.org/wiki/Trade_secret)
- [Transient (computer programming)](https://en.wikipedia.org/wiki/Transient_(computer_programming))
- [Type class](https://en.wikipedia.org/wiki/Type_class)
- [Polymorphism (computer science)](https://en.wikipedia.org/wiki/Polymorphism_(computer_science))
- [UBJSON](https://en.wikipedia.org/wiki/UBJSON)
- [Unicode](https://en.wikipedia.org/wiki/Unicode)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [Marshalling (computer science)](https://en.wikipedia.org/wiki/Marshalling_(computer_science))
- [Pointer swizzling](https://en.wikipedia.org/wiki/Pointer_swizzling)
- [Uuencoding](https://en.wikipedia.org/wiki/Uuencoding)
- [Virtual machine](https://en.wikipedia.org/wiki/Virtual_machine)
- [WDDX](https://en.wikipedia.org/wiki/WDDX)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Wikidata](https://en.wikipedia.org/wiki/Wikidata)
- [XML](https://en.wikipedia.org/wiki/XML)
- [XML Schema (W3C)](https://en.wikipedia.org/wiki/XML_Schema_(W3C))
- [Xerox Network Systems](https://en.wikipedia.org/wiki/Xerox_Network_Systems)
- [YAML](https://en.wikipedia.org/wiki/YAML)
- [YEnc](https://en.wikipedia.org/wiki/YEnc)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:External links](https://en.wikipedia.org/wiki/Wikipedia:External_links)
- [Wikipedia:What Wikipedia is not](https://en.wikipedia.org/wiki/Wikipedia:What_Wikipedia_is_not)
- [Template:Data exchange](https://en.wikipedia.org/wiki/Template:Data_exchange)
- [Template talk:Data exchange](https://en.wikipedia.org/wiki/Template_talk:Data_exchange)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Wikipedia external links cleanup from August 2024](https://en.wikipedia.org/wiki/Category:Wikipedia_external_links_cleanup_from_August_2024)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:50:54.470402+00:00_