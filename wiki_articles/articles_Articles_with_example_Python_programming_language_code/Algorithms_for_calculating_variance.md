# Algorithms for calculating variance

## Metadata
- **Last Updated:** 2024-12-03 06:50:42 UTC
- **Original Article:** [Algorithms for calculating variance](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance)
- **Language:** en
- **Page ID:** 1063

## Summary
Algorithms for calculating variance play a major role in computational statistics. A key difficulty in the design of good algorithms for this problem is that formulas for the variance may involve sums of squares, which can lead to numerical instability as well as to arithmetic overflow when dealing with large values.

## Categories
This article belongs to the following categories:

- Category:All articles with unsourced statements
- Category:Articles with example Python (programming language) code
- Category:Articles with example pseudocode
- Category:Articles with short description
- Category:Articles with unsourced statements from March 2023
- Category:Short description matches Wikidata
- Category:Statistical algorithms
- Category:Statistical deviation and dispersion
- Category:Use dmy dates from July 2020

## Table of Contents

- Naïve algorithm
- Two-pass algorithm
- Welford's online algorithm
- Weighted incremental algorithm
- Parallel algorithm
- Example
- Higher-order statistics
- Covariance
- See also
- References
- External links

## Content

Algorithms for calculating variance play a major role in computational statistics. A key difficulty in the design of good algorithms for this problem is that formulas for the variance may involve sums of squares, which can lead to numerical instability as well as to arithmetic overflow when dealing with large values.

Naïve algorithm
A formula for calculating the variance of an entire population of size N is:

  
    
      
        
          σ
          
            2
          
        
        =
        
          
            
              (
              
                x
                
                  2
                
              
              )
            
            ¯
          
        
        −
        
          
            
              
                x
                ¯
              
            
          
          
            2
          
        
        =
        
          
            
              
                ∑
                
                  i
                  =
                  1
                
                
                  N
                
              
              
                x
                
                  i
                
                
                  2
                
              
              −
              (
              
                ∑
                
                  i
                  =
                  1
                
                
                  N
                
              
              
                x
                
                  i
                
              
              
                )
                
                  2
                
              
              
                /
              
              N
            
            N
          
        
        .
      
    
    {\displaystyle \sigma ^{2}={\overline {(x^{2})}}-{\bar {x}}^{2}={\frac {\sum _{i=1}^{N}x_{i}^{2}-(\sum _{i=1}^{N}x_{i})^{2}/N}{N}}.}
  

Using Bessel's correction to calculate an unbiased estimate of the population variance from a finite sample of n observations, the formula is:

  
    
      
        
          s
          
            2
          
        
        =
        
          (
          
            
              
                
                  
                    ∑
                    
                      i
                      =
                      1
                    
                    
                      n
                    
                  
                  
                    x
                    
                      i
                    
                    
                      2
                    
                  
                
                n
              
            
            −
            
              
                (
                
                  
                    
                      
                        ∑
                        
                          i
                          =
                          1
                        
                        
                          n
                        
                      
                      
                        x
                        
                          i
                        
                      
                    
                    n
                  
                
                )
              
              
                2
              
            
          
          )
        
        ⋅
        
          
            n
            
              n
              −
              1
            
          
        
        .
      
    
    {\displaystyle s^{2}=\left({\frac {\sum _{i=1}^{n}x_{i}^{2}}{n}}-\left({\frac {\sum _{i=1}^{n}x_{i}}{n}}\right)^{2}\right)\cdot {\frac {n}{n-1}}.}
  

Therefore, a naïve algorithm to calculate the estimated variance is given by the following:

This algorithm can easily be adapted to compute the variance of a finite population: simply divide by n instead of n − 1 on the last line.
Because SumSq and (Sum×Sum)/n can be very similar numbers, cancellation can lead to the precision of the result to be much less than the inherent precision of the floating-point arithmetic used to perform the computation.  Thus this algorithm should not be used in practice, and several alternate, numerically stable, algorithms have been proposed. This is particularly bad if the standard deviation is small relative to the mean.

Computing shifted data
The variance is invariant with respect to changes in a location parameter, a property which can be used to avoid the catastrophic cancellation in this formula.

  
    
      
        Var
        ⁡
        (
        X
        −
        K
        )
        =
        Var
        ⁡
        (
        X
        )
        .
      
    
    {\displaystyle \operatorname {Var} (X-K)=\operatorname {Var} (X).}
  

with 
  
    
      
        K
      
    
    {\displaystyle K}
  
 any constant, which leads to the new formula

  
    
      
        
          σ
          
            2
          
        
        =
        
          
            
              
                ∑
                
                  i
                  =
                  1
                
                
                  n
                
              
              (
              
                x
                
                  i
                
              
              −
              K
              
                )
                
                  2
                
              
              −
              (
              
                ∑
                
                  i
                  =
                  1
                
                
                  n
                
              
              (
              
                x
                
                  i
                
              
              −
              K
              )
              
                )
                
                  2
                
              
              
                /
              
              n
            
            
              n
              −
              1
            
          
        
        .
      
    
    {\displaystyle \sigma ^{2}={\frac {\sum _{i=1}^{n}(x_{i}-K)^{2}-(\sum _{i=1}^{n}(x_{i}-K))^{2}/n}{n-1}}.}
  

the closer 
  
    
      
        K
      
    
    {\displaystyle K}
  
 is to the mean value the more accurate the result will be, but just choosing a value inside the
samples range will guarantee the desired stability. If the values 
  
    
      
        (
        
          x
          
            i
          
        
        −
        K
        )
      
    
    {\displaystyle (x_{i}-K)}
  
 are small then there are no problems with the sum of its squares, on the contrary, if they are large it necessarily means that the variance is large as well. In any case the second term in the formula is always smaller than the first one therefore no cancellation may occur.
If just the first sample is taken as 
  
    
      
        K
      
    
    {\displaystyle K}
  
 the algorithm can be written in Python programming language as

This formula also facilitates the incremental computation that can be expressed as

Two-pass algorithm
An alternative approach, using a different formula for the variance, first computes the sample mean,

  
    
      
        
          
            
              x
              ¯
            
          
        
        =
        
          
            
              
                ∑
                
                  j
                  =
                  1
                
                
                  n
                
              
              
                x
                
                  j
                
              
            
            n
          
        
        ,
      
    
    {\displaystyle {\bar {x}}={\frac {\sum _{j=1}^{n}x_{j}}{n}},}
  

and then computes the sum of the squares of the differences from the mean,

  
    
      
        
          sample variance
        
        =
        
          s
          
            2
          
        
        =
        
          
            
              
                
                  ∑
                  
                    i
                    =
                    1
                  
                  
                    n
                  
                
                (
                
                  x
                  
                    i
                  
                
                −
                
                  
                    
                      x
                      ¯
                    
                  
                
                
                  )
                  
                    2
                  
                
              
              
                n
                −
                1
              
            
          
        
        ,
      
    
    {\displaystyle {\text{sample variance}}=s^{2}={\dfrac {\sum _{i=1}^{n}(x_{i}-{\bar {x}})^{2}}{n-1}},}
  

where s is the standard deviation.  This is given by the following code:

This algorithm is numerically stable if n is small. However, the results of both of these simple algorithms ("naïve" and "two-pass") can depend inordinately on the ordering of the data and can give poor results for very large data sets due to repeated roundoff error in the accumulation of the sums. Techniques such as compensated summation can be used to combat this error to a degree.

Welford's online algorithm
It is often useful to be able to compute the variance in a single pass, inspecting each value 
  
    
      
        
          x
          
            i
          
        
      
    
    {\displaystyle x_{i}}
  
 only once; for example, when the data is being collected without enough storage to keep all the values, or when costs of memory access dominate those of computation.  For such an online algorithm, a recurrence relation is required between quantities from which the required statistics can be calculated in a numerically stable fashion.
