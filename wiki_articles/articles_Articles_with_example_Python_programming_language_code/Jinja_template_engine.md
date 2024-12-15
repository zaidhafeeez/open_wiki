# Jinja (template engine)

## Article Metadata

- **Last Updated:** 2024-12-15T04:31:23.950945+00:00
- **Original Article:** [Jinja (template engine)](https://en.wikipedia.org/wiki/Jinja_(template_engine))
- **Language:** en
- **Page ID:** 4218966

## Summary

Jinja is a web template engine for the Python programming language. It was created by Armin Ronacher and is licensed under a BSD License. Jinja is similar to the Django template engine, but provides Python-like expressions while ensuring that the templates are evaluated in a sandbox. It is a text-based template language and thus can be used to generate any markup as well as source code.
The Jinja template engine allows customization of tags, filters (for formatting or transforming values), tests

## Categories

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

## Related Articles

### Internal Links

- [Ansible (software)](https://en.wikipedia.org/wiki/Ansible_(software))
- [Armin Ronacher](https://en.wikipedia.org/wiki/Armin_Ronacher)
- [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses)
- [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses)
- [Cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting)
- [Data build tool](https://en.wikipedia.org/wiki/Data_build_tool)
- [Django (web framework)](https://en.wikipedia.org/wiki/Django_(web_framework))
- [Filter (software)](https://en.wikipedia.org/wiki/Filter_(software))
- [Flask (web framework)](https://en.wikipedia.org/wiki/Flask_(web_framework))
- [For loop](https://en.wikipedia.org/wiki/For_loop)
- [Global variable](https://en.wikipedia.org/wiki/Global_variable)
- [HTML sanitization](https://en.wikipedia.org/wiki/HTML_sanitization)
- [Hyphen-minus](https://en.wikipedia.org/wiki/Hyphen-minus)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Macro (computer science)](https://en.wikipedia.org/wiki/Macro_(computer_science))
- [Pipeline (Unix)](https://en.wikipedia.org/wiki/Pipeline_(Unix))
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Salt (software)](https://en.wikipedia.org/wiki/Salt_(software))
- [Sandbox (computer security)](https://en.wikipedia.org/wiki/Sandbox_(computer_security))
- [Smarty (template engine)](https://en.wikipedia.org/wiki/Smarty_(template_engine))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Software testing](https://en.wikipedia.org/wiki/Software_testing)
- [Tag (programming)](https://en.wikipedia.org/wiki/Tag_(programming))
- [Web template system](https://en.wikipedia.org/wiki/Web_template_system)
- [Trac](https://en.wikipedia.org/wiki/Trac)
- [Unix](https://en.wikipedia.org/wiki/Unix)
- [Vertical bar](https://en.wikipedia.org/wiki/Vertical_bar)
- [Web template system](https://en.wikipedia.org/wiki/Web_template_system)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:31:23.950945+00:00_