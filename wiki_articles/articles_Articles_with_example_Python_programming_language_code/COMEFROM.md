# COMEFROM

## Metadata
- **Last Updated:** 2024-12-15 06:12:56 UTC
- **Original Article:** [COMEFROM](https://en.wikipedia.org/wiki/COMEFROM)
- **Language:** en
- **Page ID:** 994284

## Summary
In computer programming, COMEFROM (or COME FROM) is an obscure control flow structure used in some programming languages, originally as a joke. COMEFROM is the inverse of GOTO in that it can take the execution state from any arbitrary point in code to a COMEFROM statement.
The point in code where the state transfer happens is usually given as a parameter to COMEFROM. Whether the transfer happens before or after the instruction at the specified transfer point depends on the language used. Depending on the language used, multiple COMEFROMs referencing the same departure point may be invalid, be non-deterministic, be executed in some sort of defined priority, or even induce parallel or otherwise concurrent execution as seen in Threaded Intercal.
A simple example of a "COMEFROM x" statement is a label x (which does not need to be physically located anywhere near its corresponding COMEFROM) that acts as a "trap door". When code execution reaches the label, control gets passed to the statement following the COMEFROM. This may also be conditional, passing control only if a condition is satisfied, analogous to a GOTO within an IF statement. The primary difference from GOTO is that GOTO only depends on the local structure of the code, while COMEFROM depends on the global structure – a GOTO transfers control when it reaches a line with a GOTO statement, while COMEFROM requires scanning the entire program or scope to see if any COMEFROM statements are in scope for the line, and then verifying if a condition is hit. The effect of this is primarily to make debugging (and understanding the control flow of the program) extremely difficult, since there is no indication near the line or label in question that control will mysteriously jump to another point of the program – one must study the entire program to see if any COMEFROM statements reference that line or label.
Debugger hooks can be used to implement a COMEFROM statement, as in the humorous Python goto module; see below. This also can be implemented with the gcc feature "asm goto" as used by the Linux kernel configuration option CONFIG_JUMP_LABEL. A no-op has its location stored, to be replaced by a jump to an executable fragment that at its end returns to the instruction after the no-op.

## Categories
This article belongs to the following categories:

- Category:All articles with unsourced statements
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from September 2019
- Category:Computer humour
- Category:Control flow
- Category:Short description matches Wikidata

## Table of Contents

- History
- Practical uses
- See also
- References
- External links

## Content

In computer programming, COMEFROM (or COME FROM) is an obscure control flow structure used in some programming languages, originally as a joke. COMEFROM is the inverse of GOTO in that it can take the execution state from any arbitrary point in code to a COMEFROM statement.
The point in code where the state transfer happens is usually given as a parameter to COMEFROM. Whether the transfer happens before or after the instruction at the specified transfer point depends on the language used. Depending on the language used, multiple COMEFROMs referencing the same departure point may be invalid, be non-deterministic, be executed in some sort of defined priority, or even induce parallel or otherwise concurrent execution as seen in Threaded Intercal.
A simple example of a "COMEFROM x" statement is a label x (which does not need to be physically located anywhere near its corresponding COMEFROM) that acts as a "trap door". When code execution reaches the label, control gets passed to the statement following the COMEFROM. This may also be conditional, passing control only if a condition is satisfied, analogous to a GOTO within an IF statement. The primary difference from GOTO is that GOTO only depends on the local structure of the code, while COMEFROM depends on the global structure – a GOTO transfers control when it reaches a line with a GOTO statement, while COMEFROM requires scanning the entire program or scope to see if any COMEFROM statements are in scope for the line, and then verifying if a condition is hit. The effect of this is primarily to make debugging (and understanding the control flow of the program) extremely difficult, since there is no indication near the line or label in question that control will mysteriously jump to another point of the program – one must study the entire program to see if any COMEFROM statements reference that line or label.
Debugger hooks can be used to implement a COMEFROM statement, as in the humorous Python goto module; see below. This also can be implemented with the gcc feature "asm goto" as used by the Linux kernel configuration option CONFIG_JUMP_LABEL. A no-op has its location stored, to be replaced by a jump to an executable fragment that at its end returns to the instruction after the no-op.

History
COMEFROM was initially seen in lists of joke assembly language instructions (as 'CMFRM'). It was elaborated upon in a Datamation article by R. Lawrence Clark in 1973, written in response to Edsger Dijkstra's letter Go To Statement Considered Harmful. COMEFROM was eventually implemented in the C-INTERCAL variant of the esoteric programming language INTERCAL along with the even more obscure 'computed COMEFROM'. There were also Fortran proposals for 'assigned COME FROM' and a 'DONT' keyword (to complement the existing 'DO' loop).
On 1 April 2004, Richie Hindle published an implementation of both GOTO and COMEFROM for the Python programming language. Despite being released on April Fools' Day and not being intended for serious use, the syntax is valid and the implementation fully works.

Practical uses
Examples
The following is an example of a program in a hypothetical BASIC dialect with "COMEFROM" instead of "GOTO".

This program (hypothetically) works by asking the user for their name, greeting them with the same name, and continuing all over again. The instruction "REM" on line 40 is simply a NOP (in this case, a REMark or comment) — the "COMEFROM" statement on line 10 causes a branch back to that line when execution reaches line 40, regardless of its contents.
A fully runnable example in Python with the joke goto module installed (which uses debugger hooks to control program execution) looks like this:

This is an implementation in Ruby of the Intercal COME FROM statement.

OS/360 Fortran G
The OS/360 Fortran G compiler has a debug packet feature. Its "AT" statement is similar to COMEFROM in that it hands the control flow over to the debug block. Breakpoints in general are similar.

Example 1: the values of SOLON, GFAR, and EWELL are examined as they were at the completion of statement 10.  The AT statement indicates statement 11.

Example 2: all the values of STOCK are displayed when statement 35 is encountered.

Example 3: tracing begins at statement 10, at statement 20, tracing stops while the loop is executed, and resumes after the loop.  Tracing stops just before statement 30 is executed.

See also
F. X. Reid, an expert on the semantics of COMEFROM
Action at a distance
INTERCAL
Serious programming contrivances involving ideas resembling COMEFROM:

Pointcut in aspect-oriented programming
Continuation
Database triggers
Observer pattern
Event-driven programming
Webhook
Goto/From signal routing blocks in MATLAB Simulink

References
External links
COMEFROM Information Page
Datamation Article
Joke Assembler Instruction List Including CMFRM
comefrom support for Perl

## Archive Info
- **Archived on:** 2024-12-15 21:03:56 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 4895 bytes
- **Word Count:** 789 words
