---
title: Zope
url: https://en.wikipedia.org/wiki/Zope
language: en
categories: ["Category:1995 establishments in Virginia", "Category:All articles with unsourced statements", "Category:Articles with short description", "Category:Articles with unsourced statements from August 2011", "Category:Cross-platform free software", "Category:Free content management systems", "Category:Free software programmed in Python", "Category:Python (programming language) web frameworks", "Category:Short description is different from Wikidata", "Category:Software companies based in Virginia", "Category:Software companies established in 1995", "Category:Software companies of the United States", "Category:Web development software", "Category:Web server software for Linux", "Category:Zope"]
references: 0
last_modified: 2024-12-19T13:42:14Z
---

# Zope

## Summary

Zope is a family of free and open-source web application servers written in Python, and their associated online community. Zope stands for "Z Object Publishing Environment", and was the first system using the now common object publishing methodology for the Web. Zope has been called a Python killer app, an application that helped put Python in the spotlight.
Over the last few years, the Zope community has spawned several additional web frameworks with disparate aims and principles, but sharing p

## Full Content

Zope is a family of free and open-source web application servers written in Python, and their associated online community. Zope stands for "Z Object Publishing Environment", and was the first system using the now common object publishing methodology for the Web. Zope has been called a Python killer app, an application that helped put Python in the spotlight.
Over the last few years, the Zope community has spawned several additional web frameworks with disparate aims and principles, but sharing philosophy, people, and source code. Zope 2 is still the most widespread of these frameworks, largely thanks to the Plone content management system, which runs on Zope 2. BlueBream (earlier called Zope 3) is less widespread but underlies several large sites, including Launchpad. Grok was started as a more programmer-friendly framework, "Zope 3 for cavemen", and in 2009 Pyramid gained popularity in the Zope community as a minimalistic framework based on Zope principles.

History
The Zope Corporation was formed in 1995 in Fredericksburg, Virginia under the name Digital Creations, as a joint venture with InfiNet (a joint newspaper chain venture). The company developed a classified advertisement engine for the Internet. In 1997, the company became independently owned and private. The company's software engineers are led by CTO Jim Fulton. PythonLabs, creators of Python, became part of the company in 2000 (Python founder Guido van Rossum left Zope Corp in 2003).
What is now known as Zope 2 began with the merging of three separate software products – Bobo, Document Template, and BoboPOS – into the Principia application server. At the behest of its largest investor, Opticality Ventures, Principia was re-released as free software under the name Zope in 1998. Bobo, and therefore Zope, was the first Web object publishing solution.
In November 2004, Zope 3 was released. Zope 3 is a complete rewrite that preserves only the original ZODB object database. It is directly intended for enterprise Web application development using the newest development paradigms. Zope 3 is, however, not compatible with Zope 2, so Zope 2 applications do not run on Zope 3. It was originally intended to introduce a backwards-compatibility layer so that Zope 2 software would run on Zope 3. Instead a module known as Five introduced the new Zope 3 paradigms into Zope 2, although full compatibility isn't possible that way either.
The existence of two incompatible Web frameworks called Zope has caused a lot of confusion. In response, in January 2010, Zope 3 was renamed "BlueBream". "Zope" and "blue bream" are names of a kind of fish, Ballerus ballerus.

Zope Foundation
The Zope Foundation is an organization that promotes the development of the Zope platform by supporting the community that develops and maintains the relevant software components. The community includes both open source software, documentation and web infrastructure contributors, as well as business and organization consumers of the software platform. It manages the zope.org websites, an infrastructure for open source collaboration.

Zope versions
Zope 2
A Zope website is usually composed of objects in a Zope Object Database, not files on a file system, as is usual with most web servers. This allows users to harness the advantages of object technologies, such as encapsulation. Zope maps URLs to objects using the containment hierarchy of such objects; methods are considered to be contained in their objects as well. Data can be stored in other databases as well, or on the file system, but ZODB is the most common solution.
Zope provides two mechanisms for HTML templating: Document Template Markup Language (DTML) and Zope Page Templates (ZPT). DTML is a tag-based language that allows implementation of simple scripting in the templates. DTML has provisions for variable inclusion, conditions, and loops. However, DTML can be problematic: DTML tags interspersed with HTML form non-valid HTML documents, and its use requires care when including logic into templates, to retain code readability. The use of DTML is discouraged by many leading Zope developers. ZPT is a technology that addresses the shortcomings of DTML. ZPT templates can be either well-formed XML documents or HTML documents, in which all special markup is presented as attributes in the TAL (Template Attribute Language) namespace. ZPT offers a very limited set of tools for conditional inclusion and repetition of XML elements. Consequently, the templates are usually quite simple, with most logic implemented in Python code. One significant advantage of ZPT templates is that they can be edited in most graphical HTML editors. ZPT also offers direct support for internationalization.
Zope 2 underlies the Plone content management system, as well as the ERP5 open source enterprise resource planning system.

