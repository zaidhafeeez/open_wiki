# Inverse Gaussian distribution

## Article Metadata

- **Last Updated:** 2024-12-14T19:38:58.303613+00:00
- **Original Article:** [Inverse Gaussian distribution](https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution)
- **Language:** en
- **Page ID:** 5246161

## Summary

In probability theory, the inverse Gaussian distribution (also known as the Wald distribution) is a two-parameter family of continuous probability distributions with support on (0,∞).
Its probability density function is given by

  
    
      
        f
        (
        x
        ;
        μ
        ,
        λ
        )
        =
        
          
            
              λ
              
                2
                π
                
                  x
                  
         

## Categories

- Category:Articles contradicting other articles
- Category:Articles with example Java code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:CS1: long volume value
- Category:CS1 French-language sources (fr)
- Category:CS1 German-language sources (de)
- Category:Continuous distributions
- Category:Exponential family distributions
- Category:Infinitely divisible probability distributions
- Category:Short description matches Wikidata

## Table of Contents

- Properties
- Relationship with Brownian motion
- Maximum likelihood
- Sampling from an inverse-Gaussian distribution
- Related distributions
- History
- Numeric computation and software
- See also
- References
- Further reading
- External links

## Content

In probability theory, the inverse Gaussian distribution (also known as the Wald distribution) is a two-parameter family of continuous probability distributions with support on (0,∞).
Its probability density function is given by

  
    
      
        f
        (
        x
        ;
        μ
        ,
        λ
        )
        =
        
          
            
              λ
              
                2
                π
                
                  x
                  
                    3
                  
                
              
            
          
        
        exp
        ⁡
        
          
            (
          
        
        −
        
          
            
              λ
              (
              x
              −
              μ
              
                )
                
                  2
                
              
            
            
              2
              
                μ
                
                  2
                
              
              x
            
          
        
        
          
            )
          
        
      
    
    {\displaystyle f(x;\mu ,\lambda )={\sqrt {\frac {\lambda }{2\pi x^{3}}}}\exp {\biggl (}-{\frac {\lambda (x-\mu )^{2}}{2\mu ^{2}x}}{\biggr )}}
  

for x > 0, where 
  
    
      
        μ
        >
        0
      
    
    {\displaystyle \mu >0}
  
 is the mean and 
  
    
      
        λ
        >
        0
      
    
    {\displaystyle \lambda >0}
  
 is the shape parameter.
The inverse Gaussian distribution has several properties analogous to a Gaussian distribution.  The name can be misleading:  it is an "inverse" only in that, while the Gaussian describes a Brownian motion's level at a fixed time, the inverse Gaussian describes the distribution of the time a Brownian motion with positive drift takes to reach a fixed positive level.
Its cumulant generating function (logarithm of the characteristic function) is the inverse of the cumulant generating function of a Gaussian random variable.
To indicate that a random variable X is inverse Gaussian-distributed with mean μ and shape parameter λ we write 
  
    
      
        X
        ∼
        IG
        ⁡
        (
        μ
        ,
        λ
        )
        
        
      
    
    {\displaystyle X\sim \operatorname {IG} (\mu ,\lambda )\,\!}
  
.

Properties
Single parameter form
The probability density function (pdf) of the inverse Gaussian distribution has a single parameter form given by

  
    
      
        f
        (
        x
        ;
        μ
        ,
        
          μ
          
            2
          
        
        )
        =
        
          
            μ
            
              2
              π
              
                x
                
                  3
                
              
            
          
        
        exp
        ⁡
        
          
            (
          
        
        −
        
          
            
              (
              x
              −
              μ
              
                )
                
                  2
                
              
            
            
              2
              x
            
          
        
        
          
            )
          
        
        .
      
    
    {\displaystyle f(x;\mu ,\mu ^{2})={\frac {\mu }{\sqrt {2\pi x^{3}}}}\exp {\biggl (}-{\frac {(x-\mu )^{2}}{2x}}{\biggr )}.}
  

In this form, the mean and variance of the distribution are equal, 
  
    
      
        
          E
        
        [
        X
        ]
        =
        
          Var
        
        (
        X
        )
        .
      
    
    {\displaystyle \mathbb {E} [X]={\text{Var}}(X).}
  

Also, the cumulative distribution function (cdf) of the single parameter inverse Gaussian distribution is related to the standard normal distribution by

  
    
      
        
          
            
              
                Pr
                (
                X
                <
                x
                )
              
              
                
                =
                Φ
                (
                −
                
                  z
                  
                    1
                  
                
                )
                +
                
                  e
                  
                    2
                    μ
                  
                
                Φ
                (
                −
                
                  z
                  
                    2
                  
                
                )
                ,
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\Pr(X<x)&=\Phi (-z_{1})+e^{2\mu }\Phi (-z_{2}),\end{aligned}}}
  

where 
  
    
      
        
          z
          
            1
          
        
        =
        
          
            μ
            
              x
              
                1
                
                  /
                
                2
              
            
          
        
        −
        
          x
          
            1
            
              /
            
            2
          
        
      
    
    {\displaystyle z_{1}={\frac {\mu }{x^{1/2}}}-x^{1/2}}
  
, 
  
    
      
        
          z
          
            2
          
        
        =
        
          
            μ
            
              x
              
                1
                
                  /
                
                2
              
            
          
        
        +
        
          x
          
            1
            
              /
            
            2
          
        
        ,
      
    
    {\displaystyle z_{2}={\frac {\mu }{x^{1/2}}}+x^{1/2},}
  
 and the 
  
    
      
        Φ
      
    
    {\displaystyle \Phi }
  
 is the cdf of standard normal distribution. The variables 
  
    
      
        
          z
          
            1
          
        
      
    
    {\displaystyle z_{1}}
  
 and 
  
    
      
        
          z
          
            2
          
        
      
    
    {\displaystyle z_{2}}
  
 are related to each other by the identity 
  
    
      
        
          z
          
            2
          
          
            2
          
        
        =
        
          z
          
            1
          
          
            2
          
        
        +
        4
        μ
        .
      
    
    {\displaystyle z_{2}^{2}=z_{1}^{2}+4\mu .}
  

In the single parameter form, the MGF simplifies to

  
    
      
        M
        (
        t
        )
        =
        exp
        ⁡
        [
        μ
        (
        1
        −
        
          
            1
            −
            2
            t
          
        
        )
        ]
        .
      
    
    {\displaystyle M(t)=\exp[\mu (1-{\sqrt {1-2t}})].}
  

An inverse Gaussian distribution in double parameter form 
  
    
      
        f
        (
        x
        ;
        μ
        ,
        λ
        )
      
    
    {\displaystyle f(x;\mu ,\lambda )}
  
 can be transformed into a single parameter form 
  
    
      
        f
        (
        y
        ;
        
          μ
          
            0
          
        
        ,
        
          μ
          
            0
          
          
            2
          
        
        )
      
    
    {\displaystyle f(y;\mu _{0},\mu _{0}^{2})}
  
 by appropriate scaling 
  
    
      
        y
        =
        
          
            
              
                μ
                
                  2
                
              
              x
            
            λ
          
        
        ,
      
    
    {\displaystyle y={\frac {\mu ^{2}x}{\lambda }},}
  
 where 
  
    
      
        
          μ
          
            0
          
        
        =
        
          μ
          
            3
          
        
        
          /
        
        λ
        .
      
    
    {\displaystyle \mu _{0}=\mu ^{3}/\lambda .}
  

