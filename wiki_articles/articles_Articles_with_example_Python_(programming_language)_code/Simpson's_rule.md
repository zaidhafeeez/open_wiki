# Simpson's rule

## Article Metadata

- **Last Updated:** 2024-12-14T19:45:06.218761+00:00
- **Original Article:** [Simpson's rule](https://en.wikipedia.org/wiki/Simpson%27s_rule)
- **Language:** en
- **Page ID:** 219962

## Summary

In numerical integration, Simpson's rules are several approximations for definite integrals, named after Thomas Simpson (1710–1761).
The most basic of these rules, called Simpson's 1/3 rule, or just Simpson's rule, reads

  
    
      
        
          ∫
          
            a
          
          
            b
          
        
        f
        (
        x
        )
        
        d
        x
        ≈
        
          
            
              b
              −
              a
 

## Categories

- Category:Articles containing German-language text
- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with short description
- Category:Integral calculus
- Category:Numerical analysis
- Category:Numerical integration (quadrature)
- Category:Short description is different from Wikidata
- Category:Use dmy dates from January 2020
- Category:Wikipedia articles incorporating text from PlanetMath

## Table of Contents

- Simpson's 1/3 rule
- Simpson's 3/8 rule
- Alternative extended Simpson's rule
- Composite Simpson's rule for irregularly spaced data
- See also
- Notes
- References
- External links

## Content

In numerical integration, Simpson's rules are several approximations for definite integrals, named after Thomas Simpson (1710–1761).
The most basic of these rules, called Simpson's 1/3 rule, or just Simpson's rule, reads

  
    
      
        
          ∫
          
            a
          
          
            b
          
        
        f
        (
        x
        )
        
        d
        x
        ≈
        
          
            
              b
              −
              a
            
            6
          
        
        
          [
          
            f
            (
            a
            )
            +
            4
            f
            
              (
              
                
                  
                    a
                    +
                    b
                  
                  2
                
              
              )
            
            +
            f
            (
            b
            )
          
          ]
        
        .
      
    
    {\displaystyle \int _{a}^{b}f(x)\,dx\approx {\frac {b-a}{6}}\left[f(a)+4f\left({\frac {a+b}{2}}\right)+f(b)\right].}
  

In German and some other languages, it is named after Johannes Kepler, who derived it in 1615 after seeing it used for wine barrels (barrel rule, Keplersche Fassregel). The approximate equality in the rule becomes exact if f is a polynomial up to and including 3rd degree.
If the 1/3 rule is applied to n equal subdivisions of the integration range [a, b], one obtains the composite Simpson's 1/3 rule. Points inside the integration range are given alternating weights 4/3 and 2/3.
Simpson's 3/8 rule, also called Simpson's second rule, requires one more function evaluation inside the integration range and gives lower error bounds, but does not improve the order of the error.
If the 3/8 rule is applied to n equal subdivisions of the integration range [a, b], one obtains the composite Simpson's 3/8 rule.
Simpson's 1/3 and 3/8 rules are two special cases of closed Newton–Cotes formulas.
In naval architecture and ship stability estimation, there also exists Simpson's third rule, which has no special importance in general numerical analysis, see Simpson's rules (ship stability).

Simpson's 1/3 rule
Simpson's 1/3 rule, also simply called Simpson's rule, is a method for numerical integration proposed by Thomas Simpson. It is based upon a quadratic interpolation and is the composite Simpson's 1/3 rule evaluated for 
  
    
      
        n
        =
        2
      
    
    {\displaystyle n=2}
  
. Simpson's 1/3 rule is as follows:

  
    
      
        
          
            
              
                
                  ∫
                  
                    a
                  
                  
                    b
                  
                
                f
                (
                x
                )
                
                d
                x
              
              
                
                ≈
                
                  
                    
                      b
                      −
                      a
                    
                    6
                  
                
                
                  [
                  
                    f
                    (
                    a
                    )
                    +
                    4
                    f
                    
                      (
                      
                        
                          
                            a
                            +
                            b
                          
                          2
                        
                      
                      )
                    
                    +
                    f
                    (
                    b
                    )
                  
                  ]
                
              
            
            
              
              
                
                =
                
                  
                    1
                    3
                  
                
                h
                
                  [
                  
                    f
                    (
                    a
                    )
                    +
                    4
                    f
                    
                      (
                      
                        a
                        +
                        h
                      
                      )
                    
                    +
                    f
                    (
                    b
                    )
                  
                  ]
                
                ,
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\int _{a}^{b}f(x)\,dx&\approx {\frac {b-a}{6}}\left[f(a)+4f\left({\frac {a+b}{2}}\right)+f(b)\right]\\&={\frac {1}{3}}h\left[f(a)+4f\left(a+h\right)+f(b)\right],\end{aligned}}}
  

where 
  
    
      
        h
        =
        (
        b
        −
        a
        )
        
          /
        
        n
      
    
    {\displaystyle h=(b-a)/n}
  
 is the step size for 
  
    
      
        n
        =
        2
      
    
    {\displaystyle n=2}
  
.
The error in approximating an integral by Simpson's rule for 
  
    
      
        n
        =
        2
      
    
    {\displaystyle n=2}
  
 is

  
    
      
        −
        
          
            1
            90
          
        
        
          h
          
            5
          
        
        
          f
          
            (
            4
            )
          
        
        (
        ξ
        )
        =
        −
        
          
            
              (
              b
              −
              a
              
                )
                
                  5
                
              
            
            2880
          
        
        
          f
          
            (
            4
            )
          
        
        (
        ξ
        )
        ,
      
    
    {\displaystyle -{\frac {1}{90}}h^{5}f^{(4)}(\xi )=-{\frac {(b-a)^{5}}{2880}}f^{(4)}(\xi ),}
  

where 
  
    
      
        ξ
      
    
    {\displaystyle \xi }
  
 (the Greek letter xi) is some number between 
  
    
      
        a
      
    
    {\displaystyle a}
  
 and 
  
    
      
        b
      
    
    {\displaystyle b}
  
.
The error is asymptotically proportional to 
  
    
      
        (
        b
        −
        a
        
          )
          
            5
          
        
      
    
    {\displaystyle (b-a)^{5}}
  
. However, the above derivations suggest an error proportional to 
  
    
      
        (
        b
        −
        a
        
          )
          
            4
          
        
      
    
    {\displaystyle (b-a)^{4}}
  
