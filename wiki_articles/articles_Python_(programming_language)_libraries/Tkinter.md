# Tkinter

## Article Metadata

- **Last Updated:** 2024-12-14T19:52:34.491229+00:00
- **Original Article:** [Tkinter](https://en.wikipedia.org/wiki/Tkinter)
- **Language:** en
- **Page ID:** 2770036

## Summary

Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI. Tkinter is included with standard Linux, Microsoft Windows and macOS installs of Python.
The name Tkinter comes from Tk interface. Tkinter was written by Steen Lumholt and Guido van Rossum, then later revised by Fredrik Lundh.
Tkinter is free software released under a Python license.

## Categories

- Category:Articles with short description
- Category:Python (programming language) libraries
- Category:Short description is different from Wikidata
- Category:Tk (software)

## Table of Contents

- Description
- A minimal application
- See also
- References
- External links

## Content

Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI. Tkinter is included with standard Linux, Microsoft Windows and macOS installs of Python.
The name Tkinter comes from Tk interface. Tkinter was written by Steen Lumholt and Guido van Rossum, then later revised by Fredrik Lundh.
Tkinter is free software released under a Python license.

Description
As with most other modern Tk bindings, Tkinter is implemented as a Python wrapper around a complete Tcl interpreter embedded in the Python interpreter. Tkinter calls are translated into Tcl commands, which are fed to this embedded interpreter, thus making it possible to mix Python and Tcl in a single application.
There are several popular GUI library alternatives available, such as Kivy, Pygame, Pyglet, PyGObject, PyQt, PySide, and wxPython.

Some definitions
Window
This term has different meanings in different contexts, but in general it refers to a rectangular area somewhere on the user's display screen.

Top-level window
A window which acts as a child of the primary window. It will be decorated with the standard frame and controls for the desktop manager. It can be moved around the desktop and can usually be resized.

Widget
The generic term for any of the building blocks that make up an application in a graphical user interface.

Core widgets: The containers: frame, labelframe, toplevel, paned window. The buttons: button, radiobutton, checkbutton (checkbox), and menubutton. The text widgets: label, message, text.  The entry widgets: scale, scrollbar, listbox, slider, spinbox, entry (singleline), optionmenu, text (multiline), and canvas (vector and pixel graphics).
Tkinter provides three modules that allow pop-up dialogs to be displayed: tk.messagebox (confirmation, information, warning and error dialogs), tk.filedialog (single file, multiple file and directory selection dialogs) and tk.colorchooser (colour picker).
Python 2.7 and Python 3.1 incorporate the "themed Tk" ("ttk") functionality of Tk 8.5. This allows Tk widgets to be easily themed to look like the native desktop environment in which the application is running, thereby addressing a long-standing criticism of Tk (and hence of Tkinter). Some widgets are exclusive to ttk, such as the combobox, progressbar, treeview, notebook, separator and sizegrip.

Frame
In Tkinter, the Frame widget is the basic unit of organization for complex layouts. A frame is a rectangular area that can contain other widgets.

Child and parent
When any widget is created, a parent–child relationship is created. For example, if you place a text label inside a frame, the frame is the parent of the label.

A minimal application
Here is a minimal Python 3 Tkinter application with one widget:

For Python 2, the only difference is the word "tkinter" in the import command will be capitalized to "Tkinter".

Process
There are four stages to creating a widget

Create
create it within a frame
Configure
change the widgets attributes.
Pack
pack it into position so it becomes visible. Developers also have the option to use .grid() (row=int, column=int to define rows and columns to position the widget, defaults to 0) and .place() (relx=int or decimal, rely=int or decimal, define coordinates in the frame, or window).
Bind
bind it to a function or event.
These are often compressed, and the order can vary.

Simple application
Using the object-oriented paradigm in Python, a simple program would be (requires Tcl version 8.6, which is not used by Python on MacOS by default):

line 1: Hashbang directive to the program launcher, allowing the selection of an appropriate interpreter executable, when self-executing.
line 2: Imports the tkinter module into your program's namespace, but renames it as tk.
line 5: The application class inherits from Tkinter's Frame class.
line 7: Defines the function that sets up the Frame.
line 8: Calls the constructor for the parent class, Frame.
line 12: Defining the widgets.
line 13: Creates a label, named MedialLabel with the text "Hello World".
line 14: Sets the MedialLabel background colour to cyan.
line 15: Places the label on the application so it is visible using the grid geometry manager method.
line 16: Creates a button labeled “Quit”.
line 17: Places the button on the application. Grid, place and pack are all methods of making the widget visible.
line 20: The main program starts here by instantiating the Application class.
line 21: Creates main window app.root as a Tk object.
line 22: This method call sets the title of the window to “Sample application”.
line 23: Starts the application's main loop, waiting for mouse and keyboard events.

See also
IDLE — integrated development environment in Python, written exclusively using Tkinter

References
External links
TkInter, Python Wiki
Tkinter GUI Tutorial, covers each widget individually.
TkDocs: includes language-neutral and Python-specific information and a tutorial
John Shipman, Tkinter 8.5 reference: a GUI for Python
Ferg, Stephen, Thinking in Tkinter

## Related Articles

### Internal Links

- [.NET](https://en.wikipedia.org/wiki/.NET)
- [Abstract Window Toolkit](https://en.wikipedia.org/wiki/Abstract_Window_Toolkit)
- [Active Template Library](https://en.wikipedia.org/wiki/Active_Template_Library)
- [Adobe Flash](https://en.wikipedia.org/wiki/Adobe_Flash)
- [Allegro Common Lisp](https://en.wikipedia.org/wiki/Allegro_Common_Lisp)
- [AmigaOS](https://en.wikipedia.org/wiki/AmigaOS)
- [Android (operating system)](https://en.wikipedia.org/wiki/Android_(operating_system))
- [Android software development](https://en.wikipedia.org/wiki/Android_software_development)
- [Apache Flex](https://en.wikipedia.org/wiki/Apache_Flex)
- [BOOPSI](https://en.wikipedia.org/wiki/BOOPSI)
- [BeOS](https://en.wikipedia.org/wiki/BeOS)
- [BeOS](https://en.wikipedia.org/wiki/BeOS)
- [Bedrock (framework)](https://en.wikipedia.org/wiki/Bedrock_(framework))
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CDK (programming library)](https://en.wikipedia.org/wiki/CDK_(programming_library))
- [CEGUI](https://en.wikipedia.org/wiki/CEGUI)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Carbon (API)](https://en.wikipedia.org/wiki/Carbon_(API))
- [Classic Mac OS](https://en.wikipedia.org/wiki/Classic_Mac_OS)
- [Cocoa (API)](https://en.wikipedia.org/wiki/Cocoa_(API))
- [UIKit](https://en.wikipedia.org/wiki/UIKit)
- [Common Language Infrastructure](https://en.wikipedia.org/wiki/Common_Language_Infrastructure)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Common Lisp Interface Manager](https://en.wikipedia.org/wiki/Common_Lisp_Interface_Manager)
- [Component Library for Cross Platform](https://en.wikipedia.org/wiki/Component_Library_for_Cross_Platform)
- [Dart (programming language)](https://en.wikipedia.org/wiki/Dart_(programming_language))
- [De facto standard](https://en.wikipedia.org/wiki/De_facto_standard)
- [Desktop environment](https://en.wikipedia.org/wiki/Desktop_environment)
- [Dialog (software)](https://en.wikipedia.org/wiki/Dialog_(software))
- [Dojo Toolkit](https://en.wikipedia.org/wiki/Dojo_Toolkit)
- [Echo (framework)](https://en.wikipedia.org/wiki/Echo_(framework))
- [Enlightenment Foundation Libraries](https://en.wikipedia.org/wiki/Enlightenment_Foundation_Libraries)
- [Ext JS](https://en.wikipedia.org/wiki/Ext_JS)
- [Extensible Application Markup Language](https://en.wikipedia.org/wiki/Extensible_Application_Markup_Language)
- [FLTK](https://en.wikipedia.org/wiki/FLTK)
- [FXML](https://en.wikipedia.org/wiki/FXML)
- [FireMonkey](https://en.wikipedia.org/wiki/FireMonkey)
- [Flutter (software)](https://en.wikipedia.org/wiki/Flutter_(software))
- [Fox toolkit](https://en.wikipedia.org/wiki/Fox_toolkit)
- [FpGUI](https://en.wikipedia.org/wiki/FpGUI)
- [Free software](https://en.wikipedia.org/wiki/Free_software)
- [Fyne (software)](https://en.wikipedia.org/wiki/Fyne_(software))
- [GDK](https://en.wikipedia.org/wiki/GDK)
- [GNUstep](https://en.wikipedia.org/wiki/GNUstep)
- [GTK](https://en.wikipedia.org/wiki/GTK)
- [Glade Interface Designer](https://en.wikipedia.org/wiki/Glade_Interface_Designer)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Google Closure Tools](https://en.wikipedia.org/wiki/Google_Closure_Tools)
- [Google Web Toolkit](https://en.wikipedia.org/wiki/Google_Web_Toolkit)
- [Graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface)
- [GTK](https://en.wikipedia.org/wiki/GTK)
- [Gtkmm](https://en.wikipedia.org/wiki/Gtkmm)
- [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
- [Haiku (operating system)](https://en.wikipedia.org/wiki/Haiku_(operating_system))
- [Shebang (Unix)](https://en.wikipedia.org/wiki/Shebang_(Unix))
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [IDLE](https://en.wikipedia.org/wiki/IDLE)
- [IP Pascal](https://en.wikipedia.org/wiki/IP_Pascal)
- [IUP (software)](https://en.wikipedia.org/wiki/IUP_(software))
- [Interpreter (computing)](https://en.wikipedia.org/wiki/Interpreter_(computing))
- [Interpreter directive](https://en.wikipedia.org/wiki/Interpreter_directive)
- [Intuition (Amiga)](https://en.wikipedia.org/wiki/Intuition_(Amiga))
- [JQuery UI](https://en.wikipedia.org/wiki/JQuery_UI)
- [JUCE](https://en.wikipedia.org/wiki/JUCE)
- [JavaFX](https://en.wikipedia.org/wiki/JavaFX)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Java OpenGL](https://en.wikipedia.org/wiki/Java_OpenGL)
- [Kivy (framework)](https://en.wikipedia.org/wiki/Kivy_(framework))
- [Language binding](https://en.wikipedia.org/wiki/Language_binding)
- [Language interpretation](https://en.wikipedia.org/wiki/Language_interpretation)
- [Lazarus Component Library](https://en.wikipedia.org/wiki/Lazarus_Component_Library)
- [LessTif](https://en.wikipedia.org/wiki/LessTif)
- [LWJGL](https://en.wikipedia.org/wiki/LWJGL)
- [Lightweight User Interface Toolkit](https://en.wikipedia.org/wiki/Lightweight_User_Interface_Toolkit)
- [Linux](https://en.wikipedia.org/wiki/Linux)
- [LispWorks](https://en.wikipedia.org/wiki/LispWorks)
- [List of widget toolkits](https://en.wikipedia.org/wiki/List_of_widget_toolkits)
- [Lively Kernel](https://en.wikipedia.org/wiki/Lively_Kernel)
- [Lua (programming language)](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [MXML](https://en.wikipedia.org/wiki/MXML)
- [MacApp](https://en.wikipedia.org/wiki/MacApp)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [Macintosh Toolbox](https://en.wikipedia.org/wiki/Macintosh_Toolbox)
- [Magic User Interface](https://en.wikipedia.org/wiki/Magic_User_Interface)
- [Microsoft Foundation Class Library](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library)
- [Microsoft Silverlight](https://en.wikipedia.org/wiki/Microsoft_Silverlight)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Microsoft XNA](https://en.wikipedia.org/wiki/Microsoft_XNA)
- [MonoGame](https://en.wikipedia.org/wiki/MonoGame)
- [Mono (software)](https://en.wikipedia.org/wiki/Mono_(software))
- [Moonlight (runtime)](https://en.wikipedia.org/wiki/Moonlight_(runtime))
- [Motif (software)](https://en.wikipedia.org/wiki/Motif_(software))
- [Newt (programming library)](https://en.wikipedia.org/wiki/Newt_(programming_library))
- [OLIT](https://en.wikipedia.org/wiki/OLIT)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object Pascal](https://en.wikipedia.org/wiki/Object_Pascal)
- [Object Windows Library](https://en.wikipedia.org/wiki/Object_Windows_Library)
- [Objective-C](https://en.wikipedia.org/wiki/Objective-C)
- [OpenGL](https://en.wikipedia.org/wiki/OpenGL)
- [OpenTK](https://en.wikipedia.org/wiki/OpenTK)
- [OpenUI5](https://en.wikipedia.org/wiki/OpenUI5)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PHP-GTK](https://en.wikipedia.org/wiki/PHP-GTK)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [PowerPlant](https://en.wikipedia.org/wiki/PowerPlant)
- [PyGTK](https://en.wikipedia.org/wiki/PyGTK)
- [PyGTK](https://en.wikipedia.org/wiki/PyGTK)
- [PyQt](https://en.wikipedia.org/wiki/PyQt)
- [PySide](https://en.wikipedia.org/wiki/PySide)
- [Pygame](https://en.wikipedia.org/wiki/Pygame)
- [Pyglet](https://en.wikipedia.org/wiki/Pyglet)
- [Pyjs](https://en.wikipedia.org/wiki/Pyjs)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python License](https://en.wikipedia.org/wiki/Python_License)
- [Qooxdoo](https://en.wikipedia.org/wiki/Qooxdoo)
- [Qt (software)](https://en.wikipedia.org/wiki/Qt_(software))
- [Qt (software)](https://en.wikipedia.org/wiki/Qt_(software))
- [QtJambi](https://en.wikipedia.org/wiki/QtJambi)
- [ReAction GUI](https://en.wikipedia.org/wiki/ReAction_GUI)
- [Rogue Wave Software](https://en.wikipedia.org/wiki/Rogue_Wave_Software)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Why the lucky stiff](https://en.wikipedia.org/wiki/Why_the_lucky_stiff)
- [Simple DirectMedia Layer](https://en.wikipedia.org/wiki/Simple_DirectMedia_Layer)
- [Simple and Fast Multimedia Library](https://en.wikipedia.org/wiki/Simple_and_Fast_Multimedia_Library)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Standard Widget Toolkit](https://en.wikipedia.org/wiki/Standard_Widget_Toolkit)
- [Swift (programming language)](https://en.wikipedia.org/wiki/Swift_(programming_language))
- [Swing (Java)](https://en.wikipedia.org/wiki/Swing_(Java))
- [THINK C](https://en.wikipedia.org/wiki/THINK_C)
- [Tao Framework](https://en.wikipedia.org/wiki/Tao_Framework)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Tk (software)](https://en.wikipedia.org/wiki/Tk_(software))
- [Fox toolkit](https://en.wikipedia.org/wiki/Fox_toolkit)
- [UIML](https://en.wikipedia.org/wiki/UIML)
- [Ultimate++](https://en.wikipedia.org/wiki/Ultimate%2B%2B)
- [Universal Windows Platform](https://en.wikipedia.org/wiki/Universal_Windows_Platform)
- [Unix](https://en.wikipedia.org/wiki/Unix)
- [Unix shell](https://en.wikipedia.org/wiki/Unix_shell)
- [Visual Component Library](https://en.wikipedia.org/wiki/Visual_Component_Library)
- [WIMP (computing)](https://en.wikipedia.org/wiki/WIMP_(computing))
- [Widget toolkit](https://en.wikipedia.org/wiki/Widget_toolkit)
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
- [Template:Widget toolkits](https://en.wikipedia.org/wiki/Template:Widget_toolkits)
- [Template talk:Widget toolkits](https://en.wikipedia.org/wiki/Template_talk:Widget_toolkits)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:52:34.491229+00:00_