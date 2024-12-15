# Fast Walsh–Hadamard transform

## Article Metadata

- **Last Updated:** 2024-12-15T04:24:55.375704+00:00
- **Original Article:** [Fast Walsh–Hadamard transform](https://en.wikipedia.org/wiki/Fast_Walsh%E2%80%93Hadamard_transform)
- **Language:** en
- **Page ID:** 17548051

## Summary

In computational mathematics, the Hadamard ordered fast Walsh–Hadamard transform (FWHTh) is an efficient algorithm to compute the Walsh–Hadamard transform (WHT).  A naive implementation of the WHT of order 
  
    
      
        n
        =
        
          2
          
            m
          
        
      
    
    {\displaystyle n=2^{m}}
  
 would have a computational complexity of O(
  
    
      
        
          n
          
            2
          
        
      
    
    {\displ

## Categories

- Category:Algorithms and data structures stubs
- Category:All Wikipedia articles written in American English
- Category:All stub articles
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Digital signal processing
- Category:Short description is different from Wikidata
- Category:Signal processing stubs
- Category:Use American English from January 2019

## Table of Contents

- Python example code
- See also
- References
- External links

## Content

In computational mathematics, the Hadamard ordered fast Walsh–Hadamard transform (FWHTh) is an efficient algorithm to compute the Walsh–Hadamard transform (WHT).  A naive implementation of the WHT of order 
  
    
      
        n
        =
        
          2
          
            m
          
        
      
    
    {\displaystyle n=2^{m}}
  
 would have a computational complexity of O(
  
    
      
        
          n
          
            2
          
        
      
    
    {\displaystyle n^{2}}
  
).  The FWHTh requires only 
  
    
      
        n
        log
        ⁡
        n
      
    
    {\displaystyle n\log n}
  
 additions or subtractions.
The FWHTh is a divide-and-conquer algorithm that recursively breaks down a WHT of size 
  
    
      
        n
      
    
    {\displaystyle n}
  
 into two smaller WHTs of size 
  
    
      
        n
        
          /
        
        2
      
    
    {\displaystyle n/2}
  
.   This implementation follows the recursive definition of the 
  
    
      
        
          2
          
            m
          
        
        ×
        
          2
          
            m
          
        
      
    
    {\displaystyle 2^{m}\times 2^{m}}
  
 Hadamard matrix 
  
    
      
        
          H
          
            m
          
        
      
    
    {\displaystyle H_{m}}
  
:

  
    
      
        
          H
          
            m
          
        
        =
        
          
            1
            
              2
            
          
        
        
          
            (
            
              
                
                  
                    H
                    
                      m
                      −
                      1
                    
                  
                
                
                  
                    H
                    
                      m
                      −
                      1
                    
                  
                
              
              
                
                  
                    H
                    
                      m
                      −
                      1
                    
                  
                
                
                  −
                  
                    H
                    
                      m
                      −
                      1
                    
                  
                
              
            
            )
          
        
        .
      
    
    {\displaystyle H_{m}={\frac {1}{\sqrt {2}}}{\begin{pmatrix}H_{m-1}&H_{m-1}\\H_{m-1}&-H_{m-1}\end{pmatrix}}.}
  

The 
  
    
      
        1
        
          /
        
        
          
            2
          
        
      
    
    {\displaystyle 1/{\sqrt {2}}}
  
 normalization factors for each stage may be grouped together or even omitted.
The sequency-ordered, also known as Walsh-ordered, fast Walsh–Hadamard transform, FWHTw, is obtained by computing the FWHTh as above, and then rearranging the outputs.
A simple fast nonrecursive implementation of the Walsh–Hadamard transform follows from decomposition of the Hadamard transform matrix as 
  
    
      
        
          H
          
            m
          
        
        =
        
          A
          
            m
          
        
      
    
    {\displaystyle H_{m}=A^{m}}
  
, where A is m-th root of 
  
    
      
        
          H
          
            m
          
        
      
    
    {\displaystyle H_{m}}
  
.

Python example code
See also
Fast Fourier transform

References
External links
Charles Constantine Gumas, A century old, the fast Hadamard transform proves useful in digital communications

## Related Articles

### Internal Links

- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Computational complexity theory](https://en.wikipedia.org/wiki/Computational_complexity_theory)
- [Data structure](https://en.wikipedia.org/wiki/Data_structure)
- [Divide-and-conquer algorithm](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform)
- [Hadamard matrix](https://en.wikipedia.org/wiki/Hadamard_matrix)
- [Recursion](https://en.wikipedia.org/wiki/Recursion)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Signal processing](https://en.wikipedia.org/wiki/Signal_processing)
- [Walsh matrix](https://en.wikipedia.org/wiki/Walsh_matrix)
- [Hadamard transform](https://en.wikipedia.org/wiki/Hadamard_transform)
- [Wikipedia:Stub](https://en.wikipedia.org/wiki/Wikipedia:Stub)
- [Template:Algorithm-stub](https://en.wikipedia.org/wiki/Template:Algorithm-stub)
- [Template:Signal-processing-stub](https://en.wikipedia.org/wiki/Template:Signal-processing-stub)
- [Template talk:Algorithm-stub](https://en.wikipedia.org/wiki/Template_talk:Algorithm-stub)
- [Template talk:Signal-processing-stub](https://en.wikipedia.org/wiki/Template_talk:Signal-processing-stub)
- [Category:Use American English from January 2019](https://en.wikipedia.org/wiki/Category:Use_American_English_from_January_2019)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:24:55.375704+00:00_