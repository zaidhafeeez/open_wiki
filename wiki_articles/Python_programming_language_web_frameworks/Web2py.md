---
title: Web2py
url: https://en.wikipedia.org/wiki/Web2py
language: en
categories: ["Category:All articles needing additional references", "Category:All articles with self-published sources", "Category:Articles needing additional references from November 2013", "Category:Articles with self-published sources from April 2024", "Category:Articles with short description", "Category:Free content management systems", "Category:Python (programming language) web frameworks", "Category:Short description matches Wikidata"]
references: 0
last_modified: 2024-12-19T14:11:43Z
---

# Web2py

## Summary

Web2py is an open-source web application framework written in the Python programming language. Web2py allows web developers to program dynamic web content using Python. Web2py is designed to help reduce tedious web development tasks, such as developing web forms from scratch, although a web developer may build a form from scratch if required.
Web2py was originally designed as a teaching tool with emphasis on ease of use and deployment. Therefore, it does not have any project-level configuration 

## Full Content

Web2py is an open-source web application framework written in the Python programming language. Web2py allows web developers to program dynamic web content using Python. Web2py is designed to help reduce tedious web development tasks, such as developing web forms from scratch, although a web developer may build a form from scratch if required.
Web2py was originally designed as a teaching tool with emphasis on ease of use and deployment. Therefore, it does not have any project-level configuration files. The design of web2py was inspired by the Ruby on Rails and Django frameworks. Like these frameworks, web2py focuses on rapid development, favors convention over configuration approach and follows a model–view–controller (MVC) architectural pattern.

Overview
Web2py is a full-stack framework in that it has built-in components for all major functions, including:

HTTP requests, HTTP responses, cookies, sessions;
multiple protocols HTML/XML, REST, ATOM and RSS, RTF and CSV, JSON, JSON-RPC and XML-RPC, AMF-RPC (Flash/Flex), and SOAP;
CRUD API;
multiple authentication mechanisms and role-based access control;
database abstraction layer (DAL) that dynamically generates SQL and runs on multiple compatible database backends;
RAM, disk, and memcached-based caching for scalability;
internationalization support;
jQuery for Ajax and UI effects;
automatic logging of errors with context.
Web2py encourages sound software engineering practices such as

the model–view–controller (MVC) pattern;
self-submission of web forms;
server-side sessions;
safe handling of uploaded files.
Web2py uses the WSGI protocol, the Python-oriented protocol for communication between web server and web applications. It also provides handlers for CGI and the FastCGI protocols, and it includes the multi-threaded, SSL-enabled Rocket wsgiserver.

Distinctive features
Web-based integrated development environment (IDE)
All development, debugging, testing, maintenance and remote database administration can (optionally) be performed without third-party tools, via a web interface, itself a web2py application. Internationalization (adding languages and writing translations) can also be performed from this IDE. Each application has an automatically generated database administrative interface, similar to Django. The web IDE also includes web-based testing.
Applications can also be created from the command line or developed with other IDEs. Further debugging options:

Wing IDE allows graphical debugging of web2py applications as you interact with it from your web browser, you can inspect and modify variables, make function calls etc.
Eclipse/PyDev — Eclipse with the Aptana PyDev plugin — supports web2py as well.
The extensible pdb debugger is a module of Python's standard library.
With the platform-independent open-source Winpdb debugger, one can perform remote debugging over TCP/IP, through encrypted connection.
The Hello World program with web2py in its simplest form (simple web page with no template) looks like:

Web2py includes pure Python-based template language, with no indentation requirements and a server-side Document Object Model (DOM).
The template system works without web2py. Joomla 1.x templates can be converted to web2py layouts.
Web2py also includes two markup libraries: the markdown2 text-to-HTML filter, which converts Markdown markup to HTML on the fly; and markmin which is inspired by markdown but supports tables, html5 video/audio and oembed protocol.
A controller without a view automatically uses a generic view that render the variables returned by the controller, enabling the development of an application's business logic before writing HTML. The "Hello World" example using a default template:

The dict() output of an action is automatically rendered in HTML if the page is request with a .html extension, in JSON if the page is requested with a .json extension, in XML if requested with .xml. It supports other protocols including jsonp, rss, ics, google maps, etc. and is extensible.
Here is a more complex code example which defines a table, and exposes a grid to logged in users:

Ticketing system
Each web2py application comes with a ticketing system:

If an error occurs, it is logged and a ticket is issued to the user. That allows error tracking.
Errors and source code are accessible only to the administrator, who can search and retrieve errors by date or client-IP. No error can result in code being exposed to the users.

Portable cron
Cron is a mechanism for creating and running recurrent tasks in background. It looks for an application-specific crontab file which is in standard crontab format. Three modes of operation are available:

