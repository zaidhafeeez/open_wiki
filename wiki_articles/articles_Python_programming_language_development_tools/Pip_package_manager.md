# Pip (package manager)

## Metadata
- **Last Updated:** 2024-12-06 05:49:10 UTC
- **Original Article:** [Pip (package manager)](https://en.wikipedia.org/wiki/Pip_(package_manager))
- **Language:** en
- **Page ID:** 34292335

## Summary
pip (also known by Python 3's alias pip3) is a package-management system written in Python and is used to install and manage software packages. The Python Software Foundation recommends using pip for installing Python applications and its dependencies during deployment. Pip connects to an online repository of public packages, called the Python Package Index. Pip can be configured to connect to other package repositories (local or remote), provided that they comply to Python Enhancement Proposal 503.
Most distributions of Python come with pip preinstalled. Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default.

## Categories
This article belongs to the following categories:

- Category:All articles lacking reliable references
- Category:Articles lacking reliable references from November 2022
- Category:Articles with short description
- Category:Free package management systems
- Category:Free software programmed in Python
- Category:Python (programming language) development tools
- Category:Short description matches Wikidata
- Category:Software using the MIT license
- Category:Use dmy dates from June 2018

## Table of Contents

- History
- Command-line interface
- Custom repository
- See also
- References
- External links

## Content

pip (also known by Python 3's alias pip3) is a package-management system written in Python and is used to install and manage software packages. The Python Software Foundation recommends using pip for installing Python applications and its dependencies during deployment. Pip connects to an online repository of public packages, called the Python Package Index. Pip can be configured to connect to other package repositories (local or remote), provided that they comply to Python Enhancement Proposal 503.
Most distributions of Python come with pip preinstalled. Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default.

History
First introduced as pyinstall in 2008 by Ian Bicking (the creator of the virtualenv package) as an alternative to easy install, pip was chosen as the new name from one of several suggestions that the creator received on his blog post. According to Bicking himself, the name is a recursive acronym for "Pip Installs Packages". In 2011, the Python Packaging Authority (PyPA) was created to take over the maintenance of pip and virtualenv from Bicking, led by Carl Meyer, Brian Rosner, and Jannis Leidel.
With the release of pip version 6.0 (2014-12-22), the version naming process was changed to have version in X.Y format and drop the preceding 1 from the version label.

Command-line interface
Pip's command-line interface allows the install of Python software packages by issuing a command: pip install some-package-name
Users can also remove the package by issuing a command: pip uninstall some-package-name
pip has a feature to manage full lists of packages and corresponding version numbers, possible through a "requirements" file. This permits the efficient re-creation of an entire group of packages in a separate environment (e.g. another computer) or virtual environment. This can be achieved with a properly formatted file and the following command, where requirements.txt is the name of the file: pip install -r requirements.txt.
To install some package for a specific python version, pip provides the following command, where ${version} is replaced by 2, 3, 3.4, etc.: pip${version} install some-package-name.

Using setup.py
Pip provides a way to install user-defined projects locally with the use of setup.py file. This method requires the python project to have the following file structure:

example_project/
├── exampleproject/      Python package with source code.
|    ├── __init__.py     Make the folder a package.
|    └── example.py      Example module.
└── README.md            README with info of the project.

Within this structure, user can add setup.py to the root of the project (i.e. example_project for above structure) with the following content:

After this, pip can install this custom project by running the following command, from the project root directory: pip install -e.

Custom repository
Besides the default PyPI repository, Pip supports custom repositories as well. Such repositories can be located on an HTTP(s) URL or on a file system location.
A custom repository can be specified using the -i or—index-url option, like so: pip install -i https://your-custom-repo/simple <package name>; or with a filesystem: pip install -i /path/to/your/custom-repo/simple <package name>.

See also
Setuptools
Pipenv
Python Poetry
Conda (package manager) for Anaconda distribution
PyPM - ActiveState's proprietary package manager

References
External links
Official Pip website
Python Packaging Authority

## Archive Info
- **Archived on:** 2024-12-15 20:27:14 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 3526 bytes
- **Word Count:** 523 words
