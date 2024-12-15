# Flask (web framework)

## Metadata
- **Last Updated:** 2024-12-06 05:58:06 UTC
- **Original Article:** [Flask (web framework)](https://en.wikipedia.org/wiki/Flask_(web_framework))
- **Language:** en
- **Page ID:** 29040606

## Summary
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools.
Applications that use the Flask framework include Pinterest and LinkedIn.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 21:04:25 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 3378 bytes
- **Word Count:** 499 words
