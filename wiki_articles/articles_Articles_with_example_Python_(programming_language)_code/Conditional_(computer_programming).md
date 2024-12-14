# Conditional (computer programming)

## Article Metadata

- **Last Updated:** 2024-12-14T19:35:44.218531+00:00
- **Original Article:** [Conditional (computer programming)](https://en.wikipedia.org/wiki/Conditional_(computer_programming))
- **Language:** en
- **Page ID:** 462839

## Summary

In computer science, conditionals (that is, conditional statements, conditional expressions and conditional constructs) are programming language constructs that perform different computations or actions or return different values depending on the value of a Boolean expression, called a condition.
Conditionals are typically implemented by selectively executing instructions. Although dynamic dispatch is not usually classified as a conditional construct, it is another way to select between alternat

## Categories

- Category:All articles with unsourced statements
- Category:Articles with example C code
- Category:Articles with example Haskell code
- Category:Articles with example Pascal code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Tcl code
- Category:Articles with example pseudocode
- Category:Articles with short description
- Category:Articles with unsourced statements from November 2015
- Category:Commons category link from Wikidata
- Category:Conditional constructs
- Category:Short description is different from Wikidata
- Category:Webarchive template wayback links

## Table of Contents

- Terminology
- If–then(–else)
- Case and switch statements
- Pattern matching
- Hash-based conditionals
- Predication
- Choice system cross reference
- See also
- References
- External links

## Content

In computer science, conditionals (that is, conditional statements, conditional expressions and conditional constructs) are programming language constructs that perform different computations or actions or return different values depending on the value of a Boolean expression, called a condition.
Conditionals are typically implemented by selectively executing instructions. Although dynamic dispatch is not usually classified as a conditional construct, it is another way to select between alternatives at runtime.

Terminology
Conditional statements are imperative constructs executed for side-effect, while conditional expressions return values. Many programming languages (such as C) have distinct conditional statements and conditional expressions. Although in pure functional programming, conditional expressions do not have side-effects, many languages with conditional expressions (such as Lisp) support conditional side-effects.

If–then(–else)
The if–then or if–then–else construction is used in many programming languages. Although the syntax varies from language to language, the basic structure (in pseudocode form) looks like this:

If (Boolean condition) Then
   (consequent)
Else
   (alternative)
End If

For example:

If stock=0 Then
   message= order new stock
Else
   message= there is stock
End If

In the example code above, the part represented by (Boolean condition) constitutes a conditional expression, having intrinsic value (e.g., it may be substituted by either of the values True or False) but having no intrinsic meaning. In contrast, the combination of this expression, the If and Then surrounding it, and the consequent that follows afterward constitute a conditional statement, having intrinsic meaning (e.g., expressing a coherent logical rule) but no intrinsic value.
When an interpreter finds an If, it expects a Boolean condition – for example, x > 0, which means "the variable x contains a number that is greater than zero" – and evaluates that condition. If the condition is true, the statements following the then are executed. Otherwise, the execution continues in the following branch – either in the else block (which is usually optional), or if there is no else branch, then after the end If.
After either branch has been executed, control returns to the point after the end If.

History and development
In early programming languages, especially some dialects of BASIC in the 1980s home computers, an if–then statement could only contain GOTO statements (equivalent to a branch instruction). This led to a hard-to-read style of programming known as spaghetti programming, with programs in this style called spaghetti code.  As a result, structured programming, which allows (virtually) arbitrary statements to be put in statement blocks inside an if statement, gained in popularity, until it became the norm even in most BASIC programming circles. Such mechanisms and principles were based on the older but more advanced ALGOL family of languages, and ALGOL-like languages such as Pascal and Modula-2 influenced modern BASIC variants for many years. While it is possible while using only GOTO statements in if–then statements to write programs that are not spaghetti code and are just as well structured and readable as programs written in a structured programming language, structured programming makes this easier and enforces it.  Structured if–then–else statements like the example above are one of the key elements of structured programming, and they are present in most popular high-level programming languages such as C, Java, JavaScript and Visual Basic .

The "dangling else" problem
The else keyword is made to target a specific if–then statement preceding it, but for nested if–then statements, classic programming languages such as ALGOL 60 struggled to define which specific statement to target. Without clear boundaries for which statement is which, an else keyword could target any preceding if–then statement in the nest, as parsed.

if a then if b then s else s2

can be parsed as

if a then (if b then s) else s2

or

if a then (if b then s else s2)

depending on whether the else is associated with the first if or second if. This is known as the dangling else problem, and is resolved in various ways, depending on the language (commonly via the end if statement or {...} brackets).

Else if
By using else if, it is possible to combine several conditions. Only the statements following the first condition that is found to be true will be executed. All other statements will be skipped.

if condition then
   -- statements
elseif condition then
   -- more statements
elseif condition then
   -- more statements;
...
else
   -- other statements;
end if;

For example, for a shop offering as much as a 30% discount for an item:

if discount < 11% then
   print (you have to pay $30)
elseif discount<21% then
   print (you have to pay $20)
elseif discount<31% then
   print (you have to pay $10)
end if;

In the example above, if the discount is 10%, then the first if statement will be evaluated as true and "you have to pay $30" will be printed out. All other statements below that first if statement will be skipped.
The elseif statement, in the Ada language for example, is simply syntactic sugar for else followed by if. In Ada, the difference is that only one end if is needed, if one uses elseif instead of else followed by if. PHP uses the elseif keyword both for its curly brackets or colon syntaxes. Perl provides the keyword elsif to avoid the large number of braces that would be required by multiple if and else statements. Python uses the special keyword elif because structure is denoted by indentation rather than braces, so a repeated use of else and if would require increased indentation after every condition. Some implementations of BASIC, such as Visual Basic, use ElseIf too. Similarly, the earlier UNIX shells (later gathered up to the POSIX shell syntax) use elif too, but giving the choice of delimiting with spaces, line breaks, or both.
However, in many languages more directly descended from Algol, such as Simula, Pascal, BCPL and C, this special syntax for the else if construct is not present, nor is it present in the many syntactical derivatives of C, such as Java, ECMAScript, and so on. This works because in these languages, any single statement (in this case if cond...) can follow a conditional without being enclosed in a block.
This design choice has a slight "cost". Each else if branch effectively adds an extra nesting level. This complicates the job for the compiler (or the people who write the compiler), because the compiler must analyse and implement arbitrarily long else if chains recursively.
If all terms in the sequence of conditionals are testing the value of a single expression (e.g., if x=0 ... else if x=1 ... else if x=2...), an alternative is the switch statement, also called case-statement or select-statement. Conversely, in languages that do not have a switch statement, these can be produced by a sequence of else if statements.

If–then–else expressions
Many languages support conditional expressions, which are similar to if statements, but return a value as a result. Thus, they are true expressions (which evaluate to a value), not statements (which may not be permitted in the context of a value).  The concept of conditional expressions was first developed by John McCarthy during his research into symbolic processing in the late 1950s.

Algol family
ALGOL 60 and some other members of the ALGOL family allow if–then–else as an expression.  The idea of including conditional expressions was suggested by John McCarthy, though the ALGOL committee decided to use English words rather than McCarthy's mathematical syntax:

  myvariable := if x > 20 then 1 else 2

Lisp dialects
In dialects of Lisp – Scheme, Racket and Common Lisp :

Haskell
In Haskell 98, there is only an if expression, no if statement, and the else part is compulsory, as every expression must have some value. Logic that would be expressed with conditionals in other languages is usually expressed with pattern matching in recursive functions.
Because Haskell is lazy, it is possible to write control structures, such as if, as ordinary expressions; the lazy evaluation means that an if function can evaluate only the condition and proper branch (where a strict language would evaluate all three). It can be written like this:

C-like languages
C and C-like languages have a special ternary operator (?:) for conditional expressions with a function that may be described by a template like this:

condition ? evaluated-when-true : evaluated-when-false

This means that it can be inlined into expressions, unlike if-statements, in C-like languages:

which can be compared to the Algol-family if–then–else expressions (in contrast to a statement) (and similar in Ruby and Scala, among others).
To accomplish the same using an if-statement, this would take more than one line of code (under typical layout conventions), and require mentioning "my_variable" twice:

Some argue that the explicit if/then statement is easier to read and that it may compile to more efficient code than the ternary operator, while others argue that concise expressions are easier to read than statements spread over several lines containing repetition.

Small Basic
First, when the user runs the program, a cursor appears waiting for the reader to type a number. If that number is greater than 10, the text "My variable is named 'foo'." is displayed on the screen. If the number is smaller than 10, then the message "My variable is named 'bar'." is printed on the screen.

Visual Basic
In Visual Basic and some other languages, a function called IIf is provided, which can be used as a conditional expression. However, it does not behave like a true conditional expression, because both the true and false branches are always evaluated; it is just that the result of one of them is thrown away, while the result of the other is returned by the IIf function.

Tcl
In Tcl if is not a keyword but a function (in Tcl known as command or proc). For example

invokes a function named if passing 2 arguments: The first one being the condition and the second one being the true branch. Both arguments are passed as strings (in Tcl everything within curly brackets is a string).
In the above example the condition is not evaluated before calling the function. Instead, the implementation of the if function receives the condition as a string value and is responsible to evaluate this string as an expression in the callers scope.
Such a behavior is possible by using uplevel and expr commands:

Uplevel makes it possible to implement new control constructs as Tcl procedures (for example, uplevel could be used to implement the while construct as a Tcl procedure).
Because if is actually a function it also returns a value:

The return value from the command is the result of the body script that was executed, or an empty string if none of the expressions was non-zero and there was no bodyN.

Rust
In Rust, if is always an expression. It evaluates to the value of whichever branch is executed, or to the unit type () if no branch is executed. If a branch does not provide a return value, it evaluates to () by default. To ensure the if expression's type is known at compile time, each branch must evaluate to a value of the same type. For this reason, an else branch is effectively compulsory unless the other branches evaluate to (), because an if without an else can always evaluate to () by default.

Guarded conditionals
The Guarded Command Language (GCL) of Edsger Dijkstra supports conditional execution as a list of commands consisting of a Boolean-valued guard (corresponding to a condition) and its corresponding statement. In GCL, exactly one of the statements whose guards is true is evaluated, but which one is arbitrary. In this code

if G0 → S0
 □ G1 → S1
...
 □ Gn → Sn
fi

the Gi's are the guards and the Si's are the statements. If none of the guards is true, the program's behavior is undefined.
GCL is intended primarily for reasoning about programs, but similar notations have been implemented in Concurrent Pascal and occam.

Arithmetic if
Up to Fortran 77, the language Fortran has had an arithmetic if statement which jumps to one of three labels depending on whether its argument e is e < 0, e = 0, e > 0. This was the earliest conditional statement in Fortran.

Syntax
Where e is any numeric expression (not necessarily an integer).

Semantics
This is equivalent to this sequence, where e is evaluated only once.

Stylistics
Arithmetic if is an unstructured control statement, and is not used in structured programming.
In practice it has been observed that most arithmetic IF statements reference the following statement with one or two of the labels.
This was the only conditional control statement in the original implementation of Fortran on the IBM 704 computer. On that computer the test-and-branch op-code had three addresses for those three states. Other computers would have "flag" registers such as positive, zero, negative, even, overflow, carry, associated with the last arithmetic operations and would use instructions such as 'Branch if accumulator negative' then 'Branch if accumulator zero' or similar. Note that the expression is evaluated once only, and in cases such as integer arithmetic where overflow may occur, the overflow or carry flags would be considered also.

Object-oriented implementation in Smalltalk
In contrast to other languages, in Smalltalk the conditional statement is not a language construct but defined in the class Boolean as an abstract method that takes two parameters, both closures. Boolean has two subclasses, True and False, which both define the method, True executing the first closure only, False executing the second closure only.

JavaScript
JavaScript uses if-else statements similar to those in C languages. A Boolean value is accepted within parentheses between the reserved if keyword and a left curly bracket.

The above example takes the conditional of Math.random() < 0.5 which outputs true if a random float value between 0 and 1 is greater than 0.5. The statement uses it to randomly choose between outputting You got Heads! or You got Tails! to the console. Else and else-if statements can also be chained after the curly bracket of the statement preceding it as many times as necessary, as shown below:

Lambda calculus
In Lambda calculus, the concept of an if-then-else conditional can be expressed using the following expressions:

true = λx. λy. x
false = λx. λy. y
ifThenElse = (λc. λx. λy. (c x y))

true takes up to two arguments and once both are provided (see currying), it returns the first argument given.
false takes up to two arguments and once both are provided(see currying), it returns the second argument given.
ifThenElse takes up to three arguments and once all are provided, it passes both second and third argument to the first argument(which is a function that given two arguments, and produces a result). We expect ifThenElse to only take true or false as an argument, both of which project the given two arguments to their preferred single argument, which is then returned.
note: if ifThenElse is passed two functions as the left and right conditionals; it is necessary to also pass an empty tuple () to the result of ifThenElse in order to actually call the chosen function, otherwise ifThenElse will just return the function object without getting called.
In a system where numbers can be used without definition (like Lisp, Traditional paper math, so on), the above can be expressed as a single closure below:

Here, true, false, and ifThenElse are bound to their respective definitions which are passed to their scope at the end of their block.
A working JavaScript analogy(using only functions of single variable for rigor) to this is as follows:

The code above with multivariable functions looks like this:

Another version of the earlier example without a system where numbers are assumed is below.
The first example shows the first branch being taken, while second example shows the second branch being taken.

Smalltalk uses a similar idea for its  true and false representations, with True and False being singleton objects that respond to messages ifTrue/ifFalse differently.
Haskell used to use this exact model for its Boolean type, but at the time of writing, most Haskell programs use syntactic sugar "if a then b else c" construct which unlike ifThenElse does not compose unless
either wrapped in another function or re-implemented as shown in The Haskell section of this page.

Case and switch statements
Switch statements (in some languages, case statements or multiway branches) compare a given value with specified constants and take action according to the first constant to match. There is usually a provision for a default action ('else','otherwise') to be taken if no match succeeds. Switch statements can allow compiler optimizations, such as lookup tables. In dynamic languages, the cases may not be limited to constant expressions, and might extend to pattern matching, as in the shell script example on the right, where the '*)' implements the default case as a regular expression matching any string.

Pattern matching
Pattern matching may be seen as an alternative to both if–then–else, and case statements. It is available in many programming languages with functional programming features, such as Wolfram Language, ML and many others. Here is a simple example written in the OCaml language:

The power of pattern matching is the ability to concisely match not only actions but also values to patterns of data. Here is an example written in Haskell which illustrates both of these features:

This code defines a function map, which applies the first argument (a function) to each of the elements of the second argument (a list), and returns the resulting list. The two lines are the two definitions of the function for the two kinds of arguments possible in this case – one where the list is empty (just return an empty list) and the other case where the list is not empty.
Pattern matching is not strictly speaking always a choice construct, because it is possible in Haskell to write only one alternative, which is guaranteed to always be matched – in this situation, it is not being used as a choice construct, but simply as a way to bind names to values. However, it is frequently used as a choice construct in the languages in which it is available.

Hash-based conditionals
In programming languages that have associative arrays or comparable data structures, such as Python, Perl, PHP or Objective-C, it is idiomatic to use them to implement conditional assignment.

In languages that have anonymous functions or that allow a programmer to assign a named function to a variable reference, conditional flow can be implemented by using a hash as a dispatch table.

Predication
An alternative to conditional branch instructions is predication. Predication is an architectural feature that enables instructions to be conditionally executed instead of modifying the control flow.

Choice system cross reference
This table refers to the most recent language specification of each language. For languages that do not have a specification, the latest officially released implementation is referred to.

See also
Branch (computer science)
Conditional compilation
Dynamic dispatch for another way to make execution choices
McCarthy Formalism for history and historical references
Named condition
Relational operator
Test (Unix)
Yoda conditions
Conditional move

References
External links

 Media related to Conditional (computer programming) at Wikimedia Commons
IF NOT (ActionScript 3.0) video

## Related Articles

### Internal Links

- [Ternary conditional operator](https://en.wikipedia.org/wiki/Ternary_conditional_operator)
- [ALGOL](https://en.wikipedia.org/wiki/ALGOL)
- [ALGOL 60](https://en.wikipedia.org/wiki/ALGOL_60)
- [APL (programming language)](https://en.wikipedia.org/wiki/APL_(programming_language))
- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language))
- [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- [Arithmetic IF](https://en.wikipedia.org/wiki/Arithmetic_IF)
- [Associative array](https://en.wikipedia.org/wiki/Associative_array)
- [BASIC](https://en.wikipedia.org/wiki/BASIC)
- [Bash (Unix shell)](https://en.wikipedia.org/wiki/Bash_(Unix_shell))
- [Block (programming)](https://en.wikipedia.org/wiki/Block_(programming))
- [Boolean data type](https://en.wikipedia.org/wiki/Boolean_data_type)
- [Branch (computer science)](https://en.wikipedia.org/wiki/Branch_(computer_science))
- [Predication (computer architecture)](https://en.wikipedia.org/wiki/Predication_(computer_architecture))
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [COBOL](https://en.wikipedia.org/wiki/COBOL)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [C syntax](https://en.wikipedia.org/wiki/C_syntax)
- [SQL syntax](https://en.wikipedia.org/wiki/SQL_syntax)
- [Closure (computer programming)](https://en.wikipedia.org/wiki/Closure_(computer_programming))
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Concurrent Pascal](https://en.wikipedia.org/wiki/Concurrent_Pascal)
- [Conditional compilation](https://en.wikipedia.org/wiki/Conditional_compilation)
- [Predication (computer architecture)](https://en.wikipedia.org/wiki/Predication_(computer_architecture))
- [Control flow](https://en.wikipedia.org/wiki/Control_flow)
- [Currying](https://en.wikipedia.org/wiki/Currying)
- [Dangling else](https://en.wikipedia.org/wiki/Dangling_else)
- [Delphi (software)](https://en.wikipedia.org/wiki/Delphi_(software))
- [Dispatch table](https://en.wikipedia.org/wiki/Dispatch_table)
- [Dynamic dispatch](https://en.wikipedia.org/wiki/Dynamic_dispatch)
- [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript)
- [Edsger W. Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra)
- [Eiffel (programming language)](https://en.wikipedia.org/wiki/Eiffel_(programming_language))
- [Expression (computer science)](https://en.wikipedia.org/wiki/Expression_(computer_science))
- [F Sharp (programming language)](https://en.wikipedia.org/wiki/F_Sharp_(programming_language))
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [Goto](https://en.wikipedia.org/wiki/Goto)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Guard (computer science)](https://en.wikipedia.org/wiki/Guard_(computer_science))
- [Guarded Command Language](https://en.wikipedia.org/wiki/Guarded_Command_Language)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Home computer](https://en.wikipedia.org/wiki/Home_computer)
- [IBM 704](https://en.wikipedia.org/wiki/IBM_704)
- [IIf](https://en.wikipedia.org/wiki/IIf)
- [Conditional (computer programming)](https://en.wikipedia.org/wiki/Conditional_(computer_programming))
- [If Then Else](https://en.wikipedia.org/wiki/If_Then_Else)
- [Include directive](https://en.wikipedia.org/wiki/Include_directive)
- [Instruction set architecture](https://en.wikipedia.org/wiki/Instruction_set_architecture)
- [Interpreter (computing)](https://en.wikipedia.org/wiki/Interpreter_(computing))
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus)
- [Language construct](https://en.wikipedia.org/wiki/Language_construct)
- [Lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation)
- [Lisp (programming language)](https://en.wikipedia.org/wiki/Lisp_(programming_language))
- [Lookup table](https://en.wikipedia.org/wiki/Lookup_table)
- [ML (programming language)](https://en.wikipedia.org/wiki/ML_(programming_language))
- [Wolfram Mathematica](https://en.wikipedia.org/wiki/Wolfram_Mathematica)
- [McCarthy Formalism](https://en.wikipedia.org/wiki/McCarthy_Formalism)
- [Modula-2](https://en.wikipedia.org/wiki/Modula-2)
- [COBOL](https://en.wikipedia.org/wiki/COBOL)
- [Nesting (computing)](https://en.wikipedia.org/wiki/Nesting_(computing))
- [OCaml](https://en.wikipedia.org/wiki/OCaml)
- [Oberon (programming language)](https://en.wikipedia.org/wiki/Oberon_(programming_language))
- [Object Pascal](https://en.wikipedia.org/wiki/Object_Pascal)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [Occam (programming language)](https://en.wikipedia.org/wiki/Occam_(programming_language))
- [Optimizing compiler](https://en.wikipedia.org/wiki/Optimizing_compiler)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Preprocessor](https://en.wikipedia.org/wiki/Preprocessor)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Pseudocode](https://en.wikipedia.org/wiki/Pseudocode)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [QuickBASIC](https://en.wikipedia.org/wiki/QuickBASIC)
- [Racket (programming language)](https://en.wikipedia.org/wiki/Racket_(programming_language))
- [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Relational operator](https://en.wikipedia.org/wiki/Relational_operator)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Execution (computing)](https://en.wikipedia.org/wiki/Execution_(computing))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [SQL-92](https://en.wikipedia.org/wiki/SQL-92)
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scheme (programming language)](https://en.wikipedia.org/wiki/Scheme_(programming_language))
- [Shell script](https://en.wikipedia.org/wiki/Shell_script)
- [Side effect (computer science)](https://en.wikipedia.org/wiki/Side_effect_(computer_science))
- [Simula](https://en.wikipedia.org/wiki/Simula)
- [Microsoft Small Basic](https://en.wikipedia.org/wiki/Microsoft_Small_Basic)
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code)
- [Statement (computer science)](https://en.wikipedia.org/wiki/Statement_(computer_science))
- [Structured programming](https://en.wikipedia.org/wiki/Structured_programming)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Switch statement](https://en.wikipedia.org/wiki/Switch_statement)
- [Syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Ternary conditional operator](https://en.wikipedia.org/wiki/Ternary_conditional_operator)
- [Ternary operation](https://en.wikipedia.org/wiki/Ternary_operation)
- [Test (Unix)](https://en.wikipedia.org/wiki/Test_(Unix))
- [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic)
- [Visual Basic (.NET)](https://en.wikipedia.org/wiki/Visual_Basic_(.NET))
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [PowerShell](https://en.wikipedia.org/wiki/PowerShell)
- [Wolfram Language](https://en.wikipedia.org/wiki/Wolfram_Language)
- [Yoda conditions](https://en.wikipedia.org/wiki/Yoda_conditions)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Category:Articles with unsourced statements from November 2015](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_November_2015)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:35:44.218531+00:00_