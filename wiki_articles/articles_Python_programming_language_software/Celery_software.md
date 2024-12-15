# Celery (software)

## Article Metadata

- **Last Updated:** 2024-12-15T03:25:42.166622+00:00
- **Original Article:** [Celery (software)](https://en.wikipedia.org/wiki/Celery_(software))
- **Language:** en
- **Page ID:** 36164746

## Summary

Celery is an open source asynchronous task queue or job queue which is based on distributed message passing. While it supports scheduling, its focus is on operations in real time.

## Categories

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

## Related Articles

### Internal Links

- [Advanced Message Queuing Protocol](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol)
- [Amazon Simple Queue Service](https://en.wikipedia.org/wiki/Amazon_Simple_Queue_Service)
- [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses)
- [Computing platform](https://en.wikipedia.org/wiki/Computing_platform)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Instagram](https://en.wikipedia.org/wiki/Instagram)
- [Message-oriented middleware](https://en.wikipedia.org/wiki/Message-oriented_middleware)
- [Message broker](https://en.wikipedia.org/wiki/Message_broker)
- [Multiprocessing](https://en.wikipedia.org/wiki/Multiprocessing)
- [Node.js](https://en.wikipedia.org/wiki/Node.js)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [RabbitMQ](https://en.wikipedia.org/wiki/RabbitMQ)
- [Redis](https://en.wikipedia.org/wiki/Redis)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Scheduling (computing)](https://en.wikipedia.org/wiki/Scheduling_(computing))
- [Webhook](https://en.wikipedia.org/wiki/Webhook)
- [Wikipedia:Link rot](https://en.wikipedia.org/wiki/Wikipedia:Link_rot)
- [Wikipedia:No original research](https://en.wikipedia.org/wiki/Wikipedia:No_original_research)
- [Wikipedia:Stub](https://en.wikipedia.org/wiki/Wikipedia:Stub)
- [Template:Free-software-stub](https://en.wikipedia.org/wiki/Template:Free-software-stub)
- [Template talk:Free-software-stub](https://en.wikipedia.org/wiki/Template_talk:Free-software-stub)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles lacking reliable references from July 2024](https://en.wikipedia.org/wiki/Category:Articles_lacking_reliable_references_from_July_2024)
- [Category:Articles with dead external links from November 2019](https://en.wikipedia.org/wiki/Category:Articles_with_dead_external_links_from_November_2019)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:25:42.166622+00:00_