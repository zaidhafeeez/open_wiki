# Twisted (software)

## Article Metadata

- **Last Updated:** 2024-12-14T19:59:00.357459+00:00
- **Original Article:** [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- **Language:** en
- **Page ID:** 1793652

## Summary

Twisted is an event-driven network programming framework written in Python and licensed under the MIT License.
Twisted projects variously support TCP, UDP, SSL/TLS, IP multicast, Unix domain sockets, many protocols (including HTTP, XMPP, NNTP, IMAP, SSH, IRC, FTP, and others), and much more. Twisted is based on the event-driven programming paradigm, which means that users of Twisted write short callbacks which are called by the framework.

## Categories

- Category:All articles needing additional references
- Category:All articles with dead external links
- Category:All articles with unsourced statements
- Category:Articles needing additional references from March 2017
- Category:Articles with dead external links from July 2018
- Category:Articles with permanently dead external links
- Category:Articles with short description
- Category:Articles with unsourced statements from March 2017
- Category:Free network-related software
- Category:Free software programmed in Python
- Category:Free system software
- Category:Python (programming language) libraries
- Category:Python (programming language) software
- Category:Short description matches Wikidata
- Category:Software using the MIT license
- Category:Webarchive template wayback links

## Table of Contents

- Core ideas
- Applications using Twisted
- See also
- References
- External links

## Content

Twisted is an event-driven network programming framework written in Python and licensed under the MIT License.
Twisted projects variously support TCP, UDP, SSL/TLS, IP multicast, Unix domain sockets, many protocols (including HTTP, XMPP, NNTP, IMAP, SSH, IRC, FTP, and others), and much more. Twisted is based on the event-driven programming paradigm, which means that users of Twisted write short callbacks which are called by the framework.

Core ideas
Separation of protocols and transports
Twisted is designed for complete separation between logical protocols (usually relying on stream-based connection semantics, such as HTTP or POP3) and transport layers supporting such stream-based semantics (such as files, sockets or SSL libraries). Connection between a logical protocol and a transport layer happens at the last possible moment — just before information is passed into the logical protocol instance. The logical protocol is informed of the transport layer instance, and can use it to send messages back and to check for the peer's identity. Note that it is still possible, in protocol code, to deeply query the transport layer on transport issues (such as checking a client-side SSL certificate). Naturally, such protocol code will fail (raise an exception) if the transport layer does not support such semantics.

Deferreds
Central to the Twisted application model is the concept of a deferred (elsewhere called a future). A deferred is an instance of a class designed to receive and process a result which has not been computed yet, for example because it is based on data from a remote peer. Deferreds can be passed around, just like regular objects, but cannot be asked for their value. Each deferred supports a callback chain. When the deferred gets the value, it is passed to the functions on the callback chain, with the result of each callback becoming the input for the next. Deferreds make it possible to operate on the result of a function call before its value has become available.
For example, if a deferred returns a string from a remote peer containing an IP address in quad format, a callback can be attached to translate it into a 32-bit number. Any user of the deferred can now treat it as a deferred returning a 32-bit number. This, and the related ability to define "errbacks" (callbacks which are called as error handlers), allows code to specify in advance what to do when an asynchronous event occurs, without stopping to wait for the event. In non-event-driven systems, for example using threads, the operating system incurs premature and additional overhead organizing threads each time a blocking call is made.

Thread support
Twisted supports an abstraction over raw threads — using a thread as a deferred source. Thus, a deferred is returned immediately, which will receive a value when the thread finishes. Callbacks can be attached which will run in the main thread, thus alleviating the need for complex locking solutions. A prime example of such usage, which comes from Twisted's support libraries, is using this model to call into databases. The database call itself happens on a foreign thread, but the analysis of the result happens in the main thread.

Foreign loop support
Twisted can integrate with foreign event loops, such as those of GTK+, Qt and Cocoa (through PyObjC). This allows using Twisted as the network layer in graphical user interface (GUI) programs, using all of its libraries without adding a thread-per-socket overhead, as using Python's native library would. A full-fledged web server can be integrated in-process with a GUI program using this model, for example.

Applications using Twisted
The BuildBot continuous-integration system relies on Twisted for client/server communication.
ITA Software has developed an airline-reservation system for Air Canada that uses Twisted extensively.
SageMath, an open-source alternative to Mathematica, Maple, Magma, MATLAB, has a web-based interface, SageMath notebook, that runs on a Twisted server.
Twisted was used in the Omegle one-on-one chat service until it was replaced with gevent for performance reasons.
The Apple Calendar Server uses Twisted, as do some internal projects of NASA.
Conch, an implementation of the Secure Shell (SSH) protocol
The original version of social networking and microblogging site Jaiku used Twisted.
Fluidinfo, an online cloud data-store, uses Twisted extensively for internal RPC (partly in combination with Thrift and AMQP), for its internal services, and for external APIs.
The file-hosting service Ubuntu One used Twisted.
Tor2web, an HTTP proxy for Tor Hidden Services (HS), uses Twisted.
GlobaLeaks, an open-source whistleblowing framework, uses Twisted.
Cloudkick, a cloud-server management web-application, used Twisted. It now has been rewritten using Node.js.
Twilio, a cloud telephony provider, uses Twisted.
Twitch, a video game broadcasting and chat community, uses Twisted.
Velocity Weather, a meteorological data processing and integration API is built on Twisted.
qwebirc, a web-based IRC client, uses Twisted.
Zenoss Core, a network management platform, uses Twisted for many internal and collection daemons.
Scrapy, a web crawler based on Twisted.
Listen to Wikipedia, a Wikipedia audio-visualizer, uses Twisted to broadcast real-time edit events to browsers.
Tahoe-LAFS, a distributed data store and distributed file system.
Deluge, a highly modular BitTorrent client, uses Twisted.
Magic Wormhole, a secure file transfer tool using PAKE.

Nevow
Nevow (pronounced like the French nouveau) is a Python web application framework originally developed by the company Divmod.  Template substitution is achieved via a small Tag Attribute Language, which is usually embedded in on-disk XML templates, though there is also a pure-Python domain-specific language called Stan, for expressing this markup programmatically.  Nevow integrates well with Twisted.
Nevow was deployed on several high-profile web sites, most notably the official Python site.
As of mid-2010, Divmod went out of business, causing development work on Nevow to all but cease, and in 2011 its homepage was no longer accessible. There is a project on Launchpad, hosting the source code of Divmod including the source code of the Nevow project.

Athena
Athena is a Nevow component which facilitates bi-directional, asynchronous communication between the Python and JavaScript portions of a web application in the form of remote procedure calls.  This technique is typically called Ajax or Comet, though Nevow's implementation predates both of these labels.  Athena also includes an inheritance-based JavaScript object system, which forms the basis of a client-side widget abstraction, module system and in-browser unit testing kit.

See also
Application server
Reactor pattern
Perl Object Environment, a comparable framework for the Perl programming language
Netty, for the Java programming language
Node.js, for Javascript
EventMachine, an event-processing library for Ruby
Kivy (framework), a multi-platform GUI framework (including iOS and Android)

References
External links
Official website

## Related Articles

### Internal Links

- [Advanced Message Queuing Protocol](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol)
- [Air Canada](https://en.wikipedia.org/wiki/Air_Canada)
- [Ajax (programming)](https://en.wikipedia.org/wiki/Ajax_(programming))
- [Application server](https://en.wikipedia.org/wiki/Application_server)
- [Asynchronous communication](https://en.wikipedia.org/wiki/Asynchronous_communication)
- [BitTorrent](https://en.wikipedia.org/wiki/BitTorrent)
- [Buildbot](https://en.wikipedia.org/wiki/Buildbot)
- [Callback (computer programming)](https://en.wikipedia.org/wiki/Callback_(computer_programming))
- [Rackspace Technology](https://en.wikipedia.org/wiki/Rackspace_Technology)
- [Cocoa (API)](https://en.wikipedia.org/wiki/Cocoa_(API))
- [Comet (programming)](https://en.wikipedia.org/wiki/Comet_(programming))
- [Computer network programming](https://en.wikipedia.org/wiki/Computer_network_programming)
- [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Deluge (software)](https://en.wikipedia.org/wiki/Deluge_(software))
- [Domain-specific language](https://en.wikipedia.org/wiki/Domain-specific_language)
- [Event-driven programming](https://en.wikipedia.org/wiki/Event-driven_programming)
- [EventMachine](https://en.wikipedia.org/wiki/EventMachine)
- [Exception handling](https://en.wikipedia.org/wiki/Exception_handling)
- [XMPP](https://en.wikipedia.org/wiki/XMPP)
- [File Transfer Protocol](https://en.wikipedia.org/wiki/File_Transfer_Protocol)
- [Fluidinfo](https://en.wikipedia.org/wiki/Fluidinfo)
- [Futures and promises](https://en.wikipedia.org/wiki/Futures_and_promises)
- [GTK](https://en.wikipedia.org/wiki/GTK)
- [Graphical widget](https://en.wikipedia.org/wiki/Graphical_widget)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [GlobaLeaks](https://en.wikipedia.org/wiki/GlobaLeaks)
- [Glyph Lefkowitz](https://en.wikipedia.org/wiki/Glyph_Lefkowitz)
- [Graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface)
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [IP address](https://en.wikipedia.org/wiki/IP_address)
- [IP multicast](https://en.wikipedia.org/wiki/IP_multicast)
- [IRC](https://en.wikipedia.org/wiki/IRC)
- [ITA Software](https://en.wikipedia.org/wiki/ITA_Software)
- [Inheritance (object-oriented programming)](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
- [Internet Message Access Protocol](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol)
- [Jaiku](https://en.wikipedia.org/wiki/Jaiku)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Kivy (framework)](https://en.wikipedia.org/wiki/Kivy_(framework))
- [Launchpad (website)](https://en.wikipedia.org/wiki/Launchpad_(website))
- [Listen to Wikipedia](https://en.wikipedia.org/wiki/Listen_to_Wikipedia)
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [MIT License](https://en.wikipedia.org/wiki/MIT_License)
- [Magma (computer algebra system)](https://en.wikipedia.org/wiki/Magma_(computer_algebra_system))
- [Maple (software)](https://en.wikipedia.org/wiki/Maple_(software))
- [Wolfram Mathematica](https://en.wikipedia.org/wiki/Wolfram_Mathematica)
- [Modular programming](https://en.wikipedia.org/wiki/Modular_programming)
- [NASA](https://en.wikipedia.org/wiki/NASA)
- [Netty (software)](https://en.wikipedia.org/wiki/Netty_(software))
- [Network News Transfer Protocol](https://en.wikipedia.org/wiki/Network_News_Transfer_Protocol)
- [Node.js](https://en.wikipedia.org/wiki/Node.js)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Open Hub](https://en.wikipedia.org/wiki/Open_Hub)
- [Omegle](https://en.wikipedia.org/wiki/Omegle)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Post Office Protocol](https://en.wikipedia.org/wiki/Post_Office_Protocol)
- [Password-authenticated key agreement](https://en.wikipedia.org/wiki/Password-authenticated_key_agreement)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Perl Object Environment](https://en.wikipedia.org/wiki/Perl_Object_Environment)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [PyObjC](https://en.wikipedia.org/wiki/PyObjC)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Qt (software)](https://en.wikipedia.org/wiki/Qt_(software))
- [QuakeNet](https://en.wikipedia.org/wiki/QuakeNet)
- [Reactor pattern](https://en.wikipedia.org/wiki/Reactor_pattern)
- [Remote procedure call](https://en.wikipedia.org/wiki/Remote_procedure_call)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [SageMath](https://en.wikipedia.org/wiki/SageMath)
- [Scrapy](https://en.wikipedia.org/wiki/Scrapy)
- [Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software framework](https://en.wikipedia.org/wiki/Software_framework)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Template Attribute Language](https://en.wikipedia.org/wiki/Template_Attribute_Language)
- [Tahoe-LAFS](https://en.wikipedia.org/wiki/Tahoe-LAFS)
- [Thread (computing)](https://en.wikipedia.org/wiki/Thread_(computing))
- [Apache Thrift](https://en.wikipedia.org/wiki/Apache_Thrift)
- [Tor2web](https://en.wikipedia.org/wiki/Tor2web)
- [Tor (network)](https://en.wikipedia.org/wiki/Tor_(network))
- [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
- [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security)
- [Twilio](https://en.wikipedia.org/wiki/Twilio)
- [Twitch (service)](https://en.wikipedia.org/wiki/Twitch_(service))
- [Ubuntu One](https://en.wikipedia.org/wiki/Ubuntu_One)
- [Unit testing](https://en.wikipedia.org/wiki/Unit_testing)
- [Unix domain socket](https://en.wikipedia.org/wiki/Unix_domain_socket)
- [User Datagram Protocol](https://en.wikipedia.org/wiki/User_Datagram_Protocol)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [Web browser](https://en.wikipedia.org/wiki/Web_browser)
- [Website](https://en.wikipedia.org/wiki/Website)
- [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia)
- [XML](https://en.wikipedia.org/wiki/XML)
- [Zenoss](https://en.wikipedia.org/wiki/Zenoss)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Link rot](https://en.wikipedia.org/wiki/Wikipedia:Link_rot)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from March 2017](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_March_2017)
- [Category:Articles with dead external links from July 2018](https://en.wikipedia.org/wiki/Category:Articles_with_dead_external_links_from_July_2018)
- [Category:Articles with unsourced statements from March 2017](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_March_2017)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:59:00.357459+00:00_