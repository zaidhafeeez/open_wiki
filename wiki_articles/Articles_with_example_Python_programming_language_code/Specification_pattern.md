---
title: Specification pattern
url: https://en.wikipedia.org/wiki/Specification_pattern
language: en
categories: ["Category:Architectural pattern (computer science)", "Category:Articles with example C++ code", "Category:Articles with example C Sharp code", "Category:Articles with example JavaScript code", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Programming language comparisons", "Category:Short description is different from Wikidata", "Category:Software design patterns"]
references: 0
last_modified: 2024-12-19T14:04:34Z
---

# Specification pattern

## Summary

In computer programming, the specification pattern is a particular software design pattern, whereby business rules can be recombined by chaining the business rules together using boolean logic. The pattern is frequently used in the context of domain-driven design.
A specification pattern outlines a business rule that is combinable with other business rules. In this pattern, a unit of business logic inherits its functionality from the abstract aggregate Composite Specification class. The Composit

## Full Content

In computer programming, the specification pattern is a particular software design pattern, whereby business rules can be recombined by chaining the business rules together using boolean logic. The pattern is frequently used in the context of domain-driven design.
A specification pattern outlines a business rule that is combinable with other business rules. In this pattern, a unit of business logic inherits its functionality from the abstract aggregate Composite Specification class. The Composite Specification class has one function called IsSatisfiedBy that returns a boolean value. After instantiation, the specification is "chained" with other specifications, making new specifications easily maintainable, yet highly customizable business logic. Furthermore, upon instantiation the business logic may, through method invocation or inversion of control, have its state altered in order to become a delegate of other classes such as a persistence repository.
As a consequence of performing runtime composition of high-level business/domain logic, the Specification pattern is a convenient tool for converting ad-hoc user search criteria into low level logic to be processed by repositories.
Since a specification is an encapsulation of logic in a reusable form it is very simple to thoroughly unit test, and when used in this context is also an implementation of the humble object pattern.

Code examples
C#
C# 6.0 with generics
Python
C++
TypeScript
Example of use
In the next example, invoices are retrieved and sent to a collection agency if:

they are overdue,
notices have been sent, and
they are not already with the collection agency.
This example is meant to show the result of how the logic is 'chained' together.
This usage example assumes a previously defined OverdueSpecification class that is satisfied when an invoice's due date is 30 days or older, a NoticeSentSpecification class that is satisfied when three notices have been sent to the customer, and an InCollectionSpecification class that is satisfied when an invoice has already been sent to the collection agency. The implementation of these classes isn't important here.
Using these three specifications, we created a new specification called SendToCollection which will be satisfied when an invoice is overdue, when notices have been sent to the customer, and are not already with the collection agency.

References
Evans, Eric (2004). Domain Driven Design. Addison-Wesley. p. 224.

External links
Specifications by Eric Evans and Martin Fowler
The Specification Pattern: A Primer by Matt Berther
The Specification Pattern: A Four Part Introduction using VB.Net  by Richard Dalton
The Specification Pattern in PHP by Moshe Brevda
Happyr Doctrine Specification in PHP by Happyr
The Specification Pattern in Swift by Simon Strandgaard
The Specification Pattern in TypeScript and JavaScript by Thiago Delgado Pinto
specification pattern in flash actionscript 3 by Rolf Vreijdenberger
