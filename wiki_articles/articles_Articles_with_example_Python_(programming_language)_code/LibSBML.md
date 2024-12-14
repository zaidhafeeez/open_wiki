# LibSBML

## Article Metadata

- **Last Updated:** 2024-12-14T19:39:46.306058+00:00
- **Original Article:** [LibSBML](https://en.wikipedia.org/wiki/LibSBML)
- **Language:** en
- **Page ID:** 36121017

## Summary

LibSBML is an open-source software library that provides an application programming interface (API) for the SBML (Systems Biology Markup Language ) format. The libSBML library can be embedded in a software application or used in a web servlet (such as one that might be served by Apache Tomcat) as part of the application or servlet's implementation of support for reading, writing, and manipulating SBML documents and data streams. The core of libSBML is written in ISO standard C++; the library pro

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:C++ libraries
- Category:CS1 maint: DOI inactive as of December 2024
- Category:Cross-platform free software
- Category:Free computer libraries
- Category:Free science software
- Category:Free software programmed in C++
- Category:Short description is different from Wikidata
- Category:Software using the LGPL license

## Table of Contents

- Description
- Usage
- See also
- References
- External links

## Content

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

## Related Articles

### Internal Links

- [Abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
- [Apache Tomcat](https://en.wikipedia.org/wiki/Apache_Tomcat)
- [Apache Xerces](https://en.wikipedia.org/wiki/Apache_Xerces)
- [API](https://en.wikipedia.org/wiki/API)
- [BZIP domain](https://en.wikipedia.org/wiki/BZIP_domain)
- [BioModels](https://en.wikipedia.org/wiki/BioModels)
- [BioPAX](https://en.wikipedia.org/wiki/BioPAX)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [COPASI](https://en.wikipedia.org/wiki/COPASI)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [CellML](https://en.wikipedia.org/wiki/CellML)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Class (computer programming)](https://en.wikipedia.org/wiki/Class_(computer_programming))
- [Computational model](https://en.wikipedia.org/wiki/Computational_model)
- [DARPA](https://en.wikipedia.org/wiki/DARPA)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Expat (software)](https://en.wikipedia.org/wiki/Expat_(software))
- [Free Software Foundation](https://en.wikipedia.org/wiki/Free_Software_Foundation)
- [Free software](https://en.wikipedia.org/wiki/Free_software)
- [Gzip](https://en.wikipedia.org/wiki/Gzip)
- [Hiroaki Kitano](https://en.wikipedia.org/wiki/Hiroaki_Kitano)
- [JSBML](https://en.wikipedia.org/wiki/JSBML)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [GNU Lesser General Public License](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)
- [Library (computing)](https://en.wikipedia.org/wiki/Library_(computing))
- [Libxml2](https://en.wikipedia.org/wiki/Libxml2)
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [Minimum information about a simulation experiment](https://en.wikipedia.org/wiki/Minimum_information_about_a_simulation_experiment)
- [Minimum information required in the annotation of models](https://en.wikipedia.org/wiki/Minimum_information_required_in_the_annotation_of_models)
- [Mac operating systems](https://en.wikipedia.org/wiki/Mac_operating_systems)
- [MathML](https://en.wikipedia.org/wiki/MathML)
- [Member variable](https://en.wikipedia.org/wiki/Member_variable)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [National Institute of General Medical Sciences](https://en.wikipedia.org/wiki/National_Institute_of_General_Medical_Sciences)
- [GNU Octave](https://en.wikipedia.org/wiki/GNU_Octave)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [PubMed](https://en.wikipedia.org/wiki/PubMed)
- [Pedro Mendes (scientist)](https://en.wikipedia.org/wiki/Pedro_Mendes_(scientist))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [SBML](https://en.wikipedia.org/wiki/SBML)
- [SWIG](https://en.wikipedia.org/wiki/SWIG)
- [Jakarta Servlet](https://en.wikipedia.org/wiki/Jakarta_Servlet)
- [Application software](https://en.wikipedia.org/wiki/Application_software)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Library (computing)](https://en.wikipedia.org/wiki/Library_(computing))
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Systems Biology Ontology](https://en.wikipedia.org/wiki/Systems_Biology_Ontology)
- [Systems biology](https://en.wikipedia.org/wiki/Systems_biology)
- [Unix-like](https://en.wikipedia.org/wiki/Unix-like)
- [XML](https://en.wikipedia.org/wiki/XML)
- [XML validation](https://en.wikipedia.org/wiki/XML_validation)
- [ZIP (file format)](https://en.wikipedia.org/wiki/ZIP_(file_format))
- [Template:Cite journal](https://en.wikipedia.org/wiki/Template:Cite_journal)
- [Category:CS1 maint: DOI inactive as of December 2024](https://en.wikipedia.org/wiki/Category:CS1_maint:_DOI_inactive_as_of_December_2024)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:39:46.306058+00:00_