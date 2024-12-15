# Matplotlib

## Metadata
- **Last Updated:** 2024-12-10 16:48:53 UTC
- **Original Article:** [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
- **Language:** en
- **Page ID:** 2901907

## Summary
Matplotlib (portmanteau of MATLAB, plot, and library) is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. There is also a procedural "pylab" interface based on a state machine (like OpenGL), designed to closely resemble that of MATLAB, though its use is discouraged. SciPy makes use of Matplotlib.
Matplotlib was originally written by John D. Hunter. Since then it has had an active development community and is distributed under a BSD-style license. Michael Droettboom was nominated as matplotlib's lead developer shortly before John Hunter's death in August 2012 and was further joined by Thomas Caswell. Matplotlib is a NumFOCUS fiscally sponsored project.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 20:26:35 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 3821 bytes
- **Word Count:** 523 words
