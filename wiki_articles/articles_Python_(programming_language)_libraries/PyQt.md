# PyQt

## Article Metadata

- **Last Updated:** 2024-12-14T19:51:27.882598+00:00
- **Original Article:** [PyQt](https://en.wikipedia.org/wiki/PyQt)
- **Language:** en
- **Page ID:** 817919

## Summary

PyQt is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in. PyQt is free software developed by the British firm Riverbank Computing. It is available under similar terms to Qt versions older than 4.5; this means a variety of licenses including GNU General Public License (GPL) and commercial license, but not the GNU Lesser General Public License (LGPL). PyQt supports Microsoft Windows as well as various kinds of UNIX, including Linux and MacOS (or Darwin).
PyQt 

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Commons category link from Wikidata
- Category:Cross-platform free software
- Category:Free computer libraries
- Category:Free software programmed in C++
- Category:Free software programmed in Python
- Category:Official website different in Wikidata and Wikipedia
- Category:Python (programming language) libraries
- Category:Qt (software)
- Category:Short description is different from Wikidata
- Category:Widget toolkits

## Table of Contents

- History
- Main components
- Versions
- Hello World example
- Notable applications that use PyQt
- See also
- References
- Further reading
- External links

## Content

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

## Related Articles

### Internal Links

- [.NET](https://en.wikipedia.org/wiki/.NET)
- [2D computer graphics](https://en.wikipedia.org/wiki/2D_computer_graphics)
- [3D computer graphics](https://en.wikipedia.org/wiki/3D_computer_graphics)
- [Abstract Window Toolkit](https://en.wikipedia.org/wiki/Abstract_Window_Toolkit)
- [ActiveX](https://en.wikipedia.org/wiki/ActiveX)
- [Active Template Library](https://en.wikipedia.org/wiki/Active_Template_Library)
- [Adobe Flash](https://en.wikipedia.org/wiki/Adobe_Flash)
- [Allegro Common Lisp](https://en.wikipedia.org/wiki/Allegro_Common_Lisp)
- [AmigaOS](https://en.wikipedia.org/wiki/AmigaOS)
- [Android (operating system)](https://en.wikipedia.org/wiki/Android_(operating_system))
- [Android software development](https://en.wikipedia.org/wiki/Android_software_development)
- [Anki (software)](https://en.wikipedia.org/wiki/Anki_(software))
- [Apache Flex](https://en.wikipedia.org/wiki/Apache_Flex)
- [Springer Nature](https://en.wikipedia.org/wiki/Springer_Nature)
- [AsteroidOS](https://en.wikipedia.org/wiki/AsteroidOS)
- [BOOPSI](https://en.wikipedia.org/wiki/BOOPSI)
- [BeOS](https://en.wikipedia.org/wiki/BeOS)
- [BeOS](https://en.wikipedia.org/wiki/BeOS)
- [Bedrock (framework)](https://en.wikipedia.org/wiki/Bedrock_(framework))
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CDK (programming library)](https://en.wikipedia.org/wiki/CDK_(programming_library))
- [CEGUI](https://en.wikipedia.org/wiki/CEGUI)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Calibre (software)](https://en.wikipedia.org/wiki/Calibre_(software))
- [Carbon (API)](https://en.wikipedia.org/wiki/Carbon_(API))
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Classic Mac OS](https://en.wikipedia.org/wiki/Classic_Mac_OS)
- [Cocoa (API)](https://en.wikipedia.org/wiki/Cocoa_(API))
- [UIKit](https://en.wikipedia.org/wiki/UIKit)
- [Common Language Infrastructure](https://en.wikipedia.org/wiki/Common_Language_Infrastructure)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Common Lisp Interface Manager](https://en.wikipedia.org/wiki/Common_Lisp_Interface_Manager)
- [Component Library for Cross Platform](https://en.wikipedia.org/wiki/Component_Library_for_Cross_Platform)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Dart (programming language)](https://en.wikipedia.org/wiki/Dart_(programming_language))
- [Database](https://en.wikipedia.org/wiki/Database)
- [Dialog (software)](https://en.wikipedia.org/wiki/Dialog_(software))
- [Document Object Model](https://en.wikipedia.org/wiki/Document_Object_Model)
- [Dojo Toolkit](https://en.wikipedia.org/wiki/Dojo_Toolkit)
- [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System)
- [Dropbox](https://en.wikipedia.org/wiki/Dropbox)
- [Echo (framework)](https://en.wikipedia.org/wiki/Echo_(framework))
- [Enlightenment Foundation Libraries](https://en.wikipedia.org/wiki/Enlightenment_Foundation_Libraries)
- [Eric (software)](https://en.wikipedia.org/wiki/Eric_(software))
- [Ext JS](https://en.wikipedia.org/wiki/Ext_JS)
- [Extensible Application Markup Language](https://en.wikipedia.org/wiki/Extensible_Application_Markup_Language)
- [FLTK](https://en.wikipedia.org/wiki/FLTK)
- [File Transfer Protocol](https://en.wikipedia.org/wiki/File_Transfer_Protocol)
- [FXML](https://en.wikipedia.org/wiki/FXML)
- [FeatherPad](https://en.wikipedia.org/wiki/FeatherPad)
- [FireMonkey](https://en.wikipedia.org/wiki/FireMonkey)
- [Flutter (software)](https://en.wikipedia.org/wiki/Flutter_(software))
- [Fox toolkit](https://en.wikipedia.org/wiki/Fox_toolkit)
- [FpGUI](https://en.wikipedia.org/wiki/FpGUI)
- [Free software](https://en.wikipedia.org/wiki/Free_software)
- [Frescobaldi (software)](https://en.wikipedia.org/wiki/Frescobaldi_(software))
- [Fyne (software)](https://en.wikipedia.org/wiki/Fyne_(software))
- [GDK](https://en.wikipedia.org/wiki/GDK)
- [Graphical Network Simulator-3](https://en.wikipedia.org/wiki/Graphical_Network_Simulator-3)
- [GNU General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License)
- [GNU Lesser General Public License](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)
- [GNUstep](https://en.wikipedia.org/wiki/GNUstep)
- [GTK](https://en.wikipedia.org/wiki/GTK)
- [Graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface)
- [Graphical widget](https://en.wikipedia.org/wiki/Graphical_widget)
- [Gambas](https://en.wikipedia.org/wiki/Gambas)
- [Glade Interface Designer](https://en.wikipedia.org/wiki/Glade_Interface_Designer)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Google Closure Tools](https://en.wikipedia.org/wiki/Google_Closure_Tools)
- [Google Web Toolkit](https://en.wikipedia.org/wiki/Google_Web_Toolkit)
- [GTK](https://en.wikipedia.org/wiki/GTK)
- [Gtkmm](https://en.wikipedia.org/wiki/Gtkmm)
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [Haiku (operating system)](https://en.wikipedia.org/wiki/Haiku_(operating_system))
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [IOS](https://en.wikipedia.org/wiki/IOS)
- [IP Pascal](https://en.wikipedia.org/wiki/IP_Pascal)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [IUP (software)](https://en.wikipedia.org/wiki/IUP_(software))
- [Intuition (Amiga)](https://en.wikipedia.org/wiki/Intuition_(Amiga))
- [JQuery UI](https://en.wikipedia.org/wiki/JQuery_UI)
- [JUCE](https://en.wikipedia.org/wiki/JUCE)
- [JavaFX](https://en.wikipedia.org/wiki/JavaFX)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Java OpenGL](https://en.wikipedia.org/wiki/Java_OpenGL)
- [KDE](https://en.wikipedia.org/wiki/KDE)
- [KDE Partition Manager](https://en.wikipedia.org/wiki/KDE_Partition_Manager)
- [KDE Plasma](https://en.wikipedia.org/wiki/KDE_Plasma)
- [Kdenlive](https://en.wikipedia.org/wiki/Kdenlive)
- [Kivy (framework)](https://en.wikipedia.org/wiki/Kivy_(framework))
- [LXQt](https://en.wikipedia.org/wiki/LXQt)
- [Language binding](https://en.wikipedia.org/wiki/Language_binding)
- [Lazarus Component Library](https://en.wikipedia.org/wiki/Lazarus_Component_Library)
- [Leo (text editor)](https://en.wikipedia.org/wiki/Leo_(text_editor))
- [LessTif](https://en.wikipedia.org/wiki/LessTif)
- [LWJGL](https://en.wikipedia.org/wiki/LWJGL)
- [Lightweight User Interface Toolkit](https://en.wikipedia.org/wiki/Lightweight_User_Interface_Toolkit)
- [LilyPond](https://en.wikipedia.org/wiki/LilyPond)
- [Linux](https://en.wikipedia.org/wiki/Linux)
- [LispWorks](https://en.wikipedia.org/wiki/LispWorks)
- [List of language bindings for Qt 4](https://en.wikipedia.org/wiki/List_of_language_bindings_for_Qt_4)
- [List of language bindings for Qt 5](https://en.wikipedia.org/wiki/List_of_language_bindings_for_Qt_5)
- [List of widget toolkits](https://en.wikipedia.org/wiki/List_of_widget_toolkits)
- [Lively Kernel](https://en.wikipedia.org/wiki/Lively_Kernel)
- [Lua (programming language)](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [Lubuntu](https://en.wikipedia.org/wiki/Lubuntu)
- [Lumina (desktop environment)](https://en.wikipedia.org/wiki/Lumina_(desktop_environment))
- [MXML](https://en.wikipedia.org/wiki/MXML)
- [MacApp](https://en.wikipedia.org/wiki/MacApp)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [Macintosh Toolbox](https://en.wikipedia.org/wiki/Macintosh_Toolbox)
- [Magic User Interface](https://en.wikipedia.org/wiki/Magic_User_Interface)
- [MeeGo](https://en.wikipedia.org/wiki/MeeGo)
- [Mer (software distribution)](https://en.wikipedia.org/wiki/Mer_(software_distribution))
- [Meta-object System](https://en.wikipedia.org/wiki/Meta-object_System)
- [Microsoft Foundation Class Library](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library)
- [Microsoft Silverlight](https://en.wikipedia.org/wiki/Microsoft_Silverlight)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Microsoft XNA](https://en.wikipedia.org/wiki/Microsoft_XNA)
- [Model–view–controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
- [MonoGame](https://en.wikipedia.org/wiki/MonoGame)
- [Mono (software)](https://en.wikipedia.org/wiki/Mono_(software))
- [Moonlight (runtime)](https://en.wikipedia.org/wiki/Moonlight_(runtime))
- [Motif (software)](https://en.wikipedia.org/wiki/Motif_(software))
- [MySQL](https://en.wikipedia.org/wiki/MySQL)
- [Newt (programming library)](https://en.wikipedia.org/wiki/Newt_(programming_library))
- [Ninja-IDE](https://en.wikipedia.org/wiki/Ninja-IDE)
- [Nokia](https://en.wikipedia.org/wiki/Nokia)
- [Open Database Connectivity](https://en.wikipedia.org/wiki/Open_Database_Connectivity)
- [OLIT](https://en.wikipedia.org/wiki/OLIT)
- [Object Pascal](https://en.wikipedia.org/wiki/Object_Pascal)
- [Object Windows Library](https://en.wikipedia.org/wiki/Object_Windows_Library)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [OpenGL](https://en.wikipedia.org/wiki/OpenGL)
- [OpenGL](https://en.wikipedia.org/wiki/OpenGL)
- [OpenLP](https://en.wikipedia.org/wiki/OpenLP)
- [OpenShot](https://en.wikipedia.org/wiki/OpenShot)
- [OpenTK](https://en.wikipedia.org/wiki/OpenTK)
- [OpenUI5](https://en.wikipedia.org/wiki/OpenUI5)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Oracle Database](https://en.wikipedia.org/wiki/Oracle_Database)
- [Orange (software)](https://en.wikipedia.org/wiki/Orange_(software))
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PHP-GTK](https://en.wikipedia.org/wiki/PHP-GTK)
- [Parsing](https://en.wikipedia.org/wiki/Parsing)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Phonon (software)](https://en.wikipedia.org/wiki/Phonon_(software))
- [KDE Plasma 4](https://en.wikipedia.org/wiki/KDE_Plasma_4)
- [Plug-in (computing)](https://en.wikipedia.org/wiki/Plug-in_(computing))
- [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)
- [PowerPlant](https://en.wikipedia.org/wiki/PowerPlant)
- [Prentice Hall](https://en.wikipedia.org/wiki/Prentice_Hall)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Puddletag](https://en.wikipedia.org/wiki/Puddletag)
- [PyGTK](https://en.wikipedia.org/wiki/PyGTK)
- [PySide](https://en.wikipedia.org/wiki/PySide)
- [Pyjs](https://en.wikipedia.org/wiki/Pyjs)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [QGIS](https://en.wikipedia.org/wiki/QGIS)
- [QML](https://en.wikipedia.org/wiki/QML)
- [QNX](https://en.wikipedia.org/wiki/QNX)
- [Qbs (build tool)](https://en.wikipedia.org/wiki/Qbs_(build_tool))
- [Qmake](https://en.wikipedia.org/wiki/Qmake)
- [Qooxdoo](https://en.wikipedia.org/wiki/Qooxdoo)
- [Qt (software)](https://en.wikipedia.org/wiki/Qt_(software))
- [QtScript](https://en.wikipedia.org/wiki/QtScript)
- [Qt (software)](https://en.wikipedia.org/wiki/Qt_(software))
- [Qt (software)](https://en.wikipedia.org/wiki/Qt_(software))
- [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator)
- [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator)
- [QtJambi](https://en.wikipedia.org/wiki/QtJambi)
- [Qt Project](https://en.wikipedia.org/wiki/Qt_Project)
- [Qt Quick](https://en.wikipedia.org/wiki/Qt_Quick)
- [Qutebrowser](https://en.wikipedia.org/wiki/Qutebrowser)
- [ReAction GUI](https://en.wikipedia.org/wiki/ReAction_GUI)
- [RecordMyDesktop](https://en.wikipedia.org/wiki/RecordMyDesktop)
- [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Rogue Wave Software](https://en.wikipedia.org/wiki/Rogue_Wave_Software)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [SIP (software)](https://en.wikipedia.org/wiki/SIP_(software))
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [SQLite](https://en.wikipedia.org/wiki/SQLite)
- [Sailfish OS](https://en.wikipedia.org/wiki/Sailfish_OS)
- [SVG](https://en.wikipedia.org/wiki/SVG)
- [Scintilla (software)](https://en.wikipedia.org/wiki/Scintilla_(software))
- [Shared memory](https://en.wikipedia.org/wiki/Shared_memory)
- [Why the lucky stiff](https://en.wikipedia.org/wiki/Why_the_lucky_stiff)
- [Signals and slots](https://en.wikipedia.org/wiki/Signals_and_slots)
- [Simple API for XML](https://en.wikipedia.org/wiki/Simple_API_for_XML)
- [Simple DirectMedia Layer](https://en.wikipedia.org/wiki/Simple_DirectMedia_Layer)
- [Simple and Fast Multimedia Library](https://en.wikipedia.org/wiki/Simple_and_Fast_Multimedia_Library)
- [Scanner Access Now Easy](https://en.wikipedia.org/wiki/Scanner_Access_Now_Easy)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Spyder (software)](https://en.wikipedia.org/wiki/Spyder_(software))
- [Standard Widget Toolkit](https://en.wikipedia.org/wiki/Standard_Widget_Toolkit)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Swing (Java)](https://en.wikipedia.org/wiki/Swing_(Java))
- [THINK C](https://en.wikipedia.org/wiki/THINK_C)
- [Tao Framework](https://en.wikipedia.org/wiki/Tao_Framework)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Qt Group](https://en.wikipedia.org/wiki/Qt_Group)
- [Tk (software)](https://en.wikipedia.org/wiki/Tk_(software))
- [Tkinter](https://en.wikipedia.org/wiki/Tkinter)
- [Fox toolkit](https://en.wikipedia.org/wiki/Fox_toolkit)
- [TortoiseHg](https://en.wikipedia.org/wiki/TortoiseHg)
- [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
- [UIML](https://en.wikipedia.org/wiki/UIML)
- [Ultimate++](https://en.wikipedia.org/wiki/Ultimate%2B%2B)
- [Unicode](https://en.wikipedia.org/wiki/Unicode)
- [United Kingdom](https://en.wikipedia.org/wiki/United_Kingdom)
- [Universal Windows Platform](https://en.wikipedia.org/wiki/Universal_Windows_Platform)
- [Unix](https://en.wikipedia.org/wiki/Unix)
- [Unix shell](https://en.wikipedia.org/wiki/Unix_shell)
- [User Datagram Protocol](https://en.wikipedia.org/wiki/User_Datagram_Protocol)
- [VLC media player](https://en.wikipedia.org/wiki/VLC_media_player)
- [Veusz](https://en.wikipedia.org/wiki/Veusz)
- [Visual Component Library](https://en.wikipedia.org/wiki/Visual_Component_Library)
- [VxWorks](https://en.wikipedia.org/wiki/VxWorks)
- [Widget toolkit](https://en.wikipedia.org/wiki/Widget_toolkit)
- [Windows 10 Mobile](https://en.wikipedia.org/wiki/Windows_10_Mobile)
- [Windows API](https://en.wikipedia.org/wiki/Windows_API)
- [Windows Forms](https://en.wikipedia.org/wiki/Windows_Forms)
- [Windows Presentation Foundation](https://en.wikipedia.org/wiki/Windows_Presentation_Foundation)
- [Windows Runtime](https://en.wikipedia.org/wiki/Windows_Runtime)
- [Windows Template Library](https://en.wikipedia.org/wiki/Windows_Template_Library)
- [Windows UI Library](https://en.wikipedia.org/wiki/Windows_UI_Library)
- [Wt (web toolkit)](https://en.wikipedia.org/wiki/Wt_(web_toolkit))
- [WxHaskell](https://en.wikipedia.org/wiki/WxHaskell)
- [WxPHP](https://en.wikipedia.org/wiki/WxPHP)
- [List of language bindings for wxWidgets](https://en.wikipedia.org/wiki/List_of_language_bindings_for_wxWidgets)
- [WxPython](https://en.wikipedia.org/wiki/WxPython)
- [WxWidgets](https://en.wikipedia.org/wiki/WxWidgets)
- [XCB](https://en.wikipedia.org/wiki/XCB)
- [XForms (toolkit)](https://en.wikipedia.org/wiki/XForms_(toolkit))
- [XML](https://en.wikipedia.org/wiki/XML)
- [XUL](https://en.wikipedia.org/wiki/XUL)
- [XVT](https://en.wikipedia.org/wiki/XVT)
- [XView](https://en.wikipedia.org/wiki/XView)
- [X Athena Widgets](https://en.wikipedia.org/wiki/X_Athena_Widgets)
- [X Toolkit Intrinsics](https://en.wikipedia.org/wiki/X_Toolkit_Intrinsics)
- [X Window System](https://en.wikipedia.org/wiki/X_Window_System)
- [Xamarin](https://en.wikipedia.org/wiki/Xamarin)
- [Xlib](https://en.wikipedia.org/wiki/Xlib)
- [YUI Library](https://en.wikipedia.org/wiki/YUI_Library)
- [Zune (widget toolkit)](https://en.wikipedia.org/wiki/Zune_(widget_toolkit))
- [Template:Qt platform](https://en.wikipedia.org/wiki/Template:Qt_platform)
- [Template:Widget toolkits](https://en.wikipedia.org/wiki/Template:Widget_toolkits)
- [Template talk:Qt platform](https://en.wikipedia.org/wiki/Template_talk:Qt_platform)
- [Template talk:Widget toolkits](https://en.wikipedia.org/wiki/Template_talk:Widget_toolkits)
- [Category:KDE software](https://en.wikipedia.org/wiki/Category:KDE_software)
- [Category:Software that uses Qt](https://en.wikipedia.org/wiki/Category:Software_that_uses_Qt)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:51:27.882598+00:00_