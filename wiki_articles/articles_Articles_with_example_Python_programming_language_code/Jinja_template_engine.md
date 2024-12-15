# Jinja (template engine)

## Metadata
- **Last Updated:** 2024-12-03 07:01:54 UTC
- **Original Article:** [Jinja (template engine)](https://en.wikipedia.org/wiki/Jinja_(template_engine))
- **Language:** en
- **Page ID:** 4218966

## Summary
Jinja is a web template engine for the Python programming language. It was created by Armin Ronacher and is licensed under a BSD License. Jinja is similar to the Django template engine, but provides Python-like expressions while ensuring that the templates are evaluated in a sandbox. It is a text-based template language and thus can be used to generate any markup as well as source code.
The Jinja template engine allows customization of tags, filters (for formatting or transforming values), tests (for evaluating conditions), and globals.  Also, unlike the Django template engine, Jinja allows the template designer to call functions with arguments on objects.
Jinja is Flask's default template engine  and it is also used by Ansible, Trac, and Salt. It is also used to make SQL macros, for example for use with dbt.

## Categories
This article belongs to the following categories:

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Free software programmed in Python
- Category:Free system software
- Category:Python (programming language) libraries
- Category:Python (programming language) software
- Category:Short description matches Wikidata
- Category:Software using the BSD license
- Category:Template engines

## Table of Contents

- Features
- Syntax
- Example
- References
- External links

## Content

Jinja is a web template engine for the Python programming language. It was created by Armin Ronacher and is licensed under a BSD License. Jinja is similar to the Django template engine, but provides Python-like expressions while ensuring that the templates are evaluated in a sandbox. It is a text-based template language and thus can be used to generate any markup as well as source code.
The Jinja template engine allows customization of tags, filters (for formatting or transforming values), tests (for evaluating conditions), and globals.  Also, unlike the Django template engine, Jinja allows the template designer to call functions with arguments on objects.
Jinja is Flask's default template engine  and it is also used by Ansible, Trac, and Salt. It is also used to make SQL macros, for example for use with dbt.

Features
Some of the features of Jinja are:

sandboxed execution
automatic HTML escaping to prevent cross-site scripting (XSS) attacks
template inheritance
compiles down to the optimal Python code just-in-time
optional ahead-of-time template compilation
easy to debug (for example, line numbers of exceptions directly point to the correct line in the template)
configurable syntax
Jinja, like Smarty, also ships with an easy-to-use filter system similar to the Unix pipeline.

Syntax
The syntax for printing output in Jinja is using the double curly braces, for example {{ Hello, World! }}.
Statements which set variables in jinja or those which do not have an output can be wrapped within {% and %}, using the set keyword. For example {% set foo = 42 %} sets a variable called foo with a value of 42.
Similar to above, comments in jinja can be written using a number sign (#) instead of a percentage (%), for example, {# helpful comment #}.
The syntax for creating a filter in Jinja is a vertical bar (|), for example {{ variable|filter }}. A variable can have multiple filters, for example {{ variable|filter|filter }}).
The syntax for creating a test in Jinja is the keyword is as well as the conditions for evaluating the validity of a test, such as for example {% if variable is divisibleby 10 %}do something{% endif %}).
For loops can be used to iterate over sequences, while retaining their object properties. The following example demonstrates iterating over a list of users with username and password fields.

Although break and continue are not allowed inside loops, sequences can be filtered.

Example
Here is a small example of a template file example.html.jinja:

and templating code:
This produces the HTML string:

Note the minus sign (-) after the tag  {%:  If you add a minus sign (-) to the start or end of a block (e.g. a For tag), a comment, or a variable expression, the whitespaces before or after that block will be removed.

References
External links
Official website

## Archive Info
- **Archived on:** 2024-12-15 20:38:22 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2813 bytes
- **Word Count:** 467 words