The standard form of inverse Gaussian distribution is

  
    
      
        f
        (
        x
        ;
        1
        ,
        1
        )
        =
        
          
            1
            
              2
              π
              
                x
                
                  3
                
              
            
          
        
        exp
        ⁡
        
          
            (
          
        
        −
        
          
            
              (
              x
              −
              1
              
                )
                
                  2
                
              
            
            
              2
              x
            
          
        
        
          
            )
          
        
        .
      
    
    {\displaystyle f(x;1,1)={\frac {1}{\sqrt {2\pi x^{3}}}}\exp {\biggl (}-{\frac {(x-1)^{2}}{2x}}{\biggr )}.}

Summation
If Xi has an 
  
    
      
        IG
        ⁡
        (
        
          μ
          
            0
          
        
        
          w
          
            i
          
        
        ,
        
          λ
          
            0
          
        
        
          w
          
            i
          
          
            2
          
        
        )
        
        
      
    
    {\displaystyle \operatorname {IG} (\mu _{0}w_{i},\lambda _{0}w_{i}^{2})\,\!}
  
 distribution for i = 1, 2, ..., n
and all Xi are independent, then

  
    
      
        S
        =
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        
          X
          
            i
          
        
        ∼
        IG
        ⁡
        
          (
          
            
              μ
              
                0
              
            
            ∑
            
              w
              
                i
              
            
            ,
            
              λ
              
                0
              
            
            
              
                (
                
                  ∑
                  
                    w
                    
                      i
                    
                  
                
                )
              
              
                2
              
            
          
          )
        
        .
      
    
    {\displaystyle S=\sum _{i=1}^{n}X_{i}\sim \operatorname {IG} \left(\mu _{0}\sum w_{i},\lambda _{0}\left(\sum w_{i}\right)^{2}\right).}
  

Note that

  
    
      
        
          
            
              Var
              ⁡
              (
              
                X
                
                  i
                
              
              )
            
            
              E
              ⁡
              (
              
                X
                
                  i
                
              
              )
            
          
        
        =
        
          
            
              
                μ
                
                  0
                
                
                  2
                
              
              
                w
                
                  i
                
                
                  2
                
              
            
            
              
                λ
                
                  0
                
              
              
                w
                
                  i
                
                
                  2
                
              
            
          
        
        =
        
          
            
              μ
              
                0
              
              
                2
              
            
            
              λ
              
                0
              
            
          
        
      
    
    {\displaystyle {\frac {\operatorname {Var} (X_{i})}{\operatorname {E} (X_{i})}}={\frac {\mu _{0}^{2}w_{i}^{2}}{\lambda _{0}w_{i}^{2}}}={\frac {\mu _{0}^{2}}{\lambda _{0}}}}
  

is constant for all i. This is a necessary condition for the summation. Otherwise S would not be Inverse Gaussian distributed.

Scaling
For any t > 0 it holds that

  
    
      
        X
        ∼
        IG
        ⁡
        (
        μ
        ,
        λ
        )
        
        
        
        
        
        
        ⇒
        
        
        
        
        
        
        t
        X
        ∼
        IG
        ⁡
        (
        t
        μ
        ,
        t
        λ
        )
        .
      
    
    {\displaystyle X\sim \operatorname {IG} (\mu ,\lambda )\,\,\,\,\,\,\Rightarrow \,\,\,\,\,\,tX\sim \operatorname {IG} (t\mu ,t\lambda ).}

Exponential family
The inverse Gaussian distribution is a two-parameter exponential family with natural parameters −λ/(2μ2) and −λ/2, and natural statistics X and 1/X.
For 
  
    
      
        λ
        >
        0
      
    
    {\displaystyle \lambda >0}
  
 fixed, it is also a single-parameter natural exponential family distribution where the base distribution has density

  
    
      
        h
        (
        x
        )
        =
        
          
            
              λ
              
                2
                π
                
                  x
                  
                    3
                  
                
              
            
          
        
        exp
        ⁡
        
          (
          
            −
            
              
                λ
                
                  2
                  x
                
              
            
          
          )
        
        
          
            1
          
          
            [
            0
            ,
            ∞
            )
          
        
        (
        x
        )
        
        .
      
    
    {\displaystyle h(x)={\sqrt {\frac {\lambda }{2\pi x^{3}}}}\exp \left(-{\frac {\lambda }{2x}}\right)\mathbb {1} _{[0,\infty )}(x)\,.}
  

Indeed, with 
  
    
      
        θ
        ≤
        0
      
    
    {\displaystyle \theta \leq 0}
  
,

  
    
      
        p
        (
        x
        ;
        θ
        )
        =
        
          
            
              exp
              ⁡
              (
              θ
              x
              )
              h
              (
              x
              )
            
            
              ∫
              exp
              ⁡
              (
              θ
              y
              )
              h
              (
              y
              )
              d
              y
            
          
        
      
    
    {\displaystyle p(x;\theta )={\frac {\exp(\theta x)h(x)}{\int \exp(\theta y)h(y)dy}}}
  

is a density over the reals. Evaluating the integral, we get

  
    
      
        p
        (
        x
        ;
        θ
        )
        =
        
          
            
              λ
              
                2
                π
                
                  x
                  
                    3
                  
                
              
            
          
        
        exp
        ⁡
        
          (
          
            −
            
              
                λ
                
                  2
                  x
                
              
            
            +
            θ
            x
            −
            
              
                −
                2
                λ
                θ
              
            
          
          )
        
        
          
            1
          
          
            [
            0
            ,
            ∞
            )
          
        
        (
        x
        )
        
        .
      
    
    {\displaystyle p(x;\theta )={\sqrt {\frac {\lambda }{2\pi x^{3}}}}\exp \left(-{\frac {\lambda }{2x}}+\theta x-{\sqrt {-2\lambda \theta }}\right)\mathbb {1} _{[0,\infty )}(x)\,.}
  

Substituting 
  
    
      
        θ
        =
        −
        λ
        
          /
        
        (
        2
        
          μ
          
            2
          
        
        )
      
    
    {\displaystyle \theta =-\lambda /(2\mu ^{2})}
  
 makes the above expression equal to 
  
    
      
        f
        (
        x
        ;
        μ
        ,
        λ
        )
      
    
    {\displaystyle f(x;\mu ,\lambda )}
  
.

Relationship with Brownian motion
Let the stochastic process Xt be given by

  
    
      
        
          X
          
            0
          
        
        =
        0
        
      
    
    {\displaystyle X_{0}=0\quad }
  

  
    
      
        
          X
          
            t
          
        
        =
        ν
        t
        +
        σ
        
          W
          
            t
          
        
        
        
        
        
      
    
    {\displaystyle X_{t}=\nu t+\sigma W_{t}\quad \quad \quad \quad }
  

