# Side effect (computer science)

## Article Metadata

- **Last Updated:** 2024-12-15T04:48:04.263091+00:00
- **Original Article:** [Side effect (computer science)](https://en.wikipedia.org/wiki/Side_effect_(computer_science))
- **Language:** en
- **Page ID:** 29519

## Summary

In computer science, an operation, function or expression is said to have a side effect if it has any observable effect other than its primary effect of reading the value of its arguments and returning a value to the invoker of the operation. Example side effects include modifying a non-local variable, a static local variable or a mutable argument passed by reference; raising errors or exceptions; performing I/O; or calling other functions with side-effects. In the presence of side effects, a pr

## Categories

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

## Related Articles

### Internal Links

- [ACL2](https://en.wikipedia.org/wiki/ACL2)
- [Abstract interpretation](https://en.wikipedia.org/wiki/Abstract_interpretation)
- [Abstract rewriting system](https://en.wikipedia.org/wiki/Abstract_rewriting_system)
- [Action at a distance (computer programming)](https://en.wikipedia.org/wiki/Action_at_a_distance_(computer_programming))
- [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
- [Agda (programming language)](https://en.wikipedia.org/wiki/Agda_(programming_language))
- [Alias analysis](https://en.wikipedia.org/wiki/Alias_analysis)
- [Alloy (specification language)](https://en.wikipedia.org/wiki/Alloy_(specification_language))
- [Assembly language](https://en.wikipedia.org/wiki/Assembly_language)
- [Assignment (computer science)](https://en.wikipedia.org/wiki/Assignment_(computer_science))
- [Axiomatic semantics](https://en.wikipedia.org/wiki/Axiomatic_semantics)
- [Operational semantics](https://en.wikipedia.org/wiki/Operational_semantics)
- [Binary decision diagram](https://en.wikipedia.org/wiki/Binary_decision_diagram)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Categorical logic](https://en.wikipedia.org/wiki/Categorical_logic)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Completeness (logic)](https://en.wikipedia.org/wiki/Completeness_(logic))
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Concolic testing](https://en.wikipedia.org/wiki/Concolic_testing)
- [Constrained Horn clauses](https://en.wikipedia.org/wiki/Constrained_Horn_clauses)
- [Constraint programming](https://en.wikipedia.org/wiki/Constraint_programming)
- [Control-flow graph](https://en.wikipedia.org/wiki/Control-flow_graph)
- [Control-flow analysis](https://en.wikipedia.org/wiki/Control-flow_analysis)
- [Coq (software)](https://en.wikipedia.org/wiki/Coq_(software))
- [Correctness (computer science)](https://en.wikipedia.org/wiki/Correctness_(computer_science))
- [Curry–Howard correspondence](https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence)
- [Data-flow analysis](https://en.wikipedia.org/wiki/Data-flow_analysis)
- [David Turner (computer scientist)](https://en.wikipedia.org/wiki/David_Turner_(computer_scientist))
- [Declarative programming](https://en.wikipedia.org/wiki/Declarative_programming)
- [Denotational semantics](https://en.wikipedia.org/wiki/Denotational_semantics)
- [Dependence analysis](https://en.wikipedia.org/wiki/Dependence_analysis)
- [Deterministic algorithm](https://en.wikipedia.org/wiki/Deterministic_algorithm)
- [Disjoint-set data structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)
- [Don't-care term](https://en.wikipedia.org/wiki/Don%27t-care_term)
- [Dynamic program analysis](https://en.wikipedia.org/wiki/Dynamic_program_analysis)
- [Dynamic program analysis](https://en.wikipedia.org/wiki/Dynamic_program_analysis)
- [E-graph](https://en.wikipedia.org/wiki/E-graph)
- [Effect system](https://en.wikipedia.org/wiki/Effect_system)
- [Escape analysis](https://en.wikipedia.org/wiki/Escape_analysis)
- [Evaluation strategy](https://en.wikipedia.org/wiki/Evaluation_strategy)
- [Expression (computer science)](https://en.wikipedia.org/wiki/Expression_(computer_science))
- [F* (programming language)](https://en.wikipedia.org/wiki/F*_(programming_language))
- [Formal methods](https://en.wikipedia.org/wiki/Formal_methods)
- [Formal specification](https://en.wikipedia.org/wiki/Formal_specification)
- [Formal verification](https://en.wikipedia.org/wiki/Formal_verification)
- [Frame problem](https://en.wikipedia.org/wiki/Frame_problem)
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [Fuzzing](https://en.wikipedia.org/wiki/Fuzzing)
- [HOL (proof assistant)](https://en.wikipedia.org/wiki/HOL_(proof_assistant))
- [HOL Light](https://en.wikipedia.org/wiki/HOL_Light)
- [Hash consing](https://en.wikipedia.org/wiki/Hash_consing)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Side effect (computer science)](https://en.wikipedia.org/wiki/Side_effect_(computer_science))
- [Hidden variable](https://en.wikipedia.org/wiki/Hidden_variable)
- [Hoare logic](https://en.wikipedia.org/wiki/Hoare_logic)
- [Hyperproperty](https://en.wikipedia.org/wiki/Hyperproperty)
- [Input/output](https://en.wikipedia.org/wiki/Input/output)
- [Idempotence](https://en.wikipedia.org/wiki/Idempotence)
- [Idris (programming language)](https://en.wikipedia.org/wiki/Idris_(programming_language))
- [Imperative programming](https://en.wikipedia.org/wiki/Imperative_programming)
- [Input/output](https://en.wikipedia.org/wiki/Input/output)
- [Instruction pipelining](https://en.wikipedia.org/wiki/Instruction_pipelining)
- [Instruction set architecture](https://en.wikipedia.org/wiki/Instruction_set_architecture)
- [Invariant (mathematics)](https://en.wikipedia.org/wiki/Invariant_(mathematics))
- [Isabelle (proof assistant)](https://en.wikipedia.org/wiki/Isabelle_(proof_assistant))
- [Isabelle (proof assistant)](https://en.wikipedia.org/wiki/Isabelle_(proof_assistant))
- [James Cook University](https://en.wikipedia.org/wiki/James_Cook_University)
- [LEGO (proof assistant)](https://en.wikipedia.org/wiki/LEGO_(proof_assistant))
- [Lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus)
- [Lean (proof assistant)](https://en.wikipedia.org/wiki/Lean_(proof_assistant))
- [Linear logic](https://en.wikipedia.org/wiki/Linear_logic)
- [Loop invariant](https://en.wikipedia.org/wiki/Loop_invariant)
- [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
- [Matthias Felleisen](https://en.wikipedia.org/wiki/Matthias_Felleisen)
- [Mizar system](https://en.wikipedia.org/wiki/Mizar_system)
- [Model checking](https://en.wikipedia.org/wiki/Model_checking)
- [Model of computation](https://en.wikipedia.org/wiki/Model_of_computation)
- [Monad (functional programming)](https://en.wikipedia.org/wiki/Monad_(functional_programming))
- [Non-local variable](https://en.wikipedia.org/wiki/Non-local_variable)
- [Nuprl](https://en.wikipedia.org/wiki/Nuprl)
- [Operational semantics](https://en.wikipedia.org/wiki/Operational_semantics)
- [Operator associativity](https://en.wikipedia.org/wiki/Operator_associativity)
- [Out-of-order execution](https://en.wikipedia.org/wiki/Out-of-order_execution)
- [Path explosion](https://en.wikipedia.org/wiki/Path_explosion)
- [Petri net](https://en.wikipedia.org/wiki/Petri_net)
- [Pointer analysis](https://en.wikipedia.org/wiki/Pointer_analysis)
- [Polyvariance](https://en.wikipedia.org/wiki/Polyvariance)
- [Process calculus](https://en.wikipedia.org/wiki/Process_calculus)
- [Processor register](https://en.wikipedia.org/wiki/Processor_register)
- [Program analysis](https://en.wikipedia.org/wiki/Program_analysis)
- [Refinement (computing)](https://en.wikipedia.org/wiki/Refinement_(computing))
- [Program slicing](https://en.wikipedia.org/wiki/Program_slicing)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Proof assistant](https://en.wikipedia.org/wiki/Proof_assistant)
- [Prototype Verification System](https://en.wikipedia.org/wiki/Prototype_Verification_System)
- [Pure function](https://en.wikipedia.org/wiki/Pure_function)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Referential transparency](https://en.wikipedia.org/wiki/Referential_transparency)
- [Rice's theorem](https://en.wikipedia.org/wiki/Rice%27s_theorem)
- [Runtime verification](https://en.wikipedia.org/wiki/Runtime_verification)
- [SAT solver](https://en.wikipedia.org/wiki/SAT_solver)
- [Satisfiability modulo theories](https://en.wikipedia.org/wiki/Satisfiability_modulo_theories)
- [Safety and liveness properties](https://en.wikipedia.org/wiki/Safety_and_liveness_properties)
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scheme (programming language)](https://en.wikipedia.org/wiki/Scheme_(programming_language))
- [Semantics (computer science)](https://en.wikipedia.org/wiki/Semantics_(computer_science))
- [Separation logic](https://en.wikipedia.org/wiki/Separation_logic)
- [Sequence point](https://en.wikipedia.org/wiki/Sequence_point)
- [Shape analysis (program analysis)](https://en.wikipedia.org/wiki/Shape_analysis_(program_analysis))
- [Shriram Krishnamurthi](https://en.wikipedia.org/wiki/Shriram_Krishnamurthi)
- [Side-channel attack](https://en.wikipedia.org/wiki/Side-channel_attack)
- [Operational semantics](https://en.wikipedia.org/wiki/Operational_semantics)
- [Software testing](https://en.wikipedia.org/wiki/Software_testing)
- [Soundness](https://en.wikipedia.org/wiki/Soundness)
- [Specification language](https://en.wikipedia.org/wiki/Specification_language)
- [Standard ML](https://en.wikipedia.org/wiki/Standard_ML)
- [Finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine)
- [Local variable](https://en.wikipedia.org/wiki/Local_variable)
- [Static program analysis](https://en.wikipedia.org/wiki/Static_program_analysis)
- [Status register](https://en.wikipedia.org/wiki/Status_register)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Symbolic execution](https://en.wikipedia.org/wiki/Symbolic_execution)
- [TLA+](https://en.wikipedia.org/wiki/TLA%2B)
- [Temporal logic](https://en.wikipedia.org/wiki/Temporal_logic)
- [Termination analysis](https://en.wikipedia.org/wiki/Termination_analysis)
- [Turing machine](https://en.wikipedia.org/wiki/Turing_machine)
- [Twelf](https://en.wikipedia.org/wiki/Twelf)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Typestate analysis](https://en.wikipedia.org/wiki/Typestate_analysis)
- [Undefined behavior](https://en.wikipedia.org/wiki/Undefined_behavior)
- [Undefined behavior](https://en.wikipedia.org/wiki/Undefined_behavior)
- [University of Arizona](https://en.wikipedia.org/wiki/University_of_Arizona)
- [Unspecified behavior](https://en.wikipedia.org/wiki/Unspecified_behavior)
- [Value (computer science)](https://en.wikipedia.org/wiki/Value_(computer_science))
- [Template:Program analysis](https://en.wikipedia.org/wiki/Template:Program_analysis)
- [Category:Program analysis](https://en.wikipedia.org/wiki/Category:Program_analysis)
- [Category:Use dmy dates from December 2021](https://en.wikipedia.org/wiki/Category:Use_dmy_dates_from_December_2021)
- [Category:Use list-defined references from August 2022](https://en.wikipedia.org/wiki/Category:Use_list-defined_references_from_August_2022)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:48:04.263091+00:00_