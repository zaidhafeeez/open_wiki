# Control flow

## Article Metadata

- **Last Updated:** 2024-12-14T19:35:47.962883+00:00
- **Original Article:** [Control flow](https://en.wikipedia.org/wiki/Control_flow)
- **Language:** en
- **Page ID:** 45459

## Summary

In computer science, control flow (or flow of control) is the order in which individual statements, instructions or function calls of an imperative program are executed or evaluated. The emphasis on explicit control flow distinguishes an imperative programming language from a declarative programming language.
Within an imperative programming language, a control flow statement is a statement that results in a choice being made as to which of two or more paths to follow. For non-strict functional 

## Categories

- Category:All articles with unsourced statements
- Category:Articles with example ALGOL 60 code
- Category:Articles with example ALGOL 68 code
- Category:Articles with example Ada code
- Category:Articles with example C++ code
- Category:Articles with example C Sharp code
- Category:Articles with example C code
- Category:Articles with example D code
- Category:Articles with example Fortran code
- Category:Articles with example Haskell code
- Category:Articles with example JavaScript code
- Category:Articles with example Java code
- Category:Articles with example Lisp (programming language) code
- Category:Articles with example MATLAB/Octave code
- Category:Articles with example PHP code
- Category:Articles with example Pascal code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Ruby code
- Category:Articles with example Smalltalk code
- Category:Articles with short description
- Category:Articles with unsourced statements from July 2014
- Category:Commons category link from Wikidata
- Category:Control flow
- Category:Iteration in programming
- Category:Programming language comparisons
- Category:Recursion
- Category:Short description is different from Wikidata
- Category:Webarchive template wayback links
- Category:Wikipedia articles needing clarification from November 2015

## Table of Contents

- Categories
- Primitives
- Minimal structured control flow
- Control structures in practice
- Choice
- Loops
- Structured non-local control flow
- Proposed control structures
- Security
- See also
- Notes
- References
- Further reading
- External links

## Content

In computer science, control flow (or flow of control) is the order in which individual statements, instructions or function calls of an imperative program are executed or evaluated. The emphasis on explicit control flow distinguishes an imperative programming language from a declarative programming language.
Within an imperative programming language, a control flow statement is a statement that results in a choice being made as to which of two or more paths to follow. For non-strict functional languages, functions and language constructs exist to achieve the same result, but they are usually not termed control flow statements.
A set of statements is in turn generally structured as a block, which in addition to grouping, also defines a lexical scope.
Interrupts and signals are low-level mechanisms that can alter the flow of control in a way similar to a subroutine, but usually occur as a response to some external stimulus or event (that can occur asynchronously), rather than execution of an in-line control flow statement.
At the level of machine language or assembly language, control flow instructions usually work by altering the program counter. For some central processing units (CPUs), the only control flow instructions available are conditional or unconditional branch instructions, also termed jumps.

Categories
The kinds of control flow statements supported by different languages vary, but can be categorized by their effect:

Continuation at a different statement (unconditional branch or jump)
Executing a set of statements only if some condition is met (choice - i.e., conditional branch)
Executing a set of statements zero or more times, until some condition is met (i.e., loop - the same as conditional branch)
Executing a set of distant statements, after which the flow of control usually returns (subroutines, coroutines, and continuations)
Stopping the program, preventing any further execution (unconditional halt)

Primitives
Labels
A label is an explicit name or number assigned to a fixed position within the source code, and which may be referenced by control flow statements appearing elsewhere in the source code. A label marks a position within source code and has no other effect.
Line numbers are an alternative to a named label used in some languages (such as BASIC). They are whole numbers placed at the start of each line of text in the source code. Languages which use these often impose the constraint that the line numbers must increase in value in each following line, but may not require that they be consecutive. For example, in BASIC:

In other languages such as C and Ada, a label is an identifier, usually appearing at the start of a line and immediately followed by a colon. For example, in C:

The language ALGOL 60 allowed both whole numbers and identifiers as labels (both linked by colons to the following statement), but few if any other ALGOL variants allowed whole numbers. Early Fortran compilers only allowed whole numbers as labels. Beginning with Fortran-90, alphanumeric labels have also been allowed.

Goto
The goto statement (a combination of the English words go and to, and pronounced accordingly) is the most basic form of unconditional transfer of control.
Although the keyword may either be in upper or lower case depending on the language, it is usually written as:

   goto label

The effect of a goto statement is to cause the next statement to be executed to be the statement appearing at (or immediately after) the indicated label.
Goto statements have been considered harmful by many computer scientists, notably Dijkstra.

Subroutines
The terminology for subroutines varies; they may alternatively be known as routines, procedures, functions (especially if they return results) or methods (especially if they belong to classes or type classes).
In the 1950s, computer memories were very small by current standards so subroutines were used mainly to reduce program size. A piece of code was written once and then used many times from various other places in a program.
Today, subroutines are more often used to help make a program more structured, e.g., by isolating some algorithm or hiding some data access method. If many programmers are working on one program, subroutines are one kind of modularity that can help divide the work.

Sequence
In structured programming, the ordered sequencing of successive commands is considered one of the basic control structures, which is used as a building block for programs alongside iteration, recursion and choice.

Minimal structured control flow
In May 1966, Böhm and Jacopini published an article in Communications of the ACM which showed that any program with gotos could be transformed into a goto-free form involving only choice (IF THEN ELSE) and loops (WHILE condition DO xxx), possibly with duplicated code and/or the addition of Boolean variables (true/false flags). Later authors showed that choice can be replaced by loops (and yet more Boolean variables).
That such minimalism is possible does not mean that it is necessarily desirable; computers theoretically need only one machine instruction (subtract one number from another and branch if the result is negative), but practical computers have dozens or even hundreds of machine instructions.
Other research showed that control structures with one entry and one exit were much easier to understand than any other form, mainly because they could be used anywhere as a statement without disrupting the control flow. In other words, they were composable. (Later developments, such as non-strict programming languages – and more recently, composable software transactions – have continued this strategy, making components of programs even more freely composable.)
Some academics took a purist approach to the Böhm–Jacopini result and argued that even instructions like break and return from the middle of loops are bad practice as they are not needed in the Böhm–Jacopini proof, and thus they advocated that all loops should have a single exit point. This purist approach is embodied in the language Pascal (designed in 1968–1969), which up to the mid-1990s was the preferred tool for teaching introductory programming in academia. The direct application of the Böhm–Jacopini theorem may result in additional local variables being introduced in the structured chart, and may also result in some code duplication. Pascal is affected by both of these problems and according to empirical studies cited by Eric S. Roberts, student programmers had difficulty formulating correct solutions in Pascal for several simple problems, including writing a function for searching an element in an array. A 1980 study by Henry Shapiro cited by Roberts found that using only the Pascal-provided control structures, the correct solution was given by only 20% of the subjects, while no subject wrote incorrect code for this problem if allowed to write a return from the middle of a loop.

Control structures in practice
Most programming languages with control structures have an initial keyword which indicates the type of control structure involved. Languages then divide as to whether or not control structures have a final keyword.

No final keyword: ALGOL 60, C, C++, Go, Haskell, Java, Pascal, Perl, PHP, PL/I, Python, PowerShell. Such languages need some way of grouping statements together:
ALGOL 60 and Pascal: begin ... end
C, C++, Go, Java, Perl, PHP, and PowerShell: curly brackets { ... }
PL/I: DO ... END
Python: uses indent level (see Off-side rule)
Haskell: either indent level or curly brackets can be used, and they can be freely mixed
Lua: uses do ... end
Final keyword: Ada, APL, ALGOL 68, Modula-2, Fortran 77, Mythryl, Visual Basic. The forms of the final keyword vary:
Ada: final keyword is end + space + initial keyword e.g., if ... end if, loop ... end loop
APL: final keyword is :End optionally + initial keyword, e.g., :If ... :End or :If ... :EndIf, Select ... :End or :Select ... :EndSelect, however, if adding an end condition, the end keyword becomes :Until
ALGOL 68, Mythryl: initial keyword spelled backwards e.g., if ... fi, case ... esac
Fortran 77: final keyword is END + initial keyword e.g., IF ... ENDIF, DO ... ENDDO
Modula-2: same final keyword END for everything
Visual Basic: every control structure has its own keyword. If ... End If; For ... Next; Do ... Loop; While ... Wend

Choice
If-then-(else) statements
Conditional expressions and conditional constructs are features of a programming language that perform different computations or actions depending on whether a programmer-specified Boolean condition evaluates to true or false. 

IF..GOTO. A form found in unstructured languages, mimicking a typical machine code instruction, would jump to (GOTO) a label or line number when the condition was met.
IF..THEN..(ENDIF). Rather than being restricted to a jump, any simple statement, or nested block, could follow the THEN key keyword. This a structured form.
IF..THEN..ELSE..(ENDIF). As above, but with a second action to be performed if the condition is false. This is one of the most common forms, with many variations. Some require a terminal ENDIF, others do not. C and related languages do not require a terminal keyword, or a 'then', but do require parentheses around the condition.
Conditional statements can be and often are nested inside other conditional statements. Some languages allow ELSE and IF to be combined into ELSEIF, avoiding the need to have a series of ENDIF or other final statements at the end of a compound statement.

Less common variations include:

Some languages, such as early Fortran, have a three-way or arithmetic if, testing whether a numeric value is negative, zero, or positive.
Some languages have a functional form of an if statement, for instance Lisp's cond.
Some languages have an operator form of an if statement, such as C's ternary operator.
Perl supplements a C-style if with when and unless.
Smalltalk uses ifTrue and ifFalse messages to implement conditionals, rather than any fundamental language construct.

Case and switch statements
Switch statements (or case statements, or multiway branches) compare a given value with specified constants and take action according to the first constant to match. There is usually a provision for a default action ("else", "otherwise") to be taken if no match succeeds. Switch statements can allow compiler optimizations, such as lookup tables. In dynamic languages, the cases may not be limited to constant expressions, and might extend to pattern matching, as in the shell script example on the right, where the *) implements the default case as a glob matching any string. Case logic can also be implemented in functional form, as in SQL's decode statement.