The following formulas can be used to update the mean and (estimated) variance of the sequence, for an additional element xn. Here, 
  
    
      
        
          
            
              x
              ¯
            
          
          
            n
          
        
        =
        
          
            1
            n
          
        
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        
          x
          
            i
          
        
      
    
    {\textstyle {\overline {x}}_{n}={\frac {1}{n}}\sum _{i=1}^{n}x_{i}}
  
 denotes the sample mean of the first n samples 
  
    
      
        (
        
          x
          
            1
          
        
        ,
        …
        ,
        
          x
          
            n
          
        
        )
      
    
    {\displaystyle (x_{1},\dots ,x_{n})}
  
, 
  
    
      
        
          σ
          
            n
          
          
            2
          
        
        =
        
          
            1
            n
          
        
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        
          
            (
            
              
                x
                
                  i
                
              
              −
              
                
                  
                    x
                    ¯
                  
                
                
                  n
                
              
            
            )
          
          
            2
          
        
      
    
    {\textstyle \sigma _{n}^{2}={\frac {1}{n}}\sum _{i=1}^{n}\left(x_{i}-{\overline {x}}_{n}\right)^{2}}
  
 their biased sample variance, and 
  
    
      
        
          s
          
            n
          
          
            2
          
        
        =
        
          
            1
            
              n
              −
              1
            
          
        
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        
          
            (
            
              
                x
                
                  i
                
              
              −
              
                
                  
                    x
                    ¯
                  
                
                
                  n
                
              
            
            )
          
          
            2
          
        
      
    
    {\textstyle s_{n}^{2}={\frac {1}{n-1}}\sum _{i=1}^{n}\left(x_{i}-{\overline {x}}_{n}\right)^{2}}
  
 their unbiased sample variance.

  
    
      
        
          
            
              
                x
                ¯
              
            
          
          
            n
          
        
        =
        
          
            
              (
              n
              −
              1
              )
              
              
                
                  
                    
                      x
                      ¯
                    
                  
                
                
                  n
                  −
                  1
                
              
              +
              
                x
                
                  n
                
              
            
            n
          
        
        =
        
          
            
              
                x
                ¯
              
            
          
          
            n
            −
            1
          
        
        +
        
          
            
              
                x
                
                  n
                
              
              −
              
                
                  
                    
                      x
                      ¯
                    
                  
                
                
                  n
                  −
                  1
                
              
            
            n
          
        
      
    
    {\displaystyle {\bar {x}}_{n}={\frac {(n-1)\,{\bar {x}}_{n-1}+x_{n}}{n}}={\bar {x}}_{n-1}+{\frac {x_{n}-{\bar {x}}_{n-1}}{n}}}
  

  
    
      
        
          σ
          
            n
          
          
            2
          
        
        =
        
          
            
              (
              n
              −
              1
              )
              
              
                σ
                
                  n
                  −
                  1
                
                
                  2
                
              
              +
              (
              
                x
                
                  n
                
              
              −
              
                
                  
                    
                      x
                      ¯
                    
                  
                
                
                  n
                  −
                  1
                
              
              )
              (
              
                x
                
                  n
                
              
              −
              
                
                  
                    
                      x
                      ¯
                    
                  
                
                
                  n
                
              
              )
            
            n
          
        
        =
        
          σ
          
            n
            −
            1
          
          
            2
          
        
        +
        
          
            
              (
              
                x
                
                  n
                
              
              −
              
                
                  
                    
                      x
                      ¯
                    
                  
                
                
                  n
                  −
                  1
                
              
              )
              (
              
                x
                
                  n
                
              
              −
              
                
                  
                    
                      x
                      ¯
                    
                  
                
                
                  n
                
              
              )
              −
              
                σ
                
                  n
                  −
                  1
                
                
                  2
                
              
            
            n
          
        
        .
      
    
    {\displaystyle \sigma _{n}^{2}={\frac {(n-1)\,\sigma _{n-1}^{2}+(x_{n}-{\bar {x}}_{n-1})(x_{n}-{\bar {x}}_{n})}{n}}=\sigma _{n-1}^{2}+{\frac {(x_{n}-{\bar {x}}_{n-1})(x_{n}-{\bar {x}}_{n})-\sigma _{n-1}^{2}}{n}}.}
  

  
    
      
        
          s
          
            n
          
          
            2
          
        
        =
        
          
            
              n
              −
              2
            
            
              n
              −
              1
            
          
        
        
        
          s
          
            n
            −
            1
          
          
            2
          
        
        +
        
          
            
              (
              
                x
                
                  n
                
              
              −
              
                
                  
                    
                      x
                      ¯
                    
                  
                
                
                  n
                  −
                  1
                
              
              
                )
                
                  2
                
              
            
            n
          
        
        =
        
          s
          
            n
            −
            1
          
          
            2
          
        
        +
        
          
            
              (
              
                x
                
                  n
                
              
              −
              
                
                  
                    
                      x
                      ¯
                    
                  
                
                
                  n
                  −
                  1
                
              
              
                )
                
                  2
                
              
            
            n
          
        
        −
        
          
            
              s
              
                n
                −
                1
              
              
                2
              
            
            
              n
              −
              1
            
          
        
        ,
        
        n
        >
        1
      
    
    {\displaystyle s_{n}^{2}={\frac {n-2}{n-1}}\,s_{n-1}^{2}+{\frac {(x_{n}-{\bar {x}}_{n-1})^{2}}{n}}=s_{n-1}^{2}+{\frac {(x_{n}-{\bar {x}}_{n-1})^{2}}{n}}-{\frac {s_{n-1}^{2}}{n-1}},\quad n>1}
  

These formulas suffer from numerical instability , as they repeatedly subtract a small number from a big number which scales with n. A better quantity for updating is the sum of squares of differences from the current mean, 
  
    
      
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        (
        
          x
          
            i
          
        
        −
        
          
            
              
                x
                ¯
              
            
          
          
            n
          
        
        
          )
          
            2
          
        
      
    
    {\textstyle \sum _{i=1}^{n}(x_{i}-{\bar {x}}_{n})^{2}}
  
, here denoted 
  
    
      
        
          M
          
            2
            ,
            n
          
        
      
    
    {\displaystyle M_{2,n}}
  
:

  
    
      
        
          
            
              
                
                  M
                  
                    2
                    ,
                    n
                  
                
              
              
                
                =
                
                  M
                  
                    2
                    ,
                    n
                    −
                    1
                  
                
                +
                (
                
                  x
                  
                    n
                  
                
                −
                
                  
                    
                      
                        x
                        ¯
                      
                    
                  
                  
                    n
                    −
                    1
                  
                
                )
                (
                
                  x
                  
                    n
                  
                
                −
                
                  
                    
                      
                        x
                        ¯
                      
                    
                  
                  
                    n
                  
                
                )
              
            
            
              
                
                  σ
                  
                    n
                  
                  
                    2
                  
                
              
              
                
                =
                
                  
                    
                      M
                      
                        2
                        ,
                        n
                      
                    
                    n
                  
                
              
            
            
              
                
                  s
                  
                    n
                  
                  
                    2
                  
                
              
              
                
                =
                
                  
                    
                      M
                      
                        2
                        ,
                        n
                      
                    
                    
                      n
                      −
                      1
                    
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}M_{2,n}&=M_{2,n-1}+(x_{n}-{\bar {x}}_{n-1})(x_{n}-{\bar {x}}_{n})\\[4pt]\sigma _{n}^{2}&={\frac {M_{2,n}}{n}}\\[4pt]s_{n}^{2}&={\frac {M_{2,n}}{n-1}}\end{aligned}}}
  

