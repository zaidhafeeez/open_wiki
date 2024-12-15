# Docstring

## Article Metadata

- **Last Updated:** 2024-12-15T03:15:41.224129+00:00
- **Original Article:** [Docstring](https://en.wikipedia.org/wiki/Docstring)
- **Language:** en
- **Page ID:** 4225907

## Summary

In programming, a docstring is a string literal specified in source code that is used, like a comment, to document a specific segment of code. Unlike conventional source code comments, or even specifically formatted comments like docblocks, docstrings are not stripped from the source tree when it is parsed and are retained throughout the runtime of the program. This allows the programmer to inspect these comments at run time, for instance as an interactive help system, or as metadata.
Languages 

## Categories

- Category:Articles with short description
- Category:Lisp (programming language)
- Category:Programming constructs
- Category:Python (programming language)
- Category:Short description matches Wikidata
- Category:Source code documentation formats
- Category:String (computer science)

## Table of Contents

- Implementation examples
- Tools using docstrings
- See also
- References
- External links

## Content

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

## Related Articles

### Internal Links

- [Clojure](https://en.wikipedia.org/wiki/Clojure)
- [Cobra (programming language)](https://en.wikipedia.org/wiki/Cobra_(programming_language))
- [Comment (computer programming)](https://en.wikipedia.org/wiki/Comment_(computer_programming))
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [Comment (computer programming)](https://en.wikipedia.org/wiki/Comment_(computer_programming))
- [Doctest](https://en.wikipedia.org/wiki/Doctest)
- [Doxygen](https://en.wikipedia.org/wiki/Doxygen)
- [Elixir (programming language)](https://en.wikipedia.org/wiki/Elixir_(programming_language))
- [Epydoc](https://en.wikipedia.org/wiki/Epydoc)
- [Cucumber (software)](https://en.wikipedia.org/wiki/Cucumber_(software))
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Julia (programming language)](https://en.wikipedia.org/wiki/Julia_(programming_language))
- [Lisp (programming language)](https://en.wikipedia.org/wiki/Lisp_(programming_language))
- [Literate programming](https://en.wikipedia.org/wiki/Literate_programming)
- [Markdown](https://en.wikipedia.org/wiki/Markdown)
- [Markup language](https://en.wikipedia.org/wiki/Markup_language)
- [Metadata](https://en.wikipedia.org/wiki/Metadata)
- [Parsing](https://en.wikipedia.org/wiki/Parsing)
- [Plain Old Documentation](https://en.wikipedia.org/wiki/Plain_Old_Documentation)
- [Pydoc](https://en.wikipedia.org/wiki/Pydoc)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Execution (computing)](https://en.wikipedia.org/wiki/Execution_(computing))
- [SourceForge](https://en.wikipedia.org/wiki/SourceForge)
- [Source code](https://en.wikipedia.org/wiki/Source_code)
- [Sphinx (documentation generator)](https://en.wikipedia.org/wiki/Sphinx_(documentation_generator))
- [String literal](https://en.wikipedia.org/wiki/String_literal)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:15:41.224129+00:00_