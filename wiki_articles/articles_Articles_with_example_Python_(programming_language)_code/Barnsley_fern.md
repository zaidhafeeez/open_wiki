# Barnsley fern

_Last updated: 2024-12-14T15:39:36.877643_

**Original Article:** [Barnsley fern](https://en.wikipedia.org/wiki/Barnsley_fern)

**Summary:** The Barnsley fern is a fractal named after the British mathematician Michael Barnsley who first described it in his book Fractals Everywhere. He made it to resemble the black spleenwort, Asplenium adiantum-nigrum.

## Categories
- Category:Affine geometry
- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with short description
- Category:L-systems
- Category:Short description matches Wikidata

## Content

The Barnsley fern is a fractal named after the British mathematician Michael Barnsley who first described it in his book Fractals Everywhere. He made it to resemble the black spleenwort, Asplenium adiantum-nigrum.

History
The fern is one of the basic examples of self-similar sets, i.e. it is a mathematically generated pattern that can be reproducible at any magnification or reduction. Like the Sierpinski triangle, the Barnsley fern shows how graphically beautiful structures can be built from repetitive uses of mathematical formulas with computers. Barnsley's 1988 book Fractals Everywhere is based on the course which he taught for undergraduate and graduate students in the School of Mathematics, Georgia Institute of Technology, called Fractal Geometry. After publishing the book, a second course was developed, called Fractal Measure Theory. Barnsley's work has been a source of inspiration to graphic artists attempting to imitate nature with mathematical models.
The fern code developed by Barnsley is an example of an iterated function system (IFS) to create a fractal. This follows from the collage theorem. He has used fractals to model a diverse range of phenomena
in science and technology, but most specifically plant structures.

IFSs provide models for certain plants, leaves, and ferns, by virtue of the self-similarity which often occurs in branching structures in nature. But nature also exhibits randomness and variation from one level to the next; no two ferns are exactly alike, and the branching fronds become leaves at a smaller scale. V-variable fractals allow for such randomness and variability across scales, while at the same time admitting a continuous dependence on parameters which facilitates geometrical modelling. These factors allow us to make the hybrid biological models...
...we speculate that when a V -variable geometrical fractal model is found that has a good match to the geometry of a given plant, then there is a specific relationship between these code trees and the information stored in the genes of the plant.—Michael Barnsley et al.

Construction
Barnsley's fern uses four affine transformations.  The formula for one transformation is the following:

  
    
      
        
          f
          
            w
          
        
        (
        x
        ,
        y
        )
        =
        
          
            [
            
              
                
                  a
                
                
                  b
                
              
              
                
                  c
                
                
                  d
                
              
            
            ]
          
        
        
          
            [
            
              
                
                  x
                
              
              
                
                  y
                
              
            
            ]
          
        
        +
        
          
            [
            
              
                
                  e
                
              
              
                
                  f
                
              
            
            ]
          
        
      
    
    {\displaystyle f_{w}(x,y)={\begin{bmatrix}a&b\\c&d\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}+{\begin{bmatrix}e\\f\end{bmatrix}}}
  

Barnsley shows the IFS code for his Black Spleenwort fern fractal as a matrix of values shown in a table. In the table, the columns "a" through "f" are the coefficients of the equation, and "p" represents the probability factor.

These correspond to the following transformations:

  
    
      
        
          
            
              
                
                  f
                  
                    1
                  
                
                (
                x
                ,
                y
                )
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.00
                        
                        
                          0.00
                        
                      
                      
                        
                          0.00
                        
                        
                          0.16
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          x
                        
                      
                      
                        
                          y
                        
                      
                    
                    ]
                  
                
              
            
            
              
                
                  f
                  
                    2
                  
                
                (
                x
                ,
                y
                )
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.85
                        
                        
                          0.04
                        
                      
                      
                        
                          −
                          0.04
                        
                        
                          0.85
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          x
                        
                      
                      
                        
                          y
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          0.00
                        
                      
                      
                        
                          1.60
                        
                      
                    
                    ]
                  
                
              
            
            
              
                
                  f
                  
                    3
                  
                
                (
                x
                ,
                y
                )
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.20
                        
                        
                          −
                          0.26
                        
                      
                      
                        
                          0.23
                        
                        
                          0.22
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          x
                        
                      
                      
                        
                          y
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          0.00
                        
                      
                      
                        
                          1.60
                        
                      
                    
                    ]
                  
                
              
            
            
              
                
                  f
                  
                    4
                  
                
                (
                x
                ,
                y
                )
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          −
                          0.15
                        
                        
                          0.28
                        
                      
                      
                        
                          0.26
                        
                        
                          0.24
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          x
                        
                      
                      
                        
                          y
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          0.00
                        
                      
                      
                        
                          0.44
                        
                      
                    
                    ]
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}f_{1}(x,y)&={\begin{bmatrix}0.00&0.00\\0.00&0.16\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}\\[6px]f_{2}(x,y)&={\begin{bmatrix}0.85&0.04\\-0.04&0.85\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}+{\begin{bmatrix}0.00\\1.60\end{bmatrix}}\\[6px]f_{3}(x,y)&={\begin{bmatrix}0.20&-0.26\\0.23&0.22\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}+{\begin{bmatrix}0.00\\1.60\end{bmatrix}}\\[6px]f_{4}(x,y)&={\begin{bmatrix}-0.15&0.28\\0.26&0.24\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}+{\begin{bmatrix}0.00\\0.44\end{bmatrix}}\end{aligned}}}