This algorithm was found by Welford, and it has been thoroughly analyzed. It is also common to denote 
  
    
      
        
          M
          
            k
          
        
        =
        
          
            
              
                x
                ¯
              
            
          
          
            k
          
        
      
    
    {\displaystyle M_{k}={\bar {x}}_{k}}
  
 and 
  
    
      
        
          S
          
            k
          
        
        =
        
          M
          
            2
            ,
            k
          
        
      
    
    {\displaystyle S_{k}=M_{2,k}}
  
.
An example Python implementation for Welford's algorithm is given below.

This algorithm is much less prone to loss of precision due to catastrophic cancellation, but might not be as efficient because of the division operation inside the loop.  For a particularly robust two-pass algorithm for computing the variance, one can first compute and subtract an estimate of the mean, and then use this algorithm on the residuals.
The parallel algorithm below illustrates how to merge multiple sets of statistics calculated online.

Weighted incremental algorithm
The algorithm can be extended to handle unequal sample weights, replacing the simple counter n with the sum of weights seen so far.  West (1979) suggests this incremental algorithm:

Parallel algorithm
Chan et al. note that Welford's online algorithm detailed above is a special case of an algorithm that works for combining arbitrary sets 
  
    
      
        A
      
    
    {\displaystyle A}
  
 and 
  
    
      
        B
      
    
    {\displaystyle B}
  
:

  
    
      
        
          
            
              
                
                  n
                  
                    A
                    B
                  
                
              
              
                
                =
                
                  n
                  
                    A
                  
                
                +
                
                  n
                  
                    B
                  
                
              
            
            
              
                δ
              
              
                
                =
                
                  
                    
                      
                        x
                        ¯
                      
                    
                  
                  
                    B
                  
                
                −
                
                  
                    
                      
                        x
                        ¯
                      
                    
                  
                  
                    A
                  
                
              
            
            
              
                
                  
                    
                      
                        x
                        ¯
                      
                    
                  
                  
                    A
                    B
                  
                
              
              
                
                =
                
                  
                    
                      
                        x
                        ¯
                      
                    
                  
                  
                    A
                  
                
                +
                δ
                ⋅
                
                  
                    
                      n
                      
                        B
                      
                    
                    
                      n
                      
                        A
                        B
                      
                    
                  
                
              
            
            
              
                
                  M
                  
                    2
                    ,
                    A
                    B
                  
                
              
              
                
                =
                
                  M
                  
                    2
                    ,
                    A
                  
                
                +
                
                  M
                  
                    2
                    ,
                    B
                  
                
                +
                
                  δ
                  
                    2
                  
                
                ⋅
                
                  
                    
                      
                        n
                        
                          A
                        
                      
                      
                        n
                        
                          B
                        
                      
                    
                    
                      n
                      
                        A
                        B
                      
                    
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}n_{AB}&=n_{A}+n_{B}\\\delta &={\bar {x}}_{B}-{\bar {x}}_{A}\\{\bar {x}}_{AB}&={\bar {x}}_{A}+\delta \cdot {\frac {n_{B}}{n_{AB}}}\\M_{2,AB}&=M_{2,A}+M_{2,B}+\delta ^{2}\cdot {\frac {n_{A}n_{B}}{n_{AB}}}\\\end{aligned}}}
  
.
This may be useful when, for example, multiple processing units may be assigned to discrete parts of the input.
Chan's method for estimating the mean is numerically unstable when 
  
    
      
        
          n
          
            A
          
        
        ≈
        
          n
          
            B
          
        
      
    
    {\displaystyle n_{A}\approx n_{B}}
  
 and both are large, because the numerical error in 
  
    
      
        δ
        =
        
          
            
              
                x
                ¯
              
            
          
          
            B
          
        
        −
        
          
            
              
                x
                ¯
              
            
          
          
            A
          
        
      
    
    {\displaystyle \delta ={\bar {x}}_{B}-{\bar {x}}_{A}}
  
 is not scaled down in the way that it is in the 
  
    
      
        
          n
          
            B
          
        
        =
        1
      
    
    {\displaystyle n_{B}=1}
  
 case. In such cases, prefer 
  
    
      
        
          
            
              
                x
                ¯
              
            
          
          
            A
            B
          
        
        =
        
          
            
              
                n
                
                  A
                
              
              
                
                  
                    
                      x
                      ¯
                    
                  
                
                
                  A
                
              
              +
              
                n
                
                  B
                
              
              
                
                  
                    
                      x
                      ¯
                    
                  
                
                
                  B
                
              
            
            
              n
              
                A
                B
              
            
          
        
      
    
    {\textstyle {\bar {x}}_{AB}={\frac {n_{A}{\bar {x}}_{A}+n_{B}{\bar {x}}_{B}}{n_{AB}}}}
  
.

This can be generalized to allow parallelization with AVX, with GPUs, and computer clusters, and to covariance.

Example
Assume that all floating point operations use standard IEEE 754 double-precision arithmetic. Consider the sample (4, 7, 13, 16) from an infinite population. Based on this sample, the estimated population mean is 10, and the unbiased estimate of population variance is 30.  Both the naïve algorithm and two-pass algorithm compute these values correctly.
Next consider the sample (108 + 4, 108 + 7, 108 + 13, 108 + 16), which gives rise to the same estimated variance as the first sample.  The two-pass algorithm computes this variance estimate correctly, but the naïve algorithm returns 29.333333333333332 instead of 30.
While this loss of precision may be tolerable and viewed as a minor flaw of the naïve algorithm, further increasing the offset makes the error catastrophic.  Consider the sample (109 + 4, 109 + 7, 109 + 13, 109 + 16).  Again the estimated population variance of 30 is computed correctly by the two-pass algorithm, but the naïve algorithm now computes it as −170.66666666666666.  This is a serious problem with naïve algorithm and is due to catastrophic cancellation in the subtraction of two similar numbers at the final stage of the algorithm.

