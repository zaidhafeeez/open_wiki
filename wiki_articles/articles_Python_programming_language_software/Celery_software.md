# Celery (software)

## Metadata
- **Last Updated:** 2024-12-06 06:16:01 UTC
- **Original Article:** [Celery (software)](https://en.wikipedia.org/wiki/Celery_(software))
- **Language:** en
- **Page ID:** 36164746

## Summary
Celery is an open source asynchronous task queue or job queue which is based on distributed message passing. While it supports scheduling, its focus is on operations in real time.

## Categories
This article belongs to the following categories:

- Category:All articles with dead external links
- Category:All stub articles
- Category:Articles lacking reliable references from July 2024
- Category:Articles with dead external links from November 2019
- Category:Articles with permanently dead external links
- Category:Articles with short description
- Category:Concurrent programming libraries
- Category:Free and open-source software stubs
- Category:Free software programmed in Python
- Category:Free system software
- Category:Inter-process communication
- Category:Message-oriented middleware
- Category:Official website different in Wikidata and Wikipedia
- Category:Python (programming language) software
- Category:Short description matches Wikidata
- Category:Software using the BSD license

## Table of Contents

- Overview
- Technology
- See also
- References
- External links

## Content

Celery is an open source asynchronous task queue or job queue which is based on distributed message passing. While it supports scheduling, its focus is on operations in real time.

Overview
The execution units, called tasks, are executed concurrently on one or more worker nodes using multiprocessing, eventlet or gevent. Tasks can execute asynchronously (in the background) or synchronously (wait until ready). Celery is used in production systems, for services such as Instagram, to process millions of tasks every day.

Technology
Celery is written in Python, but the protocol can be implemented in any language. It can also operate with other languages using webhooks. There is also a Ruby-Client called RCelery, a PHP client, a Go client, a Rust client, and a Node.js client.
Celery requires a message broker to run. As of October 2024, Redis and RabbitMQ are supported and actively maintained and monitored. Amazon SQS is supported and maintained but does not support worker inspection and management at runtime, while Zookeeper and Kafka are currently in experimental development.

See also
Advanced Message Queuing Protocol

References
External links
Official website
celery on GitHub

## Archive Info
- **Archived on:** 2024-12-15 20:39:37 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 1192 bytes
- **Word Count:** 184 words
