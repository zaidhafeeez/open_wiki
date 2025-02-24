---
title: Stack trace
url: https://en.wikipedia.org/wiki/Stack_trace
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Debugging", "Category:Short description is different from Wikidata"]
references: 0
last_modified: 2024-12-19T13:45:06Z
---

# Stack trace

## Summary

In computing, a stack trace (also called stack backtrace or stack traceback) is a report of the active stack frames at a certain point in time during the execution of a program. When a program is run, memory is often dynamically allocated in two places: the stack and the heap. Memory is continuously allocated on a stack but not on a heap, thus reflective of their names. Stack also refers to a programming construct, thus to differentiate it, this stack is referred to as the program's function cal

## Full Content

In computing, a stack trace (also called stack backtrace or stack traceback) is a report of the active stack frames at a certain point in time during the execution of a program. When a program is run, memory is often dynamically allocated in two places: the stack and the heap. Memory is continuously allocated on a stack but not on a heap, thus reflective of their names. Stack also refers to a programming construct, thus to differentiate it, this stack is referred to as the program's function call stack. Technically, once a block of memory has been allocated on the stack, it cannot be easily removed as there can be other blocks of memory that were allocated before it. Each time a function is called in a program, a block of memory called an activation record is allocated on top of the call stack. Generally, the activation record stores the function's arguments and local variables. What exactly it contains and how it's laid out is determined by the calling convention.
Programmers commonly use stack tracing during interactive and post-mortem debugging. End-users may see a stack trace displayed as part of an error message, which the user can then report to a programmer.
A stack trace allows tracking the sequence of nested functions called - up to the point where the stack trace is generated. In a post-mortem scenario this extends up to the function where the failure occurred (but was not necessarily caused). Sibling calls do not appear in a stack trace.

Language support
Many programming languages, including Java and C#, have built-in support for retrieving the current stack trace via system calls. Before std::stacktrace was added in standard library as a container for std::stacktrace_entry, pre-C++23 has no built-in support for doing this, but C++ users can retrieve stack traces with (for example) the stacktrace library. In JavaScript, exceptions hold a stack property that contain the stack from the place where it was thrown.

Python
As an example, the following Python program contains an error.

Running the program under the standard Python interpreter produces the following error message.

The stack trace shows where the error occurs, namely in the c function. It also shows that the c function was called by b, which was called by a, which was in turn called by the code on line 15 (the last line) of the program. The activation records for each of these three functions would be arranged in a stack such that the a function would occupy the bottom of the stack and the c function would occupy the top of the stack.

Java
In Java, stack traces can be dumped manually with Thread.dumpStack() Take the following input:

The exception lists functions in descending order, so the most-inner call is first.

C and C++
Both C and C++ (pre-C++23) do not have native support for obtaining stack traces, but libraries such as glibc and boost provide this functionality. In these languages, some compiler optimizations may interfere with the call stack information that can be recovered at runtime. For instance, inlining can cause missing stack frames, tail call optimizations can replace one stack frame with another, and frame pointer elimination can prevent call stack analysis tools from correctly interpreting the contents of the call stack.
For example, glibc's backtrace() function returns an output with the program function and memory address.

As of C++23, stack traces can be dumped manually by printing the value returned by static member function std::stacktrace::current():

Rust
Rust has two types of errors. Functions that use the panic macro are "unrecoverable" and the current thread will become poisoned experiencing stack unwinding. Functions that return a std::result::Result are "recoverable" and can be handled gracefully. However, recoverable errors cannot generate a stack trace as they are manually added and not a result of a runtime error.
As of June 2021, Rust has experimental support for stack traces on unrecoverable errors. Rust supports printing to stderr when a thread panics, but it must be enabled by setting the RUST_BACKTRACE environment variable.
When enabled, such backtraces look similar to below, with the most recent call first.

See also
Tail call
Context (computing)
Stack overflow
Exception handling
Call stack


== References ==
