# Web2py

## Article Metadata

- **Last Updated:** 2024-12-14T20:00:32.270351+00:00
- **Original Article:** [Web2py](https://en.wikipedia.org/wiki/Web2py)
- **Language:** en
- **Page ID:** 18154641

## Summary

Web2py is an open-source web application framework written in the Python programming language. Web2py allows web developers to program dynamic web content using Python. Web2py is designed to help reduce tedious web development tasks, such as developing web forms from scratch, although a web developer may build a form from scratch if required.
Web2py was originally designed as a teaching tool with emphasis on ease of use and deployment. Therefore, it does not have any project-level configuration 

## Categories

- Category:All articles needing additional references
- Category:All articles with self-published sources
- Category:Articles needing additional references from November 2013
- Category:Articles with self-published sources from April 2024
- Category:Articles with short description
- Category:Free content management systems
- Category:Python (programming language) web frameworks
- Category:Short description matches Wikidata

## Table of Contents

- Overview
- Distinctive features
- Supported environments
- Database handling
- Licenses
- Awards
- Publications
- Background
- History and naming
- Applications built on Web2py
- Notes
- External links

## Content

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

## Related Articles

### Internal Links

- ["Hello, World!" program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)
- [.NET](https://en.wikipedia.org/wiki/.NET)
- [.NET Framework](https://en.wikipedia.org/wiki/.NET_Framework)
- [AIDA/Web](https://en.wikipedia.org/wiki/AIDA/Web)
- [API](https://en.wikipedia.org/wiki/API)
- [ASP.NET](https://en.wikipedia.org/wiki/ASP.NET)
- [ASP.NET AJAX](https://en.wikipedia.org/wiki/ASP.NET_AJAX)
- [ASP.NET Core](https://en.wikipedia.org/wiki/ASP.NET_Core)
- [ASP.NET Dynamic Data](https://en.wikipedia.org/wiki/ASP.NET_Dynamic_Data)
- [ASP.NET MVC](https://en.wikipedia.org/wiki/ASP.NET_MVC)
- [ASP.NET Razor](https://en.wikipedia.org/wiki/ASP.NET_Razor)
- [ASP.NET Web Forms](https://en.wikipedia.org/wiki/ASP.NET_Web_Forms)
- [Action Message Format](https://en.wikipedia.org/wiki/Action_Message_Format)
- [Adobe ColdFusion](https://en.wikipedia.org/wiki/Adobe_ColdFusion)
- [Adobe Flash](https://en.wikipedia.org/wiki/Adobe_Flash)
- [Apache Flex](https://en.wikipedia.org/wiki/Apache_Flex)
- [Ajax (programming)](https://en.wikipedia.org/wiki/Ajax_(programming))
- [Amazon Elastic Compute Cloud](https://en.wikipedia.org/wiki/Amazon_Elastic_Compute_Cloud)
- [AngularJS](https://en.wikipedia.org/wiki/AngularJS)
- [Angular (web framework)](https://en.wikipedia.org/wiki/Angular_(web_framework))
- [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server)
- [Apache Sling](https://en.wikipedia.org/wiki/Apache_Sling)
- [Apache Struts](https://en.wikipedia.org/wiki/Apache_Struts)
- [Apache Tapestry](https://en.wikipedia.org/wiki/Apache_Tapestry)
- [Apache Wicket](https://en.wikipedia.org/wiki/Apache_Wicket)
- [AppFuse](https://en.wikipedia.org/wiki/AppFuse)
- [Aptana](https://en.wikipedia.org/wiki/Aptana)
- [Architectural pattern](https://en.wikipedia.org/wiki/Architectural_pattern)
- [Atom (web standard)](https://en.wikipedia.org/wiki/Atom_(web_standard))
- [Atom (web standard)](https://en.wikipedia.org/wiki/Atom_(web_standard))
- [Authentication](https://en.wikipedia.org/wiki/Authentication)
- [Berkeley Software Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution)
- [Backbone.js](https://en.wikipedia.org/wiki/Backbone.js)
- [Base One Foundation Component Library](https://en.wikipedia.org/wiki/Base_One_Foundation_Component_Library)
- [Blazor](https://en.wikipedia.org/wiki/Blazor)
- [Blog](https://en.wikipedia.org/wiki/Blog)
- [Bytecode](https://en.wikipedia.org/wiki/Bytecode)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CL-HTTP](https://en.wikipedia.org/wiki/CL-HTTP)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Cache (computing)](https://en.wikipedia.org/wiki/Cache_(computing))
- [CakePHP](https://en.wikipedia.org/wiki/CakePHP)
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [Cheat sheet](https://en.wikipedia.org/wiki/Cheat_sheet)
- [Cherokee (web server)](https://en.wikipedia.org/wiki/Cherokee_(web_server))
- [CherryPy](https://en.wikipedia.org/wiki/CherryPy)
- [Chicago](https://en.wikipedia.org/wiki/Chicago)
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [CodeIgniter](https://en.wikipedia.org/wiki/CodeIgniter)
- [CodeMirror](https://en.wikipedia.org/wiki/CodeMirror)
- [ColdBox Platform](https://en.wikipedia.org/wiki/ColdBox_Platform)
- [Comma-separated values](https://en.wikipedia.org/wiki/Comma-separated_values)
- [Command-line interface](https://en.wikipedia.org/wiki/Command-line_interface)
- [Common Gateway Interface](https://en.wikipedia.org/wiki/Common_Gateway_Interface)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Communication](https://en.wikipedia.org/wiki/Communication)
- [Comparison of server-side web frameworks](https://en.wikipedia.org/wiki/Comparison_of_server-side_web_frameworks)
- [Component-based software engineering](https://en.wikipedia.org/wiki/Component-based_software_engineering)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Computing platform](https://en.wikipedia.org/wiki/Computing_platform)
- [Content management system](https://en.wikipedia.org/wiki/Content_management_system)
- [Convention over configuration](https://en.wikipedia.org/wiki/Convention_over_configuration)
- [Cookbook](https://en.wikipedia.org/wiki/Cookbook)
- [CppCMS](https://en.wikipedia.org/wiki/CppCMS)
- [Create, read, update and delete](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)
- [Cron](https://en.wikipedia.org/wiki/Cron)
- [Cron](https://en.wikipedia.org/wiki/Cron)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [CubicWeb](https://en.wikipedia.org/wiki/CubicWeb)
- [Dancer (software)](https://en.wikipedia.org/wiki/Dancer_(software))
- [Data access layer](https://en.wikipedia.org/wiki/Data_access_layer)
- [Data mapping](https://en.wikipedia.org/wiki/Data_mapping)
- [Data migration](https://en.wikipedia.org/wiki/Data_migration)
- [Database abstraction layer](https://en.wikipedia.org/wiki/Database_abstraction_layer)
- [Database transaction](https://en.wikipedia.org/wiki/Database_transaction)
- [DePaul University](https://en.wikipedia.org/wiki/DePaul_University)
- [Debugging](https://en.wikipedia.org/wiki/Debugging)
- [Distributed transaction](https://en.wikipedia.org/wiki/Distributed_transaction)
- [Django (web framework)](https://en.wikipedia.org/wiki/Django_(web_framework))
- [Document Object Model](https://en.wikipedia.org/wiki/Document_Object_Model)
- [Dojo Toolkit](https://en.wikipedia.org/wiki/Dojo_Toolkit)
- [DNN (software)](https://en.wikipedia.org/wiki/DNN_(software))
- [Drogon (software)](https://en.wikipedia.org/wiki/Drogon_(software))
- [Drupal](https://en.wikipedia.org/wiki/Drupal)
- [Dynamic web page](https://en.wikipedia.org/wiki/Dynamic_web_page)
- [EZ Publish](https://en.wikipedia.org/wiki/EZ_Publish)
- [Eclipse (software)](https://en.wikipedia.org/wiki/Eclipse_(software))
- [Eclipse (software)](https://en.wikipedia.org/wiki/Eclipse_(software))
- [Elixir (programming language)](https://en.wikipedia.org/wiki/Elixir_(programming_language))
- [Emacs](https://en.wikipedia.org/wiki/Emacs)
- [Ember.js](https://en.wikipedia.org/wiki/Ember.js)
- [Eric](https://en.wikipedia.org/wiki/Eric)
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Express.js](https://en.wikipedia.org/wiki/Express.js)
- [Ext JS](https://en.wikipedia.org/wiki/Ext_JS)
- [FAQ](https://en.wikipedia.org/wiki/FAQ)
- [FastAPI](https://en.wikipedia.org/wiki/FastAPI)
- [FastCGI](https://en.wikipedia.org/wiki/FastCGI)
- [Fastify](https://en.wikipedia.org/wiki/Fastify)
- [Fat-Free Framework](https://en.wikipedia.org/wiki/Fat-Free_Framework)
- [Firebird (database server)](https://en.wikipedia.org/wiki/Firebird_(database_server))
- [Flask (web framework)](https://en.wikipedia.org/wiki/Flask_(web_framework))
- [HTML form](https://en.wikipedia.org/wiki/HTML_form)
- [FuelPHP](https://en.wikipedia.org/wiki/FuelPHP)
- [GNU General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Git](https://en.wikipedia.org/wiki/Git)
- [Google App Engine](https://en.wikipedia.org/wiki/Google_App_Engine)
- [Google Closure Tools](https://en.wikipedia.org/wiki/Google_Closure_Tools)
- [Google Web Toolkit](https://en.wikipedia.org/wiki/Google_Web_Toolkit)
- [Grails (framework)](https://en.wikipedia.org/wiki/Grails_(framework))
- [Grav (CMS)](https://en.wikipedia.org/wiki/Grav_(CMS))
- [Grok (web framework)](https://en.wikipedia.org/wiki/Grok_(web_framework))
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Gyroscope (software)](https://en.wikipedia.org/wiki/Gyroscope_(software))
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [HTTPS](https://en.wikipedia.org/wiki/HTTPS)
- [Hard disk drive](https://en.wikipedia.org/wiki/Hard_disk_drive)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Hiawatha (web server)](https://en.wikipedia.org/wiki/Hiawatha_(web_server))
- [Horde (software)](https://en.wikipedia.org/wiki/Horde_(software))
- [Htmx](https://en.wikipedia.org/wiki/Htmx)
- [Internationalization and localization](https://en.wikipedia.org/wiki/Internationalization_and_localization)
- [IBM Db2](https://en.wikipedia.org/wiki/IBM_Db2)
- [ICEfaces](https://en.wikipedia.org/wiki/ICEfaces)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Indentation style](https://en.wikipedia.org/wiki/Indentation_style)
- [InfoWorld](https://en.wikipedia.org/wiki/InfoWorld)
- [Informix](https://en.wikipedia.org/wiki/Informix)
- [Ingres (database)](https://en.wikipedia.org/wiki/Ingres_(database))
- [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment)
- [Internationalization and localization](https://en.wikipedia.org/wiki/Internationalization_and_localization)
- [IronPython](https://en.wikipedia.org/wiki/IronPython)
- [Issue tracking system](https://en.wikipedia.org/wiki/Issue_tracking_system)
- [JBoss Seam](https://en.wikipedia.org/wiki/JBoss_Seam)
- [JHipster](https://en.wikipedia.org/wiki/JHipster)
- [JQuery](https://en.wikipedia.org/wiki/JQuery)
- [JSON](https://en.wikipedia.org/wiki/JSON)
- [JSON-RPC](https://en.wikipedia.org/wiki/JSON-RPC)
- [JWt (Java web toolkit)](https://en.wikipedia.org/wiki/JWt_(Java_web_toolkit))
- [Jakarta Faces](https://en.wikipedia.org/wiki/Jakarta_Faces)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [JavaScript library](https://en.wikipedia.org/wiki/JavaScript_library)
- [Java (software platform)](https://en.wikipedia.org/wiki/Java_(software_platform))
- [Wiley (publisher)](https://en.wikipedia.org/wiki/Wiley_(publisher))
- [Joomla](https://en.wikipedia.org/wiki/Joomla)
- [Jython](https://en.wikipedia.org/wiki/Jython)
- [Knockout (web framework)](https://en.wikipedia.org/wiki/Knockout_(web_framework))
- [GNU Lesser General Public License](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)
- [Laminas](https://en.wikipedia.org/wiki/Laminas)
- [Laravel](https://en.wikipedia.org/wiki/Laravel)
- [Li3 (software)](https://en.wikipedia.org/wiki/Li3_(software))
- [Lift (web framework)](https://en.wikipedia.org/wiki/Lift_(web_framework))
- [Lighttpd](https://en.wikipedia.org/wiki/Lighttpd)
- [Linux](https://en.wikipedia.org/wiki/Linux)
- [Massachusetts Institute of Technology](https://en.wikipedia.org/wiki/Massachusetts_Institute_of_Technology)
- [MODX](https://en.wikipedia.org/wiki/MODX)
- [Mac (computer)](https://en.wikipedia.org/wiki/Mac_(computer))
- [Markdown](https://en.wikipedia.org/wiki/Markdown)
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [Memcached](https://en.wikipedia.org/wiki/Memcached)
- [Merb](https://en.wikipedia.org/wiki/Merb)
- [Meteor (web framework)](https://en.wikipedia.org/wiki/Meteor_(web_framework))
- [Microsoft SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server)
- [Visual Studio](https://en.wikipedia.org/wiki/Visual_Studio)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Midgard (software)](https://en.wikipedia.org/wiki/Midgard_(software))
- [Mod proxy](https://en.wikipedia.org/wiki/Mod_proxy)
- [Mod python](https://en.wikipedia.org/wiki/Mod_python)
- [Model–view–controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
- [Mojolicious](https://en.wikipedia.org/wiki/Mojolicious)
- [MonoRail (software)](https://en.wikipedia.org/wiki/MonoRail_(software))
- [MooTools](https://en.wikipedia.org/wiki/MooTools)
- [MySQL](https://en.wikipedia.org/wiki/MySQL)
- [Neos Flow](https://en.wikipedia.org/wiki/Neos_Flow)
- [NestJS](https://en.wikipedia.org/wiki/NestJS)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Next.js](https://en.wikipedia.org/wiki/Next.js)
- [Nginx](https://en.wikipedia.org/wiki/Nginx)
- [Node.js](https://en.wikipedia.org/wiki/Node.js)
- [Nuxt.js](https://en.wikipedia.org/wiki/Nuxt.js)
- [Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [On the fly](https://en.wikipedia.org/wiki/On_the_fly)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [ArsDigita Community System](https://en.wikipedia.org/wiki/ArsDigita_Community_System)
- [OpenUI5](https://en.wikipedia.org/wiki/OpenUI5)
- [Oracle Application Express](https://en.wikipedia.org/wiki/Oracle_Application_Express)
- [Oracle Database](https://en.wikipedia.org/wiki/Oracle_Database)
- [Out of print](https://en.wikipedia.org/wiki/Out_of_print)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PHP-Fusion](https://en.wikipedia.org/wiki/PHP-Fusion)
- [PHP-Nuke](https://en.wikipedia.org/wiki/PHP-Nuke)
- [PL/SQL](https://en.wikipedia.org/wiki/PL/SQL)
- [PRADO (framework)](https://en.wikipedia.org/wiki/PRADO_(framework))
- [Padrino (web framework)](https://en.wikipedia.org/wiki/Padrino_(web_framework))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Phalcon (framework)](https://en.wikipedia.org/wiki/Phalcon_(framework))
- [Phoenix (web framework)](https://en.wikipedia.org/wiki/Phoenix_(web_framework))
- [Play Framework](https://en.wikipedia.org/wiki/Play_Framework)
- [Pop PHP Framework](https://en.wikipedia.org/wiki/Pop_PHP_Framework)
- [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)
- [ProcessWire](https://en.wikipedia.org/wiki/ProcessWire)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Prototype JavaScript Framework](https://en.wikipedia.org/wiki/Prototype_JavaScript_Framework)
- [Public domain](https://en.wikipedia.org/wiki/Public_domain)
- [PyCharm](https://en.wikipedia.org/wiki/PyCharm)
- [PyDev](https://en.wikipedia.org/wiki/PyDev)
- [Pyjs](https://en.wikipedia.org/wiki/Pyjs)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Tools for Visual Studio](https://en.wikipedia.org/wiki/Python_Tools_for_Visual_Studio)
- [Qcodo](https://en.wikipedia.org/wiki/Qcodo)
- [Quixote (web framework)](https://en.wikipedia.org/wiki/Quixote_(web_framework))
- [RSS](https://en.wikipedia.org/wiki/RSS)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Random-access memory](https://en.wikipedia.org/wiki/Random-access_memory)
- [Rapid application development](https://en.wikipedia.org/wiki/Rapid_application_development)
- [React (software)](https://en.wikipedia.org/wiki/React_(software))
- [Relational database](https://en.wikipedia.org/wiki/Relational_database)
- [Remix (web framework)](https://en.wikipedia.org/wiki/Remix_(web_framework))
- [Remote Application Platform](https://en.wikipedia.org/wiki/Remote_Application_Platform)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [REST](https://en.wikipedia.org/wiki/REST)
- [Rich Text Format](https://en.wikipedia.org/wiki/Rich_Text_Format)
- [Rocket (web framework)](https://en.wikipedia.org/wiki/Rocket_(web_framework))
- [Role-based access control](https://en.wikipedia.org/wiki/Role-based_access_control)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Ruby on Rails](https://en.wikipedia.org/wiki/Ruby_on_Rails)
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [SOAP](https://en.wikipedia.org/wiki/SOAP)
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [SQLAlchemy](https://en.wikipedia.org/wiki/SQLAlchemy)
- [SQLite](https://en.wikipedia.org/wiki/SQLite)
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scalability](https://en.wikipedia.org/wiki/Scalability)
- [Scalatra](https://en.wikipedia.org/wiki/Scalatra)
- [Seaside (software)](https://en.wikipedia.org/wiki/Seaside_(software))
- [Sencha Touch](https://en.wikipedia.org/wiki/Sencha_Touch)
- [Servant (web framework)](https://en.wikipedia.org/wiki/Servant_(web_framework))
- [Client–server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
- [Session (computer science)](https://en.wikipedia.org/wiki/Session_(computer_science))
- [Shiny (web framework)](https://en.wikipedia.org/wiki/Shiny_(web_framework))
- [Silverstripe CMS](https://en.wikipedia.org/wiki/Silverstripe_CMS)
- [Sinatra (software)](https://en.wikipedia.org/wiki/Sinatra_(software))
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Snap (web framework)](https://en.wikipedia.org/wiki/Snap_(web_framework))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software deployment](https://en.wikipedia.org/wiki/Software_deployment)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software engineering](https://en.wikipedia.org/wiki/Software_engineering)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software maintenance](https://en.wikipedia.org/wiki/Software_maintenance)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Software testing](https://en.wikipedia.org/wiki/Software_testing)
- [Spring Framework](https://en.wikipedia.org/wiki/Spring_Framework)
- [SproutCore](https://en.wikipedia.org/wiki/SproutCore)
- [Storm (software)](https://en.wikipedia.org/wiki/Storm_(software))
- [Streaming media](https://en.wikipedia.org/wiki/Streaming_media)
- [Stripes (framework)](https://en.wikipedia.org/wiki/Stripes_(framework))
- [Svelte](https://en.wikipedia.org/wiki/Svelte)
- [Symfony](https://en.wikipedia.org/wiki/Symfony)
- [Syntax (programming languages)](https://en.wikipedia.org/wiki/Syntax_(programming_languages))
- [Syntax highlighting](https://en.wikipedia.org/wiki/Syntax_highlighting)
- [TACTIC (web framework)](https://en.wikipedia.org/wiki/TACTIC_(web_framework))
- [Internet protocol suite](https://en.wikipedia.org/wiki/Internet_protocol_suite)
- [TYPO3](https://en.wikipedia.org/wiki/TYPO3)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Web template system](https://en.wikipedia.org/wiki/Web_template_system)
- [TextMate](https://en.wikipedia.org/wiki/TextMate)
- [Text editor](https://en.wikipedia.org/wiki/Text_editor)
- [Thread (computing)](https://en.wikipedia.org/wiki/Thread_(computing))
- [Tornado (web server)](https://en.wikipedia.org/wiki/Tornado_(web_server))
- [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security)
- [TurboGears](https://en.wikipedia.org/wiki/TurboGears)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Two-phase commit protocol](https://en.wikipedia.org/wiki/Two-phase_commit_protocol)
- [USB flash drive](https://en.wikipedia.org/wiki/USB_flash_drive)
- [Umbraco](https://en.wikipedia.org/wiki/Umbraco)
- [Unix](https://en.wikipedia.org/wiki/Unix)
- [User interface](https://en.wikipedia.org/wiki/User_interface)
- [Vaadin](https://en.wikipedia.org/wiki/Vaadin)
- [Vert.x](https://en.wikipedia.org/wiki/Vert.x)
- [Vim (text editor)](https://en.wikipedia.org/wiki/Vim_(text_editor))
- [Vue.js](https://en.wikipedia.org/wiki/Vue.js)
- [WaveMaker](https://en.wikipedia.org/wiki/WaveMaker)
- [WebGUI](https://en.wikipedia.org/wiki/WebGUI)
- [WebSharper](https://en.wikipedia.org/wiki/WebSharper)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [HTTP cookie](https://en.wikipedia.org/wiki/HTTP_cookie)
- [Web developer](https://en.wikipedia.org/wiki/Web_developer)
- [HTML form](https://en.wikipedia.org/wiki/HTML_form)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [Web server](https://en.wikipedia.org/wiki/Web_server)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [Windows CE](https://en.wikipedia.org/wiki/Windows_CE)
- [Wing IDE](https://en.wikipedia.org/wiki/Wing_IDE)
- [WordPress](https://en.wikipedia.org/wiki/WordPress)
- [Wt (web toolkit)](https://en.wikipedia.org/wiki/Wt_(web_toolkit))
- [XML](https://en.wikipedia.org/wiki/XML)
- [XML-RPC](https://en.wikipedia.org/wiki/XML-RPC)
- [XOOPS](https://en.wikipedia.org/wiki/XOOPS)
- [Yaws (web server)](https://en.wikipedia.org/wiki/Yaws_(web_server))
- [Yesod (web framework)](https://en.wikipedia.org/wiki/Yesod_(web_framework))
- [Yii](https://en.wikipedia.org/wiki/Yii)
- [ZK (framework)](https://en.wikipedia.org/wiki/ZK_(framework))
- [Zope](https://en.wikipedia.org/wiki/Zope)
- [Wikipedia:Reliable sources](https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Python web frameworks](https://en.wikipedia.org/wiki/Template:Python_web_frameworks)
- [Template:Web frameworks](https://en.wikipedia.org/wiki/Template:Web_frameworks)
- [Template talk:Python web frameworks](https://en.wikipedia.org/wiki/Template_talk:Python_web_frameworks)
- [Template talk:Web frameworks](https://en.wikipedia.org/wiki/Template_talk:Web_frameworks)
- [Help:Authority control](https://en.wikipedia.org/wiki/Help:Authority_control)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from November 2013](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_November_2013)
- [Category:Articles with self-published sources from April 2024](https://en.wikipedia.org/wiki/Category:Articles_with_self-published_sources_from_April_2024)
- [Category:Python (programming language) web frameworks](https://en.wikipedia.org/wiki/Category:Python_(programming_language)_web_frameworks)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T20:00:32.270351+00:00_