# Hi/Lo algorithm

## Metadata
- **Last Updated:** 2024-11-09 16:36:03 UTC
- **Original Article:** [Hi/Lo algorithm](https://en.wikipedia.org/wiki/Hi/Lo_algorithm)
- **Language:** en
- **Page ID:** 62235560

## Summary
Hi/Lo is an algorithm and a key generation strategy used for generating unique keys for use in a database as a primary key. It uses a sequence-based hi-lo pattern to generate values. Hi/Lo is used in scenarios where an application needs its entities to have an identity prior to persistence. It is a value generation strategy. An alternative to Hi/Lo would be for the application to generate keys as universally unique identifiers (UUID).

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 15:18:53 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 4748 bytes
- **Word Count:** 762 words