where Wt is a standard Brownian motion. That is, Xt is a Brownian motion with drift 
  
    
      
        ν
        >
        0
      
    
    {\displaystyle \nu >0}
  
.
Then the first passage time for a fixed level 
  
    
      
        α
        >
        0
      
    
    {\displaystyle \alpha >0}
  
 by Xt is distributed according to an inverse-Gaussian:

  
    
      
        
          T
          
            α
          
        
        =
        inf
        {
        t
        >
        0
        ∣
        
          X
          
            t
          
        
        =
        α
        }
        ∼
        IG
        ⁡
        
          (
          
            
              
                α
                ν
              
            
            ,
            
              
                (
                
                  
                    α
                    σ
                  
                
                )
              
              
                2
              
            
          
          )
        
        =
        
          
            α
            
              σ
              
                
                  2
                  π
                  
                    x
                    
                      3
                    
                  
                
              
            
          
        
        exp
        ⁡
        
          
            (
          
        
        −
        
          
            
              (
              α
              −
              ν
              x
              
                )
                
                  2
                
              
            
            
              2
              
                σ
                
                  2
                
              
              x
            
          
        
        
          
            )
          
        
      
    
    {\displaystyle T_{\alpha }=\inf\{t>0\mid X_{t}=\alpha \}\sim \operatorname {IG} \left({\frac {\alpha }{\nu }},\left({\frac {\alpha }{\sigma }}\right)^{2}\right)={\frac {\alpha }{\sigma {\sqrt {2\pi x^{3}}}}}\exp {\biggl (}-{\frac {(\alpha -\nu x)^{2}}{2\sigma ^{2}x}}{\biggr )}}
  

i.e

  
    
      
        P
        (
        
          T
          
            α
          
        
        ∈
        (
        T
        ,
        T
        +
        d
        T
        )
        )
        =
        
          
            α
            
              σ
              
                
                  2
                  π
                  
                    T
                    
                      3
                    
                  
                
              
            
          
        
        exp
        ⁡
        
          
            (
          
        
        −
        
          
            
              (
              α
              −
              ν
              T
              
                )
                
                  2
                
              
            
            
              2
              
                σ
                
                  2
                
              
              T
            
          
        
        
          
            )
          
        
        d
        T
      
    
    {\displaystyle P(T_{\alpha }\in (T,T+dT))={\frac {\alpha }{\sigma {\sqrt {2\pi T^{3}}}}}\exp {\biggl (}-{\frac {(\alpha -\nu T)^{2}}{2\sigma ^{2}T}}{\biggr )}dT}
  

(cf. Schrödinger equation 19, Smoluchowski, equation 8, and Folks, equation 1).

When drift is zero
A common special case of the above arises when the Brownian motion has no drift.  In that case, parameter μ tends to infinity, and the first passage time for fixed level α has probability density function

  
    
      
        f
        
          (
          
            x
            ;
            0
            ,
            
              
                (
                
                  
                    α
                    σ
                  
                
                )
              
              
                2
              
            
          
          )
        
        =
        
          
            α
            
              σ
              
                
                  2
                  π
                  
                    x
                    
                      3
                    
                  
                
              
            
          
        
        exp
        ⁡
        
          (
          
            −
            
              
                
                  α
                  
                    2
                  
                
                
                  2
                  
                    σ
                    
                      2
                    
                  
                  x
                
              
            
          
          )
        
      
    
    {\displaystyle f\left(x;0,\left({\frac {\alpha }{\sigma }}\right)^{2}\right)={\frac {\alpha }{\sigma {\sqrt {2\pi x^{3}}}}}\exp \left(-{\frac {\alpha ^{2}}{2\sigma ^{2}x}}\right)}
  

(see also Bachelier: 74 : 39 ). This is a Lévy distribution with parameters 
  
    
      
        c
        =
        
          
            (
            
              
                α
                σ
              
            
            )
          
          
            2
          
        
      
    
    {\displaystyle c=\left({\frac {\alpha }{\sigma }}\right)^{2}}
  
 and 
  
    
      
        μ
        =
        0
      
    
    {\displaystyle \mu =0}
  
.

Maximum likelihood
The model where

  
    
      
        
          X
          
            i
          
        
        ∼
        IG
        ⁡
        (
        μ
        ,
        λ
        
          w
          
            i
          
        
        )
        ,
        
        
        
        
        
        
        i
        =
        1
        ,
        2
        ,
        …
        ,
        n
      
    
    {\displaystyle X_{i}\sim \operatorname {IG} (\mu ,\lambda w_{i}),\,\,\,\,\,\,i=1,2,\ldots ,n}
  

with all wi known, (μ, λ) unknown and all Xi independent has the following likelihood function

  
    
      
        L
        (
        μ
        ,
        λ
        )
        =
        
          
            (
            
              
                λ
                
                  2
                  π
                
              
            
            )
          
          
            
              n
              2
            
          
        
        
          
            (
            
              
                ∏
                
                  i
                  =
                  1
                
                
                  n
                
              
              
                
                  
                    w
                    
                      i
                    
                  
                  
                    X
                    
                      i
                    
                    
                      3
                    
                  
                
              
            
            )
          
          
            
              1
              2
            
          
        
        exp
        ⁡
        
          (
          
            
              
                λ
                μ
              
            
            
              ∑
              
                i
                =
                1
              
              
                n
              
            
            
              w
              
                i
              
            
            −
            
              
                λ
                
                  2
                  
                    μ
                    
                      2
                    
                  
                
              
            
            
              ∑
              
                i
                =
                1
              
              
                n
              
            
            
              w
              
                i
              
            
            
              X
              
                i
              
            
            −
            
              
                λ
                2
              
            
            
              ∑
              
                i
                =
                1
              
              
                n
              
            
            
              w
              
                i
              
            
            
              
                1
                
                  X
                  
                    i
                  
                
              
            
          
          )
        
        .
      
    
    {\displaystyle L(\mu ,\lambda )=\left({\frac {\lambda }{2\pi }}\right)^{\frac {n}{2}}\left(\prod _{i=1}^{n}{\frac {w_{i}}{X_{i}^{3}}}\right)^{\frac {1}{2}}\exp \left({\frac {\lambda }{\mu }}\sum _{i=1}^{n}w_{i}-{\frac {\lambda }{2\mu ^{2}}}\sum _{i=1}^{n}w_{i}X_{i}-{\frac {\lambda }{2}}\sum _{i=1}^{n}w_{i}{\frac {1}{X_{i}}}\right).}
  

