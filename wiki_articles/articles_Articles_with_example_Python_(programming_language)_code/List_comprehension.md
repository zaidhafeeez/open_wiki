# List comprehension

## Article Metadata

- **Last Updated:** 2024-12-14T19:39:54.484863+00:00
- **Original Article:** [List comprehension](https://en.wikipedia.org/wiki/List_comprehension)
- **Language:** en
- **Page ID:** 275744

## Summary

A list comprehension is a syntactic construct available in some programming languages for creating a list based on existing lists. It follows the form of the mathematical set-builder notation (set comprehension) as distinct from the use of map and filter functions.

## Categories

- Category:Articles with example Haskell code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Racket code
- Category:Articles with example code
- Category:Articles with short description
- Category:Programming constructs
- Category:Short description is different from Wikidata

## Table of Contents

- Overview
- History
- Examples in different programming languages
- Similar constructs
- See also
- Notes and references
- External links

## Content

A list comprehension is a syntactic construct available in some programming languages for creating a list based on existing lists. It follows the form of the mathematical set-builder notation (set comprehension) as distinct from the use of map and filter functions.

Overview
Consider the following example in mathematical set-builder notation.

  
    
      
        S
        =
        {
        2
        ⋅
        x
        ∣
        x
        ∈
        
          N
        
        ,
         
        
          x
          
            2
          
        
        >
        3
        }
      
    
    {\displaystyle S=\{2\cdot x\mid x\in \mathbb {N} ,\ x^{2}>3\}}
  

or often

  
    
      
        S
        =
        {
        2
        ⋅
        x
        :
        x
        ∈
        
          N
        
        ,
         
        
          x
          
            2
          
        
        >
        3
        }
      
    
    {\displaystyle S=\{2\cdot x:x\in \mathbb {N} ,\ x^{2}>3\}}
  

This can be read, "
  
    
      
        S
      
    
    {\displaystyle S}
  
 is the set of all numbers "2 times 
  
    
      
        x
      
    
    {\displaystyle x}
  
" SUCH THAT 
  
    
      
        x
      
    
    {\displaystyle x}
  
 is an ELEMENT or MEMBER of the set of natural numbers (
  
    
      
        
          N
        
      
    
    {\displaystyle \mathbb {N} }
  
), AND 
  
    
      
        x
      
    
    {\displaystyle x}
  
 squared is greater than 
  
    
      
        3
      
    
    {\displaystyle 3}
  
."
The smallest natural number, x = 1, fails to satisfy the condition x2>3 (the condition 12>3 is false) so 2 ·1 is not included in S. The next natural number, 2, does satisfy the condition (22>3) as does every other natural number. Thus x consists of 2, 3, 4, 5... Since the set S consists of all numbers "2 times x" it is given by S = {4, 6, 8, 10,...}. S is, in other words, the set of all even numbers greater than 2.
In this annotated version of the example:

  
    
      
        S
        =
        {
        
          
            
              
                2
                ⋅
                x
              
              ⏟
            
          
          
            
              
                output expression
              
            
          
        
        ∣
        
          
            
              x
              ⏟
            
          
          
            
              
                variable
              
            
          
        
        ∈
        
          
            
              
                N
              
              ⏟
            
          
          
            
              
                input set
              
            
          
        
        ,
         
        
          
            
              
                
                  x
                  
                    2
                  
                
                >
                3
              
              ⏟
            
          
          
            
              
                predicate
              
            
          
        
        }
      
    
    {\displaystyle S=\{\underbrace {2\cdot x} _{\color {Violet}{\text{output expression}}}\mid \underbrace {x} _{\color {Violet}{\text{variable}}}\in \underbrace {\mathbb {N} } _{\color {Violet}{\text{input set}}},\ \underbrace {x^{2}>3} _{\color {Violet}{\text{predicate}}}\}}
  

  
    
      
        x
      
    
    {\displaystyle x}
  
 is the variable representing members of an input set.

  
    
      
        
          N
        
      
    
    {\displaystyle \mathbb {N} }
  
 represents the input set, which in this example is the set of natural numbers

  
    
      
        
          x
          
            2
          
        
        >
        3
      
    
    {\displaystyle x^{2}>3}
  
 is a predicate expression acting as a filter on members of the input set.

  
    
      
        2
        ⋅
        x
      
    
    {\displaystyle 2\cdot x}
  
 is an output expression producing members of the new set from members of the input set that satisfy the predicate expression.

  
    
      
        {
        }
      
    
    {\displaystyle \{\}}
  
 braces indicate that the result is a set

  
    
      
        ∣
      
    
    {\displaystyle \mid }
  
 
  
    
      
        ,
      
    
    {\displaystyle ,}
  
 the vertical bar is read as "SUCH THAT". The bar and the colon ":" are used interchangeably.
commas separate the predicates and can be read as "AND".
A list comprehension has the same syntactic components to represent generation of a list in order from an input list or iterator:

A variable representing members of an input list.
An input list (or iterator).
An optional predicate expression.
And an output expression producing members of the output list from members of the input iterable that satisfy the predicate.
The order of generation of members of the output list is based on the order of items in the input.
In Haskell's list comprehension syntax, this set-builder construct would be written similarly, as:

Here, the list [0..] represents 
  
    
      
        
          N
        
      
    
    {\displaystyle \mathbb {N} }
  
, x^2>3 represents the predicate, and 2*x represents the output expression.
List comprehensions give results in a defined order (unlike the members of sets); and list comprehensions may generate the members of a list in order, rather than produce the entirety of the list thus allowing, for example, the previous Haskell definition of the members of an infinite list.

History
The existence of related constructs predates the use of the term "List Comprehension". The SETL programming language (1969) has a set formation construct which is similar to list comprehensions. E.g., this code prints all prime numbers from 2 to N:

print([n in [2..N] | forall m in {2..n - 1} | n mod m > 0]);

The computer algebra system AXIOM (1973) has a similar construct that processes streams.
The first use of the term "comprehension" for such constructs was in Rod Burstall and John Darlington's description of their functional programming language NPL from 1977. In his retrospective "Some History of Functional Programming Languages", David Turner recalls:

NPL was implemented in POP2 by Burstall and used for Darlington’s work on program transformation (Burstall & Darlington 1977). The language was first order, strongly (but not polymorphically) typed, purely functional, call-by-value. It also had “set expressions” e.g.
setofeven (X)  <=  <:x : x in X & even(x):>}}
In a footnote attached to the term "list comprehension", Turner also notes

