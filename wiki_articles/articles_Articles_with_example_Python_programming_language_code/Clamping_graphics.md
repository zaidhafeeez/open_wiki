# Clamping (graphics)

## Metadata
- **Last Updated:** 2024-12-03 07:05:09 UTC
- **Original Article:** [Clamping (graphics)](https://en.wikipedia.org/wiki/Clamping_(graphics))
- **Language:** en
- **Page ID:** 6664825

## Summary
In computer science, clamping, or clipping is the process of limiting a value to a range between a minimum and a maximum value. Unlike wrapping, clamping merely moves the point to the nearest available value.

In Python, clamping can be defined as follows:

This is equivalent to max(minimum, min(x, maximum)) for languages that support the functions min and max.

## Categories
This article belongs to the following categories:

- Category:All articles needing additional references
- Category:All stub articles
- Category:Articles needing additional references from December 2009
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Computer graphics algorithms
- Category:Computer graphics stubs
- Category:Short description is different from Wikidata

## Table of Contents

- Uses

## Content

In computer science, clamping, or clipping is the process of limiting a value to a range between a minimum and a maximum value. Unlike wrapping, clamping merely moves the point to the nearest available value.

In Python, clamping can be defined as follows:

This is equivalent to max(minimum, min(x, maximum)) for languages that support the functions min and max.

Uses
Several programming languages and libraries provide functions for fast and vectorized clamping. In Python, the pandas library offers the Series.clip and DataFrame.clip methods. The NumPy library offers the clip function. In the Wolfram Language, it is implemented as Clip[x, {minimum, maximum}].
In OpenGL, the glClearColor function takes four GLfloat values which are then 'clamped' to the range 
  
    
      
        [
        0
        ,
        1
        ]
      
    
    {\displaystyle [0,1]}
  
.
One of the many uses of clamping in computer graphics is the placing of a detail inside a polygon—for example, a bullet hole on a wall. It can also be used with wrapping to create a variety of effects.


== References ==

## Archive Info
- **Archived on:** 2024-12-15 21:03:52 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 1098 bytes
- **Word Count:** 167 words