Loops
A loop is a sequence of statements which is specified once but which may be carried out several times in succession. The code "inside" the loop (the body of the loop, shown below as xxx) is obeyed a specified number of times, or once for each of a collection of items, or until some condition is met, or indefinitely. When one of those items is itself also a loop, it is called a "nested loop".
In functional programming languages, such as Haskell and Scheme, both recursive and iterative processes are expressed with tail recursive procedures instead of looping constructs that are syntactic.

Count-controlled loops
Most programming languages have constructions for repeating a loop a certain number of times.
In most cases counting can go downwards instead of upwards and step sizes other than 1 can be used.

In these examples, if N < 1 then the body of loop may execute once (with I having value 1) or not at all, depending on the programming language.
In many programming languages, only integers can be reliably used in a count-controlled loop. Floating-point numbers are represented imprecisely due to hardware constraints, so a loop such as

   for X := 0.1 step 0.1 to 1.0 do

might be repeated 9 or 10 times, depending on rounding errors and/or the hardware and/or the compiler version. Furthermore, if the increment of X occurs by repeated addition, accumulated rounding errors may mean that the value of X in each iteration can differ quite significantly from the expected sequence 0.1, 0.2, 0.3, ..., 1.0.

Condition-controlled loops
Most programming languages have constructions for repeating a loop until some condition changes. Some variations test the condition at the start of the loop; others test it at the end. If the test is at the start, the body may be skipped completely; if it is at the end, the body is always executed at least once.

