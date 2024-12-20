---
title: Macroprogramming
url: https://en.wikipedia.org/wiki/Macroprogramming
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Articles with example Scala code", "Category:Articles with short description", "Category:Distributed computing", "Category:Programming languages", "Category:Programming paradigms", "Category:Short description with empty Wikidata description"]
references: 0
last_modified: 2024-12-19T15:05:18Z
---

# Macroprogramming

## Summary

In computer science, macroprogramming is a programming paradigm 
aimed at expressing the macroscopic, global behaviour of an entire system of agents or computing devices.
In macroprogramming, the local programs for the individual components of a distributed system are compiled or interpreted from a macro-program typically expressed by a system-level perspective or in terms of the intended global goal.
The aim of macroprogramming approaches is to support expressing the macroscopic interactive beh

## Full Content

In computer science, macroprogramming is a programming paradigm 
aimed at expressing the macroscopic, global behaviour of an entire system of agents or computing devices.
In macroprogramming, the local programs for the individual components of a distributed system are compiled or interpreted from a macro-program typically expressed by a system-level perspective or in terms of the intended global goal.
The aim of macroprogramming approaches is to support expressing the macroscopic interactive behaviour of a whole distributed system of computing devices or agents in a single program, or, similarly, to promote their collective intelligence.
It has not to be confused with macros, the mechanism often found in programming languages (like C or Scala) to express substitution rules for program pieces.
Macroprogramming originated in the context of wireless sensor network programming
and found renewed interest in the context of the Internet of Things and swarm robotics.
Macroprogramming shares similar goals (related to  programming a system by a global perspective) with multitier programming, choreographic programming, and aggregate computing.

Context and motivation
Programming distributed systems, multi-agent systems, and collectives of software agents (e.g., robotic swarms) is difficult, for many issues (like communication, concurrency, and failure) have to be properly considered. In particular, a general recurrent problem is how to induce the intended global behaviour by defining the behaviour of the individual components or agents involved. The problem can be addressed through learning approaches, such as multi-agent reinforcement learning, or by manually defining the control program driving each component. However, addressing the problem by a fully individual (or single-node) perspective may be error-prone, because it is generally difficult to foresee the overall behaviour emerging from complex networks of activities and interactions (cf. complex systems and emergence). Therefore, researchers have started investigated ways to raise the abstraction level, promoting programming of distributed systems by a more global perspective or in terms of the overall goal to be collectively attained.

Examples
ScaFi
The following program in the ScaFi aggregate programming language  [1] defines the loop control logic needed to compute a channel (a Boolean field where the devices yielding true are those connecting, through a hop-by-hop path, a source device to a target device)  across a large set of situated devices interacting with neighbours.

What is interesting to note is that the channel function, as well as the functions that are used to implement it, namely distanceTo, distanceBetween, dilate, broadcast etc.
can be interpreted not just in terms of the individual behaviour of a device, but rather by a macroscopic perspective.
In fact, for instance, distanceTo(s) is used to compute the field of minimum distances from the closest device for which expression s yields true: this is effectively a distributed data structure that is sustained through processing and communication with neighbours, in a self-organising way.
Semantically, such functions define  a macro-level (or collective) behaviour that yields a macro-level (or collective) data structure. Such macro-level functions/behaviours can be composed together to obtain another more complex macro-level function/behaviours.

Regiment
The following program in the Regiment language  can be used to compute the mean temperature perceived by the whole system:

PyoT
The following program in PyoT  can be used to turn on a fan if the mean temperature computed by several sensors exceeds a certain threshold.

TinyDB
In TinyDB, a data-oriented macroprogramming approach is used where the programmer writes a query which turns into single-node operations and routing in a wireless sensor network.

See also
Multitier programming
Choreographic programming
Aggregate computing
Distributed computing


== References ==
