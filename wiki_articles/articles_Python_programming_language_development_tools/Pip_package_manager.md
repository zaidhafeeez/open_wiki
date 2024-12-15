# Pip (package manager)

## Article Metadata

- **Last Updated:** 2024-12-15T03:25:33.344517+00:00
- **Original Article:** [Pip (package manager)](https://en.wikipedia.org/wiki/Pip_(package_manager))
- **Language:** en
- **Page ID:** 34292335

## Summary

pip (also known by Python 3's alias pip3) is a package-management system written in Python and is used to install and manage software packages. The Python Software Foundation recommends using pip for installing Python applications and its dependencies during deployment. Pip connects to an online repository of public packages, called the Python Package Index. Pip can be configured to connect to other package repositories (local or remote), provided that they comply to Python Enhancement Proposal 

## Categories

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

## Related Articles

### Internal Links

- [.NET Framework](https://en.wikipedia.org/wiki/.NET_Framework)
- [APT-RPM](https://en.wikipedia.org/wiki/APT-RPM)
- [APT (software)](https://en.wikipedia.org/wiki/APT_(software))
- [ActiveState](https://en.wikipedia.org/wiki/ActiveState)
- [Add-on (Mozilla)](https://en.wikipedia.org/wiki/Add-on_(Mozilla))
- [Allmyapps](https://en.wikipedia.org/wiki/Allmyapps)
- [Amazon Appstore](https://en.wikipedia.org/wiki/Amazon_Appstore)
- [Anaconda (Python distribution)](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution))
- [Apache Ivy](https://en.wikipedia.org/wiki/Apache_Ivy)
- [Apache Maven](https://en.wikipedia.org/wiki/Apache_Maven)
- [AppImage](https://en.wikipedia.org/wiki/AppImage)
- [App Store (Apple)](https://en.wikipedia.org/wiki/App_Store_(Apple))
- [APT (software)](https://en.wikipedia.org/wiki/APT_(software))
- [Aptitude (software)](https://en.wikipedia.org/wiki/Aptitude_(software))
- [Aptoide](https://en.wikipedia.org/wiki/Aptoide)
- [Arch Linux](https://en.wikipedia.org/wiki/Arch_Linux)
- [Arch Linux](https://en.wikipedia.org/wiki/Arch_Linux)
- [Autopackage](https://en.wikipedia.org/wiki/Autopackage)
- [Berkeley Software Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution)
- [BitBake](https://en.wikipedia.org/wiki/BitBake)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CPAN](https://en.wikipedia.org/wiki/CPAN)
- [Cafe Bazaar](https://en.wikipedia.org/wiki/Cafe_Bazaar)
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [Chocolatey](https://en.wikipedia.org/wiki/Chocolatey)
- [Chrome Web Store](https://en.wikipedia.org/wiki/Chrome_Web_Store)
- [Command-line interface](https://en.wikipedia.org/wiki/Command-line_interface)
- [Composer (software)](https://en.wikipedia.org/wiki/Composer_(software))
- [Computing platform](https://en.wikipedia.org/wiki/Computing_platform)
- [Conda (package manager)](https://en.wikipedia.org/wiki/Conda_(package_manager))
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Cydia](https://en.wikipedia.org/wiki/Cydia)
- [Cygwin](https://en.wikipedia.org/wiki/Cygwin)
- [DNF (software)](https://en.wikipedia.org/wiki/DNF_(software))
- [Nintendo DSi](https://en.wikipedia.org/wiki/Nintendo_DSi)
- [Dpkg](https://en.wikipedia.org/wiki/Dpkg)
- [Dselect](https://en.wikipedia.org/wiki/Dselect)
- [Embedded operating system](https://en.wikipedia.org/wiki/Embedded_operating_system)
- [Enthought](https://en.wikipedia.org/wiki/Enthought)
- [Executable](https://en.wikipedia.org/wiki/Executable)
- [F-Droid](https://en.wikipedia.org/wiki/F-Droid)
- [Fink (software)](https://en.wikipedia.org/wiki/Fink_(software))
- [Flatpak](https://en.wikipedia.org/wiki/Flatpak)
- [FreeBSD Ports](https://en.wikipedia.org/wiki/FreeBSD_Ports)
- [GNU Guix](https://en.wikipedia.org/wiki/GNU_Guix)
- [GetJar](https://en.wikipedia.org/wiki/GetJar)
- [GoboLinux](https://en.wikipedia.org/wiki/GoboLinux)
- [Google Play](https://en.wikipedia.org/wiki/Google_Play)
- [Gradle](https://en.wikipedia.org/wiki/Gradle)
- [Helm (package manager)](https://en.wikipedia.org/wiki/Helm_(package_manager))
- [Helm (package manager)](https://en.wikipedia.org/wiki/Helm_(package_manager))
- [Homebrew (package manager)](https://en.wikipedia.org/wiki/Homebrew_(package_manager))
- [Huawei AppGallery](https://en.wikipedia.org/wiki/Huawei_AppGallery)
- [Illumos](https://en.wikipedia.org/wiki/Illumos)
- [Image Packaging System](https://en.wikipedia.org/wiki/Image_Packaging_System)
- [Dpkg](https://en.wikipedia.org/wiki/Dpkg)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes)
- [Linux](https://en.wikipedia.org/wiki/Linux)
- [List of software package management systems](https://en.wikipedia.org/wiki/List_of_software_package_management_systems)
- [MIT License](https://en.wikipedia.org/wiki/MIT_License)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [MacPorts](https://en.wikipedia.org/wiki/MacPorts)
- [Mac App Store](https://en.wikipedia.org/wiki/Mac_App_Store)
- [Meta Horizon Store](https://en.wikipedia.org/wiki/Meta_Horizon_Store)
- [Microsoft Store](https://en.wikipedia.org/wiki/Microsoft_Store)
- [Microsoft Store](https://en.wikipedia.org/wiki/Microsoft_Store)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Mobile operating system](https://en.wikipedia.org/wiki/Mobile_operating_system)
- [Munki (software)](https://en.wikipedia.org/wiki/Munki_(software))
- [Zenwalk](https://en.wikipedia.org/wiki/Zenwalk)
- [Nintendo eShop](https://en.wikipedia.org/wiki/Nintendo_eShop)
- [Nix (package manager)](https://en.wikipedia.org/wiki/Nix_(package_manager))
- [List of software package management systems](https://en.wikipedia.org/wiki/List_of_software_package_management_systems)
- [Npm](https://en.wikipedia.org/wiki/Npm)
- [NuGet](https://en.wikipedia.org/wiki/NuGet)
- [Nullsoft](https://en.wikipedia.org/wiki/Nullsoft)
- [OpenCSW](https://en.wikipedia.org/wiki/OpenCSW)
- [OpenPKG](https://en.wikipedia.org/wiki/OpenPKG)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Dpkg](https://en.wikipedia.org/wiki/Dpkg)
- [PEAR](https://en.wikipedia.org/wiki/PEAR)
- [Puppy Linux](https://en.wikipedia.org/wiki/Puppy_Linux)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Pardus (operating system)](https://en.wikipedia.org/wiki/Pardus_(operating_system))
- [PackageKit](https://en.wikipedia.org/wiki/PackageKit)
- [Package manager](https://en.wikipedia.org/wiki/Package_manager)
- [Package format](https://en.wikipedia.org/wiki/Package_format)
- [Package manager](https://en.wikipedia.org/wiki/Package_manager)
- [Package manager](https://en.wikipedia.org/wiki/Package_manager)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Pkgsrc](https://en.wikipedia.org/wiki/Pkgsrc)
- [PlayStation Store](https://en.wikipedia.org/wiki/PlayStation_Store)
- [Portage (software)](https://en.wikipedia.org/wiki/Portage_(software))
- [Ports collection](https://en.wikipedia.org/wiki/Ports_collection)
- [ProGet](https://en.wikipedia.org/wiki/ProGet)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Purely functional programming](https://en.wikipedia.org/wiki/Purely_functional_programming)
- [Python Package Index](https://en.wikipedia.org/wiki/Python_Package_Index)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [History of Python](https://en.wikipedia.org/wiki/History_of_Python)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Package Index](https://en.wikipedia.org/wiki/Python_Package_Index)
- [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation)
- [RPM Package Manager](https://en.wikipedia.org/wiki/RPM_Package_Manager)
- [Recursive acronym](https://en.wikipedia.org/wiki/Recursive_acronym)
- [Red Hat](https://en.wikipedia.org/wiki/Red_Hat)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [RubyGems](https://en.wikipedia.org/wiki/RubyGems)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [SMP/E](https://en.wikipedia.org/wiki/SMP/E)
- [Sbt (software)](https://en.wikipedia.org/wiki/Sbt_(software))
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scoop Package Manager](https://en.wikipedia.org/wiki/Scoop_Package_Manager)
- [Slackware](https://en.wikipedia.org/wiki/Slackware)
- [Slapt-get](https://en.wikipedia.org/wiki/Slapt-get)
- [List of mobile app distribution platforms](https://en.wikipedia.org/wiki/List_of_mobile_app_distribution_platforms)
- [Snap (software)](https://en.wikipedia.org/wiki/Snap_(software))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Software repository](https://en.wikipedia.org/wiki/Software_repository)
- [Oracle Solaris](https://en.wikipedia.org/wiki/Oracle_Solaris)
- [Source Mage](https://en.wikipedia.org/wiki/Source_Mage)
- [Source code](https://en.wikipedia.org/wiki/Source_code)
- [Slackware](https://en.wikipedia.org/wiki/Slackware)
- [Synaptic (software)](https://en.wikipedia.org/wiki/Synaptic_(software))
- [Tar (computing)](https://en.wikipedia.org/wiki/Tar_(computing))
- [TrueOS](https://en.wikipedia.org/wiki/TrueOS)
- [Ubuntu Software Center](https://en.wikipedia.org/wiki/Ubuntu_Software_Center)
- [Unix-like](https://en.wikipedia.org/wiki/Unix-like)
- [Up2date](https://en.wikipedia.org/wiki/Up2date)
- [Paldo (operating system)](https://en.wikipedia.org/wiki/Paldo_(operating_system))
- [Urpmi](https://en.wikipedia.org/wiki/Urpmi)
- [Vcpkg](https://en.wikipedia.org/wiki/Vcpkg)
- [Video game console](https://en.wikipedia.org/wiki/Video_game_console)
- [Virtualization](https://en.wikipedia.org/wiki/Virtualization)
- [Web browser](https://en.wikipedia.org/wiki/Web_browser)
- [Wii Shop Channel](https://en.wikipedia.org/wiki/Wii_Shop_Channel)
- [Windows Package Manager](https://en.wikipedia.org/wiki/Windows_Package_Manager)
- [Windows Phone Store](https://en.wikipedia.org/wiki/Windows_Phone_Store)
- [Dpkg](https://en.wikipedia.org/wiki/Dpkg)
- [Xbox Games Store](https://en.wikipedia.org/wiki/Xbox_Games_Store)
- [Yum (software)](https://en.wikipedia.org/wiki/Yum_(software))
- [Z/OS](https://en.wikipedia.org/wiki/Z/OS)
- [ZYpp](https://en.wikipedia.org/wiki/ZYpp)
- [Wikipedia:No original research](https://en.wikipedia.org/wiki/Wikipedia:No_original_research)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Package management systems](https://en.wikipedia.org/wiki/Template:Package_management_systems)
- [Template talk:Package management systems](https://en.wikipedia.org/wiki/Template_talk:Package_management_systems)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles lacking reliable references from November 2022](https://en.wikipedia.org/wiki/Category:Articles_lacking_reliable_references_from_November_2022)
- [Category:Package management systems](https://en.wikipedia.org/wiki/Category:Package_management_systems)
- [Category:Use dmy dates from June 2018](https://en.wikipedia.org/wiki/Category:Use_dmy_dates_from_June_2018)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:25:33.344517+00:00_