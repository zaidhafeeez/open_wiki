---
title: Infinite loop
url: https://en.wikipedia.org/wiki/Infinite_loop
language: en
categories: ["Category:Articles with example BASIC code", "Category:Articles with example C code", "Category:Articles with example Java code", "Category:Articles with example PHP code", "Category:Articles with example Python (programming language) code", "Category:Articles with example Rust code", "Category:Articles with short description", "Category:Control flow", "Category:Iteration in programming", "Category:Programming language comparisons", "Category:Recursion", "Category:Short description matches Wikidata", "Category:Software bugs"]
references: 0
last_modified: 2024-12-19T13:42:19Z
---

# Infinite loop

## Summary

In computer programming, an infinite loop (or endless loop) is a sequence of instructions that, as written, will continue endlessly, unless an external intervention occurs, such as turning off power via a switch or pulling a plug. It may be intentional.
There is no general algorithm to determine whether a computer program contains an infinite loop or not; this is the halting problem.

## Full Content

In computer programming, an infinite loop (or endless loop) is a sequence of instructions that, as written, will continue endlessly, unless an external intervention occurs, such as turning off power via a switch or pulling a plug. It may be intentional.
There is no general algorithm to determine whether a computer program contains an infinite loop or not; this is the halting problem.

Overview
This differs from "a type of computer program that runs the same instructions continuously until it is either stopped or interrupted". Consider the following pseudocode:

The same instructions were run continuously until it was stopped or interrupted . . . by the FALSE returned at some point by the function is_there_more_data.
By contrast, the following loop will not end by itself:

birds will alternate being 1 or 2, while fish will alternate being 2 or 1. The loop will not stop unless an external intervention occurs ("pull the plug").

Details
An infinite loop is a sequence of instructions in a computer program which loops endlessly, either due to the loop having no terminating condition, having one that can never be met, or one that causes the loop to start over. In older operating systems with cooperative multitasking, infinite loops normally caused the entire system to become unresponsive. With the now-prevalent preemptive multitasking model, infinite loops usually cause the program to consume all available processor time, but can usually be terminated by a user. Busy wait loops are also sometimes called "infinite loops". Infinite loops are one possible cause for a computer hanging or freezing; others include thrashing, deadlock, and access violations.

Intended vs unintended looping
Looping is repeating a set of instructions until a specific condition is met. An infinite loop occurs when the condition will never be met due to some inherent characteristic of the loop.

Intentional looping
There are a few situations when this is desired behavior. For example, the games on cartridge-based game consoles typically have no exit condition in their main loop, as there is no operating system for the program to exit to; the loop runs until the console is powered off.
Modern interactive computers require that the computer constantly be monitoring for user input or device activity, so at some fundamental level there is an infinite processing idle loop that must continue until the device is turned off or reset. In the Apollo Guidance Computer, for example, this outer loop was contained in the Exec program, and if the computer had absolutely no other work to do, it would loop run a dummy job that would simply turn off the "computer activity" indicator light.
Modern computers also typically do not halt the processor or motherboard circuit-driving clocks when they crash. Instead they fall back to an error condition displaying messages to the operator (such as the blue screen of death), and enter an infinite loop waiting for the user to either respond to a prompt to continue, or reset the device.

Spinlocks
Spinlocks are low-level synchronization mechanisms used in concurrent programming to protect shared resources. Unlike traditional locks that put a thread to sleep when it can't acquire the lock, spinlocks repeatedly "spin" in an infinite loop until the lock becomes available. This intentional infinite looping is a deliberate design choice aimed at minimizing the time a thread spends waiting for the lock and avoiding the overhead of higher level synchronisation mechanisms such as mutexes.

Multi-threading
In multi-threaded programs some threads can be executing inside infinite loops without causing the entire program to be stuck in an infinite loop. If the main thread exits, all threads of the process are forcefully stopped, thus all execution ends and the process/program terminates. The threads inside the infinite loops can perform "housekeeping" tasks or they can be in a blocked state waiting for input (from socket/queue) and resume execution every time input is received.

Unintentional looping
Most often, the term is used for those situations when this is not the intended result; that is, when this is a bug. Such errors are most common by novice programmers, but can be made by experienced programmers also, because their causes can be quite subtle.
One common cause, for example, is that a programmer intends to iterate over sequence of nodes in a data structure such as a linked list or tree, executing the loop code once for each node. Improperly formed links can create a reference loop in the data structure, where one node links to another that occurs earlier in the sequence. This makes part of the data structure into a ring, causing naive code to loop forever.
While most infinite loops can be found by close inspection of the code, there is no general method to determine whether a given program will ever halt or will run forever; this is the undecidability of the halting problem.

Interruption
As long as the system is responsive, infinite loops can often be interrupted by sending a signal to the process (such as SIGINT in Unix), or an interrupt to the processor, causing the current process to be aborted. This can be done in a task manager, in a terminal with the Control-C command, or by using the kill command or system call. However, this does not always work, as the process may not be responding to signals or the processor may be in an uninterruptible state, such as in the Cyrix coma bug (caused by overlapping uninterruptible instructions in an instruction pipeline). In some cases other signals such as SIGKILL can work, as they do not require the process to be responsive, while in other cases the loop cannot be terminated short of system shutdown.

