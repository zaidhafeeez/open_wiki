# Metaclass

## Article Metadata

- **Last Updated:** 2024-12-14T19:40:47.965229+00:00
- **Original Article:** [Metaclass](https://en.wikipedia.org/wiki/Metaclass)
- **Language:** en
- **Page ID:** 558359

## Summary

In object-oriented programming, a metaclass is a class whose instances are classes themselves. Unlike ordinary classes, which define the behaviors of objects, metaclasses specify the behaviors of classes and their instances. Not all object-oriented programming languages support the concept of metaclasses. For those that do, the extent of control metaclasses have over class behaviors varies. Metaclasses are often implemented by treating classes as first-class citizens, making a metaclass an objec

## Categories

- Category:All accuracy disputes
- Category:All articles needing additional references
- Category:All articles that may contain original research
- Category:All articles with style issues
- Category:Articles needing additional references from October 2013
- Category:Articles needing additional references from September 2013
- Category:Articles that may contain original research from September 2013
- Category:Articles with disputed statements from May 2015
- Category:Articles with example Python (programming language) code
- Category:Articles with multiple maintenance issues
- Category:Articles with short description
- Category:Class (computer programming)
- Category:Short description is different from Wikidata
- Category:Webarchive template wayback links
- Category:Wikipedia articles with style issues from September 2013

## Table of Contents

- Python example
- In Smalltalk-80
- In Ruby
- In Objective-C
- Support in languages and tools
- See also
- References
- External links

## Content

In object-oriented programming, a metaclass is a class whose instances are classes themselves. Unlike ordinary classes, which define the behaviors of objects, metaclasses specify the behaviors of classes and their instances. Not all object-oriented programming languages support the concept of metaclasses. For those that do, the extent of control metaclasses have over class behaviors varies. Metaclasses are often implemented by treating classes as first-class citizens, making a metaclass an object that creates and manages these classes. Each programming language adheres to its own metaobject protocol, which are the rules that determine interactions among objects, classes, and metaclasses. Metaclasses are utilized to automate code generation and to enhance framework development.

Python example
In Python, the builtin class type is a metaclass. Consider this simple Python class:

At run time, Car itself is an instance of type. The source code of the Car class, shown above, does not include such details as the size in bytes of Car objects, their binary layout in memory, how they are allocated, that the __init__ method is automatically called each time a Car is created, and so on. These details come into play not only when a new Car object is created, but also each time any attribute of a Car is accessed. In languages without metaclasses, these details are defined by the language specification and can't be overridden. In Python, the metaclass - type - controls these details of Car's behavior. They can be overridden by using a different metaclass instead of type.
The above example contains some redundant code to do with the four attributes make, model, year, and color. It is possible to eliminate some of this redundancy using a custom metaclass. In Python, a metaclass is most easily defined as a subclass of type.

This metaclass only overrides object creation.  All other aspects of class and object behavior are still handled by type.
Now the class Car can be rewritten to use this metaclass. In Python 3 this is done by providing a "keyword argument" metaclass to the class definition:

The resulting object Car can be instantiated as usual, but can contain any number of keyword arguments:

In Smalltalk-80
In Smalltalk, everything is an object. Additionally, Smalltalk is a class based system, which means that every object has a class that defines the structure of that object (i.e. the instance variables the object has) and the messages an object understands. Together this implies that a class in Smalltalk is an object and that, therefore a class needs to be an instance of a class (called metaclass).
As an example, a car object c is an instance of the class Car. In turn, the class Car is again an object and as such an instance of the metaclass of Car called Car class. Note the blank in the name of the metaclass. The name of the metaclass is the Smalltalk expression that, when evaluated, results in the metaclass object. Thus evaluating Car class results in the metaclass object for Car whose name is Car class (one can confirm this by evaluating Car class name which returns the name of the metaclass of Car.)
Class methods actually belong to the metaclass, just as instance methods actually belong to the class. When a message is sent to the object 2, the search for the method starts in Integer. If it is not found it proceeds up the superclass chain, stopping at Object whether it is found or not.
When a message is sent to Integer the search for the method starts in Integer class and proceeds up the superclass chain to Object class. Note that, so far, the metaclass inheritance chain exactly follows that of the class inheritance chain. But the metaclass chain extends further because Object class is the subclass of Class. All metaclasses are subclasses of Class.
In early Smalltalks, there was only one metaclass called Class. This implied that the methods all classes have were the same, in particular the method to create new objects, i.e., new. To allow classes to have their own methods and their own instance variables (called class instance variables and should not be confused with class variables), Smalltalk-80 introduced for each class C their own metaclass C class. This means that each metaclass is effectively a singleton class.
Since there is no requirement that metaclasses behave differently from each other, all metaclasses are instances of only one class called Metaclass. The metaclass of Metaclass is called Metaclass class which again is an instance of class Metaclass.
In Smalltalk-80, every class (except Object) has a superclass. The abstract superclass of all metaclasses is Class, which describes the general nature of classes.
The superclass hierarchy for metaclasses parallels that for classes, except for class Object. ALL metaclasses are subclasses of Class, therefore: 

Object class superclass == Class.
Like conjoined twins, classes and metaclasses are born together. Metaclass has an instance variable thisClass, which points to its conjoined class.
Note that the usual Smalltalk class browser does not show metaclasses as separate classes. Instead the class browser allows to edit the class together with its metaclass at the same time.
The names of classes in the metaclass hierarchy are easily confused with the concepts of the same name. For instance:

Object is the base class that provides common methods for all objects; "an object" is an integer, or a widget, or a Car, etc.
Class is the base of the metaclasses that provides common methods for all classes (though it is not a metaclass itself); "a class" is something like Integer, or Widget, or Car, etc.
Metaclass provides common methods for all metaclasses.
Four classes provide the facilities to describe new classes. Their inheritance hierarchy (from Object), and the main facilities they provide are:

Object - default behavior common to all objects, like class access
Behavior - minimum state for compiling methods and creating/running objects
ClassDescription (abstract class) - class/variable naming, comments
Class - similar, more comprehensive, facilities to superclasses
Metaclass - initializing class variables, instance creation messages

In Ruby
Ruby purifies the Smalltalk-80 concept of metaclasses by introducing eigenclasses,
removing the Metaclass class,
and (un)redefining the class-of map.
The change can be schematized as follows:

Note in particular the correspondence between Smalltalk's implicit metaclasses and Ruby's eigenclasses of classes.
The Ruby eigenclass model makes the concept of implicit metaclasses fully uniform: every object x has its own meta-object, called the eigenclass of x, which is one meta-level higher than x. The "higher order" eigenclasses usually exist purely conceptually – they do not contain any methods or store any (other) data in most Ruby programs.
The following diagrams show a sample core structure of Smalltalk-80 and Ruby in comparison.
In both languages, the structure consists of a built-in part which contains the circular objects (i.e. objects that appear in a cycle formed by a combination of blue or green links) and a user-part which has four explicit objects: classes A and B
and terminal objects u and v.
Green links show the child→parent relation of inheritance (with the implicit upward direction), blue links show the complementary member→container relation of instantiation (a blue link from x points to the least actual container of x that is the start point for the method lookup when a method is invoked on x). Gray nodes display the eigenclasses (resp. implicit metaclasses in the case of Smalltalk-80).

The diagram on the right also provides a picture of lazy evaluation of eigenclasses in Ruby. The v object can have its eigenclass evaluated (allocated) as a consequence of adding singleton methods to v.
According to the Ruby's introspection method named class,
the class of every class (and of every eigenclass) is
constantly the Class class (denoted by c in the diagram).
Class, and Struct are the only classes that have classes as instances.  Subclassing of Class is disallowed.
Following the standard definition of metaclasses we can conclude that Class and Struct are the only metaclasses in Ruby.
This seems to contradict the correspondence between Ruby and Smalltalk,
since in Smalltalk-80, every class has its own metaclass.
The discrepancy is based on the disagreement between
the class introspection method in Ruby and Smalltalk. While the map x ↦ x.class coincides on terminal objects, it differs in the restriction to classes. As already mentioned above, for a class x, the Ruby expression x.class evaluates constantly to Class. In Smalltalk-80, if x is a class then the expression x class corresponds
to the Ruby's x.singleton_class
– which evaluates to the eigenclass of x.

In Objective-C
Metaclasses in Objective-C are almost the same as those in Smalltalk-80—not surprising since Objective-C borrows a lot from Smalltalk. Like Smalltalk, in Objective-C, the instance variables and methods are defined by an object's class. A class is an object, hence it is an instance of a metaclass.
Like Smalltalk, in Objective-C, class methods are simply methods called on the class object, hence a class's class methods must be defined as instance methods in its metaclass. Because different classes can have different sets of class methods, each class must have its own separate metaclass. Classes and metaclasses are always created as a pair: the runtime has functions objc_allocateClassPair() and objc_registerClassPair() to create and register class-metaclass pairs, respectively.
There are no names for the metaclasses; however, a pointer to any class object can be referred to with the generic type Class (similar to the type id being used for a pointer to any object).
Because class methods are inherited through inheritance, like Smalltalk, metaclasses must follow an inheritance scheme paralleling that of classes (e.g. if class A's parent class is class B, then A's metaclass's parent class is B's metaclass), except that of the root class.
Unlike Smalltalk, the metaclass of the root class inherits from the root class (usually NSObject using the Cocoa framework) itself. This ensures that all class objects are ultimately instances of the root class, so that you can use the instance methods of the root class, usually useful utility methods for objects, on class objects themselves.
Since metaclass objects do not behave differently (you cannot add class methods for a metaclass, so metaclass objects all have the same methods), they are all instances of the same class—the metaclass of the root class (unlike Smalltalk). Thus, the metaclass of the root class is an instance of itself. The reason for this is that all metaclasses inherit from root class; hence, they must inherit the class methods of the root class.

Support in languages and tools
The following are some of the most prominent programming languages that support metaclasses.

Common Lisp, via CLOS
Delphi and other versions of Object Pascal influenced by it
Groovy
Objective-C
ooRexx
Python
Perl, via the metaclass pragma, as well as Moose
Ruby
Smalltalk
C++ (proposed for a possible inclusion in future version of the standard)
Some less widespread languages that support metaclasses include OpenJava, OpenC++, OpenAda, CorbaScript, ObjVLisp, Object-Z, MODEL-K, XOTcl, and MELDC. Several of these languages date from the early 1990s and are of academic interest.
Logtalk, an object-oriented extension of Prolog, also supports metaclasses.
Resource Description Framework (RDF) and Unified Modeling Language (UML) both support metaclasses.

See also
References
External links
What Is a Metaclass?

## Related Articles

### Internal Links

- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Abstract data type](https://en.wikipedia.org/wiki/Abstract_data_type)
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Adapter pattern](https://en.wikipedia.org/wiki/Adapter_pattern)
- [Algebraic data type](https://en.wikipedia.org/wiki/Algebraic_data_type)
- [Arbitrary-precision arithmetic](https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic)
- [Array (data type)](https://en.wikipedia.org/wiki/Array_(data_type))
- [Associative array](https://en.wikipedia.org/wiki/Associative_array)
- [Bfloat16 floating-point format](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format)
- [Bit](https://en.wikipedia.org/wiki/Bit)
- [Bit array](https://en.wikipedia.org/wiki/Bit_array)
- [Boolean data type](https://en.wikipedia.org/wiki/Boolean_data_type)
- [Bottom type](https://en.wikipedia.org/wiki/Bottom_type)
- [Boxing (computer programming)](https://en.wikipedia.org/wiki/Boxing_(computer_programming))
- [Byte](https://en.wikipedia.org/wiki/Byte)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [Character (computing)](https://en.wikipedia.org/wiki/Character_(computing))
- [Class-based programming](https://en.wikipedia.org/wiki/Class-based_programming)
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Class browser](https://en.wikipedia.org/wiki/Class_browser)
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Class variable](https://en.wikipedia.org/wiki/Class_variable)
- [Cocoa (API)](https://en.wikipedia.org/wiki/Cocoa_(API))
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Common Lisp Object System](https://en.wikipedia.org/wiki/Common_Lisp_Object_System)
- [Compiler](https://en.wikipedia.org/wiki/Compiler)
- [Complex data type](https://en.wikipedia.org/wiki/Complex_data_type)
- [Composite data type](https://en.wikipedia.org/wiki/Composite_data_type)
- [Conjoined twins](https://en.wikipedia.org/wiki/Conjoined_twins)
- [Container (abstract data type)](https://en.wikipedia.org/wiki/Container_(abstract_data_type))
- [CorbaScript](https://en.wikipedia.org/wiki/CorbaScript)
- [Data structure](https://en.wikipedia.org/wiki/Data_structure)
- [Data type](https://en.wikipedia.org/wiki/Data_type)
- [Decimal data type](https://en.wikipedia.org/wiki/Decimal_data_type)
- [Delphi (software)](https://en.wikipedia.org/wiki/Delphi_(software))
- [Dependent type](https://en.wikipedia.org/wiki/Dependent_type)
- [Double-precision floating-point format](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)
- [Empty type](https://en.wikipedia.org/wiki/Empty_type)
- [Enumerated type](https://en.wikipedia.org/wiki/Enumerated_type)
- [Exception handling](https://en.wikipedia.org/wiki/Exception_handling)
- [Extended precision](https://en.wikipedia.org/wiki/Extended_precision)
- [First-class citizen](https://en.wikipedia.org/wiki/First-class_citizen)
- [Fixed-point arithmetic](https://en.wikipedia.org/wiki/Fixed-point_arithmetic)
- [Floating-point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic)
- [Function type](https://en.wikipedia.org/wiki/Function_type)
- [Generalized algebraic data type](https://en.wikipedia.org/wiki/Generalized_algebraic_data_type)
- [Generic programming](https://en.wikipedia.org/wiki/Generic_programming)
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Half-precision floating-point format](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)
- [Herb Sutter](https://en.wikipedia.org/wiki/Herb_Sutter)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Inductive type](https://en.wikipedia.org/wiki/Inductive_type)
- [Inheritance (object-oriented programming)](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Integer (computer science)](https://en.wikipedia.org/wiki/Integer_(computer_science))
- [Interface (object-oriented programming)](https://en.wikipedia.org/wiki/Interface_(object-oriented_programming))
- [Intersection type](https://en.wikipedia.org/wiki/Intersection_type)
- [Interval arithmetic](https://en.wikipedia.org/wiki/Interval_arithmetic)
- [Intuitionistic type theory](https://en.wikipedia.org/wiki/Intuitionistic_type_theory)
- [Kind (type theory)](https://en.wikipedia.org/wiki/Kind_(type_theory))
- [Lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation)
- [List (abstract data type)](https://en.wikipedia.org/wiki/List_(abstract_data_type))
- [Logtalk](https://en.wikipedia.org/wiki/Logtalk)
- [Long double](https://en.wikipedia.org/wiki/Long_double)
- [Memory address](https://en.wikipedia.org/wiki/Memory_address)
- [Meta-analysis](https://en.wikipedia.org/wiki/Meta-analysis)
- [Meta-communication](https://en.wikipedia.org/wiki/Meta-communication)
- [Meta-emotion](https://en.wikipedia.org/wiki/Meta-emotion)
- [Metaknowledge](https://en.wikipedia.org/wiki/Metaknowledge)
- [Metalanguage](https://en.wikipedia.org/wiki/Metalanguage)
- [Meta-learning](https://en.wikipedia.org/wiki/Meta-learning)
- [Metaobject](https://en.wikipedia.org/wiki/Metaobject)
- [Meta-ontology](https://en.wikipedia.org/wiki/Meta-ontology)
- [Meta-optimization](https://en.wikipedia.org/wiki/Meta-optimization)
- [Meta-organization](https://en.wikipedia.org/wiki/Meta-organization)
- [Meta-reference](https://en.wikipedia.org/wiki/Meta-reference)
- [Meta-regulation](https://en.wikipedia.org/wiki/Meta-regulation)
- [Meta-system](https://en.wikipedia.org/wiki/Meta-system)
- [Meta (prefix)](https://en.wikipedia.org/wiki/Meta_(prefix))
- [Metabibliography](https://en.wikipedia.org/wiki/Metabibliography)
- [Metaclass (knowledge representation)](https://en.wikipedia.org/wiki/Metaclass_(knowledge_representation))
- [Metacognition](https://en.wikipedia.org/wiki/Metacognition)
- [Metacomputing](https://en.wikipedia.org/wiki/Metacomputing)
- [Metadata](https://en.wikipedia.org/wiki/Metadata)
- [Metadesign](https://en.wikipedia.org/wiki/Metadesign)
- [Metadiscourse](https://en.wikipedia.org/wiki/Metadiscourse)
- [Metaepistemology](https://en.wikipedia.org/wiki/Metaepistemology)
- [Metaethics](https://en.wikipedia.org/wiki/Metaethics)
- [Metafiction](https://en.wikipedia.org/wiki/Metafiction)
- [Metagame](https://en.wikipedia.org/wiki/Metagame)
- [Metagenomics](https://en.wikipedia.org/wiki/Metagenomics)
- [Metaheuristic](https://en.wikipedia.org/wiki/Metaheuristic)
- [Historiography](https://en.wikipedia.org/wiki/Historiography)
- [Metalogic](https://en.wikipedia.org/wiki/Metalogic)
- [Metamaterial](https://en.wikipedia.org/wiki/Metamaterial)
- [Metamathematics](https://en.wikipedia.org/wiki/Metamathematics)
- [Metamedia](https://en.wikipedia.org/wiki/Metamedia)
- [Metamemory](https://en.wikipedia.org/wiki/Metamemory)
- [Metaphysics](https://en.wikipedia.org/wiki/Metaphysics)
- [Metamodeling](https://en.wikipedia.org/wiki/Metamodeling)
- [Metamodernism](https://en.wikipedia.org/wiki/Metamodernism)
- [Metamood](https://en.wikipedia.org/wiki/Metamood)
- [Metamotivation](https://en.wikipedia.org/wiki/Metamotivation)
- [Metanarrative](https://en.wikipedia.org/wiki/Metanarrative)
- [Metaobject](https://en.wikipedia.org/wiki/Metaobject)
- [Metaobject](https://en.wikipedia.org/wiki/Metaobject)
- [Metaphenomics](https://en.wikipedia.org/wiki/Metaphenomics)
- [Metaphilosophy](https://en.wikipedia.org/wiki/Metaphilosophy)
- [Metaphysics](https://en.wikipedia.org/wiki/Metaphysics)
- [Metapolitics](https://en.wikipedia.org/wiki/Metapolitics)
- [Metapopulation](https://en.wikipedia.org/wiki/Metapopulation)
- [Metapragmatics](https://en.wikipedia.org/wiki/Metapragmatics)
- [Metaprogramming](https://en.wikipedia.org/wiki/Metaprogramming)
- [Metapsychiatry](https://en.wikipedia.org/wiki/Metapsychiatry)
- [Metapsychology](https://en.wikipedia.org/wiki/Metapsychology)
- [Metapuzzle](https://en.wikipedia.org/wiki/Metapuzzle)
- [Metascience](https://en.wikipedia.org/wiki/Metascience)
- [Metasemantics](https://en.wikipedia.org/wiki/Metasemantics)
- [Metatheorem](https://en.wikipedia.org/wiki/Metatheorem)
- [Metatheory](https://en.wikipedia.org/wiki/Metatheory)
- [Metaverse](https://en.wikipedia.org/wiki/Metaverse)
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Minifloat](https://en.wikipedia.org/wiki/Minifloat)
- [Moose (Perl)](https://en.wikipedia.org/wiki/Moose_(Perl))
- [Null-terminated string](https://en.wikipedia.org/wiki/Null-terminated_string)
- [O'Reilly Media](https://en.wikipedia.org/wiki/O%27Reilly_Media)
- [Object-Z](https://en.wikipedia.org/wiki/Object-Z)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Object Pascal](https://en.wikipedia.org/wiki/Object_Pascal)
- [Object REXX](https://en.wikipedia.org/wiki/Object_REXX)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [Octuple-precision floating-point format](https://en.wikipedia.org/wiki/Octuple-precision_floating-point_format)
- [Opaque data type](https://en.wikipedia.org/wiki/Opaque_data_type)
- [OJ (programming tool)](https://en.wikipedia.org/wiki/OJ_(programming_tool))
- [Option type](https://en.wikipedia.org/wiki/Option_type)
- [Parametric polymorphism](https://en.wikipedia.org/wiki/Parametric_polymorphism)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Physical address](https://en.wikipedia.org/wiki/Physical_address)
- [Plain text](https://en.wikipedia.org/wiki/Plain_text)
- [Pointer (computer programming)](https://en.wikipedia.org/wiki/Pointer_(computer_programming))
- [Primitive data type](https://en.wikipedia.org/wiki/Primitive_data_type)
- [Product type](https://en.wikipedia.org/wiki/Product_type)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Prolog](https://en.wikipedia.org/wiki/Prolog)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quadruple-precision floating-point format](https://en.wikipedia.org/wiki/Quadruple-precision_floating-point_format)
- [Rational data type](https://en.wikipedia.org/wiki/Rational_data_type)
- [Record (computer science)](https://en.wikipedia.org/wiki/Record_(computer_science))
- [Recursive data type](https://en.wikipedia.org/wiki/Recursive_data_type)
- [Reference (computer science)](https://en.wikipedia.org/wiki/Reference_(computer_science))
- [Refinement type](https://en.wikipedia.org/wiki/Refinement_type)
- [Reflective programming](https://en.wikipedia.org/wiki/Reflective_programming)
- [Resource Description Framework](https://en.wikipedia.org/wiki/Resource_Description_Framework)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Self-referential humor](https://en.wikipedia.org/wiki/Self-referential_humor)
- [Semaphore (programming)](https://en.wikipedia.org/wiki/Semaphore_(programming))
- [Set (abstract data type)](https://en.wikipedia.org/wiki/Set_(abstract_data_type))
- [Signedness](https://en.wikipedia.org/wiki/Signedness)
- [Single-precision floating-point format](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)
- [Singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern)
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Sociology of sociology](https://en.wikipedia.org/wiki/Sociology_of_sociology)
- [State (computer science)](https://en.wikipedia.org/wiki/State_(computer_science))
- [Stream (computing)](https://en.wikipedia.org/wiki/Stream_(computing))
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [Strongly typed identifier](https://en.wikipedia.org/wiki/Strongly_typed_identifier)
- [Subtyping](https://en.wikipedia.org/wiki/Subtyping)
- [Inheritance (object-oriented programming)](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
- [Tagged union](https://en.wikipedia.org/wiki/Tagged_union)
- [Ternary numeral system](https://en.wikipedia.org/wiki/Ternary_numeral_system)
- [Top type](https://en.wikipedia.org/wiki/Top_type)
- [Type class](https://en.wikipedia.org/wiki/Type_class)
- [Type constructor](https://en.wikipedia.org/wiki/Type_constructor)
- [Type conversion](https://en.wikipedia.org/wiki/Type_conversion)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Type theory](https://en.wikipedia.org/wiki/Type_theory)
- [Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)
- [Union type](https://en.wikipedia.org/wiki/Union_type)
- [Unit type](https://en.wikipedia.org/wiki/Unit_type)
- [Units of information](https://en.wikipedia.org/wiki/Units_of_information)
- [Variable (computer science)](https://en.wikipedia.org/wiki/Variable_(computer_science))
- [Virtual address space](https://en.wikipedia.org/wiki/Virtual_address_space)
- [Void type](https://en.wikipedia.org/wiki/Void_type)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Word (computer architecture)](https://en.wikipedia.org/wiki/Word_(computer_architecture))
- [XOTcl](https://en.wikipedia.org/wiki/XOTcl)
- [Talk:Metaclass](https://en.wikipedia.org/wiki/Talk:Metaclass)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:Accuracy dispute](https://en.wikipedia.org/wiki/Wikipedia:Accuracy_dispute)
- [Wikipedia:No original research](https://en.wikipedia.org/wiki/Wikipedia:No_original_research)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Wikipedia:Writing better articles](https://en.wikipedia.org/wiki/Wikipedia:Writing_better_articles)
- [Template:Data types](https://en.wikipedia.org/wiki/Template:Data_types)
- [Template:Meta-prefix](https://en.wikipedia.org/wiki/Template:Meta-prefix)
- [Template talk:Data types](https://en.wikipedia.org/wiki/Template_talk:Data_types)
- [Template talk:Meta-prefix](https://en.wikipedia.org/wiki/Template_talk:Meta-prefix)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from October 2013](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_October_2013)
- [Category:Articles needing additional references from September 2013](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_September_2013)
- [Category:Articles that may contain original research from September 2013](https://en.wikipedia.org/wiki/Category:Articles_that_may_contain_original_research_from_September_2013)
- [Category:Articles with disputed statements from May 2015](https://en.wikipedia.org/wiki/Category:Articles_with_disputed_statements_from_May_2015)
- [Category:Wikipedia articles with style issues from September 2013](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_with_style_issues_from_September_2013)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:40:47.965229+00:00_