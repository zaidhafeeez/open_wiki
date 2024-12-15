# SCons

## Article Metadata

- **Last Updated:** 2024-12-15T04:44:44.060877+00:00
- **Original Article:** [SCons](https://en.wikipedia.org/wiki/SCons)
- **Language:** en
- **Page ID:** 1175381

## Summary

SCons is a computer software build tool that automatically analyzes source code file dependencies and operating system adaptation requirements from a software project description and generates final binary executables for installation on the target operating system platform.  Its function is analogous to the traditional GNU build system based on the make utility and the autoconf tools.
SCons generates project configurations and build process implementations in the form of Python scripts.

## Categories

- Category:All articles with unsourced statements
- Category:Articles with example Python (programming language) code
- Category:Articles with unsourced statements from March 2014
- Category:Build automation
- Category:Compiling tools
- Category:Free software programmed in Python
- Category:Official website different in Wikidata and Wikipedia
- Category:Software using the MIT license

## Table of Contents

- History and related projects
- Major features
- Examples
- See also
- References
- External links

## Content

SCons is a computer software build tool that automatically analyzes source code file dependencies and operating system adaptation requirements from a software project description and generates final binary executables for installation on the target operating system platform.  Its function is analogous to the traditional GNU build system based on the make utility and the autoconf tools.
SCons generates project configurations and build process implementations in the form of Python scripts.

History and related projects
SCons software history started with the Cons software construction utility created by Bob Sidebotham in 1999. Cons was written in the Perl language. It served as a base for the ScCons build tool, a design which won the Software Carpentry project SC Build competition in August 2000.  ScCons was the foundation for SCons.
SCons inspired the creation of Waf, formerly known as SCons/BKsys, which emerged in the KDE community. For some time, there were plans to use it as the build tool for KDE 4 and beyond, but that effort was abandoned in favor of CMake.
Notable applications that use SCons include the following: The Battle for Wesnoth, Battlefield 1942, Doom 3, FCEUX, gem5, gpsd, GtkRadiant, Madagascar, Mixxx, MongoDB, Nullsoft Scriptable Install System, OpenNebula, VMware,, Wolfenstein: Enemy Territory, XORP and MCA2, openpilot and Godot.
.csig is the SCons Content Signature file format.

Major features
Major SCons features include the following:

Configuration files are Python scripts, which means that user-written builds have access to a complete general-purpose programming language.
Automatic dependency analysis built-in for C, C++ and Fortran. Dependency analysis is extensible through user-defined dependency scanners for other languages or file types. Unlike the GNU Compiler Collection's (GCC) built-in dependency analysis, it uses a regular expression scan for included source files.
Built-in support for C, C++, D, Java, Fortran, Objective-C, Yacc, Lex, Qt and SWIG, as well as TeX and LaTeX documents.  SCons can also handle other languages or file types through user-defined builders.
Building from central repositories of source code and pre-built targets.
Built-in ability to use Microsoft Visual Studio, including the generation of .dsp, .dsw, .sln and .vcproj files.
Detection of file content changes using MD5 signatures; optional, configurable ability to use traditional timestamps.
Ability to do parallel builds, maintaining a specified number of jobs running simultaneously regardless of directory hierarchy.
Integrated Autoconf-like support for finding #include files, libraries, functions and typedefs.
Global view of all dependencies, so multiple build passes or reordering targets is not required.
Ability to share built files in a cache to speed up multiple builds - like ccache but for any type of target file, not just C/C++ compilation.
Designed from the ground up for cross-platform builds, and known to work on POSIX systems (including Linux, IBM AIX and OS/2, *BSD Unices, HP-UX, SGI IRIX, Solaris, illumos), MS Windows NT, Apple OS X.

Examples
The following example is a very simple SConstruct file that compiles the C program file hello-world.c using the default platform compiler:

The following is a more complex example that creates an environment used to build the program hello:

See also
Buildout
CMake
qmake
Qbs (build tool)
Premake
GNU build system
List of build automation software
Waf

References
External links
Official website

## Related Articles

### Internal Links

- [Apple Inc.](https://en.wikipedia.org/wiki/Apple_Inc.)
- [Autoconf](https://en.wikipedia.org/wiki/Autoconf)
- [Battlefield 1942](https://en.wikipedia.org/wiki/Battlefield_1942)
- [Berkeley Software Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution)
- [Buildout](https://en.wikipedia.org/wiki/Buildout)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CMake](https://en.wikipedia.org/wiki/CMake)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Ccache](https://en.wikipedia.org/wiki/Ccache)
- [Software](https://en.wikipedia.org/wiki/Software)
- [Coupling (computer programming)](https://en.wikipedia.org/wiki/Coupling_(computer_programming))
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Doom 3](https://en.wikipedia.org/wiki/Doom_3)
- [FCEUX](https://en.wikipedia.org/wiki/FCEUX)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [GNU Compiler Collection](https://en.wikipedia.org/wiki/GNU_Compiler_Collection)
- [GNU Autotools](https://en.wikipedia.org/wiki/GNU_Autotools)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Godot (game engine)](https://en.wikipedia.org/wiki/Godot_(game_engine))
- [Gpsd](https://en.wikipedia.org/wiki/Gpsd)
- [Quake modding](https://en.wikipedia.org/wiki/Quake_modding)
- [HP-UX](https://en.wikipedia.org/wiki/HP-UX)
- [IBM AIX](https://en.wikipedia.org/wiki/IBM_AIX)
- [IRIX](https://en.wikipedia.org/wiki/IRIX)
- [Illumos](https://en.wikipedia.org/wiki/Illumos)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [KDE](https://en.wikipedia.org/wiki/KDE)
- [LaTeX](https://en.wikipedia.org/wiki/LaTeX)
- [Lex (software)](https://en.wikipedia.org/wiki/Lex_(software))
- [Linux](https://en.wikipedia.org/wiki/Linux)
- [List of build automation software](https://en.wikipedia.org/wiki/List_of_build_automation_software)
- [MD5](https://en.wikipedia.org/wiki/MD5)
- [MIT License](https://en.wikipedia.org/wiki/MIT_License)
- [Madagascar (software)](https://en.wikipedia.org/wiki/Madagascar_(software))
- [Make (software)](https://en.wikipedia.org/wiki/Make_(software))
- [Microsoft](https://en.wikipedia.org/wiki/Microsoft)
- [Visual Studio](https://en.wikipedia.org/wiki/Visual_Studio)
- [Mixxx](https://en.wikipedia.org/wiki/Mixxx)
- [MongoDB](https://en.wikipedia.org/wiki/MongoDB)
- [Nullsoft](https://en.wikipedia.org/wiki/Nullsoft)
- [OS/2](https://en.wikipedia.org/wiki/OS/2)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [OpenNebula](https://en.wikipedia.org/wiki/OpenNebula)
- [Openpilot](https://en.wikipedia.org/wiki/Openpilot)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [POSIX](https://en.wikipedia.org/wiki/POSIX)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Premake](https://en.wikipedia.org/wiki/Premake)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Qbs (build tool)](https://en.wikipedia.org/wiki/Qbs_(build_tool))
- [Qmake](https://en.wikipedia.org/wiki/Qmake)
- [Qt (software)](https://en.wikipedia.org/wiki/Qt_(software))
- [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [SWIG](https://en.wikipedia.org/wiki/SWIG)
- [Silicon Graphics](https://en.wikipedia.org/wiki/Silicon_Graphics)
- [The Carpentries](https://en.wikipedia.org/wiki/The_Carpentries)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Programming tool](https://en.wikipedia.org/wiki/Programming_tool)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Oracle Solaris](https://en.wikipedia.org/wiki/Oracle_Solaris)
- [TeX](https://en.wikipedia.org/wiki/TeX)
- [The Battle for Wesnoth](https://en.wikipedia.org/wiki/The_Battle_for_Wesnoth)
- [Typedef](https://en.wikipedia.org/wiki/Typedef)
- [VMware](https://en.wikipedia.org/wiki/VMware)
- [Waf (build system)](https://en.wikipedia.org/wiki/Waf_(build_system))
- [Windows NT](https://en.wikipedia.org/wiki/Windows_NT)
- [Wolfenstein: Enemy Territory](https://en.wikipedia.org/wiki/Wolfenstein:_Enemy_Territory)
- [XORP](https://en.wikipedia.org/wiki/XORP)
- [Yacc](https://en.wikipedia.org/wiki/Yacc)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Category:Articles with unsourced statements from March 2014](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_March_2014)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:44:44.060877+00:00_