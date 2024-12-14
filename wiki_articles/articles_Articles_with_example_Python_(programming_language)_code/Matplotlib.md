# Matplotlib

## Article Metadata

- **Last Updated:** 2024-12-14T19:40:38.265030+00:00
- **Original Article:** [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
- **Language:** en
- **Page ID:** 2901907

## Summary

Matplotlib (portmanteau of MATLAB, plot, and library) is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. There is also a procedural "pylab" interface based on a state machine (like OpenGL), designed to closely resemble that of MATLAB, though its use is discouraged. SciPy makes use of Matplotlib.
Matpl

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Commons category link is on Wikidata
- Category:Free data visualization software
- Category:Free plotting software
- Category:Free software programmed in Python
- Category:Python (programming language) scientific libraries
- Category:Science software that uses GTK
- Category:Science software that uses Qt
- Category:Short description is different from Wikidata

## Table of Contents

- Comparison with MATLAB
- Plot Types
- Animations
- Toolkits
- Related projects
- References
- External links

## Content

Matplotlib (portmanteau of MATLAB, plot, and library) is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. There is also a procedural "pylab" interface based on a state machine (like OpenGL), designed to closely resemble that of MATLAB, though its use is discouraged. SciPy makes use of Matplotlib.
Matplotlib was originally written by John D. Hunter. Since then it has had an active development community and is distributed under a BSD-style license. Michael Droettboom was nominated as matplotlib's lead developer shortly before John Hunter's death in August 2012 and was further joined by Thomas Caswell. Matplotlib is a NumFOCUS fiscally sponsored project.

Comparison with MATLAB
Pyplot is a Matplotlib module that provides a MATLAB-like interface. Matplotlib is designed to be as usable as MATLAB, with the ability to use Python, and the advantage of being free and open-source.

Plot Types
Matplotlib supports various types of 2 dimensional and 3 dimensional plots. The support for two dimensional plots is robust. The support for three dimensional plots was added later and while it is good, it is not as robust as 2 dimensional plots.

Examples
Animations
Matplotlib-animation capabilities are intended for visualizing how certain data changes. However, one can use the functionality in any way required.
These animations are defined as a function of frame number (or time). In other words, one defines a function that takes a frame number as input and defines/updates the matplotlib-figure based on it.

 The time at the beginning of a frame-number since the start of animation can be calculated as - 
  
    
      
        
          time
        
        =
        
          
            
              
                frame-number
              
              −
              1
            
            FPS
          
        
      
    
    {\displaystyle {\text{time}}={\frac {{\text{frame-number}}-1}{\text{FPS}}}}

Toolkits
Several toolkits are available which extend Matplotlib functionality. Some are separate downloads, others ship with the Matplotlib source code but have external dependencies.

Basemap: map plotting with various map projections, coastlines, and political boundaries
Cartopy: a mapping library featuring object-oriented map projection definitions, and arbitrary point, line, polygon and image transformation capabilities. (Matplotlib v1.2 and above)
Excel tools: utilities for exchanging data with Microsoft Excel
GTK tools: interface to the GTK library
Qt interface
Mplot3d: 3-D plots
Natgrid: interface to the natgrid library for gridding irregularly spaced data.
tikzplotlib: export to Pgfplots for smooth integration into LaTeX documents (formerly known as matplotlib2tikz)
Seaborn: provides an API on top of Matplotlib that offers sane choices for plot style and color defaults, defines simple high-level functions for common statistical plot types, and integrates with the functionality provided by Pandas
GeoPandas: simplifies geospatial work in Python without needing a spatial database like PostGIS
Cartopy: streamlines map creation in matplotlib by enabling users to specify a projection and add coastlines with a single line of code

Related projects
Biggles
Chaco
DISLIN
GNU Octave
gnuplotlib – plotting for numpy with a gnuplot backend
Gnuplot-py
PLplot – Python bindings available
SageMath – uses Matplotlib to draw plots
SciPy (modules plt and gplt)
Plotly – for interactive, online Matplotlib and Python graphs
Bokeh – Python interactive visualization library that targets modern web browsers for presentation

References
External links

Official website

## Related Articles

### Internal Links

- [API](https://en.wikipedia.org/wiki/API)
- [Anti-Grain Geometry](https://en.wikipedia.org/wiki/Anti-Grain_Geometry)
- [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses)
- [Cairo (graphics)](https://en.wikipedia.org/wiki/Cairo_(graphics))
- [Coast](https://en.wikipedia.org/wiki/Coast)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [DISLIN](https://en.wikipedia.org/wiki/DISLIN)
- [Download](https://en.wikipedia.org/wiki/Download)
- [GNU Octave](https://en.wikipedia.org/wiki/GNU_Octave)
- [GTK](https://en.wikipedia.org/wiki/GTK)
- [Widget toolkit](https://en.wikipedia.org/wiki/Widget_toolkit)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Gnuplot](https://en.wikipedia.org/wiki/Gnuplot)
- [John D. Hunter](https://en.wikipedia.org/wiki/John_D._Hunter)
- [LaTeX](https://en.wikipedia.org/wiki/LaTeX)
- [Library (computing)](https://en.wikipedia.org/wiki/Library_(computing))
- [List of information graphics software](https://en.wikipedia.org/wiki/List_of_information_graphics_software)
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [Map projection](https://en.wikipedia.org/wiki/Map_projection)
- [MayaVi](https://en.wikipedia.org/wiki/MayaVi)
- [Microsoft Excel](https://en.wikipedia.org/wiki/Microsoft_Excel)
- [NumPy](https://en.wikipedia.org/wiki/NumPy)
- [Numerical analysis](https://en.wikipedia.org/wiki/Numerical_analysis)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [OpenGL](https://en.wikipedia.org/wiki/OpenGL)
- [Open source](https://en.wikipedia.org/wiki/Open_source)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [PLplot](https://en.wikipedia.org/wiki/PLplot)
- [Pandas (software)](https://en.wikipedia.org/wiki/Pandas_(software))
- [Plotly](https://en.wikipedia.org/wiki/Plotly)
- [Plotter](https://en.wikipedia.org/wiki/Plotter)
- [Polygon](https://en.wikipedia.org/wiki/Polygon)
- [Procedural programming](https://en.wikipedia.org/wiki/Procedural_programming)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Qt (software)](https://en.wikipedia.org/wiki/Qt_(software))
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [SageMath](https://en.wikipedia.org/wiki/SageMath)
- [SciPy](https://en.wikipedia.org/wiki/SciPy)
- [Scikit-image](https://en.wikipedia.org/wiki/Scikit-image)
- [Scikit-learn](https://en.wikipedia.org/wiki/Scikit-learn)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software engine](https://en.wikipedia.org/wiki/Software_engine)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Source code](https://en.wikipedia.org/wiki/Source_code)
- [Finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine)
- [Tkinter](https://en.wikipedia.org/wiki/Tkinter)
- [Web mapping](https://en.wikipedia.org/wiki/Web_mapping)
- [WxPython](https://en.wikipedia.org/wiki/WxPython)
- [Template:SciPy ecosystem](https://en.wikipedia.org/wiki/Template:SciPy_ecosystem)
- [Template talk:SciPy ecosystem](https://en.wikipedia.org/wiki/Template_talk:SciPy_ecosystem)
- [Category:Python (programming language) scientific libraries](https://en.wikipedia.org/wiki/Category:Python_(programming_language)_scientific_libraries)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:40:38.265030+00:00_