Soft cron: cron routines are checked after web page content has been served, does not guarantee execution precision. For unprivileged Apache CGI/WSGI installs.
Hard cron: a cron thread gets started on web2py startup. For Windows and Rocket/standalone web2py installs.
System cron: cron functions get force-called from the command line, usually from the system crontab. For Unix/Linux systems and places where the cron triggers need to be executed even if web2py is not running at the moment; also good for CGI/WSGI installs if you have access to the system crontab.

Scheduler
Since version 2.3 the use of cron is discouraged since web2py comes with a master/worker scheduler. Jobs can be defined in models and are scheduled by creating an entry in the database. Users can start work processes who pickup and execute tasks in background. The schedule is better than cron because it allows to specify more parameters (start time, stop time, number of repetitions, number of trials in case of error) and do a better job at running within constant resource utilization.

Bytecode distribution
Web2py can compile web applications for distribution in bytecode compiled form, without source code. Unlike frameworks that use specialized template languages for their views, Web2py can also compile the view code into bytecode, since it is pure Python code.

Global Environment
Web2py is unique in the world of Python web frameworks because models and controllers are executed, not imported. They are not modules. They are executed in a single global environment which is initialized at each HTTP request. This design decision has pros and cons.
The major pro is the ease of development, specifically for rapid prototyping. Another pro is that all the objects defined within this environment are cleanly reset at each HTTP request and never shared across requests. This means the developer does not need to worry about changing the state of an object (for example the readable attribute of a database field) or worry about a change leaking to other concurrent requests or other applications. A third advantage is that web2py allows the coexistence of multiple applications under the same instance without conflicts even if they use different versions of the same modules or different modules with the same name.
The main disadvantage of the global environment is that model files and controller files are not modules and the order of execution matters (although it can be specified using conditional models). Naming conflict is more likely to occur than in normal Python modules. Some standard Python development tools may not understand objects defined in models and controllers. Moreover, developers must be aware that code in models is executed at every request and this may cause a performance penalty. Nothing in web2py prevents developers from using and importing normal Python modules (model-less approach) and for this purpose web2py provides a thread local object (current) to facilitate access to objects associated to the current request. Yet, in this case, the developer has to be aware of the same pitfalls that other frameworks incur: changing the state of an object defined in a module may affect other concurrent requests.
Another con is that, because models and controllers are not class-based, efficient code reuse becomes more difficult, particularly as the inability to inherit from a parent controller (e.g. the ApplicationController in Ruby on Rails) means that common controller functionality must be referenced repeatedly across all controller files.

Supported environments
Operating systems, Python versions & implementations, virtual machines, hardware
web2py runs on Windows, Windows CE phones, Mac, Unix/Linux, Google App Engine, Amazon EC2, and almost any web hosting via Python 2.7/3.5/3.6/pypy.
The current binary version of web2py (for Windows or Mac) includes Python 2.7, but the source version can be run on 2.7 and 3.5+. Support for Python 2.6 has been dropped on 2017.
web2py since v1.64.0 runs unmodified on Java with Jython 2.5, without any known limitation.
web2py code can run with IronPython on .NET. Limitations:

no csv module (so no database I/O);
no third party database drivers (not even SQLite, so no databases at all);
no built-in web server (unless you cripple it by removing signals and logging).
The web2py binary will run from a USB drive or a portable hard drive without dependencies, like Portable Python.

Web servers
Web2py can service requests via HTTP and HTTPS with its built-in Rocket server, with Apache, Lighttpd, Cherokee, Hiawatha, Nginx and almost any other web server through CGI, FastCGI, WSGI, mod_proxy, and/or mod_python.

IDEs and debuggers
While a number of web2py developers use text editors such as Vim, Emacs or TextMate Web2py also has a built-in web-based IDE. Others prefer more specialized tools providing debugging, refactoring, etc.

Aptana Studio with integrated PyDev
Eclipse with PyDev
Eric with built-in debugger.
Wing IDE
Microsoft Visual Studio with Python Tools for Visual Studio
Pycharm3 has Web2py framework support

Database handling
The database abstraction layer (DAL) of web2py dynamically and transparently generates SQL queries and runs on multiple compatible database backend without the need for database-specific SQL commands (though SQL commands can be issued explicitly).
SQLite is included in Python and is the default web2py database. A connection string change allows connection to Firebird, IBM Db2, Informix, Ingres, Microsoft SQL Server, MySQL, Oracle, PostgreSQL, and Google App Engine (GAE) with some caveats. Specialities:

Multiple database connections.
Automatic table creates and alters.
Automatic transactions.
Distributed transactions:
Since web2py v1.17 with PostgreSQL v8.2 and later, because it provides API for two-phase commits.
Since web2py v1.70.1 with Firebird and MySQL (experimental).
GAE is not a relational store, but web2py emulates certain operations.
The DAL is fast, at least comparable with SQLAlchemy and Storm.
Web2py implements a DAL, not an ORM. An ORM maps database tables into classes representing logical abstractions from the database layer (e.g., a User class or a PurchaseOrder class), and maps records into instances of those classes. The DAL instead maps database tables and records into instances of classes representing sets and records instead of higher-level abstractions. It has very similar syntax to an ORM but it is faster, and can map almost any SQL expressions into DAL expressions. The DAL can be used independently of the rest of web2py.
Here are some examples of DAL syntax:

