---
title: Roundup (issue tracker)
url: https://en.wikipedia.org/wiki/Roundup_(issue_tracker)
language: en
categories: ["Category:Articles with short description", "Category:Bug and issue tracking software", "Category:Free project management software", "Category:Free software programmed in Python", "Category:Help desk software", "Category:Python (programming language) software", "Category:Short description is different from Wikidata", "Category:Software using the MIT license", "Category:Web applications"]
references: 0
last_modified: 2024-12-19T14:02:54Z
---

# Roundup (issue tracker)

## Summary

Roundup is an open-source issue or bug tracking system featuring a command-line, web and e-mail interface. It is written in Python and designed to be highly customizable.

## Full Content

Roundup is an open-source issue or bug tracking system featuring a command-line, web and e-mail interface. It is written in Python and designed to be highly customizable.

History
Roundup was designed by Ka-Ping Yee for the Software Carpentry project and was developed from 2001 to 2016 under the direction of Richard Jones. Since then, it has been developed by the Roundup community. It was the issue tracker for the Python programming language for 17 years before migrating to GitHub. It was once described as "like Bugzilla without the six years of training, or RT without that tedious MySQL rubbish."

Features
The standard configuration of Roundup features:

a web interface for viewing, editing and searching issues
REST and XMLRPC interfaces for remote automation and web applications
a Mail gateway allowing creation and changing of issues
a database abstraction layer, currently supporting (among others) Python's built-in "anydbm" module, PostgreSQL, MySQL and SQLite
issue-specific "nosy lists", used for e-mail notifications and conversation (each issue effectively becoming a mini mailing list) 
an authorization system, based on roles (of users), classes and objects
an interactive shell for backup and restore tasks and for manipulation of objects
Roundup supports several web backends. It can be run standalone, as a background daemon process, as a CGI script or as WSGI application.

Concepts
Roundup is customized by changing the contents of the tracker instance directory:

Database schema
The database schema is defined in a Python file in the tracker instance's root directory; it is
re-read whenever the server is started anew. When changes are found (e.g. new attributes), the tables of the underlying RDBS are altered accordingly.

Page templates
Roundup uses the Template Attribute Language (TAL) to create HTML or XHTML output. Version 1.5.0 adds experimental support for alternative template engines, such as Jinja2.
Templates are named after the classes in database. Roundup automatically chooses template based on class name requested from URL. Some templates are used for several classes, e.g. _generic.index.html, which allows (authorized) users to change the objects of all classes which lack an own index template.
When an "issue123" is requested, this designator is split in the issue class and the id "123". By default an "item" template is chosen: First, an issue.item.html template file is looked for; if it can't be found, _generic.item.html is used as a fallback option. If this is missing equally, an error occurs.

Detectors
Many Roundup functions, including some of the standard functionality, are implemented using so-called detectors, which are located in the "detectors" sub-directory of the tracker instance. They are Python subroutines which have access to the object to change (if already created) and the requested attribute changes.
Detectors are distinguished between auditors and reactors. Auditors are used primarily for several automatic changes (in the standard configuration, the assignedto user is automatically added to the nosy list of the issue), and to refuse un-allowed changes; reactors are executed thereafter and used e.g. for the e-mail notification feature, sending notification mails to all users interested in a certain issue when a comment is added to it.
Detectors are triggered whenever one of the actions

create
set (change of attributes)
retire
restore
is requested. They can be used to create an elaborated custom workflow.

Extensions
The instance subdirectory "extensions" can hold additional files which are needed for extended functionalities which can't (conveniently) be done with TAL; even totally new actions are possible.
Python modules which are used by both detectors and extensions can be put in the "lib" subdirectory

See also
Comparison of issue-tracking systems

References
External links
Official website
