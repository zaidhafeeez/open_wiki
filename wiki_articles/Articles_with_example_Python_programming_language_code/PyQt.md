---
title: PyQt
url: https://en.wikipedia.org/wiki/PyQt
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Commons category link from Wikidata", "Category:Cross-platform free software", "Category:Free computer libraries", "Category:Free software programmed in C++", "Category:Free software programmed in Python", "Category:Official website different in Wikidata and Wikipedia", "Category:Python (programming language) libraries", "Category:Qt (software)", "Category:Short description is different from Wikidata", "Category:Widget toolkits"]
references: 0
last_modified: 2024-12-19T13:45:44Z
---

# PyQt

## Summary

PyQt is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in. PyQt is free software developed by the British firm Riverbank Computing. It is available under similar terms to Qt versions older than 4.5; this means a variety of licenses including GNU General Public License (GPL) and commercial license, but not the GNU Lesser General Public License (LGPL). PyQt supports Microsoft Windows as well as various kinds of UNIX, including Linux and MacOS (or Darwin).
PyQt 

## Full Content

PyQt is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in. PyQt is free software developed by the British firm Riverbank Computing. It is available under similar terms to Qt versions older than 4.5; this means a variety of licenses including GNU General Public License (GPL) and commercial license, but not the GNU Lesser General Public License (LGPL). PyQt supports Microsoft Windows as well as various kinds of UNIX, including Linux and MacOS (or Darwin).
PyQt implements around 440 classes and over 6,000 functions and methods including:

a substantial set of GUI widgets
classes for accessing SQL databases (ODBC, MySQL, PostgreSQL, Oracle, SQLite)
QScintilla, Scintilla-based rich text editor widget
data aware widgets that are automatically populated from a database
an XML parser
SVG support
classes for embedding ActiveX controls on Windows (only in commercial version)
To automatically generate these bindings, Phil Thompson developed the tool SIP, which is also used in other projects.

History
PyQt was first released by Riverbank Computing in 1998.
In August 2009, Nokia sought for the Python binding to be available under the LGPL license. At the time, Nokia owned Qt Software, the developer of QT. After failing to reach an agreement with Riverbank Computing, Nokia released its binding, PySide, providing similar functionality.

Main components
PyQt4 contains the following Python modules.

The QtCore module contains the core non-GUI classes, including the event loop and Qt's signal and slot mechanism. It also includes platform independent abstractions for Unicode, threads, mapped files, shared memory, regular expressions, and user and application settings.
The QtGui module contains the majority of the GUI classes. These include a number of table, tree and list classes based on the model–view–controller design pattern. Also provided is a sophisticated 2D canvas widget capable of storing thousands of items including ordinary widgets.
The QtNetwork module contains classes for writing UDP and TCP clients and servers. It includes classes that implement FTP and HTTP clients and support DNS lookups. Network events are integrated with the event loop making it very easy to develop networked applications.
The QtOpenGL module contains classes that enable the use of OpenGL in rendering 3D graphics in PyQt applications.
The QtSql module contains classes that integrate with open-source and proprietary SQL databases. It includes editable data models for database tables that can be used with GUI classes. It also includes an implementation of SQLite.
The QtSvg module contains classes for displaying the contents of SVG files. It supports the static features of SVG 1.2 Tiny.
The QtXml module implements SAX and DOM interfaces to Qt's XML parser.
The QtMultimedia module implements low-level multimedia functionality. Application developers would normally use the phonon module.
The QtDesigner module contains classes that allow Qt Designer to be extended using PyQt.
The Qt module consolidates the classes contained in all of the modules described above into a single module. This has the advantage that you don't have to worry about which underlying module contains a particular class. It has the disadvantage that it loads the whole of the Qt framework, thereby increasing the memory footprint of an application. Whether you use this consolidated module, or the individual component modules is down to personal taste.
The uic module implements support for handling the XML files created by Qt Designer that describe the whole or part of a graphical user interface. It includes classes that load an XML file and render it directly, and classes that generate Python code from an XML file for later execution.
PyQt5 contains the following Python modules:

QtQml Module
QtQtuick Module
QtCore Module
QtGui Module
QtPrintSupport Module
QtWidgets Module
QGLContext Module
QGLFormat Module
QGLWidget Module
QtWebKit Module
QtWebKitWidgets Module

Versions
PyQt version 4 works with both Qt 4 and Qt 5. PyQt version 5 only supports Qt version 5, and drops support for features that are deprecated in Qt 5.

Hello World example
The below code written for PyQt6 shows a small window on the screen.

Notable applications that use PyQt
Anki, a spaced repetition flashcard program
Calibre, an E-book management application
Dropbox, a file hosting service
Eric Python IDE
Frescobaldi, a score editor for LilyPond music files
Kodos, a Python Regular expression Debugger
Leo, an outliner and literate programming editor
Ninja-IDE, an extensible open-source Python IDE
OpenLP, an open-source lyrics projection program
OpenShot, a video editing program
Orange, a data mining and visualization framework
Puddletag, an open-source, cross-platform ID3 tag editor
QGIS, a free software desktop Geographic Information Systems (GIS) application
qutebrowser, a web browser with Vim-style key bindings and a minimal GUI.
qt-recordMyDesktop, a Qt4 frontend for recordMyDesktop
Spyder, a Python data science IDE
TortoiseHg, a graphical interface for the Mercurial source management program (Hg)
Veusz, a scientific plotting application
GNS3, a network software emulator

See also
PyGTK (Python wrappers for GTK)
PySide (Alternative Python wrapper for the Qt toolkit)
wxPython (Python wrapper for the wx widgets collection)
Kivy
Tkinter (bundled with Python)

References
Further reading
Willman, Joshua (2020), Beginning PyQt - A Hands-on Approach to GUI Programming (1st ed.), Apress, p. 440, ISBN 978-1-4842-5856-9
Summerfield, Mark (October 28, 2007), Rapid GUI Programming with Python and Qt (Covers PyQt4) (1st ed.), Prentice Hall, p. 648, ISBN 978-0-13-235418-9
Rempt, Boudewijn (2002), GUI Programming with Python: QT Edition (Covers PyQt3), OpenDocs, archived from the original on 2010-04-09

External links
Official website
PyQt and PyKDE community Wiki
PyQt6 Tutorial Series
PyQt5 Tutorial Series
PyQT4 tutorial series
Tutorials
Tutorial