Computer generation
Though Barnsley's fern could in theory be plotted by hand with a pen and graph paper, the number of iterations necessary runs into the tens of thousands, which makes use of a computer practically mandatory.  Many different computer models of Barnsley's fern are popular with contemporary mathematicians.  As long as math is programmed correctly using Barnsley's matrix of constants, the same fern shape will be produced.
The first point drawn is at the origin (x0 = 0, y0 = 0) and then the new points are iteratively computed by randomly applying one of the following four coordinate transformations:

f1
xn + 1 = 0
yn + 1 = 0.16 yn
This coordinate transformation is chosen 1% of the time and just maps any point to a point in the first line segment at the base of the stem. In the iterative generation, it acts as a reset to the base of the stem. Crucially it does not reset exactly to (0,0) which allows it to fill in the base stem which is translated and serves as a kind of "kernel" from which all other sections of the fern are generated via transformations f2, f3, f4.

f2
xn + 1 = 0.85 xn + 0.04 yn
yn + 1 = −0.04 xn + 0.85 yn + 1.6
This transformation encodes the self-similarity relationship of the entire fern with the sub-structure which consists of the fern with the removal of the section which includes the bottom two leaves. In the matrix representation, it can be seen to be a slight clockwise rotation, scaled to be slightly smaller and translated in the positive y direction. In the iterative generation, this transformation is applied with probability 85% and is intuitively responsible for the generation of the main stem, and the successive vertical generation of the leaves on either side of the stem from their "original" leaves at the base.

f3
xn + 1 = 0.2 xn − 0.26 yn
yn + 1 = 0.23 xn + 0.22 yn + 1.6
This transformation encodes the self-similarity of the entire fern with the bottom left leaf. In the matrix representation, it is seen to be a near-90° counterclockwise rotation, scaled down to approximately 30% size with a translation in the positive y direction. In the iterative generation, it is applied with probability 7% and is intuitively responsible for the generation of the lower-left leaf.

f4
xn + 1 = −0.15 xn + 0.28 yn
yn + 1 = 0.26 xn + 0.24 yn + 0.44
Similarly, this transformation encodes the self-similarity of the entire fern with the bottom right leaf. From its determinant it is easily seen to include a reflection and can be seen as a similar transformation as f3 albeit with a reflection about the y-axis. In the iterative-generation, it is applied with probability 7% and is responsible for the generation of the bottom right leaf.

Mutant varieties
By playing with the coefficients, it is possible to create mutant fern varieties. In his paper on V-variable fractals, Barnsley calls this trait a superfractal.
One experimenter has come up with a table of coefficients to produce another remarkably naturally looking fern however, resembling the Cyclosorus or Thelypteridaceae fern. These are:

Pseudocode


== References ==