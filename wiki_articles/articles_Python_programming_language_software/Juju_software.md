# Juju (software)

## Metadata
- **Last Updated:** 2024-12-03 07:31:08 UTC
- **Original Article:** [Juju (software)](https://en.wikipedia.org/wiki/Juju_(software))
- **Language:** en
- **Page ID:** 33085168

## Summary
Juju is a free and open-source application modeling tool developed by Canonical Ltd. Juju is an application management system. It was built to reduce the operation overhead of software by facilitating, deploying, configuring, scaling, integrating, and performing operational tasks on public and private cloud services along with bare-metal servers and local container-based deployments.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 20:39:41 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 3805 bytes
- **Word Count:** 588 words
