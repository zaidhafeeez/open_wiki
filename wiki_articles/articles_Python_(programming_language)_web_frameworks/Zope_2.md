# Zope

## Article Metadata

- **Last Updated:** 2024-12-14T20:01:12.123024+00:00
- **Original Article:** [Zope](https://en.wikipedia.org/wiki/Zope)
- **Language:** en
- **Page ID:** 34472

## Summary

Zope is a family of free and open-source web application servers written in Python, and their associated online community. Zope stands for "Z Object Publishing Environment", and was the first system using the now common object publishing methodology for the Web. Zope has been called a Python killer app, an application that helped put Python in the spotlight.
Over the last few years, the Zope community has spawned several additional web frameworks with disparate aims and principles, but sharing p

## Categories

- Category:1995 establishments in Virginia
- Category:All articles with unsourced statements
- Category:Articles with short description
- Category:Articles with unsourced statements from August 2011
- Category:Cross-platform free software
- Category:Free content management systems
- Category:Free software programmed in Python
- Category:Python (programming language) web frameworks
- Category:Short description is different from Wikidata
- Category:Software companies based in Virginia
- Category:Software companies established in 1995
- Category:Software companies of the United States
- Category:Web development software
- Category:Web server software for Linux
- Category:Zope

## Table of Contents

- History
- Zope Foundation
- Zope versions
- Zope page templates
- Notable software using Zope
- See also
- References
- External links

## Content

Zope is a family of free and open-source web application servers written in Python, and their associated online community. Zope stands for "Z Object Publishing Environment", and was the first system using the now common object publishing methodology for the Web. Zope has been called a Python killer app, an application that helped put Python in the spotlight.
Over the last few years, the Zope community has spawned several additional web frameworks with disparate aims and principles, but sharing philosophy, people, and source code. Zope 2 is still the most widespread of these frameworks, largely thanks to the Plone content management system, which runs on Zope 2. BlueBream (earlier called Zope 3) is less widespread but underlies several large sites, including Launchpad. Grok was started as a more programmer-friendly framework, "Zope 3 for cavemen", and in 2009 Pyramid gained popularity in the Zope community as a minimalistic framework based on Zope principles.

History
The Zope Corporation was formed in 1995 in Fredericksburg, Virginia under the name Digital Creations, as a joint venture with InfiNet (a joint newspaper chain venture). The company developed a classified advertisement engine for the Internet. In 1997, the company became independently owned and private. The company's software engineers are led by CTO Jim Fulton. PythonLabs, creators of Python, became part of the company in 2000 (Python founder Guido van Rossum left Zope Corp in 2003).
What is now known as Zope 2 began with the merging of three separate software products – Bobo, Document Template, and BoboPOS – into the Principia application server. At the behest of its largest investor, Opticality Ventures, Principia was re-released as free software under the name Zope in 1998. Bobo, and therefore Zope, was the first Web object publishing solution.
In November 2004, Zope 3 was released. Zope 3 is a complete rewrite that preserves only the original ZODB object database. It is directly intended for enterprise Web application development using the newest development paradigms. Zope 3 is, however, not compatible with Zope 2, so Zope 2 applications do not run on Zope 3. It was originally intended to introduce a backwards-compatibility layer so that Zope 2 software would run on Zope 3. Instead a module known as Five introduced the new Zope 3 paradigms into Zope 2, although full compatibility isn't possible that way either.
The existence of two incompatible Web frameworks called Zope has caused a lot of confusion. In response, in January 2010, Zope 3 was renamed "BlueBream". "Zope" and "blue bream" are names of a kind of fish, Ballerus ballerus.

Zope Foundation
The Zope Foundation is an organization that promotes the development of the Zope platform by supporting the community that develops and maintains the relevant software components. The community includes both open source software, documentation and web infrastructure contributors, as well as business and organization consumers of the software platform. It manages the zope.org websites, an infrastructure for open source collaboration.

Zope versions
Zope 2
A Zope website is usually composed of objects in a Zope Object Database, not files on a file system, as is usual with most web servers. This allows users to harness the advantages of object technologies, such as encapsulation. Zope maps URLs to objects using the containment hierarchy of such objects; methods are considered to be contained in their objects as well. Data can be stored in other databases as well, or on the file system, but ZODB is the most common solution.
Zope provides two mechanisms for HTML templating: Document Template Markup Language (DTML) and Zope Page Templates (ZPT). DTML is a tag-based language that allows implementation of simple scripting in the templates. DTML has provisions for variable inclusion, conditions, and loops. However, DTML can be problematic: DTML tags interspersed with HTML form non-valid HTML documents, and its use requires care when including logic into templates, to retain code readability. The use of DTML is discouraged by many leading Zope developers. ZPT is a technology that addresses the shortcomings of DTML. ZPT templates can be either well-formed XML documents or HTML documents, in which all special markup is presented as attributes in the TAL (Template Attribute Language) namespace. ZPT offers a very limited set of tools for conditional inclusion and repetition of XML elements. Consequently, the templates are usually quite simple, with most logic implemented in Python code. One significant advantage of ZPT templates is that they can be edited in most graphical HTML editors. ZPT also offers direct support for internationalization.
Zope 2 underlies the Plone content management system, as well as the ERP5 open source enterprise resource planning system.

BlueBream
BlueBream is a rewrite by the Zope developers of the Zope 2 web application server. It was created under the name "Zope 3", but the existence of two incompatible frameworks with the same name caused much confusion, and Zope 3 was renamed "BlueBream" in January 2010. BlueBream is distributed under the terms of the Zope Public License and is thus free software.
Zope 2 has proven itself as a useful framework for Web applications development, but its use revealed some shortcomings. To name a few, creating Zope 2 products involves copying a lot of boilerplate code – "magic" code – that just has to be there, and the built-in management interface is difficult to modify or replace. Zope 3 was a rewrite of the software that attempts to address these shortcomings while retaining the advantages of Zope that led to its popularity. BlueBream is based on a component architecture that makes it easy to mix software components of various origins written in Python. Although originally intended as a replacement for Zope 2, the Zope Component Architecture has instead been backported to Zope 2, starting with Zope 2.8. Many Zope platforms such as Plone are going through the same type of piece-by-piece rewriting. The first production release of the new software, Zope X3 3.0.0, was released on November 6, 2004.

History
The Zope 3 project started in February 2001 as an effort to develop a new version of Zope as an almost complete rewrite, with the goal to retain the successful features of Zope 2 while trying to fix some of its shortcomings. The goal was to create a more developer-friendly and flexible platform for programming web applications than Zope 2 is. The project began with the development of a component architecture, which allows the structuring of code into small, composable units with introspectable interfaces. The interfaces are supported by an interface package in order to provide the functionality of explicitly declared interfaces to the Python language. The first production release of the software, Zope X3, was released on November 6, 2004. In January 2010 Zope 3 was renamed BlueBream.

Technology
The goal of the project was to enable programmers to use Zope in order to expose arbitrary Python objects as model objects to the web without the need to make these objects fulfill particular behavior requirements. In Zope 2 there had been many behavior requirements to allow objects to participate in the framework, which resulted in a large amount of mixin base classes and special attributes. BlueBream uses a model/view architecture, separating the presentation code from the problem domain code. Views and models are linked together by the component architecture.
The libraries underlying BlueBream have been evolving into a collection of useful libraries for web application development rather than a single, monolithic application server. BlueBream includes separate packages for interfaces, component architecture, HTTP server, publisher, Zope Object Database (ZODB), Zope Page Templates, I18N, security policy, and so on. The component architecture is used to glue these together. The component architecture is configured using a ZCML (Zope Configuration Markup Language), an XML based configuration file language.
The Zope 3 project pioneered the practice of sprints for open source software development. Sprints are intensive development sessions when programmers, often from different countries, gather in one room and work together for a couple of days or even several weeks. During the sprints various practices drawn from agile software development are used, such as pair programming and test-driven development. Besides the goal of developing software, sprints are also useful for geographically separated developers to meet in person and attracting new people to the project. They also serve as a way for the participants to learn from each other.
BlueBream is considered a stable framework, used on production projects worldwide, most notably Launchpad.

Zope Toolkit
As a result of the development of Zope 3 / BlueBream, there are now many independent Python packages used and developed as a part of BlueBream, and although many of these are usable outside of BlueBream, many are not. The Zope Toolkit (ZTK) project was started to clarify which packages were usable outside BlueBream, and to improve the re-usability of the packages. Thus the Zope Toolkit is a base for the Zope frameworks. Zope 2.12 is the first release of a web framework that builds on Zope Toolkit, and Grok and BlueBream were set to have releases based on the ZTK during 2010.

Grok
In 2006 the Grok project was started by a number of Zope 3 developers who wanted to make Zope 3 technology more agile in use and more accessible to newcomers. Grok has since then seen regular releases and its core technology (Martian, grokcore.component) is also finding uptake in other Zope 3 and Zope 2 based projects.

Zope 4
In late 2017, development began on Zope 4. Zope 4 is a successor to Zope 2.13, making many changes that are not backwards compatible with Zope 2.

Zope 5
Zope 5 was released in 2020.

Zope page templates
As mentioned previously, Zope page templates are themselves XHTML documents, which means they can be viewed and edited using normal HTML editors or XHTML compliant tools (a big advantage compared to other template languages used for Web applications). Templates can also be checked for XHTML compliance so you can be fairly confident that they will automatically expand into proper XHTML.
However, these page templates are not meant to be rendered as is. Instead they are marked up with additional elements and attributes in special XML namespaces (see below). This additional information is used to describe how the page template should ultimately be processed.
Here are some basic examples. To conditionally include a particular element, like a div element, simply add the tal:condition attribute to the element as follows:

To control what appears inside an element, use the tal:content attribute like this:

Finally, to introduce or replace values of attributes use the tal:attributes attribute as below. You can use Python to alter the href at runtime.

This is a very cursory explanation of Zope Page Templates. The behavior of Zope Page Templates is almost completely described by a template language, fixed on TAL, TALES, and METAL specifications:

Template Attribute Language (TAL),
Template Attribute Language Expression Syntax (TALES),
Macro Expansion Template Attribute Language (METAL).

Notable software using Zope
SchoolTool is an open source student information system that uses Zope.
Plone is an open source content management system that uses Zope.

See also
Pylons project
Django
web2py
Content management (CM)
Web content management system (WCMS)
Naaya
Twisted

References
External links

Official website

## Related Articles

### Internal Links

- [.NET](https://en.wikipedia.org/wiki/.NET)
- [AIDA/Web](https://en.wikipedia.org/wiki/AIDA/Web)
- [AOLserver](https://en.wikipedia.org/wiki/AOLserver)
- [ASP.NET](https://en.wikipedia.org/wiki/ASP.NET)
- [ASP.NET AJAX](https://en.wikipedia.org/wiki/ASP.NET_AJAX)
- [ASP.NET Core](https://en.wikipedia.org/wiki/ASP.NET_Core)
- [ASP.NET Dynamic Data](https://en.wikipedia.org/wiki/ASP.NET_Dynamic_Data)
- [ASP.NET MVC](https://en.wikipedia.org/wiki/ASP.NET_MVC)
- [ASP.NET Razor](https://en.wikipedia.org/wiki/ASP.NET_Razor)
- [ASP.NET Web Forms](https://en.wikipedia.org/wiki/ASP.NET_Web_Forms)
- [Ballerus ballerus](https://en.wikipedia.org/wiki/Ballerus_ballerus)
- [Adobe ColdFusion](https://en.wikipedia.org/wiki/Adobe_ColdFusion)
- [Agile software development](https://en.wikipedia.org/wiki/Agile_software_development)
- [AngularJS](https://en.wikipedia.org/wiki/AngularJS)
- [Angular (web framework)](https://en.wikipedia.org/wiki/Angular_(web_framework))
- [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server)
- [Apache Sling](https://en.wikipedia.org/wiki/Apache_Sling)
- [Apache Struts](https://en.wikipedia.org/wiki/Apache_Struts)
- [Apache Tapestry](https://en.wikipedia.org/wiki/Apache_Tapestry)
- [Apache Tomcat](https://en.wikipedia.org/wiki/Apache_Tomcat)
- [Apache Wicket](https://en.wikipedia.org/wiki/Apache_Wicket)
- [AppFuse](https://en.wikipedia.org/wiki/AppFuse)
- [Application server](https://en.wikipedia.org/wiki/Application_server)
- [Byte (magazine)](https://en.wikipedia.org/wiki/Byte_(magazine))
- [Backbone.js](https://en.wikipedia.org/wiki/Backbone.js)
- [Backward compatibility](https://en.wikipedia.org/wiki/Backward_compatibility)
- [Ballerus ballerus](https://en.wikipedia.org/wiki/Ballerus_ballerus)
- [Base One Foundation Component Library](https://en.wikipedia.org/wiki/Base_One_Foundation_Component_Library)
- [Blazor](https://en.wikipedia.org/wiki/Blazor)
- [Boa (web server)](https://en.wikipedia.org/wiki/Boa_(web_server))
- [Boilerplate code](https://en.wikipedia.org/wiki/Boilerplate_code)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CERN httpd](https://en.wikipedia.org/wiki/CERN_httpd)
- [CL-HTTP](https://en.wikipedia.org/wiki/CL-HTTP)
- [Caddy (web server)](https://en.wikipedia.org/wiki/Caddy_(web_server))
- [CakePHP](https://en.wikipedia.org/wiki/CakePHP)
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [Caudium (web server)](https://en.wikipedia.org/wiki/Caudium_(web_server))
- [Cherokee (web server)](https://en.wikipedia.org/wiki/Cherokee_(web_server))
- [CherryPy](https://en.wikipedia.org/wiki/CherryPy)
- [CodeIgniter](https://en.wikipedia.org/wiki/CodeIgniter)
- [Hackathon](https://en.wikipedia.org/wiki/Hackathon)
- [ColdBox Platform](https://en.wikipedia.org/wiki/ColdBox_Platform)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Comparison of server-side web frameworks](https://en.wikipedia.org/wiki/Comparison_of_server-side_web_frameworks)
- [Comparison of web server software](https://en.wikipedia.org/wiki/Comparison_of_web_server_software)
- [Component-based software engineering](https://en.wikipedia.org/wiki/Component-based_software_engineering)
- [Content management](https://en.wikipedia.org/wiki/Content_management)
- [Content management system](https://en.wikipedia.org/wiki/Content_management_system)
- [CppCMS](https://en.wikipedia.org/wiki/CppCMS)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [CubicWeb](https://en.wikipedia.org/wiki/CubicWeb)
- [Dancer (software)](https://en.wikipedia.org/wiki/Dancer_(software))
- [Django (web framework)](https://en.wikipedia.org/wiki/Django_(web_framework))
- [Dojo Toolkit](https://en.wikipedia.org/wiki/Dojo_Toolkit)
- [DNN (software)](https://en.wikipedia.org/wiki/DNN_(software))
- [Drogon (software)](https://en.wikipedia.org/wiki/Drogon_(software))
- [Drupal](https://en.wikipedia.org/wiki/Drupal)
- [ERP5](https://en.wikipedia.org/wiki/ERP5)
- [EZ Publish](https://en.wikipedia.org/wiki/EZ_Publish)
- [Elixir (programming language)](https://en.wikipedia.org/wiki/Elixir_(programming_language))
- [Ember.js](https://en.wikipedia.org/wiki/Ember.js)
- [Enterprise resource planning](https://en.wikipedia.org/wiki/Enterprise_resource_planning)
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Express.js](https://en.wikipedia.org/wiki/Express.js)
- [Ext JS](https://en.wikipedia.org/wiki/Ext_JS)
- [FastAPI](https://en.wikipedia.org/wiki/FastAPI)
- [Fastify](https://en.wikipedia.org/wiki/Fastify)
- [Fat-Free Framework](https://en.wikipedia.org/wiki/Fat-Free_Framework)
- [File system](https://en.wikipedia.org/wiki/File_system)
- [Flask (web framework)](https://en.wikipedia.org/wiki/Flask_(web_framework))
- [Fredericksburg, Virginia](https://en.wikipedia.org/wiki/Fredericksburg,_Virginia)
- [Free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software)
- [Free software](https://en.wikipedia.org/wiki/Free_software)
- [FuelPHP](https://en.wikipedia.org/wiki/FuelPHP)
- [GlassFish](https://en.wikipedia.org/wiki/GlassFish)
- [Google Closure Tools](https://en.wikipedia.org/wiki/Google_Closure_Tools)
- [Google Web Toolkit](https://en.wikipedia.org/wiki/Google_Web_Toolkit)
- [Grails (framework)](https://en.wikipedia.org/wiki/Grails_(framework))
- [Grav (CMS)](https://en.wikipedia.org/wiki/Grav_(CMS))
- [Grok (web framework)](https://en.wikipedia.org/wiki/Grok_(web_framework))
- [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
- [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn)
- [Gyroscope (software)](https://en.wikipedia.org/wiki/Gyroscope_(software))
- [H2O (web server)](https://en.wikipedia.org/wiki/H2O_(web_server))
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Hiawatha (web server)](https://en.wikipedia.org/wiki/Hiawatha_(web_server))
- [Horde (software)](https://en.wikipedia.org/wiki/Horde_(software))
- [Htmx](https://en.wikipedia.org/wiki/Htmx)
- [Internationalization and localization](https://en.wikipedia.org/wiki/Internationalization_and_localization)
- [IBM WebSphere Application Server](https://en.wikipedia.org/wiki/IBM_WebSphere_Application_Server)
- [ICEfaces](https://en.wikipedia.org/wiki/ICEfaces)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Information hiding](https://en.wikipedia.org/wiki/Information_hiding)
- [Internationalization and localization](https://en.wikipedia.org/wiki/Internationalization_and_localization)
- [Internet Information Services](https://en.wikipedia.org/wiki/Internet_Information_Services)
- [JBoss Seam](https://en.wikipedia.org/wiki/JBoss_Seam)
- [JEUS](https://en.wikipedia.org/wiki/JEUS)
- [JHipster](https://en.wikipedia.org/wiki/JHipster)
- [JQuery](https://en.wikipedia.org/wiki/JQuery)
- [JWt (Java web toolkit)](https://en.wikipedia.org/wiki/JWt_(Java_web_toolkit))
- [Jakarta Faces](https://en.wikipedia.org/wiki/Jakarta_Faces)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (software platform)](https://en.wikipedia.org/wiki/Java_(software_platform))
- [Jetty (web server)](https://en.wikipedia.org/wiki/Jetty_(web_server))
- [Joomla](https://en.wikipedia.org/wiki/Joomla)
- [Killer application](https://en.wikipedia.org/wiki/Killer_application)
- [Knockout (web framework)](https://en.wikipedia.org/wiki/Knockout_(web_framework))
- [Laminas](https://en.wikipedia.org/wiki/Laminas)
- [Laravel](https://en.wikipedia.org/wiki/Laravel)
- [Launchpad (website)](https://en.wikipedia.org/wiki/Launchpad_(website))
- [Li3 (software)](https://en.wikipedia.org/wiki/Li3_(software))
- [Lift (web framework)](https://en.wikipedia.org/wiki/Lift_(web_framework))
- [Lighttpd](https://en.wikipedia.org/wiki/Lighttpd)
- [LiteSpeed Web Server](https://en.wikipedia.org/wiki/LiteSpeed_Web_Server)
- [Template Attribute Language](https://en.wikipedia.org/wiki/Template_Attribute_Language)
- [MODX](https://en.wikipedia.org/wiki/MODX)
- [Catalyst (software)](https://en.wikipedia.org/wiki/Catalyst_(software))
- [Merb](https://en.wikipedia.org/wiki/Merb)
- [Meteor (web framework)](https://en.wikipedia.org/wiki/Meteor_(web_framework))
- [Midgard (software)](https://en.wikipedia.org/wiki/Midgard_(software))
- [Mixin](https://en.wikipedia.org/wiki/Mixin)
- [Mojolicious](https://en.wikipedia.org/wiki/Mojolicious)
- [Mongoose (web server)](https://en.wikipedia.org/wiki/Mongoose_(web_server))
- [Mongrel2](https://en.wikipedia.org/wiki/Mongrel2)
- [Mongrel (web server)](https://en.wikipedia.org/wiki/Mongrel_(web_server))
- [Monkey HTTP Server](https://en.wikipedia.org/wiki/Monkey_HTTP_Server)
- [MonoRail (software)](https://en.wikipedia.org/wiki/MonoRail_(software))
- [MooTools](https://en.wikipedia.org/wiki/MooTools)
- [NCSA HTTPd](https://en.wikipedia.org/wiki/NCSA_HTTPd)
- [Naaya](https://en.wikipedia.org/wiki/Naaya)
- [NaviServer](https://en.wikipedia.org/wiki/NaviServer)
- [Neos Flow](https://en.wikipedia.org/wiki/Neos_Flow)
- [NestJS](https://en.wikipedia.org/wiki/NestJS)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Next.js](https://en.wikipedia.org/wiki/Next.js)
- [Nginx](https://en.wikipedia.org/wiki/Nginx)
- [Node.js](https://en.wikipedia.org/wiki/Node.js)
- [Nonprofit organization](https://en.wikipedia.org/wiki/Nonprofit_organization)
- [Nuxt.js](https://en.wikipedia.org/wiki/Nuxt.js)
- [O'Reilly Media](https://en.wikipedia.org/wiki/O%27Reilly_Media)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [ArsDigita Community System](https://en.wikipedia.org/wiki/ArsDigita_Community_System)
- [OpenResty](https://en.wikipedia.org/wiki/OpenResty)
- [OpenUI5](https://en.wikipedia.org/wiki/OpenUI5)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Oracle Application Express](https://en.wikipedia.org/wiki/Oracle_Application_Express)
- [Oracle WebLogic Server](https://en.wikipedia.org/wiki/Oracle_WebLogic_Server)
- [Oracle iPlanet Web Server](https://en.wikipedia.org/wiki/Oracle_iPlanet_Web_Server)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [PHP-Fusion](https://en.wikipedia.org/wiki/PHP-Fusion)
- [PHP-Nuke](https://en.wikipedia.org/wiki/PHP-Nuke)
- [PL/SQL](https://en.wikipedia.org/wiki/PL/SQL)
- [POCO C++ Libraries](https://en.wikipedia.org/wiki/POCO_C%2B%2B_Libraries)
- [PRADO (framework)](https://en.wikipedia.org/wiki/PRADO_(framework))
- [Padrino (web framework)](https://en.wikipedia.org/wiki/Padrino_(web_framework))
- [Pair programming](https://en.wikipedia.org/wiki/Pair_programming)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Phalcon (framework)](https://en.wikipedia.org/wiki/Phalcon_(framework))
- [Phoenix (web framework)](https://en.wikipedia.org/wiki/Phoenix_(web_framework))
- [Phusion Passenger](https://en.wikipedia.org/wiki/Phusion_Passenger)
- [Play Framework](https://en.wikipedia.org/wiki/Play_Framework)
- [Plone (software)](https://en.wikipedia.org/wiki/Plone_(software))
- [Plone (software)](https://en.wikipedia.org/wiki/Plone_(software))
- [Plone (software)](https://en.wikipedia.org/wiki/Plone_(software))
- [Pop PHP Framework](https://en.wikipedia.org/wiki/Pop_PHP_Framework)
- [ProcessWire](https://en.wikipedia.org/wiki/ProcessWire)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Prototype JavaScript Framework](https://en.wikipedia.org/wiki/Prototype_JavaScript_Framework)
- [Puma (web server)](https://en.wikipedia.org/wiki/Puma_(web_server))
- [Pyjs](https://en.wikipedia.org/wiki/Pyjs)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Paste](https://en.wikipedia.org/wiki/Python_Paste)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Qcodo](https://en.wikipedia.org/wiki/Qcodo)
- [Quixote (web framework)](https://en.wikipedia.org/wiki/Quixote_(web_framework))
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [React (software)](https://en.wikipedia.org/wiki/React_(software))
- [Remix (web framework)](https://en.wikipedia.org/wiki/Remix_(web_framework))
- [Remote Application Platform](https://en.wikipedia.org/wiki/Remote_Application_Platform)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Resin (software)](https://en.wikipedia.org/wiki/Resin_(software))
- [Rewrite (programming)](https://en.wikipedia.org/wiki/Rewrite_(programming))
- [Rocket (web framework)](https://en.wikipedia.org/wiki/Rocket_(web_framework))
- [Roxen (web server)](https://en.wikipedia.org/wiki/Roxen_(web_server))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Ruby on Rails](https://en.wikipedia.org/wiki/Ruby_on_Rails)
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [SAP NetWeaver Application Server](https://en.wikipedia.org/wiki/SAP_NetWeaver_Application_Server)
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scalatra](https://en.wikipedia.org/wiki/Scalatra)
- [SchoolTool](https://en.wikipedia.org/wiki/SchoolTool)
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
- [Student information system](https://en.wikipedia.org/wiki/Student_information_system)
- [Svelte](https://en.wikipedia.org/wiki/Svelte)
- [Symfony](https://en.wikipedia.org/wiki/Symfony)
- [TACTIC (web framework)](https://en.wikipedia.org/wiki/TACTIC_(web_framework))
- [Template Attribute Language](https://en.wikipedia.org/wiki/Template_Attribute_Language)
- [TYPO3](https://en.wikipedia.org/wiki/TYPO3)
- [Markup language](https://en.wikipedia.org/wiki/Markup_language)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Template Attribute Language](https://en.wikipedia.org/wiki/Template_Attribute_Language)
- [Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development)
- [Thttpd](https://en.wikipedia.org/wiki/Thttpd)
- [Tornado (web server)](https://en.wikipedia.org/wiki/Tornado_(web_server))
- [Apache Traffic Server](https://en.wikipedia.org/wiki/Apache_Traffic_Server)
- [TurboGears](https://en.wikipedia.org/wiki/TurboGears)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Umbraco](https://en.wikipedia.org/wiki/Umbraco)
- [URL](https://en.wikipedia.org/wiki/URL)
- [Vaadin](https://en.wikipedia.org/wiki/Vaadin)
- [Vert.x](https://en.wikipedia.org/wiki/Vert.x)
- [Vue.js](https://en.wikipedia.org/wiki/Vue.js)
- [WEBrick](https://en.wikipedia.org/wiki/WEBrick)
- [WaveMaker](https://en.wikipedia.org/wiki/WaveMaker)
- [Web2py](https://en.wikipedia.org/wiki/Web2py)
- [WebGUI](https://en.wikipedia.org/wiki/WebGUI)
- [WebSharper](https://en.wikipedia.org/wiki/WebSharper)
- [Web content management system](https://en.wikipedia.org/wiki/Web_content_management_system)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [Web server](https://en.wikipedia.org/wiki/Web_server)
- [Web template system](https://en.wikipedia.org/wiki/Web_template_system)
- [Website](https://en.wikipedia.org/wiki/Website)
- [WildFly](https://en.wikipedia.org/wiki/WildFly)
- [WordPress](https://en.wikipedia.org/wiki/WordPress)
- [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web)
- [Wt (web toolkit)](https://en.wikipedia.org/wiki/Wt_(web_toolkit))
- [XHTML](https://en.wikipedia.org/wiki/XHTML)
- [XML](https://en.wikipedia.org/wiki/XML)
- [XOOPS](https://en.wikipedia.org/wiki/XOOPS)
- [Xitami](https://en.wikipedia.org/wiki/Xitami)
- [Yaws (web server)](https://en.wikipedia.org/wiki/Yaws_(web_server))
- [Yesod (web framework)](https://en.wikipedia.org/wiki/Yesod_(web_framework))
- [Yii](https://en.wikipedia.org/wiki/Yii)
- [ZK (framework)](https://en.wikipedia.org/wiki/ZK_(framework))
- [Zeus Web Server](https://en.wikipedia.org/wiki/Zeus_Web_Server)
- [Zope Object Database](https://en.wikipedia.org/wiki/Zope_Object_Database)
- [Zope Public License](https://en.wikipedia.org/wiki/Zope_Public_License)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Template:Python web frameworks](https://en.wikipedia.org/wiki/Template:Python_web_frameworks)
- [Template:Web frameworks](https://en.wikipedia.org/wiki/Template:Web_frameworks)
- [Template:Web server software](https://en.wikipedia.org/wiki/Template:Web_server_software)
- [Template talk:Python web frameworks](https://en.wikipedia.org/wiki/Template_talk:Python_web_frameworks)
- [Template talk:Web frameworks](https://en.wikipedia.org/wiki/Template_talk:Web_frameworks)
- [Template talk:Web server software](https://en.wikipedia.org/wiki/Template_talk:Web_server_software)
- [Help:Authority control](https://en.wikipedia.org/wiki/Help:Authority_control)
- [Category:Articles with unsourced statements from August 2011](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_August_2011)
- [Category:Python (programming language) web frameworks](https://en.wikipedia.org/wiki/Category:Python_(programming_language)_web_frameworks)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T20:01:12.123024+00:00_