. Simpson's rule gains an extra order because the points at which the integrand is evaluated are distributed symmetrically in the interval 
  
    
      
        [
        a
        ,
         
        b
        ]
      
    
    {\displaystyle [a,\ b]}
  
.
Since the error term is proportional to the fourth derivative of 
  
    
      
        f
      
    
    {\displaystyle f}
  
 at 
  
    
      
        ξ
      
    
    {\displaystyle \xi }
  
, this shows that Simpson's rule provides exact results for any polynomial 
  
    
      
        f
      
    
    {\displaystyle f}
  
 of degree three or less, since the fourth derivative of such a polynomial is zero at all points. Another way to see this result is to note that any interpolating cubic polynomial can be expressed as the sum of the unique interpolating quadratic polynomial plus an arbitrarily scaled cubic polynomial that vanishes at all three points in the interval, and the integral of this second term vanishes because it is odd within the interval.
If the second derivative 
  
    
      
        
          f
          ″
        
      
    
    {\displaystyle f''}
  
 exists and is convex in the interval 
  
    
      
        (
        a
        ,
         
        b
        )
      
    
    {\displaystyle (a,\ b)}
  
, then

  
    
      
        (
        b
        −
        a
        )
        f
        
          (
          
            
              
                a
                +
                b
              
              2
            
          
          )
        
        +
        
          
            1
            3
          
        
        
          
            (
            
              
                
                  b
                  −
                  a
                
                2
              
            
            )
          
          
            3
          
        
        
          f
          ″
        
        
          (
          
            
              
                a
                +
                b
              
              2
            
          
          )
        
        ≤
        
          ∫
          
            a
          
          
            b
          
        
        f
        (
        x
        )
        
        d
        x
        ≤
        
          
            
              b
              −
              a
            
            6
          
        
        
          [
          
            f
            (
            a
            )
            +
            4
            f
            
              (
              
                
                  
                    a
                    +
                    b
                  
                  2
                
              
              )
            
            +
            f
            (
            b
            )
          
          ]
        
        .
      
    
    {\displaystyle (b-a)f\left({\frac {a+b}{2}}\right)+{\frac {1}{3}}\left({\frac {b-a}{2}}\right)^{3}f''\left({\frac {a+b}{2}}\right)\leq \int _{a}^{b}f(x)\,dx\leq {\frac {b-a}{6}}\left[f(a)+4f\left({\frac {a+b}{2}}\right)+f(b)\right].}

Derivations
Quadratic interpolation
One derivation replaces the integrand 
  
    
      
        f
        (
        x
        )
      
    
    {\displaystyle f(x)}
  
 by the quadratic polynomial (i.e. parabola) 
  
    
      
        P
        (
        x
        )
      
    
    {\displaystyle P(x)}
  
 that takes the same values as 
  
    
      
        f
        (
        x
        )
      
    
    {\displaystyle f(x)}
  
 at the end points 
  
    
      
        a
      
    
    {\displaystyle a}
  
 and 
  
    
      
        b
      
    
    {\displaystyle b}
  
 and the midpoint 
  
    
      
        m
        =
        (
        a
        +
        b
        )
        
          /
        
        2
      
    
    {\displaystyle m=(a+b)/2}
  
. One can use Lagrange polynomial interpolation to find an expression for this polynomial,

  
    
      
        P
        (
        x
        )
        =
        f
        (
        a
        )
        
          
            
              (
              x
              −
              m
              )
              (
              x
              −
              b
              )
            
            
              (
              a
              −
              m
              )
              (
              a
              −
              b
              )
            
          
        
        +
        f
        (
        m
        )
        
          
            
              (
              x
              −
              a
              )
              (
              x
              −
              b
              )
            
            
              (
              m
              −
              a
              )
              (
              m
              −
              b
              )
            
          
        
        +
        f
        (
        b
        )
        
          
            
              (
              x
              −
              a
              )
              (
              x
              −
              m
              )
            
            
              (
              b
              −
              a
              )
              (
              b
              −
              m
              )
            
          
        
        .
      
    
    {\displaystyle P(x)=f(a){\frac {(x-m)(x-b)}{(a-m)(a-b)}}+f(m){\frac {(x-a)(x-b)}{(m-a)(m-b)}}+f(b){\frac {(x-a)(x-m)}{(b-a)(b-m)}}.}
  

Using integration by substitution, one can show that

  
    
      
        
          ∫
          
            a
          
          
            b
          
        
        P
        (
        x
        )
        
        d
        x
        =
        
          
            
              b
              −
              a
            
            6
          
        
        
          [
          
            f
            (
            a
            )
            +
            4
            f
            
              (
              
                
                  
                    a
                    +
                    b
                  
                  2
                
              
              )
            
            +
            f
            (
            b
            )
          
          ]
        
        .
      
    
    {\displaystyle \int _{a}^{b}P(x)\,dx={\frac {b-a}{6}}\left[f(a)+4f\left({\frac {a+b}{2}}\right)+f(b)\right].}
  

Introducing the step size 
  
    
      
        h
        =
        (
        b
        −
        a
        )
        
          /
        
        2
      
    
    {\displaystyle h=(b-a)/2}
  
, this is also commonly written as

  
    
      
        
          ∫
          
            a
          
          
            b
          
        
        P
        (
        x
        )
        
        d
        x
        =
        
          
            1
            3
          
        
        h
        
          [
          
            f
            (
            a
            )
            +
            4
            f
            
              (
              
                a
                +
                h
              
              )
            
            +
            f
            (
            b
            )
          
          ]
        
        .
      
    
    {\displaystyle \int _{a}^{b}P(x)\,dx={\frac {1}{3}}h\left[f(a)+4f\left(a+h\right)+f(b)\right].}
  

Because of the 
  
    
      
        1
        
          /
        
        3
      
    
    {\displaystyle 1/3}
  
 factor, Simpson's rule is also referred to as "Simpson's 1/3 rule" (see below for generalization).

Averaging the midpoint and the trapezoidal rules
Another derivation constructs Simpson's rule from two simpler approximations: the midpoint rule

  
    
      
        M
        =
        (
        b
        −
        a
        )
        f
        
          (
          
            
              
                a
                +
                b
              
              2
            
          
          )
        
      
    
    {\displaystyle M=(b-a)f\left({\frac {a+b}{2}}\right)}
  