I initially called these ZF expressions, a reference to Zermelo–Fraenkel set theory — it was Phil Wadler who coined the better term list comprehension.
Burstall and Darlington's work with NPL influenced many functional programming languages during the 1980s, but not all included list comprehensions. An exception was Turner's influential, pure, lazy, functional programming language Miranda, released in 1985. The subsequently developed standard pure lazy functional language Haskell includes many of Miranda's features, including list comprehensions.
Comprehensions were proposed as a query notation for databases and were implemented in the Kleisli database query language.

Examples in different programming languages
Similar constructs
Monad comprehension
In Haskell, a monad comprehension is a generalization of the list comprehension to other monads in functional programming.

Set comprehension
The Python language introduces syntax for set comprehensions starting in version 2.7. Similar in form to list comprehensions, set comprehensions generate Python sets instead of lists.

Racket set comprehensions generate Racket sets instead of lists.

Dictionary comprehension
The Python language introduced a new syntax for dictionary comprehensions in version 2.7, similar in form to list comprehensions but which generate Python dicts instead of lists.

Racket hash table comprehensions generate Racket hash tables (one implementation of the Racket dictionary type).

Parallel list comprehension
The Glasgow Haskell Compiler has an extension called parallel list comprehension (also known as zip-comprehension) that permits multiple independent branches of qualifiers within the list comprehension syntax.
Whereas qualifiers separated by commas are dependent ("nested"), qualifier branches separated by pipes are evaluated in parallel (this does not refer to any form of multithreadedness: it merely means that the branches are zipped).

