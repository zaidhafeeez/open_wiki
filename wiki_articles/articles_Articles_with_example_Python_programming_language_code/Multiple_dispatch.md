# Multiple dispatch

## Metadata
- **Last Updated:** 2024-12-15 14:36:31 UTC
- **Original Article:** [Multiple dispatch](https://en.wikipedia.org/wiki/Multiple_dispatch)
- **Language:** en
- **Page ID:** 191413

## Summary
Multiple dispatch or multimethods is a feature of some programming languages in which a function or method can be dynamically dispatched based on the run-time (dynamic) type or, in the more general case, some other attribute of more than one of its arguments. This is a generalization of single-dispatch polymorphism where a function or method call is dynamically dispatched based on the derived type of the object on which the method has been called. Multiple dispatch routes the dynamic dispatch to the implementing function or method using the combined characteristics of one or more arguments.

## Categories
This article belongs to the following categories:

- Category:All articles containing potentially dated statements
- Category:All articles with unsourced statements
- Category:Articles containing potentially dated statements from 2021
- Category:Articles with example C++ code
- Category:Articles with example C code
- Category:Articles with example D code
- Category:Articles with example Java code
- Category:Articles with example Julia code
- Category:Articles with example Lisp (programming language) code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from December 2007
- Category:Method (computer programming)
- Category:Polymorphism (computer science)
- Category:Short description matches Wikidata
- Category:Webarchive template wayback links

## Table of Contents

- Understanding dispatch
- Examples
- Support in programming languages
- See also
- References
- External links

## Content

Multiple dispatch or multimethods is a feature of some programming languages in which a function or method can be dynamically dispatched based on the run-time (dynamic) type or, in the more general case, some other attribute of more than one of its arguments. This is a generalization of single-dispatch polymorphism where a function or method call is dynamically dispatched based on the derived type of the object on which the method has been called. Multiple dispatch routes the dynamic dispatch to the implementing function or method using the combined characteristics of one or more arguments.

Understanding dispatch
Developers of computer software typically organize source code into named blocks variously called subroutines, procedures, subprograms, functions, or methods. The code in the function is executed by calling it – executing a piece of code that references its name. This transfers control temporarily to the called function; when the function's execution has completed, control is typically transferred back to the instruction in the caller that follows the reference.
Function names are usually selected so as to be descriptive of the function's purpose. It is sometimes desirable to give several functions the same name, often because they perform conceptually similar tasks, but operate on different types of input data. In such cases, the name reference at the function call site is not sufficient for identifying the block of code to be executed. Instead, the number and type of the arguments to the function call are also used to select among several function implementations.
In more conventional, i.e., single-dispatch object-oriented programming languages, when invoking a method (sending a message in Smalltalk, calling a member function in C++), one of its arguments is treated specially and used to determine which of the (potentially many) classes of methods of that name is to be applied. In many languages, the special argument is indicated syntactically; for example, a number of programming languages put the special argument before a dot in making a method call: special.method(other, arguments, here), so that lion.sound() would produce a roar, whereas sparrow.sound() would produce a chirp.
In contrast, in languages with multiple dispatch, the selected method is simply the one whose arguments match the number and type of the function call. There is no special argument that owns the function/method carried out in a particular call.
The Common Lisp Object System (CLOS) is an early and well-known example of multiple dispatch. Another notable example of the use of multiple dispatch is the Julia programming language.
Multiple dispatch should be distinguished from function overloading, in which static typing information, such as a term's declared or inferred type (or base type in a language with subtyping) is used to determine which of several possibilities will be used at a given call site, and that determination is made at compile or link time (or some other time before program execution starts) and is thereafter invariant for a given deployment or run of the program.  Many languages such as C++ offer robust function overloading but do not offer dynamic multiple dispatch (C++ only permits dynamic single dispatch through use of virtual functions).

Data types
When working with languages that can discriminate data types at compile time, selecting among the alternatives can occur then. The act of creating such alternative functions for compile time selection is usually referred to as overloading a function.
In programming languages that defer data type identification until run time (i.e., late binding), selection among alternative functions must occur then, based on the dynamically determined types of function arguments. Functions whose alternative implementations are selected in this manner are referred to most generally as multimethods.
There is some run-time cost associated with dynamically dispatching function calls. In some languages, the distinction between overloading and multimethods can be blurred, with the compiler determining whether compile time selection can be applied to a given function call, or whether slower run time dispatch is needed.

Issues
There are several known issues with dynamic-dispatch, both single and multiple.  While many of these issues are solved for single-dispatch, which has been a standard feature in object-oriented programming languages for decades, these issues become more complicated in the multiple-dispatch case.

Expressiveness and modularity
In most popular programming languages, source code is delivered and deployed in granules of functionality which we will here call packages; actual terminology for this concept varies between language.  Each package may contain multiple type, value, and function definitions, packages are often compiled separately in languages with a compilation step, and a non-cyclical dependency relationship may exist.  A complete program is a set of packages, with a main package which may depend on several other packages, and the whole program consisting of the transitive closure of the dependency relationship.
The so-called expression problem relates to the ability for code in a depending package to extend behaviors (functions or datatypes) defined in a base package from within an including package, without modifying the source to the base package.  Traditional single-dispatch OO languages make it trivial to add new datatypes but not new functions; traditional functional languages tend to have the opposite effect, and multiple dispatch, if implemented correctly, allows both.  It is desirable for an implementation of multiple dispatch to have the following properties:

It is possible to define different "cases" of a multi-method from within different packages without modifying the source of a base package.
Inclusion of another package in the program should not change the behavior of a given multi-method call, when the call does not use any datatypes defined in the package.
Conversely, if a datatype is defined in a given package, and a multi-method extension using that type is also defined in the same package, and a value of that type is passed (through a base type reference or into a generic function) into another package with no dependency on that package, and then the multi-method is invoked with that value as an argument, the multi-method case defined in the package which includes the type should be employed.  To put it another way—within a given program, the same multi-method invoked with the same set of arguments should resolve to the same implementation, regardless of the location of the call site, and whether or not a given definition is "in scope" or "visible" at the point of the method call.

Ambiguity
It is generally desirable that for any given invocation of a multi-method, there be at most one "best" candidate among implementation cases of the multi-method, and/or that if there is not, that this be resolved in a predictable and deterministic fashion, including failure.  Non-deterministic behavior is undesirable.  Assuming a set of types with a non-circular subtyping relationship, one can define that one implementation of a multi-method is "better" (more specific) if all dynamically-dispatched arguments in the first are subtypes of all dynamically-dispatched arguments specified in the second, and at least one is a strict subtype.  With single dispatch and in the absence of multiple inheritance, this condition is trivially satisfied, but with multiple dispatch, it is possible for two or more candidates to satisfy a given actual argument list, but neither is more specific than the other (one dynamic argument being the subtype in one case, another being the subtype in the other case).  This particularly can happen if two different packages, neither depending on the other, both extend some multi-method with implementations concerning each package's types, and then a third package that includes both (possibly indirectly) then invokes the multi-method using arguments from both packages.
Possible resolutions include:

Treating any ambiguous calls as an error.  This might be caught at compile time (or otherwise before deployment), but might not be detected until runtime and produce a runtime error.
Ordering the arguments, so e.g. the case with the most specific first argument is selected, and subsequent arguments are not considered for ambiguity resolution unless the first argument is insufficient to resolve the issue.
Construction of other rules for resolving an ambiguity in one direction or another.  Sometimes, such rules might be arbitrary and surprising.  In the rules for static overload resolution in C++, for instance, a type which matches exactly is understandably considered a better match than a type which matches through a base type reference or a generic (template) parameter.  However, if the only possible matches are either through a base type or a generic parameter, the generic parameter is preferred over the base type, a rule that sometimes produces surprising behavior.

Efficiency
Efficient implementation of single-dispatch, including in programming languages that are separately compiled to object code and linked with a low-level (not-language-aware) linker, including dynamically at program load/start time or even under the direction of the application code, are well known.  The "vtable" method developed in C++ and other early OO languages (where each class has an array of function pointers corresponding to that class's virtual functions) is nearly as fast as a static method call, requiring O(1) overhead and only one additional memory lookup even in the un-optimized case.  However, the vtable method uses the function name and not the argument type as its lookup key, and does not scale to the multiple dispatch case.  (It also depends on the object-oriented paradigm of methods being features of classes, not standalone entities independent of any particular datatype).
Efficient implementation of multiple-dispatch remains an ongoing research problem.

Use in practice
To estimate how often multiple dispatch is used in practice, Muschevici et al. studied programs that use dynamic dispatch. They analyzed nine applications, mostly compilers, written in six different languages: Common Lisp Object System, Dylan, Cecil, MultiJava, Diesel, and Nice. Their results show that 13–32% of generic functions use the dynamic type of one argument, while 2.7–6.5% of them use the dynamic type of multiple arguments. The remaining 65–93% of generic functions have one concrete method (overrider), and thus are not considered to use the dynamic types of their arguments. Further, the study reports that 2–20% of generic functions had two and 3–6% had three concrete function implementations. The numbers decrease rapidly for functions with more concrete overriders.
Multiple dispatch is used much more heavily in Julia, where multiple dispatch was a central design concept from the origin of the language: collecting the same statistics as Muschevici on the average number of methods per generic function, it was found that the Julia standard library uses more than double the amount of overloading than in the other languages analyzed by Muschevici, and more than 10 times in the case of binary operators.
The data from these papers is summarized in the following table, where the dispatch ratio DR is the average number of methods per generic function; the choice ratio CR is the mean of the square of the number of methods (to better measure the frequency of functions with a large number of methods); and the degree of specialization DoS is the average number of type-specialized arguments per method (i.e., the number of arguments that are dispatched on):

Theory
The theory of multiple dispatching languages was first developed by Castagna et al., by defining a model for overloaded functions with late binding. It yielded the first formalization of the problem of covariance and contravariance of object-oriented languages and a solution to the problem of binary methods.

Examples
Distinguishing multiple and single dispatch may be made clearer by an example. Imagine a game that has, among its (user-visible) objects, spaceships and asteroids. When two objects collide, the program may need to do different things according to what has just hit what.

Languages with built-in multiple dispatch
C#
C# introduced support for dynamic multimethods in version 4 (April 2010) using the 'dynamic' keyword. The following example demonstrates multimethods.  Like many other statically-typed languages, C# also supports static method overloading. Microsoft expects that developers will choose static typing over dynamic typing in most scenarios.  The 'dynamic' keyword supports interoperability with COM objects and dynamically-typed .NET languages.

The example below uses features introduced in C# 9 and C# 10.

Output:

Groovy
Groovy is a general purpose Java compatible/interusable JVM language, which, contrary to Java, uses late binding / multiple dispatch.

Common Lisp
In a language with multiple dispatch, such as Common Lisp, it might look more like this (Common Lisp example shown):

and similarly for the other methods. Explicit testing and "dynamic casting" are not used.
In the presence of multiple dispatch, the traditional idea of methods as being defined in classes and contained in objects becomes less appealing—each collide-with method above is attached to two different classes, not one. Hence, the special syntax for method invocation generally disappears, so that method invocation looks exactly like ordinary function invocation, and methods are grouped not in classes but in generic functions.

Julia
Julia has built-in multiple dispatch, and it is central to the language design.  The Julia version of the example above might look like:

Output:

Raku
Raku, like Perl, uses proven ideas from other languages, and type systems have shown themselves to offer compelling advantages in compiler-side code analysis and powerful user-side semantics via multiple dispatch.
It has both multimethods, and multisubs. Since most operators are subroutines, it also has multiple dispatched operators.
Along with the usual type constraints, it also has where constraints that allow making very specialized subroutines.

Extending languages with multiple-dispatch libraries
JavaScript
In languages that do not support multiple dispatch at the language definition or syntactic level, it is often possible to add multiple dispatch using a library extension. JavaScript and TypeScript do not support multimethods at the syntax level, but it is possible to add multiple dispatch via a library. For example, the multimethod package provides an implementation of multiple dispatch, generic functions.
Dynamically-typed version in JavaScript:

Statically-typed version in TypeScript:

Python
Multiple dispatch can be added to Python using a library extension. For example, using the module multimethod.py and also with the module multimethods.py which provides CLOS-style multimethods for Python without changing the underlying syntax or keywords of the language.

Functionally, this is very similar to the CLOS example, but the syntax is conventional Python.
Using Python 2.4 decorators, Guido van Rossum produced a sample implementation of multimethods with a simplified syntax:

and then it goes on to define the multimethod decorator.
The PEAK-Rules package provides multiple dispatch with a syntax similar to the above example. It was later replaced by PyProtocols.
The Reg library also supports multiple and predicate dispatch.

With the introduction of type hints, multiple dispatch is possible with even simpler syntax. For example, using plum-dispatch,

Emulating multiple dispatch
C
C does not have dynamic dispatch, so it must be implemented manually in some form. Often an enum is used to identify the subtype of an object. Dynamic dispatch can be done by looking up this value in a function pointer branch table. Here is a simple example in C:

With the C Object System library, C does support dynamic dispatch similar to CLOS. It is fully extensible and does not need any manual handling of the methods. Dynamic message (methods) are dispatched by the dispatcher of COS, which is faster than Objective-C. Here is an example in COS:

C++
As of 2021, C++ natively supports only single dispatch, though adding multi-methods (multiple dispatch) was proposed by Bjarne Stroustrup (and collaborators) in 2007. The methods of working around this limit are analogous: use either the visitor pattern, dynamic cast or a library:

or pointer-to-method lookup table:

The YOMM2 library provides a fast, orthogonal implementation of open multimethods.
The syntax for declaring open methods is inspired by a proposal for a native C++ implementation. The library requires that the user registers all the classes used as virtual arguments (and their sub-classes), but does not require any modifications to existing code. Methods are implemented as ordinary inline C++ functions; they can be overloaded and they can be passed by pointer. There is no limit on the number of virtual arguments, and they can be arbitrarily mixed with non-virtual arguments.
The library uses a combination of techniques (compressed dispatch tables, collision free integer hash table) to implement method calls in constant time, while mitigating memory usage. Dispatching a call to an open method with a single virtual argument takes only 15–30% more time than calling an ordinary virtual member function, when a modern optimizing compiler is used.
The Asteroids example can be implemented as follows:

Stroustrup mentions in The Design and Evolution of C++ that he liked the concept of multimethods and considered implementing it in C++ but claims to have been unable to find an efficient sample implementation (comparable to virtual functions) and resolve some possible type ambiguity problems. He then states that although the feature would still be nice to have, that it can be approximately implemented using double dispatch or a type based lookup table as outlined in the C/C++ example above so is a low priority feature for future language revisions.

D
As of 2021, as do many other object-oriented programming languages, D natively supports only single dispatch. However, it is possible to emulate open multimethods as a library function in D. The openmethods library is an example.

Java
In a language with only single dispatch, such as Java, multiple dispatch can be emulated with multiple levels of single dispatch:

Run time instanceof checks at one or both levels can also be used.

Support in programming languages
Primary paradigm
Julia

Supporting general multimethods
C# 4.0
Cecil
Clojure
Common Lisp (via the Common Lisp Object System)
Dylan
Emacs Lisp (via cl-defmethod)
Fortress
Groovy
Lasso
Nim, up to v0.19.x (from v0.20.0 it is necessary to pass a compiler flag)
Raku
R
Seed7
TADS
VB.Net via late binding, also via .Net DLR
Wolfram Language via symbolic pattern matching
Xtend

Via extensions
Any .NET language (via the library MultiMethods.NET)
C (via the library C Object System)
C# (via the library multimethod-sharp)
C++ (via the library yomm2, multimethods and omm)
D (via the library openmethods)
Factor (via the standard multimethods vocabulary)
Java (using the extension MultiJava)
JavaScript (via package @arrows/multimethod)
Perl (via the module Class::Multimethods)
Python (via PEAK-Rules, RuleDispatch, gnosis.magic.multimethods, PyMultimethods, multipledispatch, or plum-dispatch)
Racket (via multimethod-lib)
Ruby (via the library The Multiple Dispatch Library and Multimethod Package and Vlx-Multimethods Package)
Scheme (via e.g. TinyCLOS)
TypeScript (via package @arrows/multimethod)

See also
Predicate dispatch

References
External links
Stroustrup, Bjarne; Solodkyy, Yuriy; Pirkelbauer, Peter (2007). Open Multi-Methods for C++ (PDF). ACM 6th International Conference on Generative Programming and Component Engineering.
"Dynamic multiple dispatch". docs.racket-lang.org. Retrieved 2018-03-12.

## Archive Info
- **Archived on:** 2024-12-15 20:38:31 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 20180 bytes
- **Word Count:** 3052 words
