# Tkinter

## Metadata
- **Last Updated:** 2024-12-06 05:02:28 UTC
- **Original Article:** [Tkinter](https://en.wikipedia.org/wiki/Tkinter)
- **Language:** en
- **Page ID:** 2770036

## Summary
Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI. Tkinter is included with standard Linux, Microsoft Windows and macOS installs of Python.
The name Tkinter comes from Tk interface. Tkinter was written by Steen Lumholt and Guido van Rossum, then later revised by Fredrik Lundh.
Tkinter is free software released under a Python license.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 20:27:37 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 5095 bytes
- **Word Count:** 796 words
