# For loop

## Article Metadata

- **Last Updated:** 2024-12-15T04:24:56.121636+00:00
- **Original Article:** [For loop](https://en.wikipedia.org/wiki/For_loop)
- **Language:** en
- **Page ID:** 468924

## Summary

In computer science, a for-loop or for loop is a control flow statement for specifying iteration. Specifically, a for-loop functions by running a section of code repeatedly until a certain condition has been satisfied.
For-loops have two parts: a header and a body. The header defines the iteration and the body is the code executed once per iteration. The header often declares an explicit loop counter or loop variable. This allows the body to know which iteration is being executed. For-loops are 

## Categories

- Category:All articles with unsourced statements
- Category:Articles with example ALGOL 68 code
- Category:Articles with example Ada code
- Category:Articles with example BASIC code
- Category:Articles with example C++ code
- Category:Articles with example C code
- Category:Articles with example Fortran code
- Category:Articles with example Haskell code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example Julia code
- Category:Articles with example MATLAB/Octave code
- Category:Articles with example OCaml code
- Category:Articles with example PHP code
- Category:Articles with example Pascal code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Ruby code
- Category:Articles with example Rust code
- Category:Articles with example Smalltalk code
- Category:Articles with short description
- Category:Articles with unsourced statements from August 2009
- Category:Control flow
- Category:Iteration in programming
- Category:Programming language comparisons
- Category:Short description is different from Wikidata

## Table of Contents

- FOR
- Loop counters
- Additional semantics and constructs
- Equivalence with while-loops
- Timeline of the for-loop syntax in various programming languages
- See also

## Content

In computer science, a for-loop or for loop is a control flow statement for specifying iteration. Specifically, a for-loop functions by running a section of code repeatedly until a certain condition has been satisfied.
For-loops have two parts: a header and a body. The header defines the iteration and the body is the code executed once per iteration. The header often declares an explicit loop counter or loop variable. This allows the body to know which iteration is being executed. For-loops are typically used when the number of iterations is known before entering the loop. For-loops can be thought of as shorthands for while-loops which increment and test a loop variable.
Various keywords are used to indicate the usage of a for loop: descendants of ALGOL use "for", while descendants of Fortran use "do". There are other possibilities, for example COBOL which uses PERFORM VARYING.
The name for-loop comes from the word for. For is used as the reserved word (or keyword) in many programming languages to introduce a for-loop. The term in English dates to ALGOL 58 and was popularized in ALGOL 60. It is the direct translation of the earlier German für and was used in Superplan (1949–1951) by Heinz Rutishauser. Rutishauser was involved in defining ALGOL 58 and ALGOL 60. The loop body is executed "for" the given values of the loop variable. This is more explicit in ALGOL versions of the for statement where a list of possible values and increments can be specified.
In Fortran and PL/I, the keyword DO is used for the same thing and it is named a do-loop; this is different from a do while loop.

FOR
A for-loop statement is available in most imperative programming languages. Even ignoring minor differences in syntax, there are many differences in how these statements work and the level of expressiveness they support. Generally, for-loops fall into one of four categories:

Traditional for-loops
The for-loop of languages like ALGOL, Simula, BASIC, Pascal, Modula, Oberon, Ada, MATLAB, OCaml, F#, and so on, requires a control variable with start- and end-values, which looks something like this:

Depending on the language, an explicit assignment sign may be used in place of the equal sign (and some languages require the word int even in the numerical case). An optional step-value (an increment or decrement ≠ 1) may also be included, although the exact syntaxes used for this differ a bit more between the languages. Some languages require a separate declaration of the control variable, some do not.
Another form was popularized by the C language. It requires 3 parts: the initialization (loop variant), the condition, and the advancement to the next iteration. All these three parts are optional. This type of "semicolon loops" came from B programming language and it was originally invented by Stephen Johnson.
In the initialization part, any variables needed are declared (and usually assigned values). If multiple variables are declared, they should all be the same type. The condition part checks a certain condition and exits the loop if false, even if the loop is never executed. If the condition is true, then the lines of code inside the loop are executed. The advancement to the next iteration part is performed exactly once every time the loop ends. The loop is then repeated if the condition evaluates to true.
Here is an example of the C-style traditional for-loop in Java.

These loops are also sometimes named numeric for-loops when contrasted with foreach loops (see below).

Iterator-based for-loops
This type of for-loop is a generalization of the numeric range type of for-loop, as it allows for the enumeration of sets of items other than number sequences. It is usually characterized by the use of an implicit or explicit iterator, in which the loop variable takes on each of the values in a sequence or other data collection. A representative example in Python is:

Where some_iterable_object is either a data collection that supports implicit iteration (like a list of employee's names), or may be an iterator itself. Some languages have this in addition to another for-loop syntax; notably, PHP has this type of loop under the name for each, as well as a three-expression for-loop (see below) under the name for.

Vectorised for-loops
Some languages offer a for-loop that acts as if processing all iterations in parallel, such as the for all keyword in Fortran 95 which has the interpretation that all right-hand-side expressions are evaluated before any assignments are made, as distinct from the explicit iteration form. For example, in the for statement in the following pseudocode fragment, when calculating the new value for A(i), except for the first (with i = 2) the reference to A(i - 1) will obtain the new value that had been placed there in the previous step. In the for all version, however, each calculation refers only to the original, unaltered A.

for     i := 2 : N - 1 do A(i) := [A(i - 1) + A(i) + A(i + 1)] / 3; next i;
for all i := 2 : N - 1 do A(i) := [A(i - 1) + A(i) + A(i + 1)] / 3;

The difference may be significant.
Some languages (such as PL/I, Fortran 95) also offer array assignment statements, that enable many for-loops to be omitted. Thus pseudocode such as A:= 0; would set all elements of array A to zero, no matter its size or dimensionality. The example loop could be rendered as

But whether that would be rendered in the style of the for-loop or the for-all-loop or something else may not be clearly described in the compiler manual.

Compound for-loops
Introduced with ALGOL 68 and followed by PL/I, this allows the iteration of a loop to be compounded with a test, as in

for i := 1 : N while A(i) > 0 do etc.

That is, a value is assigned to the loop variable i and only if the while expression is true will the loop body be executed. If the result were false the for-loop's execution stops short. Granted that the loop variable's value is defined after the termination of the loop, then the above statement will find the first non-positive element in array A (and if no such, its value will be N + 1), or, with suitable variations, the first non-blank character in a string, and so on.

Loop counters
In computer programming, a  loop counter is a control variable that controls the iterations of a loop (a computer programming language construct). It is so named because most uses of this construct result in the variable taking on a range of integer values in some orderly sequences (for example., starting at 0 and ending at 10 in increments of 1)
Loop counters change with each iteration of a loop, providing a unique value for each iteration. The loop counter is used to decide when the loop should terminate and for the program flow to continue to the next instruction after the loop.
A common identifier naming convention is for the loop counter to use the variable names i, j, and k (and so on if needed), where i would be the most outer loop, j the next inner loop, etc. The reverse order is also used by some programmers. This style is generally agreed to have originated from the early programming of Fortran, where these variable names beginning with these letters were implicitly declared as having an integer type, and so were obvious choices for loop counters that were only temporarily required. The practice dates back further to mathematical notation where indices for sums and multiplications are often i, j, etc. A variant convention is the use of duplicated letters for the index, ii, jj, and  kk, as this allows easier searching and search-replacing than using a single letter.

Example
An example of C code involving nested for loops, where the loop counter variables are i and j:

Loops in C can also be used to print the reverse of a word. As:

Here, if the input is apple, the output will be elppa.

Additional semantics and constructs
Use as infinite loops
This C-style for-loop is commonly the source of an infinite loop since the fundamental steps of iteration are completely in the control of the programmer. When infinite loops are intended, this type of for-loop can be used (with empty expressions), such as:

This style is used instead of infinite while (1) loops to avoid a type conversion warning in some C/C++ compilers. Some programmers prefer the more succinct for (;;) form over the semantically equivalent but more verbose while (true) form.

Early exit and continuation
Some languages may also provide other supporting statements, which when present can alter how the for-loop iteration proceeds. Common among these are the break and continue statements found in C and its derivatives. The break statement causes the innermost loop to be terminated immediately when executed. The continue statement will move at once to the next iteration without further progress through the loop body for the current iteration. A for statement also terminates when a break, goto, or return statement within the statement body is executed.[Wells] Other languages may have similar statements or otherwise provide means to alter the for-loop progress; for example in Fortran 95:

Some languages offer further facilities such as naming the various loop statements so that with multiple nested loops there is no doubt as to which loop is involved. Fortran 95, for example:

Thus, when "trouble" is detected in the inner loop, the CYCLE X1 (not X2) means that the skip will be to the next iteration for I, not J. The compiler will also be checking that each END DO has the appropriate label for its position: this is not just a documentation aid. The programmer must still code the problem correctly, but some possible blunders will be blocked.

Loop variable scope and semantics
Different languages specify different rules for what value the loop variable will hold on termination of its loop, and indeed some hold that it "becomes undefined". This permits a compiler to generate code that leaves any value in the loop variable, or perhaps even leaves it unchanged because the loop value was held in a register and never stored in memory. Actual behavior may even vary according to the compiler's optimization settings, as with the Honeywell Fortran66 compiler.
In some languages (not C or C++) the loop variable is immutable within the scope of the loop body, with any attempt to modify its value being regarded as a semantic error. Such modifications are sometimes a consequence of a programmer error, which can be very difficult to identify once made. However, only overt changes are likely to be detected by the compiler. Situations, where the address of the loop variable is passed as an argument to a subroutine, make it very difficult to check because the routine's behavior is in general unknowable to the compiler. Some examples in the style of Fortran:

A common approach is to calculate the iteration count at the start of a loop (with careful attention to overflow as in for i:= 0: 65535 do ... ; in sixteen-bit integer arithmetic) and with each iteration decrement this count while also adjusting the value of I: double counting results. However, adjustments to the value of I within the loop will not change the number of iterations executed.
Still, another possibility is that the code generated may employ an auxiliary variable as the loop variable, possibly held in a machine register, whose value may or may not be copied to I on each iteration. Again, modifications of I would not affect the control of the loop, but now a disjunction is possible: within the loop, references to the value of I might be to the (possibly altered) current value of I or to the auxiliary variable (held safe from improper modification) and confusing results are guaranteed. For instance, within the loop a reference to element I of an array would likely employ the auxiliary variable (especially if it were held in a machine register), but if I is a parameter to some routine (for instance, a print-statement to reveal its value), it would likely be a reference to the proper variable I instead. It is best to avoid such possibilities.

Adjustment of bounds
Just as the index variable might be modified within a for-loop, so also may its bounds and direction. But to uncertain effect. A compiler may prevent such attempts, they may have no effect, or they might even work properly - though many would declare that to do so would be wrong. Consider a statement such as

for i := first : last : step do
  A(i) := A(i) / A(last);

If the approach to compiling such a loop was to be the evaluation of first, last and step and the calculation of an iteration count via something like (last - first)/step once only at the start, then if those items were simple variables and their values were somehow adjusted during the iterations, this would have no effect on the iteration count even if the element selected for division by A(last) changed.

List of value ranges
PL/I and ALGOL 68, allow loops in which the loop variable is iterated over a list of ranges of values instead of a single range. The following PL/I example will execute the loop with six values of i: 1, 7, 12, 13, 14, 15:

Equivalence with while-loops
A for-loop is generally equivalent to a while-loop:

factorial := 1
 for counter from 2 to 5
     factorial := factorial * counter
counter:= counter - 1
print counter + "! equals " + factorial

Is equivalent to:

factorial := 1
counter := 1
 while counter < 5
    counter := counter + 1
    factorial := factorial * counter
print counter + "! equals " + factorial

As demonstrated by the output of the variables.

Timeline of the for-loop syntax in various programming languages
Given an action that must be repeated, for instance, five times, different languages' for-loops will be written differently. The syntax for a three-expression for-loop is nearly identical in all languages that have it, after accounting for different styles of block termination and so on.

1957: FORTRAN
Fortran's equivalent of the for loop is the DO loop,
using the keyword do instead of for,
The syntax of Fortran's DO loop is:

The following two examples behave equivalently to the three argument for-loop in other languages,
initializing the counter variable to 1, incrementing by 1 each iteration of the loop, and stopping at five (inclusive).

In Fortran 77 (or later), this may also be written as:

The step part may be omitted if the step is one. Example:

Spaces are irrelevant in fixed-form Fortran statements, thus SUM SQ is the same as SUMSQ. In the modern free-form Fortran style, blanks are significant.
In Fortran 90, the GO TO may be avoided by using an EXIT statement.

1958: ALGOL
ALGOL 58 introduced the for statement, using the form as Superplan:

 FOR Identifier = Base (Difference) Limit

For example to print 0 to 10 incremented by 1:

FOR x = 0 (1) 10 BEGIN
PRINT (FL) = x END

1960: COBOL
COBOL was formalized in late 1959 and has had many elaborations. It uses the PERFORM verb which has many options. Originally all loops had to be out-of-line with the iterated code occupying a separate paragraph. Ignoring the need for declaring and initializing variables, the COBOL equivalent of a for-loop would be.

In the 1980s, the addition of in-line loops and structured programming statements such as END-PERFORM resulted in a for-loop with a more familiar structure.

If the PERFORM verb has the optional clause TEST AFTER, the resulting loop is slightly different: the loop body is executed at least once, before any test.

1964: BASIC
In BASIC, a loop is sometimes named a for-next loop.

The end-loop marker specifies the name of the index variable, which must correspond to the name of the index variable at the start of the for-loop. Some languages (PL/I, Fortran 95, and later) allow a statement label at the start of a for-loop that can be matched by the compiler against the same text on the corresponding end-loop statement. Fortran also allows the EXIT and CYCLE statements to name this text; in a nest of loops, this makes clear which loop is intended. However, in these languages, the labels must be unique, so successive loops involving the same index variable cannot use the same text nor can a label be the same as the name of a variable, such as the index variable for the loop.

1964: PL/I
The LEAVE statement may be used to exit the loop. Loops can be labeled, and leave may leave a specific labeled loop in a group of nested loops. Some PL/I dialects include the ITERATE statement to terminate the current loop iteration and begin the next.

1968: ALGOL 68
ALGOL 68 has what was considered the universal loop, the full syntax is:

FOR i FROM 1 BY 2 TO 3 WHILE i≠4 DO ~ OD

Further, the single iteration range could be replaced by a list of such ranges. There are several unusual aspects of the construct

only the do ~ od portion was compulsory, in which case the loop will iterate indefinitely.
thus the clause to 100 do ~ od, will iterate exactly 100 times.
The while syntactic element allowed a programmer to break from a for loop early, as in:
INT sum sq := 0;
FOR i
 WHILE
  print(("So far:", i, new line)); # Interposed for tracing purposes. #
  sum sq ≠ 70↑2                    # This is the test for the WHILE   #
DO
  sum sq +:= i↑2
OD

Subsequent extensions to the standard ALGOL 68 allowed the to syntactic element to be replaced with upto and downto to achieve a small optimization. The same compilers also incorporated:

until
for late loop termination.
foreach
for working on arrays in parallel.

1970: Pascal
Decrementing (counting backwards) is using downto keyword instead of to, as in:

The numeric range for-loop varies somewhat more.

1972: C, C++
The statement is often a block statement; an example of this would be:

The ISO/IEC 9899:1999 publication (commonly known as C99) also allows initial declarations in for loops. All three sections in the for loop are optional, with an empty condition equivalent to true.

1972: Smalltalk
Contrary to other languages, in Smalltalk a for-loop is not a language construct but is defined in the class Number as a method with two parameters, the end value and a closure, using self as start value.

1980: Ada
The exit statement may be used to exit the loop. Loops can be labeled, and exit may leave a specifically labeled loop in a group of nested loops:

1980: Maple
Maple has two forms of for-loop, one for iterating over a range of values, and the other for iterating over the contents of a container. The value range form is as follows:

for i from f by b to t while w do
    # loop body
od;

All parts except do and od are optional. The  for I part, if present, must come first. The remaining parts (from f, by b, to t, while w) can appear in any order.
Iterating over a container is done using this form of loop:

for e in c while w do
    # loop body
od;

The  in c clause specifies the container, which may be a list, set, sum, product, unevaluated function, array, or object implementing an iterator.
A for-loop may be terminated by od, end, or end do.

1982: Maxima CAS
In Maxima CAS, one can use also integer values:

1982: PostScript
The for-loop, written as [initial] [increment] [limit] { ... } for initializes an internal variable, and executes the body as long as the internal variable is not more than the limit (or not less, if the increment is negative) and, at the end of each iteration, increments the internal variable. Before each iteration, the value of the internal variable is pushed onto the stack.

There is also a simple repeat loop.
The repeat-loop, written as X { ... } repeat, repeats the body exactly X times.

1983: Ada 83 and above
1984: MATLAB
After the loop, n would be 5 in this example.
As i is used for the Imaginary unit, its use as a loop variable is discouraged.

1987: Perl
"There's more than one way to do it" is a Perl programming motto.

1988: Mathematica
The construct corresponding to most other languages' for-loop is named Do in Mathematica.

Mathematica also has a For construct that mimics the for-loop of C-like languages.

1989: Bash
An empty loop (i.e., one with no commands between do and done) is a syntax error. If the above loops contained only comments, execution would result in the message "syntax error near unexpected token 'done'".

1990: Haskell
The built-in imperative forM_ maps a monadic expression into a list, as

or get each iteration result as a list in

But, to save the space of the [1..5] list,
a more authentic monadic forLoop_ construction can be defined as

and used as:

1991: Oberon-2, Oberon-07, Component Pascal
In the original Oberon language, the for-loop was omitted in favor of the more general Oberon loop construct. The for-loop was reintroduced in Oberon-2.

1991: Python
Python does not contain the classical for loop, rather a foreach loop is used to iterate over the output of the built-in range() function which returns an iterable sequence of integers.Using range(6) would run the loop from 0 to 5.

1993: AppleScript
It can also iterate through a list of items, similar to what can be done with arrays in other languages:

A exit repeat may also be used to exit a loop at any time. Unlike other languages, AppleScript currently has no command to continue to the next iteration of a loop.

1993: Crystal
So, this code  will print:

For-loops can also loop through a table using  to iterate numerically through arrays and  to iterate randomly through dictionaries.
Generic for-loop making use of closures:

1995: ColdFusion Markup Language (CFML)
Script syntax
Simple index loop:

Using an array:

Using a list of string values:

The above list example is only available in the dialect of CFML used by Lucee and Railo.

Tag syntax
Simple index loop:

Using an array:

Using a "list" of string values:

1995: Java
For the extended for-loop, see Foreach loop § Java.

1995: JavaScript
JavaScript supports C-style "three-expression" loops. The break and continue statements are supported inside loops.

Alternatively, it is possible to iterate over all keys of an array.

1995: PHP
This prints out a triangle of *

1995: Ruby
Ruby has several possible syntaxes, including the above samples.

1996: OCaml
See expression syntax.

1998: ActionScript 3
2008: Small Basic
2008: Nim
Nim has a foreach-type loop and various operations for creating iterators.

2009: Go
2010: Rust
2012: Julia
See also
Do while loop
Foreach
While loop
Primitive recursive function
General recursive function


== References ==

## Related Articles

### Internal Links

- [ALGOL](https://en.wikipedia.org/wiki/ALGOL)
- [ALGOL 58](https://en.wikipedia.org/wiki/ALGOL_58)
- [ALGOL 60](https://en.wikipedia.org/wiki/ALGOL_60)
- [ALGOL 68](https://en.wikipedia.org/wiki/ALGOL_68)
- [ActionScript](https://en.wikipedia.org/wiki/ActionScript)
- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language))
- [AppleScript](https://en.wikipedia.org/wiki/AppleScript)
- [Assignment (computer science)](https://en.wikipedia.org/wiki/Assignment_(computer_science))
- [Automatic vectorization](https://en.wikipedia.org/wiki/Automatic_vectorization)
- [BASIC](https://en.wikipedia.org/wiki/BASIC)
- [B (programming language)](https://en.wikipedia.org/wiki/B_(programming_language))
- [Bash (Unix shell)](https://en.wikipedia.org/wiki/Bash_(Unix_shell))
- [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra)
- [Control flow](https://en.wikipedia.org/wiki/Control_flow)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C99](https://en.wikipedia.org/wiki/C99)
- [COBOL](https://en.wikipedia.org/wiki/COBOL)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C syntax](https://en.wikipedia.org/wiki/C_syntax)
- [Closure (computer programming)](https://en.wikipedia.org/wiki/Closure_(computer_programming))
- [ColdFusion Markup Language](https://en.wikipedia.org/wiki/ColdFusion_Markup_Language)
- [Compiler](https://en.wikipedia.org/wiki/Compiler)
- [Component Pascal](https://en.wikipedia.org/wiki/Component_Pascal)
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Control flow](https://en.wikipedia.org/wiki/Control_flow)
- [Crystal (programming language)](https://en.wikipedia.org/wiki/Crystal_(programming_language))
- [Declaration (computer programming)](https://en.wikipedia.org/wiki/Declaration_(computer_programming))
- [Do while loop](https://en.wikipedia.org/wiki/Do_while_loop)
- [Equals sign](https://en.wikipedia.org/wiki/Equals_sign)
- [F Sharp (programming language)](https://en.wikipedia.org/wiki/F_Sharp_(programming_language))
- [Foreach loop](https://en.wikipedia.org/wiki/Foreach_loop)
- [Foreach loop](https://en.wikipedia.org/wiki/Foreach_loop)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [General recursive function](https://en.wikipedia.org/wiki/General_recursive_function)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Heinz Rutishauser](https://en.wikipedia.org/wiki/Heinz_Rutishauser)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Naming convention (programming)](https://en.wikipedia.org/wiki/Naming_convention_(programming))
- [Imaginary unit](https://en.wikipedia.org/wiki/Imaginary_unit)
- [Immutable object](https://en.wikipedia.org/wiki/Immutable_object)
- [Imperative programming](https://en.wikipedia.org/wiki/Imperative_programming)
- [Index notation](https://en.wikipedia.org/wiki/Index_notation)
- [Infinite loop](https://en.wikipedia.org/wiki/Infinite_loop)
- [Instruction set architecture](https://en.wikipedia.org/wiki/Instruction_set_architecture)
- [Iteration](https://en.wikipedia.org/wiki/Iteration)
- [Iterator](https://en.wikipedia.org/wiki/Iterator)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Julia (programming language)](https://en.wikipedia.org/wiki/Julia_(programming_language))
- [Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson)
- [Label (computer science)](https://en.wikipedia.org/wiki/Label_(computer_science))
- [Language construct](https://en.wikipedia.org/wiki/Language_construct)
- [Loop variant](https://en.wikipedia.org/wiki/Loop_variant)
- [Lucee](https://en.wikipedia.org/wiki/Lucee)
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [Maple (software)](https://en.wikipedia.org/wiki/Maple_(software))
- [Mathematical notation](https://en.wikipedia.org/wiki/Mathematical_notation)
- [Maxima (software)](https://en.wikipedia.org/wiki/Maxima_(software))
- [Microsoft Small Basic](https://en.wikipedia.org/wiki/Microsoft_Small_Basic)
- [Modula](https://en.wikipedia.org/wiki/Modula)
- [Monad (functional programming)](https://en.wikipedia.org/wiki/Monad_(functional_programming))
- [Multiplication](https://en.wikipedia.org/wiki/Multiplication)
- [Niklaus Wirth](https://en.wikipedia.org/wiki/Niklaus_Wirth)
- [Nim (programming language)](https://en.wikipedia.org/wiki/Nim_(programming_language))
- [OCaml](https://en.wikipedia.org/wiki/OCaml)
- [Oberon-2](https://en.wikipedia.org/wiki/Oberon-2)
- [Oberon (programming language)](https://en.wikipedia.org/wiki/Oberon_(programming_language))
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PL/I](https://en.wikipedia.org/wiki/PL/I)
- [Parallel computing](https://en.wikipedia.org/wiki/Parallel_computing)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [PostScript](https://en.wikipedia.org/wiki/PostScript)
- [Primitive recursive function](https://en.wikipedia.org/wiki/Primitive_recursive_function)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Railo](https://en.wikipedia.org/wiki/Railo)
- [Reserved word](https://en.wikipedia.org/wiki/Reserved_word)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [Sides of an equation](https://en.wikipedia.org/wiki/Sides_of_an_equation)
- [Simula](https://en.wikipedia.org/wiki/Simula)
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Statement (computer science)](https://en.wikipedia.org/wiki/Statement_(computer_science))
- [Stephen C. Johnson](https://en.wikipedia.org/wiki/Stephen_C._Johnson)
- [Structured programming](https://en.wikipedia.org/wiki/Structured_programming)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Summation](https://en.wikipedia.org/wiki/Summation)
- [Superplan](https://en.wikipedia.org/wiki/Superplan)
- [Syntax (programming languages)](https://en.wikipedia.org/wiki/Syntax_(programming_languages))
- [Tag (programming)](https://en.wikipedia.org/wiki/Tag_(programming))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Variable (computer science)](https://en.wikipedia.org/wiki/Variable_(computer_science))
- [While loop](https://en.wikipedia.org/wiki/While_loop)
- [While loop](https://en.wikipedia.org/wiki/While_loop)
- [Wolfram Language](https://en.wikipedia.org/wiki/Wolfram_Language)
- [Wolfram Mathematica](https://en.wikipedia.org/wiki/Wolfram_Mathematica)
- [YouTube](https://en.wikipedia.org/wiki/YouTube)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Template:Loop constructs](https://en.wikipedia.org/wiki/Template:Loop_constructs)
- [Template talk:Loop constructs](https://en.wikipedia.org/wiki/Template_talk:Loop_constructs)
- [Category:Articles with unsourced statements from August 2009](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_August_2009)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:24:56.121636+00:00_