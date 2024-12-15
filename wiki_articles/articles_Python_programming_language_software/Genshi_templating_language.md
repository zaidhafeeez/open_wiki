# Genshi (templating language)

## Article Metadata

- **Last Updated:** 2024-12-15T03:59:06.399611+00:00
- **Original Article:** [Genshi (templating language)](https://en.wikipedia.org/wiki/Genshi_(templating_language))
- **Language:** en
- **Page ID:** 8471397

## Summary

Genshi is a template engine for XML-based vocabularies written in 
Python.  Genshi is used to easily insert generated output into XML-based languages, usually HTML, and reuse elements between documents.  Genshi's syntax is based on Kid, but its architecture is different. Genshi aims to implement some of its functionality while processing templates faster, by dynamically processing templates using a stream based API, instead of compiling templates to Python code.
Genshi can be used with several P

## Categories

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

## Related Articles

### Internal Links

- [CherryPy](https://en.wikipedia.org/wiki/CherryPy)
- [Code generation (compiler)](https://en.wikipedia.org/wiki/Code_generation_(compiler))
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [HTML editor](https://en.wikipedia.org/wiki/HTML_editor)
- [Comparison of web template engines](https://en.wikipedia.org/wiki/Comparison_of_web_template_engines)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Web template system](https://en.wikipedia.org/wiki/Web_template_system)
- [TurboGears](https://en.wikipedia.org/wiki/TurboGears)
- [WYSIWYG](https://en.wikipedia.org/wiki/WYSIWYG)
- [Web2py](https://en.wikipedia.org/wiki/Web2py)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [XInclude](https://en.wikipedia.org/wiki/XInclude)
- [XML](https://en.wikipedia.org/wiki/XML)
- [XML namespace](https://en.wikipedia.org/wiki/XML_namespace)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:59:06.399611+00:00_