# Tracing just-in-time compilation

## Metadata
- **Last Updated:** 2024-12-03 07:33:13 UTC
- **Original Article:** [Tracing just-in-time compilation](https://en.wikipedia.org/wiki/Tracing_just-in-time_compilation)
- **Language:** en
- **Page ID:** 35604013

## Summary
Tracing just-in-time compilation is a technique used by virtual machines to optimize the execution of a program at runtime. This is done by recording a linear sequence of frequently executed operations, compiling them to native machine code and executing them. This is opposed to traditional just-in-time (JIT) compilers that work on a per-method basis.

## Categories
This article belongs to the following categories:

- Category:All articles with unsourced statements
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from May 2018
- Category:Compiler construction
- Category:Short description matches Wikidata
- Category:Software optimization

## Table of Contents

- Overview
- Technical details
- History
- Example of a trace
- See also
- References
- External links

## Content

Tracing just-in-time compilation is a technique used by virtual machines to optimize the execution of a program at runtime. This is done by recording a linear sequence of frequently executed operations, compiling them to native machine code and executing them. This is opposed to traditional just-in-time (JIT) compilers that work on a per-method basis.

Overview
Just-in-time compilation is a technique to increase execution speed of programs by compiling parts of a program to machine code at runtime. One way to categorize different JIT compilers is by their compilation scope. Whereas method-based JIT compilers translate one method at a time to machine code, tracing JITs use frequently executed loops as their unit of compilation.
Tracing JITs are based on the assumptions that programs
spend most of their time in some loops of the program ("hot loops") and subsequent loop iterations often take similar paths. Virtual machines that have a tracing JIT are often mixed-mode execution environments, meaning that they have either an interpreter or a method compiler in addition to the tracing JIT.

Technical details
A tracing JIT compiler goes through various phases at runtime. First, profiling information for loops is collected. After a hot loop has been identified, a special tracing phase is entered, which records all executed operations of that loop. This sequence of operations is called a trace. The trace is then optimized and compiled to machine code. When this loop is executed again, the compiled trace is called instead of the program counterpart.
These steps are explained in detail in the following:

Profiling phase
The goal of profiling is to identify hot loops. This is often done by counting the number of iterations for every loop. After the count of a loop exceeds a certain threshold, the loop is considered to be hot, and tracing phase is entered.

Tracing phase
In the tracing phase the execution of the loop proceeds normally, but in addition every executed operation is recorded into a trace. The recorded operations are typically stored in trace tree, often in an intermediate representation (IR). Tracing follows function calls, which leads to them being inlined into the trace. Tracing continues until the loop reaches its end and jumps back to the start.
Since the trace is recorded by following one concrete execution path of the loop, later executions of that trace can diverge from that path. To identify the places where that can happen, special guard instructions are inserted into the trace. One example for such a place are if statements. The guard is a quick check to determine whether the original condition is still true. If a guard fails, the execution of the trace is aborted.
Since tracing is done during execution, the trace can be made to contain runtime information (e.g. type information). This information can later be used in the optimization phase to increase code efficiency.

Optimization and code-generation phase
Traces are easy to optimize, since they represent only one execution path, which means that no control flow exists and needs no handling. Typical optimizations include common-subexpression elimination, dead code elimination, register allocation, invariant-code motion, constant folding, and escape analysis.
After the optimization, the trace is turned into machine code. Similarly to optimization, this is easy due to the linear nature of traces.

Execution
After the trace has been compiled to machine code, it can be executed in subsequent iterations of the loop. Trace execution continues until a guard fails.

History
Whereas the idea of JITs reaches back to the 1960s, tracing JITs have become used more often only recently. The first mention of an idea that is similar to today's idea of tracing JITs was in 1970. It was observed that compiled code could be derived from an interpreter at run-time by simply storing the actions performed during interpretation.
The first implementation of tracing is Dynamo, "a software dynamic optimization system that is capable of transparently improving the performance of a native instruction stream as it executes on the processor". To do this, the native instruction stream is interpreted until a "hot" instruction sequence is found. For this sequence an optimized version is generated, cached and executed.
Dynamo was later extended to DynamoRIO. One DynamoRIO-based project was a framework for interpreter construction that combines tracing and partial evaluation. It was used to "dynamically remove interpreter overhead from language implementations".
In 2006, HotpathVM, the first tracing JIT compiler for a high-level language was developed. This VM was capable of dynamically identifying frequently executed bytecode instructions, which are traced and then compiled to machine code using static single assignment (SSA) construction. The motivation for HotpathVM was to have an efficient JVM for resource constrained mobile devices.
Another example of a tracing JIT is TraceMonkey, one of Mozilla’s JavaScript implementations for Firefox (2009). TraceMonkey compiles frequently executed loop traces in the dynamic language JavaScript at run-time and specializes the generated code for the actual dynamic types occurring on each path.
Another project that utilizes tracing JITs is PyPy. It enables the use of tracing JITs for language implementations that were written with PyPy's translation toolchain, thus improving the performance of any program that is executed using that interpreter. This is possible by tracing the interpreter itself, instead of the program that is executed by the interpreter.
Tracing JITs have also been explored by Microsoft in the SPUR project for their Common Intermediate Language (CIL). SPUR is a generic tracer for CIL, which can also be used to trace through a JavaScript implementation.

Example of a trace
Consider the following Python program that computes a sum of squares of successive whole numbers until that sum exceeds 100000:

A trace for this program could look something like this:

Note how the function call to square is inlined into the trace and how the if statement is turned into a guard_false.

See also
Code generation
Dalvik
HotSpot
Interpreter
Profile-guided optimization
RPython
Semantic dictionary encoding

References
External links
Official website of LuaJIT

## Archive Info
- **Archived on:** 2024-12-15 21:06:25 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 6343 bytes
- **Word Count:** 984 words
