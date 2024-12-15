# Reflective programming

## Article Metadata

- **Last Updated:** 2024-12-15T04:44:41.317927+00:00
- **Original Article:** [Reflective programming](https://en.wikipedia.org/wiki/Reflective_programming)
- **Language:** en
- **Page ID:** 314905

## Summary

In computer science, reflective programming or reflection is the ability of a process to examine, introspect, and modify its own structure and behavior.

## Categories

- Category:All articles needing additional references
- Category:All articles with unsourced statements
- Category:Articles needing additional references from January 2008
- Category:Articles with example BASIC code
- Category:Articles with example C Sharp code
- Category:Articles with example C code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example Julia code
- Category:Articles with example Lisp (programming language) code
- Category:Articles with example Objective-C code
- Category:Articles with example PHP code
- Category:Articles with example Pascal code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with example Ruby code
- Category:Articles with short description
- Category:Articles with unsourced statements from July 2015
- Category:Programming constructs
- Category:Programming language comparisons
- Category:Short description is different from Wikidata
- Category:Webarchive template wayback links

## Table of Contents

- Historical background
- Uses
- Implementation
- Security considerations
- Examples
- See also
- References
- Further reading
- External links

## Content

In computer science, reflective programming or reflection is the ability of a process to examine, introspect, and modify its own structure and behavior.

Historical background
The earliest computers were programmed in their native assembly languages, which were inherently reflective, as these original architectures could be programmed by defining instructions as data and using self-modifying code. As the bulk of programming moved to higher-level compiled languages such as Algol, Cobol, Fortran, Pascal, and C, this reflective ability largely disappeared until new programming languages with reflection built into their type systems appeared.
Brian Cantwell Smith's 1982 doctoral dissertation introduced the notion of computational reflection in procedural programming languages and the notion of the meta-circular interpreter as a component of 3-Lisp.

Uses
Reflection helps programmers make generic software libraries to display data, process different formats of data, perform serialization and deserialization of data for communication, or do bundling and unbundling of data for containers or bursts of communication.
Effective use of reflection almost always requires a plan: A design framework, encoding description, object library, a map of a database or entity relations.
Reflection makes a language more suited to network-oriented code. For example, it assists languages such as Java to operate well in networks by enabling libraries for serialization, bundling and varying data formats. Languages without reflection such as C are required to use auxiliary compilers for tasks like Abstract Syntax Notation to produce code for serialization and bundling.
Reflection can be used for observing and modifying program execution at runtime. A reflection-oriented program component can monitor the execution of an enclosure of code and can modify itself according to a desired goal of that enclosure. This is typically accomplished by dynamically assigning program code at runtime.
In object-oriented programming languages such as Java, reflection allows inspection of classes, interfaces, fields and methods at runtime without knowing the names of the interfaces, fields, methods at compile time. It also allows instantiation of new objects and invocation of methods.
Reflection is often used as part of software testing, such as for the runtime creation/instantiation of mock objects.
Reflection is also a key strategy for metaprogramming.
In some object-oriented programming languages such as C# and Java, reflection can be used to bypass member accessibility rules. For C#-properties this can be achieved by writing directly onto the (usually invisible) backing field of a non-public property. It is also possible to find non-public methods of classes and types and manually invoke them. This works for project-internal files as well as external libraries such as .NET's assemblies and Java's archives.

Implementation
A language that supports reflection provides a number of features available at runtime that would otherwise be difficult to accomplish in a lower-level language. Some of these features are the abilities to:

Discover and modify source-code constructions (such as code blocks, classes, methods, protocols, etc.) as first-class objects at runtime.
Convert a string matching the symbolic name of a class or function into a reference to or invocation of that class or function.
Evaluate a string as if it were a source-code statement at runtime.
Create a new interpreter for the language's bytecode to give a new meaning or purpose for a programming construct.
These features can be implemented in different ways. In MOO, reflection forms a natural part of everyday programming idiom. When verbs (methods) are called, various variables such as verb (the name of the verb being called) and this (the object on which the verb is called) are populated to give the context of the call. Security is typically managed by accessing the caller stack programmatically: Since callers() is a list of the methods by which the current verb was eventually called, performing tests on callers()[0] (the command invoked by the original user) allows the verb to protect itself against unauthorised use.
Compiled languages rely on their runtime system to provide information about the source code. A compiled Objective-C executable, for example, records the names of all methods in a block of the executable, providing a table to correspond these with the underlying methods (or selectors for these methods) compiled into the program. In a compiled language that supports runtime creation of functions, such as Common Lisp, the runtime environment must include a compiler or an interpreter.
Reflection can be implemented for languages without built-in reflection by using a program transformation system to define automated source-code changes.

Security considerations
Reflection may allow a user to create unexpected control flow paths through an application, potentially bypassing security measures. This may be exploited by attackers. Historical vulnerabilities in Java caused by unsafe reflection allowed code retrieved from potentially untrusted remote machines to break out of the Java sandbox security mechanism. A large scale study of 120 Java vulnerabilities in 2013 concluded that unsafe reflection is the most common vulnerability in Java, though not the most exploited.

Examples
The following code snippets create an instance foo of class Foo and invoke its method PrintHello. For each programming language, normal and reflection-based call sequences are shown.

Common Lisp
The following is an example in Common Lisp using the Common Lisp Object System:

C#
The following is an example in C#:

Delphi, Object Pascal
This Delphi and Object Pascal example assumes that a TFoo class has been declared in a unit called Unit1:

eC
The following is an example in eC:

Go
The following is an example in Go:

Java
The following is an example in Java:

JavaScript
The following is an example in JavaScript:

Julia
The following is an example in Julia:

Objective-C
The following is an example in Objective-C, implying either the OpenStep or Foundation Kit framework is used:

Perl
The following is an example in Perl:

PHP
The following is an example in PHP:

Python
The following is an example in Python:

R
The following is an example in R:

Ruby
The following is an example in Ruby:

Xojo
The following is an example using Xojo:

See also
List of reflective programming languages and platforms
Mirror (programming)
Programming paradigms
Self-hosting (compilers)
Self-modifying code
Type introspection
typeof

References
Citations
Sources
Further reading
Ira R. Forman and Nate Forman, Java Reflection in Action (2005), ISBN 1-932394-18-4
Ira R. Forman and Scott Danforth, Putting Metaclasses to Work (1999), ISBN 0-201-43305-2

External links
Reflection in logic, functional and object-oriented programming: a short comparative study
An Introduction to Reflection-Oriented Programming
Brian Foote's pages on Reflection in Smalltalk
Java Reflection API Tutorial from Oracle

## Related Articles

### Internal Links

- [.NET Framework](https://en.wikipedia.org/wiki/.NET_Framework)
- [ALGOL](https://en.wikipedia.org/wiki/ALGOL)
- [Abductive logic programming](https://en.wikipedia.org/wiki/Abductive_logic_programming)
- [ASN.1](https://en.wikipedia.org/wiki/ASN.1)
- [Action language](https://en.wikipedia.org/wiki/Action_language)
- [Actor model](https://en.wikipedia.org/wiki/Actor_model)
- [Agent-oriented programming](https://en.wikipedia.org/wiki/Agent-oriented_programming)
- [Algebraic modeling language](https://en.wikipedia.org/wiki/Algebraic_modeling_language)
- [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- [Answer set programming](https://en.wikipedia.org/wiki/Answer_set_programming)
- [Applicative programming language](https://en.wikipedia.org/wiki/Applicative_programming_language)
- [Array programming](https://en.wikipedia.org/wiki/Array_programming)
- [Aspect-oriented programming](https://en.wikipedia.org/wiki/Aspect-oriented_programming)
- [Assembly language](https://en.wikipedia.org/wiki/Assembly_language)
- [Attribute-oriented programming](https://en.wikipedia.org/wiki/Attribute-oriented_programming)
- [Automata-based programming](https://en.wikipedia.org/wiki/Automata-based_programming)
- [Automatic mutual exclusion](https://en.wikipedia.org/wiki/Automatic_mutual_exclusion)
- [Automatic programming](https://en.wikipedia.org/wiki/Automatic_programming)
- [Bayesian program synthesis](https://en.wikipedia.org/wiki/Bayesian_program_synthesis)
- [Block (programming)](https://en.wikipedia.org/wiki/Block_(programming))
- [Brian Cantwell Smith](https://en.wikipedia.org/wiki/Brian_Cantwell_Smith)
- [Bytecode](https://en.wikipedia.org/wiki/Bytecode)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Choreographic programming](https://en.wikipedia.org/wiki/Choreographic_programming)
- [Class-based programming](https://en.wikipedia.org/wiki/Class-based_programming)
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [COBOL](https://en.wikipedia.org/wiki/COBOL)
- [Command language](https://en.wikipedia.org/wiki/Command_language)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Common Lisp Object System](https://en.wikipedia.org/wiki/Common_Lisp_Object_System)
- [Comparison of functional programming languages](https://en.wikipedia.org/wiki/Comparison_of_functional_programming_languages)
- [Comparison of multi-paradigm programming languages](https://en.wikipedia.org/wiki/Comparison_of_multi-paradigm_programming_languages)
- [Comparison of programming languages (object-oriented programming)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(object-oriented_programming))
- [Compile time](https://en.wikipedia.org/wiki/Compile_time)
- [Compiled language](https://en.wikipedia.org/wiki/Compiled_language)
- [Compiled language](https://en.wikipedia.org/wiki/Compiled_language)
- [Component-based software engineering](https://en.wikipedia.org/wiki/Component-based_software_engineering)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Concatenative programming language](https://en.wikipedia.org/wiki/Concatenative_programming_language)
- [Concurrent computing](https://en.wikipedia.org/wiki/Concurrent_computing)
- [Concurrent constraint logic programming](https://en.wikipedia.org/wiki/Concurrent_constraint_logic_programming)
- [Concurrent logic programming](https://en.wikipedia.org/wiki/Concurrent_logic_programming)
- [Concurrent object-oriented programming](https://en.wikipedia.org/wiki/Concurrent_object-oriented_programming)
- [Constraint logic programming](https://en.wikipedia.org/wiki/Constraint_logic_programming)
- [Constraint programming](https://en.wikipedia.org/wiki/Constraint_programming)
- [Control flow](https://en.wikipedia.org/wiki/Control_flow)
- [Data-driven programming](https://en.wikipedia.org/wiki/Data-driven_programming)
- [Data-oriented design](https://en.wikipedia.org/wiki/Data-oriented_design)
- [Dataflow programming](https://en.wikipedia.org/wiki/Dataflow_programming)
- [Declarative programming](https://en.wikipedia.org/wiki/Declarative_programming)
- [Delphi (software)](https://en.wikipedia.org/wiki/Delphi_(software))
- [Dependent type](https://en.wikipedia.org/wiki/Dependent_type)
- [Design by contract](https://en.wikipedia.org/wiki/Design_by_contract)
- [Differentiable programming](https://en.wikipedia.org/wiki/Differentiable_programming)
- [Distributed computing](https://en.wikipedia.org/wiki/Distributed_computing)
- [Domain-specific language](https://en.wikipedia.org/wiki/Domain-specific_language)
- [Dynamic programming language](https://en.wikipedia.org/wiki/Dynamic_programming_language)
- [End-user development](https://en.wikipedia.org/wiki/End-user_development)
- [Esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language)
- [Event-driven programming](https://en.wikipedia.org/wiki/Event-driven_programming)
- [Expression-oriented programming language](https://en.wikipedia.org/wiki/Expression-oriented_programming_language)
- [Extensible programming](https://en.wikipedia.org/wiki/Extensible_programming)
- [Feature-oriented programming](https://en.wikipedia.org/wiki/Feature-oriented_programming)
- [Fifth-generation programming language](https://en.wikipedia.org/wiki/Fifth-generation_programming_language)
- [Filter (software)](https://en.wikipedia.org/wiki/Filter_(software))
- [First-class citizen](https://en.wikipedia.org/wiki/First-class_citizen)
- [First-generation programming language](https://en.wikipedia.org/wiki/First-generation_programming_language)
- [Flow-based programming](https://en.wikipedia.org/wiki/Flow-based_programming)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Foundation Kit](https://en.wikipedia.org/wiki/Foundation_Kit)
- [Fourth-generation programming language](https://en.wikipedia.org/wiki/Fourth-generation_programming_language)
- [Function-level programming](https://en.wikipedia.org/wiki/Function-level_programming)
- [Functional logic programming](https://en.wikipedia.org/wiki/Functional_logic_programming)
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [Functional reactive programming](https://en.wikipedia.org/wiki/Functional_reactive_programming)
- [Generalized algebraic data type](https://en.wikipedia.org/wiki/Generalized_algebraic_data_type)
- [Generic programming](https://en.wikipedia.org/wiki/Generic_programming)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Grammar-oriented programming](https://en.wikipedia.org/wiki/Grammar-oriented_programming)
- [Graph rewriting](https://en.wikipedia.org/wiki/Graph_rewriting)
- [High-level programming language](https://en.wikipedia.org/wiki/High-level_programming_language)
- [Higher-order programming](https://en.wikipedia.org/wiki/Higher-order_programming)
- [Homoiconicity](https://en.wikipedia.org/wiki/Homoiconicity)
- [Hygienic macro](https://en.wikipedia.org/wiki/Hygienic_macro)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Immutable object](https://en.wikipedia.org/wiki/Immutable_object)
- [Imperative programming](https://en.wikipedia.org/wiki/Imperative_programming)
- [Indiana University](https://en.wikipedia.org/wiki/Indiana_University)
- [Inductive logic programming](https://en.wikipedia.org/wiki/Inductive_logic_programming)
- [Inductive programming](https://en.wikipedia.org/wiki/Inductive_programming)
- [Inferential programming](https://en.wikipedia.org/wiki/Inferential_programming)
- [Instance (computer science)](https://en.wikipedia.org/wiki/Instance_(computer_science))
- [Intentional programming](https://en.wikipedia.org/wiki/Intentional_programming)
- [Interactive programming](https://en.wikipedia.org/wiki/Interactive_programming)
- [Interface description language](https://en.wikipedia.org/wiki/Interface_description_language)
- [Interpreter (computing)](https://en.wikipedia.org/wiki/Interpreter_(computing))
- [Interpreter (computing)](https://en.wikipedia.org/wiki/Interpreter_(computing))
- [Type introspection](https://en.wikipedia.org/wiki/Type_introspection)
- [Invariant-based programming](https://en.wikipedia.org/wiki/Invariant-based_programming)
- [Jackson structured programming](https://en.wikipedia.org/wiki/Jackson_structured_programming)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Julia (programming language)](https://en.wikipedia.org/wiki/Julia_(programming_language))
- [Language-oriented programming](https://en.wikipedia.org/wiki/Language-oriented_programming)
- [List comprehension](https://en.wikipedia.org/wiki/List_comprehension)
- [List of object-oriented programming languages](https://en.wikipedia.org/wiki/List_of_object-oriented_programming_languages)
- [List of reflective programming languages and platforms](https://en.wikipedia.org/wiki/List_of_reflective_programming_languages_and_platforms)
- [Literate programming](https://en.wikipedia.org/wiki/Literate_programming)
- [Logic programming](https://en.wikipedia.org/wiki/Logic_programming)
- [Low-code development platform](https://en.wikipedia.org/wiki/Low-code_development_platform)
- [Low-level programming language](https://en.wikipedia.org/wiki/Low-level_programming_language)
- [MOO](https://en.wikipedia.org/wiki/MOO)
- [Machine code](https://en.wikipedia.org/wiki/Machine_code)
- [Macro (computer science)](https://en.wikipedia.org/wiki/Macro_(computer_science))
- [Macroprogramming](https://en.wikipedia.org/wiki/Macroprogramming)
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Meta-circular evaluator](https://en.wikipedia.org/wiki/Meta-circular_evaluator)
- [Metalinguistic abstraction](https://en.wikipedia.org/wiki/Metalinguistic_abstraction)
- [Metaprogramming](https://en.wikipedia.org/wiki/Metaprogramming)
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Mirror (programming)](https://en.wikipedia.org/wiki/Mirror_(programming))
- [Mock object](https://en.wikipedia.org/wiki/Mock_object)
- [Modeling language](https://en.wikipedia.org/wiki/Modeling_language)
- [Modular programming](https://en.wikipedia.org/wiki/Modular_programming)
- [Multi-stage programming](https://en.wikipedia.org/wiki/Multi-stage_programming)
- [Multitier programming](https://en.wikipedia.org/wiki/Multitier_programming)
- [Natural-language programming](https://en.wikipedia.org/wiki/Natural-language_programming)
- [Nested function](https://en.wikipedia.org/wiki/Nested_function)
- [Non-English-based programming languages](https://en.wikipedia.org/wiki/Non-English-based_programming_languages)
- [Non-structured programming](https://en.wikipedia.org/wiki/Non-structured_programming)
- [Nondeterministic programming](https://en.wikipedia.org/wiki/Nondeterministic_programming)
- [Object-based language](https://en.wikipedia.org/wiki/Object-based_language)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object Pascal](https://en.wikipedia.org/wiki/Object_Pascal)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [Ontology language](https://en.wikipedia.org/wiki/Ontology_language)
- [OpenStep](https://en.wikipedia.org/wiki/OpenStep)
- [Organic computing](https://en.wikipedia.org/wiki/Organic_computing)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Page description language](https://en.wikipedia.org/wiki/Page_description_language)
- [Parallel computing](https://en.wikipedia.org/wiki/Parallel_computing)
- [Parallel programming model](https://en.wikipedia.org/wiki/Parallel_programming_model)
- [Partial application](https://en.wikipedia.org/wiki/Partial_application)
- [Partitioned global address space](https://en.wikipedia.org/wiki/Partitioned_global_address_space)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Persistent programming language](https://en.wikipedia.org/wiki/Persistent_programming_language)
- [Phrack](https://en.wikipedia.org/wiki/Phrack)
- [Pipeline (software)](https://en.wikipedia.org/wiki/Pipeline_(software))
- [Probabilistic logic programming](https://en.wikipedia.org/wiki/Probabilistic_logic_programming)
- [Probabilistic programming](https://en.wikipedia.org/wiki/Probabilistic_programming)
- [Procedural programming](https://en.wikipedia.org/wiki/Procedural_programming)
- [Process-oriented programming](https://en.wikipedia.org/wiki/Process-oriented_programming)
- [Process (computing)](https://en.wikipedia.org/wiki/Process_(computing))
- [Production system (computer science)](https://en.wikipedia.org/wiki/Production_system_(computer_science))
- [Program synthesis](https://en.wikipedia.org/wiki/Program_synthesis)
- [Program transformation](https://en.wikipedia.org/wiki/Program_transformation)
- [Programming by demonstration](https://en.wikipedia.org/wiki/Programming_by_demonstration)
- [Programming by example](https://en.wikipedia.org/wiki/Programming_by_example)
- [Programming in the large and programming in the small](https://en.wikipedia.org/wiki/Programming_in_the_large_and_programming_in_the_small)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Programming language generations](https://en.wikipedia.org/wiki/Programming_language_generations)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)
- [Prototype-based programming](https://en.wikipedia.org/wiki/Prototype-based_programming)
- [Purely functional programming](https://en.wikipedia.org/wiki/Purely_functional_programming)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quantum programming](https://en.wikipedia.org/wiki/Quantum_programming)
- [Query language](https://en.wikipedia.org/wiki/Query_language)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Reactive programming](https://en.wikipedia.org/wiki/Reactive_programming)
- [Recursion (computer science)](https://en.wikipedia.org/wiki/Recursion_(computer_science))
- [Reflection (computer graphics)](https://en.wikipedia.org/wiki/Reflection_(computer_graphics))
- [Relativistic programming](https://en.wikipedia.org/wiki/Relativistic_programming)
- [Role-oriented programming](https://en.wikipedia.org/wiki/Role-oriented_programming)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Execution (computing)](https://en.wikipedia.org/wiki/Execution_(computing))
- [Sandbox (computer security)](https://en.wikipedia.org/wiki/Sandbox_(computer_security))
- [Scientific programming language](https://en.wikipedia.org/wiki/Scientific_programming_language)
- [Scripting language](https://en.wikipedia.org/wiki/Scripting_language)
- [Second-generation programming language](https://en.wikipedia.org/wiki/Second-generation_programming_language)
- [Self-hosting (compilers)](https://en.wikipedia.org/wiki/Self-hosting_(compilers))
- [Self-modifying code](https://en.wikipedia.org/wiki/Self-modifying_code)
- [Separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)
- [Serialization](https://en.wikipedia.org/wiki/Serialization)
- [Service-oriented programming](https://en.wikipedia.org/wiki/Service-oriented_programming)
- [Set theoretic programming](https://en.wikipedia.org/wiki/Set_theoretic_programming)
- [SIGNAL (programming language)](https://en.wikipedia.org/wiki/SIGNAL_(programming_language))
- [Simulation language](https://en.wikipedia.org/wiki/Simulation_language)
- [Software testing](https://en.wikipedia.org/wiki/Software_testing)
- [Source code](https://en.wikipedia.org/wiki/Source_code)
- [Spacecraft command language](https://en.wikipedia.org/wiki/Spacecraft_command_language)
- [Stack-oriented programming](https://en.wikipedia.org/wiki/Stack-oriented_programming)
- [Stream processing](https://en.wikipedia.org/wiki/Stream_processing)
- [Strict programming language](https://en.wikipedia.org/wiki/Strict_programming_language)
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [Structured concurrency](https://en.wikipedia.org/wiki/Structured_concurrency)
- [Structured programming](https://en.wikipedia.org/wiki/Structured_programming)
- [Subject-oriented programming](https://en.wikipedia.org/wiki/Subject-oriented_programming)
- [Symbolic programming](https://en.wikipedia.org/wiki/Symbolic_programming)
- [Synchronous programming language](https://en.wikipedia.org/wiki/Synchronous_programming_language)
- [System programming language](https://en.wikipedia.org/wiki/System_programming_language)
- [Tacit programming](https://en.wikipedia.org/wiki/Tacit_programming)
- [Tactile programming language](https://en.wikipedia.org/wiki/Tactile_programming_language)
- [Template metaprogramming](https://en.wikipedia.org/wiki/Template_metaprogramming)
- [Template processor](https://en.wikipedia.org/wiki/Template_processor)
- [Third-generation programming language](https://en.wikipedia.org/wiki/Third-generation_programming_language)
- [Total functional programming](https://en.wikipedia.org/wiki/Total_functional_programming)
- [Transformation language](https://en.wikipedia.org/wiki/Transformation_language)
- [Type introspection](https://en.wikipedia.org/wiki/Type_introspection)
- [Typeof](https://en.wikipedia.org/wiki/Typeof)
- [Uniform Function Call Syntax](https://en.wikipedia.org/wiki/Uniform_Function_Call_Syntax)
- [Value-level programming](https://en.wikipedia.org/wiki/Value-level_programming)
- [Very high-level programming language](https://en.wikipedia.org/wiki/Very_high-level_programming_language)
- [Visual programming language](https://en.wikipedia.org/wiki/Visual_programming_language)
- [Vulnerability (computer security)](https://en.wikipedia.org/wiki/Vulnerability_(computer_security))
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Xojo](https://en.wikipedia.org/wiki/Xojo)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Programming paradigms navbox](https://en.wikipedia.org/wiki/Template:Programming_paradigms_navbox)
- [Template:Types of programming languages](https://en.wikipedia.org/wiki/Template:Types_of_programming_languages)
- [Template talk:Programming paradigms navbox](https://en.wikipedia.org/wiki/Template_talk:Programming_paradigms_navbox)
- [Template talk:Types of programming languages](https://en.wikipedia.org/wiki/Template_talk:Types_of_programming_languages)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from January 2008](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_January_2008)
- [Category:Articles with unsourced statements from July 2015](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_July_2015)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:44:41.317927+00:00_