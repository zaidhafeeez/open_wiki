# Web Server Gateway Interface

## Article Metadata

- **Last Updated:** 2024-12-15T03:24:56.543992+00:00
- **Original Article:** [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- **Language:** en
- **Page ID:** 1441500

## Summary

The Web Server Gateway Interface (WSGI, pronounced whiskey or WIZ-ghee) is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language. The current version of WSGI, version 1.0.1, is specified in Python Enhancement Proposal (PEP) 3333.
WSGI was originally specified as PEP-333 in 2003. PEP-3333, published in 2010, updates the specification for Python 3.

## Categories

- Category:All articles with too many examples
- Category:Articles with short description
- Category:Articles with too many examples from September 2018
- Category:Python (programming language)
- Category:Short description matches Wikidata
- Category:Wikipedia articles with style issues from September 2018

## Table of Contents

- Background
- Specification overview
- WSGI middleware
- Examples
- WSGI-compatible applications and frameworks
- See also
- References
- External links

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

## Related Articles

### Internal Links

- ["Hello, World!" program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)
- [ActiveX](https://en.wikipedia.org/wiki/ActiveX)
- [Active Server Pages](https://en.wikipedia.org/wiki/Active_Server_Pages)
- [Ajax (programming)](https://en.wikipedia.org/wiki/Ajax_(programming))
- [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server)
- [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server)
- [Apache JServ Protocol](https://en.wikipedia.org/wiki/Apache_JServ_Protocol)
- [API](https://en.wikipedia.org/wiki/API)
- [Application server](https://en.wikipedia.org/wiki/Application_server)
- [Asynchronous Server Gateway Interface](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface)
- [Zope](https://en.wikipedia.org/wiki/Zope)
- [Browser Helper Object](https://en.wikipedia.org/wiki/Browser_Helper_Object)
- [Browser extension](https://en.wikipedia.org/wiki/Browser_extension)
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [CLPython](https://en.wikipedia.org/wiki/CLPython)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [Calling convention](https://en.wikipedia.org/wiki/Calling_convention)
- [Canvas element](https://en.wikipedia.org/wiki/Canvas_element)
- [CherryPy](https://en.wikipedia.org/wiki/CherryPy)
- [CircuitPython](https://en.wikipedia.org/wiki/CircuitPython)
- [Client–server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
- [Client-side persistent data](https://en.wikipedia.org/wiki/Client-side_persistent_data)
- [Common Gateway Interface](https://en.wikipedia.org/wiki/Common_Gateway_Interface)
- [Communication protocol](https://en.wikipedia.org/wiki/Communication_protocol)
- [Computer network](https://en.wikipedia.org/wiki/Computer_network)
- [Cross-origin resource sharing](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
- [Cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting)
- [Cython](https://en.wikipedia.org/wiki/Cython)
- [DOM event](https://en.wikipedia.org/wiki/DOM_event)
- [Django (web framework)](https://en.wikipedia.org/wiki/Django_(web_framework))
- [Document Object Model](https://en.wikipedia.org/wiki/Document_Object_Model)
- [Dynamic HTML](https://en.wikipedia.org/wiki/Dynamic_HTML)
- [Dynamic web page](https://en.wikipedia.org/wiki/Dynamic_web_page)
- [Encrypted Media Extensions](https://en.wikipedia.org/wiki/Encrypted_Media_Extensions)
- [Environment variable](https://en.wikipedia.org/wiki/Environment_variable)
- [Eric (software)](https://en.wikipedia.org/wiki/Eric_(software))
- [FastCGI](https://en.wikipedia.org/wiki/FastCGI)
- [Flask (web framework)](https://en.wikipedia.org/wiki/Flask_(web_framework))
- [Frontend and backend](https://en.wikipedia.org/wiki/Frontend_and_backend)
- [Gears (software)](https://en.wikipedia.org/wiki/Gears_(software))
- [Generator (computer programming)](https://en.wikipedia.org/wiki/Generator_(computer_programming))
- [Google App Engine](https://en.wikipedia.org/wiki/Google_App_Engine)
- [Google Native Client](https://en.wikipedia.org/wiki/Google_Native_Client)
- [GraphQL](https://en.wikipedia.org/wiki/GraphQL)
- [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
- [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn)
- [HTML5 File API](https://en.wikipedia.org/wiki/HTML5_File_API)
- [HTML audio](https://en.wikipedia.org/wiki/HTML_audio)
- [HTML video](https://en.wikipedia.org/wiki/HTML_video)
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [HTTP/2](https://en.wikipedia.org/wiki/HTTP/2)
- [HTTP/3](https://en.wikipedia.org/wiki/HTTP/3)
- [HTTPS](https://en.wikipedia.org/wiki/HTTPS)
- [HTTP handler](https://en.wikipedia.org/wiki/HTTP_handler)
- [Hydration (web development)](https://en.wikipedia.org/wiki/Hydration_(web_development))
- [IDLE](https://en.wikipedia.org/wiki/IDLE)
- [Indexed Database API](https://en.wikipedia.org/wiki/Indexed_Database_API)
- [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment)
- [Interface (computing)](https://en.wikipedia.org/wiki/Interface_(computing))
- [Internet Information Services](https://en.wikipedia.org/wiki/Internet_Information_Services)
- [Internet Server Application Programming Interface](https://en.wikipedia.org/wiki/Internet_Server_Application_Programming_Interface)
- [IronPython](https://en.wikipedia.org/wiki/IronPython)
- [JSGI](https://en.wikipedia.org/wiki/JSGI)
- [Jakarta Servlet](https://en.wikipedia.org/wiki/Jakarta_Servlet)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java Portlet Specification](https://en.wikipedia.org/wiki/Java_Portlet_Specification)
- [Jython](https://en.wikipedia.org/wiki/Jython)
- [Khronos Group](https://en.wikipedia.org/wiki/Khronos_Group)
- [List of Apache modules](https://en.wikipedia.org/wiki/List_of_Apache_modules)
- [List of Python software](https://en.wikipedia.org/wiki/List_of_Python_software)
- [List of application servers](https://en.wikipedia.org/wiki/List_of_application_servers)
- [Comparison of integrated development environments](https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments)
- [Load balancing (computing)](https://en.wikipedia.org/wiki/Load_balancing_(computing))
- [Mashup (web application hybrid)](https://en.wikipedia.org/wiki/Mashup_(web_application_hybrid))
- [Media Source Extensions](https://en.wikipedia.org/wiki/Media_Source_Extensions)
- [MicroPython](https://en.wikipedia.org/wiki/MicroPython)
- [Microservices](https://en.wikipedia.org/wiki/Microservices)
- [Middleware](https://en.wikipedia.org/wiki/Middleware)
- [List of Apache modules](https://en.wikipedia.org/wiki/List_of_Apache_modules)
- [Mod lisp](https://en.wikipedia.org/wiki/Mod_lisp)
- [Mod mono](https://en.wikipedia.org/wiki/Mod_mono)
- [Parrot virtual machine](https://en.wikipedia.org/wiki/Parrot_virtual_machine)
- [Mod perl](https://en.wikipedia.org/wiki/Mod_perl)
- [Mod proxy](https://en.wikipedia.org/wiki/Mod_proxy)
- [Mod python](https://en.wikipedia.org/wiki/Mod_python)
- [Mod ruby](https://en.wikipedia.org/wiki/Mod_ruby)
- [Mod wsgi](https://en.wikipedia.org/wiki/Mod_wsgi)
- [NPAPI](https://en.wikipedia.org/wiki/NPAPI)
- [Netscape Server Application Programming Interface](https://en.wikipedia.org/wiki/Netscape_Server_Application_Programming_Interface)
- [Nginx](https://en.wikipedia.org/wiki/Nginx)
- [Ninja-IDE](https://en.wikipedia.org/wiki/Ninja-IDE)
- [Numba](https://en.wikipedia.org/wiki/Numba)
- [Open API](https://en.wikipedia.org/wiki/Open_API)
- [Open Web Interface for .NET](https://en.wikipedia.org/wiki/Open_Web_Interface_for_.NET)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Plack (software)](https://en.wikipedia.org/wiki/Plack_(software))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Phusion Passenger](https://en.wikipedia.org/wiki/Phusion_Passenger)
- [Plack (software)](https://en.wikipedia.org/wiki/Plack_(software))
- [Plug-in (computing)](https://en.wikipedia.org/wiki/Plug-in_(computing))
- [Process (computing)](https://en.wikipedia.org/wiki/Process_(computing))
- [Programming language implementation](https://en.wikipedia.org/wiki/Programming_language_implementation)
- [Progressive web app](https://en.wikipedia.org/wiki/Progressive_web_app)
- [Psyco](https://en.wikipedia.org/wiki/Psyco)
- [Push technology](https://en.wikipedia.org/wiki/Push_technology)
- [PyCharm](https://en.wikipedia.org/wiki/PyCharm)
- [PyDev](https://en.wikipedia.org/wiki/PyDev)
- [PyPy](https://en.wikipedia.org/wiki/PyPy)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [History of Python](https://en.wikipedia.org/wiki/History_of_Python)
- [Python Conference](https://en.wikipedia.org/wiki/Python_Conference)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Paste](https://en.wikipedia.org/wiki/Python_Paste)
- [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation)
- [Python for S60](https://en.wikipedia.org/wiki/Python_for_S60)
- [REST](https://en.wikipedia.org/wiki/REST)
- [Rack (web server interface)](https://en.wikipedia.org/wiki/Rack_(web_server_interface))
- [Remote scripting](https://en.wikipedia.org/wiki/Remote_scripting)
- [Resource-oriented architecture](https://en.wikipedia.org/wiki/Resource-oriented_architecture)
- [Rich Internet Application](https://en.wikipedia.org/wiki/Rich_Internet_Application)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Simple Common Gateway Interface](https://en.wikipedia.org/wiki/Simple_Common_Gateway_Interface)
- [SVG](https://en.wikipedia.org/wiki/SVG)
- [Server-sent events](https://en.wikipedia.org/wiki/Server-sent_events)
- [Client–server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
- [Server-side scripting](https://en.wikipedia.org/wiki/Server-side_scripting)
- [Server (computing)](https://en.wikipedia.org/wiki/Server_(computing))
- [Server Side Includes](https://en.wikipedia.org/wiki/Server_Side_Includes)
- [Server application programming interface](https://en.wikipedia.org/wiki/Server_application_programming_interface)
- [Shed Skin](https://en.wikipedia.org/wiki/Shed_Skin)
- [Simple Common Gateway Interface](https://en.wikipedia.org/wiki/Simple_Common_Gateway_Interface)
- [Single-page application](https://en.wikipedia.org/wiki/Single-page_application)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software portability](https://en.wikipedia.org/wiki/Software_portability)
- [Solution stack](https://en.wikipedia.org/wiki/Solution_stack)
- [Spyder (software)](https://en.wikipedia.org/wiki/Spyder_(software))
- [Stackless Python](https://en.wikipedia.org/wiki/Stackless_Python)
- [Static web page](https://en.wikipedia.org/wiki/Static_web_page)
- [Tornado (web server)](https://en.wikipedia.org/wiki/Tornado_(web_server))
- [Trac](https://en.wikipedia.org/wiki/Trac)
- [TurboGears](https://en.wikipedia.org/wiki/TurboGears)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [UWSGI](https://en.wikipedia.org/wiki/UWSGI)
- [URL](https://en.wikipedia.org/wiki/URL)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [W3C Geolocation API](https://en.wikipedia.org/wiki/W3C_Geolocation_API)
- [WHATWG](https://en.wikipedia.org/wiki/WHATWG)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [WSGI (AM)](https://en.wikipedia.org/wiki/WSGI_(AM))
- [Web-oriented architecture](https://en.wikipedia.org/wiki/Web-oriented_architecture)
- [Reddit](https://en.wikipedia.org/wiki/Reddit)
- [Web2py](https://en.wikipedia.org/wiki/Web2py)
- [WebAssembly](https://en.wikipedia.org/wiki/WebAssembly)
- [WebAuthn](https://en.wikipedia.org/wiki/WebAuthn)
- [WebCL](https://en.wikipedia.org/wiki/WebCL)
- [WebDAV](https://en.wikipedia.org/wiki/WebDAV)
- [WebGL](https://en.wikipedia.org/wiki/WebGL)
- [WebGPU](https://en.wikipedia.org/wiki/WebGPU)
- [WebRTC](https://en.wikipedia.org/wiki/WebRTC)
- [WebSocket](https://en.wikipedia.org/wiki/WebSocket)
- [WebUSB](https://en.wikipedia.org/wiki/WebUSB)
- [WebXR](https://en.wikipedia.org/wiki/WebXR)
- [Web API](https://en.wikipedia.org/wiki/Web_API)
- [Web API security](https://en.wikipedia.org/wiki/Web_API_security)
- [Web IDL](https://en.wikipedia.org/wiki/Web_IDL)
- [Web Messaging](https://en.wikipedia.org/wiki/Web_Messaging)
- [Web SQL Database](https://en.wikipedia.org/wiki/Web_SQL_Database)
- [Web Services for Remote Portlets](https://en.wikipedia.org/wiki/Web_Services_for_Remote_Portlets)
- [Web application](https://en.wikipedia.org/wiki/Web_application)
- [Web container](https://en.wikipedia.org/wiki/Web_container)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [Web page](https://en.wikipedia.org/wiki/Web_page)
- [Web resource](https://en.wikipedia.org/wiki/Web_resource)
- [Web server](https://en.wikipedia.org/wiki/Web_server)
- [Web service](https://en.wikipedia.org/wiki/Web_service)
- [Web standards](https://en.wikipedia.org/wiki/Web_standards)
- [Web storage](https://en.wikipedia.org/wiki/Web_storage)
- [Web worker](https://en.wikipedia.org/wiki/Web_worker)
- [Webhook](https://en.wikipedia.org/wiki/Webhook)
- [World Wide Web Consortium](https://en.wikipedia.org/wiki/World_Wide_Web_Consortium)
- [XAML Browser Applications](https://en.wikipedia.org/wiki/XAML_Browser_Applications)
- [XMLHttpRequest](https://en.wikipedia.org/wiki/XMLHttpRequest)
- [XSLT](https://en.wikipedia.org/wiki/XSLT)
- [YouTube](https://en.wikipedia.org/wiki/YouTube)
- [Wikipedia:Example cruft](https://en.wikipedia.org/wiki/Wikipedia:Example_cruft)
- [Wikipedia:Manual of Style/Lists](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lists)
- [Wikipedia:Neutral point of view](https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view)
- [Template:Python (programming language)](https://en.wikipedia.org/wiki/Template:Python_(programming_language))
- [Template:Web interfaces](https://en.wikipedia.org/wiki/Template:Web_interfaces)
- [Template talk:Python (programming language)](https://en.wikipedia.org/wiki/Template_talk:Python_(programming_language))
- [Template talk:Web interfaces](https://en.wikipedia.org/wiki/Template_talk:Web_interfaces)
- [Help:Pronunciation respelling key](https://en.wikipedia.org/wiki/Help:Pronunciation_respelling_key)
- [Category:Articles with too many examples from September 2018](https://en.wikipedia.org/wiki/Category:Articles_with_too_many_examples_from_September_2018)
- [Category:Wikipedia articles with style issues from September 2018](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_with_style_issues_from_September_2018)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:24:56.543992+00:00_