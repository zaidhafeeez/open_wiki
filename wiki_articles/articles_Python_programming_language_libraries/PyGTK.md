# PyGTK

## Metadata
- **Last Updated:** 2024-12-03 06:54:40 UTC
- **Original Article:** [PyGTK](https://en.wikipedia.org/wiki/PyGTK)
- **Language:** en
- **Page ID:** 890353

## Summary
PyGTK is a set of Python wrappers for the GTK graphical user interface library. PyGTK is free software and licensed under the LGPL. It is analogous to PyQt/PySide and wxPython, the Python wrappers for Qt and wxWidgets, respectively. Its original author is GNOME developer James Henstridge. There are six people in the core development team, with various other people who have submitted patches and bug reports. PyGTK has been selected as the environment of choice for applications running on One Laptop Per Child systems.
PyGTK will be phased out with the transition to GTK version 3 and be replaced with PyGObject, which uses GObject Introspection to generate bindings for Python and other languages on the fly. This is expected to eliminate the delay between GTK updates and corresponding language binding updates, as well as reduce maintenance burden on the developers.

## Categories
This article belongs to the following categories:

- Category:Articles with short description
- Category:GTK language bindings
- Category:Python (programming language) libraries
- Category:Short description matches Wikidata
- Category:Software that uses PyGObject
- Category:Software that uses PyGTK
- Category:Widget toolkits

## Table of Contents

- Syntax
- PyGObject
- See also
- References
- External links

## Content

PyGTK is a set of Python wrappers for the GTK graphical user interface library. PyGTK is free software and licensed under the LGPL. It is analogous to PyQt/PySide and wxPython, the Python wrappers for Qt and wxWidgets, respectively. Its original author is GNOME developer James Henstridge. There are six people in the core development team, with various other people who have submitted patches and bug reports. PyGTK has been selected as the environment of choice for applications running on One Laptop Per Child systems.
PyGTK will be phased out with the transition to GTK version 3 and be replaced with PyGObject, which uses GObject Introspection to generate bindings for Python and other languages on the fly. This is expected to eliminate the delay between GTK updates and corresponding language binding updates, as well as reduce maintenance burden on the developers.

Syntax
The Python code below will produce a 200x200 pixel window with the words "Hello World" inside.

Notable applications that have used PyGTK
PyGTK has been used in a number of notable applications, some examples:

PyGObject
PyGObject provides a wrapper for use in Python programs when accessing GObject libraries. GObject is an object system used by GTK, GLib, GIO, GStreamer and other libraries.
Like the GObject library itself, PyGObject is licensed under the GNU LGPL, so it is suitable for use in both free software and proprietary applications. It is already in use in many applications ranging from small single-purpose scripts to large full-featured applications.
PyGObject can dynamically access any GObject libraries that use GObject Introspection. It replaces the need for separate modules such as PyGTK, GIO and python-gnome to build a full GNOME 3.0 application.  Once new functionality is added to GObject library it is instantly available as a Python API without the need for intermediate Python glue.

Notable applications that use PyGObject
PyGObject has replaced PyGTK, but it has taken a considerable amount of time for many programs to be ported. Most of the software listed here has an older version which used PyGTK.

See also
PyQt (Python wrapper for the Qt toolkit)
PySide (Alternative Python wrapper for the Qt toolkit)
wxPython (Python wrapper for the wx widgets collection)

References
External links
PyGTK Homepage
PyGTK FAQ
PyGTK Tutorial
PyGTK Notebook A Journey Through Python Gnome Technologies by Peter Gill
PyGTK at Python wiki
PyGObject Homepage
PyGObject tutorial

## Archive Info
- **Archived on:** 2024-12-15 20:27:31 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2476 bytes
- **Word Count:** 389 words
