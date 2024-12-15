# Evaluation strategy

## Metadata
- **Last Updated:** 2024-12-03 06:59:39 UTC
- **Original Article:** [Evaluation strategy](https://en.wikipedia.org/wiki/Evaluation_strategy)
- **Language:** en
- **Page ID:** 2977119

## Summary
In a programming language, an evaluation strategy is a set of rules for evaluating expressions. The term is often used to refer to the more specific notion of a parameter-passing strategy that defines the kind of value that is passed to the function for each parameter (the binding strategy) and whether to evaluate the parameters of a function call, and if so in what order (the evaluation order). The notion of reduction strategy is distinct, although some authors conflate the two terms and the definition of each term is not widely agreed upon.
To illustrate, executing a function call f(a,b) may first evaluate the arguments a and b, store the results in references or memory locations ref_a and ref_b, then evaluate the function's body with those references passed in. This gives the function the ability to look up the original argument values passed in through dereferencing the parameters (some languages use specific operators to perform this), to modify them via assignment as if they were local variables, and to return values via the references. This is the call-by-reference evaluation strategy.
Evaluation strategy is part of the semantics of the programming language definition. Some languages, such as PureScript, have variants with different evaluation strategies. Some declarative languages, such as Datalog, support multiple evaluation strategies. Some languages define a calling convention.

## Categories
This article belongs to the following categories:

- Category:All articles lacking in-text citations
- Category:Articles lacking in-text citations from April 2012
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:CS1 errors: periodical ignored
- Category:Evaluation strategy
- Category:Short description is different from Wikidata
- Category:Wikipedia articles needing clarification from June 2023

## Table of Contents

- Table
- Evaluation orders
- Strict binding strategies
- Non-strict binding strategies
- See also
- References
- Further reading
- External links

## Content

In a programming language, an evaluation strategy is a set of rules for evaluating expressions. The term is often used to refer to the more specific notion of a parameter-passing strategy that defines the kind of value that is passed to the function for each parameter (the binding strategy) and whether to evaluate the parameters of a function call, and if so in what order (the evaluation order). The notion of reduction strategy is distinct, although some authors conflate the two terms and the definition of each term is not widely agreed upon.
To illustrate, executing a function call f(a,b) may first evaluate the arguments a and b, store the results in references or memory locations ref_a and ref_b, then evaluate the function's body with those references passed in. This gives the function the ability to look up the original argument values passed in through dereferencing the parameters (some languages use specific operators to perform this), to modify them via assignment as if they were local variables, and to return values via the references. This is the call-by-reference evaluation strategy.
Evaluation strategy is part of the semantics of the programming language definition. Some languages, such as PureScript, have variants with different evaluation strategies. Some declarative languages, such as Datalog, support multiple evaluation strategies. Some languages define a calling convention.

Table
This is a table of evaluation strategies and representative languages by year introduced. The representative languages are listed in chronological order, starting with the language(s) that introduced the strategy and followed by prominent languages that use the strategy.: 434

Evaluation orders
While the order of operations defines the abstract syntax tree of the expression, the evaluation order defines the order in which expressions are evaluated. For example, the Python program

outputs 123 due to Python's left-to-right evaluation order, but a similar program in OCaml:

outputs 213 due to OCaml's right-to-left evaluation order.
The evaluation order is mainly visible in code with side effects, but it also affects the performance of the code because a rigid order inhibits instruction scheduling. For this reason language standards such as C++ traditionally left the order unspecified, although languages such as Java and C# define the evaluation order as left-to-right: 240–241  and the C++17 standard has added constraints on the evaluation order.

Strict evaluation
Applicative order is a family of evaluation orders in which a function's arguments are evaluated completely before the function is applied.
 This has the effect of making the function strict, i.e. the function's result is undefined if any of the arguments are undefined, so applicative order evaluation is more commonly called strict evaluation. Furthermore, a function call is performed as soon as it is encountered in a procedure, so it is also called eager evaluation or greedy evaluation. Some authors refer to strict evaluation as "call by value" due to the call-by-value binding strategy requiring strict evaluation.
Common Lisp, Eiffel and Java evaluate function arguments left-to-right. C leaves the order undefined. Scheme requires the execution order to be the sequential execution of an unspecified permutation of the arguments. OCaml similarly leaves the order unspecified, but in practice evaluates arguments right-to-left due to the design of its abstract machine. All of these are strict evaluation.

Non-strict evaluation
A non-strict evaluation order is an evaluation order that is not strict, that is, a function may return a result before all of its arguments are fully evaluated.: 46–47  The prototypical example is normal order evaluation, which does not evaluate any of the arguments until they are needed in the body of the function. Normal order evaluation has the property that it terminates without error whenever any other evaluation order would have terminated without error. The name "normal order" comes from the lambda calculus, where normal order reduction will find a normal form if there is one (it is a "normalizing" reduction strategy). Lazy evaluation is classified in this article as a binding technique rather than an evaluation order. But this distinction is not always followed and some authors define lazy evaluation as normal order evaluation or vice-versa, or confuse non-strictness with lazy evaluation.: 43–44 
Boolean expressions in many languages use a form of non-strict evaluation called short-circuit evaluation, where evaluation evaluates the left expression but may skip the right expression if the result can be determined—for example, in a disjunctive expression (OR) where true is encountered, or in a conjunctive expression (AND) where false is encountered, and so forth. Conditional expressions similarly use non-strict evaluation - only one of the branches is evaluated.

Comparison of applicative order and normal order evaluation
With normal order evaluation, expressions containing an expensive computation, an error, or an infinite loop will be ignored if not needed, allowing the specification of user-defined control flow constructs, a facility not available with applicative order evaluation. Normal order evaluation uses complex structures such as thunks for unevaluated expressions, compared to the call stack used in applicative order evaluation. Normal order evaluation has historically had a lack of usable debugging tools due to its complexity.

Strict binding strategies
Call by value
In call by value (or pass by value), the evaluated value of the argument expression is bound to the corresponding variable in the function (frequently by copying the value into a new memory region). If the function or procedure is able to assign values to its parameters, only its local variable is assigned—that is, anything passed into a function call is unchanged in the caller's scope when the function returns. For example, in Pascal, passing an array by value will cause the entire array to be copied, and any mutations to this array will be invisible to the caller:

Semantic drift
Strictly speaking, under call by value, no operations performed by the called routine can be visible to the caller, other than as part of the return value. This implies a form of purely functional programming in the implementation semantics. However, the circumlocution "call by value where the value is a reference" has become common in some languages, for example, the Java community. Compared to traditional pass by value, the value which is passed is not a value as understood by the ordinary meaning of value, such as an integer that can be written as a literal, but an implementation-internal reference handle. Mutations to this reference handle are visible in the caller. Due to the visible mutation, this form of "call by value" is more properly referred to as call by sharing.
In purely functional languages, values and data structures are immutable, so there is no possibility for a function to modify any of its arguments. As such, there is typically no semantic difference between passing by value and passing by reference or a pointer to the data structure, and implementations frequently use call by reference internally for the efficiency benefits. Nonetheless, these languages are typically described as call by value languages.

Call by reference
Call by reference (or pass by reference) is an evaluation strategy where a parameter is bound to an implicit reference to the variable used as argument, rather than a copy of its value. This typically means that the function can modify (i.e., assign to) the variable used as argument—something that will be seen by its caller. Call by reference can therefore be used to provide an additional channel of communication between the called function and the calling function. Pass by reference can significantly improve performance: calling a function with a many-megabyte structure as an argument does not have to copy the large structure, only the reference to the structure (which is generally a machine word and only a few bytes). However, a call-by-reference language makes it more difficult for a programmer to track the effects of a function call, and may introduce subtle bugs.
Due to variation in syntax, the difference between call by reference (where the reference type is implicit) and call by sharing (where the reference type is explicit) is often unclear on first glance. A simple litmus test is if it's possible to write a traditional swap(a, b) function in the language. For example in Fortran:

Therefore, Fortran's inout intent implements call-by-reference; any variable can be implicitly converted to a reference handle. In contrast the closest one can get in Java is:

where an explicit Box type must be used to introduce a handle. Java is call-by-sharing but not call-by-reference.

Call by copy-restore
Call by copy-restore—also known as "copy-in copy-out", "call by value result", "call by value return" (as termed in the Fortran community)—is a variation of call by reference. With call by copy-restore, the contents of the argument are copied to a new variable local to the call invocation. The function may then modify this variable, similarly to call by reference, but as the variable is local, the modifications are not visible outside of the call invocation during the call. When the function call returns, the updated contents of this variable are copied back to overwrite the original argument ("restored").
The semantics of call by copy-restore is similar in many cases to call by reference, but differs when two or more function arguments alias one another (i.e., point to the same variable in the caller's environment). Under call by reference, writing to one argument will affect the other during the function's execution. Under call by copy-restore, writing to one argument will not affect the other during the function's execution, but at the end of the call, the values of the two arguments may differ, and it is unclear which argument is copied back first and therefore what value the caller's variable receives. For example, Ada specifies that the copy-out assignment for each in out or out parameter occurs in an arbitrary order. From the following program (illegal in Ada 2012) it can be seen that the behavior of GNAT is to copy in left-to-right order on return:

If the program returned 1 it would be copying right-to-left, and under call by reference semantics the program would return 3.
When the reference is passed to the caller uninitialized (for example an out parameter in Ada as opposed to an in out parameter), this evaluation strategy may be called "call by result".
This strategy has gained attention in multiprocessing and remote procedure calls, as unlike call-by-reference it does not require frequent communication between threads of execution for variable access.

Call by sharing
Call by sharing (also known as "pass by sharing", "call by object", or "call by object-sharing") is an evaluation strategy that is intermediate between call by value and call by reference. Rather than every variable being exposed as a reference, only a specific class of values, termed "references", "boxed types", or "objects", have reference semantics, and it is the addresses of these pointers that are passed into the function. Like call by value, the value of the address passed is a copy, and direct assignment to the parameter of the function overwrites the copy and is not visible to the calling function. Like call by reference, mutating the target of the pointer is visible to the calling function. Mutations of a mutable object within the function are visible to the caller because the object is not copied or cloned—it is shared, hence the name "call by sharing".
The technique was first noted by Barbara Liskov in 1974 for the CLU language. It is used by many modern languages such as Python (the shared values being called "objects"), Java (objects), Ruby (objects), JavaScript (objects), Scheme (data structures such as vectors), AppleScript (lists, records, dates, and script objects), OCaml and ML (references, records, arrays, objects, and other compound data types), Maple (rtables and tables), and Tcl (objects). The term "call by sharing" as used in this article is not in common use; the terminology is inconsistent across different sources. For example, in the Java community, they say that Java is call by value.
For immutable objects, there is no real difference between call by sharing and call by value, except if object identity is visible in the language. The use of call by sharing with mutable objects is an alternative to input/output parameters: the parameter is not assigned to (the argument is not overwritten and object identity is not changed), but the object (argument) is mutated.
For example, in Python, lists are mutable and passed with call by sharing, so:

outputs [1] because the append method modifies the object on which it is called.
In contrast, assignments within a function are not noticeable to the caller. For example, this code binds the formal argument to a new object, but it is not visible to the caller because it does not mutate a_list:

Call by address
Call by address, pass by address, or call/pass by pointer is a parameter passing method where the address of the argument is passed as the formal parameter. Inside the function, the address (pointer) may be used to access or modify the value of the argument. For example, the swap operation can be implemented as follows in C:

Some authors treat & as part of the syntax of calling swap. Under this view, C supports the call-by-reference parameter passing strategy. Other authors take a differing view that the presented implementation of swap in C is only a simulation of call-by-reference using pointers. Under this "simulation" view, mutable variables in C are not first-class (that is, l-values are not expressions), rather pointer types are. In this view, the presented swap program is syntactic sugar for a program that uses pointers throughout, for example this program (read and assign have been added to highlight the similarities to the Java Box call-by-sharing program above):

Because in this program, swap operates on pointers and cannot change the pointers themselves, but only the values the pointers point to, this view holds that C's main evaluation strategy is more similar to call-by-sharing.
C++ confuses the issue further by allowing swap to be declared and used with a very lightweight "reference" syntax:

Semantically, this is equivalent to the C examples. As such, many authors consider call-by-address to be a unique parameter passing strategy distinct from call-by-value, call-by-reference, and call-by-sharing.

Call by unification
In logic programming, the evaluation of an expression may simply correspond to the unification of the terms involved combined with the application of some form of resolution. Unification must be classified as a strict binding strategy because it is fully performed. However, unification can also be performed on unbounded variables, so calls may not necessarily commit to final values for all its variables.

Non-strict binding strategies
Call by name
Call by name is an evaluation strategy where the arguments to a function are not evaluated before the function is called—rather, they are substituted directly into the function body (using capture-avoiding substitution) and then left to be evaluated whenever they appear in the function. If an argument is not used in the function body, the argument is never evaluated; if it is used several times, it is re-evaluated each time it appears. (See Jensen's device for a programming technique that exploits this.)
Call-by-name evaluation is occasionally preferable to call-by-value evaluation. If a function's argument is not used in the function, call by name will save time by not evaluating the argument, whereas call by value will evaluate it regardless. If the argument is a non-terminating computation, the advantage is enormous. However, when the function argument is used, call by name is often slower, requiring a mechanism such as a thunk.
.NET languages can simulate call by name using delegates or Expression<T> parameters. The latter results in an abstract syntax tree being given to the function. Eiffel provides agents, which represent an operation to be evaluated when needed. Seed7 provides call by name with function parameters. Java programs can accomplish similar lazy evaluation using lambda expressions and the java.util.function.Supplier<T> interface.

Call by need
Call by need is a memoized variant of call by name, where, if the function argument is evaluated, that value is stored for subsequent use. If the argument is pure (i.e., free of side effects), this produces the same results as call by name, saving the cost of recomputing the argument.
Haskell is a well-known language that uses call-by-need evaluation. Because evaluation of expressions may happen arbitrarily far into a computation, Haskell supports only side effects (such as mutation) via the use of monads. This eliminates any unexpected behavior from variables whose values change prior to their delayed evaluation.
In R's implementation of call by need, all arguments are passed, meaning that R allows arbitrary side effects.
Lazy evaluation is the most common implementation of call-by-need semantics, but variations like optimistic evaluation exist. .NET languages implement call by need using the type Lazy<T>.
Graph reduction is an efficient implementation of lazy evaluation.

Call by macro expansion
Call by macro expansion is similar to call by name, but uses textual substitution rather than capture-avoiding substitution. Macro substitution may therefore result in variable capture, leading to mistakes and undesired behavior. Hygienic macros avoid this problem by checking for and replacing shadowed variables that are not parameters.

Call by future
"Call by future", also known as "parallel call by name" or "lenient evaluation", is a concurrent evaluation strategy combining non-strict semantics with eager evaluation. The method requires fine-grained dynamic scheduling and synchronization but is suitable for massively parallel machines.
The strategy creates a future (promise) for the function's body and each of its arguments. These futures are computed concurrently with the flow of the rest of the program. When a future A requires the value of another future B that has not yet been computed, future A blocks until future B finishes computing and has a value. If future B has already finished computing the value is returned immediately. Conditionals block until their condition is evaluated, and lambdas do not create futures until they are fully applied.
If implemented with processes or threads, creating a future will spawn one or more new processes or threads (for the promises), accessing the value will synchronize these with the main thread, and terminating the computation of the future corresponds to killing the promises computing its value. If implemented with a coroutine, as in .NET async/await, creating a future calls a coroutine (an async function), which may yield to the caller, and in turn be yielded back to when the value is used, cooperatively multitasking.
The strategy is non-deterministic, as the evaluation can occur at any time between creation of the future (i.e., when the expression is given) and use of the future's value. The strategy is non-strict because the function body may return a value before the arguments are evaluated. However, in most implementations, execution may still get stuck evaluating an unneeded argument. For example, the program

may either have g finish before f, and output 1, or may result in an error due to evaluating 1/0.
Call-by-future is similar to call by need in that values are computed only once. With careful handling of errors and nontermination, in particular terminating futures partway through if it is determined they will not be needed, call-by-future also has the same termination properties as call-by-need evaluation. However, call-by-future may perform unnecessary speculative work compared to call-by-need, such as deeply evaluating a lazy data structure. This can be avoided by using lazy futures that do not start computation until it is certain the value is needed.

Optimistic evaluation
Optimistic evaluation is a call-by-need variant where the function's argument is partly evaluated in a call-by-value style for some amount of time (which may be adjusted at runtime). After that time has passed, evaluation is aborted and the function is applied using call by need. This approach avoids some of call-by-need's runtime expenses while retaining desired termination characteristics.

See also
Beta normal form
Comparison of programming languages
De re and de dicto
eval
Lambda calculus
Call-by-push-value
Partial evaluation

References
Further reading
Baker-Finch, Clem; King, David; Hall, Jon; Trinder, Phil (1999-03-10). "An Operational Semantics for Parallel Call-by-Need" (ps). Research Report. 99 (1). Faculty of Mathematics & Computing, The Open University.
Ennals, Robert; Peyton Jones, Simon (2003). Optimistic Evaluation: A Fast Evaluation Strategy for Non-Strict Programs (PDF). International Conference on Functional Programming. ACM Press.
Ludäscher, Bertram (2001-01-24). "CSE 130 lecture notes". CSE 130: Programming Languages: Principles & Paradigms.
Pierce, Benjamin C. (2002). Types and Programming Languages. MIT Press. ISBN 0-262-16209-1.
Sestoft, Peter (2002). Mogensen, T; Schmidt, D; Sudborough, I. H. (eds.). Demonstrating Lambda Calculus Reduction (PDF). Lecture Notes in Computer Science. Vol. 2566. Springer-Verlag. pp. 420–435. ISBN 3-540-00326-6. {{cite book}}: |work= ignored (help)
"Call by Value and Call by Reference in C Programming". Call by Value and Call by Reference in C Programming explained. Archived from the original on 2013-01-21.

External links
The interactive on-line Geometry of Interaction visualiser, implementing a graph-based machine for several common evaluation strategies.

## Archive Info
- **Archived on:** 2024-12-15 15:18:33 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 22229 bytes
- **Word Count:** 3449 words
