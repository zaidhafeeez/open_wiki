---
title: SimPy
url: https://en.wikipedia.org/wiki/SimPy
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Cross-platform software", "Category:Free science software", "Category:Python (programming language) libraries", "Category:Short description matches Wikidata", "Category:Simulation programming languages"]
references: 0
last_modified: 2024-12-19T13:43:23Z
---

# SimPy

## Summary

SimPy stands for “Simulation in Python”, is a process-based discrete-event simulation framework based on standard Python. It enables users to model active components such as customers, vehicles, or agents as simple Python generator functions. SimPy is released as open source software under the MIT License. The first version was released in December 2002.

## Full Content

SimPy stands for “Simulation in Python”, is a process-based discrete-event simulation framework based on standard Python. It enables users to model active components such as customers, vehicles, or agents as simple Python generator functions. SimPy is released as open source software under the MIT License. The first version was released in December 2002.

Overview
Its event dispatcher is based on Python's generators and can be used for asynchronous networking or to implement multi-agent systems (with both, simulated and real communication). Simulations can be performed “as fast as possible”, in real time (wall clock time) or by manually stepping through the events. Though it is theoretically possible to do continuous simulations with SimPy, it lacks features to support them. However, for simulations with a fixed step size where processes don't interact with each other or with shared resources, a simple while loop is sufficient.
Additionally, SimPy provides different types of shared resources to simulate congestion points that have limited capacity, such as servers, checkout counters, and tunnels. In version 3.1 and above, SimPy offers monitoring capabilities to assist in collecting statistics about processes and resources.
SimPy 3.0 requires Python 3., while SimPy 4.0 requires Python 3.6+. SimPy distribution contains tutorials, documentation, and examples.

Example
The following is a SimPy simulation  showing a clock process that prints the current simulation time at each step:


== References ==
