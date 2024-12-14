# Django (web framework)

## Article Metadata

- **Last Updated:** 2024-12-14T19:58:29.160347+00:00
- **Original Article:** [Django (web framework)](https://en.wikipedia.org/wiki/Django_(web_framework))
- **Language:** en
- **Page ID:** 2247376

## Summary

Django ( JANG-goh; sometimes stylized as django) is a free and open-source, Python-based web framework that runs on a web server. It follows the model–template–views (MTV) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501(c)(3) non-profit.
Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and "pluggability" of components, less code, low 

## Categories

- Category:All articles lacking reliable references
- Category:Articles lacking reliable references from January 2015
- Category:Articles prone to spam from December 2017
- Category:Articles with short description
- Category:Commons category link from Wikidata
- Category:Free software programmed in Python
- Category:Python (programming language) web frameworks
- Category:Short description matches Wikidata
- Category:Software using the BSD license
- Category:Use dmy dates from July 2024
- Category:Web frameworks
- Category:Webarchive template wayback links

## Table of Contents

- History
- Features
- Version history
- DjangoCon
- Ports to other languages
- CMSs based on Django Framework
- See also
- References
- Bibliography
- External links

## Content

Django ( JANG-goh; sometimes stylized as django) is a free and open-source, Python-based web framework that runs on a web server. It follows the model–template–views (MTV) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501(c)(3) non-profit.
Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself. Python is used throughout, even for settings, files, and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models.
Some well-known sites that use Django include Instagram, Mozilla, Disqus, Bitbucket, Nextdoor, and Clubhouse.

History
Django was created in the autumn of 2003, when the web programmers at the Lawrence Journal-World newspaper, Adrian Holovaty and Simon Willison, began using Python to build applications. Jacob Kaplan-Moss was hired early in Django's development shortly before Willison's internship ended. It was released publicly under a BSD license in July 2005. The framework was named after guitarist Django Reinhardt. Holovaty is a Romani jazz guitar player inspired in part by Reinhardt's music.
In June 2008, it was announced that a newly formed Django Software Foundation (DSF) would maintain Django in the future.

Features
Components
Despite having its own nomenclature, such as naming the callable objects generating the HTTP responses "views", the core Django framework can be seen as an MVC architecture. It consists of an object-relational mapper (ORM) that mediates between data models (defined as Python classes) and a relational database ("Model"), a system for processing HTTP requests with a web templating system ("View"), and a regular-expression-based URL dispatcher ("Controller").
Also included in the core framework are:

a lightweight and standalone web server for development and testing
a form serialization and validation system that can translate between HTML forms and values suitable for storage in the database
a template system that utilizes the concept of inheritance borrowed from object-oriented programming
a caching framework that can use any of several cache methods
support for middleware classes that can intervene at various stages of request processing and carry out custom functions
an internal dispatcher system that allows components of an application to communicate events to each other via pre-defined signals
an internationalization system, including translations of Django's own components into a variety of languages
a serialization system that can produce and read XML and/or JSON representations of Django model instances
a system for extending the capabilities of the template engine
an interface to Python's built-in unit test framework

Bundled applications
The main Django distribution also bundles a number of applications in its "contrib" package, including:

an extensible authentication system
the dynamic administrative interface
tools for generating RSS and Atom syndication feeds
a "Sites" framework that allows one Django installation to run multiple websites, each with their own content and applications
tools for generating Sitemaps
built-in mitigation for cross-site request forgery, cross-site scripting, SQL injection, password cracking and other typical web attacks, most of them turned on by default
a framework for creating geographic information system (GIS) applications

Extensibility
Django's configuration system allows third party code to be plugged into a regular project, provided that it follows the reusable app conventions. More than 5000 packages are available to extend the framework's original behavior, providing solutions to issues the original tool didn't tackle: registration, search, API provision and consumption, CMS, etc.
This extensibility is, however, mitigated by internal components' dependencies. While the Django philosophy implies loose coupling, the template filters and tags assume one engine implementation, and both the auth and admin bundled applications require the use of the internal ORM. None of these filters or bundled apps are mandatory to run a Django project, but reusable apps tend to depend on them, encouraging developers to keep using the official stack in order to benefit fully from the apps ecosystem.

Server arrangements
Django can be run in conjunction with Apache, Nginx using WSGI, Gunicorn, or Cherokee using flup (a Python module). Django also includes the ability to launch a FastCGI server, enabling use behind any web server which supports FastCGI, such as Lighttpd or Hiawatha. It is also possible to use other WSGI-compliant web servers. Django officially supports five database backends: PostgreSQL, MySQL, MariaDB, SQLite, and Oracle. Microsoft SQL Server can be used with django-mssql while similarly external backends exist for IBM Db2, SQL Anywhere and Firebird. There is a fork named django-nonrel, which supports NoSQL databases, such as MongoDB and Google App Engine's Datastore.
Django may also be run in conjunction with Python on any Java EE application server such as GlassFish or JBoss. In this case django-jython must be installed in order to provide JDBC drivers for database connectivity, which also can provide functionality to compile Django in to a .war suitable for deployment.

Version history
The Django team will occasionally designate certain releases to be "long-term support" (LTS) releases. LTS releases will get security and data loss fixes applied for a guaranteed period of time, typically 3+ years, regardless of the pace of releases afterwards.

DjangoCon
There is a semiannual conference for Django developers and users, named "DjangoCon", that has been held since September 2008. DjangoCon is held annually in Europe, in May or June; while another is held in the United States in August or September, in various cities. The 2012 DjangoCon took place in Washington, D.C., from September 3 to 8. 2013 DjangoCon was held in Chicago at the Hyatt Regency Hotel and the post-conference Sprints were hosted at Digital Bootcamp, computer training center. The 2014 DjangoCon US returned to Portland, OR from August 30 to 6 September. The 2015 DjangoCon US was held in Austin, TX from September 6 to 11 at the AT&T Executive Center. The 2016 DjangoCon US was held in Philadelphia, PA at The Wharton School of the University of Pennsylvania from July 17 to 22. The 2017 DjangoCon US was held in Spokane, WA; in 2018 DjangoCon US was held in San Diego, CA. DjangoCon US 2019 was held again in San Diego, CA from September 22 to 27. DjangoCon 2021 took place virtually and in 2022, DjangoCon US returned to San Diego from October 16 to 21. DjangoCon US 2023 was held from October 16 to 20 at the Durham, NC convention center and DjangoCon US 2024 is scheduled to return to Durham for September 22 to 27.
Django mini-conferences are usually held every year as part of the Australian Python Conference 'PyCon AU'. Previously, these mini-conferences have been held in:

Hobart, Australia, in July 2013,
Brisbane, Australia, in August 2014 and 2015,
Melbourne, Australia in August 2016 and 2017, and
Sydney, Australia, in August 2018 and 2019.
Django has spawned user groups and meetups around the world, the most notable group is the Django Girls organization, which began in Poland but now has had events in 91 countries.

Ports to other languages
Programmers have ported Django's template engine design from Python to other languages, providing decent cross-platform support. Some of these options are more direct ports; others, though inspired by Django and retaining its concepts, take the liberty to deviate from Django's design:

Liquid for Ruby
Template::Swig for Perl
Twig for PHP and JavaScript
Jinja for Python
ErlyDTL for Erlang

CMSs based on Django Framework
Django as a framework is capable of building a complete CMS, however there are dedicated CMS projects which are built upon and extend the Django framework. Below is a list of a few of the more popular Django-based CMSs:

Django CMS
Wagtail
Mezzanine

See also
FastAPI
Flask
Jam.py
Pylons project
Web2py
Tornado
Ruby on Rails
Comparison of web frameworks
Django REST framework

References
Bibliography
External links

Official website

## Related Articles

### Internal Links

- [.NET](https://en.wikipedia.org/wiki/.NET)
- [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses)
- [501(c)(3) organization](https://en.wikipedia.org/wiki/501(c)(3)_organization)
- [AIDA/Web](https://en.wikipedia.org/wiki/AIDA/Web)
- [Asynchronous Server Gateway Interface](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface)
- [ASP.NET](https://en.wikipedia.org/wiki/ASP.NET)
- [ASP.NET AJAX](https://en.wikipedia.org/wiki/ASP.NET_AJAX)
- [ASP.NET Core](https://en.wikipedia.org/wiki/ASP.NET_Core)
- [ASP.NET Dynamic Data](https://en.wikipedia.org/wiki/ASP.NET_Dynamic_Data)
- [ASP.NET MVC](https://en.wikipedia.org/wiki/ASP.NET_MVC)
- [ASP.NET Razor](https://en.wikipedia.org/wiki/ASP.NET_Razor)
- [ASP.NET Web Forms](https://en.wikipedia.org/wiki/ASP.NET_Web_Forms)
- [Adobe ColdFusion](https://en.wikipedia.org/wiki/Adobe_ColdFusion)
- [Adrian Holovaty](https://en.wikipedia.org/wiki/Adrian_Holovaty)
- [AngularJS](https://en.wikipedia.org/wiki/AngularJS)
- [Angular (web framework)](https://en.wikipedia.org/wiki/Angular_(web_framework))
- [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server)
- [Apache Sling](https://en.wikipedia.org/wiki/Apache_Sling)
- [Apache Struts](https://en.wikipedia.org/wiki/Apache_Struts)
- [Apache Tapestry](https://en.wikipedia.org/wiki/Apache_Tapestry)
- [Apache Wicket](https://en.wikipedia.org/wiki/Apache_Wicket)
- [AppFuse](https://en.wikipedia.org/wiki/AppFuse)
- [API](https://en.wikipedia.org/wiki/API)
- [Architectural pattern](https://en.wikipedia.org/wiki/Architectural_pattern)
- [Atom (web standard)](https://en.wikipedia.org/wiki/Atom_(web_standard))
- [Austin, Texas](https://en.wikipedia.org/wiki/Austin,_Texas)
- [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses)
- [Backbone.js](https://en.wikipedia.org/wiki/Backbone.js)
- [Base One Foundation Component Library](https://en.wikipedia.org/wiki/Base_One_Foundation_Component_Library)
- [Bitbucket](https://en.wikipedia.org/wiki/Bitbucket)
- [Blazor](https://en.wikipedia.org/wiki/Blazor)
- [Brisbane](https://en.wikipedia.org/wiki/Brisbane)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CL-HTTP](https://en.wikipedia.org/wiki/CL-HTTP)
- [Cross-site request forgery](https://en.wikipedia.org/wiki/Cross-site_request_forgery)
- [CakePHP](https://en.wikipedia.org/wiki/CakePHP)
- [Callable object](https://en.wikipedia.org/wiki/Callable_object)
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [Cherokee (web server)](https://en.wikipedia.org/wiki/Cherokee_(web_server))
- [CherryPy](https://en.wikipedia.org/wiki/CherryPy)
- [Clubhouse (app)](https://en.wikipedia.org/wiki/Clubhouse_(app))
- [CodeIgniter](https://en.wikipedia.org/wiki/CodeIgniter)
- [ColdBox Platform](https://en.wikipedia.org/wiki/ColdBox_Platform)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Comparison of server-side web frameworks](https://en.wikipedia.org/wiki/Comparison_of_server-side_web_frameworks)
- [Content management system](https://en.wikipedia.org/wiki/Content_management_system)
- [Content management system](https://en.wikipedia.org/wiki/Content_management_system)
- [CppCMS](https://en.wikipedia.org/wiki/CppCMS)
- [Create, read, update and delete](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)
- [Cross-site request forgery](https://en.wikipedia.org/wiki/Cross-site_request_forgery)
- [Cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting)
- [CubicWeb](https://en.wikipedia.org/wiki/CubicWeb)
- [Dancer (software)](https://en.wikipedia.org/wiki/Dancer_(software))
- [Data model](https://en.wikipedia.org/wiki/Data_model)
- [Data modeling](https://en.wikipedia.org/wiki/Data_modeling)
- [Disqus](https://en.wikipedia.org/wiki/Disqus)
- [Django](https://en.wikipedia.org/wiki/Django)
- [Django CMS](https://en.wikipedia.org/wiki/Django_CMS)
- [Django Girls](https://en.wikipedia.org/wiki/Django_Girls)
- [Django Reinhardt](https://en.wikipedia.org/wiki/Django_Reinhardt)
- [Django Software Foundation](https://en.wikipedia.org/wiki/Django_Software_Foundation)
- [Dojo Toolkit](https://en.wikipedia.org/wiki/Dojo_Toolkit)
- [Don't repeat yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
- [DNN (software)](https://en.wikipedia.org/wiki/DNN_(software))
- [Drogon (software)](https://en.wikipedia.org/wiki/Drogon_(software))
- [Drupal](https://en.wikipedia.org/wiki/Drupal)
- [Durham, North Carolina](https://en.wikipedia.org/wiki/Durham,_North_Carolina)
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
- [File size](https://en.wikipedia.org/wiki/File_size)
- [Firebird (database server)](https://en.wikipedia.org/wiki/Firebird_(database_server))
- [Flask (web framework)](https://en.wikipedia.org/wiki/Flask_(web_framework))
- [Fork (software development)](https://en.wikipedia.org/wiki/Fork_(software_development))
- [Free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software)
- [FuelPHP](https://en.wikipedia.org/wiki/FuelPHP)
- [Geographic information system](https://en.wikipedia.org/wiki/Geographic_information_system)
- [GlassFish](https://en.wikipedia.org/wiki/GlassFish)
- [Google App Engine](https://en.wikipedia.org/wiki/Google_App_Engine)
- [Google Closure Tools](https://en.wikipedia.org/wiki/Google_Closure_Tools)
- [Google Web Toolkit](https://en.wikipedia.org/wiki/Google_Web_Toolkit)
- [Grails (framework)](https://en.wikipedia.org/wiki/Grails_(framework))
- [Grav (CMS)](https://en.wikipedia.org/wiki/Grav_(CMS))
- [Grok (web framework)](https://en.wikipedia.org/wiki/Grok_(web_framework))
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn)
- [Gyroscope (software)](https://en.wikipedia.org/wiki/Gyroscope_(software))
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Hiawatha (web server)](https://en.wikipedia.org/wiki/Hiawatha_(web_server))
- [Hobart](https://en.wikipedia.org/wiki/Hobart)
- [Horde (software)](https://en.wikipedia.org/wiki/Horde_(software))
- [Htmx](https://en.wikipedia.org/wiki/Htmx)
- [IBM Db2](https://en.wikipedia.org/wiki/IBM_Db2)
- [ICEfaces](https://en.wikipedia.org/wiki/ICEfaces)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Inheritance (object-oriented programming)](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
- [Instagram](https://en.wikipedia.org/wiki/Instagram)
- [Internationalization and localization](https://en.wikipedia.org/wiki/Internationalization_and_localization)
- [WildFly](https://en.wikipedia.org/wiki/WildFly)
- [JBoss Seam](https://en.wikipedia.org/wiki/JBoss_Seam)
- [Java Database Connectivity](https://en.wikipedia.org/wiki/Java_Database_Connectivity)
- [JHipster](https://en.wikipedia.org/wiki/JHipster)
- [JQuery](https://en.wikipedia.org/wiki/JQuery)
- [JSON](https://en.wikipedia.org/wiki/JSON)
- [JWt (Java web toolkit)](https://en.wikipedia.org/wiki/JWt_(Java_web_toolkit))
- [Jakarta Faces](https://en.wikipedia.org/wiki/Jakarta_Faces)
- [Jam.py (web framework)](https://en.wikipedia.org/wiki/Jam.py_(web_framework))
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (software platform)](https://en.wikipedia.org/wiki/Java_(software_platform))
- [Jakarta EE](https://en.wikipedia.org/wiki/Jakarta_EE)
- [Jinja (template engine)](https://en.wikipedia.org/wiki/Jinja_(template_engine))
- [Joomla](https://en.wikipedia.org/wiki/Joomla)
- [Knockout (web framework)](https://en.wikipedia.org/wiki/Knockout_(web_framework))
- [Laminas](https://en.wikipedia.org/wiki/Laminas)
- [Laravel](https://en.wikipedia.org/wiki/Laravel)
- [Lawrence Journal-World](https://en.wikipedia.org/wiki/Lawrence_Journal-World)
- [Li3 (software)](https://en.wikipedia.org/wiki/Li3_(software))
- [Lift (web framework)](https://en.wikipedia.org/wiki/Lift_(web_framework))
- [Lighttpd](https://en.wikipedia.org/wiki/Lighttpd)
- [MODX](https://en.wikipedia.org/wiki/MODX)
- [MariaDB](https://en.wikipedia.org/wiki/MariaDB)
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [Megabyte](https://en.wikipedia.org/wiki/Megabyte)
- [Melbourne](https://en.wikipedia.org/wiki/Melbourne)
- [Merb](https://en.wikipedia.org/wiki/Merb)
- [Meteor (web framework)](https://en.wikipedia.org/wiki/Meteor_(web_framework))
- [Mezzanine (CMS)](https://en.wikipedia.org/wiki/Mezzanine_(CMS))
- [Microsoft SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server)
- [Middleware](https://en.wikipedia.org/wiki/Middleware)
- [Midgard (software)](https://en.wikipedia.org/wiki/Midgard_(software))
- [Model–view–controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
- [Mojolicious](https://en.wikipedia.org/wiki/Mojolicious)
- [MongoDB](https://en.wikipedia.org/wiki/MongoDB)
- [MonoRail (software)](https://en.wikipedia.org/wiki/MonoRail_(software))
- [MooTools](https://en.wikipedia.org/wiki/MooTools)
- [Mozilla Foundation](https://en.wikipedia.org/wiki/Mozilla_Foundation)
- [MySQL](https://en.wikipedia.org/wiki/MySQL)
- [Neos Flow](https://en.wikipedia.org/wiki/Neos_Flow)
- [NestJS](https://en.wikipedia.org/wiki/NestJS)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Next.js](https://en.wikipedia.org/wiki/Next.js)
- [Nextdoor](https://en.wikipedia.org/wiki/Nextdoor)
- [Nginx](https://en.wikipedia.org/wiki/Nginx)
- [NoSQL](https://en.wikipedia.org/wiki/NoSQL)
- [Node.js](https://en.wikipedia.org/wiki/Node.js)
- [Nuxt.js](https://en.wikipedia.org/wiki/Nuxt.js)
- [Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
- [ArsDigita Community System](https://en.wikipedia.org/wiki/ArsDigita_Community_System)
- [OpenUI5](https://en.wikipedia.org/wiki/OpenUI5)
- [Oracle Application Express](https://en.wikipedia.org/wiki/Oracle_Application_Express)
- [Oracle Database](https://en.wikipedia.org/wiki/Oracle_Database)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PHP-Fusion](https://en.wikipedia.org/wiki/PHP-Fusion)
- [PHP-Nuke](https://en.wikipedia.org/wiki/PHP-Nuke)
- [PL/SQL](https://en.wikipedia.org/wiki/PL/SQL)
- [PRADO (framework)](https://en.wikipedia.org/wiki/PRADO_(framework))
- [Padrino (web framework)](https://en.wikipedia.org/wiki/Padrino_(web_framework))
- [Password cracking](https://en.wikipedia.org/wiki/Password_cracking)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Phalcon (framework)](https://en.wikipedia.org/wiki/Phalcon_(framework))
- [Phoenix (web framework)](https://en.wikipedia.org/wiki/Phoenix_(web_framework))
- [Play Framework](https://en.wikipedia.org/wiki/Play_Framework)
- [Pop PHP Framework](https://en.wikipedia.org/wiki/Pop_PHP_Framework)
- [Portland, Oregon](https://en.wikipedia.org/wiki/Portland,_Oregon)
- [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)
- [ProcessWire](https://en.wikipedia.org/wiki/ProcessWire)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Prototype JavaScript Framework](https://en.wikipedia.org/wiki/Prototype_JavaScript_Framework)
- [Pyjs](https://en.wikipedia.org/wiki/Pyjs)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Conference](https://en.wikipedia.org/wiki/Python_Conference)
- [Qcodo](https://en.wikipedia.org/wiki/Qcodo)
- [Quixote (web framework)](https://en.wikipedia.org/wiki/Quixote_(web_framework))
- [RSS](https://en.wikipedia.org/wiki/RSS)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [React (software)](https://en.wikipedia.org/wiki/React_(software))
- [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Relational database](https://en.wikipedia.org/wiki/Relational_database)
- [Remix (web framework)](https://en.wikipedia.org/wiki/Remix_(web_framework))
- [Remote Application Platform](https://en.wikipedia.org/wiki/Remote_Application_Platform)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Reusability](https://en.wikipedia.org/wiki/Reusability)
- [Rocket (web framework)](https://en.wikipedia.org/wiki/Rocket_(web_framework))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Ruby on Rails](https://en.wikipedia.org/wiki/Ruby_on_Rails)
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [SQL Anywhere](https://en.wikipedia.org/wiki/SQL_Anywhere)
- [SQL injection](https://en.wikipedia.org/wiki/SQL_injection)
- [SQLite](https://en.wikipedia.org/wiki/SQLite)
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scalatra](https://en.wikipedia.org/wiki/Scalatra)
- [Seaside (software)](https://en.wikipedia.org/wiki/Seaside_(software))
- [Sencha Touch](https://en.wikipedia.org/wiki/Sencha_Touch)
- [Serialization](https://en.wikipedia.org/wiki/Serialization)
- [Servant (web framework)](https://en.wikipedia.org/wiki/Servant_(web_framework))
- [Shiny (web framework)](https://en.wikipedia.org/wiki/Shiny_(web_framework))
- [Silverstripe CMS](https://en.wikipedia.org/wiki/Silverstripe_CMS)
- [Simon Willison](https://en.wikipedia.org/wiki/Simon_Willison)
- [Sinatra (software)](https://en.wikipedia.org/wiki/Sinatra_(software))
- [Sitemaps](https://en.wikipedia.org/wiki/Sitemaps)
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Snap (web framework)](https://en.wikipedia.org/wiki/Snap_(web_framework))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Spring Framework](https://en.wikipedia.org/wiki/Spring_Framework)
- [Timeboxing](https://en.wikipedia.org/wiki/Timeboxing)
- [SproutCore](https://en.wikipedia.org/wiki/SproutCore)
- [Stripes (framework)](https://en.wikipedia.org/wiki/Stripes_(framework))
- [Svelte](https://en.wikipedia.org/wiki/Svelte)
- [Sydney](https://en.wikipedia.org/wiki/Sydney)
- [Symfony](https://en.wikipedia.org/wiki/Symfony)
- [TACTIC (web framework)](https://en.wikipedia.org/wiki/TACTIC_(web_framework))
- [TYPO3](https://en.wikipedia.org/wiki/TYPO3)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Tornado (web server)](https://en.wikipedia.org/wiki/Tornado_(web_server))
- [TurboGears](https://en.wikipedia.org/wiki/TurboGears)
- [Twig (template engine)](https://en.wikipedia.org/wiki/Twig_(template_engine))
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Type introspection](https://en.wikipedia.org/wiki/Type_introspection)
- [Umbraco](https://en.wikipedia.org/wiki/Umbraco)
- [URL](https://en.wikipedia.org/wiki/URL)
- [Unit testing](https://en.wikipedia.org/wiki/Unit_testing)
- [Vaadin](https://en.wikipedia.org/wiki/Vaadin)
- [Vert.x](https://en.wikipedia.org/wiki/Vert.x)
- [Vue.js](https://en.wikipedia.org/wiki/Vue.js)
- [Wagtail (CMS)](https://en.wikipedia.org/wiki/Wagtail_(CMS))
- [WaveMaker](https://en.wikipedia.org/wiki/WaveMaker)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Web2py](https://en.wikipedia.org/wiki/Web2py)
- [WebGUI](https://en.wikipedia.org/wiki/WebGUI)
- [WebSharper](https://en.wikipedia.org/wiki/WebSharper)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [Web cache](https://en.wikipedia.org/wiki/Web_cache)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [Web development](https://en.wikipedia.org/wiki/Web_development)
- [Web server](https://en.wikipedia.org/wiki/Web_server)
- [Web template system](https://en.wikipedia.org/wiki/Web_template_system)
- [Wharton School](https://en.wikipedia.org/wiki/Wharton_School)
- [WordPress](https://en.wikipedia.org/wiki/WordPress)
- [Wt (web toolkit)](https://en.wikipedia.org/wiki/Wt_(web_toolkit))
- [XML](https://en.wikipedia.org/wiki/XML)
- [XOOPS](https://en.wikipedia.org/wiki/XOOPS)
- [Yaws (web server)](https://en.wikipedia.org/wiki/Yaws_(web_server))
- [Yesod (web framework)](https://en.wikipedia.org/wiki/Yesod_(web_framework))
- [Yii](https://en.wikipedia.org/wiki/Yii)
- [ZK (framework)](https://en.wikipedia.org/wiki/ZK_(framework))
- [Zope](https://en.wikipedia.org/wiki/Zope)
- [Wikipedia:No original research](https://en.wikipedia.org/wiki/Wikipedia:No_original_research)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Python web frameworks](https://en.wikipedia.org/wiki/Template:Python_web_frameworks)
- [Template:Web frameworks](https://en.wikipedia.org/wiki/Template:Web_frameworks)
- [Template talk:Python web frameworks](https://en.wikipedia.org/wiki/Template_talk:Python_web_frameworks)
- [Template talk:Web frameworks](https://en.wikipedia.org/wiki/Template_talk:Web_frameworks)
- [Help:IPA/English](https://en.wikipedia.org/wiki/Help:IPA/English)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Pronunciation respelling key](https://en.wikipedia.org/wiki/Help:Pronunciation_respelling_key)
- [Category:Articles lacking reliable references from January 2015](https://en.wikipedia.org/wiki/Category:Articles_lacking_reliable_references_from_January_2015)
- [Category:Articles prone to spam from December 2017](https://en.wikipedia.org/wiki/Category:Articles_prone_to_spam_from_December_2017)
- [Category:Python (programming language) web frameworks](https://en.wikipedia.org/wiki/Category:Python_(programming_language)_web_frameworks)
- [Category:Use dmy dates from July 2024](https://en.wikipedia.org/wiki/Category:Use_dmy_dates_from_July_2024)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:58:29.160347+00:00_