Racket's comprehensions standard library contains parallel and nested versions of its comprehensions, distinguished by "for" vs "for*" in the name. For example, the vector comprehensions "for/vector" and "for*/vector" create vectors by parallel versus nested iteration over sequences. The following is Racket code for the Haskell list comprehension examples.

In Python, we could do as follows:

In Julia, practically the same results can be achieved as follows:

with the only difference that instead of lists, in Julia, we have arrays.

XQuery and XPath
Like the original NPL use, these are fundamentally database access languages.
This makes the comprehension concept more important, because it is computationally infeasible to retrieve the entire list and operate on it (the initial 'entire list' may be an entire XML database).
In XPath, the expression:

is conceptually evaluated as a series of "steps" where each step produces a list and the next step applies a filter function to each element in the previous step's output.
In XQuery, full XPath is available, but FLWOR statements are also used, which is a more powerful comprehension construct.

Here the XPath //book is evaluated to create a sequence (aka list); the where clause is a functional "filter", the order by sorts the result, and the <shortBook>...</shortBook> XML snippet is actually an anonymous function that builds/transforms XML for each element in the sequence using the 'map' approach found in other functional languages.
So, in another functional language the above FLWOR statement may be implemented like this:

LINQ in C#
C# 3.0 has a group of related features called LINQ, which defines a set of query operators for manipulating object enumerations.

It also offers an alternative comprehension syntax, reminiscent of SQL:

LINQ provides a capability over typical list comprehension implementations. When the root object of the comprehension implements the IQueryable interface, rather than just executing the chained methods of the comprehension, the entire sequence of commands are converted into an abstract syntax tree (AST) object, which is passed to the IQueryable object to interpret and execute.
This allows, amongst other things, for the IQueryable to

rewrite an incompatible or inefficient comprehension
translate the AST into another query language (e.g. SQL) for execution

C++
C++ does not have any language features directly supporting list comprehensions but operator overloading (e.g., overloading |, >>, >>=) has been used successfully to provide expressive syntax for "embedded" query domain-specific languages (DSL). Alternatively, list comprehensions can be constructed using the erase-remove idiom to select elements in a container and the STL algorithm for_each to transform them.

There is some effort in providing C++ with list-comprehension constructs/syntax similar to the set builder notation.

In Boost. Range [1] library there is a notion of adaptors [2] that can be applied to any range and do filtering, transformation etc. With this library, the original Haskell example would look like (using Boost.Lambda [3] for anonymous filtering and transforming functions) (Full example):
This implementation uses a macro and overloads the << operator. It evaluates any expression valid inside an 'if', and any variable name may be chosen. It's not threadsafe, however. Usage example:

This implementation provides head/tail slicing using classes and operator overloading, and the | operator for filtering lists (using functions). Usage example:

Language for Embedded Query and Traversal (LEESA) is an embedded DSL in C++ that implements X-Path-like queries using operator overloading. The queries are executed on richly typed  xml trees obtained using xml-to-c++ binding from an XSD. There is absolutely no string encoding. Even the names of the xml tags are classes and therefore, there is no way for typos. If a LEESA expression forms an incorrect path that does not exist in the data model, the C++ compiler will reject the code.Consider a catalog xml.

LEESA provides >> for XPath's / separator. XPath's // separator that "skips" intermediate nodes in the tree is implemented in LEESA using what's known as Strategic Programming. In the example below, catalog_, book_, author_, and name_ are instances of catalog, book, author, and name classes, respectively.

See also
Set-builder notation
The SELECT statement together with its FROM and WHERE clauses in SQL

Notes and references
List Comprehension in The Free On-line Dictionary of Computing, Editor Denis Howe.
Wadler, Philip (1990). "Comprehending Monads". Proceedings of the 1990 ACM Conference on LISP and Functional Programming, Nice.

External links
SQL-like set operations with list comprehension one-liners in the Python Cookbook
Discussion on list comprehensions in Scheme and related constructs
List Comprehensions across languages

Axiom
Axiom stream examples

Clojure
Clojure API documentation - for macro

Common Lisp
Implementation of a Lisp comprehension macro by Guy Lapalme

