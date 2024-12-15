# SCons

## Metadata
- **Last Updated:** 2024-12-15 18:19:18 UTC
- **Original Article:** [SCons](https://en.wikipedia.org/wiki/SCons)
- **Language:** en
- **Page ID:** 1175381

## Summary
SCons is a software development tool that analyzes source code dependencies and operating system adaptation requirements from a software project description and generates final binary executables for installation on the target operating system platform. Its function is similar to the more popular GNU build system.
The tool generates Python scripts for project configuration and build logic.

## Categories
This article belongs to the following categories:

- Category:All articles with unsourced statements
- Category:Articles with example Python (programming language) code
- Category:Articles with unsourced statements from March 2014
- Category:Build automation
- Category:Compiling tools
- Category:Free software programmed in Python
- Category:Official website different in Wikidata and Wikipedia
- Category:Pages displaying wikidata descriptions as a fallback via Module:Annotated link
- Category:Software using the MIT license

## Table of Contents

- History
- Features
- Examples
- See also
- References
- External links

## Content

SCons is a software development tool that analyzes source code dependencies and operating system adaptation requirements from a software project description and generates final binary executables for installation on the target operating system platform. Its function is similar to the more popular GNU build system.
The tool generates Python scripts for project configuration and build logic.

History
The Cons software construction utility, written in the Perl, was created by Bob Sidebotham in 1999. It served as a base for the ScCons build tool, a design which won the Software Carpentry project SC Build competition in August 2000.  ScCons was the foundation for SCons.
SCons inspired the creation of Waf, formerly known as SCons/BKsys, which emerged in the KDE community. For some time, there were plans to use it as the build tool for KDE 4 and beyond, but that effort was abandoned in favor of CMake.
Notable projects that use SCons (or used it at one time) include: The Battle for Wesnoth, Battlefield 1942, Doom 3, FCEUX, gem5, gpsd, GtkRadiant, Madagascar, Mixxx, MongoDB, Nullsoft Scriptable Install System, OpenNebula, VMware,, Wolfenstein: Enemy Territory, XORP and MCA2, openpilot and Godot.
.csig is the SCons Content Signature file format.

Features
Major features include:

Configuration files are Python; user-written builds can leverage a general-purpose, cross-platform programming language
Dependency analysis for C, C++ and Fortran
Dependency analysis is extensible through user-defined scanners for other languages or file types; unlike GNU Compiler Collection (GCC) dependency analysis, SCons uses a regular expression scan for included source files
Built-in support for C, C++, D, Java, Fortran, Objective-C, Yacc, Lex, Qt and SWIG, as well as TeX and LaTeX documents
Support for other languages via custom builders
Building from central repositories of source code and pre-built targets
Ability to use Visual Studio, including the generation of .dsp, .dsw, .sln and .vcproj files
Detection of file content changes using MD5 signatures; optional, configurable ability to use traditional timestamps
Ability to do parallel builds, maintaining a specified number of jobs running simultaneously regardless of directory hierarchy
Autoconf-like support for finding #include files, libraries, functions and typedefs
Global view of dependencies, so multiple build passes or reordering targets is not required.
Ability to share built files in a cache to speed up multiple builds - like ccache but for any type of target file, not just C/C++ compilation
Designed from the ground up for cross-platform builds; known to work on POSIX systems (including Linux, AIX and OS/2, *BSD Unices, HP-UX, SGI IRIX, Solaris, illumos), Windows NT, OS X

Examples
The following is an SConstruct file that builds a hello world C program using the default platform compiler:

The following is a SConstruct file for a project that includes two source files and specifies build tool options:

See also
Buildout – programming tool aimed to assist with deploying softwarePages displaying wikidata descriptions as a fallback
qmake – software build tool that generates MakefilesPages displaying wikidata descriptions as a fallback
Qbs (build tool) – cross-platform free and open-source software for managing the build process of softwarePages displaying wikidata descriptions as a fallback
Premake – software development utilityPages displaying wikidata descriptions as a fallback
List of build automation software

References
External links
Official website

## Archive Info
- **Archived on:** 2024-12-15 20:38:44 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 3557 bytes
- **Word Count:** 529 words