A control break is a value change detection method used within ordinary loops to trigger processing for groups of values. Values are monitored within the loop and a change diverts program flow to the handling of the group event associated with them.

   DO UNTIL (End-of-File)
      IF new-zipcode <> current-zipcode
         display_tally(current-zipcode, zipcount)
         
         current-zipcode = new-zipcode
         zipcount = 0
      ENDIF
      
      zipcount++
   LOOP

Collection-controlled loops
Several programming languages (e.g., Ada, D, C++11, Smalltalk, PHP, Perl, Object Pascal, Java, C#, MATLAB, Visual Basic, Ruby, Python, JavaScript, Fortran 95 and later) have special constructs which allow implicit looping through all elements of an array, or all members of a set or collection.

   someCollection do: [:eachElement |xxx].

   for Item in Collection do begin xxx end;

   foreach (item; myCollection) { xxx }

   foreach someArray { xxx }

   foreach ($someArray as $k => $v) { xxx }

   Collection<String> coll; for (String s : coll) {}

   foreach (string s in myStringCollection) { xxx }

   someCollection | ForEach-Object { $_ }

   forall ( index = first:last:step... )

Scala has for-expressions, which generalise collection-controlled loops, and also support other uses, such as asynchronous programming. Haskell has do-expressions and comprehensions, which together provide similar function to for-expressions in Scala.

General iteration
General iteration constructs such as C's for statement and Common Lisp's do form can be used to express any of the above sorts of loops, and others, such as looping over some number of collections in parallel. Where a more specific looping construct can be used, it is usually preferred over the general iteration construct, since it often makes the purpose of the expression clearer.

Infinite loops
Infinite loops are used to assure a program segment loops forever or until an exceptional condition arises, such as an error. For instance, an event-driven program (such as a server) should loop forever, handling events as they occur, only stopping when the process is terminated by an operator.
Infinite loops can be implemented using other control flow constructs. Most commonly, in unstructured programming this is jump back up (goto), while in structured programming this is an indefinite loop (while loop) set to never end, either by omitting the condition or explicitly setting it to true, as while (true) .... Some languages have special constructs for infinite loops, typically by omitting the condition from an indefinite loop. Examples include Ada (loop ... end loop), Fortran (DO ... END DO), Go (for { ... }), and Ruby (loop do ... end).
Often, an infinite loop is unintentionally created by a programming error in a condition-controlled loop, wherein the loop condition uses variables that never change within the loop.

Continuation with next iteration
Sometimes within the body of a loop there is a desire to skip the remainder of the loop body and continue with the next iteration of the loop. Some languages provide a statement such as continue (most languages), skip, cycle (Fortran), or next (Perl and Ruby), which will do this. The effect is to prematurely terminate the innermost loop body and then resume as normal with the next iteration. If the iteration is the last one in the loop, the effect is to terminate the entire loop early.

Redo current iteration
Some languages, like Perl and Ruby, have a redo statement that restarts the current iteration from the start.

Restart loop
Ruby has a retry statement that restarts the entire loop from the initial iteration.

Early exit from loops
When using a count-controlled loop to search through a table, it might be desirable to stop searching as soon as the required item is found. Some programming languages provide a statement such as break (most languages), Exit (Visual Basic), or last (Perl), which effect is to terminate the current loop immediately, and transfer control to the statement immediately after that loop. Another term for early-exit loops is loop-and-a-half.
The following example is done in Ada which supports both early exit from loops and loops with test in the middle. Both features are very similar and comparing both code snippets will show the difference: early exit must be combined with an if statement while a condition in the middle is a self-contained construct.

Python supports conditional execution of code depending on whether a loop was exited early (with a break statement) or not by using an else-clause with the loop. For example,

The else clause in the above example is linked to the for statement, and not the inner if statement. Both Python's for and while loops support such an else clause, which is executed only if early exit of the loop has not occurred.
Some languages support breaking out of nested loops; in theory circles, these are called multi-level breaks. One common use example is searching a multi-dimensional table. This can be done either via multilevel breaks (break out of N levels), as in bash and PHP, or via labeled breaks (break out and continue at given label), as in Go, Java and Perl. Alternatives to multilevel breaks include single breaks, together with a state variable which is tested to break out another level; exceptions, which are caught at the level being broken out to; placing the nested loops in a function and using return to effect termination of the entire nested loop; or using a label and a goto statement. C does not include a multilevel break, and the usual alternative is to use a goto to implement a labeled break. Python does not have a multilevel break or continue – this was proposed in PEP 3136, and rejected on the basis that the added complexity was not worth the rare legitimate use.
The notion of multi-level breaks is of some interest in theoretical computer science, because it gives rise to what is today called the Kosaraju hierarchy. In 1973 S. Rao Kosaraju refined the structured program theorem by proving that it is possible to avoid adding additional variables in structured programming, as long as arbitrary-depth, multi-level breaks from loops are allowed. Furthermore, Kosaraju proved that a strict hierarchy of programs exists: for every integer n, there exists a program containing a multi-level break of depth n that cannot be rewritten as a program with multi-level breaks of depth less than n without introducing added variables.
One can also return out of a subroutine executing the looped statements, breaking out of both the nested loop and the subroutine. There are other proposed control structures for multiple breaks, but these are generally implemented as exceptions instead.
In his 2004 textbook, David Watt uses Tennent's notion of sequencer to explain the similarity between multi-level breaks and return statements. Watt notes that a class of sequencers known as escape sequencers, defined as "sequencer that terminates execution of a textually enclosing command or procedure", encompasses both breaks from loops (including multi-level breaks) and return statements. As commonly implemented, however, return sequencers may also carry a (return) value, whereas the break sequencer as implemented in contemporary languages usually cannot.

Loop variants and invariants
Loop variants and loop invariants are used to express correctness of loops.
In practical terms, a loop variant is an integer expression which has an initial non-negative value. The variant's value must decrease during each loop iteration but must never become negative during the correct execution of the loop. Loop variants are used to guarantee that loops will terminate.
A loop invariant is an assertion which must be true before the first loop iteration and remain true after each iteration. This implies that when a loop terminates correctly, both the exit condition and the loop invariant are satisfied. Loop invariants are used to monitor specific properties of a loop during successive iterations.
Some programming languages, such as Eiffel contain native support for loop variants and invariants. In other cases, support is an add-on, such as the Java Modeling Language's specification for loop statements in Java.

Loop sublanguage
Some Lisp dialects provide an extensive sublanguage for describing Loops. An early example can be found in Conversional Lisp of Interlisp. Common Lisp provides a Loop macro which implements such a sublanguage.

Loop system cross-reference table
a  while (true) does not count as an infinite loop for this purpose, because it is not a dedicated language structure.
a b c d e f g h  C's for (init; test; increment) loop is a general loop construct, not specifically a counting one, although it is often used for that.
a b c  Deep breaks may be accomplished in APL, C, C++ and C# through the use of labels and gotos.
a  Iteration over objects was added in PHP 5.
a b c  A counting loop can be simulated by iterating over an incrementing list or generator, for instance, Python's range().
a b c d e  Deep breaks may be accomplished through the use of exception handling.
a  There is no special construct, since the while function can be used for this.
a  There is no special construct, but users can define general loop functions.
a  The C++11 standard introduced the range-based for. In the STL, there is a std::for_each template function which can iterate on STL containers and call a unary function for each element. The functionality also can be constructed as macro on these containers.
a  Count-controlled looping is effected by iteration across an integer interval; early exit by including an additional condition for exit.
a  Eiffel supports a reserved word retry, however it is used in exception handling, not loop control.
a  Requires Java Modeling Language (JML) behavioral interface specification language.
a  Requires loop variants to be integers; transfinite variants are not supported. [1]
a  D supports infinite collections, and the ability to iterate over those collections. This does not require any special construct.
a  Deep breaks can be achieved using GO TO and procedures.
a  Common Lisp predates the concept of generic collection type.

Structured non-local control flow
Many programming languages, especially those favoring more dynamic styles of programming, offer constructs for non-local control flow. These cause the flow of execution to jump out of a given context and resume at some predeclared point. Conditions, exceptions and continuations are three common sorts of non-local control constructs; more exotic ones also exist, such as generators, coroutines and the async keyword.

Conditions
PL/I has some 22 standard conditions (e.g., ZERODIVIDE SUBSCRIPTRANGE ENDFILE) which can be raised and which can be intercepted by: ON condition action; Programmers can also define and use their own named conditions.
Like the unstructured if, only one statement can be specified so in many cases a GOTO is needed to decide where flow of control should resume.
Unfortunately, some implementations had a substantial overhead in both space and time (especially SUBSCRIPTRANGE), so many programmers tried to avoid using conditions.
Common Syntax examples:

 ON condition GOTO label

Exceptions
Modern languages have a specialized structured construct for exception handling which does not rely on the use of GOTO or (multi-level) breaks or returns. For example, in C++ one can write:

Any number and variety of catch clauses can be used above. If there is no catch matching a particular throw, control percolates back through subroutine calls and/or nested blocks until a matching catch is found or until the end of the main program is reached, at which point the program is forcibly stopped with a suitable error message.
Via C++'s influence, catch is the keyword reserved for declaring a pattern-matching exception handler in other languages popular today, like Java or C#. Some other languages like Ada use the keyword exception to introduce an exception handler and then may even employ a different keyword (when in Ada) for the pattern matching. A few languages like AppleScript incorporate placeholders in the exception handler syntax to automatically extract several pieces of information when the exception occurs. This approach is exemplified below by the on error construct from AppleScript:

David Watt's 2004 textbook also analyzes exception handling in the framework of sequencers (introduced in this article in the section on early exits from loops). Watt notes that an abnormal situation, generally exemplified with arithmetic overflows or input/output failures like file not found, is a kind of error that "is detected in some low-level program unit, but [for which] a handler is more naturally located in a high-level program unit". For example, a program might contain several calls to read files, but the action to perform when a file is not found depends on the meaning (purpose) of the file in question to the program and thus a handling routine for this abnormal situation cannot be located in low-level system code. Watts further notes that introducing status flags testing in the caller, as single-exit structured programming or even (multi-exit) return sequencers would entail, results in a situation where "the application code tends to get cluttered by tests of status flags" and that "the programmer might forgetfully or lazily omit to test a status flag. In fact, abnormal situations represented by status flags are by default ignored!" Watt notes that in contrast to status flags testing, exceptions have the opposite default behavior, causing the program to terminate unless the program deals with the exception explicitly in some way, possibly by adding explicit code to ignore it. Based on these arguments, Watt concludes that jump sequencers or escape sequencers are less suitable as a dedicated exception sequencer with the semantics discussed above.
In Object Pascal, D, Java, C#, and Python a finally clause can be added to the try construct. No matter how control leaves the try the code inside the finally clause is guaranteed to execute. This is useful when writing code that must relinquish an expensive resource (such as an opened file or a database connection) when finished processing:

Since this pattern is fairly common, C# has a special syntax:

Upon leaving the using-block, the compiler guarantees that the stm object is released, effectively binding the variable to the file stream while abstracting from the side effects of initializing and releasing the file. Python's with statement and Ruby's block argument to File.open are used to similar effect.
All the languages mentioned above define standard exceptions and the circumstances under which they are thrown. Users can throw exceptions of their own; C++ allows users to throw and catch almost any type, including basic types like int, whereas other languages like Java are less permissive.

Continuations
Async
C# 5.0 introduced the async keyword for supporting asynchronous I/O in a "direct style".

Generators
Generators, also known as semicoroutines, allow control to be yielded to a consumer method temporarily, typically using a yield keyword (yield description) . Like the async keyword, this supports programming in a "direct style".

Coroutines
Coroutines are functions that can yield control to each other - a form of co-operative multitasking without threads.
Coroutines can be implemented as a library if the programming language provides either continuations or generators - so the distinction between coroutines and generators in practice is a technical detail.

Non-local control flow cross reference
Proposed control structures
In a spoof Datamation article in 1973, R. Lawrence Clark suggested that the GOTO statement could be replaced by the COMEFROM statement, and provides some entertaining examples. COMEFROM was implemented in one esoteric programming language named INTERCAL.
Donald Knuth's 1974 article "Structured Programming with go to Statements", identifies two situations which were not covered by the control structures listed above, and gave examples of control structures which could handle these situations. Despite their utility, these constructs have not yet found their way into mainstream programming languages.

Loop with test in the middle
The following was proposed by Dahl in 1972:

   loop                           loop
       xxx1                           read(char);
   while test;                    while not atEndOfFile;
       xxx2                           write(char);
   repeat;                        repeat;

If xxx1 is omitted, we get a loop with the test at the top (a traditional while loop). If xxx2 is omitted, we get a loop with the test at the bottom, equivalent to a do while loop in many languages. If while is omitted, we get an infinite loop. The construction here can be thought of as a do loop with the while check in the middle. Hence this single construction can replace several constructions in most programming languages.
Languages lacking this construct generally emulate it using an equivalent infinite-loop-with-break idiom:

while (true) {
    xxx1
    if (not test)
        break
    xxx2
}

A possible variant is to allow more than one while test; within the loop, but the use of exitwhen (see next section) appears to cover this case better.
In Ada, the above loop construct (loop-while-repeat) can be represented using a standard infinite loop (loop - end loop) that has an exit when clause in the middle (not to be confused with the exitwhen statement in the following section).

Naming a loop (like Read_Data in this example) is optional but permits leaving the outer loop of several nested loops.

Multiple early exit/exit from nested loops
This construct was proposed by Zahn in 1974. A modified version is presented here.

   exitwhen EventA or EventB or EventC;
       xxx
   exits
       EventA: actionA
       EventB: actionB
       EventC: actionC
   endexit;

exitwhen is used to specify the events which may occur within xxx,
their occurrence is indicated by using the name of the event as a statement. When some event does occur, the relevant action is carried out, and then control passes just after endexit. This construction provides a very clear separation between determining that some situation applies, and the action to be taken for that situation.
exitwhen is conceptually similar to exception handling, and exceptions or similar constructs are used for this purpose in many languages.
The following simple example involves searching a two-dimensional table for a particular item.

   exitwhen found or missing;
       for I := 1 to N do
           for J := 1 to M do
               if table[I,J] = target then found;
       missing;
   exits
       found:   print ("item is in table");
       missing: print ("item is not in table");
   endexit;

Security
One way to attack a piece of software is to redirect the flow of execution of a program. A variety of control-flow integrity techniques, including stack canaries, buffer overflow protection, shadow stacks, and vtable pointer verification, are used to defend against these attacks.

See also
Notes
References
Further reading
Hoare, C. A. R. "Partition: Algorithm 63," "Quicksort: Algorithm 64," and "Find: Algorithm 65." Comm. ACM 4, 321–322, 1961.

External links

 Media related to Control flow at Wikimedia Commons
Go To Statement Considered Harmful
A Linguistic Contribution of GOTO-less Programming
"Structured Programming with Go To Statements" (PDF). Archived from the original (PDF) on 2009-08-24. (2.88 MB)
"IBM 704 Manual" (PDF). (31.4 MB)

## Related Articles

### Internal Links

- [ACM Computing Surveys](https://en.wikipedia.org/wiki/ACM_Computing_Surveys)
- [ALGOL](https://en.wikipedia.org/wiki/ALGOL)
- [ALGOL 60](https://en.wikipedia.org/wiki/ALGOL_60)
- [ALGOL 68](https://en.wikipedia.org/wiki/ALGOL_68)
- [APL (programming language)](https://en.wikipedia.org/wiki/APL_(programming_language))
- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language))
- [AppleScript](https://en.wikipedia.org/wiki/AppleScript)
- [Arithmetic IF](https://en.wikipedia.org/wiki/Arithmetic_IF)
- [Assembly language](https://en.wikipedia.org/wiki/Assembly_language)
- [Asynchronous I/O](https://en.wikipedia.org/wiki/Asynchronous_I/O)
- [Asynchrony (computer programming)](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming))
- [Asynchronous system](https://en.wikipedia.org/wiki/Asynchronous_system)
- [BASIC](https://en.wikipedia.org/wiki/BASIC)
- [Block (programming)](https://en.wikipedia.org/wiki/Block_(programming))
- [Boolean data type](https://en.wikipedia.org/wiki/Boolean_data_type)
- [Branch (computer science)](https://en.wikipedia.org/wiki/Branch_(computer_science))
- [Buffer overflow protection](https://en.wikipedia.org/wiki/Buffer_overflow_protection)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C++11](https://en.wikipedia.org/wiki/C%2B%2B11)
- [COBOL](https://en.wikipedia.org/wiki/COBOL)
- [COMEFROM](https://en.wikipedia.org/wiki/COMEFROM)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [C preprocessor](https://en.wikipedia.org/wiki/C_preprocessor)
- [Central processing unit](https://en.wikipedia.org/wiki/Central_processing_unit)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Cooperative multitasking](https://en.wikipedia.org/wiki/Cooperative_multitasking)
- [Duplicate code](https://en.wikipedia.org/wiki/Duplicate_code)
- [Communications of the ACM](https://en.wikipedia.org/wiki/Communications_of_the_ACM)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Computer program](https://en.wikipedia.org/wiki/Computer_program)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Conditional (computer programming)](https://en.wikipedia.org/wiki/Conditional_(computer_programming))
- [Branch (computer science)](https://en.wikipedia.org/wiki/Branch_(computer_science))
- [Considered harmful](https://en.wikipedia.org/wiki/Considered_harmful)
- [Container (abstract data type)](https://en.wikipedia.org/wiki/Container_(abstract_data_type))
- [Continuation](https://en.wikipedia.org/wiki/Continuation)
- [Control-flow diagram](https://en.wikipedia.org/wiki/Control-flow_diagram)
- [Control-flow graph](https://en.wikipedia.org/wiki/Control-flow_graph)
- [Control-flow integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)
- [Control break](https://en.wikipedia.org/wiki/Control_break)
- [Control-flow analysis](https://en.wikipedia.org/wiki/Control-flow_analysis)
- [Control table](https://en.wikipedia.org/wiki/Control_table)
- [Coroutine](https://en.wikipedia.org/wiki/Coroutine)
- [Coroutine](https://en.wikipedia.org/wiki/Coroutine)
- [List of programming languages by type](https://en.wikipedia.org/wiki/List_of_programming_languages_by_type)
- [Cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity)
- [DRAKON](https://en.wikipedia.org/wiki/DRAKON)
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Datamation](https://en.wikipedia.org/wiki/Datamation)
- [David Watt (computer scientist)](https://en.wikipedia.org/wiki/David_Watt_(computer_scientist))
- [Declarative programming](https://en.wikipedia.org/wiki/Declarative_programming)
- [Default (computer science)](https://en.wikipedia.org/wiki/Default_(computer_science))
- [Do while loop](https://en.wikipedia.org/wiki/Do_while_loop)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Donald Knuth](https://en.wikipedia.org/wiki/Donald_Knuth)
- [Dynamic programming language](https://en.wikipedia.org/wiki/Dynamic_programming_language)
- [Edsger W. Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra)
- [Eiffel (programming language)](https://en.wikipedia.org/wiki/Eiffel_(programming_language))
- [Eric S. Roberts](https://en.wikipedia.org/wiki/Eric_S._Roberts)
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language)
- [Exception handling](https://en.wikipedia.org/wiki/Exception_handling)
- [Execution (computing)](https://en.wikipedia.org/wiki/Execution_(computing))
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [F Sharp (programming language)](https://en.wikipedia.org/wiki/F_Sharp_(programming_language))
- [Fixed-point combinator](https://en.wikipedia.org/wiki/Fixed-point_combinator)
- [Flow control (data)](https://en.wikipedia.org/wiki/Flow_control_(data))
- [Flowchart](https://en.wikipedia.org/wiki/Flowchart)
- [For loop](https://en.wikipedia.org/wiki/For_loop)
- [Foreach loop](https://en.wikipedia.org/wiki/Foreach_loop)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [Futures and promises](https://en.wikipedia.org/wiki/Futures_and_promises)
- [Goto](https://en.wikipedia.org/wiki/Goto)
- [Generator (computer programming)](https://en.wikipedia.org/wiki/Generator_(computer_programming))
- [Generator (computer programming)](https://en.wikipedia.org/wiki/Generator_(computer_programming))
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Glob (programming)](https://en.wikipedia.org/wiki/Glob_(programming))
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Goto](https://en.wikipedia.org/wiki/Goto)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [INTERCAL](https://en.wikipedia.org/wiki/INTERCAL)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Identifier](https://en.wikipedia.org/wiki/Identifier)
- [Imperative programming](https://en.wikipedia.org/wiki/Imperative_programming)
- [Indentation style](https://en.wikipedia.org/wiki/Indentation_style)
- [Infinite loop](https://en.wikipedia.org/wiki/Infinite_loop)
- [Input/output](https://en.wikipedia.org/wiki/Input/output)
- [Instruction set architecture](https://en.wikipedia.org/wiki/Instruction_set_architecture)
- [Interlisp](https://en.wikipedia.org/wiki/Interlisp)
- [Interrupt](https://en.wikipedia.org/wiki/Interrupt)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Java Modeling Language](https://en.wikipedia.org/wiki/Java_Modeling_Language)
- [Jeroo](https://en.wikipedia.org/wiki/Jeroo)
- [Reserved word](https://en.wikipedia.org/wiki/Reserved_word)
- [Label (computer science)](https://en.wikipedia.org/wiki/Label_(computer_science))
- [Label (computer science)](https://en.wikipedia.org/wiki/Label_(computer_science))
- [Language construct](https://en.wikipedia.org/wiki/Language_construct)
- [Scope (computer science)](https://en.wikipedia.org/wiki/Scope_(computer_science))
- [Line number](https://en.wikipedia.org/wiki/Line_number)
- [Lisp (programming language)](https://en.wikipedia.org/wiki/Lisp_(programming_language))
- [Lookup table](https://en.wikipedia.org/wiki/Lookup_table)
- [While loop](https://en.wikipedia.org/wiki/While_loop)
- [Loop invariant](https://en.wikipedia.org/wiki/Loop_invariant)
- [Loop variant](https://en.wikipedia.org/wiki/Loop_variant)
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [Machine code](https://en.wikipedia.org/wiki/Machine_code)
- [Event loop](https://en.wikipedia.org/wiki/Event_loop)
- [Mathias Payer](https://en.wikipedia.org/wiki/Mathias_Payer)
- [Modula-2](https://en.wikipedia.org/wiki/Modula-2)
- [Modular programming](https://en.wikipedia.org/wiki/Modular_programming)
- [Name binding](https://en.wikipedia.org/wiki/Name_binding)
- [Natural number](https://en.wikipedia.org/wiki/Natural_number)
- [Strict programming language](https://en.wikipedia.org/wiki/Strict_programming_language)
- [OCaml](https://en.wikipedia.org/wiki/OCaml)
- [Object Pascal](https://en.wikipedia.org/wiki/Object_Pascal)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [Off-side rule](https://en.wikipedia.org/wiki/Off-side_rule)
- [Ole-Johan Dahl](https://en.wikipedia.org/wiki/Ole-Johan_Dahl)
- [One-instruction set computer](https://en.wikipedia.org/wiki/One-instruction_set_computer)
- [Operator (computer programming)](https://en.wikipedia.org/wiki/Operator_(computer_programming))
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PL/I](https://en.wikipedia.org/wiki/PL/I)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [PowerShell](https://en.wikipedia.org/wiki/PowerShell)
- [Program counter](https://en.wikipedia.org/wiki/Program_counter)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Rebol](https://en.wikipedia.org/wiki/Rebol)
- [Recursion](https://en.wikipedia.org/wiki/Recursion)
- [Recursion (computer science)](https://en.wikipedia.org/wiki/Recursion_(computer_science))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [S-algol](https://en.wikipedia.org/wiki/S-algol)
- [S. Rao Kosaraju](https://en.wikipedia.org/wiki/S._Rao_Kosaraju)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scheduling (computing)](https://en.wikipedia.org/wiki/Scheduling_(computing))
- [Scheme (programming language)](https://en.wikipedia.org/wiki/Scheme_(programming_language))
- [Server (computing)](https://en.wikipedia.org/wiki/Server_(computing))
- [Shell script](https://en.wikipedia.org/wiki/Shell_script)
- [Signal (IPC)](https://en.wikipedia.org/wiki/Signal_(IPC))
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Software transactional memory](https://en.wikipedia.org/wiki/Software_transactional_memory)
- [Source code](https://en.wikipedia.org/wiki/Source_code)
- [Spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code)
- [Stack buffer overflow](https://en.wikipedia.org/wiki/Stack_buffer_overflow)
- [Standard ML](https://en.wikipedia.org/wiki/Standard_ML)
- [Standard Template Library](https://en.wikipedia.org/wiki/Standard_Template_Library)
- [State diagram](https://en.wikipedia.org/wiki/State_diagram)
- [Statement (computer science)](https://en.wikipedia.org/wiki/Statement_(computer_science))
- [Strict programming language](https://en.wikipedia.org/wiki/Strict_programming_language)
- [Structured program theorem](https://en.wikipedia.org/wiki/Structured_program_theorem)
- [Structured programming](https://en.wikipedia.org/wiki/Structured_programming)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Switch statement](https://en.wikipedia.org/wiki/Switch_statement)
- [Tail call](https://en.wikipedia.org/wiki/Tail_call)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Template (C++)](https://en.wikipedia.org/wiki/Template_(C%2B%2B))
- [Ternary operation](https://en.wikipedia.org/wiki/Ternary_operation)
- [Theoretical computer science](https://en.wikipedia.org/wiki/Theoretical_computer_science)
- [Type class](https://en.wikipedia.org/wiki/Type_class)
- [Unary function](https://en.wikipedia.org/wiki/Unary_function)
- [Virtual method table](https://en.wikipedia.org/wiki/Virtual_method_table)
- [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic)
- [Visual Basic (.NET)](https://en.wikipedia.org/wiki/Visual_Basic_(.NET))
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [While loop](https://en.wikipedia.org/wiki/While_loop)
- [Zahn's construct](https://en.wikipedia.org/wiki/Zahn%27s_construct)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Please clarify](https://en.wikipedia.org/wiki/Wikipedia:Please_clarify)
- [Template:Loop constructs](https://en.wikipedia.org/wiki/Template:Loop_constructs)
- [Template talk:Loop constructs](https://en.wikipedia.org/wiki/Template_talk:Loop_constructs)
- [Category:Articles with unsourced statements from July 2014](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_July_2014)
- [Category:Wikipedia articles needing clarification from November 2015](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_needing_clarification_from_November_2015)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:35:47.962883+00:00_