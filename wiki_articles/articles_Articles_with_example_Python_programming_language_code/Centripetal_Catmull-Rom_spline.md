# Centripetal Catmull–Rom spline

## Metadata
- **Last Updated:** 2024-12-03 07:37:51 UTC
- **Original Article:** [Centripetal Catmull–Rom spline](https://en.wikipedia.org/wiki/Centripetal_Catmull%E2%80%93Rom_spline)
- **Language:** en
- **Page ID:** 40760845

## Summary
In computer graphics, the centripetal Catmull–Rom spline is a variant form of the Catmull–Rom spline, originally formulated by Edwin Catmull and Raphael Rom, which can be evaluated using a recursive algorithm proposed by Barry and Goldman. It is a type of interpolating spline (a curve that goes through its control points) defined by four control points 
  
    
      
        
          
            P
          
          
            0
          
        
        ,
        
          
            P
          
          
            1
          
        
        ,
        
          
            P
          
          
            2
          
        
        ,
        
          
            P
          
          
            3
          
        
      
    
    {\displaystyle \mathbf {P} _{0},\mathbf {P} _{1},\mathbf {P} _{2},\mathbf {P} _{3}}
  
, with the curve drawn only from 
  
    
      
        
          
            P
          
          
            1
          
        
      
    
    {\displaystyle \mathbf {P} _{1}}
  
 to 
  
    
      
        
          
            P
          
          
            2
          
        
      
    
    {\displaystyle \mathbf {P} _{2}}
  
.

## Categories
This article belongs to the following categories:

- Category:All Wikipedia articles needing clarification
- Category:Articles with example C Sharp code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:CS1 maint: multiple names: authors list
- Category:Short description is different from Wikidata
- Category:Splines (mathematics)
- Category:Wikipedia articles needing clarification from September 2016

## Table of Contents

- Definition
- Advantages
- Other uses
- Code example in Python
- Code example in Unity C#
- Code example in Unreal C++
- See also
- References
- External links

## Content

In computer graphics, the centripetal Catmull–Rom spline is a variant form of the Catmull–Rom spline, originally formulated by Edwin Catmull and Raphael Rom, which can be evaluated using a recursive algorithm proposed by Barry and Goldman. It is a type of interpolating spline (a curve that goes through its control points) defined by four control points 
  
    
      
        
          
            P
          
          
            0
          
        
        ,
        
          
            P
          
          
            1
          
        
        ,
        
          
            P
          
          
            2
          
        
        ,
        
          
            P
          
          
            3
          
        
      
    
    {\displaystyle \mathbf {P} _{0},\mathbf {P} _{1},\mathbf {P} _{2},\mathbf {P} _{3}}
  
, with the curve drawn only from 
  
    
      
        
          
            P
          
          
            1
          
        
      
    
    {\displaystyle \mathbf {P} _{1}}
  
 to 
  
    
      
        
          
            P
          
          
            2
          
        
      
    
    {\displaystyle \mathbf {P} _{2}}
  
.

Definition
Let 
  
    
      
        
          
            P
          
          
            i
          
        
        =
        [
        
          x
          
            i
          
        
        
        
          y
          
            i
          
        
        
          ]
          
            T
          
        
      
    
    {\displaystyle \mathbf {P} _{i}=[x_{i}\quad y_{i}]^{T}}
  
 denote a point. For a curve segment 
  
    
      
        
          C
        
      
    
    {\displaystyle \mathbf {C} }
  
 defined by points 
  
    
      
        
          
            P
          
          
            0
          
        
        ,
        
          
            P
          
          
            1
          
        
        ,
        
          
            P
          
          
            2
          
        
        ,
        
          
            P
          
          
            3
          
        
      
    
    {\displaystyle \mathbf {P} _{0},\mathbf {P} _{1},\mathbf {P} _{2},\mathbf {P} _{3}}
  
 and knot sequence 
  
    
      
        
          t
          
            0
          
        
        ,
        
          t
          
            1
          
        
        ,
        
          t
          
            2
          
        
        ,
        
          t
          
            3
          
        
      
    
    {\displaystyle t_{0},t_{1},t_{2},t_{3}}
  
, the centripetal Catmull–Rom spline can be produced by:

  
    
      
        
          C
        
        =
        
          
            
              
                t
                
                  2
                
              
              −
              t
            
            
              
                t
                
                  2
                
              
              −
              
                t
                
                  1
                
              
            
          
        
        
          
            B
          
          
            1
          
        
        +
        
          
            
              t
              −
              
                t
                
                  1
                
              
            
            
              
                t
                
                  2
                
              
              −
              
                t
                
                  1
                
              
            
          
        
        
          
            B
          
          
            2
          
        
      
    
    {\displaystyle \mathbf {C} ={\frac {t_{2}-t}{t_{2}-t_{1}}}\mathbf {B} _{1}+{\frac {t-t_{1}}{t_{2}-t_{1}}}\mathbf {B} _{2}}
  

where

  
    
      
        
          
            B
          
          
            1
          
        
        =
        
          
            
              
                t
                
                  2
                
              
              −
              t
            
            
              
                t
                
                  2
                
              
              −
              
                t
                
                  0
                
              
            
          
        
        
          
            A
          
          
            1
          
        
        +
        
          
            
              t
              −
              
                t
                
                  0
                
              
            
            
              
                t
                
                  2
                
              
              −
              
                t
                
                  0
                
              
            
          
        
        
          
            A
          
          
            2
          
        
      
    
    {\displaystyle \mathbf {B} _{1}={\frac {t_{2}-t}{t_{2}-t_{0}}}\mathbf {A} _{1}+{\frac {t-t_{0}}{t_{2}-t_{0}}}\mathbf {A} _{2}}
  

  
    
      
        
          
            B
          
          
            2
          
        
        =
        
          
            
              
                t
                
                  3
                
              
              −
              t
            
            
              
                t
                
                  3
                
              
              −
              
                t
                
                  1
                
              
            
          
        
        
          
            A
          
          
            2
          
        
        +
        
          
            
              t
              −
              
                t
                
                  1
                
              
            
            
              
                t
                
                  3
                
              
              −
              
                t
                
                  1
                
              
            
          
        
        
          
            A
          
          
            3
          
        
      
    
    {\displaystyle \mathbf {B} _{2}={\frac {t_{3}-t}{t_{3}-t_{1}}}\mathbf {A} _{2}+{\frac {t-t_{1}}{t_{3}-t_{1}}}\mathbf {A} _{3}}
  

  
    
      
        
          
            A
          
          
            1
          
        
        =
        
          
            
              
                t
                
                  1
                
              
              −
              t
            
            
              
                t
                
                  1
                
              
              −
              
                t
                
                  0
                
              
            
          
        
        
          
            P
          
          
            0
          
        
        +
        
          
            
              t
              −
              
                t
                
                  0
                
              
            
            
              
                t
                
                  1
                
              
              −
              
                t
                
                  0
                
              
            
          
        
        
          
            P
          
          
            1
          
        
      
    
    {\displaystyle \mathbf {A} _{1}={\frac {t_{1}-t}{t_{1}-t_{0}}}\mathbf {P} _{0}+{\frac {t-t_{0}}{t_{1}-t_{0}}}\mathbf {P} _{1}}
  

  
    
      
        
          
            A
          
          
            2
          
        
        =
        
          
            
              
                t
                
                  2
                
              
              −
              t
            
            
              
                t
                
                  2
                
              
              −
              
                t
                
                  1
                
              
            
          
        
        
          
            P
          
          
            1
          
        
        +
        
          
            
              t
              −
              
                t
                
                  1
                
              
            
            
              
                t
                
                  2
                
              
              −
              
                t
                
                  1
                
              
            
          
        
        
          
            P
          
          
            2
          
        
      
    
    {\displaystyle \mathbf {A} _{2}={\frac {t_{2}-t}{t_{2}-t_{1}}}\mathbf {P} _{1}+{\frac {t-t_{1}}{t_{2}-t_{1}}}\mathbf {P} _{2}}
  

  
    
      
        
          
            A
          
          
            3
          
        
        =
        
          
            
              
                t
                
                  3
                
              
              −
              t
            
            
              
                t
                
                  3
                
              
              −
              
                t
                
                  2
                
              
            
          
        
        
          
            P
          
          
            2
          
        
        +
        
          
            
              t
              −
              
                t
                
                  2
                
              
            
            
              
                t
                
                  3
                
              
              −
              
                t
                
                  2
                
              
            
          
        
        
          
            P
          
          
            3
          
        
      
    
    {\displaystyle \mathbf {A} _{3}={\frac {t_{3}-t}{t_{3}-t_{2}}}\mathbf {P} _{2}+{\frac {t-t_{2}}{t_{3}-t_{2}}}\mathbf {P} _{3}}
  

and

  
    
      
        
          t
          
            i
            +
            1
          
        
        =
        
          
            [
            
              
                (
                
                  x
                  
                    i
                    +
                    1
                  
                
                −
                
                  x
                  
                    i
                  
                
                
                  )
                  
                    2
                  
                
                +
                (
                
                  y
                  
                    i
                    +
                    1
                  
                
                −
                
                  y
                  
                    i
                  
                
                
                  )
                  
                    2
                  
                
              
            
            ]
          
          
            α
          
        
        +
        
          t
          
            i
          
        
      
    
    {\displaystyle t_{i+1}=\left[{\sqrt {(x_{i+1}-x_{i})^{2}+(y_{i+1}-y_{i})^{2}}}\right]^{\alpha }+t_{i}}
  

in which 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 ranges from 0 to 1 for knot parameterization, and 
  
    
      
        i
        =
        0
        ,
        1
        ,
        2
        ,
        3
      
    
    {\displaystyle i=0,1,2,3}
  
 with 
  
    
      
        
          t
          
            0
          
        
        =
        0
      
    
    {\displaystyle t_{0}=0}
  
. For centripetal Catmull–Rom spline, the value of 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 is 
  
    
      
        0.5
      
    
    {\displaystyle 0.5}
  
. When 
  
    
      
        α
        =
        0
      
    
    {\displaystyle \alpha =0}
  
, the resulting curve is the standard uniform Catmull–Rom spline; when 
  
    
      
        α
        =
        1
      
    
    {\displaystyle \alpha =1}
  
, the result is a chordal Catmull–Rom spline.

Plugging 
  
    
      
        t
        =
        
          t
          
            1
          
        
      
    
    {\displaystyle t=t_{1}}
  
 into the spline equations 
  
    
      
        
          
            A
          
          
            1
          
        
        ,
        
          
            A
          
          
            2
          
        
        ,
        
          
            A
          
          
            3
          
        
        ,
        
          
            B
          
          
            1
          
        
        ,
        
          
            B
          
          
            2
          
        
        ,
      
    
    {\displaystyle \mathbf {A} _{1},\mathbf {A} _{2},\mathbf {A} _{3},\mathbf {B} _{1},\mathbf {B} _{2},}
  
 and 
  
    
      
        
          C
        
      
    
    {\displaystyle \mathbf {C} }
  
 shows that the value of the spline curve at 
  
    
      
        
          t
          
            1
          
        
      
    
    {\displaystyle t_{1}}
  
 is 
  
    
      
        
          C
        
        =
        
          
            P
          
          
            1
          
        
      
    
    {\displaystyle \mathbf {C} =\mathbf {P} _{1}}
  
. Similarly, substituting 
  
    
      
        t
        =
        
          t
          
            2
          
        
      
    
    {\displaystyle t=t_{2}}
  
 into the spline equations shows that 
  
    
      
        
          C
        
        =
        
          
            P
          
          
            2
          
        
      
    
    {\displaystyle \mathbf {C} =\mathbf {P} _{2}}
  
 at 
  
    
      
        
          t
          
            2
          
        
      
    
    {\displaystyle t_{2}}
  
. This is true independent of the value of 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 since the equation for 
  
    
      
        
          t
          
            i
            +
            1
          
        
      
    
    {\displaystyle t_{i+1}}
  
 is not needed to calculate the value of 
  
    
      
        
          C
        
      
    
    {\displaystyle \mathbf {C} }
  
 at points 
  
    
      
        
          t
          
            1
          
        
      
    
    {\displaystyle t_{1}}
  
 and 
  
    
      
        
          t
          
            2
          
        
      
    
    {\displaystyle t_{2}}
  
.

The extension to 3D points is simply achieved by considering 
  
    
      
        
          
            P
          
          
            i
          
        
        =
        [
        
          x
          
            i
          
        
        
        
          y
          
            i
          
        
        
        
          z
          
            i
          
        
        
          ]
          
            T
          
        
      
    
    {\displaystyle \mathbf {P} _{i}=[x_{i}\quad y_{i}\quad z_{i}]^{T}}
  
a generic 3D point 
  
    
      
        
          
            P
          
          
            i
          
        
      
    
    {\displaystyle \mathbf {P} _{i}}
  
 and

  
    
      
        
          t
          
            i
            +
            1
          
        
        =
        
          
            [
            
              
                (
                
                  x
                  
                    i
                    +
                    1
                  
                
                −
                
                  x
                  
                    i
                  
                
                
                  )
                  
                    2
                  
                
                +
                (
                
                  y
                  
                    i
                    +
                    1
                  
                
                −
                
                  y
                  
                    i
                  
                
                
                  )
                  
                    2
                  
                
                +
                (
                
                  z
                  
                    i
                    +
                    1
                  
                
                −
                
                  z
                  
                    i
                  
                
                
                  )
                  
                    2
                  
                
              
            
            ]
          
          
            α
          
        
        +
        
          t
          
            i
          
        
      
    
    {\displaystyle t_{i+1}=\left[{\sqrt {(x_{i+1}-x_{i})^{2}+(y_{i+1}-y_{i})^{2}+(z_{i+1}-z_{i})^{2}}}\right]^{\alpha }+t_{i}}

Advantages
Centripetal Catmull–Rom spline has several desirable mathematical properties compared to the original and the other types of Catmull-Rom formulation. First, it will not form loop or self-intersection within a curve segment. Second, cusp will never occur within a curve segment. Third, it follows the control points more tightly.

Other uses
In computer vision, centripetal Catmull-Rom spline has been used to formulate an active model for segmentation. The method is termed active spline model. The model is devised on the basis of active shape model, but uses centripetal Catmull-Rom spline to join two successive points (active shape model uses simple straight line), so that the total number of points necessary to depict a shape is less. The use of centripetal Catmull-Rom spline makes the training of a shape model much simpler, and it enables a better way to edit a contour after segmentation.

Code example in Python
The following is an implementation of the Catmull–Rom spline in Python that produces the plot shown beneath.

Code example in Unity C#
Code example in Unreal C++
See also
Cubic Hermite splines

References
External links
Catmull-Rom curve with no cusps and no self-intersections –  implementation in Java
Catmull-Rom curve with no cusps and no self-intersections –  simplified implementation in C++
Catmull-Rom splines –  interactive generation via Python, in a Jupyter notebook
Smooth Paths Using Catmull-Rom Splines –  another versatile implementation in C++ including centripetal CR splines

## Archive Info
- **Archived on:** 2024-12-15 21:03:48 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 19716 bytes
- **Word Count:** 976 words