and the trapezoidal rule

  
    
      
        T
        =
        
          
            1
            2
          
        
        (
        b
        −
        a
        )
        
          
            (
          
        
        f
        (
        a
        )
        +
        f
        (
        b
        )
        
          
            )
          
        
        .
      
    
    {\displaystyle T={\frac {1}{2}}(b-a){\big (}f(a)+f(b){\big )}.}
  

The errors in these approximations are

  
    
      
        
          
            1
            24
          
        
        (
        b
        −
        a
        
          )
          
            3
          
        
        
          f
          ″
        
        (
        a
        )
        +
        O
        
          
            (
          
        
        (
        b
        −
        a
        
          )
          
            4
          
        
        
          
            )
          
        
      
    
    {\displaystyle {\frac {1}{24}}(b-a)^{3}f''(a)+O{\big (}(b-a)^{4}{\big )}}
  

and

  
    
      
        −
        
          
            1
            12
          
        
        (
        b
        −
        a
        
          )
          
            3
          
        
        
          f
          ″
        
        (
        a
        )
        +
        O
        
          
            (
          
        
        (
        b
        −
        a
        
          )
          
            4
          
        
        
          
            )
          
        
      
    
    {\displaystyle -{\frac {1}{12}}(b-a)^{3}f''(a)+O{\big (}(b-a)^{4}{\big )}}
  

respectively, where 
  
    
      
        O
        
          
            (
          
        
        (
        b
        −
        a
        
          )
          
            4
          
        
        
          
            )
          
        
      
    
    {\displaystyle O{\big (}(b-a)^{4}{\big )}}
  
 denotes a term asymptotically proportional to 
  
    
      
        (
        b
        −
        a
        
          )
          
            4
          
        
      
    
    {\displaystyle (b-a)^{4}}
  
. The two 
  
    
      
        O
        
          
            (
          
        
        (
        b
        −
        a
        
          )
          
            4
          
        
        
          
            )
          
        
      
    
    {\displaystyle O{\big (}(b-a)^{4}{\big )}}
  
 terms are not equal; see Big O notation for more details. It follows from the above formulas for the errors of the midpoint and trapezoidal rule that the leading error term vanishes if we take the weighted average

  
    
      
        
          
            
              2
              M
              +
              T
            
            3
          
        
        .
      
    
    {\displaystyle {\frac {2M+T}{3}}.}
  

This weighted average is exactly Simpson's rule.
Using another approximation (for example, the trapezoidal rule with twice as many points), it is possible to take a suitable weighted average and eliminate another error term. This is Romberg's method.

Undetermined coefficients
The third derivation starts from the ansatz

  
    
      
        
          
            1
            
              b
              −
              a
            
          
        
        
          ∫
          
            a
          
          
            b
          
        
        f
        (
        x
        )
        
        d
        x
        ≈
        α
        f
        (
        a
        )
        +
        β
        f
        
          (
          
            
              
                a
                +
                b
              
              2
            
          
          )
        
        +
        γ
        f
        (
        b
        )
        .
      
    
    {\displaystyle {\frac {1}{b-a}}\int _{a}^{b}f(x)\,dx\approx \alpha f(a)+\beta f\left({\frac {a+b}{2}}\right)+\gamma f(b).}
  

The coefficients α, β and γ can be fixed by requiring that this approximation be exact for all quadratic polynomials. This yields Simpson's rule. (This derivation is essentially a less rigorous version of the quadratic interpolation derivation, where one saves significant calculation effort by guessing the correct functional form.)

Composite Simpson's 1/3 rule
If the interval of integration 
  
    
      
        [
        a
        ,
        b
        ]
      
    
    {\displaystyle [a,b]}
  
 is in some sense "small", then Simpson's rule with 
  
    
      
        n
        =
        2
      
    
    {\displaystyle n=2}
  
 subintervals will provide an adequate approximation to the exact integral. By "small" we mean that the function being integrated is relatively smooth over the interval 
  
    
      
        [
        a
        ,
        b
        ]
      
    
    {\displaystyle [a,b]}
  
. For such a function, a smooth quadratic interpolant like the one used in Simpson's rule will give good results.
However, it is often the case that the function we are trying to integrate is not smooth over the interval. Typically, this means that either the function is highly oscillatory or lacks derivatives at certain points. In these cases, Simpson's rule may give very poor results. One common way of handling this problem is by breaking up the interval 
  
    
      
        [
        a
        ,
        b
        ]
      
    
    {\displaystyle [a,b]}
  
 into 
  
    
      
        n
        >
        2
      
    
    {\displaystyle n>2}
  
 small subintervals. Simpson's rule is then applied to each subinterval, with the results being summed to produce an approximation for the integral over the entire interval. This sort of approach is termed the composite Simpson's 1/3 rule, or just composite Simpson's rule.
Suppose that the interval 
  
    
      
        [
        a
        ,
        b
        ]
      
    
    {\displaystyle [a,b]}
  
 is split up into 
  
    
      
        n
      
    
    {\displaystyle n}
  
 subintervals, with 
  
    
      
        n
      
    
    {\displaystyle n}
  
 an even number. Then, the composite Simpson's rule is given by
