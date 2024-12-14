# SQLAlchemy

## Article Metadata

- **Last Updated:** 2024-12-14T19:52:26.786003+00:00
- **Original Article:** [SQLAlchemy](https://en.wikipedia.org/wiki/SQLAlchemy)
- **Language:** en
- **Page ID:** 9465815

## Summary

SQLAlchemy is an open-source Python library that provides an SQL toolkit (called "SQLAlchemy Core") and an Object Relational Mapper (ORM) for database interactions. It allows developers to work with databases using Python objects, enabling efficient and flexible database access.

## Categories

- Category:2006 software
- Category:Articles with short description
- Category:Object–relational mapping
- Category:Python (programming language) libraries
- Category:Short description is different from Wikidata
- Category:Software using the MIT license

## Table of Contents

- Description
- History
- Example
- See also
- References

## Content

SQLAlchemy is an open-source Python library that provides an SQL toolkit (called "SQLAlchemy Core") and an Object Relational Mapper (ORM) for database interactions. It allows developers to work with databases using Python objects, enabling efficient and flexible database access.

Description
SQLAlchemy offers tools for database schema generation, querying, and object-relational mapping. Key features include:

A comprehensive embedded domain-specific language for SQL in Python called "SQLAlchemy Core" that provides means to construct and execute SQL queries.
A powerful ORM that allows the mapping of Python classes to database tables.
Support for database schema migrations.
Compatibility with multiple database backends.
Tools for database connection pooling and transaction management.

History
SQLAlchemy was first released in February 2006. It has evolved to include a wide range of features for database interaction and has gained popularity among Python developers. Notable versions include:

Version 0.1 (2006): Initial release.
Version 1.0 (2015): Major enhancements in ORM and SQL expression language.
Version 1.4 (2021): Introduction of a new ORM API.

Example
The following example represents an n-to-1 relationship between movies and their directors. It is shown how user-defined Python classes create corresponding database tables, how instances with relationships are created from either side of the relationship, and finally how the data can be queried — illustrating automatically generated SQL queries for both lazy and eager loading.

Schema definition
Creating two Python classes and corresponding database tables in the DBMS:

Data insertion
One can insert a director-movie relationship via either entity:

Querying
SQLAlchemy issues the following query to the DBMS (omitting aliases):

The output:

Setting lazy=True (default) instead, SQLAlchemy would first issue a query to get the list of movies and only when needed (lazy) for each director a query to get the name of the corresponding director:

See also
SQLObject
Storm
Pylons
TurboGears
Cubes (OLAP server)

References

Notes
Gift, Noah (12 Aug 2008). "Using SQLAlchemy". Developerworks. IBM. Retrieved 8 Feb 2011.
Rick Copeland, Essential SQLAlchemy, O'Reilly, 2008, ISBN 0-596-51614-2

## Related Articles

### Internal Links

- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Cubes (OLAP server)](https://en.wikipedia.org/wiki/Cubes_(OLAP_server))
- [Domain-specific language](https://en.wikipedia.org/wiki/Domain-specific_language)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Lazy loading](https://en.wikipedia.org/wiki/Lazy_loading)
- [MIT License](https://en.wikipedia.org/wiki/MIT_License)
- [O'Reilly Media](https://en.wikipedia.org/wiki/O%27Reilly_Media)
- [Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
- [Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
- [Open source](https://en.wikipedia.org/wiki/Open_source)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Python Conference](https://en.wikipedia.org/wiki/Python_Conference)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [SQLObject](https://en.wikipedia.org/wiki/SQLObject)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Storm (software)](https://en.wikipedia.org/wiki/Storm_(software))
- [TurboGears](https://en.wikipedia.org/wiki/TurboGears)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:52:26.786003+00:00_