Solving the likelihood equation yields the following maximum likelihood estimates

  
    
      
        
          
            
              μ
              ^
            
          
        
        =
        
          
            
              
                ∑
                
                  i
                  =
                  1
                
                
                  n
                
              
              
                w
                
                  i
                
              
              
                X
                
                  i
                
              
            
            
              
                ∑
                
                  i
                  =
                  1
                
                
                  n
                
              
              
                w
                
                  i
                
              
            
          
        
        ,
        
        
        
        
        
        
        
        
        
          
            1
            
              
                λ
                ^
              
            
          
        
        =
        
          
            1
            n
          
        
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        
          w
          
            i
          
        
        
          (
          
            
              
                1
                
                  X
                  
                    i
                  
                
              
            
            −
            
              
                1
                
                  
                    μ
                    ^
                  
                
              
            
          
          )
        
        .
      
    
    {\displaystyle {\widehat {\mu }}={\frac {\sum _{i=1}^{n}w_{i}X_{i}}{\sum _{i=1}^{n}w_{i}}},\,\,\,\,\,\,\,\,{\frac {1}{\widehat {\lambda }}}={\frac {1}{n}}\sum _{i=1}^{n}w_{i}\left({\frac {1}{X_{i}}}-{\frac {1}{\widehat {\mu }}}\right).}
  

  
    
      
        
          
            
              μ
              ^
            
          
        
      
    
    {\displaystyle {\widehat {\mu }}}
  
 and 
  
    
      
        
          
            
              λ
              ^
            
          
        
      
    
    {\displaystyle {\widehat {\lambda }}}
  
 are independent and

  
    
      
        
          
            
              μ
              ^
            
          
        
        ∼
        IG
        ⁡
        
          (
          
            μ
            ,
            λ
            
              ∑
              
                i
                =
                1
              
              
                n
              
            
            
              w
              
                i
              
            
          
          )
        
        ,
        
        
          
            n
            
              
                λ
                ^
              
            
          
        
        ∼
        
          
            1
            λ
          
        
        
          χ
          
            n
            −
            1
          
          
            2
          
        
        .
      
    
    {\displaystyle {\widehat {\mu }}\sim \operatorname {IG} \left(\mu ,\lambda \sum _{i=1}^{n}w_{i}\right),\qquad {\frac {n}{\widehat {\lambda }}}\sim {\frac {1}{\lambda }}\chi _{n-1}^{2}.}

Sampling from an inverse-Gaussian distribution
The following algorithm may be used.

Generate a random variate from a normal distribution with mean 0 and standard deviation equal 1

  
    
      
        
          ν
          ∼
          N
          (
          0
          ,
          1
          )
          .
        
      
    
    {\displaystyle \displaystyle \nu \sim N(0,1).}
  

Square the value

  
    
      
        
          y
          =
          
            ν
            
              2
            
          
        
      
    
    {\displaystyle \displaystyle y=\nu ^{2}}
  

and use the relation

  
    
      
        x
        =
        μ
        +
        
          
            
              
                μ
                
                  2
                
              
              y
            
            
              2
              λ
            
          
        
        −
        
          
            μ
            
              2
              λ
            
          
        
        
          
            4
            μ
            λ
            y
            +
            
              μ
              
                2
              
            
            
              y
              
                2
              
            
          
        
        .
      
    
    {\displaystyle x=\mu +{\frac {\mu ^{2}y}{2\lambda }}-{\frac {\mu }{2\lambda }}{\sqrt {4\mu \lambda y+\mu ^{2}y^{2}}}.}
  

Generate another random variate, this time sampled from a uniform distribution between 0 and 1

  
    
      
        
          z
          ∼
          U
          (
          0
          ,
          1
          )
          .
        
      
    
    {\displaystyle \displaystyle z\sim U(0,1).}
  

If

  
    
      
        z
        ≤
        
          
            μ
            
              μ
              +
              x
            
          
        
      
    
    {\displaystyle z\leq {\frac {\mu }{\mu +x}}}
  

then return

  
    
      
        
          x
        
      
    
    {\displaystyle \displaystyle x}
  

else return

  
    
      
        
          
            
              μ
              
                2
              
            
            x
          
        
        .
      
    
    {\displaystyle {\frac {\mu ^{2}}{x}}.}
  

Sample code in Java:

And to plot Wald distribution in Python using matplotlib and NumPy:

Related distributions
If 
  
    
      
        X
        ∼
        IG
        ⁡
        (
        μ
        ,
        λ
        )
      
    
    {\displaystyle X\sim \operatorname {IG} (\mu ,\lambda )}
  
, then 
  
    
      
        k
        X
        ∼
        IG
        ⁡
        (
        k
        μ
        ,
        k
        λ
        )
      
    
    {\displaystyle kX\sim \operatorname {IG} (k\mu ,k\lambda )}
  
 for any number 
  
    
      
        k
        >
        0.
      
    
    {\displaystyle k>0.}
  

If 
  
    
      
        
          X
          
            i
          
        
        ∼
        IG
        ⁡
        (
        μ
        ,
        λ
        )
        
      
    
    {\displaystyle X_{i}\sim \operatorname {IG} (\mu ,\lambda )\,}
  
 then 
  
    
      
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        
          X
          
            i
          
        
        ∼
        IG
        ⁡
        (
        n
        μ
        ,
        
          n
          
            2
          
        
        λ
        )
        
      
    
    {\displaystyle \sum _{i=1}^{n}X_{i}\sim \operatorname {IG} (n\mu ,n^{2}\lambda )\,}
  

If 
  
    
      
        
          X
          
            i
          
        
        ∼
        IG
        ⁡
        (
        μ
        ,
        λ
        )
        
      
    
    {\displaystyle X_{i}\sim \operatorname {IG} (\mu ,\lambda )\,}
  
 for 
  
    
      
        i
        =
        1
        ,
        …
        ,
        n
        
      
    
    {\displaystyle i=1,\ldots ,n\,}
  
 then 
  
    
      
        
          
            
              X
              ¯
            
          
        
        ∼
        IG
        ⁡
        (
        μ
        ,
        n
        λ
        )
        
      
    
    {\displaystyle {\bar {X}}\sim \operatorname {IG} (\mu ,n\lambda )\,}
  

If 
  
    
      
        
          X
          
            i
          
        
        ∼
        IG
        ⁡
        (
        
          μ
          
            i
          
        
        ,
        2
        
          μ
          
            i
          
          
            2
          
        
        )
        
      
    
    {\displaystyle X_{i}\sim \operatorname {IG} (\mu _{i},2\mu _{i}^{2})\,}
  
 then 
  
    
      
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        
          X
          
            i
          
        
        ∼
        IG
        ⁡
        
          (
          
            
              ∑
              
                i
                =
                1
              
              
                n
              
            
            
              μ
              
                i
              
            
            ,
            2
            
              
                (
                
                  
                    ∑
                    
                      i
                      =
                      1
                    
                    
                      n
                    
                  
                  
                    μ
                    
                      i
                    
                  
                
                )
              
              
                2
              
            
          
          )
        
        
      
    
    {\displaystyle \sum _{i=1}^{n}X_{i}\sim \operatorname {IG} \left(\sum _{i=1}^{n}\mu _{i},2\left(\sum _{i=1}^{n}\mu _{i}\right)^{2}\right)\,}
  

If 
  
    
      
        X
        ∼
        IG
        ⁡
        (
        μ
        ,
        λ
        )
      
    
    {\displaystyle X\sim \operatorname {IG} (\mu ,\lambda )}
  
