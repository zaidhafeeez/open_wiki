# Machine epsilon

## Metadata
- **Last Updated:** 2024-12-03 06:59:51 UTC
- **Original Article:** [Machine epsilon](https://en.wikipedia.org/wiki/Machine_epsilon)
- **Language:** en
- **Page ID:** 3076863

## Summary
Machine epsilon or machine precision is an upper bound on the relative approximation error due to rounding in floating point number systems. This value characterizes computer arithmetic in the field of numerical analysis, and by extension in the subject of computational science. The quantity is also called macheps and it has the symbols Greek epsilon 
  
    
      
        ε
      
    
    {\displaystyle \varepsilon }
  
.
There are two prevailing definitions, denoted here as rounding machine epsilon or the formal definition and interval machine epsilon or mainstream definition.
In the mainstream definition, machine epsilon is independent of rounding method, and is defined simply as the difference between 1 and the next larger floating point number.
In the formal definition, machine epsilon is dependent on the type of rounding used and is also called unit roundoff, which has the symbol bold Roman u.
The two terms can generally be considered to differ by simply a factor of two, with the formal definition yielding an epsilon half the size of the mainstream definition, as summarized in the tables in the next section.

## Categories
This article belongs to the following categories:

- Category:Articles with example C code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Computer arithmetic
- Category:Short description is different from Wikidata
- Category:Wikipedia articles needing clarification from March 2021

## Table of Contents

- Values for standard hardware arithmetics
- Alternative definitions for epsilon
- How to determine machine epsilon
- Relationship to absolute relative error
- See also
- Notes and references
- External links

## Content

Machine epsilon or machine precision is an upper bound on the relative approximation error due to rounding in floating point number systems. This value characterizes computer arithmetic in the field of numerical analysis, and by extension in the subject of computational science. The quantity is also called macheps and it has the symbols Greek epsilon 
  
    
      
        ε
      
    
    {\displaystyle \varepsilon }
  
.
There are two prevailing definitions, denoted here as rounding machine epsilon or the formal definition and interval machine epsilon or mainstream definition.
In the mainstream definition, machine epsilon is independent of rounding method, and is defined simply as the difference between 1 and the next larger floating point number.
In the formal definition, machine epsilon is dependent on the type of rounding used and is also called unit roundoff, which has the symbol bold Roman u.
The two terms can generally be considered to differ by simply a factor of two, with the formal definition yielding an epsilon half the size of the mainstream definition, as summarized in the tables in the next section.

Values for standard hardware arithmetics
The following table lists machine epsilon values for standard floating-point formats.

Alternative definitions for epsilon
The IEEE standard does not define the terms machine epsilon and unit roundoff, so differing definitions of these terms are in use, which can cause some confusion.
The two terms differ by simply a factor of two.  The more-widely used term (referred to as the mainstream definition in this article), is used in most modern programming languages and is simply defined as machine epsilon is the difference between 1 and the next larger floating point number.  The formal definition can generally be considered to yield an epsilon half the size of the mainstream definition, although its definition does vary depending on the form of rounding used.
The two terms are described at length in the next two subsections.

Formal definition (Rounding machine epsilon)
The formal definition for machine epsilon is the one used by Prof. James Demmel in lecture scripts, the LAPACK linear algebra package, numerics research papers and some scientific computing software.  Most numerical analysts use the words machine epsilon and unit roundoff interchangeably with this meaning, which is explored in depth throughout this subsection.
Rounding is a procedure for choosing the representation of a real number in a floating point number system.  For a number system and a rounding procedure, machine epsilon is the maximum relative error of the chosen rounding procedure.
Some background is needed to determine a value from this definition. A floating point number system is characterized by a radix which is also called the base, 
  
    
      
        b
      
    
    {\displaystyle b}
  
, and by the precision 
  
    
      
        p
      
    
    {\displaystyle p}
  
, i.e. the number of radix 
  
    
      
        b
      
    
    {\displaystyle b}
  
 digits of the significand (including any leading implicit bit). All the numbers with the same exponent, 
  
    
      
        e
      
    
    {\displaystyle e}
  
, have the spacing, 
  
    
      
        
          b
          
            e
            −
            (
            p
            −
            1
            )
          
        
      
    
    {\displaystyle b^{e-(p-1)}}
  
. The spacing changes at the numbers that are perfect powers of 
  
    
      
        b
      
    
    {\displaystyle b}
  
; the spacing on the side of larger magnitude is 
  
    
      
        b
      
    
    {\displaystyle b}
  
 times larger than the spacing on the side of smaller magnitude.
Since machine epsilon is a bound for relative error, it suffices to consider numbers with exponent 
  
    
      
        e
        =
        0
      
    
    {\displaystyle e=0}
  
. It also suffices to consider positive numbers. For the usual round-to-nearest kind of rounding, the absolute rounding error is at most half the spacing, or 
  
    
      
        
          b
          
            −
            (
            p
            −
            1
            )
          
        
        
          /
        
        2
      
    
    {\displaystyle b^{-(p-1)}/2}
  
. This value is the biggest possible numerator for the relative error. The denominator in the relative error is the number being rounded, which should be as small as possible to make the relative error large. The worst relative error therefore happens when rounding is applied to numbers of the form 
  
    
      
        1
        +
        a
      
    
    {\displaystyle 1+a}
  
 where 
  
    
      
        a
      
    
    {\displaystyle a}
  
 is between 
  
    
      
        0
      
    
    {\displaystyle 0}
  
 and 
  
    
      
        
          b
          
            −
            (
            p
            −
            1
            )
          
        
        
          /
        
        2
      
    
    {\displaystyle b^{-(p-1)}/2}
  
. All these numbers round to 
  
    
      
        1
      
    
    {\displaystyle 1}
  
 with relative error 
  
    
      
        a
        
          /
        
        (
        1
        +
        a
        )
      
    
    {\displaystyle a/(1+a)}
  
. The maximum occurs when 
  
    
      
        a
      
    
    {\displaystyle a}
  
 is at the upper end of its range. The 
  
    
      
        1
        +
        a
      
    
    {\displaystyle 1+a}
  
 in the denominator is negligible compared to the numerator, so it is left off for expediency, and just 
  
    
      
        
          b
          
            −
            (
            p
            −
            1
            )
          
        
        
          /
        
        2
      
    
    {\displaystyle b^{-(p-1)}/2}
  
 is taken as machine epsilon. As has been shown here, the relative error is worst for numbers that round to 
  
    
      
        1
      
    
    {\displaystyle 1}
  
, so machine epsilon also is called unit roundoff meaning roughly "the maximum error that can occur when rounding to the unit value".
Thus, the maximum spacing between a normalised floating point number, 
  
    
      
        x
      
    
    {\displaystyle x}
  
, and an adjacent normalised number is 
  
    
      
        2
        ε
        
          |
        
        x
        
          |
        
      
    
    {\displaystyle 2\varepsilon |x|}
  
.

Arithmetic model
Numerical analysis uses machine epsilon to study the effects of rounding error. The actual errors of machine arithmetic are far too complicated to be studied directly, so instead, the following simple model is used. The IEEE arithmetic standard says all floating-point operations are done as if it were possible to perform the infinite-precision operation, and then, the result is rounded to a floating-point number. Suppose (1) 
  
    
      
        x
      
    
    {\displaystyle x}
  
, 
  
    
      
        y
      
    
    {\displaystyle y}
  
 are floating-point numbers, (2) 
  
    
      
        ∙
      
    
    {\displaystyle \bullet }
  
 is an arithmetic operation on floating-point numbers such as addition or multiplication, and (3) 
  
    
      
        ∘
      
    
    {\displaystyle \circ }
  
 is the infinite precision operation. According to the standard, the computer calculates:

  
    
      
        x
        ∙
        y
        =
        
          
            round
          
        
        (
        x
        ∘
        y
        )
      
    
    {\displaystyle x\bullet y={\mbox{round}}(x\circ y)}
  

By the meaning of machine epsilon, the relative error of the rounding is at most machine epsilon in magnitude, so:

  
    
      
        x
        ∙
        y
        =
        (
        x
        ∘
        y
        )
        (
        1
        +
        z
        )
      
    
    {\displaystyle x\bullet y=(x\circ y)(1+z)}
  

where 
  
    
      
        z
      
    
    {\displaystyle z}
  
 in absolute magnitude is at most 
  
    
      
        ε
      
    
    {\displaystyle \varepsilon }
  
 or u. The books by Demmel and Higham in the references can be consulted to see how this model is used to analyze the errors of, say, Gaussian elimination.

Mainstream definition (Interval machine epsilon)
This alternative definition is significantly more widespread: machine epsilon is the difference between 1 and the next larger floating point number.  This definition is used in language constants in Ada, C, C++, Fortran, MATLAB, Mathematica, Octave, Pascal, Python and Rust etc., and defined in textbooks like «Numerical Recipes» by Press et al.
By this definition, ε equals the value of the unit in the last place relative to 1, i.e. 
  
    
      
        
          b
          
            −
            (
            p
            −
            1
            )
          
        
      
    
    {\displaystyle b^{-(p-1)}}
  
 (where b is the base of the floating point system and p is the precision) and the unit roundoff is u = ε / 2, assuming round-to-nearest mode, and u = ε, assuming round-by-chop.
The prevalence of this definition is rooted in its use in the ISO C Standard for constants relating to floating-point types and corresponding constants in other programming languages. It is also widely used in scientific computing software and in the numerics and computing literature.

How to determine machine epsilon
Where standard libraries do not provide precomputed values (as <float.h> does with FLT_EPSILON, DBL_EPSILON and LDBL_EPSILON for C and <limits> does with std::numeric_limits<T>::epsilon() in C++), the best way to determine machine epsilon is to refer to the table, above, and use the appropriate power formula.  Computing machine epsilon is often given as a textbook exercise. The following examples compute interval machine epsilon in the sense of the spacing of the floating point numbers at 1 rather than in the sense of the unit roundoff.
Note that results depend on the particular floating-point format used, such as float, double, long double, or similar as supported by the programming language, the compiler, and the runtime library for the actual platform.
Some formats supported by the processor might not be supported by the chosen compiler and operating system. Other formats might be emulated by the runtime library, including arbitrary-precision arithmetic available in some languages and libraries.
In a strict sense the term machine epsilon means the 
  
    
      
        1
        +
        ε
      
    
    {\displaystyle 1+\varepsilon }
  
 accuracy directly supported by the processor (or coprocessor), not some 
  
    
      
        1
        +
        ε
      
    
    {\displaystyle 1+\varepsilon }
  
 accuracy supported by a specific compiler for a specific operating system, unless it's known to use the best format.
IEEE 754 floating-point formats have the property that, when reinterpreted as a two's complement integer of the same width, they monotonically increase over positive values and monotonically decrease over negative values (see the binary representation of 32 bit floats). They also have the property that 
  
    
      
        0
        <
        
          |
        
        f
        (
        x
        )
        
          |
        
        <
        ∞
      
    
    {\displaystyle 0<|f(x)|<\infty }
  
, and 
  
    
      
        
          |
        
        f
        (
        x
        +
        1
        )
        −
        f
        (
        x
        )
        
          |
        
        ≥
        
          |
        
        f
        (
        x
        )
        −
        f
        (
        x
        −
        1
        )
        
          |
        
      
    
    {\displaystyle |f(x+1)-f(x)|\geq |f(x)-f(x-1)|}
  
 (where 
  
    
      
        f
        (
        x
        )
      
    
    {\displaystyle f(x)}
  
 is the aforementioned integer reinterpretation of 
  
    
      
        x
      
    
    {\displaystyle x}
  
). In languages that allow type punning and always use IEEE 754–1985, we can exploit this to compute a machine epsilon in constant time. For example, in C:

This will give a result of the same sign as value. If a positive result is always desired, the return statement of machine_eps can be replaced with:

Example in Python:

64-bit doubles give 2.220446e-16, which is 2−52 as expected.

Approximation
The following simple algorithm can be used to approximate the machine epsilon, to within a factor of two (one order of magnitude) of its true value, using a linear search.

epsilon = 1.0;

while (1.0 + 0.5 * epsilon) ≠ 1.0:
    epsilon = 0.5 * epsilon

The machine epsilon, 
  
    
      
        
          ε
          
            mach
          
        
      
    
    {\textstyle \varepsilon _{\text{mach}}}
  
 can also simply be calculated as two to the negative power of the number of bits used for the mantissa.

  
    
      
        
          ε
          
            mach
          
        
         
        =
         
        
          2
          
            −
            
              bits used for magnitude of mantissa
            
          
        
      
    
    {\displaystyle \varepsilon _{\text{mach}}\ =\ 2^{-{\text{bits used for magnitude of mantissa}}}}

Relationship to absolute relative error
If 
  
    
      
        y
      
    
    {\textstyle y}
  
 is the machine representation of a number 
  
    
      
        x
      
    
    {\textstyle x}
  
 then the absolute relative error in the representation is 
  
    
      
        
          |
          
            
              
                
                  x
                  −
                  y
                
                x
              
            
          
          |
        
        ≤
        
          ε
          
            mach
          
        
        .
      
    
    {\textstyle \left|{\dfrac {x-y}{x}}\right|\leq \varepsilon _{\text{mach}}.}

Proof
The following proof is limited to positive numbers and machine representations using round-by-chop.
If 
  
    
      
        x
      
    
    {\textstyle x}
  
 is a positive number we want to represent, it will be between a machine number 
  
    
      
        
          x
          
            b
          
        
      
    
    {\textstyle x_{b}}
  
 below 
  
    
      
        x
      
    
    {\textstyle x}
  
 and a machine number 
  
    
      
        
          x
          
            u
          
        
      
    
    {\textstyle x_{u}}
  
 above 
  
    
      
        x
      
    
    {\textstyle x}
  
.
If 
  
    
      
        
          x
          
            b
          
        
        =
        
          
            (
            
              1.
              
                b
                
                  1
                
              
              
                b
                
                  2
                
              
              …
              
                b
                
                  m
                
              
            
            )
          
          
            2
          
        
        ×
        
          2
          
            k
          
        
      
    
    {\textstyle x_{b}=\left(1.b_{1}b_{2}\ldots b_{m}\right)_{2}\times 2^{k}}
  
, where 
  
    
      
        m
      
    
    {\textstyle m}
  
 is the number of bits used for the magnitude of the significand, then:

  
    
      
        
          
            
              
                
                  x
                  
                    u
                  
                
              
              
                
                =
                
                  [
                  
                    (
                    1.
                    
                      b
                      
                        1
                      
                    
                    
                      b
                      
                        2
                      
                    
                    …
                    
                      b
                      
                        m
                      
                    
                    
                      )
                      
                        2
                      
                    
                    +
                    (
                    0.00
                    …
                    1
                    
                      )
                      
                        2
                      
                    
                  
                  ]
                
                ×
                
                  2
                  
                    k
                  
                
              
            
            
              
              
                
                =
                
                  [
                  
                    (
                    1.
                    
                      b
                      
                        1
                      
                    
                    
                      b
                      
                        2
                      
                    
                    …
                    
                      b
                      
                        m
                      
                    
                    
                      )
                      
                        2
                      
                    
                    +
                    
                      2
                      
                        −
                        m
                      
                    
                  
                  ]
                
                ×
                
                  2
                  
                    k
                  
                
              
            
            
              
              
                
                =
                (
                1.
                
                  b
                  
                    1
                  
                
                
                  b
                  
                    2
                  
                
                …
                
                  b
                  
                    m
                  
                
                
                  )
                  
                    2
                  
                
                ×
                
                  2
                  
                    k
                  
                
                +
                
                  2
                  
                    −
                    m
                  
                
                ×
                
                  2
                  
                    k
                  
                
              
            
            
              
              
                
                =
                (
                1.
                
                  b
                  
                    1
                  
                
                
                  b
                  
                    2
                  
                
                …
                
                  b
                  
                    m
                  
                
                
                  )
                  
                    2
                  
                
                ×
                
                  2
                  
                    k
                  
                
                +
                
                  2
                  
                    −
                    m
                    +
                    k
                  
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}x_{u}&=\left[(1.b_{1}b_{2}\ldots b_{m})_{2}+(0.00\ldots 1)_{2}\right]\times 2^{k}\\&=\left[(1.b_{1}b_{2}\ldots b_{m})_{2}+2^{-m}\right]\times 2^{k}\\&=(1.b_{1}b_{2}\ldots b_{m})_{2}\times 2^{k}+2^{-m}\times 2^{k}\\&=(1.b_{1}b_{2}\ldots b_{m})_{2}\times 2^{k}+2^{-m+k}.\end{aligned}}}
  