Dividing the interval 
  
    
      
        [
        a
        ,
        b
        ]
      
    
    {\displaystyle [a,b]}
  
 into 
  
    
      
        n
      
    
    {\displaystyle n}
  
 subintervals of length 
  
    
      
        h
        =
        (
        b
        −
        a
        )
        
          /
        
        n
      
    
    {\displaystyle h=(b-a)/n}
  
 and introducing the points 
  
    
      
        
          x
          
            i
          
        
        =
        a
        +
        i
        h
      
    
    {\displaystyle x_{i}=a+ih}
  
 for 
  
    
      
        0
        ≤
        i
        ≤
        n
      
    
    {\displaystyle 0\leq i\leq n}
  
 (in particular, 
  
    
      
        
          x
          
            0
          
        
        =
        a
      
    
    {\displaystyle x_{0}=a}
  
 and 
  
    
      
        
          x
          
            n
          
        
        =
        b
      
    
    {\displaystyle x_{n}=b}
  
), we have

  
    
      
        
          
            
              
                
                  ∫
                  
                    a
                  
                  
                    b
                  
                
                f
                (
                x
                )
                
                d
                x
              
              
                
                ≈
                
                  
                    1
                    3
                  
                
                h
                
                  ∑
                  
                    i
                    =
                    1
                  
                  
                    n
                    
                      /
                    
                    2
                  
                
                
                  
                    [
                  
                
                f
                (
                
                  x
                  
                    2
                    i
                    −
                    2
                  
                
                )
                +
                4
                f
                (
                
                  x
                  
                    2
                    i
                    −
                    1
                  
                
                )
                +
                f
                (
                
                  x
                  
                    2
                    i
                  
                
                )
                
                  
                    ]
                  
                
              
            
            
              
              
                
                =
                
                  
                    1
                    3
                  
                
                h
                
                  
                    [
                  
                
                f
                (
                
                  x
                  
                    0
                  
                
                )
                +
                4
                f
                (
                
                  x
                  
                    1
                  
                
                )
                +
                2
                f
                (
                
                  x
                  
                    2
                  
                
                )
                +
                4
                f
                (
                
                  x
                  
                    3
                  
                
                )
                +
                2
                f
                (
                
                  x
                  
                    4
                  
                
                )
                +
                ⋯
                +
                2
                f
                (
                
                  x
                  
                    n
                    −
                    2
                  
                
                )
                +
                4
                f
                (
                
                  x
                  
                    n
                    −
                    1
                  
                
                )
                +
                f
                (
                
                  x
                  
                    n
                  
                
                )
                
                  
                    ]
                  
                
              
            
            
              
              
                
                =
                
                  
                    1
                    3
                  
                
                h
                
                  [
                  
                    f
                    (
                    
                      x
                      
                        0
                      
                    
                    )
                    +
                    4
                    
                      ∑
                      
                        i
                        =
                        1
                      
                      
                        n
                        
                          /
                        
                        2
                      
                    
                    f
                    (
                    
                      x
                      
                        2
                        i
                        −
                        1
                      
                    
                    )
                    +
                    2
                    
                      ∑
                      
                        i
                        =
                        1
                      
                      
                        n
                        
                          /
                        
                        2
                        −
                        1
                      
                    
                    f
                    (
                    
                      x
                      
                        2
                        i
                      
                    
                    )
                    +
                    f
                    (
                    
                      x
                      
                        n
                      
                    
                    )
                  
                  ]
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\int _{a}^{b}f(x)\,dx&\approx {\frac {1}{3}}h\sum _{i=1}^{n/2}{\big [}f(x_{2i-2})+4f(x_{2i-1})+f(x_{2i}){\big ]}\\&={\frac {1}{3}}h{\big [}f(x_{0})+4f(x_{1})+2f(x_{2})+4f(x_{3})+2f(x_{4})+\dots +2f(x_{n-2})+4f(x_{n-1})+f(x_{n}){\big ]}\\&={\frac {1}{3}}h\left[f(x_{0})+4\sum _{i=1}^{n/2}f(x_{2i-1})+2\sum _{i=1}^{n/2-1}f(x_{2i})+f(x_{n})\right].\end{aligned}}}
  

This composite rule with 
  
    
      
        n
        =
        2
      
    
    {\displaystyle n=2}
  
 corresponds with the regular Simpson's rule of the preceding section.
The error committed by the composite Simpson's rule is

  
    
      
        −
        
          
            1
            180
          
        
        
          h
          
            4
          
        
        (
        b
        −
        a
        )
        
          f
          
            (
            4
            )
          
        
        (
        ξ
        )
        ,
      
    
    {\displaystyle -{\frac {1}{180}}h^{4}(b-a)f^{(4)}(\xi ),}
  

where 
  
    
      
        ξ
      
    
    {\displaystyle \xi }
  
 is some number between 
  
    
      
        a
      
    
    {\displaystyle a}
  
 and 
  
    
      
        b
      
    
    {\displaystyle b}
  
, and 
  
    
      
        h
        =
        (
        b
        −
        a
        )
        
          /
        
        n
      
    
    {\displaystyle h=(b-a)/n}
  
 is the "step length". The error is bounded (in absolute value) by

  
    
      
        
          
            1
            180
          
        
        
          h
          
            4
          
        
        (
        b
        −
        a
        )
        
          max
          
            ξ
            ∈
            [
            a
            ,
            b
            ]
          
        
        
          |
          
            
              f
              
                (
                4
                )
              
            
            (
            ξ
            )
          
          |
        
        .
      
    
    {\displaystyle {\frac {1}{180}}h^{4}(b-a)\max _{\xi \in [a,b]}\left|f^{(4)}(\xi )\right|.}
  

This formulation splits the interval 
  
    
      
        [
        a
        ,
        b
        ]
      
    
    {\displaystyle [a,b]}
  
 in subintervals of equal length. In practice, it is often advantageous to use subintervals of different lengths and concentrate the efforts on the places where the integrand is less well-behaved. This leads to the adaptive Simpson's method.

Simpson's 3/8 rule
Simpson's 3/8 rule, also called Simpson's second rule, is another method for numerical integration proposed by Thomas Simpson. It is based upon a cubic interpolation rather than a quadratic interpolation. Simpson's 3/8 rule is as follows:

  
    
      
        
          
            
              
                
                  ∫
                  
                    a
                  
                  
                    b
                  
                
                f
                (
                x
                )
                
                d
                x
              
              
                
                ≈
                
                  
                    
                      b
                      −
                      a
                    
                    8
                  
                
                
                  [
                  
                    f
                    (
                    a
                    )
                    +
                    3
                    f
                    
                      (
                      
                        
                          
                            2
                            a
                            +
                            b
                          
                          3
                        
                      
                      )
                    
                    +
                    3
                    f
                    
                      (
                      
                        
                          
                            a
                            +
                            2
                            b
                          
                          3
                        
                      
                      )
                    
                    +
                    f
                    (
                    b
                    )
                  
                  ]
                
              
            
            
              
              
                
                =
                
                  
                    3
                    8
                  
                
                h
                
                  [
                  
                    f
                    (
                    a
                    )
                    +
                    3
                    f
                    
                      (
                      
                        a
                        +
                        h
                      
                      )
                    
                    +
                    3
                    f
                    
                      (
                      
                        a
                        +
                        2
                        h
                      
                      )
                    
                    +
                    f
                    (
                    b
                    )
                  
                  ]
                
                ,
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\int _{a}^{b}f(x)\,dx&\approx {\frac {b-a}{8}}\left[f(a)+3f\left({\frac {2a+b}{3}}\right)+3f\left({\frac {a+2b}{3}}\right)+f(b)\right]\\&={\frac {3}{8}}h\left[f(a)+3f\left(a+h\right)+3f\left(a+2h\right)+f(b)\right],\end{aligned}}}
  