The latest version of the DAL has support for 2D GIS functions with Spatialite and PostGIS. The current API are experimental because of a possible move to 3D APIs.

Automatic database migrations
web2py supports database migrations—change the definition of a table and web2py ALTERs the table accordingly. Migrations are automatic, but can be disabled for any table, and migration is typically disabled when an application is ready for live distribution. Migrations and migration attempts are logged, documenting the changes.
Limitations:

SQLite cannot alter table and change a column type, but rather simply stores new values according to the new type.
GAE has no concept of alter-table, so migrations are limited.

Licenses
Web2py code is released under GNU Lesser General Public License (LGPL) version 3 as of web2py version 1.91.1.
Web2py code before version 1.91.1 was released under GNU GPL v2.0 with commercial exception.
Various third-party packages distributed with web2py have their own licenses, generally public domain, MIT or BSD-type licenses. Applications built with web2py are not covered by the LGPL license.
Web2py is copyrighted by Massimo DiPierro. The web2py trademark is owned by Massimo DiPierro.

Awards
In 2011 InfoWorld ranked web2py highest among the top six Python web frameworks, awarded web2py the Bossie award 2011 for best open source application development software. In 2012 web2py won the InfoWorld Technology of the Year award.

Publications
web2py Book
The base web2py documentation is The Official web2py Book, by  Massimo DiPierro. The manual is a full web2py application and it's freely available online, in PDF format or printed form.

1st Edition: out of print. Wiley; September 16, 2008; 256 pages; ISBN 978-0-470-43232-7.
2nd Edition: web2py Manual. Wiley; August 26, 2009; 341 pages; ISBN 978-0-470-59235-9.
3rd Edition: Lulu; September 25, 2010 357 pages.
4th Edition: Lulu; December 9, 2011 583 pages.
5th Edition: PDF Copy; March 3, 2013 614 pages; ISBN 978-0-578-12021-8.
latest online sources: on GitHub

Online documentation
Online documentation is linked from the web2py home page, with cookbook, videos, interactive examples, interactive API reference, epydoc s (complete library reference), FAQ, cheat sheet, online tools etc.

Cheat sheet for web2py.
web2pyslices, recipes posted using the movuca social network in web2py.
Crash Course in Web2py (5-part series).
Web2py slides (old).

Videos
web2py Enterprise Web Framework Tutorial.
web2py "Shootout" video tutorial.
web2py on the Google appengine.
web2py: Create, edit, and deploy a basic web app.

Printed
"web2py application development cookbook", Packt, 2012
Web programming with web2py; Python Magazine; Marco Tabini & Associates, Inc.; June 2008

Background
Developers
The lead developer of web2py is Massimo DiPierro, an associate professor of Computer Science at DePaul University in Chicago. As of 2011, the web2py homepage lists over 70 "main contributors".

Development source code
The web2py development source code is available from the main repository:

Git on GitHub: Web2Py

Third-party software included in web2py
Python-based components:
Rocket, a fast, HTTP/1.1-compliant, multi-threaded, SSL-enabled and streaming-capable WSGI server;
fcgi.py: a FastCGI/WSGI gateway;
Login API for Janrain, Dropbox, Google, LDAP, PAM, X509, CAS, OpenID, OAuth 1&2, Loginza
simplejson: a simple, fast, complete, correct and extensible JSON encoder and decoder;
markdown2: a Markdown processor;
fpdf a library for PDF generation;
PyRTF: an RTF document generator;
a syntax highlighter;
pysimplesoap for SOAP services;
PyRSS2Gen: an RSS generator;
feedparser: to parse RSS and Atom feeds.
JavaScript-based components:
jQuery: a lightweight JavaScript library;
CodeMirror: a free editor for source code;
C-based components:
SQLite: a relational database;
memcached: a general-purpose distributed memory caching system.
Payment API for Authorize.Net, Google Wallet, Stripe.com

History and naming
The source code for the first public version of web2py was released under GNU GPL v2.0 on 2007-09-27 by Massimo DiPierro as the Enterprise Web Framework (EWF). The name was changed twice due to name conflicts: EWF v1.7 was followed by Gluon v1.0, and Gluon v1.15 was followed by web2py v1.16. The license was changed to LGPLv3 as of web2py version 1.91.1 on 2010-12-21.

Applications built on Web2py
Movuca CMS and Social Network Engine.
Instant Press Blog platform.
Ourway Social networking site.
NoobMusic A rock music website.
LinkFindr Network diagnostic tool.
StarMaker Develops karaoke-style social music apps.

Notes
External links

Official website
