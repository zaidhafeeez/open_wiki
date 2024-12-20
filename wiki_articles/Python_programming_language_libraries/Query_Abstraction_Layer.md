---
title: Query Abstraction Layer
url: https://en.wikipedia.org/wiki/Query_Abstraction_Layer
language: en
categories: ["Category:Articles with imported Creative Commons licensed text", "Category:Cross-platform free software", "Category:Free software programmed in Python", "Category:Python (programming language) libraries"]
references: 0
last_modified: 2024-11-24T06:40:53Z
---

# Query Abstraction Layer

## Summary

QAL is an open-source development project that aims to create a collection of libraries for mixing, moving, merging, substituting and transforming data; also in some cases, such as MongoDB, schemas.

## Full Content

QAL is an open-source development project that aims to create a collection of libraries for mixing, moving, merging, substituting and transforming data; also in some cases, such as MongoDB, schemas.

Description
Sources and destinations include different database backends, file formats like .csv, XML and spreadsheets. Even untidy HTML web pages can be used as both a source and destination.
For SQL/RDBMS backends, it has a database abstraction layer that supports basic connectivity to Postgres, MySQL / MariaDB, IBM Db2, Oracle and MS SQL Server. It uses XML formats (the SQL schema is self-generated) for representation of queries, transformation and merging, making it all processable by scripts.
With regards to SQL, QAL uses a subset of SQL features and data types, which while obviously not complete however is sufficient for most usages. It is however easy to instead use backend-specific SQL when the queries do not have to be backend-agnostic.
It is currently distributed as a Python Library (.egg) and a Debian package file (.deb).
It is related to the Optimal BPM (Business Process Management) project. The Optimal BPM SourceForge project used to be DAL/QAL.

References
This article incorporates http://sourceforge.net/projects/qal/ text available under the CC0 license.

External links
QAL Documentation and examples
API documentation