where 
  
    
      
        h
        =
        (
        b
        −
        a
        )
        
          /
        
        3
      
    
    {\displaystyle h=(b-a)/3}
  
 is the step size.
The error of this method is

  
    
      
        −
        
          
            3
            80
          
        
        
          h
          
            5
          
        
        
          f
          
            (
            4
            )
          
        
        (
        ξ
        )
        =
        −
        
          
            
              (
              b
              −
              a
              
                )
                
                  5
                
              
            
            6480
          
        
        
          f
          
            (
            4
            )
          
        
        (
        ξ
        )
        ,
      
    
    {\displaystyle -{\frac {3}{80}}h^{5}f^{(4)}(\xi )=-{\frac {(b-a)^{5}}{6480}}f^{(4)}(\xi ),}
  

where 
  
    
      
        ξ
      
    
    {\displaystyle \xi }
  
 is some number between 
  
    
      
        a
      
    
    {\displaystyle a}
  
 and 
  
    
      
        b
      
    
    {\displaystyle b}
  
. Thus, the 3/8 rule is about twice as accurate as the standard method, but it uses one more function value. A composite 3/8 rule also exists, similarly as above.
A further generalization of this concept for interpolation with arbitrary-degree polynomials are the Newton–Cotes formulas.

Composite Simpson's 3/8 rule
Dividing the interval 
  
    
      
        [
        a
        ,
        b
        ]
      
    
    {\displaystyle [a,b]}
  
 into 
  
    
      
        n
      
    
    {\displaystyle n}
  
 subintervals of length 
  
    
      
        h
        =
        (
        b
        −
        a
        )
        
          /
        
        n
      
    
    {\displaystyle h=(b-a)/n}
  
 and introducing the points 
  
    
      
        
          x
          
            i
          
        
        =
        a
        +
        i
        h
      
    
    {\displaystyle x_{i}=a+ih}
  
 for 
  
    
      
        0
        ≤
        i
        ≤
        n
      
    
    {\displaystyle 0\leq i\leq n}
  
 (in particular, 
  
    
      
        
          x
          
            0
          
        
        =
        a
      
    
    {\displaystyle x_{0}=a}
  
 and 
  
    
      
        
          x
          
            n
          
        
        =
        b
      
    
    {\displaystyle x_{n}=b}
  
), we have

  
    
      
        
          
            
              
                
                  ∫
                  
                    a
                  
                  
                    b
                  
                
                f
                (
                x
                )
                
                d
                x
              
              
                
                ≈
                
                  
                    3
                    8
                  
                
                h
                
                  ∑
                  
                    i
                    =
                    1
                  
                  
                    n
                    
                      /
                    
                    3
                  
                
                
                  
                    [
                  
                
                f
                (
                
                  x
                  
                    3
                    i
                    −
                    3
                  
                
                )
                +
                3
                f
                (
                
                  x
                  
                    3
                    i
                    −
                    2
                  
                
                )
                +
                3
                f
                (
                
                  x
                  
                    3
                    i
                    −
                    1
                  
                
                )
                +
                f
                (
                
                  x
                  
                    3
                    i
                  
                
                )
                
                  
                    ]
                  
                
              
            
            
              
              
                
                =
                
                  
                    3
                    8
                  
                
                h
                
                  
                    [
                  
                
                f
                (
                
                  x
                  
                    0
                  
                
                )
                +
                3
                f
                (
                
                  x
                  
                    1
                  
                
                )
                +
                3
                f
                (
                
                  x
                  
                    2
                  
                
                )
                +
                2
                f
                (
                
                  x
                  
                    3
                  
                
                )
                +
                3
                f
                (
                
                  x
                  
                    4
                  
                
                )
                +
                3
                f
                (
                
                  x
                  
                    5
                  
                
                )
                +
                2
                f
                (
                
                  x
                  
                    6
                  
                
                )
                +
                …
              
            
            
              
              
                
                
                +
                2
                f
                (
                
                  x
                  
                    n
                    −
                    3
                  
                
                )
                +
                3
                f
                (
                
                  x
                  
                    n
                    −
                    2
                  
                
                )
                +
                3
                f
                (
                
                  x
                  
                    n
                    −
                    1
                  
                
                )
                +
                f
                (
                
                  x
                  
                    n
                  
                
                )
                
                  
                    ]
                  
                
              
            
            
              
              
                
                =
                
                  
                    3
                    8
                  
                
                h
                
                  [
                  
                    f
                    (
                    
                      x
                      
                        0
                      
                    
                    )
                    +
                    3
                    
                      ∑
                      
                        i
                        =
                        1
                        ,
                         
                        3
                        ∤
                        i
                      
                      
                        n
                        −
                        1
                      
                    
                    f
                    (
                    
                      x
                      
                        i
                      
                    
                    )
                    +
                    2
                    
                      ∑
                      
                        i
                        =
                        1
                      
                      
                        n
                        
                          /
                        
                        3
                        −
                        1
                      
                    
                    f
                    (
                    
                      x
                      
                        3
                        i
                      
                    
                    )
                    +
                    f
                    (
                    
                      x
                      
                        n
                      
                    
                    )
                  
                  ]
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\int _{a}^{b}f(x)\,dx&\approx {\frac {3}{8}}h\sum _{i=1}^{n/3}{\big [}f(x_{3i-3})+3f(x_{3i-2})+3f(x_{3i-1})+f(x_{3i}){\big ]}\\&={\frac {3}{8}}h{\big [}f(x_{0})+3f(x_{1})+3f(x_{2})+2f(x_{3})+3f(x_{4})+3f(x_{5})+2f(x_{6})+\dots \\&\qquad +2f(x_{n-3})+3f(x_{n-2})+3f(x_{n-1})+f(x_{n}){\big ]}\\&={\frac {3}{8}}h\left[f(x_{0})+3\sum _{i=1,\ 3\nmid i}^{n-1}f(x_{i})+2\sum _{i=1}^{n/3-1}f(x_{3i})+f(x_{n})\right].\end{aligned}}}
  

