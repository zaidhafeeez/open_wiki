# Default argument

## Article Metadata

- **Last Updated:** 2024-12-15T04:22:25.249189+00:00
- **Original Article:** [Default argument](https://en.wikipedia.org/wiki/Default_argument)
- **Language:** en
- **Page ID:** 330297

## Summary

In computer programming, a default argument is an argument to a function that a programmer is not required to specify.
In most programming languages, functions may take one or more arguments. Usually, each argument must be specified in full (this is the case in the C programming language). Later languages (for example, in C++) allow the programmer to specify default arguments that always have a value, even if one is not specified when calling the function.

## Categories

- Category:All articles needing additional references
- Category:Articles needing additional references from May 2009
- Category:Articles with example C++ code
- Category:Articles with example Python (programming language) code
- Category:C++
- Category:Subroutines
- Category:Use dmy dates from November 2020

## Table of Contents

- Default arguments in C++
- Overloaded methods
- Evaluation
- Extent

## Content

In computer programming, a default argument is an argument to a function that a programmer is not required to specify.
In most programming languages, functions may take one or more arguments. Usually, each argument must be specified in full (this is the case in the C programming language). Later languages (for example, in C++) allow the programmer to specify default arguments that always have a value, even if one is not specified when calling the function.

Default arguments in C++
Consider the following function declaration:

This function takes three arguments, of which the last one has a default of twelve. The programmer may call this function in two ways:

In the first case the value for the argument called c is specified explicitly. In the second case, the argument is omitted, and the default value of 12 will be used instead.
For the function called, there is no means to know if the argument has been specified by the caller or if the default value was used.
The above-mentioned method is especially useful when one wants to set default criteria so that the function can be called with or without parameters.
Consider the following:

The function call:

will by default print "hello world!" to the standard output std::cout (typically the screen). On the other hand, any object of type std::ostream can now be passed to the same function and the function will print to the given stream instead of to the standard output. The example below sets the std::ostream& to std::cerr, and thus prints the output the standard error stream.

Because default arguments' values are "filled in" at the call site rather than in the body of the function being called, virtual functions take their default argument values from the static type of the pointer or reference through which the call is made, rather than from the dynamic type of the object supplying the virtual function's body.

Overloaded methods
Some languages, such as Java, do not have default arguments. However, the same behaviour can be simulated by using method overloading to create overloaded methods of the same name, which take different numbers of arguments; and the versions with fewer arguments simply call the versions with more arguments, with the default arguments as the missing arguments:

However, in addition to several other disadvantages, since the default arguments are not modeled in the type system, the type of a callback (aka higher-order function) can't express that it accepts either of the overloads nor simulate the default arguments with overloaded functions. Whereas, in JavaScript the non-overloaded function definition can substitute the default when the input value is undefined (regardless if it was implicitly undefined via the argument's absence at the call site or an explicitly passed undefined value); which is modeled as an optional argument parameter type ?: in TypeScript. JavaScript's solution is not resolved statically (i.e. not at compile-time, which is why TypeScript models only the optionality and not the default values in the function's type signature) thus incurs additional runtime overhead, although it does provide more flexibility in that callbacks can independently control their defaults instead of centrally dictated by the (callback's type signature in the) type signature of the function which inputs the callback. The TypeScript solution can be simulated in Java with the Optional type except the analogous of an implicit undefined for each absent argument is an explicit Optional.<Integer>absent() at the call site.

Evaluation
For every function call default argument values must be passed to the called function. If a default argument value contains side-effects, it is significant when those side effects are evaluated – once for the entire program (at parse time, compile time, or load time), or once per function call, at call time.
Python is a notable language that evaluates expressions in default arguments once, at the time the function declaration is evaluated. If evaluation per function call is desired, it can be replicated by having the default argument be a sentinel value, such as None, and then having the body of the function evaluate the default value's side effects only if the sentinel value was passed in.
For example:

Extent
Generally a default argument will behave identically to an argument passed by parameter or a local variable declared at the start of the function, and have the same scope and extent (lifetime) as a parameter or other local variable, namely an automatic variable which is deallocated on function termination.
In other cases a default argument may instead be statically allocated. If the variable is mutable, it will then retain its value across function calls, as with a static variable.
This behavior is found in Python for mutable types, such as lists. As with evaluation, in order to ensure the same extent as a local variable, one can use a sentinel value:


== References ==

## Related Articles

### Internal Links

- ["Hello, World!" program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)
- [Automatic variable](https://en.wikipedia.org/wiki/Automatic_variable)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Function overloading](https://en.wikipedia.org/wiki/Function_overloading)
- [Parameter (computer programming)](https://en.wikipedia.org/wiki/Parameter_(computer_programming))
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Scope (computer science)](https://en.wikipedia.org/wiki/Scope_(computer_science))
- [Sentinel value](https://en.wikipedia.org/wiki/Sentinel_value)
- [Standard streams](https://en.wikipedia.org/wiki/Standard_streams)
- [Static variable](https://en.wikipedia.org/wiki/Static_variable)
- [Virtual function](https://en.wikipedia.org/wiki/Virtual_function)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from May 2009](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_May_2009)
- [Category:Use dmy dates from November 2020](https://en.wikipedia.org/wiki/Category:Use_dmy_dates_from_November_2020)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:22:25.249189+00:00_