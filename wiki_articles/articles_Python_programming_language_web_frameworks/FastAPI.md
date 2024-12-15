# FastAPI

## Metadata
- **Last Updated:** 2024-12-03 07:57:51 UTC
- **Original Article:** [FastAPI](https://en.wikipedia.org/wiki/FastAPI)
- **Language:** en
- **Page ID:** 65756731

## Summary
FastAPI is a high-performance web framework for building HTTP-based service APIs in Python 3.8+.  It uses Pydantic and type hints to validate, serialize and deserialize data. FastAPI also automatically generates OpenAPI documentation for APIs built with it. It was first released in 2018.

## Categories
This article belongs to the following categories:

- Category:2018 software
- Category:All articles lacking reliable references
- Category:All articles with a promotional tone
- Category:All stub articles
- Category:Articles lacking reliable references from February 2022
- Category:Articles with a promotional tone from February 2022
- Category:Articles with multiple maintenance issues
- Category:Articles with short description
- Category:Python (programming language) web frameworks
- Category:Short description is different from Wikidata
- Category:Software using the MIT license
- Category:Web frameworks
- Category:Web software stubs

## Table of Contents

- Components
- Example
- See also
- External links

## Content

FastAPI is a high-performance web framework for building HTTP-based service APIs in Python 3.8+.  It uses Pydantic and type hints to validate, serialize and deserialize data. FastAPI also automatically generates OpenAPI documentation for APIs built with it. It was first released in 2018.

Components
Pydantic
Pydantic is a data validation library for Python. While writing code in an IDE, Pydantic provides type hints for schema validation and serialization through type annotations.

Starlette
Starlette is a lightweight ASGI framework/toolkit, to support async functionality in Python.

Uvicorn
Uvicorn is a minimal low-level server/application web server for async frameworks, following the ASGI specification. Technically, it implements a multi-process model with one main process, which is responsible for managing a pool of worker processes and distributing incoming HTTP requests to them. The number of worker processes is pre-configured, but can also be adjusted up or down at runtime.

OpenAPI Integration
FastAPI automatically generates OpenAPI documentation for your APIs. This documentation includes both Swagger UI and ReDoc, which provide interactive API documentation that you can use to explore and test your endpoints in real time. This is particularly useful for developing, testing, and sharing APIs with other developers or users.

Example
The following code shows a simple web application that displays "Hello World!" when visited:

See also
Django (web framework)
Flask (web framework)
Pylons project
Web2py
Tornado (web server)
Comparison of server-side web frameworks § Python
REST
Python (programming language)

External links
Official website 
fastapi on GitHub


== References ==

## Archive Info
- **Archived on:** 2024-12-15 20:39:59 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 1708 bytes
- **Word Count:** 245 words
