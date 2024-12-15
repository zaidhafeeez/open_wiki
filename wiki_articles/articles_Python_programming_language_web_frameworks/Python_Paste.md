# Python Paste

## Metadata
- **Last Updated:** 2024-12-03 07:09:08 UTC
- **Original Article:** [Python Paste](https://en.wikipedia.org/wiki/Python_Paste)
- **Language:** en
- **Page ID:** 10720945

## Summary
Python Paste, often simply called paste, is a set of utilities for web development in Python.  Paste has been described as "a framework for web frameworks".
The Python Paste package contains Python modules that help in implementing WSGI middleware.
The package includes a WSGI wrapper for CGI applications. It also includes a simple webserver that can produce WSGI requests.

## Categories
This article belongs to the following categories:

- Category:All articles needing additional references
- Category:All articles with topics of unclear notability
- Category:Articles needing additional references from December 2017
- Category:Articles with multiple maintenance issues
- Category:Articles with short description
- Category:Articles with topics of unclear notability from May 2021
- Category:Official website missing URL
- Category:Products articles with topics of unclear notability
- Category:Python (programming language) web frameworks
- Category:Short description is different from Wikidata

## Table of Contents

- WSGI middleware
- Subcomponents of Paste
- See also
- References

## Content

Python Paste, often simply called paste, is a set of utilities for web development in Python.  Paste has been described as "a framework for web frameworks".
The Python Paste package contains Python modules that help in implementing WSGI middleware.
The package includes a WSGI wrapper for CGI applications. It also includes a simple webserver that can produce WSGI requests.

WSGI middleware
The WSGI standard is an interface that allows applications to use Python code to handle HTTP requests. A WSGI application is passed a Python representation of an HTTP request by an application, and returns content which will normally eventually be rendered by a web browser. A common use for this is when a web server serves content created by Python code.
There are, however, other uses: WSGI middleware is Python code that receives a WSGI request and then performs logic based upon this request, before passing the request on to a WSGI application or more WSGI middleware. WSGI middleware appears to an application as a server, and to the server as an application. This is analogous to the function of pipes on Unix systems. Functionality provided by WSGI middleware may include authentication, logging, URL redirection, creation of sessions, and compression.
Paste helps in developing such WSGI middleware systems. For example, it is used in the Pylons web application framework.

Subcomponents of Paste
Paste has been a long-running open source project, dating from at least 2005. As it has grown, it has unbundled several other utilities from the Paste core. These utilities are part of the Paste project, but form their own packages and have their own version numbers. They include:

Paste Deploy is a system for finding and configuring WSGI applications and servers.
Paste Script, ScriptType, INITools, Tempita, WaitForIt, WPHP, WSGIFilter, and WSGIProxy are other notable bundles.
WebTest
WebOb is a wrapper around the WSGI environment.
WebTest and WebOb have migrated and are now part of the Pylons project.

See also
TurboGears
Pylons project
Smalltalk Seaside
Java servlet
Internet Server Application Programming Interface (ISAPI)
FastCGI
Apache Thrift (from Facebook and Evernote teams)
Server-side JavaScript
PHP
Web framework

References


== External links ==

## Archive Info
- **Archived on:** 2024-12-15 20:40:00 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2266 bytes
- **Word Count:** 353 words