Higher-order statistics
Terriberry extends Chan's formulae to calculating the third and fourth central moments, needed for example when estimating skewness and kurtosis:

  
    
      
        
          
            
              
                
                  M
                  
                    3
                    ,
                    X
                  
                
                =
                
                  M
                  
                    3
                    ,
                    A
                  
                
                +
                
                  M
                  
                    3
                    ,
                    B
                  
                
              
              
                
                

                
                +
                
                  δ
                  
                    3
                  
                
                
                  
                    
                      
                        n
                        
                          A
                        
                      
                      
                        n
                        
                          B
                        
                      
                      (
                      
                        n
                        
                          A
                        
                      
                      −
                      
                        n
                        
                          B
                        
                      
                      )
                    
                    
                      n
                      
                        X
                      
                      
                        2
                      
                    
                  
                
                +
                3
                δ
                
                  
                    
                      
                        n
                        
                          A
                        
                      
                      
                        M
                        
                          2
                          ,
                          B
                        
                      
                      −
                      
                        n
                        
                          B
                        
                      
                      
                        M
                        
                          2
                          ,
                          A
                        
                      
                    
                    
                      n
                      
                        X
                      
                    
                  
                
              
            
            
              
                
                  M
                  
                    4
                    ,
                    X
                  
                
                =
                
                  M
                  
                    4
                    ,
                    A
                  
                
                +
                
                  M
                  
                    4
                    ,
                    B
                  
                
              
              
                
                

                
                +
                
                  δ
                  
                    4
                  
                
                
                  
                    
                      
                        n
                        
                          A
                        
                      
                      
                        n
                        
                          B
                        
                      
                      
                        (
                        
                          
                            n
                            
                              A
                            
                            
                              2
                            
                          
                          −
                          
                            n
                            
                              A
                            
                          
                          
                            n
                            
                              B
                            
                          
                          +
                          
                            n
                            
                              B
                            
                            
                              2
                            
                          
                        
                        )
                      
                    
                    
                      n
                      
                        X
                      
                      
                        3
                      
                    
                  
                
              
            
            
              
              
                
                

                
                +
                6
                
                  δ
                  
                    2
                  
                
                
                  
                    
                      
                        n
                        
                          A
                        
                        
                          2
                        
                      
                      
                        M
                        
                          2
                          ,
                          B
                        
                      
                      +
                      
                        n
                        
                          B
                        
                        
                          2
                        
                      
                      
                        M
                        
                          2
                          ,
                          A
                        
                      
                    
                    
                      n
                      
                        X
                      
                      
                        2
                      
                    
                  
                
                +
                4
                δ
                
                  
                    
                      
                        n
                        
                          A
                        
                      
                      
                        M
                        
                          3
                          ,
                          B
                        
                      
                      −
                      
                        n
                        
                          B
                        
                      
                      
                        M
                        
                          3
                          ,
                          A
                        
                      
                    
                    
                      n
                      
                        X
                      
                    
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}M_{3,X}=M_{3,A}+M_{3,B}&{}+\delta ^{3}{\frac {n_{A}n_{B}(n_{A}-n_{B})}{n_{X}^{2}}}+3\delta {\frac {n_{A}M_{2,B}-n_{B}M_{2,A}}{n_{X}}}\\[6pt]M_{4,X}=M_{4,A}+M_{4,B}&{}+\delta ^{4}{\frac {n_{A}n_{B}\left(n_{A}^{2}-n_{A}n_{B}+n_{B}^{2}\right)}{n_{X}^{3}}}\\[6pt]&{}+6\delta ^{2}{\frac {n_{A}^{2}M_{2,B}+n_{B}^{2}M_{2,A}}{n_{X}^{2}}}+4\delta {\frac {n_{A}M_{3,B}-n_{B}M_{3,A}}{n_{X}}}\end{aligned}}}
  

Here the 
  
    
      
        
          M
          
            k
          
        
      
    
    {\displaystyle M_{k}}
  
 are again the sums of powers of differences from the mean 
  
    
      
        ∑
        (
        x
        −
        
          
            x
            ¯
          
        
        
          )
          
            k
          
        
      
    
    {\textstyle \sum (x-{\overline {x}})^{k}}
  
, giving

  
    
      
        
          
            
              
              
                
                  skewness
                
                =
                
                  g
                  
                    1
                  
                
                =
                
                  
                    
                      
                        
                          n
                        
                      
                      
                        M
                        
                          3
                        
                      
                    
                    
                      M
                      
                        2
                      
                      
                        3
                        
                          /
                        
                        2
                      
                    
                  
                
                ,
              
            
            
              
              
                
                  kurtosis
                
                =
                
                  g
                  
                    2
                  
                
                =
                
                  
                    
                      n
                      
                        M
                        
                          4
                        
                      
                    
                    
                      M
                      
                        2
                      
                      
                        2
                      
                    
                  
                
                −
                3.
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}&{\text{skewness}}=g_{1}={\frac {{\sqrt {n}}M_{3}}{M_{2}^{3/2}}},\\[4pt]&{\text{kurtosis}}=g_{2}={\frac {nM_{4}}{M_{2}^{2}}}-3.\end{aligned}}}
  

For the incremental case (i.e., 
  
    
      
        B
        =
        {
        x
        }
      
    
    {\displaystyle B=\{x\}}
  
), this simplifies to:

  
    
      
        
          
            
              
                δ
              
              
                
                =
                x
                −
                m
              
            
            
              
                
                  m
                  ′
                
              
              
                
                =
                m
                +
                
                  
                    δ
                    n
                  
                
              
            
            
              
                
                  M
                  
                    2
                  
                  ′
                
              
              
                
                =
                
                  M
                  
                    2
                  
                
                +
                
                  δ
                  
                    2
                  
                
                
                  
                    
                      n
                      −
                      1
                    
                    n
                  
                
              
            
            
              
                
                  M
                  
                    3
                  
                  ′
                
              
              
                
                =
                
                  M
                  
                    3
                  
                
                +
                
                  δ
                  
                    3
                  
                
                
                  
                    
                      (
                      n
                      −
                      1
                      )
                      (
                      n
                      −
                      2
                      )
                    
                    
                      n
                      
                        2
                      
                    
                  
                
                −
                
                  
                    
                      3
                      δ
                      
                        M
                        
                          2
                        
                      
                    
                    n
                  
                
              
            
            
              
                
                  M
                  
                    4
                  
                  ′
                
              
              
                
                =
                
                  M
                  
                    4
                  
                
                +
                
                  
                    
                      
                        δ
                        
                          4
                        
                      
                      (
                      n
                      −
                      1
                      )
                      (
                      
                        n
                        
                          2
                        
                      
                      −
                      3
                      n
                      +
                      3
                      )
                    
                    
                      n
                      
                        3
                      
                    
                  
                
                +
                
                  
                    
                      6
                      
                        δ
                        
                          2
                        
                      
                      
                        M
                        
                          2
                        
                      
                    
                    
                      n
                      
                        2
                      
                    
                  
                
                −
                
                  
                    
                      4
                      δ
                      
                        M
                        
                          3
                        
                      
                    
                    n
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\delta &=x-m\\[5pt]m'&=m+{\frac {\delta }{n}}\\[5pt]M_{2}'&=M_{2}+\delta ^{2}{\frac {n-1}{n}}\\[5pt]M_{3}'&=M_{3}+\delta ^{3}{\frac {(n-1)(n-2)}{n^{2}}}-{\frac {3\delta M_{2}}{n}}\\[5pt]M_{4}'&=M_{4}+{\frac {\delta ^{4}(n-1)(n^{2}-3n+3)}{n^{3}}}+{\frac {6\delta ^{2}M_{2}}{n^{2}}}-{\frac {4\delta M_{3}}{n}}\end{aligned}}}
  

By preserving the value 
  
    
      
        δ
        
          /
        
        n
      
    
    {\displaystyle \delta /n}
  
, only one division operation is needed and the higher-order statistics can thus be calculated for little incremental cost.
An example of the online algorithm for kurtosis implemented as described is:

Pébaÿ
further extends these results to arbitrary-order central moments, for the incremental and the pairwise cases, and subsequently Pébaÿ et al.
for weighted and compound moments. One can also find there similar formulas for covariance.
Choi and Sweetman
offer two alternative methods to compute the skewness and kurtosis, each of which can save substantial computer memory requirements and CPU time in certain applications. The first approach is to compute the statistical moments by separating the data into bins and then computing the moments from the geometry of the resulting histogram, which effectively becomes a one-pass algorithm for higher moments. One benefit is that the statistical moment calculations can be carried out to arbitrary accuracy such that the computations can be tuned to the precision of, e.g., the data storage format or the original measurement hardware.  A relative histogram of a random variable can be constructed in the conventional way: the range of potential values is divided into bins and the number of occurrences within each bin are counted and plotted such that the area of each rectangle equals the portion of the sample values within that bin:

  
    
      
        H
        (
        
          x
          
            k
          
        
        )
        =
        
          
            
              h
              (
              
                x
                
                  k
                
              
              )
            
            A
          
        
      
    
    {\displaystyle H(x_{k})={\frac {h(x_{k})}{A}}}
  

