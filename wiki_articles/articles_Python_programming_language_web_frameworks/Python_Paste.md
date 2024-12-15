# Python Paste

## Article Metadata

- **Last Updated:** 2024-12-15T03:43:30.642344+00:00
- **Original Article:** [Python Paste](https://en.wikipedia.org/wiki/Python_Paste)
- **Language:** en
- **Page ID:** 10720945

## Summary

Python Paste, often simply called paste, is a set of utilities for web development in Python.  Paste has been described as "a framework for web frameworks".
The Python Paste package contains Python modules that help in implementing WSGI middleware.
The package includes a WSGI wrapper for CGI applications. It also includes a simple webserver that can produce WSGI requests.

## Categories

- Category:All articles needing additional references
- Category:All articles with topics of unclear notability
- Category:Articles needing additional references from December 2017
- Category:Articles with multiple maintenance issues
- Category:Articles with short description
- Category:Articles with topics of unclear notability from May 2021
- Category:Official website missing URL
- Category:Products articles with topics of unclear notability
- Category:Python (programming language) web frameworks
- Category:Short description is different from Wikidata

## Table of Contents

- WSGI middleware
- Subcomponents of Paste
- See also
- References

## Content

Python Paste, often simply called paste, is a set of utilities for web development in Python.  Paste has been described as "a framework for web frameworks".
The Python Paste package contains Python modules that help in implementing WSGI middleware.
The package includes a WSGI wrapper for CGI applications. It also includes a simple webserver that can produce WSGI requests.

WSGI middleware
The WSGI standard is an interface that allows applications to use Python code to handle HTTP requests. A WSGI application is passed a Python representation of an HTTP request by an application, and returns content which will normally eventually be rendered by a web browser. A common use for this is when a web server serves content created by Python code.
There are, however, other uses: WSGI middleware is Python code that receives a WSGI request and then performs logic based upon this request, before passing the request on to a WSGI application or more WSGI middleware. WSGI middleware appears to an application as a server, and to the server as an application. This is analogous to the function of pipes on Unix systems. Functionality provided by WSGI middleware may include authentication, logging, URL redirection, creation of sessions, and compression.
Paste helps in developing such WSGI middleware systems. For example, it is used in the Pylons web application framework.

Subcomponents of Paste
Paste has been a long-running open source project, dating from at least 2005. As it has grown, it has unbundled several other utilities from the Paste core. These utilities are part of the Paste project, but form their own packages and have their own version numbers. They include:

Paste Deploy is a system for finding and configuring WSGI applications and servers.
Paste Script, ScriptType, INITools, Tempita, WaitForIt, WPHP, WSGIFilter, and WSGIProxy are other notable bundles.
WebTest
WebOb is a wrapper around the WSGI environment.
WebTest and WebOb have migrated and are now part of the Pylons project.

See also
TurboGears
Pylons project
Smalltalk Seaside
Java servlet
Internet Server Application Programming Interface (ISAPI)
FastCGI
Apache Thrift (from Facebook and Evernote teams)
Server-side JavaScript
PHP
Web framework

References


== External links ==

## Related Articles

### Internal Links

- [AOLserver](https://en.wikipedia.org/wiki/AOLserver)
- [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server)
- [Apache Thrift](https://en.wikipedia.org/wiki/Apache_Thrift)
- [Apache Tomcat](https://en.wikipedia.org/wiki/Apache_Tomcat)
- [Boa (web server)](https://en.wikipedia.org/wiki/Boa_(web_server))
- [CERN httpd](https://en.wikipedia.org/wiki/CERN_httpd)
- [Caddy (web server)](https://en.wikipedia.org/wiki/Caddy_(web_server))
- [Caudium (web server)](https://en.wikipedia.org/wiki/Caudium_(web_server))
- [Cherokee (web server)](https://en.wikipedia.org/wiki/Cherokee_(web_server))
- [CherryPy](https://en.wikipedia.org/wiki/CherryPy)
- [Common Gateway Interface](https://en.wikipedia.org/wiki/Common_Gateway_Interface)
- [Comparison of server-side web frameworks](https://en.wikipedia.org/wiki/Comparison_of_server-side_web_frameworks)
- [Comparison of web server software](https://en.wikipedia.org/wiki/Comparison_of_web_server_software)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [CubicWeb](https://en.wikipedia.org/wiki/CubicWeb)
- [Django (web framework)](https://en.wikipedia.org/wiki/Django_(web_framework))
- [FastAPI](https://en.wikipedia.org/wiki/FastAPI)
- [FastCGI](https://en.wikipedia.org/wiki/FastCGI)
- [Flask (web framework)](https://en.wikipedia.org/wiki/Flask_(web_framework))
- [GlassFish](https://en.wikipedia.org/wiki/GlassFish)
- [Grok (web framework)](https://en.wikipedia.org/wiki/Grok_(web_framework))
- [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn)
- [H2O (web server)](https://en.wikipedia.org/wiki/H2O_(web_server))
- [Hiawatha (web server)](https://en.wikipedia.org/wiki/Hiawatha_(web_server))
- [IBM WebSphere Application Server](https://en.wikipedia.org/wiki/IBM_WebSphere_Application_Server)
- [Internet Information Services](https://en.wikipedia.org/wiki/Internet_Information_Services)
- [Internet Server Application Programming Interface](https://en.wikipedia.org/wiki/Internet_Server_Application_Programming_Interface)
- [JEUS](https://en.wikipedia.org/wiki/JEUS)
- [Jakarta Servlet](https://en.wikipedia.org/wiki/Jakarta_Servlet)
- [Jetty (web server)](https://en.wikipedia.org/wiki/Jetty_(web_server))
- [Lighttpd](https://en.wikipedia.org/wiki/Lighttpd)
- [LiteSpeed Web Server](https://en.wikipedia.org/wiki/LiteSpeed_Web_Server)
- [MIT License](https://en.wikipedia.org/wiki/MIT_License)
- [Mongoose (web server)](https://en.wikipedia.org/wiki/Mongoose_(web_server))
- [Mongrel2](https://en.wikipedia.org/wiki/Mongrel2)
- [Mongrel (web server)](https://en.wikipedia.org/wiki/Mongrel_(web_server))
- [Monkey HTTP Server](https://en.wikipedia.org/wiki/Monkey_HTTP_Server)
- [NCSA HTTPd](https://en.wikipedia.org/wiki/NCSA_HTTPd)
- [NaviServer](https://en.wikipedia.org/wiki/NaviServer)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Nginx](https://en.wikipedia.org/wiki/Nginx)
- [OpenResty](https://en.wikipedia.org/wiki/OpenResty)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Oracle WebLogic Server](https://en.wikipedia.org/wiki/Oracle_WebLogic_Server)
- [Oracle iPlanet Web Server](https://en.wikipedia.org/wiki/Oracle_iPlanet_Web_Server)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [POCO C++ Libraries](https://en.wikipedia.org/wiki/POCO_C%2B%2B_Libraries)
- [Phusion Passenger](https://en.wikipedia.org/wiki/Phusion_Passenger)
- [Pipeline (Unix)](https://en.wikipedia.org/wiki/Pipeline_(Unix))
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Puma (web server)](https://en.wikipedia.org/wiki/Puma_(web_server))
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Pylons project](https://en.wikipedia.org/wiki/Pylons_project)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quixote (web framework)](https://en.wikipedia.org/wiki/Quixote_(web_framework))
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Resin (software)](https://en.wikipedia.org/wiki/Resin_(software))
- [Roxen (web server)](https://en.wikipedia.org/wiki/Roxen_(web_server))
- [SAP NetWeaver Application Server](https://en.wikipedia.org/wiki/SAP_NetWeaver_Application_Server)
- [Seaside (software)](https://en.wikipedia.org/wiki/Seaside_(software))
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Session (computer science)](https://en.wikipedia.org/wiki/Session_(computer_science))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [TACTIC (web framework)](https://en.wikipedia.org/wiki/TACTIC_(web_framework))
- [Thttpd](https://en.wikipedia.org/wiki/Thttpd)
- [Tornado (web server)](https://en.wikipedia.org/wiki/Tornado_(web_server))
- [Apache Traffic Server](https://en.wikipedia.org/wiki/Apache_Traffic_Server)
- [TurboGears](https://en.wikipedia.org/wiki/TurboGears)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [URL redirection](https://en.wikipedia.org/wiki/URL_redirection)
- [Utility software](https://en.wikipedia.org/wiki/Utility_software)
- [WEBrick](https://en.wikipedia.org/wiki/WEBrick)
- [Web2py](https://en.wikipedia.org/wiki/Web2py)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [Web development](https://en.wikipedia.org/wiki/Web_development)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [Web server](https://en.wikipedia.org/wiki/Web_server)
- [WildFly](https://en.wikipedia.org/wiki/WildFly)
- [Xitami](https://en.wikipedia.org/wiki/Xitami)
- [Yaws (web server)](https://en.wikipedia.org/wiki/Yaws_(web_server))
- [Zeus Web Server](https://en.wikipedia.org/wiki/Zeus_Web_Server)
- [Zope](https://en.wikipedia.org/wiki/Zope)
- [Talk:Python Paste](https://en.wikipedia.org/wiki/Talk:Python_Paste)
- [Wikipedia:Deletion policy](https://en.wikipedia.org/wiki/Wikipedia:Deletion_policy)
- [Wikipedia:Independent sources](https://en.wikipedia.org/wiki/Wikipedia:Independent_sources)
- [Wikipedia:Merging](https://en.wikipedia.org/wiki/Wikipedia:Merging)
- [Wikipedia:Notability (organizations and companies)](https://en.wikipedia.org/wiki/Wikipedia:Notability_(organizations_and_companies))
- [Wikipedia:Redirect](https://en.wikipedia.org/wiki/Wikipedia:Redirect)
- [Wikipedia:Reliable sources](https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Python web frameworks](https://en.wikipedia.org/wiki/Template:Python_web_frameworks)
- [Template:Web server software](https://en.wikipedia.org/wiki/Template:Web_server_software)
- [Template talk:Python web frameworks](https://en.wikipedia.org/wiki/Template_talk:Python_web_frameworks)
- [Template talk:Web server software](https://en.wikipedia.org/wiki/Template_talk:Web_server_software)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from December 2017](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_December_2017)
- [Category:Articles with topics of unclear notability from May 2021](https://en.wikipedia.org/wiki/Category:Articles_with_topics_of_unclear_notability_from_May_2021)
- [Category:Python (programming language) web frameworks](https://en.wikipedia.org/wiki/Category:Python_(programming_language)_web_frameworks)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:43:30.642344+00:00_