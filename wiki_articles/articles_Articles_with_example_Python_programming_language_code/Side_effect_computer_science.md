# Side effect (computer science)

## Metadata
- **Last Updated:** 2024-12-05 18:44:16 UTC
- **Original Article:** [Side effect (computer science)](https://en.wikipedia.org/wiki/Side_effect_(computer_science))
- **Language:** en
- **Page ID:** 29519

## Summary
In computer science, an operation, function or expression is said to have a side effect if it has any observable effect other than its primary effect of reading the value of its arguments and returning a value to the invoker of the operation. Example side effects include modifying a non-local variable, a static local variable or a mutable argument passed by reference; raising errors or exceptions; performing I/O; or calling other functions with side-effects. In the presence of side effects, a program's behaviour may depend on history; that is, the order of evaluation matters. Understanding and debugging a function with side effects requires knowledge about the context and its possible histories.
Side effects play an important role in the design and analysis of programming languages. The degree to which side effects are used depends on the programming paradigm. For example, imperative programming is commonly used to produce side effects, to update a system's state. By contrast, declarative programming is commonly used to report on the state of system, without side effects. 
Functional programming aims to minimize or eliminate side effects. The lack of side effects makes it easier to do formal verification of a program. The functional language Haskell eliminates side effects such as I/O and other stateful computations by replacing them with monadic actions. Functional languages such as Standard ML, Scheme and Scala do not restrict side effects, but it is customary for programmers to avoid them. 
Effect systems extend types to keep track of effects, permitting concise notation for functions with effects, while maintaining information about the extent and nature of side effects. In particular, functions without effects  correspond to pure functions.
Assembly language programmers must be aware of hidden side effects—instructions that modify parts of the processor state which are not mentioned in the instruction's mnemonic. A classic example of a hidden side effect is an arithmetic instruction that implicitly modifies condition codes (a hidden side effect) while it explicitly modifies a register (the intended effect). One potential drawback of an instruction set with hidden side effects is that, if many instructions have side effects on a single piece of state, like condition codes, then the logic required to update that state sequentially may become a performance bottleneck. The problem is particularly acute on some processors designed with pipelining (since 1990) or with out-of-order execution. Such a processor may require additional control circuitry to detect hidden side effects and stall the pipeline if the next instruction depends on the results of those effects.

## Categories
This article belongs to the following categories:

- Category:Articles with example C code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Computer programming
- Category:Functional programming
- Category:Programming language theory
- Category:Short description is different from Wikidata
- Category:Use dmy dates from December 2021
- Category:Use list-defined references from August 2022

## Table of Contents

- Referential transparency
- Temporal side effects
- Idempotence
- Example
- See also

## Content

In computer science, an operation, function or expression is said to have a side effect if it has any observable effect other than its primary effect of reading the value of its arguments and returning a value to the invoker of the operation. Example side effects include modifying a non-local variable, a static local variable or a mutable argument passed by reference; raising errors or exceptions; performing I/O; or calling other functions with side-effects. In the presence of side effects, a program's behaviour may depend on history; that is, the order of evaluation matters. Understanding and debugging a function with side effects requires knowledge about the context and its possible histories.
Side effects play an important role in the design and analysis of programming languages. The degree to which side effects are used depends on the programming paradigm. For example, imperative programming is commonly used to produce side effects, to update a system's state. By contrast, declarative programming is commonly used to report on the state of system, without side effects. 
Functional programming aims to minimize or eliminate side effects. The lack of side effects makes it easier to do formal verification of a program. The functional language Haskell eliminates side effects such as I/O and other stateful computations by replacing them with monadic actions. Functional languages such as Standard ML, Scheme and Scala do not restrict side effects, but it is customary for programmers to avoid them. 
Effect systems extend types to keep track of effects, permitting concise notation for functions with effects, while maintaining information about the extent and nature of side effects. In particular, functions without effects  correspond to pure functions.
Assembly language programmers must be aware of hidden side effects—instructions that modify parts of the processor state which are not mentioned in the instruction's mnemonic. A classic example of a hidden side effect is an arithmetic instruction that implicitly modifies condition codes (a hidden side effect) while it explicitly modifies a register (the intended effect). One potential drawback of an instruction set with hidden side effects is that, if many instructions have side effects on a single piece of state, like condition codes, then the logic required to update that state sequentially may become a performance bottleneck. The problem is particularly acute on some processors designed with pipelining (since 1990) or with out-of-order execution. Such a processor may require additional control circuitry to detect hidden side effects and stall the pipeline if the next instruction depends on the results of those effects.

Referential transparency
Absence of side effects is a necessary, but not sufficient, condition for referential transparency. Referential transparency means that an expression (such as a function call) can be replaced with its value. This requires that the expression is pure, that is to say the expression must be deterministic (always give the same value for the same input) and side-effect free.

Temporal side effects
Side effects caused by the time taken for an operation to execute are usually ignored when discussing side effects and referential transparency. There are some cases, such as with hardware timing or testing, where operations are inserted specifically for their temporal side effects e.g. sleep(5000) or for (int i = 0; i < 10000; ++i) {}. These instructions do not change state other than taking an amount of time to complete.

Idempotence
A subroutine with side effects is idempotent if multiple applications of the subroutine have the same effect on the system state as a single application, in other words if the function from the system state space to itself associated with the subroutine is idempotent in the mathematical sense. For instance, consider the following Python program:

setx is idempotent because the second application of setx to 3 has the same effect on the system state as the first application: x was already set to 3 after the first application, and it is still set to 3 after the second application.
A pure function is idempotent if it is idempotent in the mathematical sense. For instance, consider the following Python program:

abs is idempotent because the second application of abs to the return value of the first application to -3 returns the same value as the first application to -3.

Example
One common demonstration of side effect behavior is that of the assignment operator in C. The assignment a = b is an expression that evaluates to the same value as the expression b, with the side effect of storing the R-value of b into the L-value of a. This allows multiple assignment:

Because the operator right associates, this is equivalent to

This presents a potential hangup for novice programmers who may confuse

with

See also
Action at a distance (computer programming)
Don't-care term
Sequence point
Side-channel attack
Undefined behaviour
Unspecified behaviour
Frame problem


== References ==

## Archive Info
- **Archived on:** 2024-12-15 21:06:04 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 5070 bytes
- **Word Count:** 797 words
