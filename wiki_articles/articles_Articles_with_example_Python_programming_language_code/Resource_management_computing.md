# Resource management (computing)

## Metadata
- **Last Updated:** 2024-12-06 05:14:33 UTC
- **Original Article:** [Resource management (computing)](https://en.wikipedia.org/wiki/Resource_management_(computing))
- **Language:** en
- **Page ID:** 41836840

## Summary
In computer programming, resource management refers to techniques for managing resources (components with limited availability).
Computer programs may manage their own resources by using features exposed by programming languages (Elder, Jackson & Liblit (2008) is a survey article contrasting different approaches), or may elect to manage them by a host – an operating system or virtual machine – or another program.
Host-based management is known as resource tracking, and consists of cleaning up resource leaks: terminating access to resources that have been acquired but not released after use. This is known as reclaiming resources, and is analogous to garbage collection for memory. On many systems, the operating system reclaims resources after the process makes the exit system call.

## Categories
This article belongs to the following categories:

- Category:All articles with specifically marked weasel-worded phrases
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with specifically marked weasel-worded phrases from November 2016
- Category:CS1 errors: external links
- Category:CS1 maint: postscript
- Category:Programming constructs
- Category:Short description is different from Wikidata

## Table of Contents

- Controlling access
- Memory management
- Lexical management and explicit management
- Basic techniques
- Approaches
- See also
- References
- Further reading
- External links

## Content

In computer programming, resource management refers to techniques for managing resources (components with limited availability).
Computer programs may manage their own resources by using features exposed by programming languages (Elder, Jackson & Liblit (2008) is a survey article contrasting different approaches), or may elect to manage them by a host – an operating system or virtual machine – or another program.
Host-based management is known as resource tracking, and consists of cleaning up resource leaks: terminating access to resources that have been acquired but not released after use. This is known as reclaiming resources, and is analogous to garbage collection for memory. On many systems, the operating system reclaims resources after the process makes the exit system call.

Controlling access
The omission of releasing a resource when a program has finished using it is known as a resource leak, and is an issue in sequential computing. Multiple processes wish to access a limited resource can be an issue in concurrent computing, and is known as resource contention.
Resource management seeks to control access in order to prevent both of these situations.

Resource leak
Formally, resource management (preventing resource leaks) consists of ensuring that a resource is released if and only if it is successfully acquired. This general problem can be abstracted as "before, body, and after" code, which normally are executed in this order, with the condition that the after code is called if and only if the before code successfully completes, regardless of whether the body code executes successfully or not. This is also known as execute around or a code sandwich, and occurs in various other contexts, such as a temporary change of program state, or tracing entry and exit into a subroutine. However, resource management is the most commonly cited application. In aspect-oriented programming, such execute around logic is a form of advice.
In the terminology of control flow analysis, resource release must postdominate successful resource acquisition; failure to ensure this is a bug, and a code path that violates this condition causes a resource leak. Resource leaks are often minor problems, generally not crashing the program, but instead causing some slowdown to the program or the overall system. However, they may cause crashes – either the program itself or other programs – due to resource exhaustion: if the system runs out of resources, acquisition requests fail. This can present a security bug if an attack can cause resource exhaustion. Resource leaks may happen under regular program flow – such as simply forgetting to release a resource – or only in exceptional circumstances, such as when a resource is not released if there is an exception in another part of the program. Resource leaks are very frequently caused by early exit from a subroutine, either by a return statement, or an exception raised either by the subroutine itself, or a deeper subroutine that it calls. While resource release due to return statements can be handled by carefully releasing within the subroutine before the return, exceptions cannot be handled without some additional language facility that guarantees that release code is executed.
More subtly, successful resource acquisition must dominate resource release, as otherwise the code will try to release a resource it has not acquired. The consequences of such an incorrect release range from being silently ignored to crashing the program or unpredictable behavior. These bugs generally manifest rarely, as they require resource allocation to first fail, which is generally an exceptional case. Further, the consequences may not be serious, as the program may already be crashing due to failure to acquire an essential resource. However, these can prevent recovery from the failure, or turn an orderly shutdown into a disorderly shutdown. This condition is generally ensured by first checking that the resource was successfully acquired before releasing it, either by having a boolean variable to record "successfully acquired" – which lacks atomicity if the resource is acquired but the flag variable fails to be updated, or conversely – or by the handle to the resource being a nullable type, where "null" indicates "not successfully acquired", which ensures atomicity.

Resource contention
In computer science, resource contention refers to a conflict that arises when multiple entities attempt to access a shared resource, like random access memory, disk storage, cache memory, internal buses, or external network devices.
{{expand section|daresource contention

Memory management
Memory can be treated as a resource, but memory management is usually considered separately, primarily because memory allocation and deallocation is significantly more frequent than acquisition and release of other resources, such as file handles. Memory managed by an external system has similarities to both (internal) memory management (since it is memory) and resource management (since it is managed by an external system). Examples include memory managed via native code and used from Java (via Java Native Interface); and objects in the Document Object Model (DOM), used from JavaScript. In both these cases, the memory manager (garbage collector) of the runtime environment (virtual machine) is unable to manage the external memory (there is no shared memory management), and thus the external memory is treated as a resource, and managed analogously. However, cycles between systems (JavaScript referring to the DOM, referring back to JavaScript) can make management difficult or impossible.

Lexical management and explicit management
A key distinction in resource management within a program is between lexical management and explicit management – whether a resource can be handled as having a lexical scope, such as a stack variable (lifetime is restricted to a single lexical scope, being acquired on entry to or within a particular scope, and released when execution exits that scope), or whether a resource must be explicitly allocated and released, such as a resource acquired within a function and then returned from it, which must then be released outside of the acquiring function.  Lexical management, when applicable, allows a better separation of concerns and is less error-prone.

Basic techniques
The basic approach to resource management is to acquire a resource, do something with it, then release it, yielding code of the form (illustrated with opening a file in Python):

This is correct if the intervening ... code does not contain an early exit (return), the language does not have exceptions, and open is guaranteed to succeed. However, it causes a resource leak if there is a return or exception, and causes an incorrect release of unacquired resource if open can fail.
There are two more fundamental problems: the acquisition-release pair is not adjacent (the release code must be written far from the acquisition code), and resource management is not encapsulated – the programmer must manually ensure that they are always paired. In combination, these mean that acquisition and release must be explicitly paired, but cannot be placed together, thus making it easy for these to not be paired correctly.
The resource leak can be resolved in languages that support a finally construction (like Python) by placing the body in a try clause, and the release in a finally clause:

This ensures correct release even if there is a return within the body or an exception thrown. Further, note that the acquisition occurs before the try clause, ensuring that the finally clause is only executed if the open code succeeds (without throwing an exception), assuming that "no exception" means "success" (as is the case for open in Python). If resource acquisition can fail without throwing an exception, such as by returning a form of null, it must also be checked before release, such as:

While this ensures correct resource management, it fails to provide adjacency or encapsulation. In many languages there are mechanisms that provide encapsulation, such as the with statement in Python:

The above techniques – unwind protection (finally) and some form of encapsulation – are the most common approach to resource management, found in various forms in C#, Common Lisp, Java, Python, Ruby, Scheme, and Smalltalk, among others; they date to the late 1970s in the NIL dialect of Lisp; see Exception handling § History. There are many variations in the implementation, and there are also significantly different approaches.

Approaches
Unwind protection
The most common approach to resource management across languages is to use unwind protection, which is called when execution exits a scope – by execution running off the end of the block, returning from within the block, or an exception being thrown. This works for stack-managed resources, and is implemented in many languages, including C#, Common Lisp, Java, Python, Ruby, and Scheme. The main problems with this approach is that the release code (most commonly in a finally clause) may be very distant from the acquisition code (it lacks adjacency), and that the acquisition and release code must always be paired by the caller (it lacks encapsulation). These can be remedied either functionally, by using closures/callbacks/coroutines (Common Lisp, Ruby, Scheme), or by using an object that handles both the acquisition and release, and adding a language construct to call these methods when control enters and exits a scope (C# using, Java try-with-resources, Python with); see below.
An alternative, more imperative approach, is to write asynchronous code in direct style: acquire a resource, and then in the next line have a deferred release, which is called when the scope is exited – synchronous acquisition followed by asynchronous release. This originated in C++ as the ScopeGuard class, by Andrei Alexandrescu and Petru Marginean in 2000,
 with improvements by Joshua Lehrer, and has direct language support in D via the scope keyword (ScopeGuardStatement), where it is one approach to exception safety, in addition to RAII (see below). It has also been included in Go, as the defer statement. This approach lacks encapsulation – one must explicitly match acquisition and release – but avoids having to create an object for each resource (code-wise, avoid writing a class for each type of resource).

Object-oriented programming
In object-oriented programming, resources are encapsulated within objects that use them, such as a file object having a field whose value is a file descriptor (or more general file handle). This allows the object to use and manage the resource without users of the object needing to do so. However, there is a wide variety of ways that objects and resources can be related.
Firstly, there is the question of ownership: does an object have a resource?

Objects can own resources (via object composition, a strong "has a" relationship).
Objects can view resources (via object aggregation, a weak "has a" relationship).
Objects can communicate with other objects that have resources (via Association).
Objects that have a resource can acquire and release it in different ways, at different points during the object lifetime; these occur in pairs, but in practice they are often not used symmetrically (see below):

Acquire/release while the object is valid, via (instance) methods such as open or dispose.
Acquire/release during object creation/destruction (in the initializer and finalizer).
Neither acquire nor release the resource, instead simply having a view or reference to a resource managed externally to the object, as in dependency injection; concretely, an object that has a resource (or can communicate with one that does) is passed in as an argument to a method or constructor.
Most common is to acquire a resource during object creation, and then explicitly release it via an instance method, commonly called dispose. This is analogous to traditional file management (acquire during open, release by explicit close), and is known as the dispose pattern. This is the basic approach used in several major modern object-oriented languages, including Java, C# and Python, and these languages have additional constructs to automate resource management. However, even in these languages, more complex object relationships result in more complex resource management, as discussed below.

RAII
A natural approach is to make holding a resource be a class invariant: resources are acquired during object creation (specifically initialization), and released during object destruction (specifically finalization). This is known as Resource Acquisition Is Initialization (RAII), and ties resource management to object lifetime, ensuring that live objects have all necessary resources. Other approaches do not make holding the resource a class invariant, and thus objects may not have necessary resources (because they've not been acquired yet, have already been released, or are being managed externally), resulting in errors such as trying to read from a closed file. This approach ties resource management to memory management (specifically object management), so if there are no memory leaks (no object leaks), there are no resource leaks. RAII works naturally for heap-managed resources, not only stack-managed resources, and is composable: resources held by objects in arbitrarily complicated relationships (a complicated object graph) are released transparently simply by object destruction (so long as this is done properly!).
RAII is the standard resource management approach in C++, but is little-used outside C++, despite its appeal, because it works poorly with modern automatic memory management, specifically tracing garbage collection: RAII ties resource management to memory management, but these have significant differences. Firstly, because resources are expensive, it is desirable to release them promptly, so objects holding resources should be destroyed as soon as they become garbage (are no longer in use). Object destruction is prompt in deterministic memory management, such as in C++ (stack-allocated objects are destroyed on stack unwind, heap-allocated objects are destroyed manually via calling delete or automatically using unique_ptr) or in deterministic reference-counting (where objects are destroyed immediately when their reference count falls to 0), and thus RAII works well in these situations. However, most modern automatic memory management is non-deterministic, making no guarantees that objects will be destroyed promptly or even at all! This is because it is cheaper to leave some garbage allocated than to precisely collect each object immediately on its becoming garbage. Secondly, releasing resources during object destruction means that an object must have a finalizer (in deterministic memory management known as a destructor) – the object cannot simply be deallocated – which significantly complicates and slows garbage collection.

Complex relationships
When multiple objects rely on a single resource, resource management can be complicated.
A fundamental question is whether a "has a" relationship is one of owning another object (object composition), or viewing another object (object aggregation). A common case is when one two objects are chained, as in pipe and filter pattern, the delegation pattern, the decorator pattern, or the adapter pattern. If the second object (which is not used directly) holds a resource, is the first object (which is used directly) responsible for managing the resource? This is generally answered identically to whether the first object owns the second object: if so, then the owning object is also responsible for resource management ("having a resource" is transitive), while if not, then it is not. Further, a single object may "have" several other objects, owning some and viewing others.
Both cases are commonly found, and conventions differ. Having objects that use resources indirectly be responsible for the resource (composition) provides encapsulation (one only needs the object that clients use, without separate objects for the resources), but results in considerable complexity, particularly when a resource is shared by multiple objects or objects have complex relationships. If only the object that directly uses the resource is responsible for the resource (aggregation), relationships between other objects that use the resources can be ignored, but there is no encapsulation (beyond the directly using object): the resource must be managed directly, and might not be available to the indirectly using object (if it has been released separately).
Implementation-wise, in object composition, if using the dispose pattern, the owning object thus will also have a dispose method, which in turn calls the dispose methods of owned objects that must be disposed; in RAII this is handled automatically (so long as owned objects are themselves automatically destroyed: in C++ if they are a value or a unique_ptr, but not a raw pointer: see pointer ownership). In object aggregation, nothing needs to be done by the viewing object, as it is not responsible for the resource.
Both are commonly found. For example, in the Java Class Library, Reader#close() closes the underlying stream, and these can be chained. For example, a BufferedReader may contain a InputStreamReader, which in turn contains a FileInputStream, and calling close on the BufferedReader in turn closes the InputStreamReader, which in turn closes the FileInputStream, which in turn releases the system file resource. Indeed, the object that directly uses the resource can even be anonymous, thanks to encapsulation:

However, it is also possible to manage only the object that directly uses the resource, and not use resource management on wrapper objects:

By contrast, in Python, a csv.reader does not own the file that it is reading, so there is no need (and it is not possible) to close the reader, and instead the file itself must be closed.

In .NET, convention is to only have direct user of resources be responsible: "You should implement IDisposable only if your type uses unmanaged resources directly."
In case of a more complicated object graph, such as multiple objects sharing a resource, or cycles between objects that hold resources, proper resource management can be quite complicated, and exactly the same issues arise as in object finalization (via destructors or finalizers); for example, the lapsed listener problem can occur and cause resource leaks if using the
observer pattern (and observers hold resources). Various mechanisms exist to allow greater control of resource management. For example, in the Google Closure Library, the goog.Disposable class provides a registerDisposable method to register other objects to be disposed with this object, together with various lower-level instance and class methods to manage disposal.

Structured programming
In structured programming, stack resource management is done simply by nesting code sufficiently to handle all cases. This requires only a single return at the end of the code, and can result in heavily nested code if many resources must be acquired, which is considered an anti-pattern by some – the Arrow Anti Pattern, due to the triangular shape from the successive nesting.

Cleanup clause
One other approach, which allows early return but consolidates cleanup in one place, is to have a single exit return of a function, preceded by cleanup code, and to use goto to jump to the cleanup before exit. This is infrequently seen in modern code, but occurs in some uses of C.

See also
Memory management
Pool (computer science)

References
Further reading
DG Update: Dispose, Finalization, and Resource Management, Joe Duffy

External links
Deterministic Resource Management, WikiWikiWeb

## Archive Info
- **Archived on:** 2024-12-15 20:38:43 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 19940 bytes
- **Word Count:** 3068 words