, then 
  
    
      
        λ
        (
        X
        −
        μ
        
          )
          
            2
          
        
        
          /
        
        
          μ
          
            2
          
        
        X
        ∼
        
          χ
          
            2
          
        
        (
        1
        )
      
    
    {\displaystyle \lambda (X-\mu )^{2}/\mu ^{2}X\sim \chi ^{2}(1)}
  
.
The convolution of an inverse Gaussian distribution (a Wald distribution) and an exponential (an ex-Wald distribution) is used as a model for response times in psychology, with visual search as one example.

History
This distribution appears to have been first derived in 1900 by Louis Bachelier as the time a stock reaches a certain price for the first time. In 1915 it was used independently by Erwin Schrödinger and Marian v. Smoluchowski as the time to first passage of a Brownian motion. In the field of reproduction modeling it is known as the Hadwiger function, after Hugo Hadwiger who described it in 1940. Abraham Wald re-derived this distribution in 1944 as the limiting form of a sample in a sequential probability ratio test. The name inverse Gaussian was proposed by Maurice Tweedie in 1945. Tweedie investigated this distribution in 1956 and 1957 and established some of its statistical properties. The distribution was extensively reviewed by Folks and Chhikara in 1978.

Rated Inverse Gaussian Distribution
Assuming that the time intervals between occurrences of a random phenomenon follow an inverse Gaussian distribution, the probability distribution for the number of occurrences of this event within a specified time window is referred to as rated inverse Gaussian. While, first and second moment of this distribution are calculated, the derivation of the moment generating function remains an open problem.

Numeric computation and software
Despite the simple formula for the probability density function, numerical probability calculations for the inverse Gaussian distribution nevertheless require special care to achieve full machine accuracy in floating point arithmetic for all parameter values.  Functions for the inverse Gaussian distribution are provided for the R programming language by several packages including rmutil, SuppDists, STAR, invGauss, LaplacesDemon, and statmod.

See also
Generalized inverse Gaussian distribution
Tweedie distributions—The inverse Gaussian distribution is a member of the family of Tweedie exponential dispersion models
Stopping time

References
Further reading
Høyland, Arnljot; Rausand, Marvin (1994). System Reliability Theory. New York: Wiley. ISBN 978-0-471-59397-3.
Seshadri, V. (1993). The Inverse Gaussian Distribution. Oxford University Press. ISBN 978-0-19-852243-0.

External links
Inverse Gaussian Distribution in Wolfram website.

## Related Articles

### Internal Links

