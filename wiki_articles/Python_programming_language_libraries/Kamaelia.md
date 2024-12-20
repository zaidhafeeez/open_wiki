---
title: Kamaelia
url: https://en.wikipedia.org/wiki/Kamaelia
language: en
categories: ["Category:Articles with short description", "Category:BBC Research & Development", "Category:Free software programmed in Python", "Category:Free system software", "Category:Python (programming language) libraries", "Category:Short description matches Wikidata", "Category:Use dmy dates from April 2022", "Category:Webarchive template wayback links"]
references: 0
last_modified: 2024-12-19T13:57:05Z
---

# Kamaelia

## Summary

Kamaelia is a  free software/open source Python-based systems-development tool and concurrency framework produced by BBC Research & Development.
Kamaelia applications are produced by linking independent components together. These components communicate entirely through "inboxes" and "outboxes" (queues) largely removing the burdens of thread-safety and IPC from the developer. This also makes components reusable in different systems, allows easy unit testing and results in parallelism (between com

## Full Content

Kamaelia is a  free software/open source Python-based systems-development tool and concurrency framework produced by BBC Research & Development.
Kamaelia applications are produced by linking independent components together. These components communicate entirely through "inboxes" and "outboxes" (queues) largely removing the burdens of thread-safety and IPC from the developer. This also makes components reusable in different systems, allows easy unit testing and results in parallelism (between components) by default.
Components are generally implemented as generators - a method more light-weight than allocating a thread to each (though this is also supported). As a result, switching between the execution of components in Kamaelia systems is very fast.
Applications that have been produced using Kamaelia include a Freeview digital video recorder, a network-shared whiteboard, a 3D GUI, an HTTP Server, an audio mixer, a stream multicasting system and a simple BitTorrent client.

License change
Kamaelia's License changed in July 2010  from the Mozilla tri-license (MPL, GPL and LGPL) to the Apache License, with a note that usage under the old licensing scheme was permitted if necessary (due to license incompatibilities), given the rationale for change was to make the codebase more usable by developers not less.

References
External links
Official website