# Jam.py (web framework)

## Article Metadata

- **Last Updated:** 2024-12-14T19:58:59.447985+00:00
- **Original Article:** [Jam.py (web framework)](https://en.wikipedia.org/wiki/Jam.py_(web_framework))
- **Language:** en
- **Page ID:** 59662859

## Summary

Jam.py is free and open-source low-code/no-code "full stack" WSGI rapid application development framework for the JavaScript and Python programming language.
Jam.py is a  Single-page, event driven
 low-code development platform for database-driven business web applications, based on DRY principle, with emphasis on CRUD.
It is designed to automatically create JavaScript web forms from the underlying database tables, although a form can be created manually if required.
It offers a built-in web ser

## Categories

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

## Related Articles

### Internal Links

- ["Hello, World!" program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)
- [.NET](https://en.wikipedia.org/wiki/.NET)
- [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses)
- [AIDA/Web](https://en.wikipedia.org/wiki/AIDA/Web)
- [ASP.NET](https://en.wikipedia.org/wiki/ASP.NET)
- [ASP.NET AJAX](https://en.wikipedia.org/wiki/ASP.NET_AJAX)
- [ASP.NET Core](https://en.wikipedia.org/wiki/ASP.NET_Core)
- [ASP.NET Dynamic Data](https://en.wikipedia.org/wiki/ASP.NET_Dynamic_Data)
- [ASP.NET MVC](https://en.wikipedia.org/wiki/ASP.NET_MVC)
- [ASP.NET Razor](https://en.wikipedia.org/wiki/ASP.NET_Razor)
- [ASP.NET Web Forms](https://en.wikipedia.org/wiki/ASP.NET_Web_Forms)
- [Adobe ColdFusion](https://en.wikipedia.org/wiki/Adobe_ColdFusion)
- [Ajax (programming)](https://en.wikipedia.org/wiki/Ajax_(programming))
- [AngularJS](https://en.wikipedia.org/wiki/AngularJS)
- [Angular (web framework)](https://en.wikipedia.org/wiki/Angular_(web_framework))
- [Apache Sling](https://en.wikipedia.org/wiki/Apache_Sling)
- [Apache Struts](https://en.wikipedia.org/wiki/Apache_Struts)
- [Apache Tapestry](https://en.wikipedia.org/wiki/Apache_Tapestry)
- [Apache Wicket](https://en.wikipedia.org/wiki/Apache_Wicket)
- [AppFuse](https://en.wikipedia.org/wiki/AppFuse)
- [Asynchronous Server Gateway Interface](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface)
- [Authentication](https://en.wikipedia.org/wiki/Authentication)
- [Backbone.js](https://en.wikipedia.org/wiki/Backbone.js)
- [Base One Foundation Component Library](https://en.wikipedia.org/wiki/Base_One_Foundation_Component_Library)
- [Blazor](https://en.wikipedia.org/wiki/Blazor)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CL-HTTP](https://en.wikipedia.org/wiki/CL-HTTP)
- [CLPython](https://en.wikipedia.org/wiki/CLPython)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [CakePHP](https://en.wikipedia.org/wiki/CakePHP)
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [CherryPy](https://en.wikipedia.org/wiki/CherryPy)
- [CircuitPython](https://en.wikipedia.org/wiki/CircuitPython)
- [CodeIgniter](https://en.wikipedia.org/wiki/CodeIgniter)
- [ColdBox Platform](https://en.wikipedia.org/wiki/ColdBox_Platform)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Comparison of server-side web frameworks](https://en.wikipedia.org/wiki/Comparison_of_server-side_web_frameworks)
- [Computing platform](https://en.wikipedia.org/wiki/Computing_platform)
- [CppCMS](https://en.wikipedia.org/wiki/CppCMS)
- [Create, read, update and delete](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [CubicWeb](https://en.wikipedia.org/wiki/CubicWeb)
- [Cython](https://en.wikipedia.org/wiki/Cython)
- [Don't repeat yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
- [Dancer (software)](https://en.wikipedia.org/wiki/Dancer_(software))
- [Data migration](https://en.wikipedia.org/wiki/Data_migration)
- [Delphi (software)](https://en.wikipedia.org/wiki/Delphi_(software))
- [Django (web framework)](https://en.wikipedia.org/wiki/Django_(web_framework))
- [Dojo Toolkit](https://en.wikipedia.org/wiki/Dojo_Toolkit)
- [DNN (software)](https://en.wikipedia.org/wiki/DNN_(software))
- [Drogon (software)](https://en.wikipedia.org/wiki/Drogon_(software))
- [Drupal](https://en.wikipedia.org/wiki/Drupal)
- [EZ Publish](https://en.wikipedia.org/wiki/EZ_Publish)
- [Elixir (programming language)](https://en.wikipedia.org/wiki/Elixir_(programming_language))
- [Ember.js](https://en.wikipedia.org/wiki/Ember.js)
- [Eric (software)](https://en.wikipedia.org/wiki/Eric_(software))
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Event-driven architecture](https://en.wikipedia.org/wiki/Event-driven_architecture)
- [Express.js](https://en.wikipedia.org/wiki/Express.js)
- [Ext JS](https://en.wikipedia.org/wiki/Ext_JS)
- [FastAPI](https://en.wikipedia.org/wiki/FastAPI)
- [Fastify](https://en.wikipedia.org/wiki/Fastify)
- [Fat-Free Framework](https://en.wikipedia.org/wiki/Fat-Free_Framework)
- [Firebird (database server)](https://en.wikipedia.org/wiki/Firebird_(database_server))
- [Flask (web framework)](https://en.wikipedia.org/wiki/Flask_(web_framework))
- [Foreign key](https://en.wikipedia.org/wiki/Foreign_key)
- [Free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software)
- [FuelPHP](https://en.wikipedia.org/wiki/FuelPHP)
- [Google Closure Tools](https://en.wikipedia.org/wiki/Google_Closure_Tools)
- [Google Web Toolkit](https://en.wikipedia.org/wiki/Google_Web_Toolkit)
- [Grails (framework)](https://en.wikipedia.org/wiki/Grails_(framework))
- [Graphical user interface builder](https://en.wikipedia.org/wiki/Graphical_user_interface_builder)
- [Grav (CMS)](https://en.wikipedia.org/wiki/Grav_(CMS))
- [Grok (web framework)](https://en.wikipedia.org/wiki/Grok_(web_framework))
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
- [Gyroscope (software)](https://en.wikipedia.org/wiki/Gyroscope_(software))
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Horde (software)](https://en.wikipedia.org/wiki/Horde_(software))
- [Htmx](https://en.wikipedia.org/wiki/Htmx)
- [ICEfaces](https://en.wikipedia.org/wiki/ICEfaces)
- [IDLE](https://en.wikipedia.org/wiki/IDLE)
- [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment)
- [Internationalization](https://en.wikipedia.org/wiki/Internationalization)
- [IronPython](https://en.wikipedia.org/wiki/IronPython)
- [JBoss Seam](https://en.wikipedia.org/wiki/JBoss_Seam)
- [JHipster](https://en.wikipedia.org/wiki/JHipster)
- [JQuery](https://en.wikipedia.org/wiki/JQuery)
- [JSON](https://en.wikipedia.org/wiki/JSON)
- [JWt (Java web toolkit)](https://en.wikipedia.org/wiki/JWt_(Java_web_toolkit))
- [Jakarta Faces](https://en.wikipedia.org/wiki/Jakarta_Faces)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (software platform)](https://en.wikipedia.org/wiki/Java_(software_platform))
- [Joomla](https://en.wikipedia.org/wiki/Joomla)
- [Jython](https://en.wikipedia.org/wiki/Jython)
- [Knockout (web framework)](https://en.wikipedia.org/wiki/Knockout_(web_framework))
- [Laminas](https://en.wikipedia.org/wiki/Laminas)
- [Laravel](https://en.wikipedia.org/wiki/Laravel)
- [Li3 (software)](https://en.wikipedia.org/wiki/Li3_(software))
- [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice)
- [Lift (web framework)](https://en.wikipedia.org/wiki/Lift_(web_framework))
- [List of Python software](https://en.wikipedia.org/wiki/List_of_Python_software)
- [Comparison of integrated development environments](https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments)
- [List of low-code development platforms](https://en.wikipedia.org/wiki/List_of_low-code_development_platforms)
- [Low-code development platform](https://en.wikipedia.org/wiki/Low-code_development_platform)
- [MODX](https://en.wikipedia.org/wiki/MODX)
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [Merb](https://en.wikipedia.org/wiki/Merb)
- [Meteor (web framework)](https://en.wikipedia.org/wiki/Meteor_(web_framework))
- [MicroPython](https://en.wikipedia.org/wiki/MicroPython)
- [Microsoft SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server)
- [Midgard (software)](https://en.wikipedia.org/wiki/Midgard_(software))
- [Mojolicious](https://en.wikipedia.org/wiki/Mojolicious)
- [MonoRail (software)](https://en.wikipedia.org/wiki/MonoRail_(software))
- [MooTools](https://en.wikipedia.org/wiki/MooTools)
- [MySQL](https://en.wikipedia.org/wiki/MySQL)
- [Neos Flow](https://en.wikipedia.org/wiki/Neos_Flow)
- [NestJS](https://en.wikipedia.org/wiki/NestJS)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Next.js](https://en.wikipedia.org/wiki/Next.js)
- [Ninja-IDE](https://en.wikipedia.org/wiki/Ninja-IDE)
- [No-code development platform](https://en.wikipedia.org/wiki/No-code_development_platform)
- [Node.js](https://en.wikipedia.org/wiki/Node.js)
- [Numba](https://en.wikipedia.org/wiki/Numba)
- [Nuxt.js](https://en.wikipedia.org/wiki/Nuxt.js)
- [ArsDigita Community System](https://en.wikipedia.org/wiki/ArsDigita_Community_System)
- [OpenDocument](https://en.wikipedia.org/wiki/OpenDocument)
- [OpenUI5](https://en.wikipedia.org/wiki/OpenUI5)
- [Oracle Application Express](https://en.wikipedia.org/wiki/Oracle_Application_Express)
- [Oracle Database](https://en.wikipedia.org/wiki/Oracle_Database)
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
- [Programming language implementation](https://en.wikipedia.org/wiki/Programming_language_implementation)
- [Prototype JavaScript Framework](https://en.wikipedia.org/wiki/Prototype_JavaScript_Framework)
- [Psyco](https://en.wikipedia.org/wiki/Psyco)
- [PyCharm](https://en.wikipedia.org/wiki/PyCharm)
- [PyDev](https://en.wikipedia.org/wiki/PyDev)
- [PyPy](https://en.wikipedia.org/wiki/PyPy)
- [Pyjs](https://en.wikipedia.org/wiki/Pyjs)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [PythonAnywhere](https://en.wikipedia.org/wiki/PythonAnywhere)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Conference](https://en.wikipedia.org/wiki/Python_Conference)
- [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation)
- [Python for S60](https://en.wikipedia.org/wiki/Python_for_S60)
- [Qcodo](https://en.wikipedia.org/wiki/Qcodo)
- [Quixote (web framework)](https://en.wikipedia.org/wiki/Quixote_(web_framework))
- [REST](https://en.wikipedia.org/wiki/REST)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Rapid application development](https://en.wikipedia.org/wiki/Rapid_application_development)
- [React (software)](https://en.wikipedia.org/wiki/React_(software))
- [Remix (web framework)](https://en.wikipedia.org/wiki/Remix_(web_framework))
- [Remote Application Platform](https://en.wikipedia.org/wiki/Remote_Application_Platform)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Rocket (web framework)](https://en.wikipedia.org/wiki/Rocket_(web_framework))
- [Role-based access control](https://en.wikipedia.org/wiki/Role-based_access_control)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Ruby on Rails](https://en.wikipedia.org/wiki/Ruby_on_Rails)
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [SQLite](https://en.wikipedia.org/wiki/SQLite)
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scalatra](https://en.wikipedia.org/wiki/Scalatra)
- [Seaside (software)](https://en.wikipedia.org/wiki/Seaside_(software))
- [Sencha Touch](https://en.wikipedia.org/wiki/Sencha_Touch)
- [Servant (web framework)](https://en.wikipedia.org/wiki/Servant_(web_framework))
- [Client–server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
- [Shed Skin](https://en.wikipedia.org/wiki/Shed_Skin)
- [Shiny (web framework)](https://en.wikipedia.org/wiki/Shiny_(web_framework))
- [Silverstripe CMS](https://en.wikipedia.org/wiki/Silverstripe_CMS)
- [Sinatra (software)](https://en.wikipedia.org/wiki/Sinatra_(software))
- [Single-page application](https://en.wikipedia.org/wiki/Single-page_application)
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Snap (web framework)](https://en.wikipedia.org/wiki/Snap_(web_framework))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software maintenance](https://en.wikipedia.org/wiki/Software_maintenance)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Spring Framework](https://en.wikipedia.org/wiki/Spring_Framework)
- [SproutCore](https://en.wikipedia.org/wiki/SproutCore)
- [Spyder (software)](https://en.wikipedia.org/wiki/Spyder_(software))
- [Stackless Python](https://en.wikipedia.org/wiki/Stackless_Python)
- [Stripes (framework)](https://en.wikipedia.org/wiki/Stripes_(framework))
- [Svelte](https://en.wikipedia.org/wiki/Svelte)
- [Symfony](https://en.wikipedia.org/wiki/Symfony)
- [TACTIC (web framework)](https://en.wikipedia.org/wiki/TACTIC_(web_framework))
- [TYPO3](https://en.wikipedia.org/wiki/TYPO3)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Web template system](https://en.wikipedia.org/wiki/Web_template_system)
- [Tornado (web server)](https://en.wikipedia.org/wiki/Tornado_(web_server))
- [TurboGears](https://en.wikipedia.org/wiki/TurboGears)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Umbraco](https://en.wikipedia.org/wiki/Umbraco)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [User interface](https://en.wikipedia.org/wiki/User_interface)
- [Vaadin](https://en.wikipedia.org/wiki/Vaadin)
- [Vert.x](https://en.wikipedia.org/wiki/Vert.x)
- [Vue.js](https://en.wikipedia.org/wiki/Vue.js)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [WaveMaker](https://en.wikipedia.org/wiki/WaveMaker)
- [Web2py](https://en.wikipedia.org/wiki/Web2py)
- [WebGUI](https://en.wikipedia.org/wiki/WebGUI)
- [WebSharper](https://en.wikipedia.org/wiki/WebSharper)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [Web application](https://en.wikipedia.org/wiki/Web_application)
- [HTML form](https://en.wikipedia.org/wiki/HTML_form)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [WordPress](https://en.wikipedia.org/wiki/WordPress)
- [Wt (web toolkit)](https://en.wikipedia.org/wiki/Wt_(web_toolkit))
- [XOOPS](https://en.wikipedia.org/wiki/XOOPS)
- [Yaws (web server)](https://en.wikipedia.org/wiki/Yaws_(web_server))
- [Yesod (web framework)](https://en.wikipedia.org/wiki/Yesod_(web_framework))
- [Yii](https://en.wikipedia.org/wiki/Yii)
- [ZK (framework)](https://en.wikipedia.org/wiki/ZK_(framework))
- [Zope](https://en.wikipedia.org/wiki/Zope)
- [Template:Cite web](https://en.wikipedia.org/wiki/Template:Cite_web)
- [Template:Python (programming language)](https://en.wikipedia.org/wiki/Template:Python_(programming_language))
- [Template:Python web frameworks](https://en.wikipedia.org/wiki/Template:Python_web_frameworks)
- [Template:Web frameworks](https://en.wikipedia.org/wiki/Template:Web_frameworks)
- [Template talk:Python (programming language)](https://en.wikipedia.org/wiki/Template_talk:Python_(programming_language))
- [Template talk:Python web frameworks](https://en.wikipedia.org/wiki/Template_talk:Python_web_frameworks)
- [Template talk:Web frameworks](https://en.wikipedia.org/wiki/Template_talk:Web_frameworks)
- [Help:CS1 errors](https://en.wikipedia.org/wiki/Help:CS1_errors)
- [Category:Python (programming language) web frameworks](https://en.wikipedia.org/wiki/Category:Python_(programming_language)_web_frameworks)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:58:59.447985+00:00_