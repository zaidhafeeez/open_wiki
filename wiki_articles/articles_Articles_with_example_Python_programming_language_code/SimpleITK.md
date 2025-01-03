# SimpleITK

## Metadata
- **Last Updated:** 2024-12-03 07:51:11 UTC
- **Original Article:** [SimpleITK](https://en.wikipedia.org/wiki/SimpleITK)
- **Language:** en
- **Page ID:** 57078264

## Summary
SimpleITK is a simplified, open-source interface to the Insight Segmentation and Registration Toolkit (ITK). The SimpleITK image analysis library is available in multiple programming languages including C++, Python, R, Java, C#, Lua, Ruby and Tcl. Binary distributions are available for all three major operating systems (Linux, macOS and Microsoft Windows).
Developed at the National Institutes of Health (NIH) as an open resource, its primary goal is to make the algorithms available in the ITK library accessible to the broadest range of scientists whose work includes image analysis, irrespective of their software development skills. 
As a consequence, the SimpleITK interface exposes only the most commonly modified algorithmic settings of the ITK components. Additionally, the library provides both an object oriented and a procedural interface to most of the image processing filters. The latter enables image analysis workflows with concise syntax. A secondary goal of the library is to promote reproducible image analysis workflows by using the SimpleITK library in conjunction with modern tools for reproducible computational workflows available in the Python (Jupyter notebooks) and R (knitr package ) programming languages.
Software development is centered on GitHub using a fork and pull model. The project is built using the CMake tool, with nightly builds posted to the project's quality dashboard.
Multiple medical image analysis applications and libraries incorporate SimpleITK as a key building block, as it provides a wide range of image filtering and image IO components with a user friendly interface. Examples include the pyOsirix scripting tool for the popular Osirix application, the pyradiomics python package for extracting radiomic features from medical imaging, the 3DSlicer image analysis application,  the SimpleElastix medical image registration library, and the NiftyNet deep learning library for medical imaging.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 21:06:05 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 3693 bytes
- **Word Count:** 540 words
