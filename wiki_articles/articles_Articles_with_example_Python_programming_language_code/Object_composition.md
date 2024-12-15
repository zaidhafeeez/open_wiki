# Object composition

## Metadata
- **Last Updated:** 2024-12-03 06:57:25 UTC
- **Original Article:** [Object composition](https://en.wikipedia.org/wiki/Object_composition)
- **Language:** en
- **Page ID:** 1911078

## Summary
In computer science, object composition and object aggregation are closely related ways to combine objects or data types into more complex ones. In conversation, the distinction between composition and aggregation is often ignored. Common kinds of compositions are objects used in object-oriented programming,  tagged unions, sets, sequences, and various graph structures. Object compositions relate to, but are not the same as, data structures. 
Object composition refers to the logical or conceptual structure of the information, not the implementation or physical data structure used to represent it. For example, a sequence differs from a set because (among other things) the order of the composed items matters for the former but not the latter. Data structures such as arrays, linked lists, hash tables, and many others can be used to implement either of them. Perhaps confusingly, some of the same terms are used for both data structures and composites. For example, "binary tree" can refer to either: as a data structure it is a means of accessing a linear sequence of items, and the actual positions of items in the tree are irrelevant (the tree can be internally rearranged however one likes, without changing its meaning). However, as an object composition, the positions are relevant, and changing them would change the meaning (as for example in cladograms).

## Categories
This article belongs to the following categories:

- Category:All Wikipedia articles written in American English
- Category:All articles with too many examples
- Category:All articles with unsourced statements
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with too many examples from August 2010
- Category:Articles with unsourced statements from April 2018
- Category:Articles with unsourced statements from October 2020
- Category:CS1 maint: others
- Category:Object (computer science)
- Category:Short description matches Wikidata
- Category:Unified Modeling Language
- Category:Use American English from January 2019
- Category:Use mdy dates from January 2019
- Category:Wikipedia articles with style issues from August 2010

## Table of Contents

- Programming technique
- UML modeling technique
- Aggregation
- Special forms
- Composite types in C
- Timeline of composition in various languages
- See also
- References
- External links

## Content

In computer science, object composition and object aggregation are closely related ways to combine objects or data types into more complex ones. In conversation, the distinction between composition and aggregation is often ignored. Common kinds of compositions are objects used in object-oriented programming,  tagged unions, sets, sequences, and various graph structures. Object compositions relate to, but are not the same as, data structures. 
Object composition refers to the logical or conceptual structure of the information, not the implementation or physical data structure used to represent it. For example, a sequence differs from a set because (among other things) the order of the composed items matters for the former but not the latter. Data structures such as arrays, linked lists, hash tables, and many others can be used to implement either of them. Perhaps confusingly, some of the same terms are used for both data structures and composites. For example, "binary tree" can refer to either: as a data structure it is a means of accessing a linear sequence of items, and the actual positions of items in the tree are irrelevant (the tree can be internally rearranged however one likes, without changing its meaning). However, as an object composition, the positions are relevant, and changing them would change the meaning (as for example in cladograms).

Programming technique
Object-oriented programming is based on using objects to encapsulate data and behavior.  It uses two main techniques for assembling and composing functionality into more complex ones, sub-typing and object composition. Object composition is about combining objects within compound objects, and at the same time, ensuring the encapsulation of each object by using their well-defined interface  without visibility of their internals. In this regard, object composition differs from data structures, which do not enforce encapsulation. 
Object composition may also be about a group of multiple related objects, such as a set or a sequence of objects. Delegation may enrich composition by forwarding requests or calls made to the enclosing composite object to one of its internal components. 
In class-based and typed programming languages, types can be divided into composite and non-composite types, and composition can be regarded as a relationship between types: an object of a composite type (e.g. car) "has" objects of other types (e.g. wheel). When a composite object contains several sub-objects of the same type, they may be assigned to particular roles, often distinguished by names or numbers. For example, a Point object might contain 3 numbers, each representing distance along a different axis, such as 'x', 'y', and 'z'. The study of part-whole relationships in general, is mereology.  
Composition must be distinguished from subtyping, which is the process of adding detail to a general data type to create a more specific data type. For instance, cars may be a specific type of vehicle: car is a vehicle. Subtyping doesn't describe a relationship between different objects, but instead, says that objects of a type are simultaneously objects of another type. The study of such relationships is ontology. 
In prototype-based programming languages such as JavaScript, objects can dynamically inherit the behaviors from a prototype object at the moment of their instantiation. Composition must be distinguished from prototyping: the newly instantiated object inherits the composition of its prototype, but it may itself be composed on its own. 
Composite objects may be represented in storage by co-locating the composed objects, by co-locating references, or in many other ways. The items within a composite object may be referred to as attributes, fields, members, properties, or other names, and the resulting composition as composite type, storage record, structure, tuple, or a user-defined type (UDT). For details, see the aggregation section below.

UML modeling technique
In UML modeling, objects can be conceptually composed, independently of the implementation with a programming language.  There are four ways of composing objects in UML: property, association, aggregation and composition: 

A property represents an attribute of the class.
An association represents a semantic relationship between instances of the associated classes.  The member-end of an association corresponds to a property of the associated class.
An aggregation is a kind of association that models a part/whole relationship between an aggregate (whole) and a group of related components (parts).
A composition, also called a composite aggregation, is a kind of aggregation that models a part/whole relationship between a composite (whole) and a group of exclusively owned parts.
The relationship between the aggregate and its components is a weak "has-a" relationship: The components may be part of several aggregates, may be accessed through other objects without going through the aggregate, and may outlive the aggregate object. The state of the component object still forms part of the aggregate object.
The relationship between the composite and its parts is a strong “has-a” relationship: The composite object has sole "responsibility for the existence and storage of the composed objects", the composed object can be part of at most one composite, and "If a composite object is deleted, all of its part instances that are objects are deleted with it".  Thus in UML, composition has a more narrow meaning than the usual object composition.

The graphical notation represents:

the property as a typed element in the box of the enclosing class,
the association as a plain line between the associated classes,
the aggregation as an unfilled diamond on the side of the aggregate and a solid line,
the composition as a filled diamond on the side of the composite and a solid line.

Aggregation
Aggregation differs from ordinary composition in that it does not imply ownership. In composition, when the owning object is destroyed, so are the contained objects. In aggregation, this is not necessarily true. For example, a university owns various departments (e.g., chemistry), and each department has a number of professors. If the university closes, the departments will no longer exist, but the professors in those departments will continue to exist. Therefore, a university can be seen as a composition of departments, whereas departments have an aggregation of professors. In addition, a professor could work in more than one department, but a department could not be part of more than one university.
Composition is usually implemented such that an object contains another object. For example, in C++:

In aggregation, the object may only contain a reference or pointer to the object (and not have lifetime responsibility for it).
Sometimes aggregation is referred to as composition when the distinction between ordinary composition and aggregation is unimportant.
The above code would transform into the following UML Class diagram:

Aggregation in COM
In Microsoft's Component Object Model, aggregation means that an object exports, as if it were their owner, one or several interfaces of another object it owns. Formally, this is more similar to composition or encapsulation than aggregation. However, instead of implementing the exported interfaces by calling the interfaces of the owned object, the interfaces of the owned object themselves are exported. The owned object is responsible for assuring that methods of those interfaces inherited from IUnknown actually invoke the corresponding methods of the owner. This is to guarantee that the reference count of the owner is correct and all interfaces of the owner are accessible through the exported interface, while no other (private) interfaces of the owned object are accessible.

Special forms
Containment
Composition that is used to store several instances of the composited data type is referred to as containment. Examples of such containers are arrays, associative arrays, binary trees, and linked lists.
In UML, containment is depicted with a multiplicity of  0..* or 1..*, indicating that the composite object is composed of an unknown number of instances of the composed class.

Recursive composition
Objects can be composed recursively, and their type is then called recursive type. Examples includes various kinds of trees, DAGs, and graphs. Each node in a tree may be a branch or leaf; in other words, each node is a tree at the same time when it belongs to another tree.
In UML, recursive composition is depicted with an association, aggregation or composition of a class with itself.

Composite pattern
The composite design pattern is an object-oriented design based on composite types, that combines recursive composition and containment to implement complex part-whole hierarchies.

Composite types in C
This is an example of composition in C.

In this example, the primitive (noncomposite) types int, enum {job_seeking, professional, non_professional, retired, student} and the composite array type  char[] are combined to form the composite structure Person. Each Person structure then "has an" age, name, and an employment type.

Timeline of composition in various languages
C calls a record a struct or structure; object-oriented languages such as Java, Smalltalk, and C++ often keep their records hidden inside objects (class instances); languages in the ML family simply call them records. COBOL was the first widespread programming language to support records directly; ALGOL 68 got it from COBOL and Pascal got it, more or less indirectly, from ALGOL 68. Common Lisp provides structures and classes (the latter via the Common Lisp Object System).

1959 – COBOL

1960 – ALGOL 60
Arrays were the only composite data type in Algol 60.

1964 – PL/I
dcl 1 newtypet based (P);
 2 (a, b, c) fixed bin(31),
 2 (i, j, k) float,
 2 r ptr;
allocate newtypet;

1968 – ALGOL 68
int max = 99;
mode newtypet = [0..9] [0..max]struct (
 long real a, b, c, short int i, j, k, ref real r
);
newtypet newarrayt = (1, 2, 3, 4, 5, 6, heap real := 7)

For example, a linked list might be declared as:

mode node = union (real, int, compl, string),
 list = struct (node val, ref list next);

For ALGOL 68 only the type name appears to the left of the equality, and most notably the construction is made – and can be read – from left to right without regard to priorities.

1970 – Pascal

1972 – K&R C

1977 – FORTRAN 77
Fortran 77 has arrays, but lacked any formal record/structure definitions. Typically compound structures were built up using EQUIVALENCE or COMMON statements:

1983 – Ada
Ada 95 brought OOP concepts through tagged types (the equivalent of a C++ class), Ada 2012 added support for substitution verification through class-wide contracts. 
1983 – C++

1991 – Python

1992 – FORTRAN 90
Arrays and strings were inherited from FORTRAN 77, and a new reserved word was introduced: type

FORTRAN 90 updated and included FORTRAN IV's concept called NAMELIST.

1994 – ANSI Common Lisp
Common Lisp provides structures and the ANSI Common Lisp standard added CLOS classes.

For more details about composition in C/C++, see Composite type.

See also
C++ structure
Composite type
Composition over inheritance
Delegation (programming)
Function composition (computer science)
Has-a
Implementation inheritance
Inheritance semantics
Law of Demeter
Object-oriented analysis and design
Virtual inheritance

References
External links
Association, Aggregation and Composition, accessed in February 2009
Harald Störrle, UML2, Addison-Wesley, 2005

## Archive Info
- **Archived on:** 2024-12-15 20:38:34 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 11631 bytes
- **Word Count:** 1804 words
