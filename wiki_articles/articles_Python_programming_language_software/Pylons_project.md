# Pylons project

## Metadata
- **Last Updated:** 2024-12-15 04:18:52 UTC
- **Original Article:** [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- **Language:** en
- **Page ID:** 36723720

## Summary
Pylons Project is an open-source organization that develops a set of web application technologies written in Python. Initially the project was a single web framework called Pylons, but after the merger with the repoze.bfg framework under the new name Pyramid, the Pylons Project now consists of multiple related web application technologies.

## Categories
This article belongs to the following categories:

- Category:Articles with short description
- Category:Cross-platform free software
- Category:Free software programmed in Python
- Category:Python (programming language) software
- Category:Python (programming language) web frameworks
- Category:Short description is different from Wikidata
- Category:Webarchive template wayback links

## Table of Contents

- Pyramid
- Pylons Web Framework
- See also
- References
- External links

## Content

Pylons Project is an open-source organization that develops a set of web application technologies written in Python. Initially the project was a single web framework called Pylons, but after the merger with the repoze.bfg framework under the new name Pyramid, the Pylons Project now consists of multiple related web application technologies.

Pyramid
Pyramid is an open source web framework written in Python and is based on WSGI. It is a minimalistic web framework inspired by Zope, Pylons and Django.
Originally called "repoze.bfg", Pyramid gathered attention mostly in the Zope and Plone community as the Open Society Institute's KARL project migrated from Plone to BFG. In 2010 it was announced that the Pylons framework will move over to using BFG as a base in version 1.5. As a result of the inclusion of BFG into the Pylons project, BFG was renamed Pyramid.

Features
Pyramid is a minimalistic, platform-independent web framework. It is persistence agnostic and is integrated both with SQL databases via SQLAlchemy and with the Zope Object Database, as well as other NoSQL databases, such as CouchDB.
Pyramid allows developers to define routes using regular expressions that map to objects. Like its fellow framework Zope, Pyramid also allows hierarchical object traversal, where each part of a URL is an object containing other objects, in a way that is similar to folders in a filesystem.

Pylons Web Framework
Pylons Framework is an open-source Web application framework written in Python. It makes extensive use of the Web Server Gateway Interface standard to promote reusability and to separate functionality into distinct modules. It is strongly influenced by Ruby on Rails: two of its main components, Routes and WebHelpers, are Python reimplementations of Rails features.

Structure
Pylons is well known for having a near-complete stack of third-party tools, eschewing the "not-invented-here" phenomenon.

Installation, dependencies, and setup
The official installation method of Pylons is through EasyInstall via the Python Package Index (PyPI), and most of the additional tools are typically installed the same way. EasyInstall also handles package dependencies when relevant. Some distributions could also package Pylons and Paste, but it is likely that any distribution's packages would lag the official distribution. Pylons may also be installed by hand by renaming its .egg file to .zip and extracting the contents.
Paste is used for project setup, testing, and deployment. Using the common INI configuration format, Paste allows for multiple "profiles", so that developers can run development and deployment setups from the same codebase without revealing sensitive parts of Pylons, such as the interactive debugger, to production users.

URL dispatch
Currently the only widely used URL dispatcher for Pylons is Routes, a Python reimplementation of Ruby on Rails' URL dispatching, although any WSGI-compatible URL dispatcher can be used.  While Routes is a separate library, it was developed for use in Pylons and its development remains closely in sync with Pylons.

HTML generation
Another piece of Rails adapted for Pylons is WebHelpers, which provides URL mapping based on the Routes configuration. WebHelpers also provides some utility functions for generating JavaScript code making use of the script.aculo.us and Prototype libraries.
FormEncode and FormBuild are used for HTML form validation and generation; there has been some use of Mako for form generation using Mako's inheritance model.

Templating
Myghty was the default Pylons templating language, but as of version 0.9.6 it has been replaced by Mako. Both templating languages are text-based (as opposed to XML-based), and support includes, inheritance and embedding arbitrary Python code.
Because of Pylons' loosely coupled layers, other templating languages can be used as well. Genshi, an XML-based templating language, can be used in lieu of either Mako or Myghty.

Database abstraction and object-relational mapping
Pylons has no default database library. Both SQLObject and SQLAlchemy are known to be used.

Merger with repoze.bfg and birth of Pyramid Web Framework
Pylons has developed into the Pylons Project, and the old code from Pylons 1.0 is now in maintenance-only mode. However, pursuant to the project's merger with repoze.bfg since November 2010, newer versions of Pylons are actually different from the original Pylons 1.0. Pylons developers initially planned to rewrite certain portions of the code, but they observed that the new code was approximating repoze.bfg, which led to the merger of Pylons and repoze.bfg. This led to repoze.bfg (a part of the Repoze Python-based web framework) to become rebranded and relaunched as the Pyramid web framework.

See also
Django (web framework)
FastAPI
Flask (web framework)
Web2py
TurboGears: a derivative project, built on top of Pylons
Tornado
Comparison of web frameworks

References
Further reading
Gardner, James (January 2009). The Definitive Guide to Pylons. Berkeley, CA: Apress. doi:10.1007/978-1-4302-0534-0. ISBN 978-1-59059-934-1.

External links
Official website

## Archive Info
- **Archived on:** 2024-12-15 20:28:01 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 5124 bytes
- **Word Count:** 772 words
