---
title: Docstring
url: https://en.wikipedia.org/wiki/Docstring
language: en
categories: ["Category:Articles with short description", "Category:Lisp (programming language)", "Category:Programming constructs", "Category:Python (programming language)", "Category:Short description matches Wikidata", "Category:Source code documentation formats", "Category:String (computer science)"]
references: 0
last_modified: 2024-12-19T13:54:14Z
---

# Docstring

## Summary

In programming, a docstring is a string literal specified in source code that is used, like a comment, to document a specific segment of code. Unlike conventional source code comments, or even specifically formatted comments like docblocks, docstrings are not stripped from the source tree when it is parsed and are retained throughout the runtime of the program. This allows the programmer to inspect these comments at run time, for instance as an interactive help system, or as metadata.
Languages 

## Full Content

In programming, a docstring is a string literal specified in source code that is used, like a comment, to document a specific segment of code. Unlike conventional source code comments, or even specifically formatted comments like docblocks, docstrings are not stripped from the source tree when it is parsed and are retained throughout the runtime of the program. This allows the programmer to inspect these comments at run time, for instance as an interactive help system, or as metadata.
Languages that support docstrings include Python, Lisp, Elixir, Clojure, Gherkin, Julia and Haskell.

Implementation examples
Elixir
Documentation is supported at language level, in the form of docstrings. Markdown is Elixir's de facto markup language of choice for use in docstrings:

Lisp
In Lisp, docstrings are known as documentation strings. The Common Lisp standard states that a particular implementation may choose to discard docstrings whenever they want, for whatever reason. When they are kept, docstrings may be viewed and changed using the DOCUMENTATION function. For instance:

Python
The common practice of documenting a code object at the head of its definition is captured by the addition of docstring syntax in the Python language.
The docstring for a Python code object (a module, class, or function) is the first statement of that code object, immediately following the definition (the 'def' or 'class' statement). The statement must be a bare string literal, not any other kind of expression. The docstring for the code object is available on that code object's __doc__ attribute and through the help function.
The following Python file shows the declaration of docstrings within a Python source file:

Assuming that the above code was saved as mymodule.py, the following is an interactive session showing how the docstrings may be accessed:

Tools using docstrings
cobra -doc (Cobra)
doctest (Python)
Epydoc (Python)
Pydoc (Python)
Sphinx (Python)

See also
Literate programming – alternative code commenting paradigm
Plain Old Documentation – Perl documentation

References
External links
Python Docstrings at Epydoc's SourceForge page
Documentation in GNU Emacs Lisp
Section from the doxygen documentation about Python docstrings
