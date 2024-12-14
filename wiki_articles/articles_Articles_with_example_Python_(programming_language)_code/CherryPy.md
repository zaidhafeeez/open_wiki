# CherryPy

## Article Metadata

- **Last Updated:** 2024-12-14T19:34:25.888206+00:00
- **Original Article:** [CherryPy](https://en.wikipedia.org/wiki/CherryPy)
- **Language:** en
- **Page ID:** 2231952

## Summary

CherryPy is an object-oriented web application framework using the Python programming language. It is designed for rapid development of web applications by wrapping the HTTP protocol but stays at a low level and does not offer much more than what is defined in RFC 7231.
CherryPy can be a web server itself or one can launch it via any WSGI compatible environment. It does not deal with tasks such as templating for output rendering or backend access. The framework is extensible with filters, which 

## Categories

- Category:All articles with self-published sources
- Category:Articles with example Python (programming language) code
- Category:Articles with self-published sources from April 2024
- Category:Articles with short description
- Category:Free computer libraries
- Category:Free software programmed in Python
- Category:Python (programming language) web frameworks
- Category:Short description matches Wikidata
- Category:Software using the BSD license
- Category:Webarchive template wayback links

## Table of Contents

- Pythonic interface
- Features
- See also
- References
- External links

## Content

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

## Related Articles

### Internal Links

- ["Hello, World!" program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)
- [.NET](https://en.wikipedia.org/wiki/.NET)
- [AIDA/Web](https://en.wikipedia.org/wiki/AIDA/Web)
- [ASP.NET](https://en.wikipedia.org/wiki/ASP.NET)
- [ASP.NET AJAX](https://en.wikipedia.org/wiki/ASP.NET_AJAX)
- [ASP.NET Core](https://en.wikipedia.org/wiki/ASP.NET_Core)
- [ASP.NET Dynamic Data](https://en.wikipedia.org/wiki/ASP.NET_Dynamic_Data)
- [ASP.NET MVC](https://en.wikipedia.org/wiki/ASP.NET_MVC)
- [ASP.NET Razor](https://en.wikipedia.org/wiki/ASP.NET_Razor)
- [ASP.NET Web Forms](https://en.wikipedia.org/wiki/ASP.NET_Web_Forms)
- [Adobe ColdFusion](https://en.wikipedia.org/wiki/Adobe_ColdFusion)
- [AngularJS](https://en.wikipedia.org/wiki/AngularJS)
- [Angular (web framework)](https://en.wikipedia.org/wiki/Angular_(web_framework))
- [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server)
- [Apache Sling](https://en.wikipedia.org/wiki/Apache_Sling)
- [Apache Struts](https://en.wikipedia.org/wiki/Apache_Struts)
- [Apache Tapestry](https://en.wikipedia.org/wiki/Apache_Tapestry)
- [Apache Wicket](https://en.wikipedia.org/wiki/Apache_Wicket)
- [AppFuse](https://en.wikipedia.org/wiki/AppFuse)
- [Authorization](https://en.wikipedia.org/wiki/Authorization)
- [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses)
- [Backbone.js](https://en.wikipedia.org/wiki/Backbone.js)
- [Base One Foundation Component Library](https://en.wikipedia.org/wiki/Base_One_Foundation_Component_Library)
- [Blazor](https://en.wikipedia.org/wiki/Blazor)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CL-HTTP](https://en.wikipedia.org/wiki/CL-HTTP)
- [CakePHP](https://en.wikipedia.org/wiki/CakePHP)
- [Canonical (company)](https://en.wikipedia.org/wiki/Canonical_(company))
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [Character encoding](https://en.wikipedia.org/wiki/Character_encoding)
- [CheetahTemplate](https://en.wikipedia.org/wiki/CheetahTemplate)
- [CodeIgniter](https://en.wikipedia.org/wiki/CodeIgniter)
- [Code coverage](https://en.wikipedia.org/wiki/Code_coverage)
- [ColdBox Platform](https://en.wikipedia.org/wiki/ColdBox_Platform)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Comparison of server-side web frameworks](https://en.wikipedia.org/wiki/Comparison_of_server-side_web_frameworks)
- [CppCMS](https://en.wikipedia.org/wiki/CppCMS)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [CubicWeb](https://en.wikipedia.org/wiki/CubicWeb)
- [Dancer (software)](https://en.wikipedia.org/wiki/Dancer_(software))
- [Django (web framework)](https://en.wikipedia.org/wiki/Django_(web_framework))
- [Dojo Toolkit](https://en.wikipedia.org/wiki/Dojo_Toolkit)
- [DNN (software)](https://en.wikipedia.org/wiki/DNN_(software))
- [Drogon (software)](https://en.wikipedia.org/wiki/Drogon_(software))
- [Drupal](https://en.wikipedia.org/wiki/Drupal)
- [EZ Publish](https://en.wikipedia.org/wiki/EZ_Publish)
- [Elixir (programming language)](https://en.wikipedia.org/wiki/Elixir_(programming_language))
- [Ember.js](https://en.wikipedia.org/wiki/Ember.js)
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Express.js](https://en.wikipedia.org/wiki/Express.js)
- [Ext JS](https://en.wikipedia.org/wiki/Ext_JS)
- [FastAPI](https://en.wikipedia.org/wiki/FastAPI)
- [FastCGI](https://en.wikipedia.org/wiki/FastCGI)
- [Fastify](https://en.wikipedia.org/wiki/Fastify)
- [Fat-Free Framework](https://en.wikipedia.org/wiki/Fat-Free_Framework)
- [Firebird (database server)](https://en.wikipedia.org/wiki/Firebird_(database_server))
- [Flask (web framework)](https://en.wikipedia.org/wiki/Flask_(web_framework))
- [FuelPHP](https://en.wikipedia.org/wiki/FuelPHP)
- [Genshi (templating language)](https://en.wikipedia.org/wiki/Genshi_(templating_language))
- [Google Closure Tools](https://en.wikipedia.org/wiki/Google_Closure_Tools)
- [Google Web Toolkit](https://en.wikipedia.org/wiki/Google_Web_Toolkit)
- [Grails (framework)](https://en.wikipedia.org/wiki/Grails_(framework))
- [Grav (CMS)](https://en.wikipedia.org/wiki/Grav_(CMS))
- [Grok (web framework)](https://en.wikipedia.org/wiki/Grok_(web_framework))
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Gyroscope (software)](https://en.wikipedia.org/wiki/Gyroscope_(software))
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Horde (software)](https://en.wikipedia.org/wiki/Horde_(software))
- [Htmx](https://en.wikipedia.org/wiki/Htmx)
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [ICEfaces](https://en.wikipedia.org/wiki/ICEfaces)
- [Internet Information Services](https://en.wikipedia.org/wiki/Internet_Information_Services)
- [JBoss Seam](https://en.wikipedia.org/wiki/JBoss_Seam)
- [JHipster](https://en.wikipedia.org/wiki/JHipster)
- [JQuery](https://en.wikipedia.org/wiki/JQuery)
- [JWt (Java web toolkit)](https://en.wikipedia.org/wiki/JWt_(Java_web_toolkit))
- [Jakarta Faces](https://en.wikipedia.org/wiki/Jakarta_Faces)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [JavaScript library](https://en.wikipedia.org/wiki/JavaScript_library)
- [Java (software platform)](https://en.wikipedia.org/wiki/Java_(software_platform))
- [Jinja (template engine)](https://en.wikipedia.org/wiki/Jinja_(template_engine))
- [Joomla](https://en.wikipedia.org/wiki/Joomla)
- [Comparison of web template engines](https://en.wikipedia.org/wiki/Comparison_of_web_template_engines)
- [Knockout (web framework)](https://en.wikipedia.org/wiki/Knockout_(web_framework))
- [Laminas](https://en.wikipedia.org/wiki/Laminas)
- [Laravel](https://en.wikipedia.org/wiki/Laravel)
- [Li3 (software)](https://en.wikipedia.org/wiki/Li3_(software))
- [Lift (web framework)](https://en.wikipedia.org/wiki/Lift_(web_framework))
- [Lighttpd](https://en.wikipedia.org/wiki/Lighttpd)
- [MODX](https://en.wikipedia.org/wiki/MODX)
- [Mako (template engine)](https://en.wikipedia.org/wiki/Mako_(template_engine))
- [MaxDB](https://en.wikipedia.org/wiki/MaxDB)
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [Merb](https://en.wikipedia.org/wiki/Merb)
- [Meteor (web framework)](https://en.wikipedia.org/wiki/Meteor_(web_framework))
- [Microsoft SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server)
- [Midgard (software)](https://en.wikipedia.org/wiki/Midgard_(software))
- [Mod python](https://en.wikipedia.org/wiki/Mod_python)
- [Mod wsgi](https://en.wikipedia.org/wiki/Mod_wsgi)
- [Mojolicious](https://en.wikipedia.org/wiki/Mojolicious)
- [MongoDB](https://en.wikipedia.org/wiki/MongoDB)
- [MonoRail (software)](https://en.wikipedia.org/wiki/MonoRail_(software))
- [MooTools](https://en.wikipedia.org/wiki/MooTools)
- [MySQL](https://en.wikipedia.org/wiki/MySQL)
- [Neos Flow](https://en.wikipedia.org/wiki/Neos_Flow)
- [NestJS](https://en.wikipedia.org/wiki/NestJS)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Next.js](https://en.wikipedia.org/wiki/Next.js)
- [Node.js](https://en.wikipedia.org/wiki/Node.js)
- [Nuxt.js](https://en.wikipedia.org/wiki/Nuxt.js)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
- [Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
- [ArsDigita Community System](https://en.wikipedia.org/wiki/ArsDigita_Community_System)
- [OpenUI5](https://en.wikipedia.org/wiki/OpenUI5)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Oracle Application Express](https://en.wikipedia.org/wiki/Oracle_Application_Express)
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
- [Plug-in (computing)](https://en.wikipedia.org/wiki/Plug-in_(computing))
- [Pop PHP Framework](https://en.wikipedia.org/wiki/Pop_PHP_Framework)
- [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)
- [ProcessWire](https://en.wikipedia.org/wiki/ProcessWire)
- [Profiling (computer programming)](https://en.wikipedia.org/wiki/Profiling_(computer_programming))
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Prototype JavaScript Framework](https://en.wikipedia.org/wiki/Prototype_JavaScript_Framework)
- [Public-domain software](https://en.wikipedia.org/wiki/Public-domain_software)
- [Pyjs](https://en.wikipedia.org/wiki/Pyjs)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Qcodo](https://en.wikipedia.org/wiki/Qcodo)
- [Quixote (web framework)](https://en.wikipedia.org/wiki/Quixote_(web_framework))
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Rapid application development](https://en.wikipedia.org/wiki/Rapid_application_development)
- [React (software)](https://en.wikipedia.org/wiki/React_(software))
- [Remix (web framework)](https://en.wikipedia.org/wiki/Remix_(web_framework))
- [Remote Application Platform](https://en.wikipedia.org/wiki/Remote_Application_Platform)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Rocket (web framework)](https://en.wikipedia.org/wiki/Rocket_(web_framework))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Ruby on Rails](https://en.wikipedia.org/wiki/Ruby_on_Rails)
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [Simple Common Gateway Interface](https://en.wikipedia.org/wiki/Simple_Common_Gateway_Interface)
- [SQLAlchemy](https://en.wikipedia.org/wiki/SQLAlchemy)
- [SQLObject](https://en.wikipedia.org/wiki/SQLObject)
- [SQLite](https://en.wikipedia.org/wiki/SQLite)
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scalatra](https://en.wikipedia.org/wiki/Scalatra)
- [Seaside (software)](https://en.wikipedia.org/wiki/Seaside_(software))
- [Sencha Touch](https://en.wikipedia.org/wiki/Sencha_Touch)
- [Servant (web framework)](https://en.wikipedia.org/wiki/Servant_(web_framework))
- [Session (computer science)](https://en.wikipedia.org/wiki/Session_(computer_science))
- [Shiny (web framework)](https://en.wikipedia.org/wiki/Shiny_(web_framework))
- [Silverstripe CMS](https://en.wikipedia.org/wiki/Silverstripe_CMS)
- [Sinatra (software)](https://en.wikipedia.org/wiki/Sinatra_(software))
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Snap (web framework)](https://en.wikipedia.org/wiki/Snap_(web_framework))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Splunk](https://en.wikipedia.org/wiki/Splunk)
- [Spring Framework](https://en.wikipedia.org/wiki/Spring_Framework)
- [SproutCore](https://en.wikipedia.org/wiki/SproutCore)
- [Storm (software)](https://en.wikipedia.org/wiki/Storm_(software))
- [Stripes (framework)](https://en.wikipedia.org/wiki/Stripes_(framework))
- [Svelte](https://en.wikipedia.org/wiki/Svelte)
- [Adaptive Server Enterprise](https://en.wikipedia.org/wiki/Adaptive_Server_Enterprise)
- [Symfony](https://en.wikipedia.org/wiki/Symfony)
- [TACTIC (web framework)](https://en.wikipedia.org/wiki/TACTIC_(web_framework))
- [TYPO3](https://en.wikipedia.org/wiki/TYPO3)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Web template system](https://en.wikipedia.org/wiki/Web_template_system)
- [Test suite](https://en.wikipedia.org/wiki/Test_suite)
- [Thread pool](https://en.wikipedia.org/wiki/Thread_pool)
- [Tornado (web server)](https://en.wikipedia.org/wiki/Tornado_(web_server))
- [TurboGears](https://en.wikipedia.org/wiki/TurboGears)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [URL](https://en.wikipedia.org/wiki/URL)
- [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu)
- [Umbraco](https://en.wikipedia.org/wiki/Umbraco)
- [Vaadin](https://en.wikipedia.org/wiki/Vaadin)
- [Vert.x](https://en.wikipedia.org/wiki/Vert.x)
- [Vue.js](https://en.wikipedia.org/wiki/Vue.js)
- [WaveMaker](https://en.wikipedia.org/wiki/WaveMaker)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Web2py](https://en.wikipedia.org/wiki/Web2py)
- [WebGUI](https://en.wikipedia.org/wiki/WebGUI)
- [WebSharper](https://en.wikipedia.org/wiki/WebSharper)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [Web application](https://en.wikipedia.org/wiki/Web_application)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [Web cache](https://en.wikipedia.org/wiki/Web_cache)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [Web server](https://en.wikipedia.org/wiki/Web_server)
- [WordPress](https://en.wikipedia.org/wiki/WordPress)
- [Adapter pattern](https://en.wikipedia.org/wiki/Adapter_pattern)
- [Wt (web toolkit)](https://en.wikipedia.org/wiki/Wt_(web_toolkit))
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
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles with self-published sources from April 2024](https://en.wikipedia.org/wiki/Category:Articles_with_self-published_sources_from_April_2024)
- [Category:Python (programming language) web frameworks](https://en.wikipedia.org/wiki/Category:Python_(programming_language)_web_frameworks)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:34:25.888206+00:00_