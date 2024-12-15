# Django (web framework)

## Metadata
- **Last Updated:** 2024-12-03 06:58:12 UTC
- **Original Article:** [Django (web framework)](https://en.wikipedia.org/wiki/Django_(web_framework))
- **Language:** en
- **Page ID:** 2247376

## Summary
Django ( JANG-goh; sometimes stylized as django) is a free and open-source, Python-based web framework that runs on a web server. It follows the model–template–views (MTV) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501(c)(3) non-profit.
Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself. Python is used throughout, even for settings, files, and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models.
Some well-known sites that use Django include Instagram, Mozilla, Disqus, Bitbucket, Nextdoor, and Clubhouse.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 21:09:26 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 8483 bytes
- **Word Count:** 1292 words