While the remainder for the rule is shown as

  
    
      
        −
        
          
            1
            80
          
        
        
          h
          
            4
          
        
        (
        b
        −
        a
        )
        
          f
          
            (
            4
            )
          
        
        (
        ξ
        )
        ,
      
    
    {\displaystyle -{\frac {1}{80}}h^{4}(b-a)f^{(4)}(\xi ),}
  

we can only use this if 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is a multiple of three. The 1/3 rule can be used for the remaining subintervals without changing the order of the error term (conversely, the 3/8 rule can be used with a composite 1/3 rule for odd-numbered subintervals).

Alternative extended Simpson's rule
This is another formulation of a composite Simpson's rule: instead of applying Simpson's rule to disjoint segments of the integral to be approximated, Simpson's rule is applied to overlapping segments, yielding

  
    
      
        
          ∫
          
            a
          
          
            b
          
        
        f
        (
        x
        )
        
        d
        x
        ≈
        
          
            1
            48
          
        
        h
        
          [
          
            17
            f
            (
            
              x
              
                0
              
            
            )
            +
            59
            f
            (
            
              x
              
                1
              
            
            )
            +
            43
            f
            (
            
              x
              
                2
              
            
            )
            +
            49
            f
            (
            
              x
              
                3
              
            
            )
            +
            48
            
              ∑
              
                i
                =
                4
              
              
                n
                −
                4
              
            
            f
            (
            
              x
              
                i
              
            
            )
            +
            49
            f
            (
            
              x
              
                n
                −
                3
              
            
            )
            +
            43
            f
            (
            
              x
              
                n
                −
                2
              
            
            )
            +
            59
            f
            (
            
              x
              
                n
                −
                1
              
            
            )
            +
            17
            f
            (
            
              x
              
                n
              
            
            )
          
          ]
        
        .
      
    
    {\displaystyle \int _{a}^{b}f(x)\,dx\approx {\frac {1}{48}}h\left[17f(x_{0})+59f(x_{1})+43f(x_{2})+49f(x_{3})+48\sum _{i=4}^{n-4}f(x_{i})+49f(x_{n-3})+43f(x_{n-2})+59f(x_{n-1})+17f(x_{n})\right].}
  

The formula above is obtained by combining the composite Simpson's 1/3 rule with the one consisting of using Simpson's 3/8 rule in the extreme subintervals and Simpson's 1/3 rule in the remaining subintervals. The result is then obtained by taking the mean of the two formulas.

Simpson's rules in the case of narrow peaks
In the task of estimation of full area of narrow peak-like functions, Simpson's rules are much less efficient than trapezoidal rule. Namely, composite Simpson's 1/3 rule requires 1.8 times more points to achieve the same accuracy as trapezoidal rule. Composite Simpson's 3/8 rule is even less accurate. Integration by Simpson's 1/3 rule can be represented as a weighted average with 2/3 of the value coming from integration by the trapezoidal rule with step h and 1/3 of the value coming from integration by the rectangle rule with step 2h. The accuracy is governed by the second (2h step) term. Averaging of Simpson's 1/3 rule composite sums with properly shifted frames produces the following rules:

  
    
      
        
          ∫
          
            a
          
          
            b
          
        
        f
        (
        x
        )
        
        d
        x
        ≈
        
          
            1
            24
          
        
        h
        
          [
          
            −
            f
            (
            
              x
              
                −
                1
              
            
            )
            +
            12
            f
            (
            
              x
              
                0
              
            
            )
            +
            25
            f
            (
            
              x
              
                1
              
            
            )
            +
            24
            
              ∑
              
                i
                =
                2
              
              
                n
                −
                2
              
            
            f
            (
            
              x
              
                i
              
            
            )
            +
            25
            f
            (
            
              x
              
                n
                −
                1
              
            
            )
            +
            12
            f
            (
            
              x
              
                n
              
            
            )
            −
            f
            (
            
              x
              
                n
                +
                1
              
            
            )
          
          ]
        
        ,
      
    
    {\displaystyle \int _{a}^{b}f(x)\,dx\approx {\frac {1}{24}}h\left[-f(x_{-1})+12f(x_{0})+25f(x_{1})+24\sum _{i=2}^{n-2}f(x_{i})+25f(x_{n-1})+12f(x_{n})-f(x_{n+1})\right],}
  

where two points outside of the integrated region are exploited, and 

  
    
      
        
          ∫
          
            a
          
          
            b
          
        
        f
        (
        x
        )
        
        d
        x
        ≈
        
          
            1
            24
          
        
        h
        
          [
          
            9
            f
            (
            
              x
              
                0
              
            
            )
            +
            28
            f
            (
            
              x
              
                1
              
            
            )
            +
            23
            f
            (
            
              x
              
                2
              
            
            )
            +
            24
            
              ∑
              
                i
                =
                3
              
              
                n
                −
                3
              
            
            f
            (
            
              x
              
                i
              
            
            )
            +
            23
            f
            (
            
              x
              
                n
                −
                2
              
            
            )
            +
            28
            f
            (
            
              x
              
                n
                −
                1
              
            
            )
            +
            9
            f
            (
            
              x
              
                n
              
            
            )
          
          ]
        
        ,
      
    
    {\displaystyle \int _{a}^{b}f(x)\,dx\approx {\frac {1}{24}}h\left[9f(x_{0})+28f(x_{1})+23f(x_{2})+24\sum _{i=3}^{n-3}f(x_{i})+23f(x_{n-2})+28f(x_{n-1})+9f(x_{n})\right],}
  

where only points within integration region are used. Application of the second rule to the region of 3 points generates 1/3 Simpson's rule, 4 points - 3/8 rule.
These rules are very much similar to the alternative extended Simpson's rule. The coefficients within the major part of the region being integrated are one with non-unit coefficients only at the edges. These two rules can be associated with Euler–MacLaurin formula with the first derivative term and named First order Euler–MacLaurin integration rules. The two rules presented above differ only in the way how the first derivative at the region end is calculated. The first derivative term in the Euler–MacLaurin integration rules accounts for integral of the second derivative, which equals the difference of the first derivatives at the edges of the integration region. It is possible to generate higher order Euler–Maclaurin rules by adding a difference of 3rd, 5th, and so on derivatives with coefficients, as defined by Euler–MacLaurin formula.

