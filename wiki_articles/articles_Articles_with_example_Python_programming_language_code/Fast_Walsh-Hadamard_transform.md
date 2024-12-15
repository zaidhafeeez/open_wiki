# Fast Walsh–Hadamard transform

## Metadata
- **Last Updated:** 2024-12-08 17:18:49 UTC
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

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 15:18:35 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 3824 bytes
- **Word Count:** 246 words
