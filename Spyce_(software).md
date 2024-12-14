# Spyce (software)

_Last updated: 2024-12-14T15:20:35.717726_

**Original Article:** [Spyce (software)](https://en.wikipedia.org/wiki/Spyce_(software))

**Summary:** Spyce is technology similar to PHP that can be used to embed Python code into webpages.  Spyce is free software, distributed under a BSD-style licence, with some additional restrictions about documentation notices.

## Categories
- Category:All articles needing additional references
- Category:All stub articles
- Category:Articles needing additional references from May 2021
- Category:Free computer programming tools
- Category:Official website different in Wikidata and Wikipedia
- Category:Programming language topic stubs
- Category:Python (programming language)

## Content

Spyce is technology similar to PHP that can be used to embed Python code into webpages.  Spyce is free software, distributed under a BSD-style licence, with some additional restrictions about documentation notices.

Common Spyce embedding methods
Since Python uses indentation to determine the beginning and end of a block, Spyce includes several ways to embed Python code. Shown below are the three most common ways. Spyce supports ASP/JSP-style delimiters (<% and %>) as well as double braces ([[ and ]])

The techniques above can be freely mixed and embedded in any HTML document.
Any legal Python code can be embedded and any Python module can be imported, which makes it especially suited for writing very robust applications (using exception handling and unit testing single modules individually).

Features
Some other features include custom tags (ala JSP), spyce lambdas and active handlers (reminiscent of ASP).

Requirements
Spyce brings Python's standard library and the programming language itself to the web. The minimum requirement is a working Python installation (it ships with a standalone web server written in Python that can be used during development), although it can be used in conjunction with several web servers such as Apache and IIS in a variety of ways.
Configuration is done using Python modules that are imported by the web server during initialization, so all that is really required to get started with Spyce is basic knowledge of Python.

See also
mod_python

References
External links
Official website