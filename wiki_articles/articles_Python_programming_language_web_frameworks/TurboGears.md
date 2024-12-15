# TurboGears

## Article Metadata

- **Last Updated:** 2024-12-15T03:59:08.792486+00:00
- **Original Article:** [TurboGears](https://en.wikipedia.org/wiki/TurboGears)
- **Language:** en
- **Page ID:** 3177599

## Summary

TurboGears is a Python web application framework consisting of several WSGI components such as WebOb, SQLAlchemy, Kajiki template language and Repoze.
TurboGears is designed around the model–view–controller (MVC) architecture, much like Struts or Ruby on Rails, designed to make rapid web application development in Python easier and more maintainable. Since version 2.3 the framework has also been providing a "minimal mode" which enables it to act as a microframework for usage in environments wher

## Categories

- Category:All articles with self-published sources
- Category:All articles with unsourced statements
- Category:Articles with self-published sources from April 2024
- Category:Articles with short description
- Category:Articles with unsourced statements from February 2007
- Category:Python (programming language) software
- Category:Python (programming language) web frameworks
- Category:Short description matches Wikidata
- Category:Software using the MIT license

## Table of Contents

- TurboGears components
- Template plugins
- Project history
- Future of TurboGears
- See also
- References
- External links

## Content

TurboGears is a Python web application framework consisting of several WSGI components such as WebOb, SQLAlchemy, Kajiki template language and Repoze.
TurboGears is designed around the model–view–controller (MVC) architecture, much like Struts or Ruby on Rails, designed to make rapid web application development in Python easier and more maintainable. Since version 2.3 the framework has also been providing a "minimal mode" which enables it to act as a microframework for usage in environments where the whole stack is not required nor wanted.

TurboGears components
TurboGears is built on top of numerous disparate libraries and middleware. The default tools have changed between the 1.x, 2.x and 2.3+ series, but most of these components can be used in either as there is support for many alternative configurations. The following are the primary components a developer would interact with.

TurboGears 2.x components
SQLAlchemy (Model) - defines the table structures of the user's database and how to link them to Python objects the user's controller can interact with.
Ming (Model) - provides the data access layer for MongoDB, much like SQLAlchemy defines how to link MongoDB collections to Python objects the user's controller can interact with.
Kajiki (previously Genshi) (View) - defines templates for the HTML or XHTML the user will generate. This is where the user defines the front-end the client will interact with.
Repoze - Repoze.who is used to handle security (identification and authentication). Users can define authorization rules based on predicates attached to controllers, the framework already provides some built-in predicates, but custom ones can be written.
ToscaWidgets - is the primary widget library for creating forms and complex GUIs. Tosca by default will generate simple HTML forms, but can also be used as a middleware to connect to more advanced JavaScript widgets and toolkits. Unlike TurboGears 1.x, there is no longer a preferred/integrated JavaScript library.
Gearbox - is the toolkit used by TurboGears to manage projects, create new ones and serve TurboGears applications but the user can also connect to Apache, Nginx, or any other WSGI-compatible webserver.
Versions before 2.3 would also use:

Pylons (Controller) - this middleware handles all the user's back-end logic and connects to the user's webserver to offer up data to the web.
Paster was the command toolkit and webserver used in place of Gearbox.
Repoze.what - Used to handle authorization respectively. When defining elements of the user's controller to be exposed to the web, repoze.what predicates define who can access them and under what conditions.

TurboGears 1.x components
SQLObject (Model) - data backend that can create a database or interface with existing data on many database servers.
SQLAlchemy is slated to become the default in TurboGears >= 1.1.
Kid (View) - XHTML frontend templating engine where all templates are valid XHTML or XML files that are usually made in a way that allows opening these templates as simple XHTML files to check the design. At the same time features are provided to embed snippets of Python in a XMLish manner.
Genshi is the successor to Kid and will replace it as the default templating engine in TurboGears >= 1.1. It is nearly 100% syntax-compatible to Kid.
CherryPy (Controller) - middleware that allows web applications to be programmed by writing event handlers that return data to (in TurboGears case) templates. The same data can also be received in Ajax fashion as a JSON data stream.
MochiKit is the preferred, but optional JavaScript library for TurboGears 1.x. It is a designed to make programming in JavaScript more pythonic. It is mostly used for implementing Ajax features and widgets as it provides an interface to get JSON data streams in asynchronous manner.

Template plugins
Templating languages other than Genshi can be used through the user's app's configuration file. Plugins currently supported in 2.1 are Myghty, Jinja2, Mako, Cheetah, and Kajiki. Kid support is not currently planned as Genshi is virtually identical. This list may continue to change in future versions.

Project history
TurboGears was originally created in 2005 by Kevin Dangoor as the framework behind the as yet unreleased Zesty News product. When he released it as an open source framework in the end of September 2005, it received more than 30,000 screencast downloads in the first 3 months.
January 2007 Kevin Dangoor retired as project leader and Alberto Valverde managed the project as his successor, but subsequently stepped down due to other personal commitments. Alberto is still involved in the TurboGears community through his ToscaWidgets project. The TurboGears project is now managed jointly by a group of about half a dozen core developers under the leadership of Mark Ramm (as the TurboGears 2 development lead) and Florent Aide (as the Turbogears 1.x release manager).
In June 2007 the community began experiments to put the TurboGears API on top of components and protocols used in Pylons and there was speculation that the two frameworks may finally be merging. However, the official TurboGears 2 documentation states that this is unlikely to happen, due to the "different, but compatible priorities" of both projects. Pylons wanted to stay focused on low level, extensible design while TurboGears was focused on offering a complete, user-friendly package, and so the two work together much in the same way Debian and Ubuntu do now. The new 2.x branch had its first stable release in May 2009.
As of Fall 2008, TurboGears has a large and healthy community with over 3000 users on the TurboGears mailing list, a book from Prentice Hall published in Nov. '06, and a number of open-source and proprietary TurboGears applications deployed to the real world. The development progresses at a moderate but steady pace and was also newly fueled by a successful participation of the project as a Google Summer of Code mentoring organization in 2008 and 2009. TurboGears 1.1, aimed at helping legacy sites make the transition to 2.x, was released in October 2009. A new revision of the book is in the works to update it in line with the changes TurboGears 2 has brought.
In 2010, the project faltered somewhat. The lead developers were called away due to real life issues. By the end of Jan, 2011, though, the project had begun reorganizing and working on getting back on track. After several months getting infrastructure in order and working through coding issues, TurboGears has managed to release new versions (2.0.4 and 2.1.2).
In 2013, while maintaining backward compatibility, the project has moved away from the Pylons codebase to support Python 3, provide speed ups and an easier install process. This led to the release of version 2.3.0 in August 2013. It has also been announced a faster release cycle which should lead to a maintenance release every ~3 months.

Future of TurboGears
TurboGears development is now focused primarily on the new 2.x branch, with version 2.3 now being the main track with Python 3 support.
A transition path from the 1.x branch to the 2.x branch is provided through the 1.1 and 1.5 releases which moved the default ORM and templating languages to match the one used by the 2.x series. The TurboGears team made it clear to new users that 2.x is the future, and 1.x is merely maintained for the convenience of existing users.
During 2011 the lead developers of TurboGears have been in talks with the Pylons project to join forces with them and Repoze.BFG's developers as a new unified project called Pyramid. Due to the backward compatibility issues this move would have, and guaranteed TurboGears keeps being a reliable platform on long term, the current team decided to collaborate with the Pylons Project on everything possible but not to base the TurboGears core on Pyramid.
Future development, Python 3 support and speed improvements have happened in the 2.3 branch which has seen a full rewrite of the TurboGears core while keeping it backward compatible with existing applications, since that release TurboGears had its own core instead of being based on the Pylons framework.
During the 2.3 series the framework has been experimenting with a so-called "minimal mode" which makes it able to act as a micro-framework de facto reducing the dependencies from tens to just 3 and positioning TurboGears between Flask and Django in the rose of python frameworks for its objectives, as it aims as being able to scale from a micro-framework to a full-stack framework depending just on the fact that the TurboGears2 or the tg.devtools package is used.
Since version 2.4 the framework has now a modular components based architecture, which allows users to enable and replace the components at their will, thus making TurboGears actually follow its mission of being a web framework that scales with users needs.

See also
Django
Comparison of web frameworks

References
Ramm, M; Dangoor, K; Sayfan, G (November 7, 2006). Rapid Web Applications with TurboGears, Prentice Hall. ISBN 0-13-243388-5

Notes
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
- [Ajax (programming)](https://en.wikipedia.org/wiki/Ajax_(programming))
- [AngularJS](https://en.wikipedia.org/wiki/AngularJS)
- [Angular (web framework)](https://en.wikipedia.org/wiki/Angular_(web_framework))
- [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server)
- [Apache Sling](https://en.wikipedia.org/wiki/Apache_Sling)
- [Apache Struts](https://en.wikipedia.org/wiki/Apache_Struts)
- [Apache Tapestry](https://en.wikipedia.org/wiki/Apache_Tapestry)
- [Apache Wicket](https://en.wikipedia.org/wiki/Apache_Wicket)
- [AppFuse](https://en.wikipedia.org/wiki/AppFuse)
- [Backbone.js](https://en.wikipedia.org/wiki/Backbone.js)
- [Base One Foundation Component Library](https://en.wikipedia.org/wiki/Base_One_Foundation_Component_Library)
- [Blazor](https://en.wikipedia.org/wiki/Blazor)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CL-HTTP](https://en.wikipedia.org/wiki/CL-HTTP)
- [CakePHP](https://en.wikipedia.org/wiki/CakePHP)
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [CheetahTemplate](https://en.wikipedia.org/wiki/CheetahTemplate)
- [CherryPy](https://en.wikipedia.org/wiki/CherryPy)
- [CodeIgniter](https://en.wikipedia.org/wiki/CodeIgniter)
- [ColdBox Platform](https://en.wikipedia.org/wiki/ColdBox_Platform)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Comparison of server-side web frameworks](https://en.wikipedia.org/wiki/Comparison_of_server-side_web_frameworks)
- [CppCMS](https://en.wikipedia.org/wiki/CppCMS)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [CubicWeb](https://en.wikipedia.org/wiki/CubicWeb)
- [Dancer (software)](https://en.wikipedia.org/wiki/Dancer_(software))
- [Data model](https://en.wikipedia.org/wiki/Data_model)
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
- [Fastify](https://en.wikipedia.org/wiki/Fastify)
- [Fat-Free Framework](https://en.wikipedia.org/wiki/Fat-Free_Framework)
- [Flask (web framework)](https://en.wikipedia.org/wiki/Flask_(web_framework))
- [FuelPHP](https://en.wikipedia.org/wiki/FuelPHP)
- [Genshi (templating language)](https://en.wikipedia.org/wiki/Genshi_(templating_language))
- [Google Closure Tools](https://en.wikipedia.org/wiki/Google_Closure_Tools)
- [Google Summer of Code](https://en.wikipedia.org/wiki/Google_Summer_of_Code)
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
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [JBoss Seam](https://en.wikipedia.org/wiki/JBoss_Seam)
- [JHipster](https://en.wikipedia.org/wiki/JHipster)
- [JQuery](https://en.wikipedia.org/wiki/JQuery)
- [JSON](https://en.wikipedia.org/wiki/JSON)
- [JWt (Java web toolkit)](https://en.wikipedia.org/wiki/JWt_(Java_web_toolkit))
- [Jakarta Faces](https://en.wikipedia.org/wiki/Jakarta_Faces)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (software platform)](https://en.wikipedia.org/wiki/Java_(software_platform))
- [Jinja (template engine)](https://en.wikipedia.org/wiki/Jinja_(template_engine))
- [Joomla](https://en.wikipedia.org/wiki/Joomla)
- [Comparison of web template engines](https://en.wikipedia.org/wiki/Comparison_of_web_template_engines)
- [Knockout (web framework)](https://en.wikipedia.org/wiki/Knockout_(web_framework))
- [GNU Lesser General Public License](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)
- [Laminas](https://en.wikipedia.org/wiki/Laminas)
- [Laravel](https://en.wikipedia.org/wiki/Laravel)
- [Li3 (software)](https://en.wikipedia.org/wiki/Li3_(software))
- [Lift (web framework)](https://en.wikipedia.org/wiki/Lift_(web_framework))
- [MIT License](https://en.wikipedia.org/wiki/MIT_License)
- [MODX](https://en.wikipedia.org/wiki/MODX)
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [Merb](https://en.wikipedia.org/wiki/Merb)
- [Meteor (web framework)](https://en.wikipedia.org/wiki/Meteor_(web_framework))
- [Microframework](https://en.wikipedia.org/wiki/Microframework)
- [Midgard (software)](https://en.wikipedia.org/wiki/Midgard_(software))
- [MochiKit](https://en.wikipedia.org/wiki/MochiKit)
- [Model–view–controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
- [Mojolicious](https://en.wikipedia.org/wiki/Mojolicious)
- [MonoRail (software)](https://en.wikipedia.org/wiki/MonoRail_(software))
- [MooTools](https://en.wikipedia.org/wiki/MooTools)
- [Neos Flow](https://en.wikipedia.org/wiki/Neos_Flow)
- [NestJS](https://en.wikipedia.org/wiki/NestJS)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Next.js](https://en.wikipedia.org/wiki/Next.js)
- [Nginx](https://en.wikipedia.org/wiki/Nginx)
- [Node.js](https://en.wikipedia.org/wiki/Node.js)
- [Nuxt.js](https://en.wikipedia.org/wiki/Nuxt.js)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
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
- [Pop PHP Framework](https://en.wikipedia.org/wiki/Pop_PHP_Framework)
- [Prentice Hall](https://en.wikipedia.org/wiki/Prentice_Hall)
- [ProcessWire](https://en.wikipedia.org/wiki/ProcessWire)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Prototype JavaScript Framework](https://en.wikipedia.org/wiki/Prototype_JavaScript_Framework)
- [Pyjs](https://en.wikipedia.org/wiki/Pyjs)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Paste](https://en.wikipedia.org/wiki/Python_Paste)
- [Qcodo](https://en.wikipedia.org/wiki/Qcodo)
- [Quixote (web framework)](https://en.wikipedia.org/wiki/Quixote_(web_framework))
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [React (software)](https://en.wikipedia.org/wiki/React_(software))
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
- [Screencast](https://en.wikipedia.org/wiki/Screencast)
- [Seaside (software)](https://en.wikipedia.org/wiki/Seaside_(software))
- [Sencha Touch](https://en.wikipedia.org/wiki/Sencha_Touch)
- [Servant (web framework)](https://en.wikipedia.org/wiki/Servant_(web_framework))
- [Shiny (web framework)](https://en.wikipedia.org/wiki/Shiny_(web_framework))
- [Silverstripe CMS](https://en.wikipedia.org/wiki/Silverstripe_CMS)
- [Sinatra (software)](https://en.wikipedia.org/wiki/Sinatra_(software))
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Snap (web framework)](https://en.wikipedia.org/wiki/Snap_(web_framework))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
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
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Umbraco](https://en.wikipedia.org/wiki/Umbraco)
- [Vaadin](https://en.wikipedia.org/wiki/Vaadin)
- [Vert.x](https://en.wikipedia.org/wiki/Vert.x)
- [Vue.js](https://en.wikipedia.org/wiki/Vue.js)
- [WaveMaker](https://en.wikipedia.org/wiki/WaveMaker)
- [Web2py](https://en.wikipedia.org/wiki/Web2py)
- [WebGUI](https://en.wikipedia.org/wiki/WebGUI)
- [WebSharper](https://en.wikipedia.org/wiki/WebSharper)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [WordPress](https://en.wikipedia.org/wiki/WordPress)
- [Wt (web toolkit)](https://en.wikipedia.org/wiki/Wt_(web_toolkit))
- [XOOPS](https://en.wikipedia.org/wiki/XOOPS)
- [Yaws (web server)](https://en.wikipedia.org/wiki/Yaws_(web_server))
- [Yesod (web framework)](https://en.wikipedia.org/wiki/Yesod_(web_framework))
- [Yii](https://en.wikipedia.org/wiki/Yii)
- [ZK (framework)](https://en.wikipedia.org/wiki/ZK_(framework))
- [Zope](https://en.wikipedia.org/wiki/Zope)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Reliable sources](https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Python web frameworks](https://en.wikipedia.org/wiki/Template:Python_web_frameworks)
- [Template:Web frameworks](https://en.wikipedia.org/wiki/Template:Web_frameworks)
- [Template talk:Python web frameworks](https://en.wikipedia.org/wiki/Template_talk:Python_web_frameworks)
- [Template talk:Web frameworks](https://en.wikipedia.org/wiki/Template_talk:Web_frameworks)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles with self-published sources from April 2024](https://en.wikipedia.org/wiki/Category:Articles_with_self-published_sources_from_April_2024)
- [Category:Articles with unsourced statements from February 2007](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_February_2007)
- [Category:Python (programming language) web frameworks](https://en.wikipedia.org/wiki/Category:Python_(programming_language)_web_frameworks)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:59:08.792486+00:00_