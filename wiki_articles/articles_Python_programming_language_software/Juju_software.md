# Juju (software)

## Article Metadata

- **Last Updated:** 2024-12-15T03:59:07.640362+00:00
- **Original Article:** [Juju (software)](https://en.wikipedia.org/wiki/Juju_(software))
- **Language:** en
- **Page ID:** 33085168

## Summary

Juju is a free and open-source application modeling tool developed by Canonical Ltd. Juju is an application management system. It was built to reduce the operation overhead of software by facilitating, deploying, configuring, scaling, integrating, and performing operational tasks on public and private cloud services along with bare-metal servers and local container-based deployments.

## Categories

- Category:All articles needing additional references
- Category:All articles with a promotional tone
- Category:Articles needing additional references from September 2014
- Category:Articles with a promotional tone from March 2014
- Category:Articles with multiple maintenance issues
- Category:Articles with short description
- Category:CS1 errors: bare URL
- Category:CS1 errors: missing title
- Category:Canonical (company)
- Category:Free software programmed in Go
- Category:Python (programming language) software
- Category:Short description matches Wikidata
- Category:Software using the GNU AGPL license

## Table of Contents

- Juju modeling complex software topologies
- Juju charms
- Juju client and environments
- Command line and GUI
- Bundles
- Charm Store
- Supported platforms

## Content

Juju is a free and open-source application modeling tool developed by Canonical Ltd. Juju is an application management system. It was built to reduce the operation overhead of software by facilitating, deploying, configuring, scaling, integrating, and performing operational tasks on public and private cloud services along with bare-metal servers and local container-based deployments.

Juju modeling complex software topologies
Juju aims to provide a modeling language that abstracts the specifics of operating complex software topologies to reduce the cost of operations and provide flexibility. A Juju model is an environment to manage and operate a set of software applications. Models can be operated on a variety of public clouds.
A Juju controller is a service that tracks the events, state, and user activity across multiple models. A database server tool and databases available on a server are an example of a Juju controller and its models. Each model can have different configurations, sets of operating software, and users with various levels of access. Examples of models include a web application, load balancer, and database in a "web-app" model. Models allow deployments to be isolated into logical solutions and managed separately.

Juju charms
The central mechanism behind Juju is called charms. Charms can be written in any programming language that can be executed from the command line. A charm is a collection of YAML configuration files and a selection of hooks. A hook is an executable file that can be used to install software, start or stop a service, manage relationships with other charms, upgrade charms, scale charms, configure charms, etc. Charms can have many properties. Using charm helpers, boiler-plate code is automatically generated, thereby speeding up charm creation.

Juju client and environments
Juju has two components: a client and a bootstrap node. After installing the client, one or more environments can be bootstrapped. Juju environments can be bootstrapped on various clouds. By creating a Juju Provider, additional cloud environments can be supported.
Juju can also be bootstrapped on bare-metal servers. Large deployments can use Canonical's Metal as a Service. Small deployments can use the manual provider, which allows any SSH-accessible Ubuntu machine to be converted into a Juju-managed machine. Juju can also be installed on a local Ubuntu machine via LXC operating system–level virtualization and the local provider.

Command line and GUI
Juju has both command line and GUI access. Automatically available on every controller, the Juju GUI allows users to visually see what software is currently running in which models. Users can also search the Charm Store [see below] and browse results with detailed charm information. Complex software stacks can be deployed via drag-and-drop.

Bundles
Juju also has a concept of bundles. A bundle is a portable specification for a model with charms, configuration, and relations, all specified in a declarative YAML format. A bundle YAML file can later be imported into another Juju model and shared with others. Bundles can also be uploaded to the Charm Store, allowing others to deploy them.
In this example bundle, two applications are modeled: MediaWiki and MySQL. Users can modify attributes declared in the bundle to customize their deployment:

Charm Store
The Juju Charm Store launched on April 3, 2012. The Charm Store regularly tests charms to notify charm authors when code breaks, in addition to ensuring that Juju users have access to the latest versions of charms.

Supported platforms
Juju is available on the Ubuntu Server, with agents available for Ubuntu, CentOS, and Microsoft Windows. Support for both CentOS and Windows has been contributed by Cloudbase Solutions.


== References ==

## Related Articles

### Internal Links

- [APT (software)](https://en.wikipedia.org/wiki/APT_(software))
- [Almquist shell](https://en.wikipedia.org/wiki/Almquist_shell)
- [AppArmor](https://en.wikipedia.org/wiki/AppArmor)
- [Aptitude (software)](https://en.wikipedia.org/wiki/Aptitude_(software))
- [Ask Ubuntu](https://en.wikipedia.org/wiki/Ask_Ubuntu)
- [Bare-metal server](https://en.wikipedia.org/wiki/Bare-metal_server)
- [Benjamin Mako Hill](https://en.wikipedia.org/wiki/Benjamin_Mako_Hill)
- [Brasero (software)](https://en.wikipedia.org/wiki/Brasero_(software))
- [Canonical (company)](https://en.wikipedia.org/wiki/Canonical_(company))
- [Canonical (company)](https://en.wikipedia.org/wiki/Canonical_(company))
- [Canonical (company)](https://en.wikipedia.org/wiki/Canonical_(company))
- [CentOS](https://en.wikipedia.org/wiki/CentOS)
- [Cloud computing](https://en.wikipedia.org/wiki/Cloud_computing)
- [Containerization (computing)](https://en.wikipedia.org/wiki/Containerization_(computing))
- [Deb (file format)](https://en.wikipedia.org/wiki/Deb_(file_format))
- [Debian](https://en.wikipedia.org/wiki/Debian)
- [Debian configuration system](https://en.wikipedia.org/wiki/Debian_configuration_system)
- [Dpkg](https://en.wikipedia.org/wiki/Dpkg)
- [EasyPeasy](https://en.wikipedia.org/wiki/EasyPeasy)
- [Edubuntu](https://en.wikipedia.org/wiki/Edubuntu)
- [Elementary OS](https://en.wikipedia.org/wiki/Elementary_OS)
- [Emmabuntüs](https://en.wikipedia.org/wiki/Emmabunt%C3%BCs)
- [Free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software)
- [Full Circle (magazine)](https://en.wikipedia.org/wiki/Full_Circle_(magazine))
- [GNOME Files](https://en.wikipedia.org/wiki/GNOME_Files)
- [GNU Affero General Public License](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License)
- [GNU Bazaar](https://en.wikipedia.org/wiki/GNU_Bazaar)
- [GetDeb](https://en.wikipedia.org/wiki/GetDeb)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Gobuntu](https://en.wikipedia.org/wiki/Gobuntu)
- [Ian Jackson](https://en.wikipedia.org/wiki/Ian_Jackson)
- [Jane Silber](https://en.wikipedia.org/wiki/Jane_Silber)
- [Jeff Waugh](https://en.wikipedia.org/wiki/Jeff_Waugh)
- [Jono Bacon](https://en.wikipedia.org/wiki/Jono_Bacon)
- [KDE neon](https://en.wikipedia.org/wiki/KDE_neon)
- [Kubuntu](https://en.wikipedia.org/wiki/Kubuntu)
- [LXC](https://en.wikipedia.org/wiki/LXC)
- [Landscape (software)](https://en.wikipedia.org/wiki/Landscape_(software))
- [Launchpad (website)](https://en.wikipedia.org/wiki/Launchpad_(website))
- [LightDM](https://en.wikipedia.org/wiki/LightDM)
- [Linux Lite](https://en.wikipedia.org/wiki/Linux_Lite)
- [Linux Mint](https://en.wikipedia.org/wiki/Linux_Mint)
- [List of Linux distributions](https://en.wikipedia.org/wiki/List_of_Linux_distributions)
- [Lubuntu](https://en.wikipedia.org/wiki/Lubuntu)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [Mark Shuttleworth](https://en.wikipedia.org/wiki/Mark_Shuttleworth)
- [MediaWiki](https://en.wikipedia.org/wiki/MediaWiki)
- [Medibuntu](https://en.wikipedia.org/wiki/Medibuntu)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Mir (software)](https://en.wikipedia.org/wiki/Mir_(software))
- [MySQL](https://en.wikipedia.org/wiki/MySQL)
- [Mythbuntu](https://en.wikipedia.org/wiki/Mythbuntu)
- [OpenCD](https://en.wikipedia.org/wiki/OpenCD)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [OS-level virtualization](https://en.wikipedia.org/wiki/OS-level_virtualization)
- [Orchestration (computing)](https://en.wikipedia.org/wiki/Orchestration_(computing))
- [Paper cut bug](https://en.wikipedia.org/wiki/Paper_cut_bug)
- [Pop! OS](https://en.wikipedia.org/wiki/Pop!_OS)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Cloud computing](https://en.wikipedia.org/wiki/Cloud_computing)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Scott James Remnant](https://en.wikipedia.org/wiki/Scott_James_Remnant)
- [Ubuntu Touch](https://en.wikipedia.org/wiki/Ubuntu_Touch)
- [Snap (software)](https://en.wikipedia.org/wiki/Snap_(software))
- [Software Updater](https://en.wikipedia.org/wiki/Software_Updater)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [GNU GRUB](https://en.wikipedia.org/wiki/GNU_GRUB)
- [Startup Disk Creator](https://en.wikipedia.org/wiki/Startup_Disk_Creator)
- [System76](https://en.wikipedia.org/wiki/System76)
- [Trisquel](https://en.wikipedia.org/wiki/Trisquel)
- [Tuxedo Computers](https://en.wikipedia.org/wiki/Tuxedo_Computers)
- [Ubiquity (software)](https://en.wikipedia.org/wiki/Ubiquity_(software))
- [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu)
- [Ubuntu-restricted-extras](https://en.wikipedia.org/wiki/Ubuntu-restricted-extras)
- [Ubuntu (typeface)](https://en.wikipedia.org/wiki/Ubuntu_(typeface))
- [Ubuntu Budgie](https://en.wikipedia.org/wiki/Ubuntu_Budgie)
- [Ubuntu Cinnamon](https://en.wikipedia.org/wiki/Ubuntu_Cinnamon)
- [Ubuntu Edge](https://en.wikipedia.org/wiki/Ubuntu_Edge)
- [Ubuntu Forums](https://en.wikipedia.org/wiki/Ubuntu_Forums)
- [Ubuntu GNOME](https://en.wikipedia.org/wiki/Ubuntu_GNOME)
- [Ubuntu JeOS](https://en.wikipedia.org/wiki/Ubuntu_JeOS)
- [Ubuntu Kylin](https://en.wikipedia.org/wiki/Ubuntu_Kylin)
- [Ubuntu MATE](https://en.wikipedia.org/wiki/Ubuntu_MATE)
- [Ubuntu Netbook Edition](https://en.wikipedia.org/wiki/Ubuntu_Netbook_Edition)
- [Ubuntu One](https://en.wikipedia.org/wiki/Ubuntu_One)
- [Ubuntu Professional Certification](https://en.wikipedia.org/wiki/Ubuntu_Professional_Certification)
- [Ubuntu Single Sign On](https://en.wikipedia.org/wiki/Ubuntu_Single_Sign_On)
- [Ubuntu Software Center](https://en.wikipedia.org/wiki/Ubuntu_Software_Center)
- [Ubuntu Studio](https://en.wikipedia.org/wiki/Ubuntu_Studio)
- [Ubuntu Titling](https://en.wikipedia.org/wiki/Ubuntu_Titling)
- [Ubuntu Touch](https://en.wikipedia.org/wiki/Ubuntu_Touch)
- [Ubuntu Unity](https://en.wikipedia.org/wiki/Ubuntu_Unity)
- [Ubuntu User](https://en.wikipedia.org/wiki/Ubuntu_User)
- [Ubuntu Touch](https://en.wikipedia.org/wiki/Ubuntu_Touch)
- [Ubuntu philosophy](https://en.wikipedia.org/wiki/Ubuntu_philosophy)
- [Ubuntu version history](https://en.wikipedia.org/wiki/Ubuntu_version_history)
- [Uncomplicated Firewall](https://en.wikipedia.org/wiki/Uncomplicated_Firewall)
- [Unity (user interface)](https://en.wikipedia.org/wiki/Unity_(user_interface))
- [Upstart (software)](https://en.wikipedia.org/wiki/Upstart_(software))
- [Usplash](https://en.wikipedia.org/wiki/Usplash)
- [Wubi (software)](https://en.wikipedia.org/wiki/Wubi_(software))
- [Wubuntu](https://en.wikipedia.org/wiki/Wubuntu)
- [Bootsplash](https://en.wikipedia.org/wiki/Bootsplash)
- [Xubuntu](https://en.wikipedia.org/wiki/Xubuntu)
- [YAML](https://en.wikipedia.org/wiki/YAML)
- [Zorin OS](https://en.wikipedia.org/wiki/Zorin_OS)
- [Talk:Juju (software)](https://en.wikipedia.org/wiki/Talk:Juju_(software))
- [Wikipedia:External links](https://en.wikipedia.org/wiki/Wikipedia:External_links)
- [Wikipedia:Neutral point of view](https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view)
- [Wikipedia:Spam](https://en.wikipedia.org/wiki/Wikipedia:Spam)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Wikipedia:What Wikipedia is not](https://en.wikipedia.org/wiki/Wikipedia:What_Wikipedia_is_not)
- [Template:Cite web](https://en.wikipedia.org/wiki/Template:Cite_web)
- [Template:Ubuntu](https://en.wikipedia.org/wiki/Template:Ubuntu)
- [Template talk:Ubuntu](https://en.wikipedia.org/wiki/Template_talk:Ubuntu)
- [Help:CS1 errors](https://en.wikipedia.org/wiki/Help:CS1_errors)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from September 2014](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_September_2014)
- [Category:Articles with a promotional tone from March 2014](https://en.wikipedia.org/wiki/Category:Articles_with_a_promotional_tone_from_March_2014)
- [Category:Ubuntu](https://en.wikipedia.org/wiki/Category:Ubuntu)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)
- [Portal:Linux](https://en.wikipedia.org/wiki/Portal:Linux)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:59:07.640362+00:00_