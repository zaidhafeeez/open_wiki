---
title: Uniform access principle
url: https://en.wikipedia.org/wiki/Uniform_access_principle
language: en
categories: ["Category:All Wikipedia articles written in American English", "Category:All articles needing additional references", "Category:All articles with style issues", "Category:Articles needing additional references from January 2010", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Programming paradigms", "Category:Programming principles", "Category:Short description matches Wikidata", "Category:Software design", "Category:Use American English from March 2019", "Category:Wikipedia articles with style issues from December 2024"]
references: 0
last_modified: 2024-12-19T18:29:06Z
---

# Uniform access principle

## Summary

The uniform access principle of computer programming was put forth by Bertrand Meyer (originally in his book Object-Oriented Software Construction). It states "All services offered by a module should be available through a uniform notation, which does not betray whether they are implemented through storage or through computation." This principle applies generally to the syntax of object-oriented programming languages. In simpler form, it states that there should be no syntactical difference betw

## Full Content

The uniform access principle of computer programming was put forth by Bertrand Meyer (originally in his book Object-Oriented Software Construction). It states "All services offered by a module should be available through a uniform notation, which does not betray whether they are implemented through storage or through computation." This principle applies generally to the syntax of object-oriented programming languages. In simpler form, it states that there should be no syntactical difference between working with an attribute, pre-computed property, or method/query of an object.
While most examples focus on the "read" aspect of the principle (i.e., retrieving a value), Meyer shows that the "write" implications (i.e., modifying a value) of the principle are harder to deal with in his monthly column on the Eiffel programming language official website.

Explanation
The problem being addressed by Meyer involves the maintenance of large software projects or software libraries. Sometimes when developing or maintaining software it is necessary, after much code is in place, to change a class or object in a way that transforms what was simply an attribute access into a method call.  Programming languages often use different syntax for attribute access and invoking a method, (e.g., object.something versus object.something()). The syntax change would require, in popular programming languages of the day, changing the source code in all the places where the attribute was used.  This might require changing source code in many different locations throughout a very large volume of source code. Or worse, if the change is in an object library used by hundreds of customers, each of those customers would have to find and change all the places the attribute was used in their own code and recompile their programs.
Going the reverse way (from method to simple attribute) really was not a problem, as one can always just keep the function and have it simply return the attribute value.
Meyer recognized the need for software developers to write code in such a way as to minimize or eliminate cascading changes in code that result from changes which convert an object attribute to a method call or vice versa. For this he developed the Uniform Access Principle.
Many programming languages do not strictly support the UAP but do support forms of it.  Properties, which are provided in a number of programming languages, address the problem Meyer was addressing with his UAP in a different way. Instead of providing a single uniform notation, properties provide a way to invoke a method of an object while using the same notation as is used for attribute access.  The separate method invocation syntax is still available.

UAP example
If the language uses the method invocation syntax it may look something like this.

// Assume print displays the variable passed to it, with or without parens
// Set Foo's attribute 'bar' to  value 5.
Foo.bar(5)
print Foo.bar()

When executed, should display :

5

Whether or not Foo.bar(5) invokes a function or simply sets an attribute is hidden from the caller.
Likewise whether Foo.bar() simply retrieves the value of the attribute, or invokes a function
to compute the value returned, is an implementation detail hidden from the caller.
If the language uses the attribute syntax the syntax may look like this.

Foo.bar = 5
print Foo.bar

Again, whether or not a method is invoked, or the value is simply assigned to an attribute is hidden
from the calling method.

Problems
However, UAP itself can lead to problems, if used in places where the differences between access methods are not negligible, such as when the returned value is expensive to compute or will trigger cache operations.

Language examples
Python
Python properties may be used to allow a method
to be invoked with the same syntax as accessing an attribute.  Whereas Meyer's UAP would have
a single notation for both attribute access and method invocation (method invocation syntax), 
a language with support for properties still supports separate notations for attribute
and method access.  Properties allow the attribute notation to be used, but to hide the
fact that a method is being invoked instead of simply retrieving or setting a value. 
As such, Python leaves the option of adherence to UAP up to the individual programmer. The built-in @property function provides a simple way to decorate any given method in attribute access syntax, thus abstracting away the syntactical difference between method invocations and attribute accesses.
In Python, we may have code that access an Egg object that could be defined such that weight and color are simple attributes as in the following 

Or the Egg object could use properties, and invoke getter and setter methods instead

Regardless of which way Egg is defined, the calling code can remain the same.  The implementation of Egg can switch from one form to the other without affecting code that uses the Egg class. Languages which implement the UAP have this property as well.

Ruby
Consider the following

Now the Egg class could be defined as follows

The above initial code segment would work fine with the Egg being defined as such. The Egg
class could also be defined as below, where color is instead a method. The calling code would
still work, unchanged if Egg were to be defined as follows.

Note how even though color looks like an attribute in one case and a pair of methods
in the next, the interface to the class remains the same.  The person maintaining the Egg class can switch from one form to the other without fear of breaking any caller's code.
Ruby follows the revised UAP, the attr_accessor :color only acts as syntactic sugar for generating accessor/setter methods for color. There is no way in Ruby to retrieve an instance variable from an object without calling a method on it.
Strictly speaking, Ruby does not follow Meyer's original UAP in that the syntax for accessing an attribute is different from the syntax for invoking a method.  But here, the access for an attribute will always actually be through a function which is often automatically generated. So in essence, either type of access invokes a function and the language does follow Meyer's revised Uniform Access Principle.

C#
The C# language supports class properties, which provide a means to define get and set operations (getters and setters) for a member variable. The syntax to access or modify the property is the same as accessing any other class member variable, but the actual implementation for doing so can be defined as either a simple read/write access or as functional code.

In the example above, class Foo contains two properties, Size and Name. The Size property is an integer that can be read (get) and written (set). Similarly, the Name property is a string that can also be read and modified, but its value is stored in a separate (private) class variable _name.
Omitting the set operation in a property definition makes the property read-only, while omitting the get operation makes it write-only.
Use of the properties employs the UAP, as shown in the code below.

C++
C++ has neither the UAP nor properties, when an object is changed such that an attribute (color) becomes a pair of functions (getA, setA). Any place in that uses an instance of the object and either sets or gets the attribute value (x = obj.color or obj.color = x) must be changed to invoke one of the functions. (x = obj.getColor() or obj.setColor(x)). Using templates and operator overloading, it is possible to fake properties, but this is more complex than in languages which directly support properties. This complicates maintenance of C++ programs. Distributed libraries of C++ objects must be careful about how they provide access to member data.

JavaScript
JavaScript has had support for computed properties since 2009.


== References ==
