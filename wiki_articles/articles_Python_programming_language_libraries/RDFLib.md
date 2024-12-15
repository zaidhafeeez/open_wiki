# RDFLib

## Metadata
- **Last Updated:** 2024-12-10 19:54:34 UTC
- **Original Article:** [RDFLib](https://en.wikipedia.org/wiki/RDFLib)
- **Language:** en
- **Page ID:** 5423881

## Summary
‹The template Manual is being considered for merging.› 

RDFLib is a Python library for working with RDF, a simple yet powerful language for representing information. This library contains parsers/serializers for almost all of the known RDF serializations, such as RDF/XML, Turtle, N-Triples, & JSON-LD, many of which are now supported in their updated form (e.g. Turtle 1.1). The library also contains both in-memory and persistent Graph back-ends for storing RDF information and numerous convenience functions for declaring graph namespaces, lodging SPARQL queries and so on. It is in continuous development with the most recent stable release, rdflib 6.1.1 having been released on 20 December 2021. It was originally created by Daniel Krech with the first release in November, 2002.
A number of other Python projects use rdflib for RDF manipulation, including:

OWL-RL - A simple implementation of the OWL2 RL Profile (reasoning engine)
pySHACL - a Python SHACL validator
pyLDAPI - an add-on module for the Python Flask web framework used to deliver Linked Data
pyLODE - a Web Ontology Language documentation tool

## Categories
This article belongs to the following categories:

- Category:All Wikipedia articles in need of updating
- Category:All articles to be expanded
- Category:All articles with empty sections
- Category:All articles with style issues
- Category:Articles to be expanded from July 2010
- Category:Articles with empty sections from July 2010
- Category:Articles with short description
- Category:Python (programming language) libraries
- Category:RDF data access
- Category:Resource Description Framework
- Category:Short description is different from Wikidata
- Category:Wikipedia articles in need of updating from October 2019
- Category:Wikipedia articles with style issues from July 2021

## Table of Contents

- History and status
- Overview
- References
- External links

## Content

‹The template Manual is being considered for merging.› 

RDFLib is a Python library for working with RDF, a simple yet powerful language for representing information. This library contains parsers/serializers for almost all of the known RDF serializations, such as RDF/XML, Turtle, N-Triples, & JSON-LD, many of which are now supported in their updated form (e.g. Turtle 1.1). The library also contains both in-memory and persistent Graph back-ends for storing RDF information and numerous convenience functions for declaring graph namespaces, lodging SPARQL queries and so on. It is in continuous development with the most recent stable release, rdflib 6.1.1 having been released on 20 December 2021. It was originally created by Daniel Krech with the first release in November, 2002.
A number of other Python projects use rdflib for RDF manipulation, including:

OWL-RL - A simple implementation of the OWL2 RL Profile (reasoning engine)
pySHACL - a Python SHACL validator
pyLDAPI - an add-on module for the Python Flask web framework used to deliver Linked Data
pyLODE - a Web Ontology Language documentation tool

History and status
Overview
RDFLib and Python idioms
RDFLib's use of various Python idioms mean it is fairly simple for programmers with only junior Python skills to manipulate RDF. On the other hand, the Python idioms are simple enough that someone familiar with RDF, but not Python, can probably work out how to use rdflib quite easily.
The core class in RDFLib is Graph which is a Python dictionary used to store collections of RDF triples in memory. It redefines certain built-in Python object methods in order to exhibit simple graph behaviour, such as simple graph merging via addition (i.e. g3 = g1 + g2).
RDFLib graphs emulate container types and are best thought of as a set of 3-item triples:

   set([
       (subject,predicate,object),
       (subject1,predicate1,object1),
       ...
       (subjectN,predicateN,objectN)
      ])

RDFLib graphs are not sorted containers; they have ordinary Python set operations, e.g. add() methods that search triples and return them in arbitrary order.

RDF graph terms
The following RDFLib classes (listed below) model RDF terms in a graph and inherit from a common Identifier class, which extends Python unicode. Instances of these are nodes in an RDF graph.

URIRef
BNode
Literal
Variable

Namespace utilities
RDFLib provides mechanisms for managing namespaces. In particular, there is a Namespace class which takes (as its only argument) the Base URI of the namespace. Fully qualified URIs in the namespace can be constructed by attribute / dictionary access on Namespace instances:

Graphs as iterators
RDFLib graphs also override __iter__ in order to support iteration over the contained triples:

Set operations on RDFLib graphs
__iadd__ and __isub__ are overridden to support adding and subtracting Graphs to/from each other (in place):

G1 += G1
G2 -= G2

Basic triple matching
RDFLib graphs support basic triple pattern matching with a triples((subject,predicate,object)) function. This function is a generator of triples that match the pattern given by the arguments. The arguments of these are RDF terms that restrict the triples that are returned. Terms that are None are treated as a wildcard.

RDF convenience APIs (RDF collections / containers)
Managing triples
Adding triples
Triples can be added in two ways:

They may be added with the parse(source, publicID=None, format="xml") function. The first argument can be a source of many kinds, but the most common is the serialization (in various formats: RDF/XML, Notation 3, N-Triples of an RDF graph as a string). The format parameter is one of turtle, n3, xml, n-triples or JSON-LD (this last when the JSON-LD plugin is used). publicID is the name of the graph into which the RDF serialization will be parsed.
Triples can also be added with the add function: add((subject, predicate, object)).

Removing triples
Similarly, triples can be removed by a call to remove: remove((subject, predicate, object))

RDF Literal support
RDFLib 'Literal's essentially behave like Unicode characters with an XML Schema datatype or language attribute. The class provides a mechanism to both convert Python literals (and their built-ins such as time/date/datetime) into equivalent RDF Literals and (conversely) convert Literals to their Python equivalent. There is some support of considering datatypes in comparing Literal instances, implemented as an override to __eq__. This mapping to and from Python literals is achieved with the following dictionaries:

Maps Python instances to WXS datatyped Literals

Maps WXS datatyped Literals to Python. This mapping is used by the toPython() method defined on all Literal instances.

SPARQL querying
RDFLIb supports a majority of the current SPARQL 1.1 specification and includes a harness for the publicly available RDF DAWG test suite.  Support for SPARQL is provided by two methods:

rdflib.graph.query() - used to pose SPARQL SELECT or ASK queries to a graph (or Store of Graphs)
rdflib.graph.update() - used to change graph content or return RDF using INSERT, DELETE and CONSTRUCT SPARQL statements

Serialization (NTriples, N3, and RDF/XML)
The RDF store API
A Universal RDF Store Interface
This document attempts to summarize some fundamental components of an RDF store. The motivation is to outline a standard set of interfaces for providing the necessary support needed in order to persist an RDF Graph in a way that is universal and not tied to any specific implementation. For the most part, the core RDF model is adhered to as well as terminology that is consistent with the RDF Model specifications. However, this suggested interface also extends an RDF store with additional requirements necessary to facilitate the aspects of Notation 3 that go beyond the RDF model to provide a framework for First Order Predicate Logic processing and persistence.

Terminology
Context
A named, unordered set of statements. Also could be called a sub-graph. The named graphs literature and ontology are relevant to this concept. A context could be thought of as only the relationship between an RDF triple and a sub-graph (this is how the term context is used in the Notation 3 Design Issues page) in which it is found or the sub-graph itself.
It's worth noting that the concept of logically grouping triples within an addressable 'set' or 'subgraph' is just barely beyond the scope of the RDF model. The RDF model defines a graph as an arbitrary collection of triples and the semantics of these triples, but doesn't give guidance on how to consistently address such arbitrary collections. Though a collection of triples can be thought of as a resource itself, the association between a triple and the collection it is a part of is not covered.
Conjunctive Graph
This refers to the 'top-level' Graph. It is the aggregation of all the contexts within it and is also the appropriate, absolute boundary for closed world assumptions / models. This distinction is the easily obtained part of RDF along the path to the semantic web and most of its value is in (corporate/enterprise) real-world problems:
There are at least two situations where the closed world assumption is used. The first is where it is assumed that a knowledge base contains all relevant facts. This is common in corporate databases. That is, the information it contains is assumed to be complete
From a store perspective, closed world assumptions also provide the benefit of better query response times due to the explicit closed world boundaries. Closed world boundaries can be made transparent by federated queries that assume each ConjunctiveGraph is a section of a larger, unbounded universe. So a closed world assumption does not preclude you from an open-world assumption.
For the sake of persistence, Conjunctive Graphs must be distinguished by identifiers (that may not necessarily be RDF identifiers or may be an RDF identifier normalized - SHA1/MD5 perhaps - for database naming purposes ) which could be referenced to indicate conjunctive queries (queries made across the entire conjunctive graph) or appear as nodes in asserted statements. In this latter case, such statements could be interpreted as being made about the entire 'known' universe. For example:

Quoted Statement
A statement that isn't asserted but is referred to in some manner. Most often, this happens when we want to make a statement about another statement (or set of statements) without necessarily saying these quoted statements (are true). For example:
Chimezie said "higher-order statements are complicated"
Which can be written as (in N3):

Formula
A context whose statements are quoted or hypothetical.
Context quoting can be thought of as very similar to reification. The main difference is that quoted statements are not asserted or considered as statements of truth about the universe and can be referenced as a group: a hypothetical RDF Graph
Universal Quantifiers / Variables. (relevant references):
OWL Definition of SWRL. (browse)
SWRL/RuleML Variable
Terms
Terms are the kinds of objects that can appear in a quoted/asserted triple. This includes those that are core to RDF:
Blank Nodes
URI References
Literals (which consist of a literal value, datatype and language tag)
Those that extend the RDF model into N3:
Formulae
Universal Quantifications (Variables)
And those that are primarily for matching against 'Nodes' in the underlying Graph:
REGEX Expressions
Date Ranges
Numerical Ranges
Nodes
Nodes are a subset of the Terms that the underlying store actually persists. The set of such Terms depends on whether or not the store is formula-aware. Stores that aren't formula-aware would only persist those terms core to the RDF Model, and those that are formula-aware would be able to persist the N3 extensions as well. However, utility terms that only serve the purpose for matching nodes by term-patterns probably will only be terms and not nodes.
"The set of nodes of an RDF graph is the set of subjects and objects of triples in the graph.
Context-aware
An RDF store capable of storing statements within contexts is considered context-aware. Essentially, such a store is able to partition the RDF model it represents into individual, named, and addressable sub-graphs.
Formula-aware
An RDF store capable of distinguishing between statements that are asserted and statements that are quoted is considered formula-aware.
Such a store is responsible for maintaining this separation and ensuring that queries against the entire model (the aggregation of all the contexts - specified by not limiting a 'query' to a specifically name context) do not include quoted statements. Also, it is responsible for distinguishing universal quantifiers (variables).
These 2 additional concepts (formulae and variables) must be thought of as core extensions and distinguishable from the other terms of a triple (for the sake of the persistence roundtrip - at the very least). It's worth noting that the 'scope' of universal quantifiers (variables) and existential quantifiers (BNodes) is the formula (or context - to be specific) in which their statements reside. Beyond this, a Formula-aware store behaves the same as a Context-aware store.
Conjunctive Query
Any query that doesn't limit the store to search within a named context only. Such a query expects a context-aware store to search the entire asserted universe (the conjunctive graph). A formula-aware store is expected not to include quoted statements when matching such a query.
N3 Round Trip
This refers to the requirements on a formula-aware RDF store's persistence mechanism necessary for it to be properly populated by a N3 parser and rendered as syntax by a N3 serializer.
Transactional Store
An RDF store capable of providing transactional integrity to the RDF operations performed on it.

Interpreting syntax
The following Notation 3 document:

Could cause the following statements to be asserted in the store:

This statement would be asserted in the partition associated with quoted statements (in a formula named _:a)

Finally, these statements would be asserted in the same partition (in a formula named _:b)

Formulae and Variables as Terms
Formulae and variables are distinguishable from URI references, Literals, and BNodes by the following syntax:

They must also be distinguishable in persistence to ensure they can be round tripped. Other issues regarding the persistence of N3 terms.

Database management
An RDF store should provide standard interfaces for the management of database connections. Such interfaces are standard to most database management systems (Oracle, MySQL, Berkeley DB, Postgres, etc..)
The following methods are defined to provide this capability:

def open(self, configuration, create=True) - Opens the store specified by the configuration string. If create is True a store will be created if it does not already exist. If create is False and a store does not already exist an exception is raised. An exception is also raised if a store exists, but there is insufficient permissions to open the store.
def close(self, commit_pending_transaction=False) - This closes the database connection. The commit_pending_transaction parameter specifies whether to commit all pending transactions before closing (if the store is transactional).
def destroy(self, configuration) - This destroys the instance of the store identified by the configuration string.
The configuration string is understood by the store implementation and represents all the necessary parameters needed to locate an individual instance of a store. This could be similar to an ODBC string, or in fact be an ODBC string if the connection protocol to the underlying database is ODBC. The open function needs to fail intelligently in order to clearly express that a store (identified by the given configuration string) already exists or that there is no store (at the location specified by the configuration string) depending on the value of create.

Triple interfaces
An RDF store could provide a standard set of interfaces for the manipulation, management, and/or retrieval of its contained triples (asserted or quoted):

def add(self, (subject, predicate, object), context=None, quoted=False) - Adds the given statement to a specific context or to the model. The quoted argument is interpreted by formula-aware stores to indicate this statement is quoted/hypothetical. It should be an error to not specify a context and have the quoted argument be True. It should also be an error for the quoted argument to be True when the store is not formula-aware.
def remove(self, (subject, predicate, object), context)
def triples(self, (subject, predicate, object), context=None) - Returns an iterator over all the triples (within the conjunctive graph or just the given context) matching the given pattern. The pattern is specified by providing explicit statement terms (which are used to match against nodes in the underlying store), or None - which indicates a wildcard. NOTE: This interface is expected to return an iterator of tuples of length 3, corresponding to the 3 terms of matching statements, which can be either of : URIRef, Blank Node, Literal, Formula, Variable, or (perhaps) a Context.
This function can be thought of as the primary mechanism for producing triples with nodes that match the corresponding terms and term pattern provided.
A conjunctive query can be indicated by either providing a value of NULL/None/Empty string value for context or the identifier associated with the Conjunctive Graph.

def __len__(self, context=None) - Number of statements in the store. This should only account for non-quoted (asserted) statements if the context is not specified, otherwise it should return the number of statements in the formula or context given.

Formula / context interfaces
These interfaces work on contexts and formulae (for stores that are formula-aware) interchangeably.

def contexts(self, triple=None) - Generator over all contexts in the graph. If triple is specified, a generator over all contexts the triple is in.
def remove_context(self, identifier) -

Named graphs / conjunctive graphs
RDFLib defines the following kinds of Graphs:

'Graph'(_store_,_identifier_)
'QuotedGraph'(_store_,_identifier_)
'ConjunctiveGraph'(_store_,_default_identifier_= None)
A Conjunctive Graph is the most relevant collection of graphs that are considered to be the boundary for closed world assumptions. This boundary is equivalent to that of the store instance (which is itself uniquely identified and distinct from other instances of Store that signify other Conjunctive Graphs). It is equivalent to all the named graphs within it and associated with a _default_ graph which is automatically assigned a BNode for an identifier - if one isn't given.

Formulae
RDFLib graphs support an additional extension of RDF semantics for formulae. For the academically inclined, Graham Klyne's 'formal' extension (see external links) is probably a good read.
Formulae are represented formally by the 'QuotedGraph' class and disjoint from regular RDF graphs in that their statements are quoted.

Persistence
RDFLib provides an abstracted Store API for persistence of RDF and Notation 3. The Graph class works with instances of this API (as the first argument to its constructor) for triple-based management of an RDF store including: garbage collection, transaction management, update, pattern matching, removal, length, and database management (_open_ / _close_ / _destroy_) . Additional persistence mechanisms can be supported by implementing this API for a different store. Currently supported databases:

HDT
MySQL
SQLite
Berkeley DB
Zope Object Database
Random-access memory
Redland RDF Application Framework
Store instances can be created with the plugin function:

'Higher-order' idioms
There are a few high-level APIs that extend RDFLib graphs into other Pythonic idioms. For more a more explicit Python binding, there are Sparta, SuRF & FunOWL.

References
External links
Official website 
RDFLib on GitHub

## Archive Info
- **Archived on:** 2024-12-15 20:27:34 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 18093 bytes
- **Word Count:** 2786 words