- [(a,b,0) class of distributions](https://en.wikipedia.org/wiki/(a,b,0)_class_of_distributions)
- [ARGUS distribution](https://en.wikipedia.org/wiki/ARGUS_distribution)
- [Abraham Wald](https://en.wikipedia.org/wiki/Abraham_Wald)
- [Annales Scientifiques de l'École Normale Supérieure](https://en.wikipedia.org/wiki/Annales_Scientifiques_de_l%27%C3%89cole_Normale_Sup%C3%A9rieure)
- [Annals of Mathematical Statistics](https://en.wikipedia.org/wiki/Annals_of_Mathematical_Statistics)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Arcsine distribution](https://en.wikipedia.org/wiki/Arcsine_distribution)
- [Arnljot Høyland](https://en.wikipedia.org/wiki/Arnljot_H%C3%B8yland)
- [Asymmetric Laplace distribution](https://en.wikipedia.org/wiki/Asymmetric_Laplace_distribution)
- [Balding–Nichols model](https://en.wikipedia.org/wiki/Balding%E2%80%93Nichols_model)
- [Bates distribution](https://en.wikipedia.org/wiki/Bates_distribution)
- [Benford's law](https://en.wikipedia.org/wiki/Benford%27s_law)
- [Benini distribution](https://en.wikipedia.org/wiki/Benini_distribution)
- [Benktander type II distribution](https://en.wikipedia.org/wiki/Benktander_type_II_distribution)
- [Benktander type I distribution](https://en.wikipedia.org/wiki/Benktander_type_I_distribution)
- [Bernoulli distribution](https://en.wikipedia.org/wiki/Bernoulli_distribution)
- [Beta-binomial distribution](https://en.wikipedia.org/wiki/Beta-binomial_distribution)
- [Beta distribution](https://en.wikipedia.org/wiki/Beta_distribution)
- [Beta negative binomial distribution](https://en.wikipedia.org/wiki/Beta_negative_binomial_distribution)
- [Beta prime distribution](https://en.wikipedia.org/wiki/Beta_prime_distribution)
- [Beta rectangular distribution](https://en.wikipedia.org/wiki/Beta_rectangular_distribution)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Bingham distribution](https://en.wikipedia.org/wiki/Bingham_distribution)
- [Binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution)
- [Bivariate von Mises distribution](https://en.wikipedia.org/wiki/Bivariate_von_Mises_distribution)
- [Borel distribution](https://en.wikipedia.org/wiki/Borel_distribution)
- [Boundary value problem](https://en.wikipedia.org/wiki/Boundary_value_problem)
- [Burr distribution](https://en.wikipedia.org/wiki/Burr_distribution)
- [Cantor distribution](https://en.wikipedia.org/wiki/Cantor_distribution)
- [Categorical distribution](https://en.wikipedia.org/wiki/Categorical_distribution)
- [Cauchy distribution](https://en.wikipedia.org/wiki/Cauchy_distribution)
- [Characteristic function (probability theory)](https://en.wikipedia.org/wiki/Characteristic_function_(probability_theory))
- [Chi-squared distribution](https://en.wikipedia.org/wiki/Chi-squared_distribution)
- [Chi distribution](https://en.wikipedia.org/wiki/Chi_distribution)
- [Circular distribution](https://en.wikipedia.org/wiki/Circular_distribution)
- [Circular uniform distribution](https://en.wikipedia.org/wiki/Circular_uniform_distribution)
- [Complex Wishart distribution](https://en.wikipedia.org/wiki/Complex_Wishart_distribution)
- [Compound Poisson distribution](https://en.wikipedia.org/wiki/Compound_Poisson_distribution)
- [Continuous Bernoulli distribution](https://en.wikipedia.org/wiki/Continuous_Bernoulli_distribution)
- [Probability distribution](https://en.wikipedia.org/wiki/Probability_distribution)
- [Continuous uniform distribution](https://en.wikipedia.org/wiki/Continuous_uniform_distribution)
- [Conway–Maxwell–Poisson distribution](https://en.wikipedia.org/wiki/Conway%E2%80%93Maxwell%E2%80%93Poisson_distribution)
- [Cumulant](https://en.wikipedia.org/wiki/Cumulant)
- [Cumulant](https://en.wikipedia.org/wiki/Cumulant)
- [Cumulative distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function)
- [Dagum distribution](https://en.wikipedia.org/wiki/Dagum_distribution)
- [Davis distribution](https://en.wikipedia.org/wiki/Davis_distribution)
- [Degenerate distribution](https://en.wikipedia.org/wiki/Degenerate_distribution)
- [Delaporte distribution](https://en.wikipedia.org/wiki/Delaporte_distribution)
- [Dirac delta function](https://en.wikipedia.org/wiki/Dirac_delta_function)
- [Directional statistics](https://en.wikipedia.org/wiki/Directional_statistics)
- [Dirichlet-multinomial distribution](https://en.wikipedia.org/wiki/Dirichlet-multinomial_distribution)
- [Dirichlet distribution](https://en.wikipedia.org/wiki/Dirichlet_distribution)
- [Discrete Weibull distribution](https://en.wikipedia.org/wiki/Discrete_Weibull_distribution)
- [Discrete phase-type distribution](https://en.wikipedia.org/wiki/Discrete_phase-type_distribution)
- [Discrete uniform distribution](https://en.wikipedia.org/wiki/Discrete_uniform_distribution)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Elliptical distribution](https://en.wikipedia.org/wiki/Elliptical_distribution)
- [Erlang distribution](https://en.wikipedia.org/wiki/Erlang_distribution)
- [Erwin Schrödinger](https://en.wikipedia.org/wiki/Erwin_Schr%C3%B6dinger)
- [Ewens's sampling formula](https://en.wikipedia.org/wiki/Ewens%27s_sampling_formula)
- [Kurtosis](https://en.wikipedia.org/wiki/Kurtosis)
- [Expected value](https://en.wikipedia.org/wiki/Expected_value)
- [Exponential-logarithmic distribution](https://en.wikipedia.org/wiki/Exponential-logarithmic_distribution)
- [Exponential dispersion model](https://en.wikipedia.org/wiki/Exponential_dispersion_model)
- [Exponential distribution](https://en.wikipedia.org/wiki/Exponential_distribution)
- [Exponential family](https://en.wikipedia.org/wiki/Exponential_family)
- [Extended negative binomial distribution](https://en.wikipedia.org/wiki/Extended_negative_binomial_distribution)
- [F-distribution](https://en.wikipedia.org/wiki/F-distribution)
- [First-hitting-time model](https://en.wikipedia.org/wiki/First-hitting-time_model)
- [Fisher's z-distribution](https://en.wikipedia.org/wiki/Fisher%27s_z-distribution)
- [Flory–Schulz distribution](https://en.wikipedia.org/wiki/Flory%E2%80%93Schulz_distribution)
- [Fokker–Planck equation](https://en.wikipedia.org/wiki/Fokker%E2%80%93Planck_equation)
- [Folded normal distribution](https://en.wikipedia.org/wiki/Folded_normal_distribution)
- [Fréchet distribution](https://en.wikipedia.org/wiki/Fr%C3%A9chet_distribution)
- [Fundamental solution](https://en.wikipedia.org/wiki/Fundamental_solution)
- [Gamma/Gompertz distribution](https://en.wikipedia.org/wiki/Gamma/Gompertz_distribution)
- [Gamma distribution](https://en.wikipedia.org/wiki/Gamma_distribution)
- [Gaussian q-distribution](https://en.wikipedia.org/wiki/Gaussian_q-distribution)
- [Gauss–Kuzmin distribution](https://en.wikipedia.org/wiki/Gauss%E2%80%93Kuzmin_distribution)
- [Generalised hyperbolic distribution](https://en.wikipedia.org/wiki/Generalised_hyperbolic_distribution)
- [Generalized Dirichlet distribution](https://en.wikipedia.org/wiki/Generalized_Dirichlet_distribution)
- [Generalized Pareto distribution](https://en.wikipedia.org/wiki/Generalized_Pareto_distribution)
- [Generalized beta distribution](https://en.wikipedia.org/wiki/Generalized_beta_distribution)
- [Generalized chi-squared distribution](https://en.wikipedia.org/wiki/Generalized_chi-squared_distribution)
- [Generalized extreme value distribution](https://en.wikipedia.org/wiki/Generalized_extreme_value_distribution)
- [Generalized gamma distribution](https://en.wikipedia.org/wiki/Generalized_gamma_distribution)
- [Generalized inverse Gaussian distribution](https://en.wikipedia.org/wiki/Generalized_inverse_Gaussian_distribution)
- [Generalized normal distribution](https://en.wikipedia.org/wiki/Generalized_normal_distribution)
- [Geometric distribution](https://en.wikipedia.org/wiki/Geometric_distribution)
- [Geometric stable distribution](https://en.wikipedia.org/wiki/Geometric_stable_distribution)
- [Gompertz distribution](https://en.wikipedia.org/wiki/Gompertz_distribution)
- [Gumbel distribution](https://en.wikipedia.org/wiki/Gumbel_distribution)
- [Half-logistic distribution](https://en.wikipedia.org/wiki/Half-logistic_distribution)
- [Half-normal distribution](https://en.wikipedia.org/wiki/Half-normal_distribution)
- [Holtsmark distribution](https://en.wikipedia.org/wiki/Holtsmark_distribution)
- [Hotelling's T-squared distribution](https://en.wikipedia.org/wiki/Hotelling%27s_T-squared_distribution)
- [Hugo Hadwiger](https://en.wikipedia.org/wiki/Hugo_Hadwiger)
- [Hyper-Erlang distribution](https://en.wikipedia.org/wiki/Hyper-Erlang_distribution)
- [Hyperbolic secant distribution](https://en.wikipedia.org/wiki/Hyperbolic_secant_distribution)
- [Hyperexponential distribution](https://en.wikipedia.org/wiki/Hyperexponential_distribution)
- [Hypergeometric distribution](https://en.wikipedia.org/wiki/Hypergeometric_distribution)
- [Hypoexponential distribution](https://en.wikipedia.org/wiki/Hypoexponential_distribution)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Inverse-Wishart distribution](https://en.wikipedia.org/wiki/Inverse-Wishart_distribution)
- [Inverse-chi-squared distribution](https://en.wikipedia.org/wiki/Inverse-chi-squared_distribution)
- [Inverse-gamma distribution](https://en.wikipedia.org/wiki/Inverse-gamma_distribution)
- [Inverse matrix gamma distribution](https://en.wikipedia.org/wiki/Inverse_matrix_gamma_distribution)
- [Irwin–Hall distribution](https://en.wikipedia.org/wiki/Irwin%E2%80%93Hall_distribution)
- [JSTOR](https://en.wikipedia.org/wiki/JSTOR)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Johnson's SU-distribution](https://en.wikipedia.org/wiki/Johnson%27s_SU-distribution)
- [Joint probability distribution](https://en.wikipedia.org/wiki/Joint_probability_distribution)
- [Journal of the Royal Statistical Society](https://en.wikipedia.org/wiki/Journal_of_the_Royal_Statistical_Society)
- [Kaniadakis Erlang distribution](https://en.wikipedia.org/wiki/Kaniadakis_Erlang_distribution)
- [Kaniadakis exponential distribution](https://en.wikipedia.org/wiki/Kaniadakis_exponential_distribution)
- [Kaniadakis Gamma distribution](https://en.wikipedia.org/wiki/Kaniadakis_Gamma_distribution)
- [Kaniadakis Gaussian distribution](https://en.wikipedia.org/wiki/Kaniadakis_Gaussian_distribution)
- [Kaniadakis logistic distribution](https://en.wikipedia.org/wiki/Kaniadakis_logistic_distribution)
- [Kaniadakis Weibull distribution](https://en.wikipedia.org/wiki/Kaniadakis_Weibull_distribution)
- [Kent distribution](https://en.wikipedia.org/wiki/Kent_distribution)
- [Kolmogorov–Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test)
- [Kumaraswamy distribution](https://en.wikipedia.org/wiki/Kumaraswamy_distribution)
- [Landau distribution](https://en.wikipedia.org/wiki/Landau_distribution)
- [Laplace distribution](https://en.wikipedia.org/wiki/Laplace_distribution)
- [Lewandowski-Kurowicka-Joe distribution](https://en.wikipedia.org/wiki/Lewandowski-Kurowicka-Joe_distribution)
- [List of probability distributions](https://en.wikipedia.org/wiki/List_of_probability_distributions)
- [Location–scale family](https://en.wikipedia.org/wiki/Location%E2%80%93scale_family)
- [Log-Cauchy distribution](https://en.wikipedia.org/wiki/Log-Cauchy_distribution)
- [Log-Laplace distribution](https://en.wikipedia.org/wiki/Log-Laplace_distribution)
- [Log-logistic distribution](https://en.wikipedia.org/wiki/Log-logistic_distribution)
- [Log-normal distribution](https://en.wikipedia.org/wiki/Log-normal_distribution)
- [Log-t distribution](https://en.wikipedia.org/wiki/Log-t_distribution)
- [Logarithmic distribution](https://en.wikipedia.org/wiki/Logarithmic_distribution)
- [Logistic distribution](https://en.wikipedia.org/wiki/Logistic_distribution)
- [Logit-normal distribution](https://en.wikipedia.org/wiki/Logit-normal_distribution)
- [Lomax distribution](https://en.wikipedia.org/wiki/Lomax_distribution)
- [Louis Bachelier](https://en.wikipedia.org/wiki/Louis_Bachelier)
- [Lévy distribution](https://en.wikipedia.org/wiki/L%C3%A9vy_distribution)
- [Marchenko–Pastur distribution](https://en.wikipedia.org/wiki/Marchenko%E2%80%93Pastur_distribution)
- [Marian Smoluchowski](https://en.wikipedia.org/wiki/Marian_Smoluchowski)
- [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
- [Matrix-exponential distribution](https://en.wikipedia.org/wiki/Matrix-exponential_distribution)
- [Matrix gamma distribution](https://en.wikipedia.org/wiki/Matrix_gamma_distribution)
- [Matrix normal distribution](https://en.wikipedia.org/wiki/Matrix_normal_distribution)
- [Matrix t-distribution](https://en.wikipedia.org/wiki/Matrix_t-distribution)
- [Maurice Tweedie](https://en.wikipedia.org/wiki/Maurice_Tweedie)
- [Maximum entropy probability distribution](https://en.wikipedia.org/wiki/Maximum_entropy_probability_distribution)
- [Maxwell–Boltzmann distribution](https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution)
- [Maxwell–Jüttner distribution](https://en.wikipedia.org/wiki/Maxwell%E2%80%93J%C3%BCttner_distribution)
- [Method of images](https://en.wikipedia.org/wiki/Method_of_images)
- [Mittag-Leffler distribution](https://en.wikipedia.org/wiki/Mittag-Leffler_distribution)
- [Mixed Poisson distribution](https://en.wikipedia.org/wiki/Mixed_Poisson_distribution)
- [Mixture distribution](https://en.wikipedia.org/wiki/Mixture_distribution)
- [Mode (statistics)](https://en.wikipedia.org/wiki/Mode_(statistics))
- [Moment-generating function](https://en.wikipedia.org/wiki/Moment-generating_function)
- [Multinomial distribution](https://en.wikipedia.org/wiki/Multinomial_distribution)
- [Multivariate Laplace distribution](https://en.wikipedia.org/wiki/Multivariate_Laplace_distribution)
- [Multivariate normal distribution](https://en.wikipedia.org/wiki/Multivariate_normal_distribution)
- [Multivariate stable distribution](https://en.wikipedia.org/wiki/Multivariate_stable_distribution)
- [Multivariate t-distribution](https://en.wikipedia.org/wiki/Multivariate_t-distribution)
- [Nakagami distribution](https://en.wikipedia.org/wiki/Nakagami_distribution)
- [Natural exponential family](https://en.wikipedia.org/wiki/Natural_exponential_family)
- [Exponential family](https://en.wikipedia.org/wiki/Exponential_family)
- [Exponential family](https://en.wikipedia.org/wiki/Exponential_family)
- [Nature (journal)](https://en.wikipedia.org/wiki/Nature_(journal))
- [Necessity and sufficiency](https://en.wikipedia.org/wiki/Necessity_and_sufficiency)
- [Negative binomial distribution](https://en.wikipedia.org/wiki/Negative_binomial_distribution)
- [Negative hypergeometric distribution](https://en.wikipedia.org/wiki/Negative_hypergeometric_distribution)
- [Negative multinomial distribution](https://en.wikipedia.org/wiki/Negative_multinomial_distribution)
- [Noncentral F-distribution](https://en.wikipedia.org/wiki/Noncentral_F-distribution)
- [Noncentral beta distribution](https://en.wikipedia.org/wiki/Noncentral_beta_distribution)
- [Noncentral chi-squared distribution](https://en.wikipedia.org/wiki/Noncentral_chi-squared_distribution)
- [Noncentral t-distribution](https://en.wikipedia.org/wiki/Noncentral_t-distribution)
- [Normal-Wishart distribution](https://en.wikipedia.org/wiki/Normal-Wishart_distribution)
- [Normal-gamma distribution](https://en.wikipedia.org/wiki/Normal-gamma_distribution)
- [Normal-inverse-Wishart distribution](https://en.wikipedia.org/wiki/Normal-inverse-Wishart_distribution)
- [Normal-inverse-gamma distribution](https://en.wikipedia.org/wiki/Normal-inverse-gamma_distribution)
- [Normal-inverse Gaussian distribution](https://en.wikipedia.org/wiki/Normal-inverse_Gaussian_distribution)
- [Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)
- [NumPy](https://en.wikipedia.org/wiki/NumPy)
- [PERT distribution](https://en.wikipedia.org/wiki/PERT_distribution)
- [PubMed Central](https://en.wikipedia.org/wiki/PubMed_Central)
- [PubMed](https://en.wikipedia.org/wiki/PubMed)
- [Parabolic fractal distribution](https://en.wikipedia.org/wiki/Parabolic_fractal_distribution)
- [Pareto distribution](https://en.wikipedia.org/wiki/Pareto_distribution)
- [Pearson distribution](https://en.wikipedia.org/wiki/Pearson_distribution)
- [Phase-type distribution](https://en.wikipedia.org/wiki/Phase-type_distribution)
- [Physikalische Zeitschrift](https://en.wikipedia.org/wiki/Physikalische_Zeitschrift)
- [Poisson binomial distribution](https://en.wikipedia.org/wiki/Poisson_binomial_distribution)
- [Poisson distribution](https://en.wikipedia.org/wiki/Poisson_distribution)
- [Poly-Weibull distribution](https://en.wikipedia.org/wiki/Poly-Weibull_distribution)
- [Probability density function](https://en.wikipedia.org/wiki/Probability_density_function)
- [Probability distribution](https://en.wikipedia.org/wiki/Probability_distribution)
- [Probability theory](https://en.wikipedia.org/wiki/Probability_theory)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Q-Gaussian distribution](https://en.wikipedia.org/wiki/Q-Gaussian_distribution)
- [Q-Weibull distribution](https://en.wikipedia.org/wiki/Q-Weibull_distribution)
- [Q-exponential distribution](https://en.wikipedia.org/wiki/Q-exponential_distribution)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Rademacher distribution](https://en.wikipedia.org/wiki/Rademacher_distribution)
- [Raised cosine distribution](https://en.wikipedia.org/wiki/Raised_cosine_distribution)
- [Random matrix](https://en.wikipedia.org/wiki/Random_matrix)
- [Random variable](https://en.wikipedia.org/wiki/Random_variable)
- [Rayleigh distribution](https://en.wikipedia.org/wiki/Rayleigh_distribution)
- [Reciprocal distribution](https://en.wikipedia.org/wiki/Reciprocal_distribution)
- [Inverse distribution](https://en.wikipedia.org/wiki/Inverse_distribution)
- [Rectified Gaussian distribution](https://en.wikipedia.org/wiki/Rectified_Gaussian_distribution)
- [Relativistic Breit–Wigner distribution](https://en.wikipedia.org/wiki/Relativistic_Breit%E2%80%93Wigner_distribution)
- [Rice distribution](https://en.wikipedia.org/wiki/Rice_distribution)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Scaled inverse chi-squared distribution](https://en.wikipedia.org/wiki/Scaled_inverse_chi-squared_distribution)
- [Shifted Gompertz distribution](https://en.wikipedia.org/wiki/Shifted_Gompertz_distribution)
- [Shifted log-logistic distribution](https://en.wikipedia.org/wiki/Shifted_log-logistic_distribution)
- [Singular distribution](https://en.wikipedia.org/wiki/Singular_distribution)
- [Skellam distribution](https://en.wikipedia.org/wiki/Skellam_distribution)
- [Skew normal distribution](https://en.wikipedia.org/wiki/Skew_normal_distribution)
- [Skewness](https://en.wikipedia.org/wiki/Skewness)
- [Slash distribution](https://en.wikipedia.org/wiki/Slash_distribution)
- [Soliton distribution](https://en.wikipedia.org/wiki/Soliton_distribution)
- [Stable distribution](https://en.wikipedia.org/wiki/Stable_distribution)
- [Independence (probability theory)](https://en.wikipedia.org/wiki/Independence_(probability_theory))
- [Statistical parameter](https://en.wikipedia.org/wiki/Statistical_parameter)
- [Stochastic process](https://en.wikipedia.org/wiki/Stochastic_process)
- [Stopping time](https://en.wikipedia.org/wiki/Stopping_time)
- [Student's t-distribution](https://en.wikipedia.org/wiki/Student%27s_t-distribution)
- [Support (mathematics)](https://en.wikipedia.org/wiki/Support_(mathematics))
- [Survival function](https://en.wikipedia.org/wiki/Survival_function)
- [The American Statistician](https://en.wikipedia.org/wiki/The_American_Statistician)
- [The R Journal](https://en.wikipedia.org/wiki/The_R_Journal)
- [Tracy–Widom distribution](https://en.wikipedia.org/wiki/Tracy%E2%80%93Widom_distribution)
- [Triangular distribution](https://en.wikipedia.org/wiki/Triangular_distribution)
- [Truncated normal distribution](https://en.wikipedia.org/wiki/Truncated_normal_distribution)
- [Tukey lambda distribution](https://en.wikipedia.org/wiki/Tukey_lambda_distribution)
- [Tweedie distribution](https://en.wikipedia.org/wiki/Tweedie_distribution)
- [Tweedie distribution](https://en.wikipedia.org/wiki/Tweedie_distribution)
- [Type-2 Gumbel distribution](https://en.wikipedia.org/wiki/Type-2_Gumbel_distribution)
- [U-quadratic distribution](https://en.wikipedia.org/wiki/U-quadratic_distribution)
- [Variance](https://en.wikipedia.org/wiki/Variance)
- [Variance-gamma distribution](https://en.wikipedia.org/wiki/Variance-gamma_distribution)
- [Voigt profile](https://en.wikipedia.org/wiki/Voigt_profile)
- [Von Mises distribution](https://en.wikipedia.org/wiki/Von_Mises_distribution)
- [Von Mises–Fisher distribution](https://en.wikipedia.org/wiki/Von_Mises%E2%80%93Fisher_distribution)
- [Weibull distribution](https://en.wikipedia.org/wiki/Weibull_distribution)
- [Wiener process](https://en.wikipedia.org/wiki/Wiener_process)
- [Wigner semicircle distribution](https://en.wikipedia.org/wiki/Wigner_semicircle_distribution)
- [Wilks's lambda distribution](https://en.wikipedia.org/wiki/Wilks%27s_lambda_distribution)
- [Wishart distribution](https://en.wikipedia.org/wiki/Wishart_distribution)
- [Wrapped Cauchy distribution](https://en.wikipedia.org/wiki/Wrapped_Cauchy_distribution)
- [Wrapped Lévy distribution](https://en.wikipedia.org/wiki/Wrapped_L%C3%A9vy_distribution)
- [Wrapped asymmetric Laplace distribution](https://en.wikipedia.org/wiki/Wrapped_asymmetric_Laplace_distribution)
- [Wrapped distribution](https://en.wikipedia.org/wiki/Wrapped_distribution)
- [Wrapped exponential distribution](https://en.wikipedia.org/wiki/Wrapped_exponential_distribution)
- [Wrapped normal distribution](https://en.wikipedia.org/wiki/Wrapped_normal_distribution)
- [Yule–Simon distribution](https://en.wikipedia.org/wiki/Yule%E2%80%93Simon_distribution)
- [Zeta distribution](https://en.wikipedia.org/wiki/Zeta_distribution)
- [Zipf's law](https://en.wikipedia.org/wiki/Zipf%27s_law)
- [Zipf–Mandelbrot law](https://en.wikipedia.org/wiki/Zipf%E2%80%93Mandelbrot_law)
- [Template:Probability distributions](https://en.wikipedia.org/wiki/Template:Probability_distributions)
- [Template talk:Probability distributions](https://en.wikipedia.org/wiki/Template_talk:Probability_distributions)
- [Help:Authority control](https://en.wikipedia.org/wiki/Help:Authority_control)
- [Category:Probability distributions](https://en.wikipedia.org/wiki/Category:Probability_distributions)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:38:58.303613+00:00_