where 
  
    
      
        h
        (
        
          x
          
            k
          
        
        )
      
    
    {\displaystyle h(x_{k})}
  
 and 
  
    
      
        H
        (
        
          x
          
            k
          
        
        )
      
    
    {\displaystyle H(x_{k})}
  
 represent the frequency and the relative frequency at bin 
  
    
      
        
          x
          
            k
          
        
      
    
    {\displaystyle x_{k}}
  
 and 
  
    
      
        A
        =
        
          ∑
          
            k
            =
            1
          
          
            K
          
        
        h
        (
        
          x
          
            k
          
        
        )
        
        Δ
        
          x
          
            k
          
        
      
    
    {\textstyle A=\sum _{k=1}^{K}h(x_{k})\,\Delta x_{k}}
  
 is the total area of the histogram. After this normalization, the 
  
    
      
        n
      
    
    {\displaystyle n}
  
 raw moments and central moments of 
  
    
      
        x
        (
        t
        )
      
    
    {\displaystyle x(t)}
  
 can be calculated from the relative histogram:

  
    
      
        
          m
          
            n
          
          
            (
            h
            )
          
        
        =
        
          ∑
          
            k
            =
            1
          
          
            K
          
        
        
          x
          
            k
          
          
            n
          
        
        H
        (
        
          x
          
            k
          
        
        )
        
        Δ
        
          x
          
            k
          
        
        =
        
          
            1
            A
          
        
        
          ∑
          
            k
            =
            1
          
          
            K
          
        
        
          x
          
            k
          
          
            n
          
        
        h
        (
        
          x
          
            k
          
        
        )
        
        Δ
        
          x
          
            k
          
        
      
    
    {\displaystyle m_{n}^{(h)}=\sum _{k=1}^{K}x_{k}^{n}H(x_{k})\,\Delta x_{k}={\frac {1}{A}}\sum _{k=1}^{K}x_{k}^{n}h(x_{k})\,\Delta x_{k}}
  

  
    
      
        
          θ
          
            n
          
          
            (
            h
            )
          
        
        =
        
          ∑
          
            k
            =
            1
          
          
            K
          
        
        
          
            (
          
        
        
          x
          
            k
          
        
        −
        
          m
          
            1
          
          
            (
            h
            )
          
        
        
          
            
              )
            
          
          
            n
          
        
        
        H
        (
        
          x
          
            k
          
        
        )
        
        Δ
        
          x
          
            k
          
        
        =
        
          
            1
            A
          
        
        
          ∑
          
            k
            =
            1
          
          
            K
          
        
        
          
            (
          
        
        
          x
          
            k
          
        
        −
        
          m
          
            1
          
          
            (
            h
            )
          
        
        
          
            
              )
            
          
          
            n
          
        
        h
        (
        
          x
          
            k
          
        
        )
        
        Δ
        
          x
          
            k
          
        
      
    
    {\displaystyle \theta _{n}^{(h)}=\sum _{k=1}^{K}{\Big (}x_{k}-m_{1}^{(h)}{\Big )}^{n}\,H(x_{k})\,\Delta x_{k}={\frac {1}{A}}\sum _{k=1}^{K}{\Big (}x_{k}-m_{1}^{(h)}{\Big )}^{n}h(x_{k})\,\Delta x_{k}}
  

where the superscript 
  
    
      
        
          
          
            (
            h
            )
          
        
      
    
    {\displaystyle ^{(h)}}
  
 indicates the moments are calculated from the histogram. For constant bin width 
  
    
      
        Δ
        
          x
          
            k
          
        
        =
        Δ
        x
      
    
    {\displaystyle \Delta x_{k}=\Delta x}
  
 these two expressions can be simplified using 
  
    
      
        I
        =
        A
        
          /
        
        Δ
        x
      
    
    {\displaystyle I=A/\Delta x}
  
:

  
    
      
        
          m
          
            n
          
          
            (
            h
            )
          
        
        =
        
          
            1
            I
          
        
        
          ∑
          
            k
            =
            1
          
          
            K
          
        
        
          x
          
            k
          
          
            n
          
        
        
        h
        (
        
          x
          
            k
          
        
        )
      
    
    {\displaystyle m_{n}^{(h)}={\frac {1}{I}}\sum _{k=1}^{K}x_{k}^{n}\,h(x_{k})}
  

  
    
      
        
          θ
          
            n
          
          
            (
            h
            )
          
        
        =
        
          
            1
            I
          
        
        
          ∑
          
            k
            =
            1
          
          
            K
          
        
        
          
            (
          
        
        
          x
          
            k
          
        
        −
        
          m
          
            1
          
          
            (
            h
            )
          
        
        
          
            
              )
            
          
          
            n
          
        
        h
        (
        
          x
          
            k
          
        
        )
      
    
    {\displaystyle \theta _{n}^{(h)}={\frac {1}{I}}\sum _{k=1}^{K}{\Big (}x_{k}-m_{1}^{(h)}{\Big )}^{n}h(x_{k})}
  

The second approach from Choi and Sweetman is an analytical methodology to combine statistical moments from individual segments of a time-history such that the resulting overall moments are those of the complete time-history. This methodology could be used for parallel computation of statistical moments with subsequent combination of those moments, or for combination of statistical moments computed at sequential times.
If 
  
    
      
        Q
      
    
    {\displaystyle Q}
  
 sets of statistical moments are known:

  
    
      
        (
        
          γ
          
            0
            ,
            q
          
        
        ,
        
          μ
          
            q
          
        
        ,
        
          σ
          
            q
          
          
            2
          
        
        ,
        
          α
          
            3
            ,
            q
          
        
        ,
        
          α
          
            4
            ,
            q
          
        
        )
        
      
    
    {\displaystyle (\gamma _{0,q},\mu _{q},\sigma _{q}^{2},\alpha _{3,q},\alpha _{4,q})\quad }
  
 for 
  
    
      
        q
        =
        1
        ,
        2
        ,
        …
        ,
        Q
      
    
    {\displaystyle q=1,2,\ldots ,Q}
  
, then each 
  
    
      
        
          γ
          
            n
          
        
      
    
    {\displaystyle \gamma _{n}}
  
 can
be expressed in terms of the equivalent 
  
    
      
        n
      
    
    {\displaystyle n}
  
 raw moments:

  
    
      
        
          γ
          
            n
            ,
            q
          
        
        =
        
          m
          
            n
            ,
            q
          
        
        
          γ
          
            0
            ,
            q
          
        
        
        
        
          
            for
          
        
        
        n
        =
        1
        ,
        2
        ,
        3
        ,
        4
        
        
           and 
        
        
        q
        =
        1
        ,
        2
        ,
        …
        ,
        Q
      
    
    {\displaystyle \gamma _{n,q}=m_{n,q}\gamma _{0,q}\qquad \quad {\textrm {for}}\quad n=1,2,3,4\quad {\text{ and }}\quad q=1,2,\dots ,Q}
  

where 
  
    
      
        
          γ
          
            0
            ,
            q
          
        
      
    
    {\displaystyle \gamma _{0,q}}
  
 is generally taken to be the duration of the 
  
    
      
        
          q
          
            t
            h
          
        
      
    
    {\displaystyle q^{th}}
  
 time-history, or the number of points if 
  
    
      
        Δ
        t
      
    
    {\displaystyle \Delta t}
  
 is constant.
The benefit of expressing the statistical moments in terms of 
  
    
      
        γ
      
    
    {\displaystyle \gamma }
  
 is that the 
  
    
      
        Q
      
    
    {\displaystyle Q}
  
 sets can be combined by addition, and there is no upper limit on the value of 
  
    
      
        Q
      
    
    {\displaystyle Q}
  
