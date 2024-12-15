# Monte Carlo integration

## Article Metadata

- **Last Updated:** 2024-12-15T04:35:42.092777+00:00
- **Original Article:** [Monte Carlo integration](https://en.wikipedia.org/wiki/Monte_Carlo_integration)
- **Language:** en
- **Page ID:** 1112960

## Summary

In mathematics, Monte Carlo integration is a technique for numerical integration using random numbers. It is a particular Monte Carlo method that numerically computes a definite integral. While other algorithms usually evaluate the integrand at a regular grid, Monte Carlo randomly chooses points at which the integrand is evaluated. This method is particularly useful for higher-dimensional integrals.
There are different methods to perform a Monte Carlo integration, such as uniform sampling, strat

## Categories

- Category:Articles with example C code
- Category:Articles with example Python (programming language) code
- Category:Articles with example code
- Category:Articles with short description
- Category:Monte Carlo methods
- Category:Short description matches Wikidata

## Table of Contents

- Overview
- Recursive stratified sampling
- Importance sampling
- See also
- Notes
- References
- External links

## Content

In mathematics, Monte Carlo integration is a technique for numerical integration using random numbers. It is a particular Monte Carlo method that numerically computes a definite integral. While other algorithms usually evaluate the integrand at a regular grid, Monte Carlo randomly chooses points at which the integrand is evaluated. This method is particularly useful for higher-dimensional integrals.
There are different methods to perform a Monte Carlo integration, such as uniform sampling, stratified sampling, importance sampling, sequential Monte Carlo (also known as a particle filter), and mean-field particle methods.

Overview
In numerical integration, methods such as the trapezoidal rule use a deterministic approach. Monte Carlo integration, on the other hand, employs a non-deterministic approach: each realization provides a different outcome. In Monte Carlo, the final outcome is an approximation of the correct value with respective error bars, and the correct value is likely to be within those error bars.
The problem Monte Carlo integration addresses is the computation of a multidimensional definite integral

  
    
      
        I
        =
        
          ∫
          
            Ω
          
        
        f
        (
        
          
            
              x
            
            ¯
          
        
        )
        
        d
        
          
            
              x
            
            ¯
          
        
      
    
    {\displaystyle I=\int _{\Omega }f({\overline {\mathbf {x} }})\,d{\overline {\mathbf {x} }}}
  

where Ω, a subset of 
  
    
      
        
          
            R
          
          
            m
          
        
      
    
    {\displaystyle \mathbb {R} ^{m}}
  
, has volume

  
    
      
        V
        =
        
          ∫
          
            Ω
          
        
        d
        
          
            
              x
            
            ¯
          
        
      
    
    {\displaystyle V=\int _{\Omega }d{\overline {\mathbf {x} }}}
  

The naive Monte Carlo approach is to sample points uniformly on Ω: given N uniform samples,

  
    
      
        
          
            
              
                x
              
              ¯
            
          
          
            1
          
        
        ,
        ⋯
        ,
        
          
            
              
                x
              
              ¯
            
          
          
            N
          
        
        ∈
        Ω
        ,
      
    
    {\displaystyle {\overline {\mathbf {x} }}_{1},\cdots ,{\overline {\mathbf {x} }}_{N}\in \Omega ,}
  

I can be approximated by

  
    
      
        I
        ≈
        
          Q
          
            N
          
        
        ≡
        V
        
          
            1
            N
          
        
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        f
        (
        
          
            
              
                x
              
              ¯
            
          
          
            i
          
        
        )
        =
        V
        ⟨
        f
        ⟩
        .
      
    
    {\displaystyle I\approx Q_{N}\equiv V{\frac {1}{N}}\sum _{i=1}^{N}f({\overline {\mathbf {x} }}_{i})=V\langle f\rangle .}
  

This is because the law of large numbers ensures that

  
    
      
        
          lim
          
            N
            →
            ∞
          
        
        
          Q
          
            N
          
        
        =
        I
        .
      
    
    {\displaystyle \lim _{N\to \infty }Q_{N}=I.}
  

Given the estimation of I from QN, the error bars of QN can be estimated by the  sample variance using the unbiased estimate of the variance.

  
    
      
        
          V
          a
          r
        
        (
        f
        )
        =
        
          E
        
        (
        
          σ
          
            N
          
          
            2
          
        
        )
        ≡
        
          
            1
            
              N
              −
              1
            
          
        
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          E
        
        
          [
          
            
              (
              
                f
                (
                
                  
                    
                      
                        x
                      
                      ¯
                    
                  
                  
                    i
                  
                
                )
                −
                ⟨
                f
                ⟩
              
              )
            
            
              2
            
          
          ]
        
        .
      
    
    {\displaystyle \mathrm {Var} (f)=\mathrm {E} (\sigma _{N}^{2})\equiv {\frac {1}{N-1}}\sum _{i=1}^{N}\mathrm {E} \left[\left(f({\overline {\mathbf {x} }}_{i})-\langle f\rangle \right)^{2}\right].}
  

which leads to

  
    
      
        
          V
          a
          r
        
        (
        
          Q
          
            N
          
        
        )
        =
        
          
            
              V
              
                2
              
            
            
              N
              
                2
              
            
          
        
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          V
          a
          r
        
        (
        f
        )
        =
        
          V
          
            2
          
        
        
          
            
              
                V
                a
                r
              
              (
              f
              )
            
            N
          
        
        =
        
          V
          
            2
          
        
        
          
            
              
                E
              
              (
              
                σ
                
                  N
                
                
                  2
                
              
              )
            
            N
          
        
        .
      
    
    {\displaystyle \mathrm {Var} (Q_{N})={\frac {V^{2}}{N^{2}}}\sum _{i=1}^{N}\mathrm {Var} (f)=V^{2}{\frac {\mathrm {Var} (f)}{N}}=V^{2}{\frac {\mathrm {E} (\sigma _{N}^{2})}{N}}.}
  

Since the sequence

  
    
      
        
          {
          
            
              E
            
            (
            
              σ
              
                1
              
              
                2
              
            
            )
            ,
            
              E
            
            (
            
              σ
              
                2
              
              
                2
              
            
            )
            ,
            
              E
            
            (
            
              σ
              
                3
              
              
                2
              
            
            )
            ,
            …
          
          }
        
      
    
    {\displaystyle \left\{\mathrm {E} (\sigma _{1}^{2}),\mathrm {E} (\sigma _{2}^{2}),\mathrm {E} (\sigma _{3}^{2}),\ldots \right\}}
  

is bounded due to being identically equal to Var(f), as long as this is assumed finite, this variance decreases asymptotically to zero as 1/N. The estimation of the error of QN is thus

  
    
      
        δ
        
          Q
          
            N
          
        
        ≈
        
          
            
              V
              a
              r
            
            (
            
              Q
              
                N
              
            
            )
          
        
        =
        V
        
          
            
              
                V
                a
                r
              
              (
              f
              )
            
            
              N
            
          
        
        ,
      
    
    {\displaystyle \delta Q_{N}\approx {\sqrt {\mathrm {Var} (Q_{N})}}=V{\frac {\sqrt {\mathrm {Var} (f)}}{\sqrt {N}}},}
  

which decreases as 
  
    
      
        
          
            
              1
              
                N
              
            
          
        
      
    
    {\displaystyle {\tfrac {1}{\sqrt {N}}}}
  
. This is standard error of the mean multiplied with 
  
    
      
        V
      
    
    {\displaystyle V}
  
. 
This result does not depend on the number of dimensions of the integral, which is the promised advantage of Monte Carlo integration against most deterministic methods that depend exponentially on the dimension. 
It is important to notice that, unlike in deterministic methods, the estimate of the error is not a strict error bound; random sampling may not uncover all the important features of the integrand that can result in an underestimate of the error.
While the naive Monte Carlo works for simple examples, an improvement over deterministic algorithms can only be accomplished with algorithms that use problem-specific sampling distributions.
With an appropriate sample distribution it is possible to exploit the fact that almost all higher-dimensional integrands are very localized and only small subspace notably contributes to the integral.
A large part of the Monte Carlo literature is dedicated in developing strategies to improve the error estimates. In particular, stratified sampling—dividing the region in sub-domains—and importance sampling—sampling from non-uniform distributions—are two examples of such techniques.

Example
A paradigmatic example of a Monte Carlo integration is the estimation of π. Consider the function

  
    
      
        H
        
          (
          
            x
            ,
            y
          
          )
        
        =
        
          
            {
            
              
                
                  1
                
                
                  
                    if 
                  
                  
                    x
                    
                      2
                    
                  
                  +
                  
                    y
                    
                      2
                    
                  
                  ≤
                  1
                
              
              
                
                  0
                
                
                  
                    else
                  
                
              
            
            
          
        
      
    
    {\displaystyle H\left(x,y\right)={\begin{cases}1&{\text{if }}x^{2}+y^{2}\leq 1\\0&{\text{else}}\end{cases}}}
  

and the set Ω = [−1,1] × [−1,1] with V = 4. Notice that

  
    
      
        
          I
          
            π
          
        
        =
        
          ∫
          
            Ω
          
        
        H
        (
        x
        ,
        y
        )
        d
        x
        d
        y
        =
        π
        .
      
    
    {\displaystyle I_{\pi }=\int _{\Omega }H(x,y)dxdy=\pi .}
  

Thus, a crude way of calculating the value of π with Monte Carlo integration is to pick N random numbers on Ω and compute

  
    
      
        
          Q
          
            N
          
        
        =
        4
        
          
            1
            N
          
        
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        H
        (
        
          x
          
            i
          
        
        ,
        
          y
          
            i
          
        
        )
      
    
    {\displaystyle Q_{N}=4{\frac {1}{N}}\sum _{i=1}^{N}H(x_{i},y_{i})}
  

In the figure on the right, the relative error 
  
    
      
        
          
            
              
                
                  Q
                  
                    N
                  
                
                −
                π
              
              π
            
          
        
      
    
    {\displaystyle {\tfrac {Q_{N}-\pi }{\pi }}}
  
  is measured as a function of N, confirming the 
  
    
      
        
          
            
              1
              
                N
              
            
          
        
      
    
    {\displaystyle {\tfrac {1}{\sqrt {N}}}}
  
.

C/C++ example
Keep in mind that a true random number generator should be used.

Python example
Made in Python.

Wolfram Mathematica example
The code below describes a process of integrating the function

  
    
      
        f
        (
        x
        )
        =
        
          
            1
            
              1
              +
              sinh
              ⁡
              (
              2
              x
              )
              log
              ⁡
              (
              x
              
                )
                
                  2
                
              
            
          
        
      
    
    {\displaystyle f(x)={\frac {1}{1+\sinh(2x)\log(x)^{2}}}}
  

from 
  
    
      
        0.8
        <
        x
        <
        3
      
    
    {\displaystyle 0.8<x<3}
  
 using the Monte-Carlo method in Mathematica:

Recursive stratified sampling
Recursive stratified sampling is a generalization of one-dimensional adaptive quadratures to multi-dimensional integrals. On each recursion step the integral and the error are estimated using a plain Monte Carlo algorithm. If the error estimate is larger than the required accuracy the integration volume is divided into sub-volumes and the procedure is recursively applied to sub-volumes.
The ordinary 'dividing by two' strategy does not work for multi-dimensions as the number of sub-volumes grows far too quickly to keep track. Instead one estimates along which dimension a subdivision should bring the most dividends and only subdivides the volume along this dimension.
The stratified sampling algorithm concentrates the sampling points in the regions where the variance of the function is largest thus reducing the grand variance and making the sampling more effective, as shown on the illustration.
The popular MISER routine implements a similar algorithm.

MISER Monte Carlo
The MISER algorithm is based on recursive stratified sampling. This technique aims to reduce the overall integration error by concentrating integration points in the regions of highest variance.
The idea of stratified sampling begins with the observation that for two disjoint regions a and b with Monte Carlo estimates of the integral 
  
    
      
        
          E
          
            a
          
        
        (
        f
        )
      
    
    {\displaystyle E_{a}(f)}
  
 and 
  
    
      
        
          E
          
            b
          
        
        (
        f
        )
      
    
    {\displaystyle E_{b}(f)}
  
 and variances 
  
    
      
        
          σ
          
            a
          
          
            2
          
        
        (
        f
        )
      
    
    {\displaystyle \sigma _{a}^{2}(f)}
  
 and 
  
    
      
        
          σ
          
            b
          
          
            2
          
        
        (
        f
        )
      
    
    {\displaystyle \sigma _{b}^{2}(f)}
  
, the variance Var(f) of the combined estimate

  
    
      
        E
        (
        f
        )
        =
        
          
            
              1
              2
            
          
        
        
          (
          
            
              E
              
                a
              
            
            (
            f
            )
            +
            
              E
              
                b
              
            
            (
            f
            )
          
          )
        
      
    
    {\displaystyle E(f)={\tfrac {1}{2}}\left(E_{a}(f)+E_{b}(f)\right)}
  

is given by,

  
    
      
        
          V
          a
          r
        
        (
        f
        )
        =
        
          
            
              
                σ
                
                  a
                
                
                  2
                
              
              (
              f
              )
            
            
              4
              
                N
                
                  a
                
              
            
          
        
        +
        
          
            
              
                σ
                
                  b
                
                
                  2
                
              
              (
              f
              )
            
            
              4
              
                N
                
                  b
                
              
            
          
        
      
    
    {\displaystyle \mathrm {Var} (f)={\frac {\sigma _{a}^{2}(f)}{4N_{a}}}+{\frac {\sigma _{b}^{2}(f)}{4N_{b}}}}
  

It can be shown that this variance is minimized by distributing the points such that,

  
    
      
        
          
            
              N
              
                a
              
            
            
              
                N
                
                  a
                
              
              +
              
                N
                
                  b
                
              
            
          
        
        =
        
          
            
              σ
              
                a
              
            
            
              
                σ
                
                  a
                
              
              +
              
                σ
                
                  b
                
              
            
          
        
      
    
    {\displaystyle {\frac {N_{a}}{N_{a}+N_{b}}}={\frac {\sigma _{a}}{\sigma _{a}+\sigma _{b}}}}
  

Hence the smallest error estimate is obtained by allocating sample points in proportion to the standard deviation of the function in each sub-region.
The MISER algorithm proceeds by bisecting the integration region along one coordinate axis to give two sub-regions at each step. The direction is chosen by examining all d possible bisections and selecting the one which will minimize the combined variance of the two sub-regions. The variance in the sub-regions is estimated by sampling with a fraction of the total number of points available to the current step. The same procedure is then repeated recursively for each of the two half-spaces from the best bisection. The remaining sample points are allocated to the sub-regions using the formula for Na and Nb. This recursive allocation of integration points continues down to a user-specified depth where each sub-region is integrated using a plain Monte Carlo estimate. These individual values and their error estimates are then combined upwards to give an overall result and an estimate of its error.

Importance sampling
There are a variety of importance sampling algorithms, such as

Importance sampling algorithm
Importance sampling provides a very important tool to perform Monte-Carlo integration. The main result of importance sampling to this method is that the uniform sampling of 
  
    
      
        
          
            
              x
            
            ¯
          
        
      
    
    {\displaystyle {\overline {\mathbf {x} }}}
  
 is a particular case of a more generic choice, on which the samples are drawn from any distribution 
  
    
      
        p
        (
        
          
            
              x
            
            ¯
          
        
        )
      
    
    {\displaystyle p({\overline {\mathbf {x} }})}
  
. The idea is that 
  
    
      
        p
        (
        
          
            
              x
            
            ¯
          
        
        )
      
    
    {\displaystyle p({\overline {\mathbf {x} }})}
  
 can be chosen to decrease the variance of the measurement QN.
Consider the following example where one would like to numerically integrate a gaussian function, centered at 0, with σ = 1, from −1000 to 1000. Naturally, if the samples are drawn uniformly on the interval [−1000, 1000], only a very small part of them would be significant to the integral. This can be improved by choosing a different distribution from where the samples are chosen, for instance by sampling according to a gaussian distribution centered at 0, with σ = 1. Of course the "right" choice strongly depends on the integrand.
Formally, given a set of samples chosen from a distribution

  
    
      
        p
        (
        
          
            
              x
            
            ¯
          
        
        )
        :
        
        
          
            
              
                x
              
              ¯
            
          
          
            1
          
        
        ,
        ⋯
        ,
        
          
            
              
                x
              
              ¯
            
          
          
            N
          
        
        ∈
        V
        ,
      
    
    {\displaystyle p({\overline {\mathbf {x} }}):\qquad {\overline {\mathbf {x} }}_{1},\cdots ,{\overline {\mathbf {x} }}_{N}\in V,}
  

the estimator for I is given by

  
    
      
        
          Q
          
            N
          
        
        ≡
        
          
            1
            N
          
        
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          
            
              f
              (
              
                
                  
                    
                      x
                    
                    ¯
                  
                
                
                  i
                
              
              )
            
            
              p
              (
              
                
                  
                    
                      x
                    
                    ¯
                  
                
                
                  i
                
              
              )
            
          
        
      
    
    {\displaystyle Q_{N}\equiv {\frac {1}{N}}\sum _{i=1}^{N}{\frac {f({\overline {\mathbf {x} }}_{i})}{p({\overline {\mathbf {x} }}_{i})}}}
  

Intuitively, this says that if we pick a particular sample twice as much as other samples, we weight it half as much as the other samples. This estimator is naturally valid for uniform sampling, the case where 
  
    
      
        p
        (
        
          
            
              x
            
            ¯
          
        
        )
      
    
    {\displaystyle p({\overline {\mathbf {x} }})}
  
 is constant.
The Metropolis–Hastings algorithm is one of the most used algorithms to generate 
  
    
      
        
          
            
              x
            
            ¯
          
        
      
    
    {\displaystyle {\overline {\mathbf {x} }}}
  
 from 
  
    
      
        p
        (
        
          
            
              x
            
            ¯
          
        
        )
      
    
    {\displaystyle p({\overline {\mathbf {x} }})}
  
, thus providing an efficient way of computing integrals.

VEGAS Monte Carlo
The VEGAS algorithm approximates the exact distribution by making a number of passes over the integration region which creates the histogram of the function f. Each histogram is used to define a sampling distribution for the next pass. Asymptotically this procedure converges to the desired distribution. In order to avoid the number of histogram bins growing like Kd, the probability distribution is approximated by a separable function:

  
    
      
        g
        (
        
          x
          
            1
          
        
        ,
        
          x
          
            2
          
        
        ,
        …
        )
        =
        
          g
          
            1
          
        
        (
        
          x
          
            1
          
        
        )
        
          g
          
            2
          
        
        (
        
          x
          
            2
          
        
        )
        …
      
    
    {\displaystyle g(x_{1},x_{2},\ldots )=g_{1}(x_{1})g_{2}(x_{2})\ldots }
  

so that the number of bins required is only Kd. This is equivalent to locating the peaks of the function from the projections of the integrand onto the coordinate axes. The efficiency of VEGAS depends on the validity of this assumption. It is most efficient when the peaks of the integrand are well-localized. If an integrand can be rewritten in a form which is approximately separable this will increase the efficiency of integration with VEGAS. VEGAS incorporates a number of additional features, and combines both stratified sampling and importance sampling.

See also
Quasi-Monte Carlo method
Auxiliary field Monte Carlo
Monte Carlo method in statistical physics
Monte Carlo method
Variance reduction

Notes
References
External links
Café math : Monte Carlo Integration : A blog article describing Monte Carlo integration (principle, hypothesis, confidence interval)
Boost.Math : Naive Monte Carlo integration: Documentation for the C++ naive Monte-Carlo routines
Monte Carlo applet applied in statistical physics problems

## Related Articles

### Internal Links

- [Acta Numerica](https://en.wikipedia.org/wiki/Acta_Numerica)
- [Adaptive quadrature](https://en.wikipedia.org/wiki/Adaptive_quadrature)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Auxiliary-field Monte Carlo](https://en.wikipedia.org/wiki/Auxiliary-field_Monte_Carlo)
- [Bias of an estimator](https://en.wikipedia.org/wiki/Bias_of_an_estimator)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [David J. C. MacKay](https://en.wikipedia.org/wiki/David_J._C._MacKay)
- [Integral](https://en.wikipedia.org/wiki/Integral)
- [Deterministic algorithm](https://en.wikipedia.org/wiki/Deterministic_algorithm)
- [Dirk Kroese](https://en.wikipedia.org/wiki/Dirk_Kroese)
- [Disjoint sets](https://en.wikipedia.org/wiki/Disjoint_sets)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Importance sampling](https://en.wikipedia.org/wiki/Importance_sampling)
- [Journal of Computational Physics](https://en.wikipedia.org/wiki/Journal_of_Computational_Physics)
- [Law of large numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers)
- [Mathematical Reviews](https://en.wikipedia.org/wiki/Mathematical_Reviews)
- [Wolfram Mathematica](https://en.wikipedia.org/wiki/Wolfram_Mathematica)
- [Mathematics](https://en.wikipedia.org/wiki/Mathematics)
- [Mean-field particle methods](https://en.wikipedia.org/wiki/Mean-field_particle_methods)
- [Metropolis–Hastings algorithm](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm)
- [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- [Monte Carlo method in statistical mechanics](https://en.wikipedia.org/wiki/Monte_Carlo_method_in_statistical_mechanics)
- [Multiple integral](https://en.wikipedia.org/wiki/Multiple_integral)
- [Numerical integration](https://en.wikipedia.org/wiki/Numerical_integration)
- [Particle filter](https://en.wikipedia.org/wiki/Particle_filter)
- [Pseudorandomness](https://en.wikipedia.org/wiki/Pseudorandomness)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quasi-Monte Carlo method](https://en.wikipedia.org/wiki/Quasi-Monte_Carlo_method)
- [Russel E. Caflisch](https://en.wikipedia.org/wiki/Russel_E._Caflisch)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Variance](https://en.wikipedia.org/wiki/Variance)
- [Standard error](https://en.wikipedia.org/wiki/Standard_error)
- [Stochastic](https://en.wikipedia.org/wiki/Stochastic)
- [Stratified sampling](https://en.wikipedia.org/wiki/Stratified_sampling)
- [Trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule)
- [Continuous uniform distribution](https://en.wikipedia.org/wiki/Continuous_uniform_distribution)
- [VEGAS algorithm](https://en.wikipedia.org/wiki/VEGAS_algorithm)
- [Variance reduction](https://en.wikipedia.org/wiki/Variance_reduction)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:35:42.092777+00:00_