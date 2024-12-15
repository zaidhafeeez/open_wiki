# Duck typing

## Metadata
- **Last Updated:** 2024-12-10 09:11:28 UTC
- **Original Article:** [Duck typing](https://en.wikipedia.org/wiki/Duck_typing)
- **Language:** en
- **Page ID:** 440018

## Summary
In computer programming, duck typing is an application of the duck test—"If it walks like a duck and it quacks like a duck, then it must be a duck"—to determine whether an object can be used for a particular purpose. With nominative typing, an object is of a given type if it is declared as such (or if a type's association with the object is inferred through mechanisms such as object inheritance). With duck typing, an object is of a given type if it has all methods and properties required by that type. Duck typing may be viewed as a usage-based structural equivalence between a given object and the requirements of a type.

## Categories
This article belongs to the following categories:

- Category:Articles with example Python (programming language) code
- Category:Articles with example pseudocode
- Category:Articles with short description
- Category:Ducks in popular culture
- Category:Object-oriented programming
- Category:Short description is different from Wikidata
- Category:Type theory
- Category:Webarchive template wayback links

## Table of Contents

- Example
- In statically typed languages
- Comparison with other type systems
- See also

## Content

In computer programming, duck typing is an application of the duck test—"If it walks like a duck and it quacks like a duck, then it must be a duck"—to determine whether an object can be used for a particular purpose. With nominative typing, an object is of a given type if it is declared as such (or if a type's association with the object is inferred through mechanisms such as object inheritance). With duck typing, an object is of a given type if it has all methods and properties required by that type. Duck typing may be viewed as a usage-based structural equivalence between a given object and the requirements of a type.

Example
This simple example in Python 3 demonstrates how any object may be used in any context until it is used in a way that it does not support.

Output:

If it can be assumed that anything that can swim is a duck because ducks can swim, a whale could be considered a duck; however, if it is also assumed that a duck must be capable of flying, the whale will not be considered a duck.

In statically typed languages
In some statically typed languages such as Boo and D, class type checking can be specified to occur at runtime rather than at compile time.

Comparison with other type systems
Structural type systems
Duck typing is similar to, but distinct from, structural typing. Structural typing is a static typing system that determines type compatibility and equivalence by a type's structure, whereas duck typing is dynamic and determines type compatibility by only that part of a type's structure that is accessed during runtime.
The TypeScript, Elm and Python languages support structural typing to varying degrees.

Protocols and interfaces
Protocols and interfaces provide a way to explicitly declare that some methods, operators or behaviors must be defined. If a third-party library implements a class that cannot be modified, a client cannot use an instance of it with an interface unknown to that library even if the class satisfies the interface requirements. A common solution to this problem is the adapter pattern. In contrast, with duck typing, the object would be accepted directly without the need for an adapter.

Templates or generic types
Template (also called generic) functions or methods apply the duck test in a static typing context; this brings all of the advantages and disadvantages of static versus dynamic type checking. Duck typing can also be more flexible in that only the methods actually called at runtime must be implemented, while templates require implementations of all methods that cannot be proven unreachable at compile time.
In languages such as Java, Scala and Objective-C, reflection may be employed to inspect whether objects implement methods or add necessary methods at runtime. For example, Java's MethodHandle API can be used in this manner.

See also
Ad hoc polymorphism
Dynamic dispatch
Dynamic programming language
Extension method
Loose coupling
Monkey patch
Operator overloading


== References ==

## Archive Info
- **Archived on:** 2024-12-15 15:18:28 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2991 bytes
- **Word Count:** 493 words
