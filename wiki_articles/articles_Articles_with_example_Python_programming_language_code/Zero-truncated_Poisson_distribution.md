# Zero-truncated Poisson distribution

## Metadata
- **Last Updated:** 2024-12-03 07:37:21 UTC
- **Original Article:** [Zero-truncated Poisson distribution](https://en.wikipedia.org/wiki/Zero-truncated_Poisson_distribution)
- **Language:** en
- **Page ID:** 40180359

## Summary
In probability theory, the zero-truncated Poisson distribution (ZTP distribution) is a certain discrete probability distribution whose support is the set of positive integers.  This distribution is also known as the conditional Poisson distribution or the positive Poisson distribution. It is the conditional probability distribution of a Poisson-distributed random variable, given that the value of the random variable is not zero. Thus it is impossible for a ZTP random variable to be zero. Consider for example the random variable of the number of items in a shopper's basket at a supermarket checkout line.  Presumably a shopper does not stand in line with nothing to buy (i.e., the minimum purchase is 1 item), so this phenomenon may follow a ZTP distribution.
Since the ZTP is a truncated distribution with the truncation stipulated as k > 0, one can derive the probability mass function g(k;λ) from a standard Poisson distribution f(k;λ) as follows:

  
    
      
        g
        (
        k
        ;
        λ
        )
        =
        P
        (
        X
        =
        k
        ∣
        X
        >
        0
        )
        =
        
          
            
              f
              (
              k
              ;
              λ
              )
            
            
              1
              −
              f
              (
              0
              ;
              λ
              )
            
          
        
        =
        
          
            
              
                λ
                
                  k
                
              
              
                e
                
                  −
                  λ
                
              
            
            
              k
              !
              
                (
                
                  1
                  −
                  
                    e
                    
                      −
                      λ
                    
                  
                
                )
              
            
          
        
        =
        
          
            
              λ
              
                k
              
            
            
              (
              
                e
                
                  λ
                
              
              −
              1
              )
              k
              !
            
          
        
      
    
    {\displaystyle g(k;\lambda )=P(X=k\mid X>0)={\frac {f(k;\lambda )}{1-f(0;\lambda )}}={\frac {\lambda ^{k}e^{-\lambda }}{k!\left(1-e^{-\lambda }\right)}}={\frac {\lambda ^{k}}{(e^{\lambda }-1)k!}}}
  

The mean is

  
    
      
        E
        ⁡
        [
        X
        ]
        =
        
          
            λ
            
              1
              −
              
                e
                
                  −
                  λ
                
              
            
          
        
        =
        
          
            
              λ
              
                e
                
                  λ
                
              
            
            
              
                e
                
                  λ
                
              
              −
              1
            
          
        
      
    
    {\displaystyle \operatorname {E} [X]={\frac {\lambda }{1-e^{-\lambda }}}={\frac {\lambda e^{\lambda }}{e^{\lambda }-1}}}
  

and the variance is

  
    
      
        Var
        ⁡
        [
        X
        ]
        =
        
          
            
              λ
              +
              
                λ
                
                  2
                
              
            
            
              1
              −
              
                e
                
                  −
                  λ
                
              
            
          
        
        −
        
          
            
              λ
              
                2
              
            
            
              (
              1
              −
              
                e
                
                  −
                  λ
                
              
              
                )
                
                  2
                
              
            
          
        
        =
        E
        ⁡
        [
        X
        ]
        (
        1
        +
        λ
        −
        E
        ⁡
        [
        X
        ]
        )
      
    
    {\displaystyle \operatorname {Var} [X]={\frac {\lambda +\lambda ^{2}}{1-e^{-\lambda }}}-{\frac {\lambda ^{2}}{(1-e^{-\lambda })^{2}}}=\operatorname {E} [X](1+\lambda -\operatorname {E} [X])}

## Categories
This article belongs to the following categories:

- Category:All articles needing additional references
- Category:Articles needing additional references from August 2013
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Discrete distributions
- Category:Poisson distribution
- Category:Short description is different from Wikidata

## Table of Contents

- Parameter estimation
- Examples
- Generating zero-truncated Poisson-distributed random variables

## Content

In probability theory, the zero-truncated Poisson distribution (ZTP distribution) is a certain discrete probability distribution whose support is the set of positive integers.  This distribution is also known as the conditional Poisson distribution or the positive Poisson distribution. It is the conditional probability distribution of a Poisson-distributed random variable, given that the value of the random variable is not zero. Thus it is impossible for a ZTP random variable to be zero. Consider for example the random variable of the number of items in a shopper's basket at a supermarket checkout line.  Presumably a shopper does not stand in line with nothing to buy (i.e., the minimum purchase is 1 item), so this phenomenon may follow a ZTP distribution.
Since the ZTP is a truncated distribution with the truncation stipulated as k > 0, one can derive the probability mass function g(k;λ) from a standard Poisson distribution f(k;λ) as follows:

  
    
      
        g
        (
        k
        ;
        λ
        )
        =
        P
        (
        X
        =
        k
        ∣
        X
        >
        0
        )
        =
        
          
            
              f
              (
              k
              ;
              λ
              )
            
            
              1
              −
              f
              (
              0
              ;
              λ
              )
            
          
        
        =
        
          
            
              
                λ
                
                  k
                
              
              
                e
                
                  −
                  λ
                
              
            
            
              k
              !
              
                (
                
                  1
                  −
                  
                    e
                    
                      −
                      λ
                    
                  
                
                )
              
            
          
        
        =
        
          
            
              λ
              
                k
              
            
            
              (
              
                e
                
                  λ
                
              
              −
              1
              )
              k
              !
            
          
        
      
    
    {\displaystyle g(k;\lambda )=P(X=k\mid X>0)={\frac {f(k;\lambda )}{1-f(0;\lambda )}}={\frac {\lambda ^{k}e^{-\lambda }}{k!\left(1-e^{-\lambda }\right)}}={\frac {\lambda ^{k}}{(e^{\lambda }-1)k!}}}
  

The mean is

  
    
      
        E
        ⁡
        [
        X
        ]
        =
        
          
            λ
            
              1
              −
              
                e
                
                  −
                  λ
                
              
            
          
        
        =
        
          
            
              λ
              
                e
                
                  λ
                
              
            
            
              
                e
                
                  λ
                
              
              −
              1
            
          
        
      
    
    {\displaystyle \operatorname {E} [X]={\frac {\lambda }{1-e^{-\lambda }}}={\frac {\lambda e^{\lambda }}{e^{\lambda }-1}}}
  

and the variance is

  
    
      
        Var
        ⁡
        [
        X
        ]
        =
        
          
            
              λ
              +
              
                λ
                
                  2
                
              
            
            
              1
              −
              
                e
                
                  −
                  λ
                
              
            
          
        
        −
        
          
            
              λ
              
                2
              
            
            
              (
              1
              −
              
                e
                
                  −
                  λ
                
              
              
                )
                
                  2
                
              
            
          
        
        =
        E
        ⁡
        [
        X
        ]
        (
        1
        +
        λ
        −
        E
        ⁡
        [
        X
        ]
        )
      
    
    {\displaystyle \operatorname {Var} [X]={\frac {\lambda +\lambda ^{2}}{1-e^{-\lambda }}}-{\frac {\lambda ^{2}}{(1-e^{-\lambda })^{2}}}=\operatorname {E} [X](1+\lambda -\operatorname {E} [X])}

Parameter estimation
The method of moments estimator 
  
    
      
        
          
            
              λ
              ^
            
          
        
      
    
    {\displaystyle {\widehat {\lambda }}}
  
 for the parameter 
  
    
      
        λ
      
    
    {\displaystyle \lambda }
  
 is obtained by solving

  
    
      
        
          
            
              
                λ
                ^
              
            
            
              1
              −
              
                e
                
                  −
                  
                    
                      
                        λ
                        ^
                      
                    
                  
                
              
            
          
        
        =
        
          
            
              x
              ¯
            
          
        
      
    
    {\displaystyle {\frac {\widehat {\lambda }}{1-e^{-{\widehat {\lambda }}}}}={\bar {x}}}
  

where 
  
    
      
        
          
            
              x
              ¯
            
          
        
      
    
    {\displaystyle {\bar {x}}}
  
 is the sample mean.
This equation has a solution in terms of the Lambert W function. In practice, a solution may be found using numerical methods.

Examples
Insurance claims:
Imagine navigating the intricate landscape of auto insurance claims, where each claim signifies a unique event – an accident or damage occurrence. The ZTP distribution seamlessly aligns with this scenario, excluding the possibility of policyholders with zero claims.
Let X denote the random variable representing the number of insurance claims. If λ is the average rate of claims, the ZTP probability mass function takes the form:

  
    
      
        P
        (
        X
        =
        k
        )
        =
        
          
            
              
                λ
                
                  k
                
              
              
                e
                
                  −
                  λ
                
              
            
            
              k
              !
              
                (
                
                  1
                  −
                  
                    e
                    
                      −
                      λ
                    
                  
                
                )
              
            
          
        
      
    
    {\displaystyle P(X=k)={\frac {\lambda ^{k}e^{-\lambda }}{k!\left(1-e^{-\lambda }\right)}}}
  
 for k= 1,2,3,...
This formula encapsulates the probability of observing k claims given that at least one claim has transpired. The denominator ensures the exclusion of the improbable zero-claim scenario. By utilizing the zero-truncated Poisson distribution, the manufacturing company can analyze and predict the frequency of defects in their products while focusing on instances where defects exist. This distribution helps in understanding and improving the quality control process, especially when it's crucial to account for at least one defect.

Generating zero-truncated Poisson-distributed random variables
Random variables sampled from the zero-truncated Poisson distribution may be achieved using algorithms derived from Poisson distribution sampling algorithms.

init:
    Let k ← 1, t ← e−λ / (1 - e−λ) * λ, s ← t.
    Generate uniform random number u in [0,1].
while s < u do:
    k ← k + 1.
    t ← t * λ / k.
    s ← s + t.
return k.

The cost of the procedure above is linear in k, which may be large for large values of 
  
    
      
        λ
      
    
    {\displaystyle \lambda }
  
. Given access to an efficient sampler for non-truncated Poisson random variates, a non-iterative approach involves sampling from a truncated exponential distribution representing the time of the first event in a Poisson point process, conditional on such an event existing.
A simple NumPy implementation is:


== References ==

## Archive Info
- **Archived on:** 2024-12-15 20:38:57 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 8989 bytes
- **Word Count:** 711 words
