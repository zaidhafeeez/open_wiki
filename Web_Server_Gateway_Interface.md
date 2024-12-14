# Web Server Gateway Interface

_Last updated: 2024-12-14T15:08:17.388201_

**Original Article:** [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)

**Summary:** The Web Server Gateway Interface (WSGI, pronounced whiskey or WIZ-ghee) is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language. The current version of WSGI, version 1.0.1, is specified in Python Enhancement Proposal (PEP) 3333.
WSGI was originally specified as PEP-333 in 2003. PEP-3333, published in 2010, updates the specification for Python 3.

## Categories
- Category:All articles with too many examples
- Category:Articles with short description
- Category:Articles with too many examples from September 2018
- Category:Python (programming language)
- Category:Short description matches Wikidata
- Category:Wikipedia articles with style issues from September 2018

## Content

The Web Server Gateway Interface (WSGI, pronounced whiskey or WIZ-ghee) is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language. The current version of WSGI, version 1.0.1, is specified in Python Enhancement Proposal (PEP) 3333.
WSGI was originally specified as PEP-333 in 2003. PEP-3333, published in 2010, updates the specification for Python 3.

Background
In 2003, Python web frameworks were typically written against only CGI, FastCGI, mod_python, or some other custom API of a specific web server. To quote PEP 333:

Python currently boasts a wide variety of web application frameworks, such as Zope, Quixote, Webware, SkunkWeb, PSO, and Twisted Web -- to name just a few. This wide variety of choices can be a problem for new Python users, because generally speaking, their choice of web framework will limit their choice of usable web servers, and vice versa... By contrast, although Java has just as many web application frameworks available, Java's "servlet" API makes it possible for applications written with any Java web application framework to run in any web server that supports the servlet API.
WSGI was thus created as an implementation-neutral interface between web servers and web applications or frameworks to promote common ground for portable web application development.

Specification overview
The WSGI has two sides:

the server/gateway side. This is often running full web server software such as Apache or Nginx, or is a lightweight application server that can communicate with a webserver, such as flup.
the application/framework side. This is a Python callable, supplied by the Python program or framework.
Between the server and the application, there may be one or more WSGI middleware components, which implement both sides of the API, typically in Python code.
WSGI does not specify how the Python interpreter should be started, nor how the application object should be loaded or configured, and different frameworks and webservers achieve this in different ways.

WSGI middleware
A WSGI middleware component is a Python callable that is itself a WSGI application, but may handle requests by delegating to other WSGI applications. These applications can themselves be WSGI middleware components.
A middleware component can perform such functions as:

Routing a request to different application objects based on the target URL, after changing the environment variables accordingly.
Allowing multiple applications or frameworks to run side-by-side in the same process
Load balancing and remote processing, by forwarding requests and responses over a network
Performing content post-processing, such as applying XSLT stylesheets

Examples
Example application
A WSGI-compatible "Hello, World!" application written in Python:

Where:

Line 1 defines a function named application, which takes two parameters, environ and start_response. environ is a dictionary containing CGI environment variables as well as other request parameters and metadata under well-defined keys.  start_response is a callable itself, taking two positional parameters, status and response_headers.
Line 2 calls start_response, specifying "200 OK" as the HTTP status and a "Content-Type" response header.
Line 3 makes the function into a generator. The body of the response is returned as an iterable of byte strings.

Example of calling an application
A full example of a WSGI network server is outside the scope of this article. Below is a sketch of how one would call a WSGI application and retrieve its HTTP status line, response headers, and response body, as Python objects. Details of how to construct the environ dict have been omitted.

WSGI-compatible applications and frameworks
Numerous web frameworks support WSGI:

Currently wrappers are available for FastCGI, CGI, SCGI, AJP (using flup), twisted.web, Apache (using mod_wsgi or mod_python), Nginx (using ngx_http_uwsgi_module), Nginx Unit (using the Python language module), and Microsoft IIS (using WFastCGI, isapi-wsgi, PyISAPIe, or an ASP gateway).

See also
Asynchronous Server Gateway Interface (ASGI) – The spiritual successor to WSGI, adding support for asynchronous applications
Rack – Ruby web server interface
PSGI – Perl Web Server Gateway Interface
SCGI – Simple Common Gateway Interface
JSGI – JavaScript web server gateway interface

References
External links
PEP 333 – Python Web Server Gateway Interface
PEP 3333 – Python Web Server Gateway Interface v1.0.1
WSGI metaframework
Comprehensive wiki about everything WSGI
WSGI Tutorial
Python standard library module wsgiref
Getting Started with WSGI
NWSGI – .NET implementation of the Python WSGI specification for IronPython and IIS
Gevent-FastCGI server implemented using gevent coroutine-based networking library