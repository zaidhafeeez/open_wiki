---
title: LibSBML
url: https://en.wikipedia.org/wiki/LibSBML
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:C++ libraries", "Category:CS1 maint: DOI inactive as of December 2024", "Category:Cross-platform free software", "Category:Free computer libraries", "Category:Free science software", "Category:Free software programmed in C++", "Category:Short description is different from Wikidata", "Category:Software using the LGPL license"]
references: 0
last_modified: 2024-12-19T14:32:35Z
---

# LibSBML

## Summary

LibSBML is an open-source software library that provides an application programming interface (API) for the SBML (Systems Biology Markup Language ) format. The libSBML library can be embedded in a software application or used in a web servlet (such as one that might be served by Apache Tomcat) as part of the application or servlet's implementation of support for reading, writing, and manipulating SBML documents and data streams. The core of libSBML is written in ISO standard C++; the library pro

## Full Content

LibSBML is an open-source software library that provides an application programming interface (API) for the SBML (Systems Biology Markup Language ) format. The libSBML library can be embedded in a software application or used in a web servlet (such as one that might be served by Apache Tomcat) as part of the application or servlet's implementation of support for reading, writing, and manipulating SBML documents and data streams. The core of libSBML is written in ISO standard C++; the library provides API for many programming languages via interfaces generated with the help of SWIG.
The libSBML library is free software released under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or any later version.  LibSBML was developed thanks to funding from many agencies, particularly the National Institute of General Medical Sciences (NIGMS, USA) as well as the Defense Advanced Research Projects Agency (DARPA, USA) under the Bio-SPICE program.

Description
The Systems Biology Markup Language (SBML) is an XML-based format for encoding computational models of a sort common in systems biology.  Although SBML is based upon XML, and thus software developers could support SBML using off-the-shelf XML parser libraries, libSBML offers numerous advantages that make it easier for developers to implement support for SBML in their software.  The premise behind the development of libSBML is that it is more convenient and efficient for developers to start with a higher-level API tailored specifically to SBML and its distinctive features than it is to start with a plain XML parser library.

Significant features of libSBML
The following is a partial list of libSBML's features:

Supports all Levels and Versions of SBML with common API classes and methods, thus smoothing the differences between different flavors of SBML from the perspective of the application software.
Provides facilities for manipulating mathematical formulas in both text-string format and MathML 2.0 format, as well as the ability to interconvert mathematical expressions between these forms.  Internally, libSBML uses familiar Abstract Syntax Trees (ASTs) to represent formulas, and provides AST-oriented methods for calling applications.
Performs validation of XML and SBML at the time of parsing files and data streams.  This helps verify the correctness of models in a way that goes beyond simple syntactic validation.
Offers support for dimensional analysis and unit checking.  LibSBML implements a thorough system for dimensional analysis and checking units of quantities in a model.
Provides facilities for the creation and manipulation of SBML annotations and notes.  These have a specific format dictated by the SBML specifications.  The formats and standards supported by libSBML include MIRIAM (Minimal Information Requested in the Annotation of a Model) and SBO (the Systems Biology Ontology).
Supports transparently reading and writing compressed files in the ZIP, GZIP and BZIP formats.
Provides interfaces for the C, C++, C#, Java, Python, Perl, MATLAB, Octave, and Ruby programming languages.  The C and C++ interfaces are implemented natively; the C#, Java, Perl, Python, and Ruby interfaces are implemented using SWIG, the Simplified Wrapper Interface Generator; and the MATLAB and Octave interfaces are implemented through custom hand-written code.
Provides many convenience methods, such as for obtaining a count of the number of boundary condition species, determining the modifier species of a reaction (assuming the reaction provides kinetics), constructing the stoichiometric matrix for all reactions in a model, and more.

Manipulation of mathematical formulas
Some further explanations may be warranted concerning libSBML's support for working with mathematical formulas.  In SBML Level 1, mathematical formulas are represented as text strings using a C-like syntax.  This representation was chosen because of its simplicity, widespread familiarity and use in applications such as GEPASI and Jarnac, whose authors contributed to the initial design of SBML.  In SBML Levels 2 and 3, there was a need to expand the mathematical vocabulary of Level 1 to include additional functions (both built-in and user-defined), mathematical constants, logical operators, relational operators and a special symbol to represent time.  Rather than growing the simple C-like syntax into something more complicated and esoteric in order to support these features, and consequently having to manage two standards in two different formats (XML and text string formulas), SBML Levels 2 and 3 leverage an existing standard for expressing mathematical formulas, namely the content portion of MathML.
As mentioned above, LibSBML provides an abstraction for working with mathematical expressions in both text-string and MathML form: Abstract Syntax Trees (ASTs).  Abstract Syntax Trees are well known in the computer science community; they are simple recursive data structures useful for representing the syntactic structure of sentences in certain kinds of languages (mathematical or otherwise).  Much as libSBML allows programmers to manipulate SBML at the level of domain-specific objects, regardless of SBML Level or version, it also allows programmers to work with mathematical formula at the level of ASTs regardless of whether the original format was C-like infix or MathML.  LibSBML goes one step further by allowing programmers to work exclusively with infix formula strings and instantly convert them to the appropriate MathML whenever needed.

Dependencies
LibSBML requires a separate library to do low-level read/write operations on XML.  It can use any one of three XML parser libraries: Xerces, expat or libxml2.  Users can specify which library they wish to use at libSBML compilation time.   LibSBML hides the differences between these parser libraries behind an abstraction layer; it seamlessly uses whichever library against which a given instance of libSBML has been compiled. (However, released binary distributions of libSBML all make use of the libxml2 library.)

Usage
LibSBML uses software objects (i.e., instances of classes) that correspond to SBML components, with member variables representing the attributes of the corresponding SBML objects.  The libSBML API is constructed to provide an intuitive way of relating SBML and the code needed to create or manipulate it with a class hierarchy that mimics the SBML structure.  More information about the libSBML objects is available in the libSBML API documentation.

Reading and writing SBML
LibSBML enables reading from and writing to either files or strings. Once an SBML document is read, libSBML stores the SBML content in an SBMLDocument object.  This object can be written out again later. The following is an example written in Python:

Creating and manipulating SBML
The libSBML API allows easy creation of objects and subobjects representing SBML elements and the subelements contained within them.  The following is an example written in C++:

Accessing attributes
Each component in SBML has a number of attributes associated with it. These are stored as member variables of a given class, and libSBML provides functions to retrieve and query these values. The syntax of these functions is consistent throughout libSBML. The following is an example written in Python:

See also
JSBML
libxml2
Xerces
Expat
XML validation
XML
BioModels Database
BioPAX
CellML
MIASE
MIRIAM
Systems Biology Ontology (SBO)
MathML

References
External links
libSBML Home Page