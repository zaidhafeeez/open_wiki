# Wing IDE

## Metadata
- **Last Updated:** 2024-12-13 13:50:34 UTC
- **Original Article:** [Wing IDE](https://en.wikipedia.org/wiki/Wing_IDE)
- **Language:** en
- **Page ID:** 23611251

## Summary
The Wing Python IDE is a family of integrated development environments (IDEs) from Wingware created specifically for the Python programming language with support for editing, testing, debugging, inspecting/browsing, and error-checking Python code.
There are three versions of the IDE, each one focused on different types of users:

Wing Pro – a full-featured commercial version, for professional programmers;
Wing Personal – a free version that omits many of these features, for students and hobbyists; and
Wing 101 – a very simplified free version for teaching beginner programmers.
Wing Pro provides AI-assisted development, local and remote debugging, editing (with multiple key bindings, auto-completion, auto-editing, and multi-selection), source browser and code navigation, code refactoring, import management, error checking, auto-reformatting, unit testing with code coverage, version control, project management, Python environment and package management, single and multi-file search, fine-grained customization, support for Docker and LXC containers, assistance for working with third-party frameworks and tools (such as Django, Flask, Matplotlib, Pandas, Blender, Maya, Unreal Engine, PyQt, wxPython, and others) through Python scripting, and comprehensive documentation.
Wing Personal and Wing 101 omit many of these features. All three versions of Wing support installation on Windows, Mac OS X, and Intel and ARM Linux.
Free licenses for Wing Pro are available for educational users and unpaid open-source software developers.

## Categories
This article belongs to the following categories:

- Category:All articles needing additional references
- Category:All articles with a promotional tone
- Category:All articles with unsourced statements
- Category:Articles needing additional references from January 2021
- Category:Articles with a promotional tone from May 2020
- Category:Articles with multiple maintenance issues
- Category:Articles with unsourced statements from July 2024
- Category:CS1 maint: numeric names: authors list
- Category:Integrated development environments
- Category:Official website different in Wikidata and Wikipedia
- Category:Pages with broken reference names
- Category:Pages with reference errors
- Category:Python (programming language) development tools

## Table of Contents

- AI Assisted Development
- Debugger
- Code intelligence
- Project Management
- Version control
- Package Management
- Unit testing
- Remote development
- Other features
- History
- See also
- References
- External links

## Content

The Wing Python IDE is a family of integrated development environments (IDEs) from Wingware created specifically for the Python programming language with support for editing, testing, debugging, inspecting/browsing, and error-checking Python code.
There are three versions of the IDE, each one focused on different types of users:

Wing Pro – a full-featured commercial version, for professional programmers;
Wing Personal – a free version that omits many of these features, for students and hobbyists; and
Wing 101 – a very simplified free version for teaching beginner programmers.
Wing Pro provides AI-assisted development, local and remote debugging, editing (with multiple key bindings, auto-completion, auto-editing, and multi-selection), source browser and code navigation, code refactoring, import management, error checking, auto-reformatting, unit testing with code coverage, version control, project management, Python environment and package management, single and multi-file search, fine-grained customization, support for Docker and LXC containers, assistance for working with third-party frameworks and tools (such as Django, Flask, Matplotlib, Pandas, Blender, Maya, Unreal Engine, PyQt, wxPython, and others) through Python scripting, and comprehensive documentation.
Wing Personal and Wing 101 omit many of these features. All three versions of Wing support installation on Windows, Mac OS X, and Intel and ARM Linux.
Free licenses for Wing Pro are available for educational users and unpaid open-source software developers.

AI Assisted Development
The AI assistant, available in Wing Pro only, can be used to write new code, refactor or redesign existing code, and inspect and understand code. Using the assistant, users may:

Refactor or rewrite selected code according to the user's written instructions;
Insert new AI-written code at the current editor insertion point according to a written description; and
Chat with an AI assistant to ask about some code or iterate towards a solution for a bug fix or extension, without changing any of the existing source code directly.

Debugger
The debugger can be used to locate and fix bugs, as well as a way to write new code interactively in the live runtime state for which the code is being designed. The level of the debugging support depends on the version used, with each tier of service giving the user more features with which they can debug.
Wing 101 supports:

Debug code launched from the IDE (as a file or module with 'python -m');
Interactive debugging from (and within) the integrated Python Shell;
Exception and traceback reporting;
View stack, local/global variables, and return values;
The data frame and array viewer;
Integrated Debug I/O tool with configurable text encoding;
Optional native console I/O; and
Steps over importlib frames.
Wing Personal adds:

Multi-threaded debugging;
Debug code launched outside of the IDE, including code running under a web framework or embedded instance of Python;
Debug value tooltips;
Alter debug data values; and
Define named entry points and debug launch configurations.
Wing Pro adds:

An interactive Debug Probe command line for inspecting the current debug frame, with auto-completion, syntax highlighting, goto-definition, call tips, and documentation links;
Multi-process and automatic child process debugging;
Launching remote debug processes from the IDE;
Conditional and ignore-counted breakpoints;
Enable/disable breakpoints;
Moving the debug program counter;
Debug unit tests;
Tutorials and extra features for Django, Flask, Jupyter, matplotlib, web2py, Plone, Zope, Docker, AWS, Vagrant, Raspberry Pi, Windows Subsystem for Linux, Blender, Unreal Engine, Nuke, and others;
The ability to press Shift-Space to view the value of all symbols in the editor;
Recursive debugging of code invoked in the context of another debug stack frame;
Convenient Restart Debugging tool;
Tracking values by reference;
Evaluating expressions;
Breakpoint manager;
Debug process attach/detach;
Inspecting sys.modules; and
Marking a range of code in the editor for quick reevaluation in Python Shell or Debug Probe.

Code intelligence
The code intelligence features speed up editing, facilitated navigation through code, and inspected code for errors. These features rely both on static analysis of Python code found in the project and on the Python Path and runtime analysis of code whenever the debugger is active or the code is active in the integrated Python Shell. The features available to the user depend on the version being used.
Wing 101 provides:

An auto-completer that offers completions in Python code and in the integrated Python shell (this feature is disabled by default in Wing 101 but can be enabled in preferences)
Source index menus in each editor provide a handy index into the source code
Goto-definition
Auto-indent
PEP8, Black, YAPF, and Ruff reformatting
Syntax and indentation error indicators
Convert indents and end-of-line characters on paste
Understands PEP 484 and 526 type hinting
Wing Personal adds:

Find Symbol: keyboard-driven goto-definition within the current file or any project file
Auto-completion in non-Python files
Indentation analysis and conversion
Source Assistant: provides context-appropriate call signature and documentation with the rendering of PEP287 docstrings
Class browser for single files or whole project
Wing Pro adds:

Code Warnings tool
Pylint, pep8 checker, mypy, flake8, and Ruff integrations
Module browser
Source Assistant includes standard library documentation links
Find all points of use of a symbol, filtering out different but like-named symbols
Find the symbol by name, in the current file or all project files
Refactoring: rename or move a symbol and update points of use, extract a range of code to a new function or method, introduce a variable, and manage imports

Project Management
Wing's project manager allows developers to set up, manage, and share development configurations. It supports creating projects for existing or new source directories, with optional code retrieval from version control repositories. The IDE facilitates easy creation and configuration of Python environments using virtualenv, pip, Poetry, pipenv, or conda, either locally, on a remote host, or with containers managed by Docker or LXC/LXD.

Version control
Wing Pro integrates with various version control systems, including Git, Mercurial, Perforce, Subversion, and CVS. It offers features such as status checking, committing, logging, blame/praise/annotate, reverting, resolving, and repository push/pull operations. A difference and merge tool is also available for comparing files or directories and reviewing uncommitted changes.

Package Management
Wing Pro includes an integrated package management tool that simplifies inspecting, adding, removing, and upgrading Python packages in the development environment. It supports pip, Poetry, pipenv, and conda environments.

Unit testing
Wing Pro supports unit testing by allowing running and debugging of unit tests written for the unittest, pytest, doctest, nose, and Django testing frameworks. It optionally tracks code coverage, to indicate how well code is being tested and to re-run only tests affected by changes to code.

Remote development
Wing Pro also supports secure development on remote hosts, virtual machines, or containers hosted by Docker, Docker Compose, or LXC/LXD. Code on the remote system may be edited, debugged, tested, and managed from the IDE, as for locally stored files. Remote development also supports externally launched debugging.

Other features
Other features present in all versions include:

Editor emulates vim, emacs, Visual Studio, Eclipse, XCode, Matlab, and Brief
Syntax highlighting for most programming languages, including Python, Django (web framework) templates, CoffeeScript, HTML/XML, CSS, JavaScript, C/C++, and about 70 others
Integrated Python shell with auto-completion, syntax highlighting
Search within the current file
Configurable colour palettes and user interface layout
Extensive documentation, How-Tos, and tutorial
German, French, and Russian UI localization
Wing Personal adds:

Multi-select to simultaneously edit multiple parts of a file
Define custom key bindings
Create projects for different development tasks
Quickly open project files by name fragment
Add, delete, rename, and move files in the project
Create new projects using existing virtualenv, Anaconda env, pipenv, or Poetry environments
Project-wide and multi-file search
Regex and wildcard search
Search documentation
Wing Pro adds:

Goto-definition, call tips, and documentation links in the integrated Python shell
Python environment creation with virtualenv, pipenv, conda, Poetry, and Docker
Python package management with pip, pipenv, conda, and Poetry
File add, delete, rename, and move operations track to the active revision control systems
Set and traverse bookmarks
Code snippets with recursive inline data entry
Perspectives for naming custom user interface layouts
Execute external commands in the integrated OS Commands tool
Extend the IDE's functionality with Python scripts

History
The first public version of Wing was released on the 7th of September of 2000, as 1.0 beta, only for Linux.
The first stable version was v1.0 for Linux, released on the 1st of December of 2000.
As of March 29, 2004, Archaeopteryx Software Inc began doing business as Wingware.
Wing version 4.x and earlier were based on GTK2 and the OS X version required X11. Wing 5 changed to Qt4 via PySide and no longer uses X11 on OS X. Wing 6 moved to Qt5 with PyQt5.  Wing 10 uses PyQt6.5.

See also
List of integrated development environments for Python

References
External links
Official website

## Archive Info
- **Archived on:** 2024-12-15 20:27:16 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 9748 bytes
- **Word Count:** 1430 words