.

  
    
      
        
          γ
          
            n
            ,
            c
          
        
        =
        
          ∑
          
            q
            =
            1
          
          
            Q
          
        
        
          γ
          
            n
            ,
            q
          
        
        
        
        
          for 
        
        n
        =
        0
        ,
        1
        ,
        2
        ,
        3
        ,
        4
      
    
    {\displaystyle \gamma _{n,c}=\sum _{q=1}^{Q}\gamma _{n,q}\quad \quad {\text{for }}n=0,1,2,3,4}
  

where the subscript 
  
    
      
        
          
          
            c
          
        
      
    
    {\displaystyle _{c}}
  
 represents the concatenated time-history or combined 
  
    
      
        γ
      
    
    {\displaystyle \gamma }
  
. These combined values of 
  
    
      
        γ
      
    
    {\displaystyle \gamma }
  
 can then be inversely transformed into raw moments representing the complete concatenated time-history

  
    
      
        
          m
          
            n
            ,
            c
          
        
        =
        
          
            
              γ
              
                n
                ,
                c
              
            
            
              γ
              
                0
                ,
                c
              
            
          
        
        
        
          for 
        
        n
        =
        1
        ,
        2
        ,
        3
        ,
        4
      
    
    {\displaystyle m_{n,c}={\frac {\gamma _{n,c}}{\gamma _{0,c}}}\quad {\text{for }}n=1,2,3,4}
  

Known relationships between the raw moments (
  
    
      
        
          m
          
            n
          
        
      
    
    {\displaystyle m_{n}}
  
) and the central moments (
  
    
      
        
          θ
          
            n
          
        
        =
        E
        ⁡
        [
        (
        x
        −
        μ
        
          )
          
            n
          
        
        ]
        )
      
    
    {\displaystyle \theta _{n}=\operatorname {E} [(x-\mu )^{n}])}
  
)
are then used to compute the central moments of the concatenated time-history.  Finally, the statistical moments of the concatenated history are computed from the central moments:

  
    
      
        
          μ
          
            c
          
        
        =
        
          m
          
            1
            ,
            c
          
        
        
        
          σ
          
            c
          
          
            2
          
        
        =
        
          θ
          
            2
            ,
            c
          
        
        
        
          α
          
            3
            ,
            c
          
        
        =
        
          
            
              θ
              
                3
                ,
                c
              
            
            
              σ
              
                c
              
              
                3
              
            
          
        
        
        
          α
          
            4
            ,
            c
          
        
        =
        
          
            
              θ
              
                4
                ,
                c
              
            
            
              σ
              
                c
              
              
                4
              
            
          
        
        −
        3
      
    
    {\displaystyle \mu _{c}=m_{1,c}\qquad \sigma _{c}^{2}=\theta _{2,c}\qquad \alpha _{3,c}={\frac {\theta _{3,c}}{\sigma _{c}^{3}}}\qquad \alpha _{4,c}={\frac {\theta _{4,c}}{\sigma _{c}^{4}}}-3}

Covariance
Very similar algorithms can be used to compute the covariance.

Naïve algorithm
The naïve algorithm is

  
    
      
        Cov
        ⁡
        (
        X
        ,
        Y
        )
        =
        
          
            
              
                ∑
                
                  i
                  =
                  1
                
                
                  n
                
              
              
                x
                
                  i
                
              
              
                y
                
                  i
                
              
              −
              (
              
                ∑
                
                  i
                  =
                  1
                
                
                  n
                
              
              
                x
                
                  i
                
              
              )
              (
              
                ∑
                
                  i
                  =
                  1
                
                
                  n
                
              
              
                y
                
                  i
                
              
              )
              
                /
              
              n
            
            n
          
        
        .
      
    
    {\displaystyle \operatorname {Cov} (X,Y)={\frac {\sum _{i=1}^{n}x_{i}y_{i}-(\sum _{i=1}^{n}x_{i})(\sum _{i=1}^{n}y_{i})/n}{n}}.}
  

For the algorithm above, one could use the following Python code:

With estimate of the mean
As for the variance, the covariance of two random variables is also shift-invariant, so given any two constant values 
  
    
      
        
          k
          
            x
          
        
      
    
    {\displaystyle k_{x}}
  
 and 
  
    
      
        
          k
          
            y
          
        
        ,
      
    
    {\displaystyle k_{y},}
  
 it can be written:

  
    
      
        Cov
        ⁡
        (
        X
        ,
        Y
        )
        =
        Cov
        ⁡
        (
        X
        −
        
          k
          
            x
          
        
        ,
        Y
        −
        
          k
          
            y
          
        
        )
        =
        
          
            
              
                
                  ∑
                  
                    i
                    =
                    1
                  
                  
                    n
                  
                
                (
                
                  x
                  
                    i
                  
                
                −
                
                  k
                  
                    x
                  
                
                )
                (
                
                  y
                  
                    i
                  
                
                −
                
                  k
                  
                    y
                  
                
                )
                −
                (
                
                  ∑
                  
                    i
                    =
                    1
                  
                  
                    n
                  
                
                (
                
                  x
                  
                    i
                  
                
                −
                
                  k
                  
                    x
                  
                
                )
                )
                (
                
                  ∑
                  
                    i
                    =
                    1
                  
                  
                    n
                  
                
                (
                
                  y
                  
                    i
                  
                
                −
                
                  k
                  
                    y
                  
                
                )
                )
                
                  /
                
                n
              
              n
            
          
        
        .
      
    
    {\displaystyle \operatorname {Cov} (X,Y)=\operatorname {Cov} (X-k_{x},Y-k_{y})={\dfrac {\sum _{i=1}^{n}(x_{i}-k_{x})(y_{i}-k_{y})-(\sum _{i=1}^{n}(x_{i}-k_{x}))(\sum _{i=1}^{n}(y_{i}-k_{y}))/n}{n}}.}
  

and again choosing a value inside the range of values will stabilize the formula against catastrophic cancellation as well as make it more robust against big sums. Taking the first value of each data set, the algorithm can be written as:

Two-pass
The two-pass algorithm first computes the sample means, and then the covariance:

  
    
      
        
          
            
              x
              ¯
            
          
        
        =
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        
          x
          
            i
          
        
        
          /
        
        n
      
    
    {\displaystyle {\bar {x}}=\sum _{i=1}^{n}x_{i}/n}
  

  
    
      
        
          
            
              y
              ¯
            
          
        
        =
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        
          y
          
            i
          
        
        
          /
        
        n
      
    
    {\displaystyle {\bar {y}}=\sum _{i=1}^{n}y_{i}/n}
  

  
    
      
        Cov
        ⁡
        (
        X
        ,
        Y
        )
        =
        
          
            
              
                ∑
                
                  i
                  =
                  1
                
                
                  n
                
              
              (
              
                x
                
                  i
                
              
              −
              
                
                  
                    x
                    ¯
                  
                
              
              )
              (
              
                y
                
                  i
                
              
              −
              
                
                  
                    y
                    ¯
                  
                
              
              )
            
            n
          
        
        .
      
    
    {\displaystyle \operatorname {Cov} (X,Y)={\frac {\sum _{i=1}^{n}(x_{i}-{\bar {x}})(y_{i}-{\bar {y}})}{n}}.}
  

The two-pass algorithm may be written as:

A slightly more accurate compensated version performs the full naive algorithm on the residuals.  The final sums 
  
    
      
        
          ∑
          
            i
          
        
        
          x
          
            i
          
        
      
    
    {\textstyle \sum _{i}x_{i}}
  
 and 
  
    
      
        
          ∑
          
            i
          
        
        
          y
          
            i
          
        
      
    
    {\textstyle \sum _{i}y_{i}}
  
 should be zero, but the second pass compensates for any small error.

