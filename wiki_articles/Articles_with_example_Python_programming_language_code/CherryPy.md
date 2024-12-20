---
title: CherryPy
url: https://en.wikipedia.org/wiki/CherryPy
language: en
categories: ["Category:All articles with self-published sources", "Category:Articles with example Python (programming language) code", "Category:Articles with self-published sources from April 2024", "Category:Articles with short description", "Category:Free computer libraries", "Category:Free software programmed in Python", "Category:Python (programming language) web frameworks", "Category:Short description matches Wikidata", "Category:Software using the BSD license", "Category:Webarchive template wayback links"]
references: 0
last_modified: 2024-12-19T13:50:06Z
---

# CherryPy

## Summary

CherryPy is an object-oriented web application framework using the Python programming language. It is designed for rapid development of web applications by wrapping the HTTP protocol but stays at a low level and does not offer much more than what is defined in RFC 7231.
CherryPy can be a web server itself or one can launch it via any WSGI compatible environment. It does not deal with tasks such as templating for output rendering or backend access. The framework is extensible with filters, which 

## Full Content

CherryPy is an object-oriented web application framework using the Python programming language. It is designed for rapid development of web applications by wrapping the HTTP protocol but stays at a low level and does not offer much more than what is defined in RFC 7231.
CherryPy can be a web server itself or one can launch it via any WSGI compatible environment. It does not deal with tasks such as templating for output rendering or backend access. The framework is extensible with filters, which are called at defined points in the request/response processing.

Pythonic interface
One of the goals of the project founder, Remi Delon, was to make CherryPy as pythonic as possible. This allows the developer to use the framework as any regular Python module and to forget (from a technical point of view) that the application is for the web.
For instance, the common Hello World program with CherryPy 3 would look like:

Features
CherryPy implements:

A HTTP/1.1-compliant, WSGI thread-pooled webserver. Typically, CherryPy itself takes only 1–2 ms per page.
Support for any other WSGI-enabled web server or adapter, including Apache, IIS, lighttpd, mod_python, FastCGI, SCGI, and mod_wsgi.
A native mod_python adapter.
Multiple HTTP servers (e.g. ability to listen on multiple ports).
A plugin system CherryPy plugins hook into events within the server process — into server startup, server shutdown, server exiting, etc. — to run code that needs to be run when the server starts up or shuts down.
Built-in tools for caching, encoding, sessions, authorization, static content, and others. CherryPy tools hook into events within the request process. Whenever the CherryPy server receives a request, there is a specific set of steps it goes through to handle that request. Page handlers are only one step in the process.  Tools also provide a syntax and configuration API for turning them on and off for a specific set of handlers.
A configuration system for developers and deployers . CherryPy deployments are configurable on site, on application and on controller level, through Python dictionaries, configuration files, and open file objects.
A complete test suite for core functionality and associated framework which can be used to test CherryPy applications.
Built-in profiling since v2.1, coverage and testing support.
CherryPy doesn't force you to use a specific object-relational mapper (ORM), template language or JavaScript library.

Can be used with CherryPy
Routes — a Python re-implementation of the Ruby on Rails's routes system for mapping URLs to controllers/actions and generating URLs.

Object-relational mappers
SQLAlchemy — a database backend and ORM for Python applications. TurboGears 2.x uses CherryPy as server and SQLAlchemy as its default ORM.
SQLObject — a popular ORM for providing an object interface to a database. Supports a number of common database backends: included in the distribution are MySQL, PostgreSQL, SQLite, Sybase SQL Server, MaxDB, Microsoft SQL Server and Firebird. TurboGears 1.x uses CherryPy as server and SQLObject as ORM.
Storm — the ORM from Canonical Ltd. (makers of Ubuntu)
Dejavu — a public domain software, thread-safe ORM for Python applications
MongoEngine — An ODM for connecting to MongoDB.

Templating languages
Mako — a template library written in Python, usable with a simple CherryPy tool.
Cheetah — an open source template engine and code generation tool, written in Python.
CherryTemplate — a templating language for CherryPy.
Genshi — a powerful XML templating language.
Jinja — a general purpose templating language. CherryPy has a tool for using Jinja templates.
Kid — a simple template language for XML based vocabularies written in Python. TurboGears 1.x uses CherryPy as server and Kid as frontend.
CherryPy wiki helps choosing a templating language.

Products using CherryPy
TurboGears — CherryPy 2.x is a main component of TurboGears 1.x.
Splunk Enterprise - CherryPy 3.1.2

See also
Comparison of web frameworks

References
External links
Official website
