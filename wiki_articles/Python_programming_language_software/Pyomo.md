---
title: Pyomo
url: https://en.wikipedia.org/wiki/Pyomo
language: en
categories: ["Category:Mathematical optimization software", "Category:Python (programming language) software", "Category:Software using the BSD license"]
references: 0
last_modified: 2024-11-27T09:14:41Z
---

# Pyomo

## Summary

Pyomo is a collection of Python software packages for formulating optimization models.
Pyomo was developed by William Hart and Jean-Paul Watson at Sandia National Laboratories and David Woodruff at University of California, Davis.  Significant extensions to Pyomo were developed by Bethany Nicholson and John Siirola at Sandia National Laboratories, Carl Laird at Purdue University, and Gabriel Hackebeil.  Pyomo is an open-source project that is freely available, and it is licensed with the BSD lic

## Full Content

Pyomo is a collection of Python software packages for formulating optimization models.
Pyomo was developed by William Hart and Jean-Paul Watson at Sandia National Laboratories and David Woodruff at University of California, Davis.  Significant extensions to Pyomo were developed by Bethany Nicholson and John Siirola at Sandia National Laboratories, Carl Laird at Purdue University, and Gabriel Hackebeil.  Pyomo is an open-source project that is freely available, and it is licensed with the BSD license.  Pyomo is developed as part of the COIN-OR project.  Pyomo is a popular open-source software package that is used by a variety of government agencies and academic institutions.

Features
Pyomo allows users to formulate optimization problems in Python in a manner that is similar to the notation commonly used in mathematical optimization. Pyomo supports an object-oriented style of formulating optimization models, which are defined with a variety of modeling components:  sets, scalar and multidimensional parameters, decision variables, objectives, constraints, equations, disjunctions and more.  Optimization models can be initialized with python data, and external data sources can be defined using spreadsheets, databases, various formats of text files.  Pyomo supports both abstract models, which are defined without data, and concrete models, which are defined with data.  In both cases, Pyomo allows for the separation of model and data.
Pyomo supports dozens of solvers, both open source and commercial, including many solvers supported by AMPL, PICO, CBC, CPLEX, IPOPT,  and GLPK. Pyomo can either invoke the solver directly or asynchronously with a solver manager.  Solver managers support remote, asynchronous execution of solvers, which supports parallel execution of Pyomo scripts.  Solver interaction is performed with a variety of solver interfaces, depending on the solver being used.  A very generic
solver interface is supported with AMPL's nl (format).

Related software
The following software packages integrate Pyomo as a library to support optimization modeling and analysis:

SolverStudio lets you use Excel to edit, save and solve optimisation models built using a variety of modeling languages, including Pyomo. Pyomo is bundled with the SolverStudio software.
TEMOA (Tools for Energy Model Optimization and Assessment) is an open source modeling framework for conducting energy system analysis. The core component of TEMOA is an energy economy optimization model. This model is formulated and optimized using Pyomo.
MinPower is an open source toolkit for students and researchers in power systems. It is designed to make working with standard power system models simple and intuitive. MinPower uses Pyomo to formulate and optimize these power system models.
linopy project, offering similar functionality to Pyomo.

See also
Algebraic modeling language

References
External links
Articles from IBM's developerWorks:
Gift, Noah (5 February 2013). "Linear optimization in Python, Part 1: Solve complex problems in the cloud with Pyomo".
Linear optimization in Python, Part 2: Build a scalable architecture in the cloud
"Pyomo Meets Fantasy Football". 2015-01-27.
APOPT Solver for LP, QP, MILP, NLP, and MINLP solutions in Pyomo
