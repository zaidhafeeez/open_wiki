# SimpleITK

## Article Metadata

- **Last Updated:** 2024-12-14T19:45:00.473485+00:00
- **Original Article:** [SimpleITK](https://en.wikipedia.org/wiki/SimpleITK)
- **Language:** en
- **Page ID:** 57078264

## Summary

SimpleITK is a simplified, open-source interface to the Insight Segmentation and Registration Toolkit (ITK). The SimpleITK image analysis library is available in multiple programming languages including C++, Python, R, Java, C#, Lua, Ruby and Tcl. Binary distributions are available for all three major operating systems (Linux, macOS and Microsoft Windows).
Developed at the National Institutes of Health (NIH) as an open resource, its primary goal is to make the algorithms available in the ITK lib

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with short description
- Category:Image processing software
- Category:Python (programming language) libraries
- Category:R (programming language)
- Category:Short description matches Wikidata

## Table of Contents

- History
- Examples
- References
- External links

## Content

SimpleITK is a simplified, open-source interface to the Insight Segmentation and Registration Toolkit (ITK). The SimpleITK image analysis library is available in multiple programming languages including C++, Python, R, Java, C#, Lua, Ruby and Tcl. Binary distributions are available for all three major operating systems (Linux, macOS and Microsoft Windows).
Developed at the National Institutes of Health (NIH) as an open resource, its primary goal is to make the algorithms available in the ITK library accessible to the broadest range of scientists whose work includes image analysis, irrespective of their software development skills. 
As a consequence, the SimpleITK interface exposes only the most commonly modified algorithmic settings of the ITK components. Additionally, the library provides both an object oriented and a procedural interface to most of the image processing filters. The latter enables image analysis workflows with concise syntax. A secondary goal of the library is to promote reproducible image analysis workflows by using the SimpleITK library in conjunction with modern tools for reproducible computational workflows available in the Python (Jupyter notebooks) and R (knitr package ) programming languages.
Software development is centered on GitHub using a fork and pull model. The project is built using the CMake tool, with nightly builds posted to the project's quality dashboard.
Multiple medical image analysis applications and libraries incorporate SimpleITK as a key building block, as it provides a wide range of image filtering and image IO components with a user friendly interface. Examples include the pyOsirix scripting tool for the popular Osirix application, the pyradiomics python package for extracting radiomic features from medical imaging, the 3DSlicer image analysis application,  the SimpleElastix medical image registration library, and the NiftyNet deep learning library for medical imaging.

History
The initial development of SimpleITK was funded by the United States National Library of Medicine under the American Recovery and Reinvestment Act (ARRA) program as a collaboration between The Mayo Clinic, Kitware Inc, The University of Iowa and NLM's intramural program. The first major release of the toolkit was announced in April-May 2017. The second major release was announced in September 2020.
Between 2013 and 2019, SimpleITK development was primarily carried out as part of the intramural research program of the National Library of Medicine with collaborators at The University of Iowa and Monash University. Since 2019, SimpleITK development is primarily carried out under the Office of Cyber Infrastructure and Computational Biology at the National Institute of Allergy and Infectious Diseases. In April 2020 the toolkit changed its logo to a more modern design.

Examples
Gaussian smoothing
Short Python scripts illustrating image reading, blurring, and writing. Using the object oriented interface:

A more concise version using the procedural interface:

Multi-modality Rigid Registration
Short R script illustrating the use of the library's registration framework for rigid registration
of two 3D images:

References
External links
Official website.
SimpleITK: A Simplified Path to Insight - an online tutorial using Jupyter notebooks in Python.
Organization on GitHub
Short examples illustrating how to use some of the library components are available on read the docs.
Class and procedure documentation is available via Doxygen.
Jupyter notebooks on GitHub with long and extensively documented examples, useful for learning and teaching how to work with SimpleITK.
Get help, post questions on the ITK discussion forum.

## Related Articles

### Internal Links

- [3D Slicer](https://en.wikipedia.org/wiki/3D_Slicer)
- [American Recovery and Reinvestment Act of 2009](https://en.wikipedia.org/wiki/American_Recovery_and_Reinvestment_Act_of_2009)
- [Apache License](https://en.wikipedia.org/wiki/Apache_License)
- [Bibliometrix](https://en.wikipedia.org/wiki/Bibliometrix)
- [Bio7](https://en.wikipedia.org/wiki/Bio7)
- [Brian D. Ripley](https://en.wikipedia.org/wiki/Brian_D._Ripley)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CMake](https://en.wikipedia.org/wiki/CMake)
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Dirk Eddelbuettel](https://en.wikipedia.org/wiki/Dirk_Eddelbuettel)
- [Distributed R](https://en.wikipedia.org/wiki/Distributed_R)
- [Doxygen](https://en.wikipedia.org/wiki/Doxygen)
- [Dplyr](https://en.wikipedia.org/wiki/Dplyr)
- [Easystats](https://en.wikipedia.org/wiki/Easystats)
- [Emacs Speaks Statistics](https://en.wikipedia.org/wiki/Emacs_Speaks_Statistics)
- [Fork and pull model](https://en.wikipedia.org/wiki/Fork_and_pull_model)
- [Ggplot2](https://en.wikipedia.org/wiki/Ggplot2)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Hadley Wickham](https://en.wikipedia.org/wiki/Hadley_Wickham)
- [IPython](https://en.wikipedia.org/wiki/IPython)
- [Image analysis](https://en.wikipedia.org/wiki/Image_analysis)
- [Insight Segmentation and Registration Toolkit](https://en.wikipedia.org/wiki/Insight_Segmentation_and_Registration_Toolkit)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Java GUI for R](https://en.wikipedia.org/wiki/Java_GUI_for_R)
- [Jenny Bryan](https://en.wikipedia.org/wiki/Jenny_Bryan)
- [John Chambers (statistician)](https://en.wikipedia.org/wiki/John_Chambers_(statistician))
- [Julia Silge](https://en.wikipedia.org/wiki/Julia_Silge)
- [KH Coder](https://en.wikipedia.org/wiki/KH_Coder)
- [Knitr](https://en.wikipedia.org/wiki/Knitr)
- [Linux](https://en.wikipedia.org/wiki/Linux)
- [Lua (programming language)](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [Luke Tierney](https://en.wikipedia.org/wiki/Luke_Tierney)
- [Lumi (software)](https://en.wikipedia.org/wiki/Lumi_(software))
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [Revolution Analytics](https://en.wikipedia.org/wiki/Revolution_Analytics)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [National Institute of Allergy and Infectious Diseases](https://en.wikipedia.org/wiki/National_Institute_of_Allergy_and_Infectious_Diseases)
- [National Institutes of Health](https://en.wikipedia.org/wiki/National_Institutes_of_Health)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [OsiriX](https://en.wikipedia.org/wiki/OsiriX)
- [Peter Dalgaard](https://en.wikipedia.org/wiki/Peter_Dalgaard)
- [Posit PBC](https://en.wikipedia.org/wiki/Posit_PBC)
- [Procedural programming](https://en.wikipedia.org/wiki/Procedural_programming)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quantitative Discourse Analysis Package](https://en.wikipedia.org/wiki/Quantitative_Discourse_Analysis_Package)
- [R-Ladies](https://en.wikipedia.org/wiki/R-Ladies)
- [RExcel](https://en.wikipedia.org/wiki/RExcel)
- [RGtk2](https://en.wikipedia.org/wiki/RGtk2)
- [RKWard](https://en.wikipedia.org/wiki/RKWard)
- [RQDA](https://en.wikipedia.org/wiki/RQDA)
- [RStudio](https://en.wikipedia.org/wiki/RStudio)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [R Commander](https://en.wikipedia.org/wiki/R_Commander)
- [Linux Foundation](https://en.wikipedia.org/wiki/Linux_Foundation)
- [R package](https://en.wikipedia.org/wiki/R_package)
- [Rattle GUI](https://en.wikipedia.org/wiki/Rattle_GUI)
- [Renjin](https://en.wikipedia.org/wiki/Renjin)
- [Reproducibility](https://en.wikipedia.org/wiki/Reproducibility)
- [Revolution Analytics](https://en.wikipedia.org/wiki/Revolution_Analytics)
- [Rhea (pipeline)](https://en.wikipedia.org/wiki/Rhea_(pipeline))
- [Rmetrics](https://en.wikipedia.org/wiki/Rmetrics)
- [Rnn (software)](https://en.wikipedia.org/wiki/Rnn_(software))
- [Robert Gentleman (statistician)](https://en.wikipedia.org/wiki/Robert_Gentleman_(statistician))
- [Roger Bivand](https://en.wikipedia.org/wiki/Roger_Bivand)
- [Ross Ihaka](https://en.wikipedia.org/wiki/Ross_Ihaka)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Shiny (web framework)](https://en.wikipedia.org/wiki/Shiny_(web_framework))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Statcheck](https://en.wikipedia.org/wiki/Statcheck)
- [Sweave](https://en.wikipedia.org/wiki/Sweave)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [The R Journal](https://en.wikipedia.org/wiki/The_R_Journal)
- [Thomas Lumley (statistician)](https://en.wikipedia.org/wiki/Thomas_Lumley_(statistician))
- [Tidyverse](https://en.wikipedia.org/wiki/Tidyverse)
- [United States National Library of Medicine](https://en.wikipedia.org/wiki/United_States_National_Library_of_Medicine)
- [Yihui Xie](https://en.wikipedia.org/wiki/Yihui_Xie)
- [Template:R (programming language)](https://en.wikipedia.org/wiki/Template:R_(programming_language))
- [Template talk:R (programming language)](https://en.wikipedia.org/wiki/Template_talk:R_(programming_language))

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:45:00.473485+00:00_