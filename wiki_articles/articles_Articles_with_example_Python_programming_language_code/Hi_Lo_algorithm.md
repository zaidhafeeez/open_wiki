# Hi/Lo algorithm

## Article Metadata

- **Last Updated:** 2024-12-15T04:26:52.223246+00:00
- **Original Article:** [Hi/Lo algorithm](https://en.wikipedia.org/wiki/Hi/Lo_algorithm)
- **Language:** en
- **Page ID:** 62235560

## Summary

Hi/Lo is an algorithm and a key generation strategy used for generating unique keys for use in a database as a primary key. It uses a sequence-based hi-lo pattern to generate values. Hi/Lo is used in scenarios where an application needs its entities to have an identity prior to persistence. It is a value generation strategy. An alternative to Hi/Lo would be for the application to generate keys as universally unique identifiers (UUID).

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with example pseudocode
- Category:Database algorithms
- Category:Object–relational mapping

## Table of Contents

- Explanation
- Algorithm
- Example
- Books
- Support
- See also
- References
- External links

## Content

Hi/Lo is an algorithm and a key generation strategy used for generating unique keys for use in a database as a primary key. It uses a sequence-based hi-lo pattern to generate values. Hi/Lo is used in scenarios where an application needs its entities to have an identity prior to persistence. It is a value generation strategy. An alternative to Hi/Lo would be for the application to generate keys as universally unique identifiers (UUID).

Explanation
The preconditions are:

There is a constant defined to hold the maximum low value. The value must be greater than zero. A suitable value could be 1000 or 32767.
There is a variable defined to hold the currently assigned high value and it is assigned the value 0 (zero).
There is a variable defined to hold the currently assigned low value and it is assigned the value of the maximum low value plus 1 (one).
The steps are:

If the currently assigned low value is greater or equal than the maximum low value then call a function to fetch a new high value and reset the currently assigned low value to 0 (zero).
Assign a key by multiplying the currently assigned high value with the maximum low value and adding the currently assigned low value.
Increment the currently assigned low value by 1 (one).

The database needs a table with a column for the table name and a column the high value.

Algorithm
The current_lo (integer) and current_hi (integer) variables are internal state variables. The internal state is retained across invocations. The max_lo (integer) constant is a configuration option. get_next_hi is a function that retrieves a new high value from a database server. In a relational database management system this could be through a stored procedure.
Precondition: max_lo must be set to a value greater than zero.

algorithm generate_key is
    output: key as a positive integer

    if current_lo ≥ max_lo then
        current_hi := get_next_hi()
        current_lo := 0

    key := current_hi × max_lo + current_lo
    current_lo := current_lo + 1

    return key

Example
Example implementation in Python. 

Output:

Books
Very briefly mentioned in the 2003 book Java Persistence for Relational Databases by Richard Sperko on page 236.
Very briefly mentioned in the 2004 book Better, Faster, Lighter Java by Bruce Tate and Justin Gehtland on page 137.
Very briefly mentioned in the 2004 book Enterprise Java Development on a Budget: Leveraging Java Open Source by Brian Sam-Bodden and Christopher M Jud on page 386.
Explained in the 2015 book Learning NHibernate 4 by Suhas Chatekar on page 53 and 144–145.
Mentioned in the 2017 book NHibernate 4.x cookbook on page 35.
Mentioned in the 2018 book ASP.NET Core 2 Fundamentals on page 219.

This implementation uses hi/lo algorithm to generate identifiers. Algorithm uses a high value retrieved from database and combines it with range of low values to generate a unique identifier. High value is from column next_id of table hibernate_unique_key by default. But you can override this to use a different table. This algorithm also supports specifying a where parameter which can be used to retrieve high value for different entities from different rows of the hibernate_unique_key table.
hilo needs a set of two numbers to work with. One is hi which is sourced from a database table and other is lo which is calculated by NHibernate. NHibernate combines these two 
numbers using a formula to generate a unique number that can be used as identifier.
While auto incremented IDs are simpler, whenever you add an entity to the context, this addition forces the entity to be inserted to the database. That is because we can only retrieve the ID if the actual insertion happens in the case of auto incremented IDs. The HiLo algorithm frees us from this restriction by reserving the IDs beforehand using a database sequence.

Support
Supported by Entity Framework Core (ORM for .NET Core) with Microsoft SQL Server using the UseHiLo extension method. Not supported by the predecessor Entity Framework.
Supported by Hibernate (ORM for Java) and NHibernate (ORM for .NET) through SequenceHiLoGenerator and TableHiLoGenerator. Had support since at least 2002. Had support since at least version 3.2 with code authored by Gavin King.
Supported by Doctrine (ORM for PHP) through the TableGenerator class.
Supported by Marten (persistence library for .NET) with PostgreSQL through the HiLoSequence class.
Supported by RavenDB (a NoSQL document database).
Not supported by Apache Cayenne, ServiceStack.OrmLite, Ruby on Rails Active Record, Dapper, and Dashing.

See also
Distributed transaction
Domain-driven design (DDD)
Primary key

References
External links
What's the Hi/Lo algorithm? - Stack Overflow
The hi/lo algorithm - Vlad Mihalcea

## Related Articles

### Internal Links

- [Apache Cayenne](https://en.wikipedia.org/wiki/Apache_Cayenne)
- [Cardinality (data modeling)](https://en.wikipedia.org/wiki/Cardinality_(data_modeling))
- [Comparison of database administration tools](https://en.wikipedia.org/wiki/Comparison_of_database_administration_tools)
- [Data source name](https://en.wikipedia.org/wiki/Data_source_name)
- [Data definition language](https://en.wikipedia.org/wiki/Data_definition_language)
- [Data manipulation language](https://en.wikipedia.org/wiki/Data_manipulation_language)
- [Data migration](https://en.wikipedia.org/wiki/Data_migration)
- [Database](https://en.wikipedia.org/wiki/Database)
- [Database-centric architecture](https://en.wikipedia.org/wiki/Database-centric_architecture)
- [Database abstraction layer](https://en.wikipedia.org/wiki/Database_abstraction_layer)
- [Database activity monitoring](https://en.wikipedia.org/wiki/Database_activity_monitoring)
- [Database administrator](https://en.wikipedia.org/wiki/Database_administrator)
- [Database application](https://en.wikipedia.org/wiki/Database_application)
- [Database audit](https://en.wikipedia.org/wiki/Database_audit)
- [Database caching](https://en.wikipedia.org/wiki/Database_caching)
- [Database connection](https://en.wikipedia.org/wiki/Database_connection)
- [Database design](https://en.wikipedia.org/wiki/Database_design)
- [Database engine](https://en.wikipedia.org/wiki/Database_engine)
- [Database forensics](https://en.wikipedia.org/wiki/Database_forensics)
- [Data integrity](https://en.wikipedia.org/wiki/Data_integrity)
- [Database machine](https://en.wikipedia.org/wiki/Database_machine)
- [Database](https://en.wikipedia.org/wiki/Database)
- [Database model](https://en.wikipedia.org/wiki/Database_model)
- [Database normalization](https://en.wikipedia.org/wiki/Database_normalization)
- [Database object](https://en.wikipedia.org/wiki/Database_object)
- [Database preservation](https://en.wikipedia.org/wiki/Database_preservation)
- [Database publishing](https://en.wikipedia.org/wiki/Database_publishing)
- [Database refactoring](https://en.wikipedia.org/wiki/Database_refactoring)
- [Database schema](https://en.wikipedia.org/wiki/Database_schema)
- [Database security](https://en.wikipedia.org/wiki/Database_security)
- [Database server](https://en.wikipedia.org/wiki/Database_server)
- [Database theory](https://en.wikipedia.org/wiki/Database_theory)
- [Database tuning](https://en.wikipedia.org/wiki/Database_tuning)
- [Database virtualization](https://en.wikipedia.org/wiki/Database_virtualization)
- [Datasource](https://en.wikipedia.org/wiki/Datasource)
- [Distributed transaction](https://en.wikipedia.org/wiki/Distributed_transaction)
- [Doctrine (PHP)](https://en.wikipedia.org/wiki/Doctrine_(PHP))
- [Domain-driven design](https://en.wikipedia.org/wiki/Domain-driven_design)
- [Enhanced entity–relationship model](https://en.wikipedia.org/wiki/Enhanced_entity%E2%80%93relationship_model)
- [Entity Framework](https://en.wikipedia.org/wiki/Entity_Framework)
- [Entity–relationship model](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model)
- [Halloween Problem](https://en.wikipedia.org/wiki/Halloween_Problem)
- [Hibernate (framework)](https://en.wikipedia.org/wiki/Hibernate_(framework))
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Query language](https://en.wikipedia.org/wiki/Query_language)
- [Integer (computer science)](https://en.wikipedia.org/wiki/Integer_(computer_science))
- [Intelligent database](https://en.wikipedia.org/wiki/Intelligent_database)
- [List of academic databases and search engines](https://en.wikipedia.org/wiki/List_of_academic_databases_and_search_engines)
- [List of biodiversity databases](https://en.wikipedia.org/wiki/List_of_biodiversity_databases)
- [List of biological databases](https://en.wikipedia.org/wiki/List_of_biological_databases)
- [List of facial expression databases](https://en.wikipedia.org/wiki/List_of_facial_expression_databases)
- [List of online databases](https://en.wikipedia.org/wiki/List_of_online_databases)
- [List of online music databases](https://en.wikipedia.org/wiki/List_of_online_music_databases)
- [List of online real estate databases](https://en.wikipedia.org/wiki/List_of_online_real_estate_databases)
- [Lists of databases](https://en.wikipedia.org/wiki/Lists_of_databases)
- [Load file](https://en.wikipedia.org/wiki/Load_file)
- [Record locking](https://en.wikipedia.org/wiki/Record_locking)
- [Locks with ordered sharing](https://en.wikipedia.org/wiki/Locks_with_ordered_sharing)
- [Log shipping](https://en.wikipedia.org/wiki/Log_shipping)
- [Microsoft SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server)
- [NHibernate](https://en.wikipedia.org/wiki/NHibernate)
- [Negative database](https://en.wikipedia.org/wiki/Negative_database)
- [Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
- [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)
- [Primary key](https://en.wikipedia.org/wiki/Primary_key)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Query language](https://en.wikipedia.org/wiki/Query_language)
- [RavenDB](https://en.wikipedia.org/wiki/RavenDB)
- [Ruby on Rails](https://en.wikipedia.org/wiki/Ruby_on_Rails)
- [Stored procedure](https://en.wikipedia.org/wiki/Stored_procedure)
- [Synonym (database)](https://en.wikipedia.org/wiki/Synonym_(database))
- [Two-phase locking](https://en.wikipedia.org/wiki/Two-phase_locking)
- [Universally unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier)
- [Wikipedia:WikiProject Databases](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Databases)
- [Template:Database](https://en.wikipedia.org/wiki/Template:Database)
- [Template talk:Database](https://en.wikipedia.org/wiki/Template_talk:Database)
- [Category:Databases](https://en.wikipedia.org/wiki/Category:Databases)
- [Category:Types of databases](https://en.wikipedia.org/wiki/Category:Types_of_databases)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:26:52.223246+00:00_