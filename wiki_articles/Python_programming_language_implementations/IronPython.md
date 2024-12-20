---
title: IronPython
url: https://en.wikipedia.org/wiki/IronPython
language: en
categories: ["Category:.NET programming languages", "Category:2006 software", "Category:All articles lacking reliable references", "Category:All articles to be expanded", "Category:All articles with unsourced statements", "Category:Articles lacking reliable references from January 2013", "Category:Articles to be expanded from July 2012", "Category:Articles with short description", "Category:Articles with unsourced statements from August 2009", "Category:Free software programmed in C Sharp", "Category:Microsoft free software", "Category:Microsoft programming languages", "Category:Python (programming language) implementations", "Category:Python (programming language) libraries", "Category:Short description is different from Wikidata", "Category:Software using the Apache license"]
references: 0
last_modified: 2024-12-19T13:46:44Z
---

# IronPython

## Summary

IronPython is an implementation of the Python programming language targeting the .NET and Mono frameworks. The project is currently maintained by a group of volunteers at GitHub. It is free and open-source software, and can be implemented with Python Tools for Visual Studio, which is a free and open-source extension for Microsoft's Visual Studio IDE.
IronPython is written entirely in C#, although some of its code is automatically generated by a code generator written in Python.
IronPython is imp

## Full Content

IronPython is an implementation of the Python programming language targeting the .NET and Mono frameworks. The project is currently maintained by a group of volunteers at GitHub. It is free and open-source software, and can be implemented with Python Tools for Visual Studio, which is a free and open-source extension for Microsoft's Visual Studio IDE.
IronPython is written entirely in C#, although some of its code is automatically generated by a code generator written in Python.
IronPython is implemented on top of the Dynamic Language Runtime (DLR), a library running on top of the Common Language Infrastructure that provides dynamic typing and dynamic method dispatch, among other things, for dynamic languages. The DLR is part of the .NET Framework 4.0 and is also a part of Mono since version 2.4 from 2009. The DLR can also be used as a library on older CLI implementations.

Status and roadmap
Jim Hugunin created the project and actively contributed to it up until Version 1.0 which was released on September 5, 2006. IronPython 2.0 was released on December 10, 2008. After version 1.0 it was maintained by a small team at Microsoft until the 2.7 Beta 1 release. Microsoft abandoned IronPython (and its sister project IronRuby) in late 2010, after which Hugunin left to work at Google. The project is currently maintained by a group of volunteers at GitHub.

Release 2.0, released on December 10, 2008, and updated as 2.0.3 on October 23, 2009, targets CPython 2.5. IronPython 2.0.3 is only compatible up to .NET Framework 3.5.
Release 2.6, released on December 11, 2009, and updated on April 12, 2010, targets CPython 2.6. IronPython 2.6.1 versions is binary compatible only with .NET Framework 4.0. IronPython 2.6.1 must be compiled from sources to run on .NET Framework 3.5. IronPython 2.6.2, released on October 21, 2010, is binary compatible with both .NET Framework 4.0 and .NET Framework 3.5.
Release 2.7 was released on March 12, 2011 and it targets CPython 2.7.
Release 2.7.1 was released on October 21, 2011 and it targets CPython 2.7.
Release 2.7.2.1 was released on March 13, 2012. It enables support for ZIP file format libraries, SQLite, and compiled executables.
Release 2.7.4 was released on September 7, 2013.
Release 2.7.5 was released on December 6, 2014 and mostly consists of bug fixes.
Release 2.7.6 was released on August 21, 2016 and only consists of bug fixes.
Release 2.7.7 was released on December 7, 2016 and only consists of bug fixes.
Release 2.7.8 was released on February 16, 2018 and consists of bug fixes, reorganized code, and an updated test infrastructure (including significant testing on Linux under Mono). It is also the first release to support .NET Core.
Release 2.7.9 was released on October 9, 2018 and consists of bug fixes, reorganized code. It is intended to be the last release before IronPython 3.
Release 2.7.10 was released on April 27, 2020 and adds .NET Core 3.1 support.
Release 2.7.11 was released on November 17, 2020 and resolves issues when running on .NET 5.
Release 2.7.12 was released on January 21, 2022 and resolves issues with .NET 6 and removes support for .NET core 2.1
Release 3.4.0 was released on December 12, 2022 and is the first release to support Python 3.x.

