# Twisted (software)

## Metadata
- **Last Updated:** 2024-12-06 10:32:58 UTC
- **Original Article:** [Twisted (software)](https://en.wikipedia.org/wiki/Twisted_(software))
- **Language:** en
- **Page ID:** 1793652

## Summary
Twisted is an event-driven network programming framework written in Python and licensed under the MIT License.
Twisted projects variously support TCP, UDP, SSL/TLS, IP multicast, Unix domain sockets, many protocols (including HTTP, XMPP, NNTP, IMAP, SSH, IRC, FTP, and others), and much more. Twisted is based on the event-driven programming paradigm, which means that users of Twisted write short callbacks which are called by the framework.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 21:07:46 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 7125 bytes
- **Word Count:** 1081 words