Composite Simpson's rule for irregularly spaced data
For some applications, the integration interval 
  
    
      
        I
        =
        [
        a
        ,
        b
        ]
      
    
    {\displaystyle I=[a,b]}
  
 needs to be divided into uneven intervals – perhaps due to uneven sampling of data, or missing or corrupted data points. Suppose we divide the interval 
  
    
      
        I
      
    
    {\displaystyle I}
  
 into an even number 
  
    
      
        N
      
    
    {\displaystyle N}
  
 of subintervals of widths 
  
    
      
        
          h
          
            k
          
        
      
    
    {\displaystyle h_{k}}
  
. Then the composite Simpson's rule is given by

  
    
      
        
          ∫
          
            a
          
          
            b
          
        
        f
        (
        x
        )
        
        d
        x
        ≈
        
          ∑
          
            i
            =
            0
          
          
            N
            
              /
            
            2
            −
            1
          
        
        
          
            
              
                h
                
                  2
                  i
                
              
              +
              
                h
                
                  2
                  i
                  +
                  1
                
              
            
            6
          
        
        
          [
          
            
              (
              
                2
                −
                
                  
                    
                      h
                      
                        2
                        i
                        +
                        1
                      
                    
                    
                      h
                      
                        2
                        i
                      
                    
                  
                
              
              )
            
            
              f
              
                2
                i
              
            
            +
            
              
                
                  (
                  
                    h
                    
                      2
                      i
                    
                  
                  +
                  
                    h
                    
                      2
                      i
                      +
                      1
                    
                  
                  
                    )
                    
                      2
                    
                  
                
                
                  
                    h
                    
                      2
                      i
                    
                  
                  
                    h
                    
                      2
                      i
                      +
                      1
                    
                  
                
              
            
            
              f
              
                2
                i
                +
                1
              
            
            +
            
              (
              
                2
                −
                
                  
                    
                      h
                      
                        2
                        i
                      
                    
                    
                      h
                      
                        2
                        i
                        +
                        1
                      
                    
                  
                
              
              )
            
            
              f
              
                2
                i
                +
                2
              
            
          
          ]
        
        ,
      
    
    {\displaystyle \int _{a}^{b}f(x)\,dx\approx \sum _{i=0}^{N/2-1}{\frac {h_{2i}+h_{2i+1}}{6}}\left[\left(2-{\frac {h_{2i+1}}{h_{2i}}}\right)f_{2i}+{\frac {(h_{2i}+h_{2i+1})^{2}}{h_{2i}h_{2i+1}}}f_{2i+1}+\left(2-{\frac {h_{2i}}{h_{2i+1}}}\right)f_{2i+2}\right],}
  

where

  
    
      
        
          f
          
            k
          
        
        =
        f
        
          (
          
            a
            +
            
              ∑
              
                i
                =
                0
              
              
                k
                −
                1
              
            
            
              h
              
                i
              
            
          
          )
        
      
    
    {\displaystyle f_{k}=f\left(a+\sum _{i=0}^{k-1}h_{i}\right)}
  

are the function values at the 
  
    
      
        k
      
    
    {\displaystyle k}
  
th sampling point on the interval 
  
    
      
        I
      
    
    {\displaystyle I}
  
.
In case of an odd number 
  
    
      
        N
      
    
    {\displaystyle N}
  
 of subintervals, the above formula is used up to the second to last interval, 
and the last interval is handled separately by adding the following to the result:

  
    
      
        α
        
          f
          
            N
          
        
        +
        β
        
          f
          
            N
            −
            1
          
        
        −
        η
        
          f
          
            N
            −
            2
          
        
        ,
      
    
    {\displaystyle \alpha f_{N}+\beta f_{N-1}-\eta f_{N-2},}
  

where

  
    
      
        
          
            
              
                α
              
              
                
                =
                
                  
                    
                      2
                      
                        h
                        
                          N
                          −
                          1
                        
                        
                          2
                        
                      
                      +
                      3
                      
                        h
                        
                          N
                          −
                          1
                        
                      
                      
                        h
                        
                          N
                          −
                          2
                        
                      
                    
                    
                      6
                      (
                      
                        h
                        
                          N
                          −
                          2
                        
                      
                      +
                      
                        h
                        
                          N
                          −
                          1
                        
                      
                      )
                    
                  
                
                ,
              
            
            
              
                β
              
              
                
                =
                
                  
                    
                      
                        h
                        
                          N
                          −
                          1
                        
                        
                          2
                        
                      
                      +
                      3
                      
                        h
                        
                          N
                          −
                          1
                        
                      
                      
                        h
                        
                          N
                          −
                          2
                        
                      
                    
                    
                      6
                      
                        h
                        
                          N
                          −
                          2
                        
                      
                    
                  
                
                ,
              
            
            
              
                η
              
              
                
                =
                
                  
                    
                      h
                      
                        N
                        −
                        1
                      
                      
                        3
                      
                    
                    
                      6
                      
                        h
                        
                          N
                          −
                          2
                        
                      
                      (
                      
                        h
                        
                          N
                          −
                          2
                        
                      
                      +
                      
                        h
                        
                          N
                          −
                          1
                        
                      
                      )
                    
                  
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\alpha &={\frac {2h_{N-1}^{2}+3h_{N-1}h_{N-2}}{6(h_{N-2}+h_{N-1})}},\\[1ex]\beta &={\frac {h_{N-1}^{2}+3h_{N-1}h_{N-2}}{6h_{N-2}}},\\[1ex]\eta &={\frac {h_{N-1}^{3}}{6h_{N-2}(h_{N-2}+h_{N-1})}}.\end{aligned}}}

See also
Newton–Cotes formulas
Gaussian quadrature

