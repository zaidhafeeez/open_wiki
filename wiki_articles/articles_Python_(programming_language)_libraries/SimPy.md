# SimPy

## Article Metadata

- **Last Updated:** 2024-12-14T19:52:21.381739+00:00
- **Original Article:** [SimPy](https://en.wikipedia.org/wiki/SimPy)
- **Language:** en
- **Page ID:** 196372

## Summary

SimPy stands for “Simulation in Python”, is a process-based discrete-event simulation framework based on standard Python. It enables users to model active components such as customers, vehicles, or agents as simple Python generator functions. SimPy is released as open source software under the MIT License. The first version was released in December 2002.

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Cross-platform software
- Category:Free science software
- Category:Python (programming language) libraries
- Category:Short description matches Wikidata
- Category:Simulation programming languages

## Table of Contents

- Overview
- Example

## Content

SimPy stands for “Simulation in Python”, is a process-based discrete-event simulation framework based on standard Python. It enables users to model active components such as customers, vehicles, or agents as simple Python generator functions. SimPy is released as open source software under the MIT License. The first version was released in December 2002.

Overview
Its event dispatcher is based on Python's generators and can be used for asynchronous networking or to implement multi-agent systems (with both, simulated and real communication). Simulations can be performed “as fast as possible”, in real time (wall clock time) or by manually stepping through the events. Though it is theoretically possible to do continuous simulations with SimPy, it lacks features to support them. However, for simulations with a fixed step size where processes don't interact with each other or with shared resources, a simple while loop is sufficient.
Additionally, SimPy provides different types of shared resources to simulate congestion points that have limited capacity, such as servers, checkout counters, and tunnels. In version 3.1 and above, SimPy offers monitoring capabilities to assist in collecting statistics about processes and resources.
SimPy 3.0 requires Python 3., while SimPy 4.0 requires Python 3.6+. SimPy distribution contains tutorials, documentation, and examples.

Example
The following is a SimPy simulation  showing a clock process that prints the current simulation time at each step:


== References ==

## Related Articles

### Internal Links

- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Discrete-event simulation](https://en.wikipedia.org/wiki/Discrete-event_simulation)
- [Discrete-event simulation](https://en.wikipedia.org/wiki/Discrete-event_simulation)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Generator (computer programming)](https://en.wikipedia.org/wiki/Generator_(computer_programming))
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Massachusetts Institute of Technology](https://en.wikipedia.org/wiki/Massachusetts_Institute_of_Technology)
- [MIT License](https://en.wikipedia.org/wiki/MIT_License)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Simpy](https://en.wikipedia.org/wiki/Simpy)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software framework](https://en.wikipedia.org/wiki/Software_framework)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [SymPy](https://en.wikipedia.org/wiki/SymPy)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:52:21.381739+00:00_