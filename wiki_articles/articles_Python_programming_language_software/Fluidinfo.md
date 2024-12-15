# Fluidinfo

## Article Metadata

- **Last Updated:** 2024-12-15T03:43:39.579492+00:00
- **Original Article:** [Fluidinfo](https://en.wikipedia.org/wiki/Fluidinfo)
- **Language:** en
- **Page ID:** 24374755

## Summary

Fluidinfo, formerly named FluidDB until early 2011, is an online cloud data store based on an attribute-value centric data model. Fluidinfo is written in Python and characterized by a publicly writeable schema-less database that provides a  query language, a fine-grained permissions model and promotes data sharing, both publicly and in groups. The lack of an underlying RDBMS structure may classify Fluidinfo as a type of publicly writeable "collective database".

## Categories

- Category:Cloud storage
- Category:NoSQL
- Category:Python (programming language) software
- Category:Structured storage
- Category:Webarchive template archiveis links
- Category:Webarchive template wayback links

## Table of Contents

- Overview
- Current status
- See also
- References
- Further reading

## Content

Fluidinfo, formerly named FluidDB until early 2011, is an online cloud data store based on an attribute-value centric data model. Fluidinfo is written in Python and characterized by a publicly writeable schema-less database that provides a  query language, a fine-grained permissions model and promotes data sharing, both publicly and in groups. The lack of an underlying RDBMS structure may classify Fluidinfo as a type of publicly writeable "collective database".

Overview
Few data stores are available with the intent to provide public write-access, except in narrow contexts. Two examples of shareable data stores operating in specific contexts are del.icio.us (shareable bookmarks) and Twitter (micro-blogging service). Fluidinfo offers a generalized shareable data store, where potentially any piece or type of information can be shared with anybody else, if desired, striving for a balance between individual, group and communal data ownership. Author and blogger Robert Scoble described Fluidinfo as a "database that acts like a wiki".
Fluidinfo emphasizes three aspects that make it unique among existing public data stores:

Data model
Query language
Permissions

Data model
The data model aims to be as flexible as possible, permitting a wide range of information to be stored in Fluidinfo. The fundamental difference between attribute-value stores (along the lines of EAV schemas) and traditional RDBMS is the lack of a highly defined top-down structure. The essence of Fluidinfo consists of arbitrary objects, which can be considered points in a data space to which tags may be attached. Objects have no owners, similar to concepts in the "real" world. Tags are initially controlled by the user/application who creates them and can be attached to objects, in a fashion reminiscent of how humans use their minds to create and associate information with physical objects or
concepts. One of the underlying motivations of Fluidinfo is to make working with information more natural. Anyone can attach tags to any data object, but only people with the right roles can see and search these tags.

Query language
The query language was designed to perform complex queries in as simple a manner as possible. The syntax is superficially reminiscent of information retrieval query languages such as CQL which are characterized as less complicated than traditional database query languages such as SQL. The query language always return object identifiers based on tag values, using the predicates below:

Numeric: To find objects based on the numeric value of tags; e.g. tim/rating > 5
Textual: To find objects based on text matching of their tag values; e.g. sally/opinion matches fantastic
Presence: Use has to request objects that have a given tag; e.g. has sally/opinion
Set contents: A tag on an object can hold a set of strings. For example, a tag called mary/product-reviews/keywords might be on an object with a value of [ "cool", "kids", "adventure" ]. The contains operator can be used to select objects with a matching value. The query mary/product-reviews/keywords contains "kids" would match the object in this example.
Exclusion: You can exclude objects with the except keyword. For example, has nytimes.com/appeared except has james/seen. The except operator performs a set difference.
Logic: Query components can be combined with and and or. For example, has sara/rating and tim/rating > 5.
Grouping: Parentheses can be used to group query components. For example, has sara/rating and (tim/rating > 5 or mike/rating > 7).

Permissions
For each action that be applied to any tag or namespace within Fluidinfo, there is:

A policy (either 'open' or 'closed'); and
A (possibly empty) list of exceptions to the policy.
The various actions that can be performed on a tag are read, update, create and see. The combination of the various actions with policies and exceptions provides a fine-grained permission model within Fluidinfo. It should be re-emphasized that only tags and namespaces have permissions allowing for various levels of control. Objects (the basic Fluidinfo data structure) do not have owners and so cannot be controlled by users/applications.
Examples of the permission model in various states are shown in the table below:

Current status
The company Fluidinfo was founded in the UK in 2007 and operates out of New York City and Barcelona. Esther Dyson provided an early-stage angel investment in the company. Tim O'Reilly is also an investor in the company.
Fluidinfo launched in alpha as "FluidDB" on August 17, 2009. Developers can sign-up for access to Fluidinfo via their homepage. This is similar to the types of RESTful API access provided by other cloud services. The company changed the name of the product from "FluidDB" to "Fluidinfo" and won Top Technology Prize at the 2011 LAUNCH Conference. During SXSW 2011, Tim O'Reilly named Fluidinfo as his favorite startup.

See also
Freebase
databaseLiquid/DBLiquid
NoSQL
DBpedia
LinkedData
Semantic Web

References
Further reading
Fluidinfo homepage
Fluidinfo documentation
Fluidinfo general discussion group
Fluidinfo API/programmer discussion group
Fluidinfo Blog

## Related Articles

### Internal Links

- [Advanced Message Queuing Protocol](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol)
- [Archive.today](https://en.wikipedia.org/wiki/Archive.today)
- [Attribute–value system](https://en.wikipedia.org/wiki/Attribute%E2%80%93value_system)
- [Barcelona](https://en.wikipedia.org/wiki/Barcelona)
- [Cloud computing](https://en.wikipedia.org/wiki/Cloud_computing)
- [Contextual Query Language](https://en.wikipedia.org/wiki/Contextual_Query_Language)
- [DBpedia](https://en.wikipedia.org/wiki/DBpedia)
- [Data sharing](https://en.wikipedia.org/wiki/Data_sharing)
- [Delicious (website)](https://en.wikipedia.org/wiki/Delicious_(website))
- [Entity–attribute–value model](https://en.wikipedia.org/wiki/Entity%E2%80%93attribute%E2%80%93value_model)
- [Esther Dyson](https://en.wikipedia.org/wiki/Esther_Dyson)
- [Freebase (database)](https://en.wikipedia.org/wiki/Freebase_(database))
- [Information retrieval](https://en.wikipedia.org/wiki/Information_retrieval)
- [Jason Calacanis](https://en.wikipedia.org/wiki/Jason_Calacanis)
- [Linked data](https://en.wikipedia.org/wiki/Linked_data)
- [Apache Lucene](https://en.wikipedia.org/wiki/Apache_Lucene)
- [New York City](https://en.wikipedia.org/wiki/New_York_City)
- [NoSQL](https://en.wikipedia.org/wiki/NoSQL)
- [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Query language](https://en.wikipedia.org/wiki/Query_language)
- [Relational database](https://en.wikipedia.org/wiki/Relational_database)
- [REST](https://en.wikipedia.org/wiki/REST)
- [Robert Scoble](https://en.wikipedia.org/wiki/Robert_Scoble)
- [Role-oriented programming](https://en.wikipedia.org/wiki/Role-oriented_programming)
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [Semantic Web](https://en.wikipedia.org/wiki/Semantic_Web)
- [Social bookmarking](https://en.wikipedia.org/wiki/Social_bookmarking)
- [South by Southwest](https://en.wikipedia.org/wiki/South_by_Southwest)
- [Tag (metadata)](https://en.wikipedia.org/wiki/Tag_(metadata))
- [Apache Thrift](https://en.wikipedia.org/wiki/Apache_Thrift)
- [Tim O'Reilly](https://en.wikipedia.org/wiki/Tim_O%27Reilly)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Twitter](https://en.wikipedia.org/wiki/Twitter)
- [United Kingdom](https://en.wikipedia.org/wiki/United_Kingdom)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:43:39.579492+00:00_