Haskell
The Haskell 98 Report, chapter 3.11 List Comprehensions.
The Glorious Glasgow Haskell Compilation System User's Guide, chapter 7.3.4 Parallel List Comprehensions.
The Hugs 98 User's Guide, chapter 5.1.2 Parallel list comprehensions (a.k.a. zip-comprehensions).

OCaml
OCaml Batteries Included
Language extensions introduced in OCaml Batteries Included

Python
The Python Tutorial, List Comprehensions.
Python Language Reference, List displays.
Python Enhancement Proposal PEP 202: List Comprehensions.
Python Language Reference, Generator expressions.
Python Enhancement Proposal PEP 289: Generator Expressions.

## Related Articles

### Internal Links

- [Abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
- [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- [Associative array](https://en.wikipedia.org/wiki/Associative_array)
- [Axiom (computer algebra system)](https://en.wikipedia.org/wiki/Axiom_(computer_algebra_system))
- [Boost (C++ libraries)](https://en.wikipedia.org/wiki/Boost_(C%2B%2B_libraries))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Comparison of programming languages (list comprehension)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(list_comprehension))
- [Computer algebra system](https://en.wikipedia.org/wiki/Computer_algebra_system)
- [David Turner (computer scientist)](https://en.wikipedia.org/wiki/David_Turner_(computer_scientist))
- [Domain-specific language](https://en.wikipedia.org/wiki/Domain-specific_language)
- [Erase–remove idiom](https://en.wikipedia.org/wiki/Erase%E2%80%93remove_idiom)
- [FLWOR](https://en.wikipedia.org/wiki/FLWOR)
- [Filter (higher-order function)](https://en.wikipedia.org/wiki/Filter_(higher-order_function))
- [Generator (computer programming)](https://en.wikipedia.org/wiki/Generator_(computer_programming))
- [Glasgow Haskell Compiler](https://en.wikipedia.org/wiki/Glasgow_Haskell_Compiler)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Heinrich Kleisli](https://en.wikipedia.org/wiki/Heinrich_Kleisli)
- [Iterator](https://en.wikipedia.org/wiki/Iterator)
- [John Darlington](https://en.wikipedia.org/wiki/John_Darlington)
- [Language Integrated Query](https://en.wikipedia.org/wiki/Language_Integrated_Query)
- [List (abstract data type)](https://en.wikipedia.org/wiki/List_(abstract_data_type))
- [Map (higher-order function)](https://en.wikipedia.org/wiki/Map_(higher-order_function))
- [Miranda (programming language)](https://en.wikipedia.org/wiki/Miranda_(programming_language))
- [Monad (functional programming)](https://en.wikipedia.org/wiki/Monad_(functional_programming))
- [NPL (programming language)](https://en.wikipedia.org/wiki/NPL_(programming_language))
- [Natural number](https://en.wikipedia.org/wiki/Natural_number)
- [Operator overloading](https://en.wikipedia.org/wiki/Operator_overloading)
- [Philip Wadler](https://en.wikipedia.org/wiki/Philip_Wadler)
- [Predicate (mathematical logic)](https://en.wikipedia.org/wiki/Predicate_(mathematical_logic))
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Racket (programming language)](https://en.wikipedia.org/wiki/Racket_(programming_language))
- [Rod Burstall](https://en.wikipedia.org/wiki/Rod_Burstall)
- [SETL](https://en.wikipedia.org/wiki/SETL)
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [Select (SQL)](https://en.wikipedia.org/wiki/Select_(SQL))
- [Set-builder notation](https://en.wikipedia.org/wiki/Set-builder_notation)
- [Set (abstract data type)](https://en.wikipedia.org/wiki/Set_(abstract_data_type))
- [Stream (computing)](https://en.wikipedia.org/wiki/Stream_(computing))
- [Syntax (programming languages)](https://en.wikipedia.org/wiki/Syntax_(programming_languages))
- [Thread safety](https://en.wikipedia.org/wiki/Thread_safety)
- [World Wide Web Consortium](https://en.wikipedia.org/wiki/World_Wide_Web_Consortium)
- [W3Schools](https://en.wikipedia.org/wiki/W3Schools)
- [Zermelo–Fraenkel set theory](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:39:54.484863+00:00_