# Clamping (graphics)

## Article Metadata

- **Last Updated:** 2024-12-15T03:59:30.332211+00:00
- **Original Article:** [Clamping (graphics)](https://en.wikipedia.org/wiki/Clamping_(graphics))
- **Language:** en
- **Page ID:** 6664825

## Summary

In computer science, clamping, or clipping is the process of limiting a value to a range between a minimum and a maximum value. Unlike wrapping, clamping merely moves the point to the nearest available value.

In Python, clamping can be defined as follows:

This is equivalent to max(minimum, min(x, maximum)) for languages that support the functions min and max.

## Categories

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

## Related Articles

### Internal Links

- [3D computer graphics](https://en.wikipedia.org/wiki/3D_computer_graphics)
- [Computer graphics](https://en.wikipedia.org/wiki/Computer_graphics)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [NumPy](https://en.wikipedia.org/wiki/NumPy)
- [OpenGL](https://en.wikipedia.org/wiki/OpenGL)
- [Pandas (software)](https://en.wikipedia.org/wiki/Pandas_(software))
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Wolfram Language](https://en.wikipedia.org/wiki/Wolfram_Language)
- [Wrapping (graphics)](https://en.wikipedia.org/wiki/Wrapping_(graphics))
- [Wikipedia:Stub](https://en.wikipedia.org/wiki/Wikipedia:Stub)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Compu-graphics-stub](https://en.wikipedia.org/wiki/Template:Compu-graphics-stub)
- [Template talk:Compu-graphics-stub](https://en.wikipedia.org/wiki/Template_talk:Compu-graphics-stub)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from December 2009](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_December_2009)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:59:30.332211+00:00_