Online
A stable one-pass algorithm exists, similar to the online algorithm for computing the variance, that computes co-moment 
  
    
      
        
          C
          
            n
          
        
        =
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        (
        
          x
          
            i
          
        
        −
        
          
            
              
                x
                ¯
              
            
          
          
            n
          
        
        )
        (
        
          y
          
            i
          
        
        −
        
          
            
              
                y
                ¯
              
            
          
          
            n
          
        
        )
      
    
    {\textstyle C_{n}=\sum _{i=1}^{n}(x_{i}-{\bar {x}}_{n})(y_{i}-{\bar {y}}_{n})}
  
:

  
    
      
        
          
            
              
                
                  
                    
                      
                        x
                        ¯
                      
                    
                  
                  
                    n
                  
                
              
              
                
                =
                
                  
                    
                      
                        x
                        ¯
                      
                    
                  
                  
                    n
                    −
                    1
                  
                
              
              
                
                +
                
              
              
                
                  
                    
                      
                        x
                        
                          n
                        
                      
                      −
                      
                        
                          
                            
                              x
                              ¯
                            
                          
                        
                        
                          n
                          −
                          1
                        
                      
                    
                    n
                  
                
              
            
            
              
                
                  
                    
                      
                        y
                        ¯
                      
                    
                  
                  
                    n
                  
                
              
              
                
                =
                
                  
                    
                      
                        y
                        ¯
                      
                    
                  
                  
                    n
                    −
                    1
                  
                
              
              
                
                +
                
              
              
                
                  
                    
                      
                        y
                        
                          n
                        
                      
                      −
                      
                        
                          
                            
                              y
                              ¯
                            
                          
                        
                        
                          n
                          −
                          1
                        
                      
                    
                    n
                  
                
              
            
            
              
                
                  C
                  
                    n
                  
                
              
              
                
                =
                
                  C
                  
                    n
                    −
                    1
                  
                
              
              
                
                +
                
              
              
                
                (
                
                  x
                  
                    n
                  
                
                −
                
                  
                    
                      
                        x
                        ¯
                      
                    
                  
                  
                    n
                  
                
                )
                (
                
                  y
                  
                    n
                  
                
                −
                
                  
                    
                      
                        y
                        ¯
                      
                    
                  
                  
                    n
                    −
                    1
                  
                
                )
              
            
            
              
              
                
                =
                
                  C
                  
                    n
                    −
                    1
                  
                
              
              
                
                +
                
              
              
                
                (
                
                  x
                  
                    n
                  
                
                −
                
                  
                    
                      
                        x
                        ¯
                      
                    
                  
                  
                    n
                    −
                    1
                  
                
                )
                (
                
                  y
                  
                    n
                  
                
                −
                
                  
                    
                      
                        y
                        ¯
                      
                    
                  
                  
                    n
                  
                
                )
              
            
          
        
      
    
    {\displaystyle {\begin{alignedat}{2}{\bar {x}}_{n}&={\bar {x}}_{n-1}&\,+\,&{\frac {x_{n}-{\bar {x}}_{n-1}}{n}}\\[5pt]{\bar {y}}_{n}&={\bar {y}}_{n-1}&\,+\,&{\frac {y_{n}-{\bar {y}}_{n-1}}{n}}\\[5pt]C_{n}&=C_{n-1}&\,+\,&(x_{n}-{\bar {x}}_{n})(y_{n}-{\bar {y}}_{n-1})\\[5pt]&=C_{n-1}&\,+\,&(x_{n}-{\bar {x}}_{n-1})(y_{n}-{\bar {y}}_{n})\end{alignedat}}}
  

The apparent asymmetry in that last equation is due to the fact that 
  
    
      
        (
        
          x
          
            n
          
        
        −
        
          
            
              
                x
                ¯
              
            
          
          
            n
          
        
        )
        =
        
          
            
              n
              −
              1
            
            n
          
        
        (
        
          x
          
            n
          
        
        −
        
          
            
              
                x
                ¯
              
            
          
          
            n
            −
            1
          
        
        )
      
    
    {\textstyle (x_{n}-{\bar {x}}_{n})={\frac {n-1}{n}}(x_{n}-{\bar {x}}_{n-1})}
  
, so both update terms are equal to 
  
    
      
        
          
            
              n
              −
              1
            
            n
          
        
        (
        
          x
          
            n
          
        
        −
        
          
            
              
                x
                ¯
              
            
          
          
            n
            −
            1
          
        
        )
        (
        
          y
          
            n
          
        
        −
        
          
            
              
                y
                ¯
              
            
          
          
            n
            −
            1
          
        
        )
      
    
    {\textstyle {\frac {n-1}{n}}(x_{n}-{\bar {x}}_{n-1})(y_{n}-{\bar {y}}_{n-1})}
  
.  Even greater accuracy can be achieved by first computing the means, then using the stable one-pass algorithm on the residuals.
Thus the covariance can be computed as

  
    
      
        
          
            
              
                
                  Cov
                  
                    N
                  
                
                ⁡
                (
                X
                ,
                Y
                )
                =
                
                  
                    
                      C
                      
                        N
                      
                    
                    N
                  
                
              
              
                
                =
                
                  
                    
                      
                        Cov
                        
                          N
                          −
                          1
                        
                      
                      ⁡
                      (
                      X
                      ,
                      Y
                      )
                      ⋅
                      (
                      N
                      −
                      1
                      )
                      +
                      (
                      
                        x
                        
                          n
                        
                      
                      −
                      
                        
                          
                            
                              x
                              ¯
                            
                          
                        
                        
                          n
                        
                      
                      )
                      (
                      
                        y
                        
                          n
                        
                      
                      −
                      
                        
                          
                            
                              y
                              ¯
                            
                          
                        
                        
                          n
                          −
                          1
                        
                      
                      )
                    
                    N
                  
                
              
            
            
              
              
                
                =
                
                  
                    
                      
                        Cov
                        
                          N
                          −
                          1
                        
                      
                      ⁡
                      (
                      X
                      ,
                      Y
                      )
                      ⋅
                      (
                      N
                      −
                      1
                      )
                      +
                      (
                      
                        x
                        
                          n
                        
                      
                      −
                      
                        
                          
                            
                              x
                              ¯
                            
                          
                        
                        
                          n
                          −
                          1
                        
                      
                      )
                      (
                      
                        y
                        
                          n
                        
                      
                      −
                      
                        
                          
                            
                              y
                              ¯
                            
                          
                        
                        
                          n
                        
                      
                      )
                    
                    N
                  
                
              
            
            
              
              
                
                =
                
                  
                    
                      
                        Cov
                        
                          N
                          −
                          1
                        
                      
                      ⁡
                      (
                      X
                      ,
                      Y
                      )
                      ⋅
                      (
                      N
                      −
                      1
                      )
                      +
                      
                        
                          
                            N
                            −
                            1
                          
                          N
                        
                      
                      (
                      
                        x
                        
                          n
                        
                      
                      −
                      
                        
                          
                            
                              x
                              ¯
                            
                          
                        
                        
                          n
                          −
                          1
                        
                      
                      )
                      (
                      
                        y
                        
                          n
                        
                      
                      −
                      
                        
                          
                            
                              y
                              ¯
                            
                          
                        
                        
                          n
                          −
                          1
                        
                      
                      )
                    
                    N
                  
                
              
            
            
              
              
                
                =
                
                  
                    
                      
                        Cov
                        
                          N
                          −
                          1
                        
                      
                      ⁡
                      (
                      X
                      ,
                      Y
                      )
                      ⋅
                      (
                      N
                      −
                      1
                      )
                      +
                      
                        
                          N
                          
                            N
                            −
                            1
                          
                        
                      
                      (
                      
                        x
                        
                          n
                        
                      
                      −
                      
                        
                          
                            
                              x
                              ¯
                            
                          
                        
                        
                          n
                        
                      
                      )
                      (
                      
                        y
                        
                          n
                        
                      
                      −
                      
                        
                          
                            
                              y
                              ¯
                            
                          
                        
                        
                          n
                        
                      
                      )
                    
                    N
                  
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\operatorname {Cov} _{N}(X,Y)={\frac {C_{N}}{N}}&={\frac {\operatorname {Cov} _{N-1}(X,Y)\cdot (N-1)+(x_{n}-{\bar {x}}_{n})(y_{n}-{\bar {y}}_{n-1})}{N}}\\&={\frac {\operatorname {Cov} _{N-1}(X,Y)\cdot (N-1)+(x_{n}-{\bar {x}}_{n-1})(y_{n}-{\bar {y}}_{n})}{N}}\\&={\frac {\operatorname {Cov} _{N-1}(X,Y)\cdot (N-1)+{\frac {N-1}{N}}(x_{n}-{\bar {x}}_{n-1})(y_{n}-{\bar {y}}_{n-1})}{N}}\\&={\frac {\operatorname {Cov} _{N-1}(X,Y)\cdot (N-1)+{\frac {N}{N-1}}(x_{n}-{\bar {x}}_{n})(y_{n}-{\bar {y}}_{n})}{N}}.\end{aligned}}}
  

