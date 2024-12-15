# Lanczos approximation

## Metadata
- **Last Updated:** 2024-12-03 06:57:36 UTC
- **Original Article:** [Lanczos approximation](https://en.wikipedia.org/wiki/Lanczos_approximation)
- **Language:** en
- **Page ID:** 1982776

## Summary
In mathematics, the Lanczos approximation is a method for computing the gamma function numerically, published by Cornelius Lanczos in 1964. It is a practical alternative to the more popular Stirling's approximation for calculating the gamma function with fixed precision.

## Categories
This article belongs to the following categories:

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Gamma and related functions
- Category:Numerical analysis
- Category:Short description is different from Wikidata

## Table of Contents

- Introduction
- Coefficients
- Derivation
- Simple implementation
- See also
- References

## Content

In mathematics, the Lanczos approximation is a method for computing the gamma function numerically, published by Cornelius Lanczos in 1964. It is a practical alternative to the more popular Stirling's approximation for calculating the gamma function with fixed precision.

Introduction
The Lanczos approximation consists of the formula

  
    
      
        Γ
        (
        z
        +
        1
        )
        =
        
          
            2
            π
          
        
        
          
            
              (
              
                z
                +
                g
                +
                
                  
                    
                      1
                      2
                    
                  
                
              
              )
            
          
          
            z
            +
            1
            
              /
            
            2
          
        
        
          e
          
            −
            (
            z
            +
            g
            +
            1
            
              /
            
            2
            )
          
        
        
          A
          
            g
          
        
        (
        z
        )
      
    
    {\displaystyle \Gamma (z+1)={\sqrt {2\pi }}{\left(z+g+{\tfrac {1}{2}}\right)}^{z+1/2}e^{-(z+g+1/2)}A_{g}(z)}
  

for the gamma function, with

  
    
      
        
          A
          
            g
          
        
        (
        z
        )
        =
        
          
            1
            2
          
        
        
          p
          
            0
          
        
        (
        g
        )
        +
        
          p
          
            1
          
        
        (
        g
        )
        
          
            z
            
              z
              +
              1
            
          
        
        +
        
          p
          
            2
          
        
        (
        g
        )
        
          
            
              z
              (
              z
              −
              1
              )
            
            
              (
              z
              +
              1
              )
              (
              z
              +
              2
              )
            
          
        
        +
        ⋯
        .
      
    
    {\displaystyle A_{g}(z)={\frac {1}{2}}p_{0}(g)+p_{1}(g){\frac {z}{z+1}}+p_{2}(g){\frac {z(z-1)}{(z+1)(z+2)}}+\cdots .}
  

Here g is a real constant that may be chosen arbitrarily subject to the restriction that Re(z+g+⁠1/2⁠) > 0. The coefficients p, which depend on g, are slightly more difficult to calculate (see below). Although the formula as stated here is only valid for arguments in the right complex half-plane, it can be extended to the entire complex plane by the reflection formula,

  
    
      
        Γ
        (
        1
        −
        z
        )
        
        Γ
        (
        z
        )
        =
        
          
            π
            
              sin
              ⁡
              π
              z
            
          
        
        .
      
    
    {\displaystyle \Gamma (1-z)\;\Gamma (z)={\pi  \over \sin \pi z}.}
  

The series A is convergent, and may be truncated to obtain an approximation with the desired precision. By choosing an appropriate g (typically a small integer), only some 5–10 terms of the series are needed to compute the gamma function with typical single or double floating-point precision. If a fixed g is chosen, the coefficients can be calculated in advance and, thanks to partial fraction decomposition, the sum is recast into the following form:

  
    
      
        
          A
          
            g
          
        
        (
        z
        )
        =
        
          c
          
            0
          
        
        +
        
          ∑
          
            k
            =
            1
          
          
            N
          
        
        
          
            
              c
              
                k
              
            
            
              z
              +
              k
            
          
        
      
    
    {\displaystyle A_{g}(z)=c_{0}+\sum _{k=1}^{N}{\frac {c_{k}}{z+k}}}
  

Thus computing the gamma function becomes a matter of evaluating only a small number of elementary functions and multiplying by stored constants.  The Lanczos approximation was popularized by Numerical Recipes, according to which computing the gamma function becomes "not much more difficult than other built-in functions that we take for granted, such as sin x or ex." The method is also implemented in the GNU Scientific Library, Boost, CPython and musl.

Coefficients
The coefficients are given by

  
    
      
        
          p
          
            k
          
        
        (
        g
        )
        =
        
          
            
              2
              
            
            π
          
        
        
          ∑
          
            ℓ
            =
            0
          
          
            k
          
        
        
          C
          
            2
            k
            +
            1
            ,
            
            2
            ℓ
            +
            1
          
        
        
          (
          
            ℓ
            −
            
              
                
                  1
                  2
                
              
            
          
          )
        
        !
        
          
            
              (
              
                ℓ
                +
                g
                +
                
                  
                    
                      1
                      2
                    
                  
                
              
              )
            
          
          
            −
            (
            ℓ
            +
            1
            
              /
            
            2
            )
          
        
        
          e
          
            ℓ
            +
            g
            +
            1
            
              /
            
            2
          
        
      
    
    {\displaystyle p_{k}(g)={\frac {\sqrt {2\,}}{\pi }}\sum _{\ell =0}^{k}C_{2k+1,\,2\ell +1}\left(\ell -{\tfrac {1}{2}}\right)!{\left(\ell +g+{\tfrac {1}{2}}\right)}^{-(\ell +1/2)}e^{\ell +g+1/2}}
  

where 
  
    
      
        
          C
          
            n
            ,
            m
          
        
      
    
    {\displaystyle C_{n,m}}
  
 represents the (n, m)th element of the matrix of coefficients for the Chebyshev polynomials, which can be calculated recursively from these identities:

  
    
      
        
          
            
              
                
                  C
                  
                    1
                    ,
                    
                    1
                  
                
              
              
                
                =
                1
              
            
            
              
                
                  C
                  
                    2
                    ,
                    
                    2
                  
                
              
              
                
                =
                1
              
            
            
              
                
                  C
                  
                    n
                    +
                    1
                    ,
                    
                    1
                  
                
              
              
                
                =
                −
                
                
                  C
                  
                    n
                    −
                    1
                    ,
                    
                    1
                  
                
              
              
                
                   for 
                
                n
              
              
                
                =
                2
                ,
                3
                ,
                4
                
                …
              
            
            
              
                
                  C
                  
                    n
                    +
                    1
                    ,
                    
                    n
                    +
                    1
                  
                
              
              
                
                =
                2
                
                
                  C
                  
                    n
                    ,
                    
                    n
                  
                
              
              
                
                   for 
                
                n
              
              
                
                =
                2
                ,
                3
                ,
                4
                
                …
              
            
            
              
                
                  C
                  
                    n
                    +
                    1
                    ,
                    
                    m
                    +
                    1
                  
                
              
              
                
                =
                2
                
                
                  C
                  
                    n
                    ,
                    
                    m
                  
                
                −
                
                  C
                  
                    n
                    −
                    1
                    ,
                    
                    m
                    +
                    1
                  
                
              
              
                
                   for 
                
                n
              
              
                
                >
                m
                =
                1
                ,
                2
                ,
                3
                
                …
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}C_{1,\,1}&=1\\[5px]C_{2,\,2}&=1\\[5px]C_{n+1,\,1}&=-\,C_{n-1,\,1}&{\text{ for  }}n&=2,3,4\,\dots \\[5px]C_{n+1,\,n+1}&=2\,C_{n,\,n}&{\text{ for  }}n&=2,3,4\,\dots \\[5px]C_{n+1,\,m+1}&=2\,C_{n,\,m}-C_{n-1,\,m+1}&{\text{ for  }}n&>m=1,2,3\,\dots \end{aligned}}}
  