Notes
References
Atkinson, Kendall E. (1989). An Introduction to Numerical Analysis (2nd ed.). John Wiley & Sons. ISBN 0-471-50023-2.
Burden, Richard L.; Faires, J. Douglas (2000). Numerical Analysis (7th ed.). Brooks/Cole. ISBN 0-534-38216-9.
Cartwright, Kenneth V. (September 2017). "Simpson's Rule Cumulative Integration with MS Excel and Irregularly-spaced Data" (PDF). Journal of Mathematical Sciences and Mathematics Education. 12 (2): 1–9. Retrieved 18 December 2022.
Kalambet, Yuri; Kozmin, Yuri; Samokhin, Andrey (2018). "Comparison of integration rules in the case of very narrow chromatographic peaks". Chemometrics and Intelligent Laboratory Systems. 179: 22–30. doi:10.1016/j.chemolab.2018.06.001. ISSN 0169-7439.
Matthews, John H. (2004). "Simpson's 3/8 Rule for Numerical Integration". Numerical Analysis - Numerical Methods Project. California State University, Fullerton. Archived from the original on 4 December 2008. Retrieved 11 November 2008.
Shklov, N. (December 1960). "Simpson's Rule for Unequally Spaced Ordinates". The American Mathematical Monthly. 67 (10): 1022–1023. doi:10.2307/2309244. JSTOR 2309244.
Süli, Endre; Mayers, David (2003). An Introduction to Numerical Analysis. Cambridge University Press. ISBN 0-521-00794-1.
Weisstein, Eric W. "Newton-Cotes Formulas". MathWorld. Retrieved 14 December 2022.

External links
"Simpson formula". Encyclopedia of Mathematics. EMS Press. 2001 [1994].
Weisstein, Eric W. "Simpson's Rule". MathWorld.
Simpson's 1/3rd rule of integration — Notes, PPT, Mathcad, Matlab, Mathematica, Maple at Numerical Methods for STEM undergraduate
A detailed description of a computer implementation is described by Dorai Sitaram in Teach Yourself Scheme in Fixnum Days, Appendix C

This article incorporates material from Code for Simpson's rule on PlanetMath, which is licensed under the Creative Commons Attribution/Share-Alike License.

## Related Articles

### Internal Links

- [Adaptive Simpson's method](https://en.wikipedia.org/wiki/Adaptive_Simpson%27s_method)
- [Ansatz](https://en.wikipedia.org/wiki/Ansatz)
- [Approximation](https://en.wikipedia.org/wiki/Approximation)
- [Barnes–Hut simulation](https://en.wikipedia.org/wiki/Barnes%E2%80%93Hut_simulation)
- [Bayesian quadrature](https://en.wikipedia.org/wiki/Bayesian_quadrature)
- [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Boole's rule](https://en.wikipedia.org/wiki/Boole%27s_rule)
- [Chebyshev–Gauss quadrature](https://en.wikipedia.org/wiki/Chebyshev%E2%80%93Gauss_quadrature)
- [Clenshaw–Curtis quadrature](https://en.wikipedia.org/wiki/Clenshaw%E2%80%93Curtis_quadrature)
- [Convex function](https://en.wikipedia.org/wiki/Convex_function)
- [Integral](https://en.wikipedia.org/wiki/Integral)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Encyclopedia of Mathematics](https://en.wikipedia.org/wiki/Encyclopedia_of_Mathematics)
- [Eric W. Weisstein](https://en.wikipedia.org/wiki/Eric_W._Weisstein)
- [Euler–Maclaurin formula](https://en.wikipedia.org/wiki/Euler%E2%80%93Maclaurin_formula)
- [European Mathematical Society](https://en.wikipedia.org/wiki/European_Mathematical_Society)
- [Filon quadrature](https://en.wikipedia.org/wiki/Filon_quadrature)
- [Gaussian quadrature](https://en.wikipedia.org/wiki/Gaussian_quadrature)
- [Gauss–Hermite quadrature](https://en.wikipedia.org/wiki/Gauss%E2%80%93Hermite_quadrature)
- [Gauss–Jacobi quadrature](https://en.wikipedia.org/wiki/Gauss%E2%80%93Jacobi_quadrature)
- [Gauss–Kronrod quadrature formula](https://en.wikipedia.org/wiki/Gauss%E2%80%93Kronrod_quadrature_formula)
- [Gauss–Laguerre quadrature](https://en.wikipedia.org/wiki/Gauss%E2%80%93Laguerre_quadrature)
- [Gauss–Legendre quadrature](https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_quadrature)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Integration by substitution](https://en.wikipedia.org/wiki/Integration_by_substitution)
- [JSTOR](https://en.wikipedia.org/wiki/JSTOR)
- [Johannes Kepler](https://en.wikipedia.org/wiki/Johannes_Kepler)
- [Lagrange polynomial](https://en.wikipedia.org/wiki/Lagrange_polynomial)
- [Lebedev quadrature](https://en.wikipedia.org/wiki/Lebedev_quadrature)
- [MathWorld](https://en.wikipedia.org/wiki/MathWorld)
- [Minimax Condorcet method](https://en.wikipedia.org/wiki/Minimax_Condorcet_method)
- [Newton–Cotes formulas](https://en.wikipedia.org/wiki/Newton%E2%80%93Cotes_formulas)
- [Numerical integration](https://en.wikipedia.org/wiki/Numerical_integration)
- [PlanetMath](https://en.wikipedia.org/wiki/PlanetMath)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quadratic function](https://en.wikipedia.org/wiki/Quadratic_function)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Riemann sum](https://en.wikipedia.org/wiki/Riemann_sum)
- [Romberg's method](https://en.wikipedia.org/wiki/Romberg%27s_method)
- [Scheme (programming language)](https://en.wikipedia.org/wiki/Scheme_(programming_language))
- [Simpson's rules (ship stability)](https://en.wikipedia.org/wiki/Simpson%27s_rules_(ship_stability))
- [Tanh-sinh quadrature](https://en.wikipedia.org/wiki/Tanh-sinh_quadrature)
- [Thomas Simpson](https://en.wikipedia.org/wiki/Thomas_Simpson)
- [Trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule)
- [Weighted arithmetic mean](https://en.wikipedia.org/wiki/Weighted_arithmetic_mean)
- [Xi (letter)](https://en.wikipedia.org/wiki/Xi_(letter))
- [Wikipedia:Text of the Creative Commons Attribution-ShareAlike 4.0 International License](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_Creative_Commons_Attribution-ShareAlike_4.0_International_License)
- [Template:Numerical integration](https://en.wikipedia.org/wiki/Template:Numerical_integration)
- [Template talk:Numerical integration](https://en.wikipedia.org/wiki/Template_talk:Numerical_integration)
- [Category:Use dmy dates from January 2020](https://en.wikipedia.org/wiki/Category:Use_dmy_dates_from_January_2020)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:45:06.218761+00:00_