Since the representation of 
  
    
      
        x
      
    
    {\textstyle x}
  
 will be either 
  
    
      
        
          x
          
            b
          
        
      
    
    {\textstyle x_{b}}
  
 or 
  
    
      
        
          x
          
            u
          
        
      
    
    {\textstyle x_{u}}
  
,

  
    
      
        
          
            
              
                
                  |
                  
                    x
                    −
                    y
                  
                  |
                
              
              
                
                ≤
                
                  |
                  
                    
                      x
                      
                        b
                      
                    
                    −
                    
                      x
                      
                        u
                      
                    
                  
                  |
                
              
            
            
              
              
                
                =
                
                  2
                  
                    −
                    m
                    +
                    k
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\left|x-y\right|&\leq \left|x_{b}-x_{u}\right|\\&=2^{-m+k}\end{aligned}}}
  
 

  
    
      
        
          
            
              
                
                  |
                  
                    
                      
                        x
                        −
                        y
                      
                      x
                    
                  
                  |
                
              
              
                
                ≤
                
                  
                    
                      2
                      
                        −
                        m
                        +
                        k
                      
                    
                    x
                  
                
              
            
            
              
              
                
                ≤
                
                  
                    
                      2
                      
                        −
                        m
                        +
                        k
                      
                    
                    
                      x
                      
                        b
                      
                    
                  
                
              
            
            
              
              
                
                =
                
                  
                    
                      2
                      
                        −
                        m
                        +
                        k
                      
                    
                    
                      (
                      1
                      ⋅
                      
                        b
                        
                          1
                        
                      
                      
                        b
                        
                          2
                        
                      
                      …
                      
                        b
                        
                          m
                        
                      
                      
                        )
                        
                          2
                        
                      
                      
                        2
                        
                          k
                        
                      
                    
                  
                
              
            
            
              
              
                
                =
                
                  
                    
                      2
                      
                        −
                        m
                      
                    
                    
                      (
                      1
                      ⋅
                      
                        b
                        
                          1
                        
                      
                      
                        b
                        
                          2
                        
                      
                      …
                      
                        b
                        
                          m
                        
                      
                      
                        )
                        
                          2
                        
                      
                    
                  
                
              
            
            
              
              
                
                ≤
                
                  2
                  
                    −
                    m
                  
                
                =
                
                  ε
                  
                    mach
                  
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\left|{\frac {x-y}{x}}\right|&\leq {\frac {2^{-m+k}}{x}}\\&\leq {\frac {2^{-m+k}}{x_{b}}}\\&={\frac {2^{-m+k}}{(1\cdot b_{1}b_{2}\ldots b_{m})_{2}2^{k}}}\\&={\frac {2^{-m}}{(1\cdot b_{1}b_{2}\ldots b_{m})_{2}}}\\&\leq 2^{-m}=\varepsilon _{\text{mach}}.\end{aligned}}}
  

Although this proof is limited to positive numbers and round-by-chop, the same method can be used to prove the inequality in relation to negative numbers and round-to-nearest machine representations.

See also
Floating point, general discussion of accuracy issues in floating point arithmetic
Unit in the last place (ULP)

Notes and references
External links
MACHAR, a routine (in C and Fortran) to "dynamically compute machine constants" (ACM algorithm 722)
Diagnosing floating point calculations precision, Implementation of MACHAR in Component Pascal and Oberon based on the Fortran 77 version of MACHAR published in Numerical Recipes (Press et al., 1992).

## Archive Info
- **Archived on:** 2024-12-15 20:26:34 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 27322 bytes
- **Word Count:** 2116 words
