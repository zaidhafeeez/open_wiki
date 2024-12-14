# Closure (computer programming)

_Last updated: 2024-12-14T15:40:15.553691_

**Original Article:** [Closure (computer programming)](https://en.wikipedia.org/wiki/Closure_(computer_programming))

**Summary:** In programming languages, a closure, also lexical closure or function closure, is a technique for implementing lexically scoped name binding in a language with first-class functions. Operationally, a closure is a record storing a function together with an environment. The environment is a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created. 

## Categories
- Category:All articles with unsourced statements
- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example D code
- Category:Articles with example Eiffel code
- Category:Articles with example Haskell code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example Objective-C code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Ruby code
- Category:Articles with example Scheme (programming language) code
- Category:Articles with example Smalltalk code
- Category:Articles with short description
- Category:Articles with unsourced statements from December 2014
- Category:Articles with unsourced statements from September 2011
- Category:Implementation of functional programming languages
- Category:Programming language concepts
- Category:Short description matches Wikidata
- Category:Subroutines
- Category:Use dmy dates from August 2020

## Content

In programming languages, a closure, also lexical closure or function closure, is a technique for implementing lexically scoped name binding in a language with first-class functions. Operationally, a closure is a record storing a function together with an environment. The environment is a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created. Unlike a plain function, a closure allows the function to access those captured variables through the closure's copies of their values or references, even when the function is invoked outside their scope.

History and etymology
The concept of closures was developed in the 1960s for the mechanical evaluation of expressions in the λ-calculus and was first fully implemented in 1970 as a language feature in the PAL programming language to support lexically scoped first-class functions.
Peter Landin defined the term closure in 1964 as having an environment part and a control part as used by his SECD machine for evaluating expressions. Joel Moses credits Landin with introducing the term closure to refer to a lambda expression with open bindings (free variables) that have been closed by (or bound in) the lexical environment, resulting in a closed expression, or closure. This use was subsequently adopted by Sussman and Steele when they defined Scheme in 1975, a lexically scoped variant of Lisp, and became widespread.
Sussman and Abelson also use the term closure in the 1980s with a second, unrelated meaning: the property of an operator that adds data to a data structure to also be able to add nested data structures. This use of the term comes from mathematics use, rather than the prior use in computer science. The authors consider this overlap in terminology to be "unfortunate."

Anonymous functions
The term closure is often used as a synonym for anonymous function, though strictly, an anonymous function is a function literal without a name, while a closure is an instance of a function, a value, whose non-local variables have been bound either to values or to storage locations (depending on the language; see the lexical environment section below).
For example, in the following Python code:

the values of a and b are closures, in both cases produced by returning a nested function with a free variable from the enclosing function, so that the free variable binds to the value of parameter x of the enclosing function. The closures in a and b are functionally identical. The only difference in implementation is that in the first case we used a nested function with a name, g, while in the second case we used an anonymous nested function (using the Python keyword lambda for creating an anonymous function). The original name, if any, used in defining them is irrelevant.
A closure is a value like any other value. It does not need to be assigned to a variable and can instead be used directly, as shown in the last two lines of the example. This usage may be deemed an "anonymous closure".
The nested function definitions are not themselves closures: they have a free variable which is not yet bound. Only once the enclosing function is evaluated with a value for the parameter is the free variable of the nested function bound, creating a closure, which is then returned from the enclosing function.
Lastly, a closure is only distinct from a function with free variables when outside of the scope of the non-local variables, otherwise the defining environment and the execution environment coincide and there is nothing to distinguish these (static and dynamic binding cannot be distinguished because the names resolve to the same values). For example, in the program below, functions with a free variable x (bound to the non-local variable x with global scope) are executed in the same environment where x is defined, so it is immaterial whether these are actually closures:

This is most often achieved by a function return, since the function must be defined within the scope of the non-local variables, in which case typically its own scope will be smaller.
This can also be achieved by variable shadowing (which reduces the scope of the non-local variable), though this is less common in practice, as it is less useful and shadowing is discouraged. In this example f can be seen to be a closure because x in the body of f is bound to the x in the global namespace, not the x local to g:

Applications
The use of closures is associated with languages where functions are first-class objects, in which functions can be returned as results from higher-order functions, or passed as arguments to other function calls; if functions with free variables are first-class, then returning one creates a closure. This includes functional programming languages such as Lisp and ML, and many modern, multi-paradigm languages, such as Julia, Python, and Rust. Closures are also often used with callbacks, particularly for event handlers, such as in JavaScript, where they are used for interactions with a dynamic web page.
Closures can also be used in a continuation-passing style to hide state. Constructs such as objects and control structures can thus be implemented with closures. In some languages, a closure may occur when a function is defined within another function, and the inner function refers to local variables of the outer function. At run-time, when the outer function executes, a closure is formed, consisting of the inner function's code and references (the upvalues) to any variables of the outer function required by the closure.

First-class functions
Closures typically appear in languages with first-class functions—in other words, such languages enable functions to be passed as arguments, returned from function calls, bound to variable names, etc., just like simpler types such as strings and integers. For example, consider the following Scheme function:

In this example, the lambda expression (lambda (book) (>= (book-sales book) threshold)) appears within the function best-selling-books.  When the lambda expression is evaluated, Scheme creates a closure consisting of the code for the lambda expression and a reference to the threshold variable, which is a free variable inside the lambda expression.
The closure is then passed to the filter function, which calls it repeatedly to determine which books are to be added to the result list and which are to be discarded. Because the closure has a reference to threshold, it can use that variable each time filter calls it. The function filter might be defined in a separate file.
Here is the same example rewritten in JavaScript, another popular language with support for closures:

The arrow operator => is used to define an arrow function expression, and an Array.filter method instead of a global filter function, but otherwise the structure and the effect of the code are the same.
A function may create a closure and return it, as in this example:

Because the closure in this case outlives the execution of the function that creates it, the variables f and dx live on after the function derivative returns, even though execution has left their scope and they are no longer visible. In languages without closures, the lifetime of an automatic local variable coincides with the execution of the stack frame where that variable is declared. In languages with closures, variables must continue to exist as long as any existing closures have references to them. This is most commonly implemented using some form of garbage collection.

State representation
A closure can be used to associate a function with a set of "private" variables, which persist over several invocations of the function. The scope of the variable encompasses only the closed-over function, so it cannot be accessed from other program code. These are analogous to private variables in object-oriented programming, and in fact closures are similar to stateful function objects (or functors) with a single call-operator method.
In stateful languages, closures can thus be used to implement paradigms for state representation and information hiding, since the closure's upvalues (its closed-over variables) are of indefinite extent, so a value established in one invocation remains available in the next.  Closures used in this way no longer have referential transparency, and are thus no longer pure functions; nevertheless, they are commonly used in impure functional languages such as Scheme.

Other uses
Closures have many uses:

Because closures delay evaluation—i.e., they do not "do" anything until they are called—they can be used to define control structures.  For example, all of Smalltalk's standard control structures, including branches (if/then/else) and loops (while and for), are defined using objects whose methods accept closures.  Users can easily define their own control structures also.
In languages which implement assignment, multiple functions can be produced that close over the same environment, enabling them to communicate privately by altering that environment. In Scheme:

Closures can be used to implement object systems.
Note: Some speakers call any data structure that binds a lexical environment a closure, but the term usually refers specifically to functions.

Implementation and theory
Closures are typically implemented with a special data structure that contains a pointer to the function code, plus a representation of the function's lexical environment (i.e., the set of available variables) at the time when the closure was created. The referencing environment binds the non-local names to the corresponding variables in the lexical environment at the time the closure is created, additionally extending their lifetime to at least as long as the lifetime of the closure. When the closure is entered at a later time, possibly with a different lexical environment, the function is executed with its non-local variables referring to the ones captured by the closure, not the current environment.
A language implementation cannot easily support full closures if its run-time memory model allocates all automatic variables on a linear stack. In such languages, a function's automatic local variables are deallocated when the function returns. However, a closure requires that the free variables it references survive the enclosing function's execution. Therefore, those variables must be allocated so that they persist until no longer needed, typically via heap allocation, rather than on the stack, and their lifetime must be managed so they survive until all closures referencing them are no longer in use.
This explains why, typically, languages that natively support closures also use garbage collection. The alternatives are manual memory management of non-local variables (explicitly allocating on the heap and freeing when done), or, if using stack allocation, for the language to accept that certain use cases will lead to undefined behaviour, due to dangling pointers to freed automatic variables, as in lambda expressions in C++11 or nested functions in GNU C. The funarg problem (or "functional argument" problem) describes the difficulty of implementing functions as first class objects in a stack-based programming language such as C or C++. Similarly in D version 1, it is assumed that the programmer knows what to do with delegates and automatic local variables, as their references will be invalid after return from its definition scope (automatic local variables are on the stack) – this still permits many useful functional patterns, but for complex cases needs explicit heap allocation for variables. D version 2 solved this by detecting which variables must be stored on the heap, and performs automatic allocation. Because D uses garbage collection, in both versions, there is no need to track usage of variables as they are passed.
In strict functional languages with immutable data (e.g. Erlang), it is very easy to implement automatic memory management (garbage collection), as there are no possible cycles in variables' references. For example, in Erlang, all arguments and variables are allocated on the heap, but references to them are additionally stored on the stack. After a function returns, references are still valid. Heap cleaning is done by incremental garbage collector.
In ML, local variables are lexically scoped, and hence define a stack-like model, but since they are bound to values and not to objects, an implementation is free to copy these values into the closure's data structure in a way that is invisible to the programmer.
Scheme, which has an ALGOL-like lexical scope system with dynamic variables and garbage collection, lacks a stack programming model and does not suffer from the limitations of stack-based languages. Closures are expressed naturally in Scheme. The lambda form encloses the code, and the free variables of its environment persist within the program as long as they can possibly be accessed, and so they can be used as freely as any other Scheme expression.
Closures are closely related to Actors in the Actor model of concurrent computation where the values in the function's lexical environment are called acquaintances. An important issue for closures in concurrent programming languages is whether the variables in a closure can be updated and, if so, how these updates can be synchronized. Actors provide one solution.
Closures are closely related to function objects; the transformation from the former to the latter is known as defunctionalization or lambda lifting; see also closure conversion.

Differences in semantics
Lexical environment
As different languages do not always have a common definition of the lexical environment, their definitions of closure may vary also. The commonly held minimalist definition of the lexical environment defines it as a set of all bindings of variables in the scope, and that is also what closures in any language have to capture. However the meaning of a variable binding also differs. In imperative languages, variables bind to relative locations in memory that can store values.  Although the relative location of a binding does not change at runtime, the value in the bound location can. In such languages, since closure captures the binding, any operation on the variable, whether done from the closure or not, are performed on the same relative memory location. This is often called capturing the variable "by reference". Here is an example illustrating the concept in ECMAScript, which is one such language:

Function foo and the closures referred to by variables f and g all use the same relative memory location signified by local variable x.
In some instances the above behaviour may be undesirable, and it is necessary to bind a different lexical closure. Again in ECMAScript, this would be done using the Function.bind().

Example 1: Reference to an unbound variable
Example 2: Accidental reference to a bound variable
For this example the expected behaviour would be that each link should emit its id when clicked; but because the variable 'e' is bound to the scope above, and lazy evaluated on click, what actually happens is that each on click event emits the id of the last element in 'elements' bound at the end of the for loop.

Again here variable e would need to be bound by the scope of the block using handle.bind(this) or the let keyword.
On the other hand, many functional languages, such as ML, bind variables directly to values. In this case, since there is no way to change the value of the variable once it is bound, there is no need to share the state between closures—they just use the same values. This is often called capturing the variable "by value". Java's local and anonymous classes also fall into this category—they require captured local variables to be final, which also means there is no need to share state.
Some languages enable choosing between capturing the value of a variable or its location. For example, in C++11, captured variables are either declared with [&], which means captured by reference, or with [=], which means captured by value.
Yet another subset, lazy functional languages such as Haskell, bind variables to results of future computations rather than values. Consider this example in Haskell:

The binding of r captured by the closure defined within function foo is to the computation (x / y)—which in this case results in division by zero. However, since it is the computation that is captured, and not the value, the error only manifests when the closure is invoked, and then attempts to use the captured binding.

Closure leaving
Yet more differences manifest themselves in the behavior of other lexically scoped constructs, such as return, break and continue statements. Such constructs can, in general, be considered in terms of invoking an escape continuation established by an enclosing control statement (in case of break and continue, such interpretation requires looping constructs to be considered in terms of recursive function calls). In some languages, such as ECMAScript, return refers to the continuation established by the closure lexically innermost with respect to the statement—thus, a return within a closure transfers control to the code that called it. However, in Smalltalk, the superficially similar operator ^ invokes the escape continuation established for the method invocation, ignoring the escape continuations of any intervening nested closures. The escape continuation of a particular closure can only be invoked in Smalltalk implicitly by reaching the end of the closure's code. These examples in ECMAScript and Smalltalk highlight the difference:

The above code snippets will behave differently because the Smalltalk ^ operator and the JavaScript return operator are not analogous.  In the ECMAScript example, return x will leave the inner closure to begin a new iteration of the forEach loop, whereas in the Smalltalk example, ^x will abort the loop and return from the method foo.
Common Lisp provides a construct that can express either of the above actions: Lisp (return-from foo x) behaves as Smalltalk ^x, while Lisp (return-from nil x) behaves as JavaScript return x. Hence, Smalltalk makes it possible for a captured escape continuation to outlive the extent in which it can be successfully invoked. Consider:

When the closure returned by the method foo is invoked, it attempts to return a value from the invocation of foo that created the closure. Since that call has already returned and the Smalltalk method invocation model does not follow the spaghetti stack discipline to facilitate multiple returns, this operation results in an error.
Some languages, such as Ruby, enable the programmer to choose the way return is captured. An example in Ruby:

Both Proc.new and lambda in this example are ways to create a closure, but semantics of the closures thus created are different with respect to the return statement.
In Scheme, definition and scope of the return control statement is explicit (and only arbitrarily named 'return' for the sake of the example). The following is a direct translation of the Ruby sample.

Closure-like constructs
Some languages have features which simulate the behavior of closures. In languages such as C++, C#, D, Java, Objective-C, and Visual Basic (.NET) (VB.NET), these features are the result of the language's object-oriented paradigm.

Callbacks (C)
Some C libraries support callbacks. This is sometimes implemented by providing two values when registering the callback with the library: a function pointer and a separate void* pointer to arbitrary data of the user's choice. When the library executes the callback function, it passes along the data pointer. This enables the callback to maintain state and to refer to information captured at the time it was registered with the library. The idiom is similar to closures in functionality, but not in syntax. The void* pointer is not type safe so this C idiom differs from type-safe closures in C#, Haskell or ML.
Callbacks are used extensively in graphical user interface (GUI) widget toolkits to implement event-driven programming by associating general functions of graphical widgets (menus, buttons, check boxes, sliders, spinners, etc.) with application-specific functions implementing the specific desired behavior for the application.

Nested function and function pointer (C)
With a GNU Compiler Collection (GCC) extension, a nested function can be used and a function pointer can emulate closures, provided the function does not exit the containing scope. The next example is invalid because adder is a top-level definition (depending on compiler version, it could produce a correct result if compiled with no optimizing, i.e., at -O0):

But moving adder (and, optionally, the typedef) in main makes it valid:

If executed this now prints 11 as expected.

Local classes and lambda functions (Java)
Java enables classes to be defined inside methods.  These are called local classes.  When such classes are not named, they are known as anonymous classes (or anonymous inner classes).  A local class (either named or anonymous) may refer to names in lexically enclosing classes, or read-only variables (marked as final) in the lexically enclosing method.

The capturing of final variables enables capturing variables by value. Even if the variable to capture is non-final, it can always be copied to a temporary final variable just before the class.
Capturing of variables by reference can be emulated by using a final reference to a mutable container, for example, a one-element array. The local class will not be able to change the value of the container reference, but it will be able to change the contents of the container.
With the advent of Java 8's lambda expressions, the closure causes the above code to be executed as:

Local classes are one of the types of inner class that are declared within the body of a method.  Java also supports inner classes that are declared as non-static members of an enclosing class. They are normally referred to just as "inner classes". These are defined in the body of the enclosing class and have full access to instance variables of the enclosing class. Due to their binding to these instance variables, an inner class may only be instantiated with an explicit binding to an instance of the enclosing class using a special syntax.

Upon execution, this will print the integers from 0 to 9. Beware to not confuse this type of class with the nested class, which is declared in the same way with an accompanied usage of the "static" modifier; those have not the desired effect but are instead just classes with no special binding defined in an enclosing class.
As of Java 8, Java supports functions as first class objects. Lambda expressions of this form are considered of type Function<T,U> with T being the domain and U the image type. The expression can be called with its .apply(T t) method, but not with a standard method call.

Blocks (C, C++, Objective-C 2.0)
Apple introduced blocks, a form of closure, as a nonstandard extension into C, C++, Objective-C 2.0 and in Mac OS X 10.6 "Snow Leopard" and iOS 4.0. Apple made their implementation available for the GCC and clang compilers.
Pointers to block and block literals are marked with ^. Normal local variables are captured by value when the block is created, and are read-only inside the block. Variables to be captured by reference are marked with __block. Blocks that need to persist outside of the scope they are created in may need to be copied.

Delegates (C#, VB.NET, D)
C# anonymous methods and lambda expressions support closure:

Visual Basic .NET, which has many language features similar to those of C#, also supports lambda expressions with closures:

In D, closures are implemented by delegates, a function pointer paired with a context pointer (e.g. a class instance, or a stack frame on the heap in the case of closures).

D version 1, has limited closure support. For example, the above code will not work correctly, because the variable a is on the stack, and after returning from test(), it is no longer valid to use it (most probably calling foo via dg(), will return a 'random' integer). This can be solved by explicitly allocating the variable 'a' on heap, or using structs or class to store all needed closed variables and construct a delegate from a method implementing the same code. Closures can be passed to other functions, as long as they are only used while the referenced values are still valid (for example calling another function with a closure as a callback parameter), and are useful for writing generic data processing code, so this limitation, in practice, is often not an issue.
This limitation was fixed in D version 2 - the variable 'a' will be automatically allocated on the heap because it is used in the inner function, and a delegate of that function can escape the current scope (via assignment to dg or return). Any other local variables (or arguments) that are not referenced by delegates or that are only referenced by delegates that do not escape the current scope, remain on the stack, which is simpler and faster than heap allocation. The same is true for inner's class methods that reference a function's variables.

Function objects (C++)
C++ enables defining function objects by overloading operator(). These objects behave somewhat like functions in a functional programming language. They may be created at runtime and may contain state, but they do not implicitly capture local variables as closures do. As of the 2011 revision, the C++ language also supports closures, which are a type of function object constructed automatically from a special language construct called lambda-expression. A C++ closure may capture its context either by storing copies of the accessed variables as members of the closure object or by reference. In the latter case, if the closure object escapes the scope of a referenced object, invoking its operator() causes undefined behavior since C++ closures do not extend the lifetime of their context.

Inline agents (Eiffel)
Eiffel includes inline agents defining closures. An inline agent is an object representing a routine, defined by giving the code of the routine in-line. For example, in

the argument to subscribe is an agent, representing a procedure with two arguments; the procedure finds the country at the corresponding coordinates and displays it. The whole agent is "subscribed" to the event type click_event for a
certain button, so that whenever an instance of the event type occurs on that button – because a user has clicked the button – the procedure will be executed with the mouse coordinates being passed as arguments for x and y.
The main limitation of Eiffel agents, which distinguishes them from closures in other languages, is that they cannot reference local variables from the enclosing scope. This design decision helps in avoiding ambiguity when talking about a local variable value in a closure - should it be the latest value of the variable or the value captured when the agent is created? Only Current (a reference to current object, analogous to this in Java), its features, and arguments of the agent can be accessed from within the agent body. The values of the outer local variables can be passed by providing additional closed operands to the agent.

C++Builder __closure reserved word
Embarcadero C++Builder provides the reserved word __closure to provide a pointer to a method with a similar syntax to a function pointer.

Standard C allows writing a typedef for a pointer to a function type using the following syntax:In a similar way, a typedef can be declared for a pointer to a method using this syntax:

See also
Notes
References
External links
Original "Lambda Papers": A classic series of papers by Guy L. Steele Jr. and Gerald Jay Sussman discussing, among other things, the versatility of closures in the context of Scheme (where they appear as lambda expressions).
Gafter, Neal (28 January 2007). "A Definition of Closures".
Bracha, Gilad; Gafter, Neal; Gosling, James; von der Ahé, Peter. "Closures for the Java Programming Language (v0.5)".
Closures: An article about closures in dynamically typed imperative languages, by Martin Fowler.
Collection closure methods: An example of a technical domain where using closures is convenient, by Martin Fowler.