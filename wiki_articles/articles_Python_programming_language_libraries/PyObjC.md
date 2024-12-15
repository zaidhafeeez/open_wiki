# PyObjC

## Metadata
- **Last Updated:** 2024-11-24 06:40:49 UTC
- **Original Article:** [PyObjC](https://en.wikipedia.org/wiki/PyObjC)
- **Language:** en
- **Page ID:** 2843493

## Summary
PyObjC is a bidirectional bridge between the Python and Objective-C programming languages, allowing programmers to use and extend existing Objective-C libraries, such as Apple's Cocoa framework, using Python.
PyObjC is used to develop macOS applications in pure Python.
There is also limited support for GNUstep, an open source, cross-platform implementation of Cocoa.

## Categories
This article belongs to the following categories:

- Category:All articles needing additional references
- Category:Articles needing additional references from November 2014
- Category:MacOS programming tools
- Category:Python (programming language) libraries

## Table of Contents

- For Python programmers
- For Objective-C programmers
- History
- Messages and methods
- Classes
- See also
- References
- External links

## Content

PyObjC is a bidirectional bridge between the Python and Objective-C programming languages, allowing programmers to use and extend existing Objective-C libraries, such as Apple's Cocoa framework, using Python.
PyObjC is used to develop macOS applications in pure Python.
There is also limited support for GNUstep, an open source, cross-platform implementation of Cocoa.

For Python programmers
The most important usage of PyObjC is enabling programmers to create GUI applications using Cocoa libraries in pure Python. Moreover, as an effect of Objective-C's close relationship with the C programming language (it is a pure superset), developers are also able to incorporate any C-based API by wrapping it with an Objective-C wrapper and then using the wrapped code over the PyObjC bridge. Using Objective-C++, the same can be done with C++ libraries.

For Objective-C programmers
Cocoa developers may also benefit, as tasks written in Python generally take fewer lines than the Objective-C equivalent. This can be used to their advantage as it enables faster prototyping.

History
PyObjC's origins date back to 1996, when Lele Gaifax built the original module in September of that year. Among the credited contributors were Guido van Rossum, creator of the Python programming language.
PyObjC was rewritten in 2002. Notable additions include the ability to directly subclass Objective-C classes from Python and nearly complete support for the Foundation, App Kit and Address Book frameworks.
Later the same year, support was added for non-framework Python builds, as well as subsequent support for the Python distribution included with Mac OS X. Along with these changes came project templates for standalone Cocoa applications for use with Project Builder, the predecessor to the current Apple platform IDE, Xcode.
Apple incorporated PyObjC into Mac OS X in 2007, with the release of Mac OS X 10.5 Leopard.

Messages and methods
In Objective-C, objects communicate with each other by sending messages, which is analogous to method calls in other object-oriented languages. When an object receives a message, it looks up the message's name, or selector, and matches it up with a method designated the same selector, which it then invokes.
The syntax for these message expressions is inherited from Smalltalk, and appears as an object, called the receiver, placed to the left of the name of the message, or selector, and both are enclosed within a pair of square brackets (the square bracket syntax is not inherited from Smalltalk). Colons within a selector indicate that it accepts one or more arguments, one for each colon. Intended to improve code readability, colons are placed within the selector such that when the required arguments are in place, the expression's intent is unambiguous:

This is distinct from the syntax used in Python, and in many other languages, where an equivalent expression would read:

Translating Objective-C selectors to Python method names is accomplished by replacing each colon with a single underscore and listing the arguments within a pair of parentheses at the end, as demonstrated above.

Classes
Objective-C classes are subclassed in the same manner as a normal Python class:

See also
libffi
RubyCocoa

References
External links
Official website 
Ronald Oussoren's warning on Xcode 4.0

## Archive Info
- **Archived on:** 2024-12-15 20:27:31 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 3326 bytes
- **Word Count:** 515 words
