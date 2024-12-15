# Macroprogramming

## Article Metadata

- **Last Updated:** 2024-12-15T04:33:58.949245+00:00
- **Original Article:** [Macroprogramming](https://en.wikipedia.org/wiki/Macroprogramming)
- **Language:** en
- **Page ID:** 73047769

## Summary

In computer science, macroprogramming is a programming paradigm 
aimed at expressing the macroscopic, global behaviour of an entire system of agents or computing devices.
In macroprogramming, the local programs for the individual components of a distributed system are compiled or interpreted from a macro-program typically expressed by a system-level perspective or in terms of the intended global goal.
The aim of macroprogramming approaches is to support expressing the macroscopic interactive beh

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with example Scala code
- Category:Articles with short description
- Category:Distributed computing
- Category:Programming languages
- Category:Programming paradigms
- Category:Short description with empty Wikidata description

## Table of Contents

- Context and motivation
- Examples
- See also

## Content

In computer science, macroprogramming is a programming paradigm 
aimed at expressing the macroscopic, global behaviour of an entire system of agents or computing devices.
In macroprogramming, the local programs for the individual components of a distributed system are compiled or interpreted from a macro-program typically expressed by a system-level perspective or in terms of the intended global goal.
The aim of macroprogramming approaches is to support expressing the macroscopic interactive behaviour of a whole distributed system of computing devices or agents in a single program, or, similarly, to promote their collective intelligence.
It has not to be confused with macros, the mechanism often found in programming languages (like C or Scala) to express substitution rules for program pieces.
Macroprogramming originated in the context of wireless sensor network programming
and found renewed interest in the context of the Internet of Things and swarm robotics.
Macroprogramming shares similar goals (related to  programming a system by a global perspective) with multitier programming, choreographic programming, and aggregate computing.

Context and motivation
Programming distributed systems, multi-agent systems, and collectives of software agents (e.g., robotic swarms) is difficult, for many issues (like communication, concurrency, and failure) have to be properly considered. In particular, a general recurrent problem is how to induce the intended global behaviour by defining the behaviour of the individual components or agents involved. The problem can be addressed through learning approaches, such as multi-agent reinforcement learning, or by manually defining the control program driving each component. However, addressing the problem by a fully individual (or single-node) perspective may be error-prone, because it is generally difficult to foresee the overall behaviour emerging from complex networks of activities and interactions (cf. complex systems and emergence). Therefore, researchers have started investigated ways to raise the abstraction level, promoting programming of distributed systems by a more global perspective or in terms of the overall goal to be collectively attained.

Examples
ScaFi
The following program in the ScaFi aggregate programming language  [1] defines the loop control logic needed to compute a channel (a Boolean field where the devices yielding true are those connecting, through a hop-by-hop path, a source device to a target device)  across a large set of situated devices interacting with neighbours.

What is interesting to note is that the channel function, as well as the functions that are used to implement it, namely distanceTo, distanceBetween, dilate, broadcast etc.
can be interpreted not just in terms of the individual behaviour of a device, but rather by a macroscopic perspective.
In fact, for instance, distanceTo(s) is used to compute the field of minimum distances from the closest device for which expression s yields true: this is effectively a distributed data structure that is sustained through processing and communication with neighbours, in a self-organising way.
Semantically, such functions define  a macro-level (or collective) behaviour that yields a macro-level (or collective) data structure. Such macro-level functions/behaviours can be composed together to obtain another more complex macro-level function/behaviours.

Regiment
The following program in the Regiment language  can be used to compute the mean temperature perceived by the whole system:

PyoT
The following program in PyoT  can be used to turn on a fan if the mean temperature computed by several sensors exceeds a certain threshold.

TinyDB
In TinyDB, a data-oriented macroprogramming approach is used where the programmer writes a query which turns into single-node operations and routing in a wireless sensor network.

See also
Multitier programming
Choreographic programming
Aggregate computing
Distributed computing


== References ==

## Related Articles

### Internal Links

- [Abductive logic programming](https://en.wikipedia.org/wiki/Abductive_logic_programming)
- [Action language](https://en.wikipedia.org/wiki/Action_language)
- [Actor model](https://en.wikipedia.org/wiki/Actor_model)
- [Agent-oriented programming](https://en.wikipedia.org/wiki/Agent-oriented_programming)
- [Algebraic modeling language](https://en.wikipedia.org/wiki/Algebraic_modeling_language)
- [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- [Answer set programming](https://en.wikipedia.org/wiki/Answer_set_programming)
- [Applicative programming language](https://en.wikipedia.org/wiki/Applicative_programming_language)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Array programming](https://en.wikipedia.org/wiki/Array_programming)
- [Aspect-oriented programming](https://en.wikipedia.org/wiki/Aspect-oriented_programming)
- [Attribute-oriented programming](https://en.wikipedia.org/wiki/Attribute-oriented_programming)
- [Automata-based programming](https://en.wikipedia.org/wiki/Automata-based_programming)
- [Automatic mutual exclusion](https://en.wikipedia.org/wiki/Automatic_mutual_exclusion)
- [Automatic programming](https://en.wikipedia.org/wiki/Automatic_programming)
- [Bayesian program synthesis](https://en.wikipedia.org/wiki/Bayesian_program_synthesis)
- [Block (programming)](https://en.wikipedia.org/wiki/Block_(programming))
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Choreographic programming](https://en.wikipedia.org/wiki/Choreographic_programming)
- [Class-based programming](https://en.wikipedia.org/wiki/Class-based_programming)
- [Collective intelligence](https://en.wikipedia.org/wiki/Collective_intelligence)
- [Collective](https://en.wikipedia.org/wiki/Collective)
- [Command language](https://en.wikipedia.org/wiki/Command_language)
- [Comparison of functional programming languages](https://en.wikipedia.org/wiki/Comparison_of_functional_programming_languages)
- [Comparison of multi-paradigm programming languages](https://en.wikipedia.org/wiki/Comparison_of_multi-paradigm_programming_languages)
- [Comparison of programming languages (object-oriented programming)](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(object-oriented_programming))
- [Complex system](https://en.wikipedia.org/wiki/Complex_system)
- [Component-based software engineering](https://en.wikipedia.org/wiki/Component-based_software_engineering)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Concatenative programming language](https://en.wikipedia.org/wiki/Concatenative_programming_language)
- [Concurrent computing](https://en.wikipedia.org/wiki/Concurrent_computing)
- [Concurrent constraint logic programming](https://en.wikipedia.org/wiki/Concurrent_constraint_logic_programming)
- [Concurrent logic programming](https://en.wikipedia.org/wiki/Concurrent_logic_programming)
- [Concurrent object-oriented programming](https://en.wikipedia.org/wiki/Concurrent_object-oriented_programming)
- [Constraint logic programming](https://en.wikipedia.org/wiki/Constraint_logic_programming)
- [Constraint programming](https://en.wikipedia.org/wiki/Constraint_programming)
- [Data-driven programming](https://en.wikipedia.org/wiki/Data-driven_programming)
- [Data-oriented design](https://en.wikipedia.org/wiki/Data-oriented_design)
- [Dataflow programming](https://en.wikipedia.org/wiki/Dataflow_programming)
- [Declarative programming](https://en.wikipedia.org/wiki/Declarative_programming)
- [Dependent type](https://en.wikipedia.org/wiki/Dependent_type)
- [Design by contract](https://en.wikipedia.org/wiki/Design_by_contract)
- [Differentiable programming](https://en.wikipedia.org/wiki/Differentiable_programming)
- [Distributed computing](https://en.wikipedia.org/wiki/Distributed_computing)
- [Distributed computing](https://en.wikipedia.org/wiki/Distributed_computing)
- [Distributed computing](https://en.wikipedia.org/wiki/Distributed_computing)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Domain-specific language](https://en.wikipedia.org/wiki/Domain-specific_language)
- [Dynamic programming language](https://en.wikipedia.org/wiki/Dynamic_programming_language)
- [Emergence](https://en.wikipedia.org/wiki/Emergence)
- [End-user development](https://en.wikipedia.org/wiki/End-user_development)
- [Event-driven programming](https://en.wikipedia.org/wiki/Event-driven_programming)
- [Expression-oriented programming language](https://en.wikipedia.org/wiki/Expression-oriented_programming_language)
- [Extensible programming](https://en.wikipedia.org/wiki/Extensible_programming)
- [Feature-oriented programming](https://en.wikipedia.org/wiki/Feature-oriented_programming)
- [Filter (software)](https://en.wikipedia.org/wiki/Filter_(software))
- [Flow-based programming](https://en.wikipedia.org/wiki/Flow-based_programming)
- [Function-level programming](https://en.wikipedia.org/wiki/Function-level_programming)
- [Functional logic programming](https://en.wikipedia.org/wiki/Functional_logic_programming)
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [Functional reactive programming](https://en.wikipedia.org/wiki/Functional_reactive_programming)
- [Generalized algebraic data type](https://en.wikipedia.org/wiki/Generalized_algebraic_data_type)
- [Generic programming](https://en.wikipedia.org/wiki/Generic_programming)
- [Grammar-oriented programming](https://en.wikipedia.org/wiki/Grammar-oriented_programming)
- [Graph rewriting](https://en.wikipedia.org/wiki/Graph_rewriting)
- [Handle System](https://en.wikipedia.org/wiki/Handle_System)
- [Higher-order programming](https://en.wikipedia.org/wiki/Higher-order_programming)
- [Homoiconicity](https://en.wikipedia.org/wiki/Homoiconicity)
- [Hygienic macro](https://en.wikipedia.org/wiki/Hygienic_macro)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Immutable object](https://en.wikipedia.org/wiki/Immutable_object)
- [Imperative programming](https://en.wikipedia.org/wiki/Imperative_programming)
- [Inductive logic programming](https://en.wikipedia.org/wiki/Inductive_logic_programming)
- [Inductive programming](https://en.wikipedia.org/wiki/Inductive_programming)
- [Inferential programming](https://en.wikipedia.org/wiki/Inferential_programming)
- [Intentional programming](https://en.wikipedia.org/wiki/Intentional_programming)
- [Interactive programming](https://en.wikipedia.org/wiki/Interactive_programming)
- [Interface description language](https://en.wikipedia.org/wiki/Interface_description_language)
- [Internet of things](https://en.wikipedia.org/wiki/Internet_of_things)
- [Invariant-based programming](https://en.wikipedia.org/wiki/Invariant-based_programming)
- [Jackson structured programming](https://en.wikipedia.org/wiki/Jackson_structured_programming)
- [Language-oriented programming](https://en.wikipedia.org/wiki/Language-oriented_programming)
- [List comprehension](https://en.wikipedia.org/wiki/List_comprehension)
- [List of object-oriented programming languages](https://en.wikipedia.org/wiki/List_of_object-oriented_programming_languages)
- [Literate programming](https://en.wikipedia.org/wiki/Literate_programming)
- [Logic programming](https://en.wikipedia.org/wiki/Logic_programming)
- [Low-code development platform](https://en.wikipedia.org/wiki/Low-code_development_platform)
- [Macro (computer science)](https://en.wikipedia.org/wiki/Macro_(computer_science))
- [Macro (computer science)](https://en.wikipedia.org/wiki/Macro_(computer_science))
- [Metalinguistic abstraction](https://en.wikipedia.org/wiki/Metalinguistic_abstraction)
- [Metaprogramming](https://en.wikipedia.org/wiki/Metaprogramming)
- [Modeling language](https://en.wikipedia.org/wiki/Modeling_language)
- [Modular programming](https://en.wikipedia.org/wiki/Modular_programming)
- [Multi-agent reinforcement learning](https://en.wikipedia.org/wiki/Multi-agent_reinforcement_learning)
- [Multi-agent system](https://en.wikipedia.org/wiki/Multi-agent_system)
- [Multi-stage programming](https://en.wikipedia.org/wiki/Multi-stage_programming)
- [Multitier programming](https://en.wikipedia.org/wiki/Multitier_programming)
- [Natural-language programming](https://en.wikipedia.org/wiki/Natural-language_programming)
- [Nested function](https://en.wikipedia.org/wiki/Nested_function)
- [Non-English-based programming languages](https://en.wikipedia.org/wiki/Non-English-based_programming_languages)
- [Non-structured programming](https://en.wikipedia.org/wiki/Non-structured_programming)
- [Nondeterministic programming](https://en.wikipedia.org/wiki/Nondeterministic_programming)
- [Object-based language](https://en.wikipedia.org/wiki/Object-based_language)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Ontology language](https://en.wikipedia.org/wiki/Ontology_language)
- [Organic computing](https://en.wikipedia.org/wiki/Organic_computing)
- [Page description language](https://en.wikipedia.org/wiki/Page_description_language)
- [Parallel computing](https://en.wikipedia.org/wiki/Parallel_computing)
- [Parallel programming model](https://en.wikipedia.org/wiki/Parallel_programming_model)
- [Partial application](https://en.wikipedia.org/wiki/Partial_application)
- [Partitioned global address space](https://en.wikipedia.org/wiki/Partitioned_global_address_space)
- [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching)
- [Persistent programming language](https://en.wikipedia.org/wiki/Persistent_programming_language)
- [Pipeline (software)](https://en.wikipedia.org/wiki/Pipeline_(software))
- [Probabilistic logic programming](https://en.wikipedia.org/wiki/Probabilistic_logic_programming)
- [Probabilistic programming](https://en.wikipedia.org/wiki/Probabilistic_programming)
- [Procedural programming](https://en.wikipedia.org/wiki/Procedural_programming)
- [Process-oriented programming](https://en.wikipedia.org/wiki/Process-oriented_programming)
- [Production system (computer science)](https://en.wikipedia.org/wiki/Production_system_(computer_science))
- [Program synthesis](https://en.wikipedia.org/wiki/Program_synthesis)
- [Programming by demonstration](https://en.wikipedia.org/wiki/Programming_by_demonstration)
- [Programming by example](https://en.wikipedia.org/wiki/Programming_by_example)
- [Programming in the large and programming in the small](https://en.wikipedia.org/wiki/Programming_in_the_large_and_programming_in_the_small)
- [Programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)
- [Prototype-based programming](https://en.wikipedia.org/wiki/Prototype-based_programming)
- [Purely functional programming](https://en.wikipedia.org/wiki/Purely_functional_programming)
- [Quantum programming](https://en.wikipedia.org/wiki/Quantum_programming)
- [Query language](https://en.wikipedia.org/wiki/Query_language)
- [Reactive programming](https://en.wikipedia.org/wiki/Reactive_programming)
- [Recursion (computer science)](https://en.wikipedia.org/wiki/Recursion_(computer_science))
- [Reflective programming](https://en.wikipedia.org/wiki/Reflective_programming)
- [Relativistic programming](https://en.wikipedia.org/wiki/Relativistic_programming)
- [Role-oriented programming](https://en.wikipedia.org/wiki/Role-oriented_programming)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scientific programming language](https://en.wikipedia.org/wiki/Scientific_programming_language)
- [Scripting language](https://en.wikipedia.org/wiki/Scripting_language)
- [Self-modifying code](https://en.wikipedia.org/wiki/Self-modifying_code)
- [Separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)
- [Service-oriented programming](https://en.wikipedia.org/wiki/Service-oriented_programming)
- [Set theoretic programming](https://en.wikipedia.org/wiki/Set_theoretic_programming)
- [SIGNAL (programming language)](https://en.wikipedia.org/wiki/SIGNAL_(programming_language))
- [Simulation language](https://en.wikipedia.org/wiki/Simulation_language)
- [Software agent](https://en.wikipedia.org/wiki/Software_agent)
- [Spacecraft command language](https://en.wikipedia.org/wiki/Spacecraft_command_language)
- [Stack-oriented programming](https://en.wikipedia.org/wiki/Stack-oriented_programming)
- [Stream processing](https://en.wikipedia.org/wiki/Stream_processing)
- [Strict programming language](https://en.wikipedia.org/wiki/Strict_programming_language)
- [Structured concurrency](https://en.wikipedia.org/wiki/Structured_concurrency)
- [Structured programming](https://en.wikipedia.org/wiki/Structured_programming)
- [Subject-oriented programming](https://en.wikipedia.org/wiki/Subject-oriented_programming)
- [Swarm robotics](https://en.wikipedia.org/wiki/Swarm_robotics)
- [Symbolic programming](https://en.wikipedia.org/wiki/Symbolic_programming)
- [Synchronous programming language](https://en.wikipedia.org/wiki/Synchronous_programming_language)
- [System programming language](https://en.wikipedia.org/wiki/System_programming_language)
- [Tacit programming](https://en.wikipedia.org/wiki/Tacit_programming)
- [Tactile programming language](https://en.wikipedia.org/wiki/Tactile_programming_language)
- [Template metaprogramming](https://en.wikipedia.org/wiki/Template_metaprogramming)
- [Template processor](https://en.wikipedia.org/wiki/Template_processor)
- [Total functional programming](https://en.wikipedia.org/wiki/Total_functional_programming)
- [Transformation language](https://en.wikipedia.org/wiki/Transformation_language)
- [Uniform Function Call Syntax](https://en.wikipedia.org/wiki/Uniform_Function_Call_Syntax)
- [Value-level programming](https://en.wikipedia.org/wiki/Value-level_programming)
- [Visual programming language](https://en.wikipedia.org/wiki/Visual_programming_language)
- [Wireless sensor network](https://en.wikipedia.org/wiki/Wireless_sensor_network)
- [Template:Programming paradigms navbox](https://en.wikipedia.org/wiki/Template:Programming_paradigms_navbox)
- [Template talk:Programming paradigms navbox](https://en.wikipedia.org/wiki/Template_talk:Programming_paradigms_navbox)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:33:58.949245+00:00_