# Set (abstract data type)

## Metadata
- **Last Updated:** 2024-12-05 11:27:27 UTC
- **Original Article:** [Set (abstract data type)](https://en.wikipedia.org/wiki/Set_(abstract_data_type))
- **Language:** en
- **Page ID:** 201127

## Summary
In computer science, a set is an abstract data type that can store unique values, without any particular order. It is a computer implementation of the mathematical concept of a finite set. Unlike most other collection types, rather than retrieving a specific element from a set, one typically tests a value for membership in a set.
Some set data structures are designed for static or frozen sets that do not change after they are constructed. Static sets allow only query operations on their elements — such as checking whether a given value is in the set, or enumerating the values in some arbitrary order.  Other variants, called dynamic or mutable sets, allow also the insertion and deletion of elements from the set.
A multiset is a special kind of set in which an element can appear multiple times in the set.

## Categories
This article belongs to the following categories:

- Category:Abstract data types
- Category:All articles needing additional references
- Category:Articles needing additional references from October 2011
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Composite data types
- Category:Data types
- Category:Short description is different from Wikidata
- Category:Wikipedia articles needing clarification from November 2020

## Table of Contents

- Type theory
- Operations
- Implementations
- Language support
- Multiset
- See also
- Notes

## Content

In computer science, a set is an abstract data type that can store unique values, without any particular order. It is a computer implementation of the mathematical concept of a finite set. Unlike most other collection types, rather than retrieving a specific element from a set, one typically tests a value for membership in a set.
Some set data structures are designed for static or frozen sets that do not change after they are constructed. Static sets allow only query operations on their elements — such as checking whether a given value is in the set, or enumerating the values in some arbitrary order.  Other variants, called dynamic or mutable sets, allow also the insertion and deletion of elements from the set.
A multiset is a special kind of set in which an element can appear multiple times in the set.

Type theory
In type theory, sets are generally identified with their indicator function (characteristic function): accordingly, a set of values of type 
  
    
      
        A
      
    
    {\displaystyle A}
  
 may be denoted by 
  
    
      
        
          2
          
            A
          
        
      
    
    {\displaystyle 2^{A}}
  
 or 
  
    
      
        
          
            P
          
        
        (
        A
        )
      
    
    {\displaystyle {\mathcal {P}}(A)}
  
. (Subtypes and subsets may be modeled by refinement types, and quotient sets may be replaced by setoids.) The characteristic function 
  
    
      
        F
      
    
    {\displaystyle F}
  
 of a set 
  
    
      
        S
      
    
    {\displaystyle S}
  
 is defined as:

  
    
      
        F
        (
        x
        )
        =
        
          
            {
            
              
                
                  1
                  ,
                
                
                  
                    
                      if 
                    
                  
                  x
                  ∈
                  S
                
              
              
                
                  0
                  ,
                
                
                  
                    
                      if 
                    
                  
                  x
                  ∉
                  S
                
              
            
            
          
        
      
    
    {\displaystyle F(x)={\begin{cases}1,&{\mbox{if }}x\in S\\0,&{\mbox{if }}x\not \in S\end{cases}}}
  

In theory, many other abstract data structures can be viewed as set structures with additional operations and/or additional axioms imposed on the standard operations. For example, an abstract heap can be viewed as a set structure with a min(S) operation that returns the element of smallest value.

Operations
Core set-theoretical operations
One may define the operations of the algebra of sets:

union(S,T): returns the union of sets S and T.
intersection(S,T): returns the intersection of  sets S and T.
difference(S,T): returns the difference of sets S and T.
subset(S,T): a predicate that tests whether the set S is a subset of set T.

Static sets
Typical operations that may be provided by a static set structure S are:

is_element_of(x,S): checks whether the value x is in the set S.
is_empty(S): checks whether the set S is empty.
size(S) or cardinality(S): returns the number of elements in S.
iterate(S): returns a function that returns one more value of S at each call, in some arbitrary order.
enumerate(S): returns a list containing the elements of S in some arbitrary order.
build(x1,x2,…,xn,): creates a set structure with values x1,x2,...,xn.
create_from(collection): creates a new set structure containing all the elements of the given collection or all the elements returned by the given iterator.

Dynamic sets
Dynamic set structures typically add:

create(): creates a new, initially empty set structure.
create_with_capacity(n): creates a new set structure, initially empty but capable of holding up to n elements.
add(S,x): adds the element x to S, if it is not present already.
remove(S, x): removes the element x from S, if it is present.
capacity(S): returns the maximum number of values that S can hold.
Some set structures may allow only some of these operations. The cost of each operation will depend on the implementation, and possibly also on the particular values stored in the set, and the order in which they are inserted.

Additional operations
There are many other operations that can (in principle) be defined in terms of the above, such as:

pop(S): returns an arbitrary element of S, deleting it from S.
pick(S): returns an arbitrary element of S. Functionally, the mutator pop can be interpreted as the pair of selectors (pick, rest), where rest returns the set consisting of all elements except for the arbitrary element. Can be interpreted in terms of iterate.
map(F,S): returns the set of distinct values resulting from applying function F to each element of S.
filter(P,S): returns the subset containing all elements of S that satisfy a given predicate P.
fold(A0,F,S): returns the value A|S| after applying Ai+1 := F(Ai, e) for each element e of S, for some binary operation F. F must be associative and commutative for this to be well-defined.
clear(S): delete all elements of S.
equal(S1', S2'): checks whether the two given sets are equal (i.e. contain all and only the same elements).
hash(S): returns a hash value for the static set S such that if equal(S1, S2) then hash(S1) = hash(S2)
Other operations can be defined for sets with elements of a special type:

sum(S): returns the sum of all elements of S for some definition of "sum". For example, over integers or reals, it may be defined as fold(0, add, S).
collapse(S): given a set of sets, return the union. For example, collapse({{1}, {2, 3}}) == {1, 2, 3}. May be considered a kind of sum.
flatten(S): given a set consisting of sets and atomic elements (elements that are not sets), returns a set whose elements are the atomic elements of the original top-level set or elements of the sets it contains. In other words, remove a level of nesting – like collapse, but allow atoms. This can be done a single time, or recursively flattening to obtain a set of only atomic elements. For example, flatten({1, {2, 3}}) == {1, 2, 3}.
nearest(S,x): returns the element of S that is closest in value to x (by some metric).
min(S), max(S): returns the minimum/maximum element of S.

Implementations
Sets can be implemented using various data structures, which provide different time and space trade-offs for various operations.  Some implementations are designed to improve the efficiency of very specialized operations, such as nearest or union.  Implementations described as "general use" typically strive to optimize the element_of, add, and delete operations. A simple implementation is to use a list, ignoring the order of the elements and taking care to avoid repeated values. This is simple but inefficient, as operations like set membership or element deletion are O(n), as they require scanning the entire list. Sets are often instead implemented using more efficient data structures, particularly various flavors of trees, tries, or hash tables.
As sets can be interpreted as a kind of map (by the indicator function), sets are commonly implemented in the same way as (partial) maps (associative arrays) – in this case in which the value of each key-value pair has the unit type or a sentinel value (like 1) – namely, a self-balancing binary search tree for sorted sets (which has O(log n) for most operations), or a hash table for unsorted sets (which has O(1) average-case, but O(n) worst-case, for most operations).  A sorted linear hash table may be used to provide deterministically ordered sets.
Further, in languages that support maps but not sets, sets can be implemented in terms of maps. For example, a common programming idiom in Perl that converts an array to a hash whose values are the sentinel value 1, for use as a set, is:

Other popular methods include arrays. In particular a subset of the integers 1..n can be implemented efficiently as an n-bit bit array, which also support very efficient union and intersection operations. A Bloom map implements a set probabilistically, using a very compact representation but risking a small chance of false positives on queries.
The Boolean set operations can be implemented in terms of more elementary operations (pop, clear, and add), but specialized algorithms may yield lower asymptotic time bounds.  If sets are implemented as sorted lists, for example, the naive algorithm for union(S,T) will take time proportional to the length m of S times the length n of T; whereas a variant of the list merging algorithm will do the job in time proportional to m+n.  Moreover, there are specialized set data structures (such as the union-find data structure) that are optimized for one or more of these operations, at the expense of others.

Language support
One of the earliest languages to support sets was Pascal; many languages now include it, whether in the core language or in a standard library.

In C++, the Standard Template Library (STL) provides the set template class, which is typically implemented using a binary search tree (e.g. red–black tree); SGI's STL also provides the hash_set template class, which implements a set using a hash table. C++11 has support for the unordered_set template class, which is implemented using a hash table. In sets, the elements themselves are the keys, in contrast to sequenced containers, where elements are accessed using their (relative or absolute) position. Set elements must have a strict weak ordering.
The Rust standard library provides the generic HashSet and BTreeSet types.
Java offers the Set interface to support sets (with the HashSet class implementing it using a hash table), and the SortedSet sub-interface to support sorted sets (with the TreeSet class implementing it using a binary search tree).
Apple's Foundation framework (part of Cocoa) provides the Objective-C classes NSSet, NSMutableSet, NSCountedSet, NSOrderedSet, and NSMutableOrderedSet. The CoreFoundation APIs provide the CFSet and CFMutableSet types for use in C.
Python has built-in set and frozenset types since 2.4, and since Python 3.0 and 2.7, supports non-empty set literals using a curly-bracket syntax, e.g.: {x, y, z}; empty sets must be created using set(), because Python uses {} to represent the empty dictionary.
The .NET Framework provides the generic HashSet and SortedSet classes that implement the generic ISet interface.
Smalltalk's class library includes Set and IdentitySet, using equality and identity for inclusion test respectively. Many dialects provide variations for compressed storage (NumberSet, CharacterSet), for ordering (OrderedSet, SortedSet, etc.) or for weak references (WeakIdentitySet).
Ruby's standard library includes a set module which contains Set and SortedSet classes that implement sets using hash tables, the latter allowing iteration in sorted order.
OCaml's standard library contains a Set module, which implements a functional set data structure using binary search trees.
The GHC implementation of Haskell provides a Data.Set module, which implements immutable sets using binary search trees.
The Tcl Tcllib package provides a set module which implements a set data structure based upon TCL lists.
The Swift standard library contains a Set type, since Swift 1.2.
JavaScript introduced Set as a standard built-in object with the ECMAScript 2015 standard.
Erlang's standard library has a sets module.
Clojure has literal syntax for hashed sets, and also implements sorted sets.
LabVIEW has native support for sets, from version 2019.
Ada provides the Ada.Containers.Hashed_Sets and Ada.Containers.Ordered_Sets packages.
As noted in the previous section, in languages which do not directly support sets but do support associative arrays, sets can be emulated using associative arrays, by using the elements as keys, and using a dummy value as the values, which are ignored.

Multiset
A generalization of the notion of a set is that of a multiset or bag, which is similar to a set but allows repeated ("equal") values (duplicates). This is used in two distinct senses: either equal values are considered identical, and are simply counted, or equal values are considered equivalent, and are stored as distinct items. For example, given a list of people (by name) and ages (in years), one could construct a multiset of ages, which simply counts the number of people of a given age. Alternatively, one can construct a multiset of people, where two people are considered equivalent if their ages are the same (but may be different people and have different names), in which case each pair (name, age) must be stored, and selecting on a given age gives all the people of a given age.
Formally, it is possible for objects in computer science to be considered "equal" under some equivalence relation but still distinct under another relation. Some types of multiset implementations will store distinct equal objects as separate items in the data structure; while others will collapse it down to one version (the first one encountered) and keep a positive integer count of the multiplicity of the element.
As with sets, multisets can naturally be implemented using hash table or trees, which yield different performance characteristics.
The set of all bags over type T is given by the expression bag T. If by multiset one considers equal items identical and simply counts them, then a multiset can be interpreted as a function from the input domain to the non-negative integers (natural numbers), generalizing the identification of a set with its indicator function. In some cases a multiset in this counting sense may be generalized to allow negative values, as in Python.

C++'s Standard Template Library implements both sorted and unsorted multisets. It provides the multiset class for the sorted multiset, as a kind of associative container, which implements this multiset using a self-balancing binary search tree. It provides the unordered_multiset class for the unsorted multiset, as a kind of unordered associative container, which implements this multiset using a hash table. The unsorted multiset is standard as of C++11; previously SGI's STL provides the hash_multiset class, which was copied and eventually standardized.
For Java, third-party libraries provide multiset functionality:
Apache Commons Collections provides the Bag and SortedBag interfaces, with implementing classes like HashBag and TreeBag.
Google Guava provides the Multiset interface, with implementing classes like HashMultiset and TreeMultiset.
Apple provides the NSCountedSet class as part of Cocoa, and the CFBag and CFMutableBag types as part of CoreFoundation.
Python's standard library includes collections.Counter, which is similar to a multiset.
Smalltalk includes the Bag class, which can be instantiated to use either identity or equality as predicate for inclusion test.
Where a multiset data structure is not available, a workaround is to use a regular set, but override the equality predicate of its items to always return "not equal" on distinct objects (however, such will still not be able to store multiple occurrences of the same object) or use an associative array mapping the values to their integer multiplicities (this will not be able to distinguish between equal elements at all).
Typical operations on bags:

contains(B, x): checks whether the element x is present (at least once) in the bag B
is_sub_bag(B1, B2): checks whether each element in the bag B1 occurs in B1 no more often than it occurs in the bag B2; sometimes denoted as B1 ⊑ B2.
count(B, x): returns the number of times that the element x occurs in the bag B; sometimes denoted as B # x.
scaled_by(B, n): given a natural number n, returns a bag which contains the same elements as the bag B, except that every element that occurs m times in B occurs n * m times in the resulting bag; sometimes denoted as n ⊗ B.
union(B1, B2): returns a bag containing just those values that occur in either the bag B1 or the bag B2, except that the number of times a value x occurs in the resulting bag is equal to (B1 # x) + (B2 # x); sometimes denoted as B1 ⊎ B2.

Multisets in SQL
In relational databases, a table can be a (mathematical) set or a multiset, depending on the presence of unicity constraints on some columns (which turns it into a candidate key).
SQL allows the selection of rows from a relational table: this operation will in general yield a multiset, unless the keyword DISTINCT is used to force the rows to be all different, or the selection includes the primary (or a candidate) key.
In ANSI SQL the MULTISET keyword can be used to transform a subquery into a collection expression:

is a general select that can be used as subquery expression of another more general query, while

transforms the subquery into a collection expression that can be used in another query, or in assignment to a column of appropriate collection type.

See also
Bloom filter
Disjoint set
Set (mathematics)

Notes


== References ==

## Archive Info
- **Archived on:** 2024-12-15 21:06:00 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 17238 bytes
- **Word Count:** 2621 words
