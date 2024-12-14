# Exception handling syntax

## Article Metadata

- **Last Updated:** 2024-12-14T19:36:52.661769+00:00
- **Original Article:** [Exception handling syntax](https://en.wikipedia.org/wiki/Exception_handling_syntax)
- **Language:** en
- **Page ID:** 3624756

## Summary

Exception handling syntax is the set of keywords and/or structures provided by a computer programming language to allow exception handling, which separates the handling of errors that arise during a program's operation from its ordinary processes. Syntax for exception handling varies between programming languages, partly to cover semantic differences but largely to fit into each language's overall syntactic structure. Some languages do not call the relevant concept "exception handling"; others m

## Categories

- Category:All articles covered by WikiProject Wikify
- Category:All articles with bare URLs for citations
- Category:All articles with dead external links
- Category:Articles covered by WikiProject Wikify from August 2022
- Category:Articles needing cleanup from August 2022
- Category:Articles with bare URLs for citations from August 2022
- Category:Articles with dead external links from October 2020
- Category:Articles with example Ada code
- Category:Articles with example BASIC code
- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example C code
- Category:Articles with example D code
- Category:Articles with example Haskell code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example Lisp (programming language) code
- Category:Articles with example OCaml code
- Category:Articles with example Objective-C code
- Category:Articles with example PHP code
- Category:Articles with example Pascal code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with example Ruby code
- Category:Articles with example Smalltalk code
- Category:Articles with example Swift code
- Category:Articles with example Tcl code
- Category:Articles with hatnote templates targeting a nonexistent page
- Category:Articles with short description
- Category:Control flow
- Category:Programming language comparisons
- Category:Programming language syntax
- Category:Short description matches Wikidata

## Table of Contents

- Catalogue of exception handling syntaxes
- References
- See also

## Content

Exception handling syntax is the set of keywords and/or structures provided by a computer programming language to allow exception handling, which separates the handling of errors that arise during a program's operation from its ordinary processes. Syntax for exception handling varies between programming languages, partly to cover semantic differences but largely to fit into each language's overall syntactic structure. Some languages do not call the relevant concept "exception handling"; others may not have direct facilities for it, but can still provide means to implement it.
Most commonly, error handling uses a try...[catch...][finally...] block, and errors are created via a throw statement, but there is significant variation in naming and syntax.

Catalogue of exception handling syntaxes
Ada
Exception declarations

Raising exceptions

Exception handling and propagation

Assembly language
Most assembly languages will have a macro instruction or an interrupt address available for the particular system to intercept events such as illegal op codes, program check, data errors, overflow, divide by zero, and other such. IBM and Univac mainframes had the STXIT macro. Digital Equipment Corporation RT11 systems had trap vectors for program errors, i/o interrupts, and such. DOS has certain interrupt addresses. Microsoft Windows has specific module calls to trap program errors.

ATS
Bash
One can set a trap for multiple errors, responding to any signal with syntax like:

trap 'echo Error at line ${LINENO}' ERR

BASIC
An On Error goto/gosub structure is used in BASIC and is quite different from modern exception handling; in BASIC there is only one global handler whereas in modern exception handling, exception handlers are stacked.

C
C does not provide direct support to exception handling: it is the programmer's responsibility to prevent errors in the first place and test return values from the functions.
In any case, a possible way to implement exception handling in standard C is to use setjmp/longjmp functions:

Microsoft-specific
Two types exist:

Structured Exception Handling (SEH)
Vectored Exception Handling (VEH, introduced in Windows XP)
Example of SEH in C programming language:

C#
A try block must have at least one catch or finally clause and at most one finally clause.

C++
In C++, a resource acquisition is initialization technique can be used to clean up resources in exceptional situations. C++ intentionally does not support finally. The outer braces for the method are optional.

ColdFusion Markup Language (CFML)
Script syntax
Adobe ColdFusion documentation

Tag syntax
Adobe ColdFusion documentation

Railo-Lucee specific syntax
Added to the standard syntax above, CFML dialects of Railo and Lucee allow a retry statement.
This statement returns processing to the start of the prior try block.
CFScript example:

Tag-syntax example:

D
In D, a finally clause or the resource acquisition is initialization technique can be used to clean up resources in exceptional situations.

Delphi
Exception declarations

Raising exceptions

Exception handling and propagation

Erlang
F#
In addition to the OCaml-based try...with, F# also has the separate try...finally construct, which has the same behavior as a try block with a finally clause in other .NET languages.
For comparison, this is a translation of the C# sample above.

For comparison, this is translation of the OCaml sample below.

Haskell
Haskell does not have special syntax for exceptions. Instead, a try/catch/finally/etc. interface is provided by functions.

prints

(1,42)

in analogy with this C++

Another example is

In purely functional code, if only one error condition exists, the Maybe type may be sufficient, and is an instance of Haskell's Monad class by default. More complex error propagation can be achieved using the Error or ErrorT monads, for which similar functionality (using `catch`) is supported.

Java
A try block must have at least one catch or finally clause and at most one finally clause.

JavaScript
The design of JavaScript makes loud/hard errors very uncommon. Soft/quiet errors are much more prevalent. Hard errors propagate to the nearest try statement, which must be followed by either a single catch clause, a single finally clause, or both.

If there is no try statement at all, then the webpage does not crash. Rather, an error is logged to the console and the stack is cleared. However, JavaScript has the interesting quirk of asynchronous externally-invoked entry points. Whereas, in most other languages, there is always some part of the code running at all times, JavaScript does not have to run linearly from start to end. For example, event listeners, Promises, and timers can be invoked by the browser at a later point in time and run in an isolated but shared context with the rest of the code. Observe how the code below will throw a new error every 4 seconds for an indefinite period of time or until the browser/tab/computer is closed.

Another interesting quirk is polymorphism: JavaScript can throw primitive values as errors.

Note that the catch clause is a catch-all, which catches every type of error. There is no syntaxical ability to assign different handlers to different error types aside from experimental and presently removed Gecko extensions from many years ago. Instead, one can either propagate the error by using a throw statement inside the catch statement, or use multiple conditional cases. Let us compare an example in Java and its rough equivalents in JavaScript.

Another aspect of exceptions are promises, which handle the exception asynchronously. Handling the exception asynchronously has the benefit that errors inside the error handler do not propagate further outwards.

Also observe how event handlers can tie into promises as well.

Lastly, note that, as JavaScript uses mark-and-sweep garbage-collection, there is never any memory leakage from throw statements because the browser automatically cleans dead objects—even with circular references.

Lisp
Common Lisp
Lua
Lua uses the pcall and xpcall functions, with xpcall taking a function to act as a catch block.

Predefined function

Anonymous function

Next Generation Shell
Defining custom exception type

Raising exceptions

Exception handling and propagation

Ignoring exceptions - try without catch

Ignoring exceptions - "tor" operator
"tor" is try-or operator. In case of any exception when evaluating the argument on the left, evaluates to the argument on the right.

"block" - facility to use exceptions to return a value

Objective-C
Exception declarations

Raising exceptions

Exception handling and propagation

OCaml
Perl 5
The Perl mechanism for exception handling uses die to throw an exception when wrapped inside an eval { ... }; block. After the eval, the special variable $@ contains the value passed from die.
Perl 5.005 added the ability to throw objects as well as strings. This allows better introspection and handling of types of exceptions.

The __DIE__ pseudo-signal can be trapped to handle calls to die. This is not suitable for exception handling since it is global. However it can be used to convert string-based exceptions from third-party packages into objects.

The forms shown above can sometimes fail if the global variable $@ is changed between when the exception is thrown and when it is checked in the if ($@) statement. This can happen in multi-threaded environments, or even in single-threaded environments when other code (typically
called in the destruction of some object) resets the global variable before the checking code.
The following example shows a way to avoid this problem (see [1] or [2];  cf. [3]). But at the cost of not being able to use return values:

Several modules in the Comprehensive Perl Archive Network (CPAN) expand on the basic mechanism:

Error provides a set of exception classes and allows use of the try/throw/catch/finally syntax.
TryCatch, Try::Tiny and Nice::Try all allow the use of try/catch/finally syntax instead of boilerplate to handle exceptions correctly.
Exception::Class is a base class and class-maker for derived exception classes. It provides a full structured stack trace in $@->trace and $@->trace->as_string.
Fatal overloads previously defined functions that return true/false e.g., open, close, read, write, etc. This allows built-in functions and others to be used as if they threw exceptions.

PHP
PowerBuilder
Exception handling is available in PowerBuilder versions 8.0 and above.

TRY
   // Normal execution path
CATCH (ExampleException ee)
   //  deal with the ExampleException
FINALLY
   // This optional section is executed upon termination of any of the try or catch blocks above
END TRY

PowerShell
Version 1.0
Version 2.0
Python
R
Rebol
Rexx
Ruby
S-Lang
try 
 {
    % code that might throw an exception
 }
 catch SomeError: 
 { 
    % code that handles this exception
 }
 catch SomeOtherError:
 {  
    % code that handles this exception
 }
 finally   % optional block
 {
    % This code will always get executed
 }

New exceptions may be created using the new_exception function, e.g., 

 new_exception ("MyIOError", IOError, "My I/O Error");

will create an exception called MyIOError as a subclass of IOError. Exceptions may be generated using the throw statement, which can throw arbitrary S-Lang objects.

Smalltalk
The general mechanism is provided by the message on:do:. Exceptions are just normal objects that subclass Error, you throw one by creating an instance and sending it a #signal message, e.g., MyException new signal. The handling mechanism (#on:do:) is again just a normal message implemented by BlockClosure. The thrown exception is passed as a parameter to the handling block closure, and can be queried, as well as potentially sending #resume to it, to allow execution flow to continue.

Swift
Exception handling is supported since Swift 2.

Tcl
Since Tcl 8.6, there is also a try command:

VBScript
Visual Basic 6
Exception handling syntax is very similar to Basic. Error handling is local on each procedure.

Example of specific (non official) implementation of exception handling, which uses object of class "Try".

Visual Basic .NET
A Try block must have at least one clause Catch or Finally clause and at most one Finally clause.

Visual Prolog
X++
References
See also
Exception handling for the semantics of exception handling
Syntax for definition of syntax in computer science

## Related Articles

### Internal Links

- [ATS (programming language)](https://en.wikipedia.org/wiki/ATS_(programming_language))
- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language))
- [Assembly language](https://en.wikipedia.org/wiki/Assembly_language)
- [BASIC](https://en.wikipedia.org/wiki/BASIC)
- [Bash (Unix shell)](https://en.wikipedia.org/wiki/Bash_(Unix_shell))
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CPAN](https://en.wikipedia.org/wiki/CPAN)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [ColdFusion Markup Language](https://en.wikipedia.org/wiki/ColdFusion_Markup_Language)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [DOS](https://en.wikipedia.org/wiki/DOS)
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Delphi (software)](https://en.wikipedia.org/wiki/Delphi_(software))
- [Digital Equipment Corporation](https://en.wikipedia.org/wiki/Digital_Equipment_Corporation)
- [Division by zero](https://en.wikipedia.org/wiki/Division_by_zero)
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Exception handling](https://en.wikipedia.org/wiki/Exception_handling)
- [Exception handling (programming)](https://en.wikipedia.org/wiki/Exception_handling_(programming))
- [F Sharp (programming language)](https://en.wikipedia.org/wiki/F_Sharp_(programming_language))
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Lisp (programming language)](https://en.wikipedia.org/wiki/Lisp_(programming_language))
- [Lua (programming language)](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [Lucee](https://en.wikipedia.org/wiki/Lucee)
- [Microsoft-specific exception handling mechanisms](https://en.wikipedia.org/wiki/Microsoft-specific_exception_handling_mechanisms)
- [Microsoft Dynamics 365](https://en.wikipedia.org/wiki/Microsoft_Dynamics_365)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [OCaml](https://en.wikipedia.org/wiki/OCaml)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [PowerBuilder](https://en.wikipedia.org/wiki/PowerBuilder)
- [PowerShell](https://en.wikipedia.org/wiki/PowerShell)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [RT-11](https://en.wikipedia.org/wiki/RT-11)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Railo](https://en.wikipedia.org/wiki/Railo)
- [Rebol](https://en.wikipedia.org/wiki/Rebol)
- [Resource acquisition is initialization](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization)
- [Rexx](https://en.wikipedia.org/wiki/Rexx)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [S-Lang](https://en.wikipedia.org/wiki/S-Lang)
- [STXIT](https://en.wikipedia.org/wiki/STXIT)
- [Setjmp.h](https://en.wikipedia.org/wiki/Setjmp.h)
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Soft error](https://en.wikipedia.org/wiki/Soft_error)
- [Stack trace](https://en.wikipedia.org/wiki/Stack_trace)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Syntax](https://en.wikipedia.org/wiki/Syntax)
- [Syntax (programming languages)](https://en.wikipedia.org/wiki/Syntax_(programming_languages))
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Type class](https://en.wikipedia.org/wiki/Type_class)
- [VBScript](https://en.wikipedia.org/wiki/VBScript)
- [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic)
- [Visual Basic (.NET)](https://en.wikipedia.org/wiki/Visual_Basic_(.NET))
- [Visual Prolog](https://en.wikipedia.org/wiki/Visual_Prolog)
- [Windows XP](https://en.wikipedia.org/wiki/Windows_XP)
- [User:Citation bot](https://en.wikipedia.org/wiki/User:Citation_bot)
- [Wikipedia:Bare URLs](https://en.wikipedia.org/wiki/Wikipedia:Bare_URLs)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:Link rot](https://en.wikipedia.org/wiki/Wikipedia:Link_rot)
- [Wikipedia:ReFill](https://en.wikipedia.org/wiki/Wikipedia:ReFill)
- [Wikipedia:Template index/Sources of articles](https://en.wikipedia.org/wiki/Wikipedia:Template_index/Sources_of_articles)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles covered by WikiProject Wikify from August 2022](https://en.wikipedia.org/wiki/Category:Articles_covered_by_WikiProject_Wikify_from_August_2022)
- [Category:Articles needing cleanup from August 2022](https://en.wikipedia.org/wiki/Category:Articles_needing_cleanup_from_August_2022)
- [Category:Articles with bare URLs for citations from August 2022](https://en.wikipedia.org/wiki/Category:Articles_with_bare_URLs_for_citations_from_August_2022)
- [Category:Articles with dead external links from October 2020](https://en.wikipedia.org/wiki/Category:Articles_with_dead_external_links_from_October_2020)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:36:52.661769+00:00_