Differences with CPython
There are some differences between the Python reference implementation CPython and IronPython. Some projects built on top of IronPython are known not to work under CPython. Conversely, CPython applications that depend on extensions to the language that are implemented in C are not compatible with IronPython
, unless they are implemented in a .NET interop. For example, NumPy was wrapped by Microsoft in 2011, allowing code and libraries dependent on it to be run directly from .NET Framework.

Silverlight
IronPython is supported on Silverlight (which is deprecated by Microsoft and already has lost support in most web browsers). It can be used as a scripting engine in the browser just like the JavaScript engine. IronPython scripts are passed like simple client-side JavaScript scripts in <script>-tags. It is then also possible to modify embedded XAML markup.
The technology behind this is called Gestalt.

The same works for IronRuby.

License
Until version 0.6, IronPython was released under the terms of Common Public License. Following recruitment of the project lead in August 2004, IronPython was made available as part of Microsoft's Shared Source initiative. This license is not OSI-approved but the authors claim it meets the open-source definition. With the 2.0 alpha release, the license was changed to the Microsoft Public License, which the OSI has approved. The latest versions are released under the terms of the Apache License 2.0.

Interface extensibility
One of IronPython's key advantages is in its function as an extensibility layer to application frameworks written in a .NET language. It is relatively simple to integrate an IronPython interpreter into an existing .NET application framework. Once in place, downstream developers can use scripts written in IronPython that interact with .NET objects in the framework, thereby extending the functionality in the framework's interface, without having to change any of the framework's code base.
IronPython makes extensive use of reflection. When passed in a reference to a .NET object, it will automatically import the types and methods available to that object. This results in a highly intuitive experience when working with .NET objects from within an IronPython script.

Examples
The following IronPython script manipulates .NET Framework objects. This script can be supplied by a third-party client-side application developer and passed into the server-side framework through an interface. Note that neither the interface, nor the server-side code is modified to support the analytics required by the client application.

In this case, assume that the .NET Framework implements a class, BookDictionary, in a module called BookService, and publishes an interface into which IronPython scripts can be sent and executed.
This script, when sent to that interface, will iterate over the entire list of books maintained by the framework, and pick out those written by Booker Prize-winning authors.
What's interesting is that the responsibility for writing the actual analytics reside with the client-side developer. The demands on the server-side developer are minimal, essentially just providing access to the data maintained by the server. This design pattern greatly simplifies the deployment and maintenance of complex application frameworks.
The following script uses the .NET Framework to create a simple Hello World message.

Performance
The performance characteristics of IronPython compared to CPython, the reference implementation of Python, depends on the exact benchmark used. IronPython performs worse than CPython on most benchmarks taken with the PyStone script but better on other benchmarks.
IronPython may perform better in Python programs that use threads or multiple cores, as it has a JIT compiler, and also because it doesn't have the Global Interpreter Lock.

Overview and key features
Integration with .NET: IronPython allows you to use .NET libraries and frameworks directly in your Python code. This means you can leverage the extensive .NET ecosystem and access features that are specific to .NET environments.
Dynamic Language Runtime (DLR): IronPython runs on the Dynamic Language Runtime, which is a set of services that support dynamic typing and dynamic method invocation in .NET languages.
Interoperability: You can call .NET code from IronPython and vice versa. This makes it possible to integrate Python scripts with existing .NET applications or use .NET components within Python projects.
Syntax and Semantics: IronPython aims to be as close as possible to the standard Python language (CPython), though there might be minor differences due to the underlying .NET platform.
Performance: While IronPython provides good performance for many applications, it might not be as fast as CPython for some tasks, particularly those that rely heavily on Python's native libraries.
Compatibility: IronPython is compatible with Python 2.x, but it does not support Python 3.x features. This means that some newer Python libraries or syntax may not be available.

See also
Boo – a language for the .NET Framework and Mono with Python-inspired syntax and features borrowed from C# and Ruby
Cobra
IronScheme
Jython – an implementation of Python for the Java Virtual Machine
Cython
PyPy – a self-hosting interpreter for the Python programming language
Tao Framework
Unladen Swallow – A (now-defunct) branch of CPython that aimed to provide superior performance using an LLVM-based just-in-time compiler

References
External links
Official website