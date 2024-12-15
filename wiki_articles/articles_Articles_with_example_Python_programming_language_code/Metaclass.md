# Metaclass

## Metadata
- **Last Updated:** 2024-12-03 06:53:39 UTC
- **Original Article:** [Metaclass](https://en.wikipedia.org/wiki/Metaclass)
- **Language:** en
- **Page ID:** 558359

## Summary
In object-oriented programming, a metaclass is a class whose instances are classes themselves. Unlike ordinary classes, which define the behaviors of objects, metaclasses specify the behaviors of classes and their instances. Not all object-oriented programming languages support the concept of metaclasses. For those that do, the extent of control metaclasses have over class behaviors varies. Metaclasses are often implemented by treating classes as first-class citizens, making a metaclass an object that creates and manages these classes. Each programming language adheres to its own metaobject protocol, which are the rules that determine interactions among objects, classes, and metaclasses. Metaclasses are utilized to automate code generation and to enhance framework development.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 20:26:38 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 11721 bytes
- **Word Count:** 1858 words
