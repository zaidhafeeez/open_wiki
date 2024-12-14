# Apache Avro

## Article Metadata

- **Last Updated:** 2024-12-14T19:32:49.434058+00:00
- **Original Article:** [Apache Avro](https://en.wikipedia.org/wiki/Apache_Avro)
- **Language:** en
- **Page ID:** 27326934

## Summary

Avro is a row-oriented remote procedure call and data serialization framework developed within Apache's Hadoop project. It uses JSON for defining data types and protocols, and serializes data in a compact binary format. Its primary use is in Apache Hadoop, where it can provide both a serialization format for persistent data, and a wire format for communication between Hadoop nodes, and from client programs to the Hadoop services.
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

## Table of Contents

- Avro Object Container File
- Schema definition
- Serializing and deserializing
- Languages with APIs
- Avro IDL
- Logo
- See also
- References
- Further reading

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

## Related Articles

### Internal Links

- [ASCII](https://en.wikipedia.org/wiki/ASCII)
- [ASN.1](https://en.wikipedia.org/wiki/ASN.1)
- [Action Message Format](https://en.wikipedia.org/wiki/Action_Message_Format)
- [Apache Accumulo](https://en.wikipedia.org/wiki/Apache_Accumulo)
- [Apache ActiveMQ](https://en.wikipedia.org/wiki/Apache_ActiveMQ)
- [Apache Airavata](https://en.wikipedia.org/wiki/Apache_Airavata)
- [Apache Airflow](https://en.wikipedia.org/wiki/Apache_Airflow)
- [Apache Allura](https://en.wikipedia.org/wiki/Apache_Allura)
- [List of Apache Software Foundation projects](https://en.wikipedia.org/wiki/List_of_Apache_Software_Foundation_projects)
- [Apache Ant](https://en.wikipedia.org/wiki/Apache_Ant)
- [Apache Apex](https://en.wikipedia.org/wiki/Apache_Apex)
- [Apache Aries](https://en.wikipedia.org/wiki/Apache_Aries)
- [Apache Arrow](https://en.wikipedia.org/wiki/Apache_Arrow)
- [Apache Axis](https://en.wikipedia.org/wiki/Apache_Axis)
- [Apache Axis2](https://en.wikipedia.org/wiki/Apache_Axis2)
- [Apache Batik](https://en.wikipedia.org/wiki/Apache_Batik)
- [Apache Beam](https://en.wikipedia.org/wiki/Apache_Beam)
- [Apache Beehive](https://en.wikipedia.org/wiki/Apache_Beehive)
- [Trac](https://en.wikipedia.org/wiki/Trac)
- [Apache Brooklyn](https://en.wikipedia.org/wiki/Apache_Brooklyn)
- [Apache CXF](https://en.wikipedia.org/wiki/Apache_CXF)
- [Apache Calcite](https://en.wikipedia.org/wiki/Apache_Calcite)
- [Apache Camel](https://en.wikipedia.org/wiki/Apache_Camel)
- [Apache CarbonData](https://en.wikipedia.org/wiki/Apache_CarbonData)
- [Apache Cassandra](https://en.wikipedia.org/wiki/Apache_Cassandra)
- [Apache Cayenne](https://en.wikipedia.org/wiki/Apache_Cayenne)
- [Apache Click](https://en.wikipedia.org/wiki/Apache_Click)
- [Apache CloudStack](https://en.wikipedia.org/wiki/Apache_CloudStack)
- [Apache Cocoon](https://en.wikipedia.org/wiki/Apache_Cocoon)
- [Apache Commons](https://en.wikipedia.org/wiki/Apache_Commons)
- [Apache Commons Logging](https://en.wikipedia.org/wiki/Apache_Commons_Logging)
- [Apache Continuum](https://en.wikipedia.org/wiki/Apache_Continuum)
- [Apache Cordova](https://en.wikipedia.org/wiki/Apache_Cordova)
- [Apache CouchDB](https://en.wikipedia.org/wiki/Apache_CouchDB)
- [Apache Derby](https://en.wikipedia.org/wiki/Apache_Derby)
- [Apache Directory](https://en.wikipedia.org/wiki/Apache_Directory)
- [Apache Drill](https://en.wikipedia.org/wiki/Apache_Drill)
- [Apache Druid](https://en.wikipedia.org/wiki/Apache_Druid)
- [Apache Empire-db](https://en.wikipedia.org/wiki/Apache_Empire-db)
- [Formatting Objects Processor](https://en.wikipedia.org/wiki/Formatting_Objects_Processor)
- [Apache Felix](https://en.wikipedia.org/wiki/Apache_Felix)
- [Apache Flex](https://en.wikipedia.org/wiki/Apache_Flex)
- [Apache Flink](https://en.wikipedia.org/wiki/Apache_Flink)
- [List of Apache Software Foundation projects](https://en.wikipedia.org/wiki/List_of_Apache_Software_Foundation_projects)
- [Apache Geronimo](https://en.wikipedia.org/wiki/Apache_Geronimo)
- [Apache Giraph](https://en.wikipedia.org/wiki/Apache_Giraph)
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Apache Guacamole](https://en.wikipedia.org/wiki/Apache_Guacamole)
- [Apache Gump](https://en.wikipedia.org/wiki/Apache_Gump)
- [Apache HBase](https://en.wikipedia.org/wiki/Apache_HBase)
- [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server)
- [Apache Hadoop](https://en.wikipedia.org/wiki/Apache_Hadoop)
- [Apache Hama](https://en.wikipedia.org/wiki/Apache_Hama)
- [Apache Harmony](https://en.wikipedia.org/wiki/Apache_Harmony)
- [Apache Helix](https://en.wikipedia.org/wiki/Apache_Helix)
- [Apache Hive](https://en.wikipedia.org/wiki/Apache_Hive)
- [Apache Iceberg](https://en.wikipedia.org/wiki/Apache_Iceberg)
- [Apache Ignite](https://en.wikipedia.org/wiki/Apache_Ignite)
- [Apache Impala](https://en.wikipedia.org/wiki/Apache_Impala)
- [Apache Ivy](https://en.wikipedia.org/wiki/Apache_Ivy)
- [Apache JMeter](https://en.wikipedia.org/wiki/Apache_JMeter)
- [Apache Jackrabbit](https://en.wikipedia.org/wiki/Apache_Jackrabbit)
- [Apache James](https://en.wikipedia.org/wiki/Apache_James)
- [Apache Jelly](https://en.wikipedia.org/wiki/Apache_Jelly)
- [Apache Jena](https://en.wikipedia.org/wiki/Apache_Jena)
- [Apache Kafka](https://en.wikipedia.org/wiki/Apache_Kafka)
- [Apache Kudu](https://en.wikipedia.org/wiki/Apache_Kudu)
- [Apache Kylin](https://en.wikipedia.org/wiki/Apache_Kylin)
- [Apache License](https://en.wikipedia.org/wiki/Apache_License)
- [Apache License](https://en.wikipedia.org/wiki/Apache_License)
- [Apache Lucene](https://en.wikipedia.org/wiki/Apache_Lucene)
- [Apache MINA](https://en.wikipedia.org/wiki/Apache_MINA)
- [Apache MXNet](https://en.wikipedia.org/wiki/Apache_MXNet)
- [Apache Mahout](https://en.wikipedia.org/wiki/Apache_Mahout)
- [Apache Marmotta](https://en.wikipedia.org/wiki/Apache_Marmotta)
- [Apache Maven](https://en.wikipedia.org/wiki/Apache_Maven)
- [Apache MyFaces](https://en.wikipedia.org/wiki/Apache_MyFaces)
- [Apache Mynewt](https://en.wikipedia.org/wiki/Apache_Mynewt)
- [Apache NiFi](https://en.wikipedia.org/wiki/Apache_NiFi)
- [Apache Nutch](https://en.wikipedia.org/wiki/Apache_Nutch)
- [Apache ODE](https://en.wikipedia.org/wiki/Apache_ODE)
- [Apache OFBiz](https://en.wikipedia.org/wiki/Apache_OFBiz)
- [Apache ORC](https://en.wikipedia.org/wiki/Apache_ORC)
- [Apache Oozie](https://en.wikipedia.org/wiki/Apache_Oozie)
- [Apache OpenEJB](https://en.wikipedia.org/wiki/Apache_OpenEJB)
- [Apache OpenJPA](https://en.wikipedia.org/wiki/Apache_OpenJPA)
- [Apache OpenNLP](https://en.wikipedia.org/wiki/Apache_OpenNLP)
- [Apache OpenOffice](https://en.wikipedia.org/wiki/Apache_OpenOffice)
- [Apache PDFBox](https://en.wikipedia.org/wiki/Apache_PDFBox)
- [Apache POI](https://en.wikipedia.org/wiki/Apache_POI)
- [Apache Parquet](https://en.wikipedia.org/wiki/Apache_Parquet)
- [Apache Phoenix](https://en.wikipedia.org/wiki/Apache_Phoenix)
- [Apache Pig](https://en.wikipedia.org/wiki/Apache_Pig)
- [Apache Pinot](https://en.wikipedia.org/wiki/Apache_Pinot)
- [Apache Pivot](https://en.wikipedia.org/wiki/Apache_Pivot)
- [Apache Portable Runtime](https://en.wikipedia.org/wiki/Apache_Portable_Runtime)
- [Apache Qpid](https://en.wikipedia.org/wiki/Apache_Qpid)
- [Apache RocketMQ](https://en.wikipedia.org/wiki/Apache_RocketMQ)
- [Apache Roller](https://en.wikipedia.org/wiki/Apache_Roller)
- [Apache SINGA](https://en.wikipedia.org/wiki/Apache_SINGA)
- [Apache Samza](https://en.wikipedia.org/wiki/Apache_Samza)
- [Apache Shale](https://en.wikipedia.org/wiki/Apache_Shale)
- [Apache Shiro](https://en.wikipedia.org/wiki/Apache_Shiro)
- [Apache Sling](https://en.wikipedia.org/wiki/Apache_Sling)
- [The Apache Software Foundation](https://en.wikipedia.org/wiki/The_Apache_Software_Foundation)
- [Apache Solr](https://en.wikipedia.org/wiki/Apache_Solr)
- [Apache SpamAssassin](https://en.wikipedia.org/wiki/Apache_SpamAssassin)
- [Apache Spark](https://en.wikipedia.org/wiki/Apache_Spark)
- [Apache Stanbol](https://en.wikipedia.org/wiki/Apache_Stanbol)
- [Apache Storm](https://en.wikipedia.org/wiki/Apache_Storm)
- [Apache Struts](https://en.wikipedia.org/wiki/Apache_Struts)
- [Apache Struts 1](https://en.wikipedia.org/wiki/Apache_Struts_1)
- [Apache Subversion](https://en.wikipedia.org/wiki/Apache_Subversion)
- [Apache Superset](https://en.wikipedia.org/wiki/Apache_Superset)
- [Apache SystemDS](https://en.wikipedia.org/wiki/Apache_SystemDS)
- [Apache Tapestry](https://en.wikipedia.org/wiki/Apache_Tapestry)
- [Apache Taverna](https://en.wikipedia.org/wiki/Apache_Taverna)
- [Apache Thrift](https://en.wikipedia.org/wiki/Apache_Thrift)
- [Apache Tika](https://en.wikipedia.org/wiki/Apache_Tika)
- [Gremlin (query language)](https://en.wikipedia.org/wiki/Gremlin_(query_language))
- [Apache Tomcat](https://en.wikipedia.org/wiki/Apache_Tomcat)
- [Apache Traffic Server](https://en.wikipedia.org/wiki/Apache_Traffic_Server)
- [List of Apache Software Foundation projects](https://en.wikipedia.org/wiki/List_of_Apache_Software_Foundation_projects)
- [List of Apache Software Foundation projects](https://en.wikipedia.org/wiki/List_of_Apache_Software_Foundation_projects)
- [Apache Velocity](https://en.wikipedia.org/wiki/Apache_Velocity)
- [Google Wave](https://en.wikipedia.org/wiki/Google_Wave)
- [Apache Wicket](https://en.wikipedia.org/wiki/Apache_Wicket)
- [Apache XML](https://en.wikipedia.org/wiki/Apache_XML)
- [Apache XMLBeans](https://en.wikipedia.org/wiki/Apache_XMLBeans)
- [Apache Xalan](https://en.wikipedia.org/wiki/Apache_Xalan)
- [Apache Xerces](https://en.wikipedia.org/wiki/Apache_Xerces)
- [Apache ZooKeeper](https://en.wikipedia.org/wiki/Apache_ZooKeeper)
- [Apache cTAKES](https://en.wikipedia.org/wiki/Apache_cTAKES)
- [Apache iBATIS](https://en.wikipedia.org/wiki/Apache_iBATIS)
- [Ascii85](https://en.wikipedia.org/wiki/Ascii85)
- [Atom (web standard)](https://en.wikipedia.org/wiki/Atom_(web_standard))
- [Avro](https://en.wikipedia.org/wiki/Avro)
- [AxKit](https://en.wikipedia.org/wiki/AxKit)
- [BSON](https://en.wikipedia.org/wiki/BSON)
- [Base32](https://en.wikipedia.org/wiki/Base32)
- [Base64](https://en.wikipedia.org/wiki/Base64)
- [Bean Scripting Framework](https://en.wikipedia.org/wiki/Bean_Scripting_Framework)
- [Bencode](https://en.wikipedia.org/wiki/Bencode)
- [Binary file](https://en.wikipedia.org/wiki/Binary_file)
- [Block (data storage)](https://en.wikipedia.org/wiki/Block_(data_storage))
- [Byte Code Engineering Library](https://en.wikipedia.org/wiki/Byte_Code_Engineering_Library)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CBOR](https://en.wikipedia.org/wiki/CBOR)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Cap'n Proto](https://en.wikipedia.org/wiki/Cap%27n_Proto)
- [Data orientation](https://en.wikipedia.org/wiki/Data_orientation)
- [Comma-separated values](https://en.wikipedia.org/wiki/Comma-separated_values)
- [Commons Daemon](https://en.wikipedia.org/wiki/Commons_Daemon)
- [Communication protocol](https://en.wikipedia.org/wiki/Communication_protocol)
- [Comparison of data-serialization formats](https://en.wikipedia.org/wiki/Comparison_of_data-serialization_formats)
- [Comparison of data-serialization formats](https://en.wikipedia.org/wiki/Comparison_of_data-serialization_formats)
- [Container (abstract data type)](https://en.wikipedia.org/wiki/Container_(abstract_data_type))
- [Cyphal](https://en.wikipedia.org/wiki/Cyphal)
- [Data exchange](https://en.wikipedia.org/wiki/Data_exchange)
- [Data type](https://en.wikipedia.org/wiki/Data_type)
- [Database schema](https://en.wikipedia.org/wiki/Database_schema)
- [Deltacloud](https://en.wikipedia.org/wiki/Deltacloud)
- [EDIFACT](https://en.wikipedia.org/wiki/EDIFACT)
- [Elixir (programming language)](https://en.wikipedia.org/wiki/Elixir_(programming_language))
- [Etch (protocol)](https://en.wikipedia.org/wiki/Etch_(protocol))
- [External Data Representation](https://en.wikipedia.org/wiki/External_Data_Representation)
- [Header (computing)](https://en.wikipedia.org/wiki/Header_(computing))
- [FlatBuffers](https://en.wikipedia.org/wiki/FlatBuffers)
- [FreeMarker](https://en.wikipedia.org/wiki/FreeMarker)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Human-readable medium and data](https://en.wikipedia.org/wiki/Human-readable_medium_and_data)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Interface description language](https://en.wikipedia.org/wiki/Interface_description_language)
- [Internet Communications Engine](https://en.wikipedia.org/wiki/Internet_Communications_Engine)
- [JSON](https://en.wikipedia.org/wiki/JSON)
- [JSON Web Encryption](https://en.wikipedia.org/wiki/JSON_Web_Encryption)
- [JSON Web Signature](https://en.wikipedia.org/wiki/JSON_Web_Signature)
- [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token)
- [Jakarta Project](https://en.wikipedia.org/wiki/Jakarta_Project)
- [Jakarta Project](https://en.wikipedia.org/wiki/Jakarta_Project)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Jini](https://en.wikipedia.org/wiki/Jini)
- [Log4j](https://en.wikipedia.org/wiki/Log4j)
- [Machine-readable medium and data](https://en.wikipedia.org/wiki/Machine-readable_medium_and_data)
- [MessagePack](https://en.wikipedia.org/wiki/MessagePack)
- [Mod perl](https://en.wikipedia.org/wiki/Mod_perl)
- [NetBeans](https://en.wikipedia.org/wiki/NetBeans)
- [Node (networking)](https://en.wikipedia.org/wiki/Node_(networking))
- [NuttX](https://en.wikipedia.org/wiki/NuttX)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Persistent data](https://en.wikipedia.org/wiki/Persistent_data)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Property list](https://en.wikipedia.org/wiki/Property_list)
- [Protocol Buffers](https://en.wikipedia.org/wiki/Protocol_Buffers)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Rebol](https://en.wikipedia.org/wiki/Rebol)
- [Remote procedure call](https://en.wikipedia.org/wiki/Remote_procedure_call)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Resource Description Framework](https://en.wikipedia.org/wiki/Resource_Description_Framework)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Serialization](https://en.wikipedia.org/wiki/Serialization)
- [Service (systems architecture)](https://en.wikipedia.org/wiki/Service_(systems_architecture))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software framework](https://en.wikipedia.org/wiki/Software_framework)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Sqoop](https://en.wikipedia.org/wiki/Sqoop)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Structure of Management Information](https://en.wikipedia.org/wiki/Structure_of_Management_Information)
- [TOML](https://en.wikipedia.org/wiki/TOML)
- [The Apache Software Foundation](https://en.wikipedia.org/wiki/The_Apache_Software_Foundation)
- [Apache Thrift](https://en.wikipedia.org/wiki/Apache_Thrift)
- [UBJSON](https://en.wikipedia.org/wiki/UBJSON)
- [UIMA](https://en.wikipedia.org/wiki/UIMA)
- [Uuencoding](https://en.wikipedia.org/wiki/Uuencoding)
- [Wire data](https://en.wikipedia.org/wiki/Wire_data)
- [XML](https://en.wikipedia.org/wiki/XML)
- [YAML](https://en.wikipedia.org/wiki/YAML)
- [YEnc](https://en.wikipedia.org/wiki/YEnc)
- [Template:Apache Software Foundation](https://en.wikipedia.org/wiki/Template:Apache_Software_Foundation)
- [Template:Data exchange](https://en.wikipedia.org/wiki/Template:Data_exchange)
- [Template talk:Apache Software Foundation](https://en.wikipedia.org/wiki/Template_talk:Apache_Software_Foundation)
- [Template talk:Data exchange](https://en.wikipedia.org/wiki/Template_talk:Data_exchange)
- [Category:Apache Software Foundation](https://en.wikipedia.org/wiki/Category:Apache_Software_Foundation)
- [Category:Use mdy dates from April 2016](https://en.wikipedia.org/wiki/Category:Use_mdy_dates_from_April_2016)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:32:49.434058+00:00_