Godfrey (2001) describes how to obtain the coefficients and also the value of the truncated series A as a matrix product.

Derivation
Lanczos derived the formula from Leonhard Euler's integral

  
    
      
        Γ
        (
        z
        +
        1
        )
        =
        
          ∫
          
            0
          
          
            ∞
          
        
        
          t
          
            z
          
        
        
        
          e
          
            −
            t
          
        
        
        d
        t
        ,
      
    
    {\displaystyle \Gamma (z+1)=\int _{0}^{\infty }t^{z}\,e^{-t}\,dt,}
  

performing a sequence of basic manipulations to obtain

  
    
      
        Γ
        (
        z
        +
        1
        )
        =
        (
        z
        +
        g
        +
        1
        
          )
          
            z
            +
            1
          
        
        
          e
          
            −
            (
            z
            +
            g
            +
            1
            )
          
        
        
          ∫
          
            0
          
          
            e
          
        
        
          
            (
          
        
        v
        (
        1
        −
        log
        ⁡
        v
        )
        
          
            
              )
            
          
          
            z
          
        
        
          v
          
            g
          
        
        
        d
        v
        ,
      
    
    {\displaystyle \Gamma (z+1)=(z+g+1)^{z+1}e^{-(z+g+1)}\int _{0}^{e}{\Big (}v(1-\log v){\Big )}^{z}v^{g}\,dv,}
  

and deriving a series for the integral.

Simple implementation
The following implementation in the Python programming language works for complex arguments and typically gives 13 correct decimal places.
Note that omitting the smallest coefficients (in pursuit of speed, for example) gives totally inaccurate results; the coefficients must be recomputed from scratch for an expansion with fewer terms.

See also
Stirling's approximation
Spouge's approximation

References

Godfrey, Paul (2001). "Lanczos Implementation of the Gamma Function".
Lanczos, Cornelius (1964). "A Precision Approximation of the Gamma Function". Journal of the Society for Industrial and Applied Mathematics, Series B: Numerical Analysis. 1 (1): 86–96. Bibcode:1964SJNA....1...86L. doi:10.1137/0701008. ISSN 0887-459X. JSTOR 2949767.
Press, W. H.; Teukolsky, S. A.; Vetterling, W. T.; Flannery, B. P. (2007), "Section 6.1. Gamma Function", Numerical Recipes: The Art of Scientific Computing (3rd ed.), New York: Cambridge University Press, ISBN 978-0-521-88068-8
Pugh, Glendon (2004). An analysis of the Lanczos Gamma approximation (PDF) (PhD thesis).
Toth, Viktor (2005). "Programmable Calculators: The Lanczos Approximation".
Weisstein, Eric W. "Lanczos Approximation". MathWorld.

## Archive Info
- **Archived on:** 2024-12-15 20:38:23 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 13986 bytes
- **Word Count:** 890 words
