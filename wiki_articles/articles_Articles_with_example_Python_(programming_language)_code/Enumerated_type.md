# Enumerated type

## Article Metadata

- **Last Updated:** 2024-12-14T19:36:44.164442+00:00
- **Original Article:** [Enumerated type](https://en.wikipedia.org/wiki/Enumerated_type)
- **Language:** en
- **Page ID:** 4723370

## Summary

In computer programming, an enumerated type (also called enumeration, enum, or factor in the R programming language, and a categorical variable in statistics) is a data type consisting of a set of named values called elements, members, enumeral,  or enumerators of the type. The enumerator names are usually identifiers that behave as constants in the language. An enumerated type can be seen as a degenerate tagged union of unit type. A variable that has been declared as having an enumerated type c

## Categories

- Category:Articles with example Ada code
- Category:Articles with example Python (programming language) code
- Category:Articles with excerpts
- Category:Articles with short description
- Category:CS1 German-language sources (de)
- Category:CS1 maint: bot: original URL status unknown
- Category:CS1 maint: multiple names: authors list
- Category:Data types
- Category:Short description is different from Wikidata
- Category:Type theory
- Category:Webarchive template wayback links

## Table of Contents

- Description
- Rationale
- Conventions
- Syntax in several programming languages
- Algebraic data type in functional programming
- Databases
- XML Schema
- See also
- References
- External links

## Content

In computer programming, an enumerated type (also called enumeration, enum, or factor in the R programming language, and a categorical variable in statistics) is a data type consisting of a set of named values called elements, members, enumeral,  or enumerators of the type. The enumerator names are usually identifiers that behave as constants in the language. An enumerated type can be seen as a degenerate tagged union of unit type. A variable that has been declared as having an enumerated type can be assigned any of the enumerators as a value. In other words, an enumerated type has values that are different from each other, and that can be compared and assigned, but are not specified by the programmer  as having any particular concrete representation in the computer's memory; compilers and interpreters can represent them arbitrarily.

Description
For example, the four suits in a deck of playing cards may be four enumerators named Club, Diamond, Heart, and Spade, belonging to an enumerated type named suit. If a variable V is declared having suit as its data type, one can assign any of those four values to it.
Although the enumerators are usually distinct, some languages may allow the same enumerator to be listed twice in the type's declaration. The names of enumerators need not be semantically complete or compatible in any sense. For example, an enumerated type called color may be defined to consist of the enumerators Red, Green, Zebra, Missing, and Bacon. In some languages, the declaration of an enumerated type also intentionally defines an ordering of its members (High, Medium and Low priorities); in others, the enumerators are unordered (English, French, German and Spanish supported languages); in others still, an implicit ordering arises from the compiler concretely representing enumerators as integers.
Some enumerator types may be built into the language. The Boolean type, for example is often a pre-defined enumeration of the values False and True. A unit type consisting of a single value may also be defined to represent null. Many languages allow users to define new enumerated types.
Values and variables of an enumerated type are usually implemented with some integer type as the underlying representation. Some languages, especially system programming languages, allow the user to specify the bit combination to be used for each enumerator, which can be useful to efficiently represent sets of enumerators as fixed-length bit strings. In type theory, enumerated types are often regarded as tagged unions of unit types. Since such types are of the form 
  
    
      
        1
        +
        1
        +
        ⋯
        +
        1
      
    
    {\displaystyle 1+1+\cdots +1}
  
, they may also be written as natural numbers.

Rationale
Some early programming languages did not originally have enumerated types. If a programmer wanted a variable, for example myColor, to have a value of red, the variable red would be declared and assigned some arbitrary value, usually an integer constant. The variable red would then be assigned to myColor. Other techniques assigned arbitrary values to strings containing the names of the enumerators.
These arbitrary values were sometimes referred to as magic numbers since there often was no explanation as to how the numbers were obtained or whether their actual values were significant. These magic numbers could make the source code harder for others to understand and maintain.
Enumerated types, on the other hand, make the code more self-documenting. Depending on the language, the compiler could automatically assign default values to the enumerators thereby hiding unnecessary detail from the programmer. These values may not even be visible to the programmer (see information hiding). Enumerated types can also prevent a programmer from writing illogical code such as performing mathematical operations on the values of the enumerators. If the value of a variable that was assigned an enumerator were to be printed, some programming languages could also print the name of the enumerator rather than its underlying numerical value. A further advantage is that enumerated types can allow compilers to enforce semantic correctness. For instance:
myColor = TRIANGLE 
can be forbidden, whilst 
myColor = RED
is accepted, even if TRIANGLE and RED are both internally represented as 1.
Conceptually, an enumerated type is similar to a list of nominals (numeric codes), since each possible value of the type is assigned a distinctive natural number. A given enumerated type is thus a concrete implementation of this notion. When order is meaningful and/or used for comparison, then an enumerated type becomes an ordinal type.

Conventions
Programming languages tend to have their own, oftentimes multiple, programming styles and naming conventions. The variable assigned to an enumeration is usually a noun in singular form, and frequently follows either a PascalCase or uppercase convention, while lowercase and others are seen less frequently.

Syntax in several programming languages
Pascal and syntactically similar languages
Pascal
In Pascal, an enumerated type can be implicitly declared by listing the values in a parenthesised list:

  
The declaration will often appear in a type synonym declaration, such that it can be used for multiple variables:

The order in which the enumeration values are given matters. An enumerated type is an ordinal type, and the pred and succ functions will give the prior or next value of the enumeration, and ord can convert enumeration values to their integer representation. Standard Pascal does not offer a conversion from arithmetic types to enumerations, however. Extended Pascal offers this functionality via an extended succ function. Some other Pascal dialects allow it via type-casts. Some modern descendants of Pascal, such as Modula-3, provide a special conversion syntax using a method called VAL; Modula-3 also treats BOOLEAN and CHAR as special pre-defined enumerated types and uses ORD and VAL for standard ASCII decoding and encoding.
Pascal style languages also allow enumeration to be used as array index:

Ada
In Ada, the use of "=" was replaced with "is" leaving the definition quite similar:

 
In addition to Pred, Succ, Val and Pos Ada also supports simple string conversions via Image and Value.
Similar to C-style languages Ada allows the internal representation of the enumeration to be specified:

Unlike C-style languages Ada also allows the number of bits of the enumeration to be specified:

Additionally, one can use enumerations as indexes for arrays, like in Pascal, but there are attributes defined for enumerations

Like Modula-3 Ada treats Boolean and Character as special pre-defined (in package "Standard") enumerated types. Unlike Modula-3 one can also define own character types:

C and syntactically similar languages
C
The original K&R dialect of the programming language C had no enumerated types. In C, enumerations are created by explicit definitions (the enum keyword by itself does not cause allocation of storage) which use the enum keyword and are reminiscent of struct and union definitions:

C exposes the integer representation of enumeration values directly to the programmer. Integers and enum values can be mixed freely, and all arithmetic operations on enum values are permitted. It is even possible for an enum variable to hold an integer that does not represent any of the enumeration values. In fact, according to the language definition, the above code will define Clubs, Diamonds, Hearts, and Spades as constants of type int, which will only be converted (silently) to enum cardsuit if they are stored in a variable of that type.
C also allows the programmer to choose the values of the enumeration constants explicitly, even without type. For example,

could be used to define a type that allows mathematical sets of suits to be represented as an enum cardsuit by bitwise logic operations.
Since C23, the underlying type of an enumeration can be specified by the programmer:

C#
Enumerated types in the C# programming language preserve most of the "small integer" semantics of C's enums. Some arithmetic operations are not defined for enums, but an enum value can be explicitly converted to an integer and back again, and an enum variable can have values that were not declared by the enum definition. For example, given

the expressions CardSuit.Diamonds + 1 and CardSuit.Hearts - CardSuit.Clubs are allowed directly (because it may make sense to step through the sequence of values or ask how many steps there are between two values), but CardSuit.Hearts * CardSuit.Spades is deemed to make less sense and is only allowed if the values are first converted to integers.
C# also provides the C-like feature of being able to define specific integer values for enumerations. By doing this it is possible to perform binary operations on enumerations, thus treating enumeration values as sets of flags. These flags can be tested using binary operations or with the enum type's builtin 'HasFlag' method.
The enumeration definition defines names for the selected integer values and is syntactic sugar, as it is possible to assign to an enum variable other integer values that are not in the scope of the enum definition.

C++
C++ has enumeration types that are directly inherited from C's and work mostly like these, except that an enumeration is a real type in C++, giving added compile-time checking. Also (as with structs), the C++ enum keyword is combined with a typedef, so that instead of naming the type enum name, simply name it name. This can be simulated in C using a typedef: typedef enum {Value1, Value2} name;
C++11 also provides a second kind of enumeration, called a scoped enumeration. These are type-safe: the enumerators are not implicitly converted to an integer type. Among other things, this allows I/O streaming to be defined for the enumeration type. Another feature of scoped enumerations is that the enumerators do not leak, so usage requires prefixing with the name of the enumeration (e.g., Color::Red for the first enumerator in the example below), unless a using enum declaration (introduced in C++20) has been used to bring the enumerators into the current scope. A scoped enumeration is specified by the phrase enum class (or enum struct). For example:

The underlying type of an enumeration is an implementation-defined integral type that is large enough to hold all enumerated values; it does not have to be the smallest possible type. The underlying type can be specified directly, which allows "forward declarations" of enumerations:

Go
Go uses the iota keyword to create enumerated constants.

Haxe
Java
The J2SE version 5.0 of the Java programming language added enumerated types whose declaration syntax is
similar to that of C:

The Java type system, however, treats enumerations as a type separate from integers, and intermixing of enum and integer values is not allowed. In fact, an enum type in Java is actually a special compiler-generated class rather than an arithmetic type, and enum values behave as global pre-generated instances of that class. Enum types can have instance methods and a constructor (the arguments of which can be specified separately for each enum value). All enum types implicitly extend the Enum abstract class. An enum type cannot be instantiated directly.
Internally, each enum value contains an integer, corresponding to the order in which they are declared in the source code, starting from 0. The programmer cannot set a custom integer for an enum value directly, but one can define overloaded constructors that can then assign arbitrary values to self-defined members of the enum class. Defining getters allows then access to those self-defined members. The internal integer can be obtained from an enum value using the ordinal() method, and the list of enum values of an enumeration type can be obtained in order using the values() method. It is generally discouraged for programmers to convert enums to integers and vice versa. Enumerated types are Comparable, using the internal integer; as a result, they can be sorted.
The Java standard library provides utility classes to use with enumerations. The EnumSet class implements a Set of enum values; it is implemented as a bit array, which makes it very compact and as efficient as explicit bit manipulation, but safer. The EnumMap class implements a Map of enum values to object. It is implemented as an array, with the integer value of the enum value serving as the index.

Perl
Dynamically typed languages in the syntactic tradition of C (e.g., Perl or JavaScript) do not, in general, provide enumerations.  But in Perl programming the same result can be obtained with the shorthand strings list and hashes (possibly slices):

Raku
Raku (formerly known as Perl 6) supports enumerations. There are multiple ways to declare enumerations in Raku, all creating a back-end Map.

PHP
Enums were added in PHP version 8.1.

Enumerators may be backed by string or integer values to aid serialization:

The Enum's interface exposes a method that gives a collection of its enumerators and their names. String/integer-backed Enums also expose the backing value and methods to (attempt) deserialization. Users may add further methods.

Rust
Though Rust uses the enum keyword like C, it uses it to describe tagged unions, which enums can be considered a degenerate form of. Rust's enums are therefore much more flexible and can contain struct and tuple variants.

Like C, Rust also supports specifying the values of each variant,

Swift
In C, enumerations assign related names to a set of integer values. In Swift, enumerations are much more flexible and need not provide a value for each case of the enumeration. If a value (termed a raw value) is provided for each enumeration case, the value can be a string, a character, or a value of any integer or floating-point type.
Alternatively, enumeration cases can specify associated values of any type to be stored along with each different case value, much as unions or variants do in other languages. One can define a common set of related cases as part of one enumeration, each of which has a different set of values of appropriate types associated with it.
In Swift, enumerations are a first-class type. They adopt many features traditionally supported only by classes, such as computed properties to provide additional information about the enumeration's current value, and instance methods to provide functionality related to the values the enumeration represents. Enumerations can also define initializers to provide an initial case value and can be extended to expand their functionality beyond their original implementation; and can conform to protocols to provide standard functionality.

Unlike C and Objective-C, Swift enumeration cases are not assigned a default integer value when they are created. In the CardSuit example above, clubs, diamonds, hearts, and spades do not implicitly equal 0, 1, 2 and 3. Instead, the different enumeration cases are fully-fledged values in their own right, with an explicitly-defined type of CardSuit.
Multiple cases can appear on a single line, separated by commas:

When working with enumerations that store integer or string raw values, one doesn't need to explicitly assign a raw value for each case because Swift will automatically assign the values.
For instance, when integers are used for raw values, the implicit value for each case is one more than the previous case. If the first case doesn't have a value set, its value is 0. For the CardSuit example, suits can be numbered starting from 1 by writing:

TypeScript
TypeScript adds an 'enum' data type to JavaScript.

By default, enums number members starting at 0; this can be overridden by setting the value of the first:

All the values can be set:

TypeScript supports mapping the numeric value to its name. For example, this finds the name of the value 2:

Python
An enum module was added to the Python standard library in version 3.4.
There is also a functional API for creating enumerations with automatically generated indices (starting with one):

Python enumerations do not enforce semantic correctness (a meaningless comparison to an incompatible enumeration always returns False rather than raising a TypeError):

Fortran
Fortran only has enumerated types for interoperability with C; hence, the semantics is similar to C and, as in C, the enum values are just integers and no further type check is done. The C example from above can be written in Fortran as

Visual Basic/VBA
Enumerated datatypes in Visual Basic (up to version 6) and VBA are automatically assigned the "Long" datatype and also become a datatype themselves:

Example Code in VB.NET

Lisp
Common Lisp uses the member type specifier, e.g.,

that states that object is of type cardsuit if it is #'eql to club, diamond, heart or spade. The member type specifier is not valid as a Common Lisp Object System (CLOS) parameter specializer, however. Instead, (eql atom), which is the equivalent to (member atom) may be used (that is, only one member of the set may be specified with an eql type specifier, however, it may be used as a CLOS parameter specializer.) In other words, to define methods to cover an enumerated type, a method must be defined for each specific element of that type.
Additionally,

may be used to define arbitrary enumerated types at runtime. For instance

would refer to a type equivalent to the prior definition of cardsuit, as of course would simply have been using

but may be less confusing with the function #'member for stylistic reasons.

Dart
Dart has a support for the most basic form of enums and has a syntax that is a lot similar with other languages supporting enums.

Note that the switch operator does not guarantee the completeness of the cases. This means if you omit one case, the compiler will not raise an error.

Algebraic data type in functional programming
In functional programming languages in the ML lineage (e.g., Standard ML (SML), OCaml, and Haskell), an algebraic data type with only nullary constructors can be used to implement an enumerated type. For example (in the syntax of SML signatures):

In these languages the small-integer representation is completely hidden from the programmer, if indeed such a representation is employed by the implementation. However, Haskell has the Enum type class which a type can derive or implement to get a mapping between the type and Int.

Databases
Some databases support enumerated types directly. MySQL provides an enumerated type ENUM with allowable values specified as strings when a table is created. The values are stored as numeric indices with the empty string stored as 0, the first string value stored as 1, the second string value stored as 2, etc. Values can be stored and retrieved as numeric indexes or string values.
Example:

XML Schema
XML Schema supports enumerated types through the enumeration facet used for constraining most primitive datatypes such as strings.

See also
Contrast set

References
External links

Enumerated types in C/C++
Enumerated types in C#
Enumerated types in Java
Enumerated types in MySQL
Enumerated types in Obix
Enumerated types in PHP
Enumerated types in Swift
Enumerated types in XML
Enumerated types in Visual Basic

## Related Articles

### Internal Links

- [Abstract data type](https://en.wikipedia.org/wiki/Abstract_data_type)
- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language))
- [Algebraic data type](https://en.wikipedia.org/wiki/Algebraic_data_type)
- [Arbitrary-precision arithmetic](https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic)
- [Array (data type)](https://en.wikipedia.org/wiki/Array_(data_type))
- [Array slicing](https://en.wikipedia.org/wiki/Array_slicing)
- [Associative array](https://en.wikipedia.org/wiki/Associative_array)
- [Bfloat16 floating-point format](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format)
- [Bit](https://en.wikipedia.org/wiki/Bit)
- [Bit array](https://en.wikipedia.org/wiki/Bit_array)
- [Boolean data type](https://en.wikipedia.org/wiki/Boolean_data_type)
- [Boolean data type](https://en.wikipedia.org/wiki/Boolean_data_type)
- [Bottom type](https://en.wikipedia.org/wiki/Bottom_type)
- [Boxing (computer programming)](https://en.wikipedia.org/wiki/Boxing_(computer_programming))
- [Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan)
- [Primitive data type](https://en.wikipedia.org/wiki/Primitive_data_type)
- [Byte](https://en.wikipedia.org/wiki/Byte)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C++11](https://en.wikipedia.org/wiki/C%2B%2B11)
- [C++20](https://en.wikipedia.org/wiki/C%2B%2B20)
- [C23 (C standard revision)](https://en.wikipedia.org/wiki/C23_(C_standard_revision))
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Categorical variable](https://en.wikipedia.org/wiki/Categorical_variable)
- [Character (computing)](https://en.wikipedia.org/wiki/Character_(computing))
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Common Lisp Object System](https://en.wikipedia.org/wiki/Common_Lisp_Object_System)
- [Complex data type](https://en.wikipedia.org/wiki/Complex_data_type)
- [Composite data type](https://en.wikipedia.org/wiki/Composite_data_type)
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [Constant (computer programming)](https://en.wikipedia.org/wiki/Constant_(computer_programming))
- [Function overloading](https://en.wikipedia.org/wiki/Function_overloading)
- [Container (abstract data type)](https://en.wikipedia.org/wiki/Container_(abstract_data_type))
- [Contrast set](https://en.wikipedia.org/wiki/Contrast_set)
- [Dart (programming language)](https://en.wikipedia.org/wiki/Dart_(programming_language))
- [Data structure](https://en.wikipedia.org/wiki/Data_structure)
- [Data type](https://en.wikipedia.org/wiki/Data_type)
- [Database](https://en.wikipedia.org/wiki/Database)
- [Decimal data type](https://en.wikipedia.org/wiki/Decimal_data_type)
- [Declaration (computer programming)](https://en.wikipedia.org/wiki/Declaration_(computer_programming))
- [Dennis Ritchie](https://en.wikipedia.org/wiki/Dennis_Ritchie)
- [Dependent type](https://en.wikipedia.org/wiki/Dependent_type)
- [Double-precision floating-point format](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Empty type](https://en.wikipedia.org/wiki/Empty_type)
- [Englewood Cliffs, New Jersey](https://en.wikipedia.org/wiki/Englewood_Cliffs,_New_Jersey)
- [Exception handling](https://en.wikipedia.org/wiki/Exception_handling)
- [Extended precision](https://en.wikipedia.org/wiki/Extended_precision)
- [Fixed-point arithmetic](https://en.wikipedia.org/wiki/Fixed-point_arithmetic)
- [Floating-point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Function type](https://en.wikipedia.org/wiki/Function_type)
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [Generalized algebraic data type](https://en.wikipedia.org/wiki/Generalized_algebraic_data_type)
- [Generic programming](https://en.wikipedia.org/wiki/Generic_programming)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Half-precision floating-point format](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)
- [Hash table](https://en.wikipedia.org/wiki/Hash_table)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Haxe](https://en.wikipedia.org/wiki/Haxe)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Identifier (computer languages)](https://en.wikipedia.org/wiki/Identifier_(computer_languages))
- [Inductive type](https://en.wikipedia.org/wiki/Inductive_type)
- [Information hiding](https://en.wikipedia.org/wiki/Information_hiding)
- [Integer (computer science)](https://en.wikipedia.org/wiki/Integer_(computer_science))
- [Interface (object-oriented programming)](https://en.wikipedia.org/wiki/Interface_(object-oriented_programming))
- [Intersection type](https://en.wikipedia.org/wiki/Intersection_type)
- [Interval arithmetic](https://en.wikipedia.org/wiki/Interval_arithmetic)
- [Intuitionistic type theory](https://en.wikipedia.org/wiki/Intuitionistic_type_theory)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Joshua Bloch](https://en.wikipedia.org/wiki/Joshua_Bloch)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Kind (type theory)](https://en.wikipedia.org/wiki/Kind_(type_theory))
- [List (abstract data type)](https://en.wikipedia.org/wiki/List_(abstract_data_type))
- [Long double](https://en.wikipedia.org/wiki/Long_double)
- [Letter case](https://en.wikipedia.org/wiki/Letter_case)
- [ML (programming language)](https://en.wikipedia.org/wiki/ML_(programming_language))
- [Magic number (programming)](https://en.wikipedia.org/wiki/Magic_number_(programming))
- [Memory address](https://en.wikipedia.org/wiki/Memory_address)
- [Metaclass](https://en.wikipedia.org/wiki/Metaclass)
- [Metaobject](https://en.wikipedia.org/wiki/Metaobject)
- [Minifloat](https://en.wikipedia.org/wiki/Minifloat)
- [Modula-3](https://en.wikipedia.org/wiki/Modula-3)
- [MySQL](https://en.wikipedia.org/wiki/MySQL)
- [Naming convention (programming)](https://en.wikipedia.org/wiki/Naming_convention_(programming))
- [Nominal number](https://en.wikipedia.org/wiki/Nominal_number)
- [Null-terminated string](https://en.wikipedia.org/wiki/Null-terminated_string)
- [Nullary constructor](https://en.wikipedia.org/wiki/Nullary_constructor)
- [OCaml](https://en.wikipedia.org/wiki/OCaml)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [Octuple-precision floating-point format](https://en.wikipedia.org/wiki/Octuple-precision_floating-point_format)
- [Opaque data type](https://en.wikipedia.org/wiki/Opaque_data_type)
- [Option type](https://en.wikipedia.org/wiki/Option_type)
- [Ordinal number](https://en.wikipedia.org/wiki/Ordinal_number)
- [Parametric polymorphism](https://en.wikipedia.org/wiki/Parametric_polymorphism)
- [Camel case](https://en.wikipedia.org/wiki/Camel_case)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Physical address](https://en.wikipedia.org/wiki/Physical_address)
- [Plain text](https://en.wikipedia.org/wiki/Plain_text)
- [Pointer (computer programming)](https://en.wikipedia.org/wiki/Pointer_(computer_programming))
- [Prentice Hall](https://en.wikipedia.org/wiki/Prentice_Hall)
- [Primitive data type](https://en.wikipedia.org/wiki/Primitive_data_type)
- [Product type](https://en.wikipedia.org/wiki/Product_type)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Programming style](https://en.wikipedia.org/wiki/Programming_style)
- [Quadruple-precision floating-point format](https://en.wikipedia.org/wiki/Quadruple-precision_floating-point_format)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Raku (programming language)](https://en.wikipedia.org/wiki/Raku_(programming_language))
- [Rational data type](https://en.wikipedia.org/wiki/Rational_data_type)
- [Record (computer science)](https://en.wikipedia.org/wiki/Record_(computer_science))
- [Recursive data type](https://en.wikipedia.org/wiki/Recursive_data_type)
- [Reference (computer science)](https://en.wikipedia.org/wiki/Reference_(computer_science))
- [Refinement type](https://en.wikipedia.org/wiki/Refinement_type)
- [Semaphore (programming)](https://en.wikipedia.org/wiki/Semaphore_(programming))
- [Set (abstract data type)](https://en.wikipedia.org/wiki/Set_(abstract_data_type))
- [Signedness](https://en.wikipedia.org/wiki/Signedness)
- [Single-precision floating-point format](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)
- [Standard ML](https://en.wikipedia.org/wiki/Standard_ML)
- [Stream (computing)](https://en.wikipedia.org/wiki/Stream_(computing))
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [String literal](https://en.wikipedia.org/wiki/String_literal)
- [Strongly typed identifier](https://en.wikipedia.org/wiki/Strongly_typed_identifier)
- [Struct (C programming language)](https://en.wikipedia.org/wiki/Struct_(C_programming_language))
- [Subtyping](https://en.wikipedia.org/wiki/Subtyping)
- [Playing card suit](https://en.wikipedia.org/wiki/Playing_card_suit)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar)
- [System programming language](https://en.wikipedia.org/wiki/System_programming_language)
- [Tagged union](https://en.wikipedia.org/wiki/Tagged_union)
- [Ternary numeral system](https://en.wikipedia.org/wiki/Ternary_numeral_system)
- [Top type](https://en.wikipedia.org/wiki/Top_type)
- [Total order](https://en.wikipedia.org/wiki/Total_order)
- [Type class](https://en.wikipedia.org/wiki/Type_class)
- [Type constructor](https://en.wikipedia.org/wiki/Type_constructor)
- [Type conversion](https://en.wikipedia.org/wiki/Type_conversion)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Type theory](https://en.wikipedia.org/wiki/Type_theory)
- [Typedef](https://en.wikipedia.org/wiki/Typedef)
- [Union type](https://en.wikipedia.org/wiki/Union_type)
- [Unit type](https://en.wikipedia.org/wiki/Unit_type)
- [Units of information](https://en.wikipedia.org/wiki/Units_of_information)
- [Letter case](https://en.wikipedia.org/wiki/Letter_case)
- [Visual Basic (.NET)](https://en.wikipedia.org/wiki/Visual_Basic_(.NET))
- [Value (computer science)](https://en.wikipedia.org/wiki/Value_(computer_science))
- [Variable (computer science)](https://en.wikipedia.org/wiki/Variable_(computer_science))
- [Virtual address space](https://en.wikipedia.org/wiki/Virtual_address_space)
- [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic)
- [Visual Basic for Applications](https://en.wikipedia.org/wiki/Visual_Basic_for_Applications)
- [Void type](https://en.wikipedia.org/wiki/Void_type)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Word (computer architecture)](https://en.wikipedia.org/wiki/Word_(computer_architecture))
- [XML Schema (W3C)](https://en.wikipedia.org/wiki/XML_Schema_(W3C))
- [Template:Cite web](https://en.wikipedia.org/wiki/Template:Cite_web)
- [Template:Data types](https://en.wikipedia.org/wiki/Template:Data_types)
- [Template talk:Data types](https://en.wikipedia.org/wiki/Template_talk:Data_types)
- [Category:CS1 maint: bot: original URL status unknown](https://en.wikipedia.org/wiki/Category:CS1_maint:_bot:_original_URL_status_unknown)
- [Category:CS1 maint: multiple names: authors list](https://en.wikipedia.org/wiki/Category:CS1_maint:_multiple_names:_authors_list)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:36:44.164442+00:00_