A small modification can also be made to compute the weighted covariance:

Likewise, there is a formula for combining the covariances of two sets that can be used to parallelize the computation:

  
    
      
        
          C
          
            X
          
        
        =
        
          C
          
            A
          
        
        +
        
          C
          
            B
          
        
        +
        (
        
          
            
              
                x
                ¯
              
            
          
          
            A
          
        
        −
        
          
            
              
                x
                ¯
              
            
          
          
            B
          
        
        )
        (
        
          
            
              
                y
                ¯
              
            
          
          
            A
          
        
        −
        
          
            
              
                y
                ¯
              
            
          
          
            B
          
        
        )
        ⋅
        
          
            
              
                n
                
                  A
                
              
              
                n
                
                  B
                
              
            
            
              n
              
                X
              
            
          
        
        .
      
    
    {\displaystyle C_{X}=C_{A}+C_{B}+({\bar {x}}_{A}-{\bar {x}}_{B})({\bar {y}}_{A}-{\bar {y}}_{B})\cdot {\frac {n_{A}n_{B}}{n_{X}}}.}

Weighted batched version
A version of the weighted online algorithm that does batched updated also exists: let 
  
    
      
        
          w
          
            1
          
        
        ,
        …
        
          w
          
            N
          
        
      
    
    {\displaystyle w_{1},\dots w_{N}}
  
 denote the weights, and write

  
    
      
        
          
            
              
                
                  
                    
                      
                        x
                        ¯
                      
                    
                  
                  
                    n
                    +
                    k
                  
                
              
              
                
                =
                
                  
                    
                      
                        x
                        ¯
                      
                    
                  
                  
                    n
                  
                
              
              
                
                +
                
              
              
                
                  
                    
                      
                        ∑
                        
                          i
                          =
                          n
                          +
                          1
                        
                        
                          n
                          +
                          k
                        
                      
                      
                        w
                        
                          i
                        
                      
                      (
                      
                        x
                        
                          i
                        
                      
                      −
                      
                        
                          
                            
                              x
                              ¯
                            
                          
                        
                        
                          n
                        
                      
                      )
                    
                    
                      
                        ∑
                        
                          i
                          =
                          1
                        
                        
                          n
                          +
                          k
                        
                      
                      
                        w
                        
                          i
                        
                      
                    
                  
                
              
            
            
              
                
                  
                    
                      
                        y
                        ¯
                      
                    
                  
                  
                    n
                    +
                    k
                  
                
              
              
                
                =
                
                  
                    
                      
                        y
                        ¯
                      
                    
                  
                  
                    n
                  
                
              
              
                
                +
                
              
              
                
                  
                    
                      
                        ∑
                        
                          i
                          =
                          n
                          +
                          1
                        
                        
                          n
                          +
                          k
                        
                      
                      
                        w
                        
                          i
                        
                      
                      (
                      
                        y
                        
                          i
                        
                      
                      −
                      
                        
                          
                            
                              y
                              ¯
                            
                          
                        
                        
                          n
                        
                      
                      )
                    
                    
                      
                        ∑
                        
                          i
                          =
                          1
                        
                        
                          n
                          +
                          k
                        
                      
                      
                        w
                        
                          i
                        
                      
                    
                  
                
              
            
            
              
                
                  C
                  
                    n
                    +
                    k
                  
                
              
              
                
                =
                
                  C
                  
                    n
                  
                
              
              
                
                +
                
              
              
                
                
                  ∑
                  
                    i
                    =
                    n
                    +
                    1
                  
                  
                    n
                    +
                    k
                  
                
                
                  w
                  
                    i
                  
                
                (
                
                  x
                  
                    i
                  
                
                −
                
                  
                    
                      
                        x
                        ¯
                      
                    
                  
                  
                    n
                    +
                    k
                  
                
                )
                (
                
                  y
                  
                    i
                  
                
                −
                
                  
                    
                      
                        y
                        ¯
                      
                    
                  
                  
                    n
                  
                
                )
              
            
            
              
              
                
                =
                
                  C
                  
                    n
                  
                
              
              
                
                +
                
              
              
                
                
                  ∑
                  
                    i
                    =
                    n
                    +
                    1
                  
                  
                    n
                    +
                    k
                  
                
                
                  w
                  
                    i
                  
                
                (
                
                  x
                  
                    i
                  
                
                −
                
                  
                    
                      
                        x
                        ¯
                      
                    
                  
                  
                    n
                  
                
                )
                (
                
                  y
                  
                    i
                  
                
                −
                
                  
                    
                      
                        y
                        ¯
                      
                    
                  
                  
                    n
                    +
                    k
                  
                
                )
              
            
          
        
      
    
    {\displaystyle {\begin{alignedat}{2}{\bar {x}}_{n+k}&={\bar {x}}_{n}&\,+\,&{\frac {\sum _{i=n+1}^{n+k}w_{i}(x_{i}-{\bar {x}}_{n})}{\sum _{i=1}^{n+k}w_{i}}}\\{\bar {y}}_{n+k}&={\bar {y}}_{n}&\,+\,&{\frac {\sum _{i=n+1}^{n+k}w_{i}(y_{i}-{\bar {y}}_{n})}{\sum _{i=1}^{n+k}w_{i}}}\\C_{n+k}&=C_{n}&\,+\,&\sum _{i=n+1}^{n+k}w_{i}(x_{i}-{\bar {x}}_{n+k})(y_{i}-{\bar {y}}_{n})\\&=C_{n}&\,+\,&\sum _{i=n+1}^{n+k}w_{i}(x_{i}-{\bar {x}}_{n})(y_{i}-{\bar {y}}_{n+k})\\\end{alignedat}}}
  

The covariance can then be computed as

  
    
      
        
          Cov
          
            N
          
        
        ⁡
        (
        X
        ,
        Y
        )
        =
        
          
            
              C
              
                N
              
            
            
              
                ∑
                
                  i
                  =
                  1
                
                
                  N
                
              
              
                w
                
                  i
                
              
            
          
        
      
    
    {\displaystyle \operatorname {Cov} _{N}(X,Y)={\frac {C_{N}}{\sum _{i=1}^{N}w_{i}}}}

See also
Kahan summation algorithm
Squared deviations from the mean
Yamartino method

References
External links
Weisstein, Eric W. "Sample Variance Computation". MathWorld.

## Archive Info
- **Archived on:** 2024-12-15 21:03:23 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 104325 bytes
- **Word Count:** 4287 words
