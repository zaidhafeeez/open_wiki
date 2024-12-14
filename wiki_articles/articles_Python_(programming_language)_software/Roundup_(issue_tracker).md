# Roundup (issue tracker)

## Article Metadata

- **Last Updated:** 2024-12-14T19:56:44.205730+00:00
- **Original Article:** [Roundup (issue tracker)](https://en.wikipedia.org/wiki/Roundup_(issue_tracker))
- **Language:** en
- **Page ID:** 10567064

## Summary

Roundup is an open-source issue or bug tracking system featuring a command-line, web and e-mail interface. It is written in Python and designed to be highly customizable.

## Categories

- Category:Articles with short description
- Category:Bug and issue tracking software
- Category:Free project management software
- Category:Free software programmed in Python
- Category:Help desk software
- Category:Python (programming language) software
- Category:Short description is different from Wikidata
- Category:Software using the MIT license
- Category:Web applications

## Table of Contents

- History
- Features
- Concepts
- See also
- References
- External links

## Content

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

## Related Articles

### Internal Links

- [Apache Allura](https://en.wikipedia.org/wiki/Apache_Allura)
- [Trac](https://en.wikipedia.org/wiki/Trac)
- [Assembla](https://en.wikipedia.org/wiki/Assembla)
- [Automation](https://en.wikipedia.org/wiki/Automation)
- [GitKraken](https://en.wikipedia.org/wiki/GitKraken)
- [Azure DevOps Server](https://en.wikipedia.org/wiki/Azure_DevOps_Server)
- [Backup](https://en.wikipedia.org/wiki/Backup)
- [Bitbucket](https://en.wikipedia.org/wiki/Bitbucket)
- [Bug tracking system](https://en.wikipedia.org/wiki/Bug_tracking_system)
- [Bugzilla](https://en.wikipedia.org/wiki/Bugzilla)
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [CodePlex](https://en.wikipedia.org/wiki/CodePlex)
- [Codeberg](https://en.wikipedia.org/wiki/Codeberg)
- [Common Gateway Interface](https://en.wikipedia.org/wiki/Common_Gateway_Interface)
- [Comparison of issue-tracking systems](https://en.wikipedia.org/wiki/Comparison_of_issue-tracking_systems)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Daemon (computing)](https://en.wikipedia.org/wiki/Daemon_(computing))
- [Database](https://en.wikipedia.org/wiki/Database)
- [Database abstraction layer](https://en.wikipedia.org/wiki/Database_abstraction_layer)
- [Debbugs](https://en.wikipedia.org/wiki/Debbugs)
- [Email](https://en.wikipedia.org/wiki/Email)
- [Fossil (software)](https://en.wikipedia.org/wiki/Fossil_(software))
- [Free software](https://en.wikipedia.org/wiki/Free_software)
- [GNATS](https://en.wikipedia.org/wiki/GNATS)
- [GNU Savannah](https://en.wikipedia.org/wiki/GNU_Savannah)
- [Gateway (telecommunications)](https://en.wikipedia.org/wiki/Gateway_(telecommunications))
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [GitLab](https://en.wikipedia.org/wiki/GitLab)
- [Gitea](https://en.wikipedia.org/wiki/Gitea)
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [Helix ALM](https://en.wikipedia.org/wiki/Helix_ALM)
- [Issue tracking system](https://en.wikipedia.org/wiki/Issue_tracking_system)
- [Jinja (template engine)](https://en.wikipedia.org/wiki/Jinja_(template_engine))
- [Jira (software)](https://en.wikipedia.org/wiki/Jira_(software))
- [Launchpad (website)](https://en.wikipedia.org/wiki/Launchpad_(website))
- [MIT License](https://en.wikipedia.org/wiki/MIT_License)
- [Mailing list](https://en.wikipedia.org/wiki/Mailing_list)
- [Mantis Bug Tracker](https://en.wikipedia.org/wiki/Mantis_Bug_Tracker)
- [Visual Studio](https://en.wikipedia.org/wiki/Visual_Studio)
- [MySQL](https://en.wikipedia.org/wiki/MySQL)
- [OSDN](https://en.wikipedia.org/wiki/OSDN)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Open-core model](https://en.wikipedia.org/wiki/Open-core_model)
- [Open source](https://en.wikipedia.org/wiki/Open_source)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Phabricator](https://en.wikipedia.org/wiki/Phabricator)
- [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)
- [Process (computing)](https://en.wikipedia.org/wiki/Process_(computing))
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Proprietary software](https://en.wikipedia.org/wiki/Proprietary_software)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Relational database](https://en.wikipedia.org/wiki/Relational_database)
- [Redmine](https://en.wikipedia.org/wiki/Redmine)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [REST](https://en.wikipedia.org/wiki/REST)
- [Request Tracker](https://en.wikipedia.org/wiki/Request_Tracker)
- [SQLite](https://en.wikipedia.org/wiki/SQLite)
- [Shell script](https://en.wikipedia.org/wiki/Shell_script)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [SourceForge](https://en.wikipedia.org/wiki/SourceForge)
- [Standalone program](https://en.wikipedia.org/wiki/Standalone_program)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Table (database)](https://en.wikipedia.org/wiki/Table_(database))
- [Template Attribute Language](https://en.wikipedia.org/wiki/Template_Attribute_Language)
- [Trac](https://en.wikipedia.org/wiki/Trac)
- [Tuleap](https://en.wikipedia.org/wiki/Tuleap)
- [User interface](https://en.wikipedia.org/wiki/User_interface)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [Web application](https://en.wikipedia.org/wiki/Web_application)
- [XHTML](https://en.wikipedia.org/wiki/XHTML)
- [XML-RPC](https://en.wikipedia.org/wiki/XML-RPC)
- [YouTrack](https://en.wikipedia.org/wiki/YouTrack)
- [Template:Bug tracking systems](https://en.wikipedia.org/wiki/Template:Bug_tracking_systems)
- [Template talk:Bug tracking systems](https://en.wikipedia.org/wiki/Template_talk:Bug_tracking_systems)
- [Category:Bug and issue tracking software](https://en.wikipedia.org/wiki/Category:Bug_and_issue_tracking_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:56:44.205730+00:00_