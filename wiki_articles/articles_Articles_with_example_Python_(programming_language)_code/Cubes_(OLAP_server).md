# Cubes (OLAP server)

## Article Metadata

- **Last Updated:** 2024-12-14T19:36:00.848861+00:00
- **Original Article:** [Cubes (OLAP server)](https://en.wikipedia.org/wiki/Cubes_(OLAP_server))
- **Language:** en
- **Page ID:** 46348793

## Summary

Cubes is a light-weight open source multidimensional modelling and OLAP toolkit for development reporting applications and browsing of aggregated data written in Python programming language released under the MIT License.
Cubes provides to an analyst or any application end-user "understandable and natural way of reporting using concept of data Cubes – multidimensional data objects".
Cubes was first publicly released in March 2011. The project was originally developed for Public Procurements of S

## Categories

- Category:Articles with example Python (programming language) code
- Category:Data analysis software
- Category:Data warehousing
- Category:Official website different in Wikidata and Wikipedia
- Category:Python (programming language) scientific libraries
- Category:Python (programming language) software
- Category:SQL

## Table of Contents

- Features
- Model
- Operations
- Server
- ROLAP and SQL
- See also
- References
- External links

## Content

Cubes is a light-weight open source multidimensional modelling and OLAP toolkit for development reporting applications and browsing of aggregated data written in Python programming language released under the MIT License.
Cubes provides to an analyst or any application end-user "understandable and natural way of reporting using concept of data Cubes – multidimensional data objects".
Cubes was first publicly released in March 2011. The project was originally developed for Public Procurements of Slovakia. Cubes 1.0 was released in September 2014 and presented on the PyData Conference in New York

Features
OLAP and aggregated browsing (default is ROLAP)
logical model of OLAP cubes in JSON or provided from external sources
hierarchical dimensions (attributes that have hierarchical dependencies, such as category-subcategory or country-region)
multiple hierarchies in a dimension
arithmetic expressions for computing derived measures and aggregates
localizable metadata and data
Cubes is capable of handling large amounts of data and complex queries. According to a review by TechTarget, Cubes can handle "data volumes in the hundreds of millions of rows" and "complex queries and calculations that require multi-level aggregations and dynamic subsetting." Additionally, the review notes that Cubes is well-suited for smaller organizations or teams that don't require the complexity and scalability of enterprise-level OLAP solutions.

Model
The logical conceptual model in Cubes is described using JSON and can be provided either in a form of a file, directory bundle or from an external model provider (for example a database). The basic model objects are: cubes and their measures and aggregates, dimensions and their attributes, hierarchies. Logical model also contains mapping from logical attributes to their physical location in a database (or other data source).
Example model:

Operations
Cubes provides basic set of operations such as Data drilling and filtering (slicing and dicing). The operations can be accessed either through Python interface or through a light web server called Slicer.
Example of the python interface:

Server
The Cubes provides a non-traditional OLAP server with HTTP queries and JSON response API. Example query to get "total amount of all contracts between January 2012 and June 2016 by month":
http://localhost:5000/cube/contracts/aggregate?drilldown=date&drilldown=criteria&cut=date:2012,1-2012,6&order=date.month:desc
The response looks like:

The simple HTTP/JSON interface makes it very easy to integrate OLAP reports in web applications written in pure HTML and JavaScript.
The Slicer server contains endpoints describing the cube metadata which helps to create generic reporting applications that don't have to know the database model structure and conceptual hierarchies up-in-front.
The Slicer server is written using the Flask (web framework).

ROLAP and SQL
The built-in SQL backend of the framework provides ROLAP functionality on top a relational database. Cubes contains a SQL query generator that translates the reporting queries into SQL statements. The query generator takes into account topology of the star or snowflake schema and executes only joins that are necessary to retrieve attributes required by the data analyst.
The SQL backend uses SQLAlchemy Python toolkit to construct the queries.

See also
SQLAlchemy

References
External links
Official website

## Related Articles

### Internal Links

- [API](https://en.wikipedia.org/wiki/API)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Data drilling](https://en.wikipedia.org/wiki/Data_drilling)
- [Expression (mathematics)](https://en.wikipedia.org/wiki/Expression_(mathematics))
- [Flask (web framework)](https://en.wikipedia.org/wiki/Flask_(web_framework))
- [Government procurement](https://en.wikipedia.org/wiki/Government_procurement)
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [Internationalization and localization](https://en.wikipedia.org/wiki/Internationalization_and_localization)
- [JSON](https://en.wikipedia.org/wiki/JSON)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [MIT License](https://en.wikipedia.org/wiki/MIT_License)
- [Measure (data warehouse)](https://en.wikipedia.org/wiki/Measure_(data_warehouse))
- [Online analytical processing](https://en.wikipedia.org/wiki/Online_analytical_processing)
- [OLAP cube](https://en.wikipedia.org/wiki/OLAP_cube)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Online analytical processing](https://en.wikipedia.org/wiki/Online_analytical_processing)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [SQLAlchemy](https://en.wikipedia.org/wiki/SQLAlchemy)
- [Slovakia](https://en.wikipedia.org/wiki/Slovakia)
- [Snowflake schema](https://en.wikipedia.org/wiki/Snowflake_schema)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Star schema](https://en.wikipedia.org/wiki/Star_schema)
- [Topology](https://en.wikipedia.org/wiki/Topology)
- [Web server](https://en.wikipedia.org/wiki/Web_server)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:36:00.848861+00:00_