BlueBream
BlueBream is a rewrite by the Zope developers of the Zope 2 web application server. It was created under the name "Zope 3", but the existence of two incompatible frameworks with the same name caused much confusion, and Zope 3 was renamed "BlueBream" in January 2010. BlueBream is distributed under the terms of the Zope Public License and is thus free software.
Zope 2 has proven itself as a useful framework for Web applications development, but its use revealed some shortcomings. To name a few, creating Zope 2 products involves copying a lot of boilerplate code – "magic" code – that just has to be there, and the built-in management interface is difficult to modify or replace. Zope 3 was a rewrite of the software that attempts to address these shortcomings while retaining the advantages of Zope that led to its popularity. BlueBream is based on a component architecture that makes it easy to mix software components of various origins written in Python. Although originally intended as a replacement for Zope 2, the Zope Component Architecture has instead been backported to Zope 2, starting with Zope 2.8. Many Zope platforms such as Plone are going through the same type of piece-by-piece rewriting. The first production release of the new software, Zope X3 3.0.0, was released on November 6, 2004.

History
The Zope 3 project started in February 2001 as an effort to develop a new version of Zope as an almost complete rewrite, with the goal to retain the successful features of Zope 2 while trying to fix some of its shortcomings. The goal was to create a more developer-friendly and flexible platform for programming web applications than Zope 2 is. The project began with the development of a component architecture, which allows the structuring of code into small, composable units with introspectable interfaces. The interfaces are supported by an interface package in order to provide the functionality of explicitly declared interfaces to the Python language. The first production release of the software, Zope X3, was released on November 6, 2004. In January 2010 Zope 3 was renamed BlueBream.

Technology
The goal of the project was to enable programmers to use Zope in order to expose arbitrary Python objects as model objects to the web without the need to make these objects fulfill particular behavior requirements. In Zope 2 there had been many behavior requirements to allow objects to participate in the framework, which resulted in a large amount of mixin base classes and special attributes. BlueBream uses a model/view architecture, separating the presentation code from the problem domain code. Views and models are linked together by the component architecture.
The libraries underlying BlueBream have been evolving into a collection of useful libraries for web application development rather than a single, monolithic application server. BlueBream includes separate packages for interfaces, component architecture, HTTP server, publisher, Zope Object Database (ZODB), Zope Page Templates, I18N, security policy, and so on. The component architecture is used to glue these together. The component architecture is configured using a ZCML (Zope Configuration Markup Language), an XML based configuration file language.
The Zope 3 project pioneered the practice of sprints for open source software development. Sprints are intensive development sessions when programmers, often from different countries, gather in one room and work together for a couple of days or even several weeks. During the sprints various practices drawn from agile software development are used, such as pair programming and test-driven development. Besides the goal of developing software, sprints are also useful for geographically separated developers to meet in person and attracting new people to the project. They also serve as a way for the participants to learn from each other.
BlueBream is considered a stable framework, used on production projects worldwide, most notably Launchpad.

Zope Toolkit
As a result of the development of Zope 3 / BlueBream, there are now many independent Python packages used and developed as a part of BlueBream, and although many of these are usable outside of BlueBream, many are not. The Zope Toolkit (ZTK) project was started to clarify which packages were usable outside BlueBream, and to improve the re-usability of the packages. Thus the Zope Toolkit is a base for the Zope frameworks. Zope 2.12 is the first release of a web framework that builds on Zope Toolkit, and Grok and BlueBream were set to have releases based on the ZTK during 2010.

Grok
In 2006 the Grok project was started by a number of Zope 3 developers who wanted to make Zope 3 technology more agile in use and more accessible to newcomers. Grok has since then seen regular releases and its core technology (Martian, grokcore.component) is also finding uptake in other Zope 3 and Zope 2 based projects.

Zope 4
In late 2017, development began on Zope 4. Zope 4 is a successor to Zope 2.13, making many changes that are not backwards compatible with Zope 2.

Zope 5
Zope 5 was released in 2020.

Zope page templates
As mentioned previously, Zope page templates are themselves XHTML documents, which means they can be viewed and edited using normal HTML editors or XHTML compliant tools (a big advantage compared to other template languages used for Web applications). Templates can also be checked for XHTML compliance so you can be fairly confident that they will automatically expand into proper XHTML.
However, these page templates are not meant to be rendered as is. Instead they are marked up with additional elements and attributes in special XML namespaces (see below). This additional information is used to describe how the page template should ultimately be processed.
Here are some basic examples. To conditionally include a particular element, like a div element, simply add the tal:condition attribute to the element as follows:

To control what appears inside an element, use the tal:content attribute like this:

Finally, to introduce or replace values of attributes use the tal:attributes attribute as below. You can use Python to alter the href at runtime.

This is a very cursory explanation of Zope Page Templates. The behavior of Zope Page Templates is almost completely described by a template language, fixed on TAL, TALES, and METAL specifications:

Template Attribute Language (TAL),
Template Attribute Language Expression Syntax (TALES),
Macro Expansion Template Attribute Language (METAL).

Notable software using Zope
SchoolTool is an open source student information system that uses Zope.
Plone is an open source content management system that uses Zope.

See also
Pylons project
Django
web2py
Content management (CM)
Web content management system (WCMS)
Naaya
Twisted

References
External links

Official website