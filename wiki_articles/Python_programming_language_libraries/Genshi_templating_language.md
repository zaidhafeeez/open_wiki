---
title: Genshi (templating language)
url: https://en.wikipedia.org/wiki/Genshi_(templating_language)
language: en
categories: ["Category:Free software programmed in Python", "Category:Free system software", "Category:Official website different in Wikidata and Wikipedia", "Category:Python (programming language) libraries", "Category:Python (programming language) software", "Category:Scripting languages", "Category:Template engines"]
references: 0
last_modified: 2024-11-24T06:40:50Z
---

# Genshi (templating language)

## Summary

Genshi is a template engine for XML-based vocabularies written in 
Python.  Genshi is used to easily insert generated output into XML-based languages, usually HTML, and reuse elements between documents.  Genshi's syntax is based on Kid, but its architecture is different. Genshi aims to implement some of its functionality while processing templates faster, by dynamically processing templates using a stream based API, instead of compiling templates to Python code.
Genshi can be used with several P

## Full Content

Genshi is a template engine for XML-based vocabularies written in 
Python.  Genshi is used to easily insert generated output into XML-based languages, usually HTML, and reuse elements between documents.  Genshi's syntax is based on Kid, but its architecture is different. Genshi aims to implement some of its functionality while processing templates faster, by dynamically processing templates using a stream based API, instead of compiling templates to Python code.
Genshi can be used with several Python web frameworks, such as CherryPy, TurboGears, Pylons and web2py. Genshi was the default templating language for TurboGears from versions 1.1 to 2.3.8.

Genshi markup
Genshi makes use of namespaces to embed instructions into HTML.  A typical instruction is given as an attribute, with a Python expression inside the quotes.  For example, the following will render a paragraph that shows 4:

Because of the use of namespaces, Genshi can be used in WYSIWYG HTML editors.

Differences between Kid and Genshi
Genshi directly interprets templates (unlike Kid, which generates Python code)
Genshi uses XInclude for template reuse
Genshi adds attributes Kid does not have, like py:choose
Genshi templates are easier to debug, because it tracks template source file names and line numbers, and errors from Genshi's interpreter produce more comprehensible stack traces than from Kid's generated code.

References
External links
Official website
