# Prepared statement

## Article Metadata

- **Last Updated:** 2024-12-14T19:43:04.457459+00:00
- **Original Article:** [Prepared statement](https://en.wikipedia.org/wiki/Prepared_statement)
- **Language:** en
- **Page ID:** 33211278

## Summary

In database management systems (DBMS), a prepared statement, parameterized statement, or parameterized query is a feature where the database pre-compiles SQL code and stores the results, separating it from data. Benefits of prepared statements are:

efficiency, because they can be used repeatedly without re-compiling
security, by reducing or eliminating SQL injection attacks
A prepared statement takes the form of a pre-compiled template into which constant values are substituted during each exec

## Categories

- Category:All articles containing potentially dated statements
- Category:Articles containing potentially dated statements from 2007
- Category:Articles with example C Sharp code
- Category:Articles with example Java code
- Category:Articles with example PHP code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Databases
- Category:SQL
- Category:Short description matches Wikidata

## Table of Contents

- Software support
- Examples
- See also

## Content

In database management systems (DBMS), a prepared statement, parameterized statement, or parameterized query is a feature where the database pre-compiles SQL code and stores the results, separating it from data. Benefits of prepared statements are:

efficiency, because they can be used repeatedly without re-compiling
security, by reducing or eliminating SQL injection attacks
A prepared statement takes the form of a pre-compiled template into which constant values are substituted during each execution, and typically use SQL DML statements such as INSERT, SELECT, or UPDATE.
A common workflow for prepared statements is:

Prepare: The application creates the statement template and sends it to the DBMS. Certain values are left unspecified, called parameters, placeholders or bind variables (labelled "?" below):
INSERT INTO products (name, price) VALUES (?, ?);
Compile: The DBMS compiles (parses, optimizes and translates) the statement template, and stores the result without executing it.
Execute: The application supplies (or binds) values for the parameters of the statement template, and the DBMS executes the statement (possibly returning a result). The application may request the DBMS to execute the statement many times with different values. In the above example, the application might supply the values "bike" for the first parameter and "10900" for the second parameter, and then later the values "shoes" and "7400".
The alternative to a prepared statement is calling SQL directly from the application source code in a way that combines code and data. The direct equivalent to the above example is:

Not all optimization can be performed at the time the statement template is compiled, for two reasons: the best plan may depend on the specific values of the parameters, and the best plan may change as tables and indexes change over time.
On the other hand, if a query is executed only once, server-side prepared statements can be slower because of the additional round-trip to the server. Implementation limitations may also lead to performance penalties; for example, some versions of MySQL did not cache results of prepared queries. 
A stored procedure, which is also precompiled and stored on the server for later execution, has similar advantages. Unlike a stored procedure, a prepared statement is not normally written in a procedural language and cannot use or modify variables or use control flow structures, relying instead on the declarative database query language. Due to their simplicity and client-side emulation, prepared statements are more portable across vendors.

Software support
Major DBMSs, including SQLite, MySQL, Oracle, IBM Db2, Microsoft SQL Server and PostgreSQL support prepared statements. Prepared statements are normally executed through a non-SQL binary protocol for efficiency and protection from SQL injection, but with some DBMSs such as MySQL prepared statements are also available using a SQL syntax for debugging purposes. 
A number of programming languages support prepared statements in their standard libraries and will emulate them on the client side even if the underlying DBMS does not support them, including Java's JDBC, Perl's DBI, PHP's PDO and Python's DB-API. Client-side emulation can be faster for queries which are executed only once, by reducing the number of round trips to the server, but is usually slower for queries executed many times. It resists SQL injection attacks equally effectively.
Many types of SQL injection attacks can be eliminated by disabling literals, effectively requiring the use of prepared statements; as of 2007 only H2 supports this feature.

Examples
Go
The placeholder parameter syntax differs depending on your database. MySQL, SQL Server and SQLite use the ? notation, but PostgreSQL uses the $N notation. For example, if you were using PostgreSQL instead you would write:

Java JDBC
This example uses Java and JDBC:

Java PreparedStatement provides "setters" (setInt(int), setString(String), setDouble(double), etc.) for all major built-in data types.

PHP PDO
This example uses PHP and PDO:

Perl DBI
This example uses Perl and DBI:

C# ADO.NET
This example uses C# and ADO.NET:

ADO.NET SqlCommand will accept any type for the value parameter of AddWithValue, and type conversion occurs automatically. Note the use of "named parameters" (i.e. "@username") rather than "?"—this allows you to use a parameter multiple times and in any arbitrary order within the query command text.
However, the AddWithValue method should not be used with variable length data types, like varchar and nvarchar. This is because .NET assumes the length of the parameter to be the length of the given value, rather than getting the actual length from the database via reflection. The consequence of this is that a different query plan is compiled and stored for each different length. In general, the maximum number of "duplicate" plans is the product of the lengths of the variable length columns as specified in the database. For this reason, it is important to use the standard Add method for variable length columns:
command.Parameters.Add(ParamName, VarChar, ParamLength).Value = ParamValue, where ParamLength is the length as specified in the database.
Since the standard Add method needs to be used for variable length data types, it is a good habit to use it for all parameter types.

Python DB-API
This example uses Python and DB-API:

Magic Direct SQL
This example uses Direct SQL from Fourth generation language like eDeveloper, uniPaaS and magic XPA from Magic Software Enterprises

Virtual username  Alpha 20   init: 'sister'
Virtual password  Alpha 20   init: 'yellow'

SQL Command:   SELECT * FROM users WHERE USERNAME=:1 AND PASSWORD=:2

Input Arguments: 
1:  username
2:  password

PureBasic
PureBasic (since v5.40 LTS) can manage 7 types of link with the following commands

SetDatabaseBlob, SetDatabaseDouble, SetDatabaseFloat, SetDatabaseLong, SetDatabaseNull, SetDatabaseQuad, SetDatabaseString

There are 2 different methods depending on the type of database
For SQLite, ODBC, MariaDB/Mysql use: ? 

For PostgreSQL use: $1, $2, $3, ...

See also
Code injection


== References ==

## Related Articles

### Internal Links

- [Fourth-generation programming language](https://en.wikipedia.org/wiki/Fourth-generation_programming_language)
- [ADO.NET](https://en.wikipedia.org/wiki/ADO.NET)
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Code injection](https://en.wikipedia.org/wiki/Code_injection)
- [Database](https://en.wikipedia.org/wiki/Database)
- [Data manipulation language](https://en.wikipedia.org/wiki/Data_manipulation_language)
- [Database](https://en.wikipedia.org/wiki/Database)
- [H2 (database)](https://en.wikipedia.org/wiki/H2_(database))
- [IBM Db2](https://en.wikipedia.org/wiki/IBM_Db2)
- [Insert (SQL)](https://en.wikipedia.org/wiki/Insert_(SQL))
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Java Database Connectivity](https://en.wikipedia.org/wiki/Java_Database_Connectivity)
- [Magic Software Enterprises](https://en.wikipedia.org/wiki/Magic_Software_Enterprises)
- [Microsoft SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server)
- [MySQL](https://en.wikipedia.org/wiki/MySQL)
- [Oracle Database](https://en.wikipedia.org/wiki/Oracle_Database)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Perl DBI](https://en.wikipedia.org/wiki/Perl_DBI)
- [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)
- [PureBasic](https://en.wikipedia.org/wiki/PureBasic)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Query optimization](https://en.wikipedia.org/wiki/Query_optimization)
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [SQL injection](https://en.wikipedia.org/wiki/SQL_injection)
- [SQLite](https://en.wikipedia.org/wiki/SQLite)
- [Select (SQL)](https://en.wikipedia.org/wiki/Select_(SQL))
- [Stored procedure](https://en.wikipedia.org/wiki/Stored_procedure)
- [Template processor](https://en.wikipedia.org/wiki/Template_processor)
- [Update (SQL)](https://en.wikipedia.org/wiki/Update_(SQL))
- [Category:Articles containing potentially dated statements from 2007](https://en.wikipedia.org/wiki/Category:Articles_containing_potentially_dated_statements_from_2007)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:43:04.457459+00:00_