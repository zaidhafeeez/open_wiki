# Genshi (templating language)

## Metadata
- **Last Updated:** 2024-11-24 06:40:50 UTC
- **Original Article:** [Genshi (templating language)](https://en.wikipedia.org/wiki/Genshi_(templating_language))
- **Language:** en
- **Page ID:** 8471397

## Summary
Genshi is a template engine for XML-based vocabularies written in 
Python.  Genshi is used to easily insert generated output into XML-based languages, usually HTML, and reuse elements between documents.  Genshi's syntax is based on Kid, but its architecture is different. Genshi aims to implement some of its functionality while processing templates faster, by dynamically processing templates using a stream based API, instead of compiling templates to Python code.
Genshi can be used with several Python web frameworks, such as CherryPy, TurboGears, Pylons and web2py. Genshi was the default templating language for TurboGears from versions 1.1 to 2.3.8.

## Categories
This article belongs to the following categories:

- Category:Free software programmed in Python
- Category:Free system software
- Category:Official website different in Wikidata and Wikipedia
- Category:Python (programming language) libraries
- Category:Python (programming language) software
- Category:Scripting languages
- Category:Template engines

## Table of Contents

- Genshi markup
- Differences between Kid and Genshi
- References
- External links

## Content

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

## Archive Info
- **Archived on:** 2024-12-15 20:27:27 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 1440 bytes
- **Word Count:** 215 words
