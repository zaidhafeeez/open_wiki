# Duck typing

## Article Metadata

- **Last Updated:** 2024-12-14T19:36:38.254342+00:00
- **Original Article:** [Duck typing](https://en.wikipedia.org/wiki/Duck_typing)
- **Language:** en
- **Page ID:** 440018

## Summary

In computer programming, duck typing is an application of the duck test—"If it walks like a duck and it quacks like a duck, then it must be a duck"—to determine whether an object can be used for a particular purpose. With nominative typing, an object is of a given type if it is declared as such (or if a type's association with the object is inferred through mechanisms such as object inheritance). With duck typing, an object is of a given type if it has all methods and properties required by that

## Categories

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

## Related Articles

### Internal Links

- [Abstract type](https://en.wikipedia.org/wiki/Abstract_type)
- [Ad hoc polymorphism](https://en.wikipedia.org/wiki/Ad_hoc_polymorphism)
- [Adapter pattern](https://en.wikipedia.org/wiki/Adapter_pattern)
- [Boo (programming language)](https://en.wikipedia.org/wiki/Boo_(programming_language))
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Dependent type](https://en.wikipedia.org/wiki/Dependent_type)
- [Duck test](https://en.wikipedia.org/wiki/Duck_test)
- [Dynamic dispatch](https://en.wikipedia.org/wiki/Dynamic_dispatch)
- [Dynamic programming language](https://en.wikipedia.org/wiki/Dynamic_programming_language)
- [Elm (programming language)](https://en.wikipedia.org/wiki/Elm_(programming_language))
- [Extension method](https://en.wikipedia.org/wiki/Extension_method)
- [Flow-sensitive typing](https://en.wikipedia.org/wiki/Flow-sensitive_typing)
- [Generic programming](https://en.wikipedia.org/wiki/Generic_programming)
- [Gradual typing](https://en.wikipedia.org/wiki/Gradual_typing)
- [Interface (object-oriented programming)](https://en.wikipedia.org/wiki/Interface_(object-oriented_programming))
- [Intersection type](https://en.wikipedia.org/wiki/Intersection_type)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Latent typing](https://en.wikipedia.org/wiki/Latent_typing)
- [Loose coupling](https://en.wikipedia.org/wiki/Loose_coupling)
- [Manifest typing](https://en.wikipedia.org/wiki/Manifest_typing)
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Monkey patch](https://en.wikipedia.org/wiki/Monkey_patch)
- [Nominal type system](https://en.wikipedia.org/wiki/Nominal_type_system)
- [Nominal type system](https://en.wikipedia.org/wiki/Nominal_type_system)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Inheritance (object-oriented programming)](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
- [Operator overloading](https://en.wikipedia.org/wiki/Operator_overloading)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Refinement type](https://en.wikipedia.org/wiki/Refinement_type)
- [Reflective programming](https://en.wikipedia.org/wiki/Reflective_programming)
- [Execution (computing)](https://en.wikipedia.org/wiki/Execution_(computing))
- [Session type](https://en.wikipedia.org/wiki/Session_type)
- [Strong and weak typing](https://en.wikipedia.org/wiki/Strong_and_weak_typing)
- [Structural type system](https://en.wikipedia.org/wiki/Structural_type_system)
- [Substructural type system](https://en.wikipedia.org/wiki/Substructural_type_system)
- [Template metaprogramming](https://en.wikipedia.org/wiki/Template_metaprogramming)
- [TypeScript](https://en.wikipedia.org/wiki/TypeScript)
- [Type inference](https://en.wikipedia.org/wiki/Type_inference)
- [Type safety](https://en.wikipedia.org/wiki/Type_safety)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Uniqueness type](https://en.wikipedia.org/wiki/Uniqueness_type)
- [Unreachable code](https://en.wikipedia.org/wiki/Unreachable_code)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Template:Type systems](https://en.wikipedia.org/wiki/Template:Type_systems)
- [Template talk:Type systems](https://en.wikipedia.org/wiki/Template_talk:Type_systems)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:36:38.254342+00:00_