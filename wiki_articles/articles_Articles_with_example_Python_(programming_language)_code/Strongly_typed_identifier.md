# Strongly typed identifier

## Article Metadata

- **Last Updated:** 2024-12-14T19:45:26.203044+00:00
- **Original Article:** [Strongly typed identifier](https://en.wikipedia.org/wiki/Strongly_typed_identifier)
- **Language:** en
- **Page ID:** 72828379

## Summary

A strongly typed identifier is user-defined data type which serves as an identifier or key that is strongly typed. This is a solution to the "primitive obsession" code smell as mentioned by Martin Fowler. The data type should preferably be immutable if possible. It is common for implementations to handle equality testing, serialization and model binding.
The strongly typed identifier commonly wraps the data type used as the primary key in the database, such as a string, an integer or universally

## Categories

- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example D code
- Category:Articles with example Haskell code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example Julia code
- Category:Articles with example PHP code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Ruby code
- Category:Articles with example Rust code
- Category:Articles with example Scala code
- Category:Articles with example Swift code
- Category:Data types
- Category:Software design patterns

## Table of Contents

- Examples
- See also
- References
- External links

## Content

A strongly typed identifier is user-defined data type which serves as an identifier or key that is strongly typed. This is a solution to the "primitive obsession" code smell as mentioned by Martin Fowler. The data type should preferably be immutable if possible. It is common for implementations to handle equality testing, serialization and model binding.
The strongly typed identifier commonly wraps the data type used as the primary key in the database, such as a string, an integer or universally unique identifier (UUID).
Web frameworks can often be configured to model bind properties on view models that are strongly typed identifiers. Object–relational mappers can often be configured with value converters to map data between the properties on a model using strongly typed identifier data types and database columns.

Examples
Passing a strongly typed identifier throughout the layers of an example application.

C#
C# have records which provide immutability and equality testing. The record is sealed to prevent inheritance. It overrides the built-in ToString() method.
This example implementation includes a static method which can be used to initialize a new instance with a randomly generated globally unique identifier (GUID).

C++
C++ have structs but not immutability so here the id field is marked as private with a method named value() to get the value.

Crystal
Crystal's standard library provides the record macro for creating records which are immutable structs and lets you create override the built-in to_s method.

D
D have immutable structs.

Dart
Dart have classes with operator overloading.

F#
F# lets you create override the Equals, GetHashCode and ToString methods.

Go
Go have structs which provide equality testing. Go however does not provide immutability.

Groovy
Groovy have record classes which provide immutability and equality testing.

Haskell
Haskell can create user-defined custom data types using the newtype keyword. It provides equality testing using the Eq standard class and printing using the Read and Show standard classes.

Java
Java have records which provide equality testing.
The record is declared using the final modifier keyword to prevent inheritance. It overrides the built-in toString() method.

JavaScript
This JavaScript example implementation provides the toJSON method used by the JSON.stringify() function to serialize the class into a simple string instead of a composite data type.
It calls Object.freeze() to make the instance immutable.
It overrides the built-in toString() method and the valueOf() method.

Julia
Julia have immutable composite data types.

Kotlin
Kotlin have "inline classes".

Nim
Nim have "distinct types".

PHP
This PHP example implementation implements the __toString() magic method.
Furthermore, it implements the JsonSerializable interface which is used by the built-in json_encode function to serialize the class into a simple string instead of a composite data type.
The class is declared using the final modifier keyword to prevent inheritance.
PHP has traits as a way to re-use code.

Python
Python has data classes which provides equality testing and can be made immutable using the frozen parameter. It overrides the __str__ dunder method.
This example implementation includes a static method which can be used to initialize a new instance with a randomly generated universally unique identifier (UUID).

Python also has NewType which can be used to create new data types.

Ruby
Ruby have data classes which provides equality testing and are immutable. It overrides the built-in to_s method.
This example implementation includes a static method which can be used to initialize a new instance with a randomly generated universally unique identifier (UUID).

Rust
In Rust this can be done using a tuple struct containing a single value. This example implementation implements the Debug and the PartialEq traits. The PartialEq trait provides equality testing.

Scala
Scala have case classes which provide immutability and equality testing. The case class is sealed to prevent inheritance.

Swift
Swift have the CustomStringConvertible protocol which can be used to provide its own representation to be used when converting an instance to a string, and the Equatable protocol which provides equality testing.

Zig
Zig have structs with constants but by design does not have operator overloading and method overriding.

See also
Domain-driven design
Type safety
Value object

References
External links
https://wiki.c2.com/?PrimitiveObsession

## Related Articles

### Internal Links

- [Abstract data type](https://en.wikipedia.org/wiki/Abstract_data_type)
- [Abstract factory pattern](https://en.wikipedia.org/wiki/Abstract_factory_pattern)
- [Action–domain–responder](https://en.wikipedia.org/wiki/Action%E2%80%93domain%E2%80%93responder)
- [Active object](https://en.wikipedia.org/wiki/Active_object)
- [Active record pattern](https://en.wikipedia.org/wiki/Active_record_pattern)
- [Adapter pattern](https://en.wikipedia.org/wiki/Adapter_pattern)
- [Algebraic data type](https://en.wikipedia.org/wiki/Algebraic_data_type)
- [Anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern)
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Arbitrary-precision arithmetic](https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic)
- [Architectural pattern](https://en.wikipedia.org/wiki/Architectural_pattern)
- [Array (data type)](https://en.wikipedia.org/wiki/Array_(data_type))
- [Associative array](https://en.wikipedia.org/wiki/Associative_array)
- [Asynchronous method invocation](https://en.wikipedia.org/wiki/Asynchronous_method_invocation)
- [Balking pattern](https://en.wikipedia.org/wiki/Balking_pattern)
- [Behavioral pattern](https://en.wikipedia.org/wiki/Behavioral_pattern)
- [Bfloat16 floating-point format](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format)
- [Binding properties pattern](https://en.wikipedia.org/wiki/Binding_properties_pattern)
- [Bit](https://en.wikipedia.org/wiki/Bit)
- [Bit array](https://en.wikipedia.org/wiki/Bit_array)
- [Blackboard (design pattern)](https://en.wikipedia.org/wiki/Blackboard_(design_pattern))
- [Boolean data type](https://en.wikipedia.org/wiki/Boolean_data_type)
- [Bottom type](https://en.wikipedia.org/wiki/Bottom_type)
- [Boxing (computer programming)](https://en.wikipedia.org/wiki/Boxing_(computer_programming))
- [Bridge pattern](https://en.wikipedia.org/wiki/Bridge_pattern)
- [Broker pattern](https://en.wikipedia.org/wiki/Broker_pattern)
- [Builder pattern](https://en.wikipedia.org/wiki/Builder_pattern)
- [Business delegate pattern](https://en.wikipedia.org/wiki/Business_delegate_pattern)
- [Byte](https://en.wikipedia.org/wiki/Byte)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Chain-of-responsibility pattern](https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern)
- [Character (computing)](https://en.wikipedia.org/wiki/Character_(computing))
- [Christopher Alexander](https://en.wikipedia.org/wiki/Christopher_Alexander)
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Code smell](https://en.wikipedia.org/wiki/Code_smell)
- [Command pattern](https://en.wikipedia.org/wiki/Command_pattern)
- [Complex data type](https://en.wikipedia.org/wiki/Complex_data_type)
- [Composite data type](https://en.wikipedia.org/wiki/Composite_data_type)
- [Composite entity pattern](https://en.wikipedia.org/wiki/Composite_entity_pattern)
- [Composite pattern](https://en.wikipedia.org/wiki/Composite_pattern)
- [Concurrency pattern](https://en.wikipedia.org/wiki/Concurrency_pattern)
- [Container (abstract data type)](https://en.wikipedia.org/wiki/Container_(abstract_data_type))
- [Creational pattern](https://en.wikipedia.org/wiki/Creational_pattern)
- [Crystal (programming language)](https://en.wikipedia.org/wiki/Crystal_(programming_language))
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Dart (programming language)](https://en.wikipedia.org/wiki/Dart_(programming_language))
- [Data access object](https://en.wikipedia.org/wiki/Data_access_object)
- [Data structure](https://en.wikipedia.org/wiki/Data_structure)
- [Data transfer object](https://en.wikipedia.org/wiki/Data_transfer_object)
- [Data type](https://en.wikipedia.org/wiki/Data_type)
- [Decimal data type](https://en.wikipedia.org/wiki/Decimal_data_type)
- [Decorator pattern](https://en.wikipedia.org/wiki/Decorator_pattern)
- [Delegation pattern](https://en.wikipedia.org/wiki/Delegation_pattern)
- [Dependency injection](https://en.wikipedia.org/wiki/Dependency_injection)
- [Dependent type](https://en.wikipedia.org/wiki/Dependent_type)
- [Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns)
- [Domain-driven design](https://en.wikipedia.org/wiki/Domain-driven_design)
- [Double-checked locking](https://en.wikipedia.org/wiki/Double-checked_locking)
- [Double-precision floating-point format](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)
- [Douglas C. Schmidt](https://en.wikipedia.org/wiki/Douglas_C._Schmidt)
- [Empty type](https://en.wikipedia.org/wiki/Empty_type)
- [Enterprise Integration Patterns](https://en.wikipedia.org/wiki/Enterprise_Integration_Patterns)
- [Entity component system](https://en.wikipedia.org/wiki/Entity_component_system)
- [Enumerated type](https://en.wikipedia.org/wiki/Enumerated_type)
- [Erich Gamma](https://en.wikipedia.org/wiki/Erich_Gamma)
- [Exception handling](https://en.wikipedia.org/wiki/Exception_handling)
- [Extended precision](https://en.wikipedia.org/wiki/Extended_precision)
- [F Sharp (programming language)](https://en.wikipedia.org/wiki/F_Sharp_(programming_language))
- [Facade pattern](https://en.wikipedia.org/wiki/Facade_pattern)
- [Factory method pattern](https://en.wikipedia.org/wiki/Factory_method_pattern)
- [Fixed-point arithmetic](https://en.wikipedia.org/wiki/Fixed-point_arithmetic)
- [Floating-point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic)
- [Flyweight pattern](https://en.wikipedia.org/wiki/Flyweight_pattern)
- [Front controller](https://en.wikipedia.org/wiki/Front_controller)
- [Function type](https://en.wikipedia.org/wiki/Function_type)
- [Generalized algebraic data type](https://en.wikipedia.org/wiki/Generalized_algebraic_data_type)
- [Generic programming](https://en.wikipedia.org/wiki/Generic_programming)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Grady Booch](https://en.wikipedia.org/wiki/Grady_Booch)
- [Guarded suspension](https://en.wikipedia.org/wiki/Guarded_suspension)
- [Half-precision floating-point format](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Identity map pattern](https://en.wikipedia.org/wiki/Identity_map_pattern)
- [Immutable object](https://en.wikipedia.org/wiki/Immutable_object)
- [Inductive type](https://en.wikipedia.org/wiki/Inductive_type)
- [Inheritance (object-oriented programming)](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
- [Integer (computer science)](https://en.wikipedia.org/wiki/Integer_(computer_science))
- [Intercepting filter pattern](https://en.wikipedia.org/wiki/Intercepting_filter_pattern)
- [Interceptor pattern](https://en.wikipedia.org/wiki/Interceptor_pattern)
- [Interface (object-oriented programming)](https://en.wikipedia.org/wiki/Interface_(object-oriented_programming))
- [Interpreter pattern](https://en.wikipedia.org/wiki/Interpreter_pattern)
- [Intersection type](https://en.wikipedia.org/wiki/Intersection_type)
- [Interval arithmetic](https://en.wikipedia.org/wiki/Interval_arithmetic)
- [Intuitionistic type theory](https://en.wikipedia.org/wiki/Intuitionistic_type_theory)
- [Inversion of control](https://en.wikipedia.org/wiki/Inversion_of_control)
- [Iterator pattern](https://en.wikipedia.org/wiki/Iterator_pattern)
- [JSP model 2 architecture](https://en.wikipedia.org/wiki/JSP_model_2_architecture)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Jim Coplien](https://en.wikipedia.org/wiki/Jim_Coplien)
- [John Vlissides](https://en.wikipedia.org/wiki/John_Vlissides)
- [Join-pattern](https://en.wikipedia.org/wiki/Join-pattern)
- [Julia (programming language)](https://en.wikipedia.org/wiki/Julia_(programming_language))
- [Kent Beck](https://en.wikipedia.org/wiki/Kent_Beck)
- [Kind (type theory)](https://en.wikipedia.org/wiki/Kind_(type_theory))
- [Kotlin (programming language)](https://en.wikipedia.org/wiki/Kotlin_(programming_language))
- [Lazy loading](https://en.wikipedia.org/wiki/Lazy_loading)
- [Linda Rising](https://en.wikipedia.org/wiki/Linda_Rising)
- [List (abstract data type)](https://en.wikipedia.org/wiki/List_(abstract_data_type))
- [Lock (computer science)](https://en.wikipedia.org/wiki/Lock_(computer_science))
- [Long double](https://en.wikipedia.org/wiki/Long_double)
- [Martin Fowler (software engineer)](https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer))
- [Mediator pattern](https://en.wikipedia.org/wiki/Mediator_pattern)
- [Memento pattern](https://en.wikipedia.org/wiki/Memento_pattern)
- [Memory address](https://en.wikipedia.org/wiki/Memory_address)
- [Metaclass](https://en.wikipedia.org/wiki/Metaclass)
- [Metaobject](https://en.wikipedia.org/wiki/Metaobject)
- [Method chaining](https://en.wikipedia.org/wiki/Method_chaining)
- [Minifloat](https://en.wikipedia.org/wiki/Minifloat)
- [Mock object](https://en.wikipedia.org/wiki/Mock_object)
- [Model–view–controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
- [Model–view–presenter](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter)
- [Model–view–viewmodel](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)
- [Monitor (synchronization)](https://en.wikipedia.org/wiki/Monitor_(synchronization))
- [Multitier architecture](https://en.wikipedia.org/wiki/Multitier_architecture)
- [Naked objects](https://en.wikipedia.org/wiki/Naked_objects)
- [Nim (programming language)](https://en.wikipedia.org/wiki/Nim_(programming_language))
- [Null-terminated string](https://en.wikipedia.org/wiki/Null-terminated_string)
- [Null object pattern](https://en.wikipedia.org/wiki/Null_object_pattern)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Object pool pattern](https://en.wikipedia.org/wiki/Object_pool_pattern)
- [Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
- [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern)
- [Octuple-precision floating-point format](https://en.wikipedia.org/wiki/Octuple-precision_floating-point_format)
- [Opaque data type](https://en.wikipedia.org/wiki/Opaque_data_type)
- [Option type](https://en.wikipedia.org/wiki/Option_type)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Parametric polymorphism](https://en.wikipedia.org/wiki/Parametric_polymorphism)
- [Physical address](https://en.wikipedia.org/wiki/Physical_address)
- [Plain text](https://en.wikipedia.org/wiki/Plain_text)
- [Pointer (computer programming)](https://en.wikipedia.org/wiki/Pointer_(computer_programming))
- [Portland Pattern Repository](https://en.wikipedia.org/wiki/Portland_Pattern_Repository)
- [Primary key](https://en.wikipedia.org/wiki/Primary_key)
- [Primitive data type](https://en.wikipedia.org/wiki/Primitive_data_type)
- [Proactor pattern](https://en.wikipedia.org/wiki/Proactor_pattern)
- [Product type](https://en.wikipedia.org/wiki/Product_type)
- [Prototype pattern](https://en.wikipedia.org/wiki/Prototype_pattern)
- [Proxy pattern](https://en.wikipedia.org/wiki/Proxy_pattern)
- [Publish–subscribe pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation)
- [Quadruple-precision floating-point format](https://en.wikipedia.org/wiki/Quadruple-precision_floating-point_format)
- [Ralph Johnson (computer scientist)](https://en.wikipedia.org/wiki/Ralph_Johnson_(computer_scientist))
- [Rational data type](https://en.wikipedia.org/wiki/Rational_data_type)
- [Reactor pattern](https://en.wikipedia.org/wiki/Reactor_pattern)
- [Readers–writer lock](https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock)
- [Record (computer science)](https://en.wikipedia.org/wiki/Record_(computer_science))
- [Recursive data type](https://en.wikipedia.org/wiki/Recursive_data_type)
- [Reference (computer science)](https://en.wikipedia.org/wiki/Reference_(computer_science))
- [Refinement type](https://en.wikipedia.org/wiki/Refinement_type)
- [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scheduled-task pattern](https://en.wikipedia.org/wiki/Scheduled-task_pattern)
- [Scheduling (computing)](https://en.wikipedia.org/wiki/Scheduling_(computing))
- [Semaphore (programming)](https://en.wikipedia.org/wiki/Semaphore_(programming))
- [Serialization](https://en.wikipedia.org/wiki/Serialization)
- [Servant (design pattern)](https://en.wikipedia.org/wiki/Servant_(design_pattern))
- [Service locator pattern](https://en.wikipedia.org/wiki/Service_locator_pattern)
- [Set (abstract data type)](https://en.wikipedia.org/wiki/Set_(abstract_data_type))
- [Signedness](https://en.wikipedia.org/wiki/Signedness)
- [Single-precision floating-point format](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)
- [Singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern)
- [Software design pattern](https://en.wikipedia.org/wiki/Software_design_pattern)
- [Specification pattern](https://en.wikipedia.org/wiki/Specification_pattern)
- [State pattern](https://en.wikipedia.org/wiki/State_pattern)
- [Strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern)
- [Stream (computing)](https://en.wikipedia.org/wiki/Stream_(computing))
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [Strong and weak typing](https://en.wikipedia.org/wiki/Strong_and_weak_typing)
- [Structural pattern](https://en.wikipedia.org/wiki/Structural_pattern)
- [Subtyping](https://en.wikipedia.org/wiki/Subtyping)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Tagged union](https://en.wikipedia.org/wiki/Tagged_union)
- [Template method pattern](https://en.wikipedia.org/wiki/Template_method_pattern)
- [Ternary numeral system](https://en.wikipedia.org/wiki/Ternary_numeral_system)
- [The Hillside Group](https://en.wikipedia.org/wiki/The_Hillside_Group)
- [Thread-local storage](https://en.wikipedia.org/wiki/Thread-local_storage)
- [Thread pool](https://en.wikipedia.org/wiki/Thread_pool)
- [Top type](https://en.wikipedia.org/wiki/Top_type)
- [Trait (computer programming)](https://en.wikipedia.org/wiki/Trait_(computer_programming))
- [Tuple](https://en.wikipedia.org/wiki/Tuple)
- [Twin pattern](https://en.wikipedia.org/wiki/Twin_pattern)
- [Shim (computing)](https://en.wikipedia.org/wiki/Shim_(computing))
- [Type class](https://en.wikipedia.org/wiki/Type_class)
- [Type constructor](https://en.wikipedia.org/wiki/Type_constructor)
- [Type conversion](https://en.wikipedia.org/wiki/Type_conversion)
- [Type safety](https://en.wikipedia.org/wiki/Type_safety)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Type theory](https://en.wikipedia.org/wiki/Type_theory)
- [Union type](https://en.wikipedia.org/wiki/Union_type)
- [Unit type](https://en.wikipedia.org/wiki/Unit_type)
- [Units of information](https://en.wikipedia.org/wiki/Units_of_information)
- [Universally unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier)
- [Value object](https://en.wikipedia.org/wiki/Value_object)
- [Variable (computer science)](https://en.wikipedia.org/wiki/Variable_(computer_science))
- [Virtual address space](https://en.wikipedia.org/wiki/Virtual_address_space)
- [Visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern)
- [Void type](https://en.wikipedia.org/wiki/Void_type)
- [Ward Cunningham](https://en.wikipedia.org/wiki/Ward_Cunningham)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [Word (computer architecture)](https://en.wikipedia.org/wiki/Word_(computer_architecture))
- [Zig (programming language)](https://en.wikipedia.org/wiki/Zig_(programming_language))
- [Template:Data types](https://en.wikipedia.org/wiki/Template:Data_types)
- [Template:Design patterns](https://en.wikipedia.org/wiki/Template:Design_patterns)
- [Template talk:Data types](https://en.wikipedia.org/wiki/Template_talk:Data_types)
- [Template talk:Design patterns](https://en.wikipedia.org/wiki/Template_talk:Design_patterns)
- [Portal:Computer programming](https://en.wikipedia.org/wiki/Portal:Computer_programming)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:45:26.203044+00:00_