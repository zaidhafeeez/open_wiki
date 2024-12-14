# Inner loop

## Article Metadata

- **Last Updated:** 2024-12-14T19:38:55.595935+00:00
- **Original Article:** [Inner loop](https://en.wikipedia.org/wiki/Inner_loop)
- **Language:** en
- **Page ID:** 1819659

## Summary

In computer programs, an important form of control flow is the loop which causes a block of code to be executed more than once. A common idiom is to have a loop nested inside another loop, with the contained loop being commonly referred to as the inner loop.

## Categories

- Category:All articles needing additional references
- Category:All stub articles
- Category:Articles needing additional references from September 2018
- Category:Articles with example Python (programming language) code
- Category:Computer programming stubs
- Category:Control flow
- Category:Software optimization

## Table of Contents

- Background
- References

## Content

In computer programs, an important form of control flow is the loop which causes a block of code to be executed more than once. A common idiom is to have a loop nested inside another loop, with the contained loop being commonly referred to as the inner loop.

Background
In many languages there are two main types of loop exist, and they can be nested within each other in multiple layers of nesting. The two types are for loop and while loop. They are slightly different in form but have the same effect. Research has shown that performance of the complete structure of a loop with an inner loop is different when compared with a loop without an inner loop. Indeed, even the performance of two loops with different types of inner loop, where one is a for loop and the other a while loop, are different.
It was observed that more computations are performed per unit time when an inner for loop is involved than otherwise. This implies, given the same number of computations to perform, the one with an inner for loop will finish faster than the one without it. This is a machine- or platform-independent technique of loop optimization and was observed across several programming languages and compilers or interpreters tested. The case of a while loop as the inner loop performed badly, performing even slower than a loop without any inner loop in some cases. Two examples below written in python present a while loop with an inner for loop and a while loop without any inner loop. Although both have the same terminating condition for their while loops, the first example will finish faster because of the inner for loop. The variable innermax is a fraction of the maxticketno variable in the first example.

References
4. Python Nested For Loop From Techgeekbuz

## Related Articles

### Internal Links

- [Computer program](https://en.wikipedia.org/wiki/Computer_program)
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [Control flow](https://en.wikipedia.org/wiki/Control_flow)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Inner loop (disambiguation)](https://en.wikipedia.org/wiki/Inner_loop_(disambiguation))
- [Control flow](https://en.wikipedia.org/wiki/Control_flow)
- [Loop optimization](https://en.wikipedia.org/wiki/Loop_optimization)
- [Control flow](https://en.wikipedia.org/wiki/Control_flow)
- [Wikipedia:Stub](https://en.wikipedia.org/wiki/Wikipedia:Stub)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Compu-prog-stub](https://en.wikipedia.org/wiki/Template:Compu-prog-stub)
- [Template talk:Compu-prog-stub](https://en.wikipedia.org/wiki/Template_talk:Compu-prog-stub)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from September 2018](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_September_2018)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:38:55.595935+00:00_