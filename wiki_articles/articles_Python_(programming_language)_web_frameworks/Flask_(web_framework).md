# Flask (web framework)

## Article Metadata

- **Last Updated:** 2024-12-14T19:58:34.811155+00:00
- **Original Article:** [Flask (web framework)](https://en.wikipedia.org/wiki/Flask_(web_framework))
- **Language:** en
- **Page ID:** 29040606

## Summary

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open

## Categories

- Category:All articles containing potentially dated statements
- Category:All articles lacking reliable references
- Category:Articles containing potentially dated statements from October 2020
- Category:Articles lacking reliable references from April 2024
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Free software programmed in Python
- Category:Python (programming language) web frameworks
- Category:Short description matches Wikidata
- Category:Software using the BSD license

## Table of Contents

- History
- Components
- Features
- Example
- See also
- References
- External links

## Content

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools.
Applications that use the Flask framework include Pinterest and LinkedIn.

History
Flask was created by Armin Ronacher of Pocoo, an international group of Python enthusiasts formed in 2004. According to Ronacher, the idea was originally an April Fool's joke that was popular enough to make into a serious application. The name is a play on the earlier Bottle framework.
When Ronacher and Georg Brandl created a bulletin board system written in Python in 2004, the Pocoo projects Werkzeug and Jinja were developed.
In April 2016, the Pocoo team was disbanded and development of Flask and related libraries passed to the newly formed Pallets project. Since 2018, Flask-related data and objects can be rendered with Bootstrap.
Flask has become popular among Python enthusiasts. As of October 2020, it has the second-most number of stars on GitHub among Python web-development frameworks, only slightly behind Django, and was voted the most popular web framework in the Python Developers Survey for years between and including 2018 and 2022.

Components
The microframework Flask is part of the Pallets Projects (formerly Pocoo), and based on several others of them, all under a BSD license.

Werkzeug
Werkzeug (German for "tool") is a utility library for the Python programming language for Web Server Gateway Interface (WSGI) applications. Werkzeug can instantiate objects for request, response, and utility functions. It can be used as the basis for a custom software framework and supports Python 2.7 and 3.5 and later.

Jinja
Jinja, also by Ronacher, is a template engine for the Python programming language. Similar to the Django web framework, it handles templates in a sandbox.

MarkupSafe
MarkupSafe is a string handling library for the Python programming language. The eponymous MarkupSafe type extends the Python string type and marks its contents as "safe"; combining MarkupSafe with regular strings automatically escapes the unmarked strings, while avoiding double escaping of already marked strings.

ItsDangerous
ItsDangerous is a safe data serialization library for the Python programming language. It is used to store the session of a Flask application in a cookie without allowing users to tamper with the session contents.

Features
Development server and debugger
Integrated support for unit testing
RESTful request dispatching
Uses Jinja templating
Support for secure cookies (client side sessions)
100% WSGI 1.0 compliant
Unicode-based
Complete documentation
Google App Engine compatibility
Extensions available to extend functionality

Example
The following code shows a simple web application that displays "Hello World!" when visited:

See also
Django (web framework)
FastAPI
Jam.py
Pylons project
Tornado
Web2py
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
- [Apache Sling](https://en.wikipedia.org/wiki/Apache_Sling)
- [Apache Struts](https://en.wikipedia.org/wiki/Apache_Struts)
- [Apache Tapestry](https://en.wikipedia.org/wiki/Apache_Tapestry)
- [Apache Wicket](https://en.wikipedia.org/wiki/Apache_Wicket)
- [AppFuse](https://en.wikipedia.org/wiki/AppFuse)
- [April Fools' Day](https://en.wikipedia.org/wiki/April_Fools%27_Day)
- [Armin Ronacher](https://en.wikipedia.org/wiki/Armin_Ronacher)
- [Asynchronous Server Gateway Interface](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface)
- [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses)
- [Backbone.js](https://en.wikipedia.org/wiki/Backbone.js)
- [Base One Foundation Component Library](https://en.wikipedia.org/wiki/Base_One_Foundation_Component_Library)
- [Blazor](https://en.wikipedia.org/wiki/Blazor)
- [Bootstrap (front-end framework)](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CL-HTTP](https://en.wikipedia.org/wiki/CL-HTTP)
- [CLPython](https://en.wikipedia.org/wiki/CLPython)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [CakePHP](https://en.wikipedia.org/wiki/CakePHP)
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [CherryPy](https://en.wikipedia.org/wiki/CherryPy)
- [CircuitPython](https://en.wikipedia.org/wiki/CircuitPython)
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [CodeIgniter](https://en.wikipedia.org/wiki/CodeIgniter)
- [ColdBox Platform](https://en.wikipedia.org/wiki/ColdBox_Platform)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Comparison of server-side web frameworks](https://en.wikipedia.org/wiki/Comparison_of_server-side_web_frameworks)
- [CppCMS](https://en.wikipedia.org/wiki/CppCMS)
- [CubicWeb](https://en.wikipedia.org/wiki/CubicWeb)
- [Cython](https://en.wikipedia.org/wiki/Cython)
- [Dancer (software)](https://en.wikipedia.org/wiki/Dancer_(software))
- [Database](https://en.wikipedia.org/wiki/Database)
- [Debugger](https://en.wikipedia.org/wiki/Debugger)
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
- [Express.js](https://en.wikipedia.org/wiki/Express.js)
- [Ext JS](https://en.wikipedia.org/wiki/Ext_JS)
- [FastAPI](https://en.wikipedia.org/wiki/FastAPI)
- [Fastify](https://en.wikipedia.org/wiki/Fastify)
- [Fat-Free Framework](https://en.wikipedia.org/wiki/Fat-Free_Framework)
- [FuelPHP](https://en.wikipedia.org/wiki/FuelPHP)
- [German language](https://en.wikipedia.org/wiki/German_language)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Google App Engine](https://en.wikipedia.org/wiki/Google_App_Engine)
- [Google Closure Tools](https://en.wikipedia.org/wiki/Google_Closure_Tools)
- [Google Web Toolkit](https://en.wikipedia.org/wiki/Google_Web_Toolkit)
- [Grails (framework)](https://en.wikipedia.org/wiki/Grails_(framework))
- [Grav (CMS)](https://en.wikipedia.org/wiki/Grav_(CMS))
- [Grok (web framework)](https://en.wikipedia.org/wiki/Grok_(web_framework))
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
- [Gyroscope (software)](https://en.wikipedia.org/wiki/Gyroscope_(software))
- [HTTP cookie](https://en.wikipedia.org/wiki/HTTP_cookie)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Horde (software)](https://en.wikipedia.org/wiki/Horde_(software))
- [Htmx](https://en.wikipedia.org/wiki/Htmx)
- [ICEfaces](https://en.wikipedia.org/wiki/ICEfaces)
- [IDLE](https://en.wikipedia.org/wiki/IDLE)
- [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment)
- [IronPython](https://en.wikipedia.org/wiki/IronPython)
- [JBoss Seam](https://en.wikipedia.org/wiki/JBoss_Seam)
- [JHipster](https://en.wikipedia.org/wiki/JHipster)
- [JQuery](https://en.wikipedia.org/wiki/JQuery)
- [JWt (Java web toolkit)](https://en.wikipedia.org/wiki/JWt_(Java_web_toolkit))
- [Jakarta Faces](https://en.wikipedia.org/wiki/Jakarta_Faces)
- [Jam.py (web framework)](https://en.wikipedia.org/wiki/Jam.py_(web_framework))
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (software platform)](https://en.wikipedia.org/wiki/Java_(software_platform))
- [Jinja (template engine)](https://en.wikipedia.org/wiki/Jinja_(template_engine))
- [Joomla](https://en.wikipedia.org/wiki/Joomla)
- [Jython](https://en.wikipedia.org/wiki/Jython)
- [Knockout (web framework)](https://en.wikipedia.org/wiki/Knockout_(web_framework))
- [Laminas](https://en.wikipedia.org/wiki/Laminas)
- [Laravel](https://en.wikipedia.org/wiki/Laravel)
- [Li3 (software)](https://en.wikipedia.org/wiki/Li3_(software))
- [Lift (web framework)](https://en.wikipedia.org/wiki/Lift_(web_framework))
- [LinkedIn](https://en.wikipedia.org/wiki/LinkedIn)
- [List of Python software](https://en.wikipedia.org/wiki/List_of_Python_software)
- [Comparison of integrated development environments](https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments)
- [MODX](https://en.wikipedia.org/wiki/MODX)
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [Merb](https://en.wikipedia.org/wiki/Merb)
- [Meteor (web framework)](https://en.wikipedia.org/wiki/Meteor_(web_framework))
- [MicroPython](https://en.wikipedia.org/wiki/MicroPython)
- [Microframework](https://en.wikipedia.org/wiki/Microframework)
- [Midgard (software)](https://en.wikipedia.org/wiki/Midgard_(software))
- [Mojolicious](https://en.wikipedia.org/wiki/Mojolicious)
- [MonoRail (software)](https://en.wikipedia.org/wiki/MonoRail_(software))
- [MooTools](https://en.wikipedia.org/wiki/MooTools)
- [Neos Flow](https://en.wikipedia.org/wiki/Neos_Flow)
- [NestJS](https://en.wikipedia.org/wiki/NestJS)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Next.js](https://en.wikipedia.org/wiki/Next.js)
- [Ninja-IDE](https://en.wikipedia.org/wiki/Ninja-IDE)
- [Node.js](https://en.wikipedia.org/wiki/Node.js)
- [Numba](https://en.wikipedia.org/wiki/Numba)
- [Nuxt.js](https://en.wikipedia.org/wiki/Nuxt.js)
- [Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
- [ArsDigita Community System](https://en.wikipedia.org/wiki/ArsDigita_Community_System)
- [OpenUI5](https://en.wikipedia.org/wiki/OpenUI5)
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
- [Pinterest](https://en.wikipedia.org/wiki/Pinterest)
- [Play Framework](https://en.wikipedia.org/wiki/Play_Framework)
- [Pop PHP Framework](https://en.wikipedia.org/wiki/Pop_PHP_Framework)
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
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Conference](https://en.wikipedia.org/wiki/Python_Conference)
- [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation)
- [Python for S60](https://en.wikipedia.org/wiki/Python_for_S60)
- [Qcodo](https://en.wikipedia.org/wiki/Qcodo)
- [Quixote (web framework)](https://en.wikipedia.org/wiki/Quixote_(web_framework))
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [React (software)](https://en.wikipedia.org/wiki/React_(software))
- [Remix (web framework)](https://en.wikipedia.org/wiki/Remix_(web_framework))
- [Remote Application Platform](https://en.wikipedia.org/wiki/Remote_Application_Platform)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [REST](https://en.wikipedia.org/wiki/REST)
- [Rocket (web framework)](https://en.wikipedia.org/wiki/Rocket_(web_framework))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Ruby on Rails](https://en.wikipedia.org/wiki/Ruby_on_Rails)
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [Sandbox (computer security)](https://en.wikipedia.org/wiki/Sandbox_(computer_security))
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scalatra](https://en.wikipedia.org/wiki/Scalatra)
- [Seaside (software)](https://en.wikipedia.org/wiki/Seaside_(software))
- [Sencha Touch](https://en.wikipedia.org/wiki/Sencha_Touch)
- [Serialization](https://en.wikipedia.org/wiki/Serialization)
- [Servant (web framework)](https://en.wikipedia.org/wiki/Servant_(web_framework))
- [Session (computer science)](https://en.wikipedia.org/wiki/Session_(computer_science))
- [Shed Skin](https://en.wikipedia.org/wiki/Shed_Skin)
- [Shiny (web framework)](https://en.wikipedia.org/wiki/Shiny_(web_framework))
- [Silverstripe CMS](https://en.wikipedia.org/wiki/Silverstripe_CMS)
- [Sinatra (software)](https://en.wikipedia.org/wiki/Sinatra_(software))
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Snap (web framework)](https://en.wikipedia.org/wiki/Snap_(web_framework))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software framework](https://en.wikipedia.org/wiki/Software_framework)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Spring Framework](https://en.wikipedia.org/wiki/Spring_Framework)
- [SproutCore](https://en.wikipedia.org/wiki/SproutCore)
- [Spyder (software)](https://en.wikipedia.org/wiki/Spyder_(software))
- [Stackless Python](https://en.wikipedia.org/wiki/Stackless_Python)
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
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
- [Unicode](https://en.wikipedia.org/wiki/Unicode)
- [Unit testing](https://en.wikipedia.org/wiki/Unit_testing)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [Vaadin](https://en.wikipedia.org/wiki/Vaadin)
- [Vert.x](https://en.wikipedia.org/wiki/Vert.x)
- [Vue.js](https://en.wikipedia.org/wiki/Vue.js)
- [WaveMaker](https://en.wikipedia.org/wiki/WaveMaker)
- [Web2py](https://en.wikipedia.org/wiki/Web2py)
- [WebGUI](https://en.wikipedia.org/wiki/WebGUI)
- [WebSharper](https://en.wikipedia.org/wiki/WebSharper)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [WordPress](https://en.wikipedia.org/wiki/WordPress)
- [Wt (web toolkit)](https://en.wikipedia.org/wiki/Wt_(web_toolkit))
- [XOOPS](https://en.wikipedia.org/wiki/XOOPS)
- [Yaws (web server)](https://en.wikipedia.org/wiki/Yaws_(web_server))
- [Yesod (web framework)](https://en.wikipedia.org/wiki/Yesod_(web_framework))
- [Yii](https://en.wikipedia.org/wiki/Yii)
- [ZK (framework)](https://en.wikipedia.org/wiki/ZK_(framework))
- [Zope](https://en.wikipedia.org/wiki/Zope)
- [Wikipedia:No original research](https://en.wikipedia.org/wiki/Wikipedia:No_original_research)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Python (programming language)](https://en.wikipedia.org/wiki/Template:Python_(programming_language))
- [Template:Python web frameworks](https://en.wikipedia.org/wiki/Template:Python_web_frameworks)
- [Template:Web frameworks](https://en.wikipedia.org/wiki/Template:Web_frameworks)
- [Template talk:Python (programming language)](https://en.wikipedia.org/wiki/Template_talk:Python_(programming_language))
- [Template talk:Python web frameworks](https://en.wikipedia.org/wiki/Template_talk:Python_web_frameworks)
- [Template talk:Web frameworks](https://en.wikipedia.org/wiki/Template_talk:Web_frameworks)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles containing potentially dated statements from October 2020](https://en.wikipedia.org/wiki/Category:Articles_containing_potentially_dated_statements_from_October_2020)
- [Category:Articles lacking reliable references from April 2024](https://en.wikipedia.org/wiki/Category:Articles_lacking_reliable_references_from_April_2024)
- [Category:Python (programming language) web frameworks](https://en.wikipedia.org/wiki/Category:Python_(programming_language)_web_frameworks)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:58:34.811155+00:00_