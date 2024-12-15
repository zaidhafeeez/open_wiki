# Jam.py (web framework)

## Metadata
- **Last Updated:** 2024-12-03 07:53:07 UTC
- **Original Article:** [Jam.py (web framework)](https://en.wikipedia.org/wiki/Jam.py_(web_framework))
- **Language:** en
- **Page ID:** 59662859

## Summary
Jam.py is free and open-source low-code/no-code "full stack" WSGI rapid application development framework for the JavaScript and Python programming language.
Jam.py is a  Single-page, event driven
 low-code development platform for database-driven business web applications, based on DRY principle, with emphasis on CRUD.
It is designed to automatically create JavaScript web forms from the underlying database tables, although a form can be created manually if required.
It offers a built-in web server, Application Builder and database access for third-party databases.

## Categories
This article belongs to the following categories:

- Category:2015 software
- Category:Articles with short description
- Category:CS1 errors: bare URL
- Category:CS1 errors: missing title
- Category:Free software programmed in Python
- Category:Low Code Application Platform
- Category:Official website different in Wikidata and Wikipedia
- Category:Python (programming language) web frameworks
- Category:Short description matches Wikidata

## Table of Contents

- Features
- Distinctive features
- PythonAnywhere
- Notes
- References
- See also
- External links

## Content

Jam.py is free and open-source low-code/no-code "full stack" WSGI rapid application development framework for the JavaScript and Python programming language.
Jam.py is a  Single-page, event driven
 low-code development platform for database-driven business web applications, based on DRY principle, with emphasis on CRUD.
It is designed to automatically create JavaScript web forms from the underlying database tables, although a form can be created manually if required.
It offers a built-in web server, Application Builder and database access for third-party databases.

Features
Single distribution which runs with both Python 2.6+ and 3.x
Can run as a standalone web development server or be used with any web server which supports WSGI
Built-in GUI builder called Application Builder
Support for JSON client data (for REST and JavaScript clients)
Support for popular databases Oracle Database, Microsoft SQL Server, PostgreSQL, SQLite, MySQL, Firebird (database server), SQLCipher
Extensible authentication mechanisms and role-based access control
Internationalization support
jQuery for Ajax and UI
Template language
Reports Templates based on LibreOffice
Files upload

Distinctive features
Built-in Application Builder
All development, maintenance and remote database administration can be performed via Builder interface. The most distinctive feature is the Client and Server Module. The Server Module enables the Python code for business logic, executed as a server-side session. The Client Module executes the JavaScript code within a browser. It is possible to exchange data between the two.
 
Application Builder is strongly influenced by Delphi visual designer.

Application Builder Client Module
The following JavaScript code shows a simple web page that displays "Hello World!" when visited: 

The above code resides in Task/Client Module(s) within the Application Builder. The task function can be accessed globally.

Application Builder Server Module
The Python libraries can be imported within the Task/Server Module(s):

The above code imports smtplib library, which might be used to send emails. The defined functions can be accessed globally.

Database migrations
Jam.py supports database migration and data import from one supported database to another.
The below code in the Task/Server Module will import data from SQLite to application database:

Limitations:

The SQLite database can not be imported into the application database which has foreign keys.

PythonAnywhere
PythonAnywhere Python 3.x deployment is supported

Notes
References
See also
Flask (web framework)
Pylons project
Web2py
Django (web framework)
Comparison of web frameworks
List of low-code development platforms

External links
Official website

## Archive Info
- **Archived on:** 2024-12-15 20:28:14 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2740 bytes
- **Word Count:** 384 words
