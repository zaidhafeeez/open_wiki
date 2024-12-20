---
title: C3 linearization
url: https://en.wikipedia.org/wiki/C3_linearization
language: en
categories: ["Category:All Wikipedia articles needing clarification", "Category:Articles with example Python (programming language) code", "Category:CS1 maint: multiple names: authors list", "Category:Object-oriented programming", "Category:Programming language implementation", "Category:Wikipedia articles needing clarification from April 2018"]
references: 0
last_modified: 2024-12-13T14:33:52Z
---

# C3 linearization

## Summary

"In object-oriented systems with multiple inheritance,
some mechanism must be used for resolving conflicts when inheriting different definitions of the same property
from multiple superclasses." C3 superclass linearization is an algorithm used primarily to obtain the order in which methods should be inherited in the presence of multiple inheritance. In other words, the output of C3 superclass linearization is a deterministic Method Resolution Order (MRO).  
C3 superclass linearization is called 

## Full Content

"In object-oriented systems with multiple inheritance,
some mechanism must be used for resolving conflicts when inheriting different definitions of the same property
from multiple superclasses." C3 superclass linearization is an algorithm used primarily to obtain the order in which methods should be inherited in the presence of multiple inheritance. In other words, the output of C3 superclass linearization is a deterministic Method Resolution Order (MRO).  
C3 superclass linearization is called C3 because it "is consistent with three properties": 

a consistent extended precedence graph,
preservation of local precedence order, and
fitting a monotonicity criterion.
It was first published at the 1996 OOPSLA conference, in a paper entitled "A Monotonic Superclass Linearization for Dylan".  It was adapted to the Open Dylan implementation in January 2012 following an enhancement proposal. It has been chosen as the default algorithm for method resolution in Python 2.3 (and newer), Raku, Parrot, Solidity, and PGF/TikZ's Object-Oriented Programming module. It is also available as an alternative, non-default MRO in the core of Perl 5 starting with version 5.10.0. An extension implementation for earlier versions of Perl 5 named Class::C3 exists on CPAN.
Python's Guido van Rossum summarizes C3 superclass linearization thus:

Basically, the idea behind C3 is that if you write down all of the ordering rules imposed by inheritance relationships in a complex class hierarchy, the algorithm will determine a monotonic ordering of the classes that satisfies all of them. If such an ordering can not be determined, the algorithm will fail.

Description
The C3 superclass linearization of a class is the sum of the class plus a unique merge of the linearizations of its parents and a list of the parents itself. The list of parents as the last argument to the merge process preserves the local precedence order of direct parent classes.
The merge of parents' linearizations and parents list is done by selecting the first head of the lists which does not appear in the tail (all elements of a list except the first) of any of the lists. Note, that a good head may appear as the first element in multiple lists at the same time, but it is forbidden to appear anywhere else. The selected element is removed from all the lists where it appears as a head and appended to the output list. The process of selecting and removing a good head to extend the output list is repeated until all remaining lists are exhausted. If at some point no good head can be selected, because the heads of all remaining lists appear in any one tail of the lists, then the merge is impossible to compute due to inconsistent orderings of dependencies in the inheritance hierarchy and no linearization of the original class exists.
A naive divide-and-conquer approach to computing the linearization of a class may invoke the algorithm recursively to find the linearizations of parent classes for the merge-subroutine. However, this will result in an infinitely looping recursion in the presence of a cyclic class hierarchy. To detect such a cycle and to break the infinite recursion (and to reuse the results of previous computations as an optimization), the recursive invocation should be shielded against re-entrance of a previous argument by means of a cache or memoization.
This algorithm is similar to finding a topological ordering.

Example
Given

the linearization of Z is computed as

Example demonstrated in Python 3
First, a metaclass to enable a short representation of the objects by name instead of the default class REPR value:

Next, we define our base classes:

Then we construct the inheritance tree:

And now:

Example demonstrated in Raku
Raku uses C3 linearization for classes by default:

(the Any and Mu are the types all Raku objects inherit from, so Any stands in place of O)


== References ==