Language support
Infinite loops can be implemented using various control flow constructs. Most commonly, in unstructured programming this is jump back up (goto), while in structured programming this is an indefinite loop (while loop) set to never end, either by omitting the condition or explicitly setting it to true, as while (true) ....
Some languages have special constructs for infinite loops, typically by omitting the condition from an indefinite loop. Examples include Ada (loop ... end loop), Fortran (DO ... END DO), Go (for { ... }), Ruby (loop do ... end), and Rust (loop { ... }).

Examples of intentional infinite loops
A simple example (in C):

The form for (;;) for an infinite loop is traditional, appearing in the standard reference The C Programming Language, and is often punningly pronounced "forever".
This is a loop that will print "Infinite Loop" without halting.
A similar example in 1980s-era BASIC:

A similar example in DOS batch files:

Here the loop is quite obvious, as the last line unconditionally sends execution back to the first.
An example in Java:

The while loop never terminates because its condition is always true.
An example in Bourne Again Shell:

An example in Rust:

Examples of unintentional infinite loops
Mathematical errors
Here is one example of an infinite loop in Visual Basic:

This creates a situation where x will never be greater than 5, since at the start of the loop code, x is assigned the value of 1 (regardless of any previous value) before it is changed to x + 1. Thus the loop will always result in x = 2 and will never break. This could be fixed by moving the x = 1 instruction outside the loop so that its initial value is set only once.
In some languages, programmer confusion about mathematical symbols may lead to an unintentional infinite loop. For example, here is a snippet in C:

The expected output is the numbers 0 through 9, with an interjected "a equals 5!" between 5 and 6. However, in the line "if (a = 5)" above, the = (assignment) operator was confused with the == (equality test) operator. Instead, this will assign the value of 5 to a at this point in the program. Thus, a will never be able to advance to 10, and this loop cannot terminate.

Rounding errors
Unexpected behavior in evaluating the terminating condition can also cause this problem. Here is an example in C:

On some systems, this loop will execute ten times as expected, but on other systems it will never terminate. The problem is that the loop terminating condition (x != 1.1) tests for exact equality of two floating point values, and the way floating point values are represented in many computers will make this test fail, because they cannot represent the value 0.1 exactly, thus introducing rounding errors on each increment (cf. box).
The same can happen in Python:

Because of the likelihood of tests for equality or not-equality failing unexpectedly, it is safer to use greater-than or less-than tests when dealing with floating-point values. For example, instead of testing whether x equals 1.1, one might test whether (x <= 1.0), or (x < 1.1), either of which would be certain to exit after a finite number of iterations. Another way to fix this particular example would be to use an integer as a loop index, counting the number of iterations that have been performed.
A similar problem occurs frequently in numerical analysis: in order to compute a certain result, an iteration is intended to be carried out until the error is smaller than a chosen tolerance. However, because of rounding errors during the iteration, the specified tolerance can never be reached, resulting in an infinite loop.

Multi-party loops
An infinite loop may be caused by several entities interacting. Consider a server that always replies with an error message if it does not understand the request. Even if there is no possibility for an infinite loop within the server itself, a system comprising two of them (A and B) may loop endlessly: if A receives a message of unknown type from B, then A replies with an error message to B; if B does not understand the error message, it replies to A with its own error message; if A does not understand the error message from B, it sends yet another error message, and so on.
One common example of such situation is an email loop. An example of an email loop is if someone receives mail from a no reply inbox, but their auto-response is on. They will reply to the no reply inbox, triggering the "this is a no reply inbox" response. This will be sent to the user, who then sends an auto reply to the no-reply inbox, and so on and so forth.

Pseudo-infinite loops
A pseudo-infinite loop is a loop that appears infinite but is really just a very long loop.

Very large numbers
An example in bash:

Impossible termination condition
An example for loop in C:

It appears that this will go on indefinitely, but in fact the value of i will eventually reach the maximum value storable in an unsigned int and adding 1 to that number will wrap-around to 0, breaking the loop. The actual limit of i depends on the details of the system and compiler used. With arbitrary-precision arithmetic, this loop would continue until the computer's memory could no longer hold i. If i was a signed integer, rather than an unsigned integer, overflow would be undefined. In this case, the compiler could optimize the code into an infinite loop.

Infinite recursion
Infinite recursion is a special case of an infinite loop that is caused by recursion. 
The following example in Visual Basic for Applications (VBA) returns a stack overflow error:

Break statement
A "while (true)" loop looks infinite at first glance, but there may be a way to escape the loop through a break statement or return statement.
Example in PHP:

Alderson loop
Alderson loop is a rare slang or jargon term for an infinite loop where there is an exit condition available, but inaccessible in an implementation of the code, typically due to a programmer error. These are most common and visible while debugging user interface code.
A C-like pseudocode example of an Alderson loop, where the program is supposed to sum numbers given by the user until zero is given, but where the wrong operator is used:

The term allegedly received its name from a programmer (last name Alderson) who in 1996 had coded a modal dialog box in Microsoft Access without either an OK or Cancel button, thereby disabling the entire program whenever the box came up.

See also
Cycle detection
Divergence (computer science)
Fork bomb (an infinite loop is one of two key components)
Infinite regress

References
External links
Make an infinite loop in several languages, on programming-idioms.org.
