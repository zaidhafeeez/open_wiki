# Pylons project

## Article Metadata

- **Last Updated:** 2024-12-15T03:43:30.274641+00:00
- **Original Article:** [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- **Language:** en
- **Page ID:** 36723720

## Summary

Pylons Project is an open-source organization that develops a set of web application technologies written in Python. Initially the project was a single web framework called Pylons, but after the merger with the repoze.bfg framework under the new name Pyramid, the Pylons Project now consists of multiple related web application technologies.

## Categories

- Category:Articles with short description
- Category:Cross-platform free software
- Category:Free software programmed in Python
- Category:Python (programming language) software
- Category:Python (programming language) web frameworks
- Category:Short description is different from Wikidata
- Category:Webarchive template wayback links

## Table of Contents

- Pyramid
- Pylons Web Framework
- See also
- References
- External links

## Content

Pylons Project is an open-source organization that develops a set of web application technologies written in Python. Initially the project was a single web framework called Pylons, but after the merger with the repoze.bfg framework under the new name Pyramid, the Pylons Project now consists of multiple related web application technologies.

Pyramid
Pyramid is an open source web framework written in Python and is based on WSGI. It is a minimalistic web framework inspired by Zope, Pylons and Django.
Originally called "repoze.bfg", Pyramid gathered attention mostly in the Zope and Plone community as the Open Society Institute's KARL project migrated from Plone to BFG. In 2010 it was announced that the Pylons framework will move over to using BFG as a base in version 1.5. As a result of the inclusion of BFG into the Pylons project, BFG was renamed Pyramid.

Features
Pyramid is a minimalistic, platform-independent web framework. It is persistence agnostic and is integrated both with SQL databases via SQLAlchemy and with the Zope Object Database, as well as other NoSQL databases, such as CouchDB.
Pyramid allows developers to define routes using regular expressions that map to objects. Like its fellow framework Zope, Pyramid also allows hierarchical object traversal, where each part of a URL is an object containing other objects, in a way that is similar to folders in a filesystem.

Pylons Web Framework
Pylons Framework is an open-source Web application framework written in Python. It makes extensive use of the Web Server Gateway Interface standard to promote reusability and to separate functionality into distinct modules. It is strongly influenced by Ruby on Rails: two of its main components, Routes and WebHelpers, are Python reimplementations of Rails features.

Structure
Pylons is well known for having a near-complete stack of third-party tools, eschewing the "not-invented-here" phenomenon.

Installation, dependencies, and setup
The official installation method of Pylons is through EasyInstall via the Python Package Index (PyPI), and most of the additional tools are typically installed the same way. EasyInstall also handles package dependencies when relevant. Some distributions could also package Pylons and Paste, but it is likely that any distribution's packages would lag the official distribution. Pylons may also be installed by hand by renaming its .egg file to .zip and extracting the contents.
Paste is used for project setup, testing, and deployment. Using the common INI configuration format, Paste allows for multiple "profiles", so that developers can run development and deployment setups from the same codebase without revealing sensitive parts of Pylons, such as the interactive debugger, to production users.

URL dispatch
Currently the only widely used URL dispatcher for Pylons is Routes, a Python reimplementation of Ruby on Rails' URL dispatching, although any WSGI-compatible URL dispatcher can be used.  While Routes is a separate library, it was developed for use in Pylons and its development remains closely in sync with Pylons.

HTML generation
Another piece of Rails adapted for Pylons is WebHelpers, which provides URL mapping based on the Routes configuration. WebHelpers also provides some utility functions for generating JavaScript code making use of the script.aculo.us and Prototype libraries.
FormEncode and FormBuild are used for HTML form validation and generation; there has been some use of Mako for form generation using Mako's inheritance model.

Templating
Myghty was the default Pylons templating language, but as of version 0.9.6 it has been replaced by Mako. Both templating languages are text-based (as opposed to XML-based), and support includes, inheritance and embedding arbitrary Python code.
Because of Pylons' loosely coupled layers, other templating languages can be used as well. Genshi, an XML-based templating language, can be used in lieu of either Mako or Myghty.

Database abstraction and object-relational mapping
Pylons has no default database library. Both SQLObject and SQLAlchemy are known to be used.

Merger with repoze.bfg and birth of Pyramid Web Framework
Pylons has developed into the Pylons Project, and the old code from Pylons 1.0 is now in maintenance-only mode. However, pursuant to the project's merger with repoze.bfg since November 2010, newer versions of Pylons are actually different from the original Pylons 1.0. Pylons developers initially planned to rewrite certain portions of the code, but they observed that the new code was approximating repoze.bfg, which led to the merger of Pylons and repoze.bfg. This led to repoze.bfg (a part of the Repoze Python-based web framework) to become rebranded and relaunched as the Pyramid web framework.

See also
Django (web framework)
FastAPI
Flask (web framework)
Web2py
TurboGears: a derivative project, built on top of Pylons
Tornado
Comparison of web frameworks

References
Further reading
Gardner, James (January 2009). The Definitive Guide to Pylons. Berkeley, CA: Apress. doi:10.1007/978-1-4302-0534-0. ISBN 978-1-59059-934-1.

External links
Official website

## Related Articles

### Internal Links

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
- [Springer Nature](https://en.wikipedia.org/wiki/Springer_Nature)
- [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses)
- [Backbone.js](https://en.wikipedia.org/wiki/Backbone.js)
- [Base One Foundation Component Library](https://en.wikipedia.org/wiki/Base_One_Foundation_Component_Library)
- [Blazor](https://en.wikipedia.org/wiki/Blazor)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CL-HTTP](https://en.wikipedia.org/wiki/CL-HTTP)
- [CakePHP](https://en.wikipedia.org/wiki/CakePHP)
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [CherryPy](https://en.wikipedia.org/wiki/CherryPy)
- [CodeIgniter](https://en.wikipedia.org/wiki/CodeIgniter)
- [ColdBox Platform](https://en.wikipedia.org/wiki/ColdBox_Platform)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Comparison of server-side web frameworks](https://en.wikipedia.org/wiki/Comparison_of_server-side_web_frameworks)
- [Apache CouchDB](https://en.wikipedia.org/wiki/Apache_CouchDB)
- [CppCMS](https://en.wikipedia.org/wiki/CppCMS)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [CubicWeb](https://en.wikipedia.org/wiki/CubicWeb)
- [Dancer (software)](https://en.wikipedia.org/wiki/Dancer_(software))
- [Django (web framework)](https://en.wikipedia.org/wiki/Django_(web_framework))
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
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
- [Fastify](https://en.wikipedia.org/wiki/Fastify)
- [Fat-Free Framework](https://en.wikipedia.org/wiki/Fat-Free_Framework)
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
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Horde (software)](https://en.wikipedia.org/wiki/Horde_(software))
- [Htmx](https://en.wikipedia.org/wiki/Htmx)
- [ICEfaces](https://en.wikipedia.org/wiki/ICEfaces)
- [INI file](https://en.wikipedia.org/wiki/INI_file)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [JBoss Seam](https://en.wikipedia.org/wiki/JBoss_Seam)
- [JHipster](https://en.wikipedia.org/wiki/JHipster)
- [JQuery](https://en.wikipedia.org/wiki/JQuery)
- [JWt (Java web toolkit)](https://en.wikipedia.org/wiki/JWt_(Java_web_toolkit))
- [Jakarta Faces](https://en.wikipedia.org/wiki/Jakarta_Faces)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (software platform)](https://en.wikipedia.org/wiki/Java_(software_platform))
- [Joomla](https://en.wikipedia.org/wiki/Joomla)
- [Knockout (web framework)](https://en.wikipedia.org/wiki/Knockout_(web_framework))
- [Laminas](https://en.wikipedia.org/wiki/Laminas)
- [Laravel](https://en.wikipedia.org/wiki/Laravel)
- [Li3 (software)](https://en.wikipedia.org/wiki/Li3_(software))
- [Lift (web framework)](https://en.wikipedia.org/wiki/Lift_(web_framework))
- [MODX](https://en.wikipedia.org/wiki/MODX)
- [Mako (template engine)](https://en.wikipedia.org/wiki/Mako_(template_engine))
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [Merb](https://en.wikipedia.org/wiki/Merb)
- [Meteor (web framework)](https://en.wikipedia.org/wiki/Meteor_(web_framework))
- [Midgard (software)](https://en.wikipedia.org/wiki/Midgard_(software))
- [Minimalism (computing)](https://en.wikipedia.org/wiki/Minimalism_(computing))
- [Mod wsgi](https://en.wikipedia.org/wiki/Mod_wsgi)
- [Mojolicious](https://en.wikipedia.org/wiki/Mojolicious)
- [MonoRail (software)](https://en.wikipedia.org/wiki/MonoRail_(software))
- [MooTools](https://en.wikipedia.org/wiki/MooTools)
- [Neos Flow](https://en.wikipedia.org/wiki/Neos_Flow)
- [NestJS](https://en.wikipedia.org/wiki/NestJS)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Next.js](https://en.wikipedia.org/wiki/Next.js)
- [NoSQL](https://en.wikipedia.org/wiki/NoSQL)
- [Node.js](https://en.wikipedia.org/wiki/Node.js)
- [Not invented here](https://en.wikipedia.org/wiki/Not_invented_here)
- [Nuxt.js](https://en.wikipedia.org/wiki/Nuxt.js)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [ArsDigita Community System](https://en.wikipedia.org/wiki/ArsDigita_Community_System)
- [OpenUI5](https://en.wikipedia.org/wiki/OpenUI5)
- [Open Society Foundations](https://en.wikipedia.org/wiki/Open_Society_Foundations)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Oracle Application Express](https://en.wikipedia.org/wiki/Oracle_Application_Express)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PHP-Fusion](https://en.wikipedia.org/wiki/PHP-Fusion)
- [PHP-Nuke](https://en.wikipedia.org/wiki/PHP-Nuke)
- [PL/SQL](https://en.wikipedia.org/wiki/PL/SQL)
- [PRADO (framework)](https://en.wikipedia.org/wiki/PRADO_(framework))
- [Padrino (web framework)](https://en.wikipedia.org/wiki/Padrino_(web_framework))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Permissive software license](https://en.wikipedia.org/wiki/Permissive_software_license)
- [Phalcon (framework)](https://en.wikipedia.org/wiki/Phalcon_(framework))
- [Phoenix (web framework)](https://en.wikipedia.org/wiki/Phoenix_(web_framework))
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Play Framework](https://en.wikipedia.org/wiki/Play_Framework)
- [Plone (software)](https://en.wikipedia.org/wiki/Plone_(software))
- [Pop PHP Framework](https://en.wikipedia.org/wiki/Pop_PHP_Framework)
- [ProcessWire](https://en.wikipedia.org/wiki/ProcessWire)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Prototype JavaScript Framework](https://en.wikipedia.org/wiki/Prototype_JavaScript_Framework)
- [Pyjs](https://en.wikipedia.org/wiki/Pyjs)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Package Index](https://en.wikipedia.org/wiki/Python_Package_Index)
- [Python Paste](https://en.wikipedia.org/wiki/Python_Paste)
- [Qcodo](https://en.wikipedia.org/wiki/Qcodo)
- [Quixote (web framework)](https://en.wikipedia.org/wiki/Quixote_(web_framework))
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [React (software)](https://en.wikipedia.org/wiki/React_(software))
- [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Remix (web framework)](https://en.wikipedia.org/wiki/Remix_(web_framework))
- [Remote Application Platform](https://en.wikipedia.org/wiki/Remote_Application_Platform)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Rocket (web framework)](https://en.wikipedia.org/wiki/Rocket_(web_framework))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Ruby on Rails](https://en.wikipedia.org/wiki/Ruby_on_Rails)
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [SQLAlchemy](https://en.wikipedia.org/wiki/SQLAlchemy)
- [SQLObject](https://en.wikipedia.org/wiki/SQLObject)
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scalatra](https://en.wikipedia.org/wiki/Scalatra)
- [Prototype JavaScript Framework](https://en.wikipedia.org/wiki/Prototype_JavaScript_Framework)
- [Seaside (software)](https://en.wikipedia.org/wiki/Seaside_(software))
- [Sencha Touch](https://en.wikipedia.org/wiki/Sencha_Touch)
- [Servant (web framework)](https://en.wikipedia.org/wiki/Servant_(web_framework))
- [Shiny (web framework)](https://en.wikipedia.org/wiki/Shiny_(web_framework))
- [Silverstripe CMS](https://en.wikipedia.org/wiki/Silverstripe_CMS)
- [Sinatra (software)](https://en.wikipedia.org/wiki/Sinatra_(software))
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Snap (web framework)](https://en.wikipedia.org/wiki/Snap_(web_framework))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Spring Framework](https://en.wikipedia.org/wiki/Spring_Framework)
- [SproutCore](https://en.wikipedia.org/wiki/SproutCore)
- [Stripes (framework)](https://en.wikipedia.org/wiki/Stripes_(framework))
- [Svelte](https://en.wikipedia.org/wiki/Svelte)
- [Symfony](https://en.wikipedia.org/wiki/Symfony)
- [TACTIC (web framework)](https://en.wikipedia.org/wiki/TACTIC_(web_framework))
- [TYPO3](https://en.wikipedia.org/wiki/TYPO3)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Tornado (web server)](https://en.wikipedia.org/wiki/Tornado_(web_server))
- [TurboGears](https://en.wikipedia.org/wiki/TurboGears)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [URL](https://en.wikipedia.org/wiki/URL)
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
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [WordPress](https://en.wikipedia.org/wiki/WordPress)
- [Wt (web toolkit)](https://en.wikipedia.org/wiki/Wt_(web_toolkit))
- [XML](https://en.wikipedia.org/wiki/XML)
- [XOOPS](https://en.wikipedia.org/wiki/XOOPS)
- [Yaws (web server)](https://en.wikipedia.org/wiki/Yaws_(web_server))
- [Yesod (web framework)](https://en.wikipedia.org/wiki/Yesod_(web_framework))
- [Yii](https://en.wikipedia.org/wiki/Yii)
- [ZK (framework)](https://en.wikipedia.org/wiki/ZK_(framework))
- [Zope](https://en.wikipedia.org/wiki/Zope)
- [Zope Object Database](https://en.wikipedia.org/wiki/Zope_Object_Database)
- [Template:Python web frameworks](https://en.wikipedia.org/wiki/Template:Python_web_frameworks)
- [Template:Web frameworks](https://en.wikipedia.org/wiki/Template:Web_frameworks)
- [Template talk:Python web frameworks](https://en.wikipedia.org/wiki/Template_talk:Python_web_frameworks)
- [Template talk:Web frameworks](https://en.wikipedia.org/wiki/Template_talk:Web_frameworks)
- [Category:Python (programming language) web frameworks](https://en.wikipedia.org/wiki/Category:Python_(programming_language)_web_frameworks)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:43:30.274641+00:00_