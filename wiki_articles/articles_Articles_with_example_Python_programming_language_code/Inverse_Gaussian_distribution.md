# Inverse Gaussian distribution

## Metadata
- **Last Updated:** 2024-12-04 22:38:16 UTC
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

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 21:04:50 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 40252 bytes
- **Word Count:** 2392 words
