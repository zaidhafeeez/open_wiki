---
title: Asynchronous Server Gateway Interface
url: https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface
language: en
categories: ["Category:All articles with topics of unclear notability", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Articles with topics of unclear notability from December 2023", "Category:Free software programmed in Python", "Category:Python (programming language)", "Category:Short description matches Wikidata"]
references: 0
last_modified: 2024-12-19T15:02:40Z
---

# Asynchronous Server Gateway Interface

## Summary

The Asynchronous Server Gateway Interface (ASGI) is a calling convention for web servers to forward requests to asynchronous-capable Python frameworks, and applications. It is built as a successor to the Web Server Gateway Interface (WSGI).
Where WSGI provided a standard for synchronous Python application, ASGI provides one for both asynchronous and synchronous applications, with a WSGI backwards-compatibility implementation and multiple servers and application frameworks.

## Full Content

The Asynchronous Server Gateway Interface (ASGI) is a calling convention for web servers to forward requests to asynchronous-capable Python frameworks, and applications. It is built as a successor to the Web Server Gateway Interface (WSGI).
Where WSGI provided a standard for synchronous Python application, ASGI provides one for both asynchronous and synchronous applications, with a WSGI backwards-compatibility implementation and multiple servers and application frameworks.

Example
An ASGI-compatible "Hello, World!" application written in Python:Where:
Line 1 defines an asynchronous function named application, which takes three parameters (unlike in WSGI which takes only two), scope, receive and send.
scope is a dict containing details about current connection, like the protocol, headers, etc.
receive and send are asynchronous callables which let the application receive and send messages from/to the client.
Line 2 receives an incoming event, for example, HTTP request or WebSocket message. The await keyword is used because the operation is asynchronous.
Line 4 asynchronously sends a response back to the client. In this case, it is a WebSocket communication.

Web Server Gateway Interface (WSGI) compatibility
ASGI is also designed to be a superset of WSGI, and there's a defined way of translating between the two, allowing WSGI applications to be run inside ASGI servers through a translation wrapper (provided in the asgiref library). A threadpool can be used to run the synchronous WSGI applications away from the async event loop.

See also
Comparison of web frameworks
FastCGI
Python (programming language)
 Web Server Gateway Interface (WSGI)

References
External links
Asynchronous Server Gateway Interface Documentation
Asynchronous Server Gateway Interface Specification