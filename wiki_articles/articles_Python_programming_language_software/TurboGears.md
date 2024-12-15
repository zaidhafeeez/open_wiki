# TurboGears

## Metadata
- **Last Updated:** 2024-12-15 04:18:50 UTC
- **Original Article:** [TurboGears](https://en.wikipedia.org/wiki/TurboGears)
- **Language:** en
- **Page ID:** 3177599

## Summary
TurboGears is a Python web application framework consisting of several WSGI components such as WebOb, SQLAlchemy, Kajiki template language and Repoze.
TurboGears is designed around the model–view–controller (MVC) architecture, much like Struts or Ruby on Rails, designed to make rapid web application development in Python easier and more maintainable. Since version 2.3 the framework has also been providing a "minimal mode" which enables it to act as a microframework for usage in environments where the whole stack is not required nor wanted.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 20:28:06 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 9127 bytes
- **Word Count:** 1469 words
