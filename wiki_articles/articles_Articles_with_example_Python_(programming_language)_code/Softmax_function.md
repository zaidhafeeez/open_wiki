# Softmax function

## Article Metadata

- **Last Updated:** 2024-12-14T19:45:13.078112+00:00
- **Original Article:** [Softmax function](https://en.wikipedia.org/wiki/Softmax_function)
- **Language:** en
- **Page ID:** 6152185

## Summary

The softmax function, also known as softargmax: 184  or normalized exponential function,: 198  converts a vector of K real numbers into a probability distribution of K possible outcomes. It is a generalization of the logistic function to multiple dimensions, and is used in multinomial logistic regression. The softmax function is often used as the last activation function of a neural network to normalize the output of a network to a probability distribution over predicted output classes.

## Categories

- Category:All articles with unsourced statements
- Category:Articles with example Julia code
- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with short description
- Category:Articles with unsourced statements from March 2024
- Category:Artificial neural networks
- Category:Computational neuroscience
- Category:Exponentials
- Category:Functions and mappings
- Category:Logistic regression
- Category:Short description is different from Wikidata

## Table of Contents

- Definition
- Interpretations
- Applications
- Computational complexity and remedies
- Mathematical properties
- History
- Example
- Alternatives
- See also
- Notes

## Content

The softmax function, also known as softargmax: 184  or normalized exponential function,: 198  converts a vector of K real numbers into a probability distribution of K possible outcomes. It is a generalization of the logistic function to multiple dimensions, and is used in multinomial logistic regression. The softmax function is often used as the last activation function of a neural network to normalize the output of a network to a probability distribution over predicted output classes.

Definition
The softmax function takes as input a vector z of K real numbers, and normalizes it into a probability distribution consisting of K probabilities proportional to the exponentials of the input numbers. That is, prior to applying softmax, some vector components could be negative, or greater than one; and might not sum to 1; but after applying softmax, each component will be in the interval 
  
    
      
        (
        0
        ,
        1
        )
      
    
    {\displaystyle (0,1)}
  
, and the components will add up to 1, so that they can be interpreted as probabilities. Furthermore, the larger input components will correspond to larger probabilities. 
Formally, the standard (unit) softmax function 
  
    
      
        σ
        :
        
          
            R
          
          
            K
          
        
        →
        (
        0
        ,
        1
        
          )
          
            K
          
        
      
    
    {\displaystyle \sigma \colon \mathbb {R} ^{K}\to (0,1)^{K}}
  
, where 
  
    
      
        K
        >
        1
      
    
    {\displaystyle K>1}
  
, takes a vector 
  
    
      
        
          z
        
        =
        (
        
          z
          
            1
          
        
        ,
        …
        ,
        
          z
          
            K
          
        
        )
        ∈
        
          
            R
          
          
            K
          
        
      
    
    {\displaystyle \mathbf {z} =(z_{1},\dotsc ,z_{K})\in \mathbb {R} ^{K}}
  
 and computes each component of vector 
  
    
      
        σ
        (
        
          z
        
        )
        ∈
        (
        0
        ,
        1
        
          )
          
            K
          
        
      
    
    {\displaystyle \sigma (\mathbf {z} )\in (0,1)^{K}}
  
 with

  
    
      
        σ
        (
        
          z
        
        
          )
          
            i
          
        
        =
        
          
            
              e
              
                
                  z
                  
                    i
                  
                
              
            
            
              
                ∑
                
                  j
                  =
                  1
                
                
                  K
                
              
              
                e
                
                  
                    z
                    
                      j
                    
                  
                
              
            
          
        
        
        .
      
    
    {\displaystyle \sigma (\mathbf {z} )_{i}={\frac {e^{z_{i}}}{\sum _{j=1}^{K}e^{z_{j}}}}\,.}
  

In words, the softmax applies the standard exponential function to each element 
  
    
      
        
          z
          
            i
          
        
      
    
    {\displaystyle z_{i}}
  
 of the input vector 
  
    
      
        
          z
        
      
    
    {\displaystyle \mathbf {z} }
  
 (consisting of 
  
    
      
        K
      
    
    {\displaystyle K}
  
 real numbers), and normalizes these values by dividing by the sum of all these exponentials. The normalization ensures that the sum of the components of the output vector 
  
    
      
        σ
        (
        
          z
        
        )
      
    
    {\displaystyle \sigma (\mathbf {z} )}
  
 is 1. The term "softmax" derives from the amplifying effects of the exponential on any maxima in the input vector. For example, the standard softmax of 
  
    
      
        (
        1
        ,
        2
        ,
        8
        )
      
    
    {\displaystyle (1,2,8)}
  
 is approximately 
  
    
      
        (
        0.001
        ,
        0.002
        ,
        0.997
        )
      
    
    {\displaystyle (0.001,0.002,0.997)}
  
, which amounts to assigning almost all of the total unit weight in the result to the position of the vector's maximal element (of 8).
In general, instead of e a different base b > 0 can be used.  As above, if b > 1 then larger input components will result in larger output probabilities, and increasing the value of b will create probability distributions that are more concentrated around the positions of the largest input values. Conversely, if 0 < b < 1 then smaller input components will result in larger output probabilities, and decreasing the value of b will create probability distributions that are more concentrated around the positions of the smallest input values. Writing 
  
    
      
        b
        =
        
          e
          
            β
          
        
      
    
    {\displaystyle b=e^{\beta }}
  
 or 
  
    
      
        b
        =
        
          e
          
            −
            β
          
        
      
    
    {\displaystyle b=e^{-\beta }}
  
 (for real β) yields the expressions:

  
    
      
        σ
        (
        
          z
        
        
          )
          
            i
          
        
        =
        
          
            
              e
              
                β
                
                  z
                  
                    i
                  
                
              
            
            
              
                ∑
                
                  j
                  =
                  1
                
                
                  K
                
              
              
                e
                
                  β
                  
                    z
                    
                      j
                    
                  
                
              
            
          
        
        
           or 
        
        σ
        (
        
          z
        
        
          )
          
            i
          
        
        =
        
          
            
              e
              
                −
                β
                
                  z
                  
                    i
                  
                
              
            
            
              
                ∑
                
                  j
                  =
                  1
                
                
                  K
                
              
              
                e
                
                  −
                  β
                  
                    z
                    
                      j
                    
                  
                
              
            
          
        
        
           for 
        
        i
        =
        1
        ,
        …
        ,
        K
        .
      
    
    {\displaystyle \sigma (\mathbf {z} )_{i}={\frac {e^{\beta z_{i}}}{\sum _{j=1}^{K}e^{\beta z_{j}}}}{\text{ or }}\sigma (\mathbf {z} )_{i}={\frac {e^{-\beta z_{i}}}{\sum _{j=1}^{K}e^{-\beta z_{j}}}}{\text{ for }}i=1,\dotsc ,K.}
  

A value proportional to the reciprocal of β is sometimes referred to as the temperature: 
  
    
      
        β
        =
        1
        
          /
        
        k
        T
      
    
    {\textstyle \beta =1/kT}
  
, where k is typically 1 or the Boltzmann constant and T is the temperature. A higher temperature results in a more uniform output distribution (i.e. with higher entropy; it is "more random"), while a lower temperature results in a sharper output distribution, with one value dominating.
In some fields, the base is fixed, corresponding to a fixed scale, while in others the parameter β (or T) is varied.

Interpretations
Smooth arg max
The Softmax function is a smooth approximation to the arg max function: the function whose value is the index of a vector's largest element. The name "softmax" may be misleading. Softmax is not a smooth maximum (that is, a smooth approximation to the maximum function). The term "softmax" is also used for the closely related LogSumExp function, which is a smooth maximum. For this reason, some prefer the more accurate term "softargmax", though the term "softmax" is conventional in machine learning. This section uses the term "softargmax" for clarity.
Formally, instead of considering the arg max as a function with categorical output 
  
    
      
        1
        ,
        …
        ,
        n
      
    
    {\displaystyle 1,\dots ,n}
  
 (corresponding to the index), consider the arg max function with one-hot representation of the output (assuming there is a unique maximum arg):

  
    
      
        
          a
          r
          g
          
          m
          a
          x
        
        ⁡
        (
        
          z
          
            1
          
        
        ,
        
        …
        ,
        
        
          z
          
            n
          
        
        )
        =
        (
        
          y
          
            1
          
        
        ,
        
        …
        ,
        
        
          y
          
            n
          
        
        )
        =
        (
        0
        ,
        
        …
        ,
        
        0
        ,
        
        1
        ,
        
        0
        ,
        
        …
        ,
        
        0
        )
        ,
      
    
    {\displaystyle \operatorname {arg\,max} (z_{1},\,\dots ,\,z_{n})=(y_{1},\,\dots ,\,y_{n})=(0,\,\dots ,\,0,\,1,\,0,\,\dots ,\,0),}
  

where the output coordinate 
  
    
      
        
          y
          
            i
          
        
        =
        1
      
    
    {\displaystyle y_{i}=1}
  
 if and only if 
  
    
      
        i
      
    
    {\displaystyle i}
  
 is the arg max of 
  
    
      
        (
        
          z
          
            1
          
        
        ,
        …
        ,
        
          z
          
            n
          
        
        )
      
    
    {\displaystyle (z_{1},\dots ,z_{n})}
  
, meaning 
  
    
      
        
          z
          
            i
          
        
      
    
    {\displaystyle z_{i}}
  
 is the unique maximum value of 
  
    
      
        (
        
          z
          
            1
          
        
        ,
        
        …
        ,
        
        
          z
          
            n
          
        
        )
      
    
    {\displaystyle (z_{1},\,\dots ,\,z_{n})}
  
. For example, in this encoding 
  
    
      
        
          a
          r
          g
          
          m
          a
          x
        
        ⁡
        (
        1
        ,
        5
        ,
        10
        )
        =
        (
        0
        ,
        0
        ,
        1
        )
        ,
      
    
    {\displaystyle \operatorname {arg\,max} (1,5,10)=(0,0,1),}
  
 since the third argument is the maximum.
This can be generalized to multiple arg max values (multiple equal 
  
    
      
        
          z
          
            i
          
        
      
    
    {\displaystyle z_{i}}
  
 being the maximum) by dividing the 1 between all max args; formally 1/k where k is the number of arguments assuming the maximum. For example, 
  
    
      
        
          a
          r
          g
          
          m
          a
          x
        
        ⁡
        (
        1
        ,
        
        5
        ,
        
        5
        )
        =
        (
        0
        ,
        
        1
        
          /
        
        2
        ,
        
        1
        
          /
        
        2
        )
        ,
      
    
    {\displaystyle \operatorname {arg\,max} (1,\,5,\,5)=(0,\,1/2,\,1/2),}
  
 since the second and third argument are both the maximum. In case all arguments are equal, this is simply 
  
    
      
        
          a
          r
          g
          
          m
          a
          x
        
        ⁡
        (
        z
        ,
        …
        ,
        z
        )
        =
        (
        1
        
          /
        
        n
        ,
        …
        ,
        1
        
          /
        
        n
        )
        .
      
    
    {\displaystyle \operatorname {arg\,max} (z,\dots ,z)=(1/n,\dots ,1/n).}
  
 Points z with multiple arg max values are singular points (or singularities, and form the singular set) – these are the points where arg max is discontinuous (with a jump discontinuity) – while points with a single arg max are known as non-singular or regular points.
With the last expression given in the introduction, softargmax is now a smooth approximation of arg max: as ⁠
  
    
      
        β
        →
        ∞
      
    
    {\displaystyle \beta \to \infty }
  
⁠, softargmax converges to arg max. There are various notions of convergence of a function; softargmax converges to arg max pointwise, meaning for each fixed input z as ⁠
  
    
      
        β
        →
        ∞
      
    
    {\displaystyle \beta \to \infty }
  
⁠, 
  
    
      
        
          σ
          
            β
          
        
        (
        
          z
        
        )
        →
        
          a
          r
          g
          
          m
          a
          x
        
        ⁡
        (
        
          z
        
        )
        .
      
    
    {\displaystyle \sigma _{\beta }(\mathbf {z} )\to \operatorname {arg\,max} (\mathbf {z} ).}
  
 However, softargmax does not converge uniformly to arg max, meaning intuitively that different points converge at different rates, and may converge arbitrarily slowly. In fact, softargmax is continuous, but arg max is not continuous at the singular set where two coordinates are equal, while the uniform limit of continuous functions is continuous. The reason it fails to converge uniformly is that for inputs where two coordinates are almost equal (and one is the maximum), the arg max is the index of one or the other, so a small change in input yields a large change in output. For example, 
  
    
      
        
          σ
          
            β
          
        
        (
        1
        ,
        
        1.0001
        )
        →
        (
        0
        ,
        1
        )
        ,
      
    
    {\displaystyle \sigma _{\beta }(1,\,1.0001)\to (0,1),}
  
 but 
  
    
      
        
          σ
          
            β
          
        
        (
        1
        ,
        
        0.9999
        )
        →
        (
        1
        ,
        
        0
        )
        ,
      
    
    {\displaystyle \sigma _{\beta }(1,\,0.9999)\to (1,\,0),}
  
 and 
  
    
      
        
          σ
          
            β
          
        
        (
        1
        ,
        
        1
        )
        =
        1
        
          /
        
        2
      
    
    {\displaystyle \sigma _{\beta }(1,\,1)=1/2}
  
 for all inputs: the closer the points are to the singular set 
  
    
      
        (
        x
        ,
        x
        )
      
    
    {\displaystyle (x,x)}
  
, the slower they converge. However, softargmax does converge compactly on the non-singular set.
Conversely, as ⁠
  
    
      
        β
        →
        −
        ∞
      
    
    {\displaystyle \beta \to -\infty }
  
⁠, softargmax converges to arg min in the same way, where here the singular set is points with two arg min values. In the language of tropical analysis, the softmax is a deformation or "quantization" of arg max and arg min, corresponding to using the log semiring instead of the max-plus semiring (respectively min-plus semiring), and recovering the arg max or arg min by taking the limit is called "tropicalization" or "dequantization".
It is also the case that, for any fixed β, if one input ⁠
  
    
      
        
          z
          
            i
          
        
      
    
    {\displaystyle z_{i}}
  
⁠ is much larger than the others relative to the temperature, 
  
    
      
        T
        =
        1
        
          /
        
        β
      
    
    {\displaystyle T=1/\beta }
  
, the output is approximately the arg max. For example, a difference of 10 is large relative to a temperature of 1:

  
    
      
        σ
        (
        0
        ,
        
        10
        )
        :=
        
          σ
          
            1
          
        
        (
        0
        ,
        
        10
        )
        =
        
          (
          
            1
            
              /
            
            
              (
              
                1
                +
                
                  e
                  
                    10
                  
                
              
              )
            
            ,
            
            
              e
              
                10
              
            
            
              /
            
            
              (
              
                1
                +
                
                  e
                  
                    10
                  
                
              
              )
            
          
          )
        
        ≈
        (
        0.00005
        ,
        
        0.99995
        )
      
    
    {\displaystyle \sigma (0,\,10):=\sigma _{1}(0,\,10)=\left(1/\left(1+e^{10}\right),\,e^{10}/\left(1+e^{10}\right)\right)\approx (0.00005,\,0.99995)}
  

However, if the difference is small relative to the temperature, the value is not close to the arg max. For example, a difference of 10 is small relative to a temperature of 100:

  
    
      
        
          σ
          
            1
            
              /
            
            100
          
        
        (
        0
        ,
        
        10
        )
        =
        
          (
          
            1
            
              /
            
            
              (
              
                1
                +
                
                  e
                  
                    1
                    
                      /
                    
                    10
                  
                
              
              )
            
            ,
            
            
              e
              
                1
                
                  /
                
                10
              
            
            
              /
            
            
              (
              
                1
                +
                
                  e
                  
                    1
                    
                      /
                    
                    10
                  
                
              
              )
            
          
          )
        
        ≈
        (
        0.475
        ,
        
        0.525
        )
        .
      
    
    {\displaystyle \sigma _{1/100}(0,\,10)=\left(1/\left(1+e^{1/10}\right),\,e^{1/10}/\left(1+e^{1/10}\right)\right)\approx (0.475,\,0.525).}
  

As ⁠
  
    
      
        β
        →
        ∞
      
    
    {\displaystyle \beta \to \infty }
  
⁠, temperature goes to zero, 
  
    
      
        T
        =
        1
        
          /
        
        β
        →
        0
      
    
    {\displaystyle T=1/\beta \to 0}
  
, so eventually all differences become large (relative to a shrinking temperature), which gives another interpretation for the limit behavior.

Probability theory
In probability theory, the output of the softargmax function can be used to represent a categorical distribution – that is, a probability distribution over K different possible outcomes.

Statistical mechanics
In statistical mechanics, the softargmax function is known as the Boltzmann distribution (or Gibbs distribution):: 7  the index set 
  
    
      
        
          1
          ,
          
          …
          ,
          
          k
        
      
    
    {\displaystyle {1,\,\dots ,\,k}}
  
 are the microstates of the system; the inputs 
  
    
      
        
          z
          
            i
          
        
      
    
    {\displaystyle z_{i}}
  
 are the energies of that state; the denominator is known as the partition function, often denoted by Z; and the factor β is called the coldness (or thermodynamic beta, or inverse temperature).

Applications
The softmax function is used in various multiclass classification methods, such as multinomial logistic regression (also known as softmax regression),: 206–209  multiclass linear discriminant analysis, naive Bayes classifiers, and artificial neural networks. Specifically, in multinomial logistic regression and linear discriminant analysis, the input to the function is the result of K distinct linear functions, and the predicted probability for the jth class given a sample vector x and a weighting vector w is:

  
    
      
        P
        (
        y
        =
        j
        ∣
        
          x
        
        )
        =
        
          
            
              e
              
                
                  
                    x
                  
                  
                    
                      T
                    
                  
                
                
                  
                    w
                  
                  
                    j
                  
                
              
            
            
              
                ∑
                
                  k
                  =
                  1
                
                
                  K
                
              
              
                e
                
                  
                    
                      x
                    
                    
                      
                        T
                      
                    
                  
                  
                    
                      w
                    
                    
                      k
                    
                  
                
              
            
          
        
      
    
    {\displaystyle P(y=j\mid \mathbf {x} )={\frac {e^{\mathbf {x} ^{\mathsf {T}}\mathbf {w} _{j}}}{\sum _{k=1}^{K}e^{\mathbf {x} ^{\mathsf {T}}\mathbf {w} _{k}}}}}
  

This can be seen as the composition of K linear functions 
  
    
      
        
          x
        
        ↦
        
          
            x
          
          
            
              T
            
          
        
        
          
            w
          
          
            1
          
        
        ,
        …
        ,
        
          x
        
        ↦
        
          
            x
          
          
            
              T
            
          
        
        
          
            w
          
          
            K
          
        
      
    
    {\displaystyle \mathbf {x} \mapsto \mathbf {x} ^{\mathsf {T}}\mathbf {w} _{1},\ldots ,\mathbf {x} \mapsto \mathbf {x} ^{\mathsf {T}}\mathbf {w} _{K}}
  
 and the softmax function (where 
  
    
      
        
          
            x
          
          
            
              T
            
          
        
        
          w
        
      
    
    {\displaystyle \mathbf {x} ^{\mathsf {T}}\mathbf {w} }
  
 denotes the inner product of 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
 and 
  
    
      
        
          w
        
      
    
    {\displaystyle \mathbf {w} }
  
). The operation is equivalent to applying a linear operator defined by 
  
    
      
        
          w
        
      
    
    {\displaystyle \mathbf {w} }
  
 to vectors 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
, thus transforming the original, probably highly-dimensional, input to vectors in a K-dimensional space 
  
    
      
        
          
            R
          
          
            K
          
        
      
    
    {\displaystyle \mathbb {R} ^{K}}
  
.

Neural networks
The standard softmax function is often used in the final layer of a neural network-based classifier. Such networks are commonly trained under a log loss (or cross-entropy) regime, giving a non-linear variant of multinomial logistic regression.
Since the function maps a vector and a specific index 
  
    
      
        i
      
    
    {\displaystyle i}
  
 to a real value, the derivative needs to take the index into account:

  
    
      
        
          
            ∂
            
              ∂
              
                q
                
                  k
                
              
            
          
        
        σ
        (
        
          
            q
          
        
        ,
        i
        )
        =
        σ
        (
        
          
            q
          
        
        ,
        i
        )
        (
        
          δ
          
            i
            k
          
        
        −
        σ
        (
        
          
            q
          
        
        ,
        k
        )
        )
        .
      
    
    {\displaystyle {\frac {\partial }{\partial q_{k}}}\sigma ({\textbf {q}},i)=\sigma ({\textbf {q}},i)(\delta _{ik}-\sigma ({\textbf {q}},k)).}
  

This expression is symmetrical in the indexes 
  
    
      
        i
        ,
        k
      
    
    {\displaystyle i,k}
  
 and thus may also be expressed as

  
    
      
        
          
            ∂
            
              ∂
              
                q
                
                  k
                
              
            
          
        
        σ
        (
        
          
            q
          
        
        ,
        i
        )
        =
        σ
        (
        
          
            q
          
        
        ,
        k
        )
        (
        
          δ
          
            i
            k
          
        
        −
        σ
        (
        
          
            q
          
        
        ,
        i
        )
        )
        .
      
    
    {\displaystyle {\frac {\partial }{\partial q_{k}}}\sigma ({\textbf {q}},i)=\sigma ({\textbf {q}},k)(\delta _{ik}-\sigma ({\textbf {q}},i)).}
  

Here, the Kronecker delta is used for simplicity (cf. the derivative of a sigmoid function, being expressed via the function itself). 
To ensure stable numerical computations subtracting the maximum value from the input vector is common. This approach, while not altering the output or the derivative theoretically, enhances stability by directly controlling the maximum exponent value computed.
If the function is scaled with the parameter 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
, then these expressions must be multiplied by 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
.
See multinomial logit for a probability model which uses the softmax activation function.

Reinforcement learning
In the field of reinforcement learning, a softmax function can be used to convert values into action probabilities. The function commonly used is:

  
    
      
        
          P
          
            t
          
        
        (
        a
        )
        =
        
          
            
              exp
              ⁡
              (
              
                q
                
                  t
                
              
              (
              a
              )
              
                /
              
              τ
              )
            
            
              
                ∑
                
                  i
                  =
                  1
                
                
                  n
                
              
              exp
              ⁡
              (
              
                q
                
                  t
                
              
              (
              i
              )
              
                /
              
              τ
              )
            
          
        
        
          ,
        
      
    
    {\displaystyle P_{t}(a)={\frac {\exp(q_{t}(a)/\tau )}{\sum _{i=1}^{n}\exp(q_{t}(i)/\tau )}}{\text{,}}}
  

where the action value 
  
    
      
        
          q
          
            t
          
        
        (
        a
        )
      
    
    {\displaystyle q_{t}(a)}
  
 corresponds to the expected reward of following action a and 
  
    
      
        τ
      
    
    {\displaystyle \tau }
  
 is called a temperature parameter (in allusion to statistical mechanics). For high temperatures (
  
    
      
        τ
        →
        ∞
      
    
    {\displaystyle \tau \to \infty }
  
), all actions have nearly the same probability and the lower the temperature, the more expected rewards affect the probability. For a low temperature (
  
    
      
        τ
        →
        
          0
          
            +
          
        
      
    
    {\displaystyle \tau \to 0^{+}}
  
), the probability of the action with the highest expected reward tends to 1.

Computational complexity and remedies
In neural network applications, the number K of possible outcomes is often large, e.g. in case of neural language models that predict the most likely outcome out of a vocabulary which might contain millions of possible words. This can make the calculations for the softmax layer (i.e. the matrix multiplications to determine the 
  
    
      
        
          z
          
            i
          
        
      
    
    {\displaystyle z_{i}}
  
, followed by the application of the softmax function itself) computationally expensive. What's more, the gradient descent backpropagation method for training such a neural network involves calculating the softmax for every training example, and the number of training examples can also become large. The computational effort for the softmax became a major limiting factor in the development of larger neural language models, motivating various remedies to reduce training times.
Approaches that reorganize the softmax layer for more efficient calculation include the hierarchical softmax and the differentiated softmax. The hierarchical softmax (introduced by Morin and Bengio in 2005) uses a binary tree structure where the outcomes (vocabulary words) are the leaves and the intermediate nodes are suitably selected "classes" of outcomes, forming latent variables. The desired probability (softmax value) of a leaf (outcome) can then be calculated as the product of the probabilities of all nodes on the path from the root to that leaf. Ideally, when the tree is balanced, this would reduce the computational complexity from 
  
    
      
        O
        (
        K
        )
      
    
    {\displaystyle O(K)}
  
 to 
  
    
      
        O
        (
        
          log
          
            2
          
        
        ⁡
        K
        )
      
    
    {\displaystyle O(\log _{2}K)}
  
. In practice, results depend on choosing a good strategy for clustering the outcomes into classes. A Huffman tree was used for this in Google's word2vec models (introduced in 2013) to achieve scalability.
A second kind of remedies is based on approximating the softmax (during training) with modified loss functions that avoid the calculation of the full normalization factor. These include methods that restrict the normalization sum to a sample of outcomes (e.g. Importance Sampling, Target Sampling).

Mathematical properties
Geometrically the softmax function maps the vector space 
  
    
      
        
          
            R
          
          
            K
          
        
      
    
    {\displaystyle \mathbb {R} ^{K}}
  
 to the boundary of the standard 
  
    
      
        (
        K
        −
        1
        )
      
    
    {\displaystyle (K-1)}
  
-simplex, cutting the dimension by one (the range is a 
  
    
      
        (
        K
        −
        1
        )
      
    
    {\displaystyle (K-1)}
  
-dimensional simplex in 
  
    
      
        K
      
    
    {\displaystyle K}
  
-dimensional space), due to the linear constraint that all output sum to 1 meaning it lies on a hyperplane.
Along the main diagonal 
  
    
      
        (
        x
        ,
        
        x
        ,
        
        …
        ,
        
        x
        )
        ,
      
    
    {\displaystyle (x,\,x,\,\dots ,\,x),}
  
 softmax is just the uniform distribution on outputs, 
  
    
      
        (
        1
        
          /
        
        n
        ,
        …
        ,
        1
        
          /
        
        n
        )
      
    
    {\displaystyle (1/n,\dots ,1/n)}
  
: equal scores yield equal probabilities.
More generally, softmax is invariant under translation by the same value in each coordinate: adding 
  
    
      
        
          c
        
        =
        (
        c
        ,
        
        …
        ,
        
        c
        )
      
    
    {\displaystyle \mathbf {c} =(c,\,\dots ,\,c)}
  
 to the inputs 
  
    
      
        
          z
        
      
    
    {\displaystyle \mathbf {z} }
  
 yields 
  
    
      
        σ
        (
        
          z
        
        +
        
          c
        
        )
        =
        σ
        (
        
          z
        
        )
      
    
    {\displaystyle \sigma (\mathbf {z} +\mathbf {c} )=\sigma (\mathbf {z} )}
  
, because it multiplies each exponent by the same factor, 
  
    
      
        
          e
          
            c
          
        
      
    
    {\displaystyle e^{c}}
  
 (because 
  
    
      
        
          e
          
            
              z
              
                i
              
            
            +
            c
          
        
        =
        
          e
          
            
              z
              
                i
              
            
          
        
        ⋅
        
          e
          
            c
          
        
      
    
    {\displaystyle e^{z_{i}+c}=e^{z_{i}}\cdot e^{c}}
  
), so the ratios do not change:

  
    
      
        σ
        (
        
          z
        
        +
        
          c
        
        
          )
          
            j
          
        
        =
        
          
            
              e
              
                
                  z
                  
                    j
                  
                
                +
                c
              
            
            
              
                ∑
                
                  k
                  =
                  1
                
                
                  K
                
              
              
                e
                
                  
                    z
                    
                      k
                    
                  
                  +
                  c
                
              
            
          
        
        =
        
          
            
              
                e
                
                  
                    z
                    
                      j
                    
                  
                
              
              ⋅
              
                e
                
                  c
                
              
            
            
              
                ∑
                
                  k
                  =
                  1
                
                
                  K
                
              
              
                e
                
                  
                    z
                    
                      k
                    
                  
                
              
              ⋅
              
                e
                
                  c
                
              
            
          
        
        =
        σ
        (
        
          z
        
        
          )
          
            j
          
        
        .
      
    
    {\displaystyle \sigma (\mathbf {z} +\mathbf {c} )_{j}={\frac {e^{z_{j}+c}}{\sum _{k=1}^{K}e^{z_{k}+c}}}={\frac {e^{z_{j}}\cdot e^{c}}{\sum _{k=1}^{K}e^{z_{k}}\cdot e^{c}}}=\sigma (\mathbf {z} )_{j}.}
  

Geometrically, softmax is constant along diagonals: this is the dimension that is eliminated, and corresponds to the softmax output being independent of a translation in the input scores (a choice of 0 score). One can normalize input scores by assuming that the sum is zero (subtract the average: 
  
    
      
        
          c
        
      
    
    {\displaystyle \mathbf {c} }
  
 where 
  
    
      
        c
        =
        
          
            1
            n
          
        
        ∑
        
          z
          
            i
          
        
      
    
    {\textstyle c={\frac {1}{n}}\sum z_{i}}
  
), and then the softmax takes the hyperplane of points that sum to zero, 
  
    
      
        ∑
        
          z
          
            i
          
        
        =
        0
      
    
    {\textstyle \sum z_{i}=0}
  
, to the open simplex of positive values that sum to 1
  
    
      
        ∑
        σ
        (
        
          z
        
        
          )
          
            i
          
        
        =
        1
      
    
    {\textstyle \sum \sigma (\mathbf {z} )_{i}=1}
  
, analogously to how the exponent takes 0 to 1, 
  
    
      
        
          e
          
            0
          
        
        =
        1
      
    
    {\displaystyle e^{0}=1}
  
 and is positive.
By contrast, softmax is not invariant under scaling. For instance, 
  
    
      
        σ
        
          
            (
          
        
        (
        0
        ,
        
        1
        )
        
          
            )
          
        
        =
        
          
            (
          
        
        1
        
          /
        
        (
        1
        +
        e
        )
        ,
        
        e
        
          /
        
        (
        1
        +
        e
        )
        
          
            )
          
        
      
    
    {\displaystyle \sigma {\bigl (}(0,\,1){\bigr )}={\bigl (}1/(1+e),\,e/(1+e){\bigr )}}
  
 but 
  
    
      
        σ
        
          
            (
          
        
        (
        0
        ,
        2
        )
        
          
            )
          
        
        =
        
          
            (
          
        
        1
        
          /
        
        
          (
          
            1
            +
            
              e
              
                2
              
            
          
          )
        
        ,
        
        
          e
          
            2
          
        
        
          /
        
        
          (
          
            1
            +
            
              e
              
                2
              
            
          
          )
        
        
          
            )
          
        
        .
      
    
    {\displaystyle \sigma {\bigl (}(0,2){\bigr )}={\bigl (}1/\left(1+e^{2}\right),\,e^{2}/\left(1+e^{2}\right){\bigr )}.}
  

The standard logistic function is the special case for a 1-dimensional axis in 2-dimensional space, say the x-axis in the (x, y) plane. One variable is fixed at 0 (say 
  
    
      
        
          z
          
            2
          
        
        =
        0
      
    
    {\displaystyle z_{2}=0}
  
), so 
  
    
      
        
          e
          
            0
          
        
        =
        1
      
    
    {\displaystyle e^{0}=1}
  
, and the other variable can vary, denote it 
  
    
      
        
          z
          
            1
          
        
        =
        x
      
    
    {\displaystyle z_{1}=x}
  
, so 
  
    
      
        
          e
          
            
              z
              
                1
              
            
          
        
        
          /
        
        
          ∑
          
            k
            =
            1
          
          
            2
          
        
        
          e
          
            
              z
              
                k
              
            
          
        
        =
        
          e
          
            x
          
        
        
          /
        
        
          (
          
            
              e
              
                x
              
            
            +
            1
          
          )
        
        ,
      
    
    {\textstyle e^{z_{1}}/\sum _{k=1}^{2}e^{z_{k}}=e^{x}/\left(e^{x}+1\right),}
  
 the standard logistic function, and 
  
    
      
        
          e
          
            
              z
              
                2
              
            
          
        
        
          /
        
        
          ∑
          
            k
            =
            1
          
          
            2
          
        
        
          e
          
            
              z
              
                k
              
            
          
        
        =
        1
        
          /
        
        
          (
          
            
              e
              
                x
              
            
            +
            1
          
          )
        
        ,
      
    
    {\textstyle e^{z_{2}}/\sum _{k=1}^{2}e^{z_{k}}=1/\left(e^{x}+1\right),}
  
 its complement (meaning they add up to 1). The 1-dimensional input could alternatively be expressed as the line 
  
    
      
        (
        x
        
          /
        
        2
        ,
        
        −
        x
        
          /
        
        2
        )
      
    
    {\displaystyle (x/2,\,-x/2)}
  
, with outputs 
  
    
      
        
          e
          
            x
            
              /
            
            2
          
        
        
          /
        
        
          (
          
            
              e
              
                x
                
                  /
                
                2
              
            
            +
            
              e
              
                −
                x
                
                  /
                
                2
              
            
          
          )
        
        =
        
          e
          
            x
          
        
        
          /
        
        
          (
          
            
              e
              
                x
              
            
            +
            1
          
          )
        
      
    
    {\displaystyle e^{x/2}/\left(e^{x/2}+e^{-x/2}\right)=e^{x}/\left(e^{x}+1\right)}
  
 and 
  
    
      
        
          e
          
            −
            x
            
              /
            
            2
          
        
        
          /
        
        
          (
          
            
              e
              
                x
                
                  /
                
                2
              
            
            +
            
              e
              
                −
                x
                
                  /
                
                2
              
            
          
          )
        
        =
        1
        
          /
        
        
          (
          
            
              e
              
                x
              
            
            +
            1
          
          )
        
        .
      
    
    {\displaystyle e^{-x/2}/\left(e^{x/2}+e^{-x/2}\right)=1/\left(e^{x}+1\right).}
  

The softmax function is also the gradient of the LogSumExp function, a smooth maximum:

  
    
      
        
          
            ∂
            
              ∂
              
                z
                
                  i
                
              
            
          
        
        LSE
        ⁡
        (
        
          z
        
        )
        =
        
          
            
              exp
              ⁡
              
                z
                
                  i
                
              
            
            
              
                ∑
                
                  j
                  =
                  1
                
                
                  K
                
              
              exp
              ⁡
              
                z
                
                  j
                
              
            
          
        
        =
        σ
        (
        
          z
        
        
          )
          
            i
          
        
        ,
        
        
           for 
        
        i
        =
        1
        ,
        …
        ,
        K
        ,
        
        
          z
        
        =
        (
        
          z
          
            1
          
        
        ,
        
        …
        ,
        
        
          z
          
            K
          
        
        )
        ∈
        
          
            R
          
          
            K
          
        
        ,
      
    
    {\displaystyle {\frac {\partial }{\partial z_{i}}}\operatorname {LSE} (\mathbf {z} )={\frac {\exp z_{i}}{\sum _{j=1}^{K}\exp z_{j}}}=\sigma (\mathbf {z} )_{i},\quad {\text{ for }}i=1,\dotsc ,K,\quad \mathbf {z} =(z_{1},\,\dotsc ,\,z_{K})\in \mathbb {R} ^{K},}
  

where the LogSumExp function is defined as 
  
    
      
        LSE
        ⁡
        (
        
          z
          
            1
          
        
        ,
        
        …
        ,
        
        
          z
          
            n
          
        
        )
        =
        log
        ⁡
        
          (
          
            exp
            ⁡
            (
            
              z
              
                1
              
            
            )
            +
            ⋯
            +
            exp
            ⁡
            (
            
              z
              
                n
              
            
            )
          
          )
        
      
    
    {\displaystyle \operatorname {LSE} (z_{1},\,\dots ,\,z_{n})=\log \left(\exp(z_{1})+\cdots +\exp(z_{n})\right)}
  
.

History
The softmax function was used in statistical mechanics as the Boltzmann distribution in the foundational paper Boltzmann (1868), formalized and popularized in the influential textbook Gibbs (1902).
The use of the softmax in decision theory is credited to R. Duncan Luce,: 1  who used the axiom of independence of irrelevant alternatives in rational choice theory to deduce the softmax in Luce's choice axiom for relative preferences.
In machine learning, the term "softmax" is credited to John S. Bridle in two 1989 conference papers, Bridle (1990a):: 1  and Bridle (1990b):

We are concerned with feed-forward non-linear networks (multi-layer perceptrons, or MLPs) with multiple outputs. We wish to treat the outputs of the network as probabilities of alternatives (e.g. pattern classes), conditioned on the inputs. We look for appropriate output non-linearities and for appropriate criteria for adaptation of the parameters of the network (e.g. weights). We explain two modifications: probability scoring, which is an alternative to squared error minimisation, and a normalised exponential (softmax) multi-input generalisation of the logistic non-linearity.: 227 

For any input, the outputs must all be positive and they must sum to unity. ...
Given a set of unconstrained values, ⁠
  
    
      
        
          V
          
            j
          
        
        (
        x
        )
      
    
    {\displaystyle V_{j}(x)}
  
⁠, we can ensure both conditions by using a Normalised Exponential transformation:

  
    
      
        
          Q
          
            j
          
        
        (
        x
        )
        =
        
          
          
            e
            
              
                V
                
                  j
                
              
              (
              x
              )
            
          
          /
        
        
          ∑
          
            k
          
        
        
          e
          
            
              V
              
                k
              
            
            (
            x
            )
          
        
      
    
    {\displaystyle Q_{j}(x)=\left.e^{V_{j}(x)}\right/\sum _{k}e^{V_{k}(x)}}
  

This transformation can be considered a multi-input generalisation of the logistic, operating on the whole output layer. It preserves the rank order of its input values, and is a differentiable generalisation of the 'winner-take-all' operation of picking the maximum value. For this reason we like to refer to it as softmax.: 213

Example
With an input of (1, 2, 3, 4, 1, 2, 3), the softmax is approximately (0.024, 0.064, 0.175, 0.475, 0.024, 0.064, 0.175). The output has most of its weight where the "4" was in the original input. This is what the function is normally used for: to highlight the largest values and suppress values which are significantly below the maximum value. But note: a change of temperature changes the output.  When the temperature is multiplied by 10, the inputs are effectively (0.1, 0.2, 0.3, 0.4, 0.1, 0.2, 0.3) and the softmax is approximately (0.125, 0.138, 0.153, 0.169, 0.125, 0.138, 0.153). This shows that high temperatures de-emphasize the maximum value.
Computation of this example using Python code:

Alternatives
The softmax function generates probability predictions densely distributed over its support. Other functions like sparsemax or α-entmax can be used when sparse probability predictions are desired. Also the Gumbel-softmax reparametrization trick can be used when sampling from a discrete-discrete distribution needs to be mimicked in a differentiable manner.

See also
Softplus
Multinomial logistic regression
Dirichlet distribution – an alternative way to sample categorical distributions
Partition function
Exponential tilting – a generalization of Softmax to more general probability distributions

Notes


== References ==

## Related Articles

### Internal Links

- [Action selection](https://en.wikipedia.org/wiki/Action_selection)
- [Activation function](https://en.wikipedia.org/wiki/Activation_function)
- [Active learning (machine learning)](https://en.wikipedia.org/wiki/Active_learning_(machine_learning))
- [Conference on Neural Information Processing Systems](https://en.wikipedia.org/wiki/Conference_on_Neural_Information_Processing_Systems)
- [Adversarial machine learning](https://en.wikipedia.org/wiki/Adversarial_machine_learning)
- [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing)
- [AlexNet](https://en.wikipedia.org/wiki/AlexNet)
- [Alex Graves (computer scientist)](https://en.wikipedia.org/wiki/Alex_Graves_(computer_scientist))
- [Alex Krizhevsky](https://en.wikipedia.org/wiki/Alex_Krizhevsky)
- [Allen Newell](https://en.wikipedia.org/wiki/Allen_Newell)
- [AlphaFold](https://en.wikipedia.org/wiki/AlphaFold)
- [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo)
- [AlphaZero](https://en.wikipedia.org/wiki/AlphaZero)
- [Andrej Karpathy](https://en.wikipedia.org/wiki/Andrej_Karpathy)
- [Andrew Ng](https://en.wikipedia.org/wiki/Andrew_Ng)
- [Anomaly detection](https://en.wikipedia.org/wiki/Anomaly_detection)
- [Apprenticeship learning](https://en.wikipedia.org/wiki/Apprenticeship_learning)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Arg max](https://en.wikipedia.org/wiki/Arg_max)
- [Artificial general intelligence](https://en.wikipedia.org/wiki/Artificial_general_intelligence)
- [Artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence)
- [Neural network (machine learning)](https://en.wikipedia.org/wiki/Neural_network_(machine_learning))
- [Association rule learning](https://en.wikipedia.org/wiki/Association_rule_learning)
- [Attention (machine learning)](https://en.wikipedia.org/wiki/Attention_(machine_learning))
- [Aurora (text-to-image model)](https://en.wikipedia.org/wiki/Aurora_(text-to-image_model))
- [AutoGPT](https://en.wikipedia.org/wiki/AutoGPT)
- [Autoencoder](https://en.wikipedia.org/wiki/Autoencoder)
- [Automated machine learning](https://en.wikipedia.org/wiki/Automated_machine_learning)
- [Autoregressive model](https://en.wikipedia.org/wiki/Autoregressive_model)
- [BERT (language model)](https://en.wikipedia.org/wiki/BERT_(language_model))
- [BIRCH](https://en.wikipedia.org/wiki/BIRCH)
- [BLOOM (language model)](https://en.wikipedia.org/wiki/BLOOM_(language_model))
- [Backpropagation](https://en.wikipedia.org/wiki/Backpropagation)
- [Base (exponentiation)](https://en.wikipedia.org/wiki/Base_(exponentiation))
- [Online machine learning](https://en.wikipedia.org/wiki/Online_machine_learning)
- [Batch normalization](https://en.wikipedia.org/wiki/Batch_normalization)
- [Bayesian network](https://en.wikipedia.org/wiki/Bayesian_network)
- [Bernard Widrow](https://en.wikipedia.org/wiki/Bernard_Widrow)
- [Bias–variance tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff)
- [Boltzmann constant](https://en.wikipedia.org/wiki/Boltzmann_constant)
- [Boltzmann distribution](https://en.wikipedia.org/wiki/Boltzmann_distribution)
- [Boltzmann machine](https://en.wikipedia.org/wiki/Boltzmann_machine)
- [Boosting (machine learning)](https://en.wikipedia.org/wiki/Boosting_(machine_learning))
- [Bootstrap aggregating](https://en.wikipedia.org/wiki/Bootstrap_aggregating)
- [Boundary (topology)](https://en.wikipedia.org/wiki/Boundary_(topology))
- [CURE algorithm](https://en.wikipedia.org/wiki/CURE_algorithm)
- [Canonical correlation](https://en.wikipedia.org/wiki/Canonical_correlation)
- [Categorical distribution](https://en.wikipedia.org/wiki/Categorical_distribution)
- [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT)
- [Chinchilla (language model)](https://en.wikipedia.org/wiki/Chinchilla_(language_model))
- [Claude (language model)](https://en.wikipedia.org/wiki/Claude_(language_model))
- [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon)
- [Cliff Shaw](https://en.wikipedia.org/wiki/Cliff_Shaw)
- [Cluster analysis](https://en.wikipedia.org/wiki/Cluster_analysis)
- [Coefficient of determination](https://en.wikipedia.org/wiki/Coefficient_of_determination)
- [Thermodynamic beta](https://en.wikipedia.org/wiki/Thermodynamic_beta)
- [Compact convergence](https://en.wikipedia.org/wiki/Compact_convergence)
- [Computational complexity](https://en.wikipedia.org/wiki/Computational_complexity)
- [Computational learning theory](https://en.wikipedia.org/wiki/Computational_learning_theory)
- [Conditional random field](https://en.wikipedia.org/wiki/Conditional_random_field)
- [Conference on Neural Information Processing Systems](https://en.wikipedia.org/wiki/Conference_on_Neural_Information_Processing_Systems)
- [Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix)
- [Conjugate gradient method](https://en.wikipedia.org/wiki/Conjugate_gradient_method)
- [Convolution](https://en.wikipedia.org/wiki/Convolution)
- [Convolutional neural network](https://en.wikipedia.org/wiki/Convolutional_neural_network)
- [Cross-entropy](https://en.wikipedia.org/wiki/Cross-entropy)
- [Cross-entropy](https://en.wikipedia.org/wiki/Cross-entropy)
- [Crowdsourcing](https://en.wikipedia.org/wiki/Crowdsourcing)
- [Curriculum learning](https://en.wikipedia.org/wiki/Curriculum_learning)
- [DALL-E](https://en.wikipedia.org/wiki/DALL-E)
- [DBSCAN](https://en.wikipedia.org/wiki/DBSCAN)
- [Data augmentation](https://en.wikipedia.org/wiki/Data_augmentation)
- [Data cleansing](https://en.wikipedia.org/wiki/Data_cleansing)
- [Data mining](https://en.wikipedia.org/wiki/Data_mining)
- [David Silver (computer scientist)](https://en.wikipedia.org/wiki/David_Silver_(computer_scientist))
- [Decision theory](https://en.wikipedia.org/wiki/Decision_theory)
- [Decision tree learning](https://en.wikipedia.org/wiki/Decision_tree_learning)
- [DeepDream](https://en.wikipedia.org/wiki/DeepDream)
- [Deep learning](https://en.wikipedia.org/wiki/Deep_learning)
- [Deep learning speech synthesis](https://en.wikipedia.org/wiki/Deep_learning_speech_synthesis)
- [Deformation (mathematics)](https://en.wikipedia.org/wiki/Deformation_(mathematics))
- [Demis Hassabis](https://en.wikipedia.org/wiki/Demis_Hassabis)
- [Density estimation](https://en.wikipedia.org/wiki/Density_estimation)
- [Differentiable neural computer](https://en.wikipedia.org/wiki/Differentiable_neural_computer)
- [Diffusion model](https://en.wikipedia.org/wiki/Diffusion_model)
- [Diffusion process](https://en.wikipedia.org/wiki/Diffusion_process)
- [Dimensionality reduction](https://en.wikipedia.org/wiki/Dimensionality_reduction)
- [Dirichlet distribution](https://en.wikipedia.org/wiki/Dirichlet_distribution)
- [Discrete uniform distribution](https://en.wikipedia.org/wiki/Discrete_uniform_distribution)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Double descent](https://en.wikipedia.org/wiki/Double_descent)
- [Dream Machine (text-to-video model)](https://en.wikipedia.org/wiki/Dream_Machine_(text-to-video_model))
- [ECML PKDD](https://en.wikipedia.org/wiki/ECML_PKDD)
- [ESA (company)](https://en.wikipedia.org/wiki/ESA_(company))
- [Echo state network](https://en.wikipedia.org/wiki/Echo_state_network)
- [Electrochemical RAM](https://en.wikipedia.org/wiki/Electrochemical_RAM)
- [Elementary Principles in Statistical Mechanics](https://en.wikipedia.org/wiki/Elementary_Principles_in_Statistical_Mechanics)
- [ElevenLabs](https://en.wikipedia.org/wiki/ElevenLabs)
- [Empirical risk minimization](https://en.wikipedia.org/wiki/Empirical_risk_minimization)
- [Ensemble learning](https://en.wikipedia.org/wiki/Ensemble_learning)
- [Entropy (information theory)](https://en.wikipedia.org/wiki/Entropy_(information_theory))
- [Expectation–maximization algorithm](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm)
- [Exponential function](https://en.wikipedia.org/wiki/Exponential_function)
- [Exponential tilting](https://en.wikipedia.org/wiki/Exponential_tilting)
- [Facial recognition system](https://en.wikipedia.org/wiki/Facial_recognition_system)
- [Factor analysis](https://en.wikipedia.org/wiki/Factor_analysis)
- [Feature engineering](https://en.wikipedia.org/wiki/Feature_engineering)
- [Feature learning](https://en.wikipedia.org/wiki/Feature_learning)
- [Feedforward neural network](https://en.wikipedia.org/wiki/Feedforward_neural_network)
- [Fei-Fei Li](https://en.wikipedia.org/wiki/Fei-Fei_Li)
- [Flux (text-to-image model)](https://en.wikipedia.org/wiki/Flux_(text-to-image_model))
- [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt)
- [Function composition](https://en.wikipedia.org/wiki/Function_composition)
- [Fuzzy clustering](https://en.wikipedia.org/wiki/Fuzzy_clustering)
- [GPT-1](https://en.wikipedia.org/wiki/GPT-1)
- [GPT-2](https://en.wikipedia.org/wiki/GPT-2)
- [GPT-3](https://en.wikipedia.org/wiki/GPT-3)
- [GPT-4](https://en.wikipedia.org/wiki/GPT-4)
- [GPT-4o](https://en.wikipedia.org/wiki/GPT-4o)
- [GPT-J](https://en.wikipedia.org/wiki/GPT-J)
- [Gated recurrent unit](https://en.wikipedia.org/wiki/Gated_recurrent_unit)
- [Gating mechanism](https://en.wikipedia.org/wiki/Gating_mechanism)
- [Gemini (chatbot)](https://en.wikipedia.org/wiki/Gemini_(chatbot))
- [Gemini (language model)](https://en.wikipedia.org/wiki/Gemini_(language_model))
- [Generative adversarial network](https://en.wikipedia.org/wiki/Generative_adversarial_network)
- [Generative model](https://en.wikipedia.org/wiki/Generative_model)
- [Generative pre-trained transformer](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer)
- [Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton)
- [Boltzmann distribution](https://en.wikipedia.org/wiki/Boltzmann_distribution)
- [GloVe](https://en.wikipedia.org/wiki/GloVe)
- [Glossary of artificial intelligence](https://en.wikipedia.org/wiki/Glossary_of_artificial_intelligence)
- [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent)
- [Grammar induction](https://en.wikipedia.org/wiki/Grammar_induction)
- [Graph neural network](https://en.wikipedia.org/wiki/Graph_neural_network)
- [Graphical model](https://en.wikipedia.org/wiki/Graphical_model)
- [Grok (chatbot)](https://en.wikipedia.org/wiki/Grok_(chatbot))
- [Hallucination (artificial intelligence)](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))
- [Handwriting recognition](https://en.wikipedia.org/wiki/Handwriting_recognition)
- [Handle System](https://en.wikipedia.org/wiki/Handle_System)
- [Herbert A. Simon](https://en.wikipedia.org/wiki/Herbert_A._Simon)
- [Hidden Markov model](https://en.wikipedia.org/wiki/Hidden_Markov_model)
- [Hierarchical clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering)
- [Highway network](https://en.wikipedia.org/wiki/Highway_network)
- [Huawei PanGu](https://en.wikipedia.org/wiki/Huawei_PanGu)
- [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding)
- [Human-in-the-loop](https://en.wikipedia.org/wiki/Human-in-the-loop)
- [Human image synthesis](https://en.wikipedia.org/wiki/Human_image_synthesis)
- [Hyperparameter (machine learning)](https://en.wikipedia.org/wiki/Hyperparameter_(machine_learning))
- [Hyperplane](https://en.wikipedia.org/wiki/Hyperplane)
- [IBM Granite](https://en.wikipedia.org/wiki/IBM_Granite)
- [IBM Watson](https://en.wikipedia.org/wiki/IBM_Watson)
- [IBM Watsonx](https://en.wikipedia.org/wiki/IBM_Watsonx)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Ian Goodfellow](https://en.wikipedia.org/wiki/Ian_Goodfellow)
- [Ideogram (text-to-image model)](https://en.wikipedia.org/wiki/Ideogram_(text-to-image_model))
- [Ilya Sutskever](https://en.wikipedia.org/wiki/Ilya_Sutskever)
- [Google Brain](https://en.wikipedia.org/wiki/Google_Brain)
- [Imitation learning](https://en.wikipedia.org/wiki/Imitation_learning)
- [Independence of irrelevant alternatives](https://en.wikipedia.org/wiki/Independence_of_irrelevant_alternatives)
- [Independent component analysis](https://en.wikipedia.org/wiki/Independent_component_analysis)
- [International Conference on Learning Representations](https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations)
- [International Conference on Machine Learning](https://en.wikipedia.org/wiki/International_Conference_on_Machine_Learning)
- [International Joint Conference on Artificial Intelligence](https://en.wikipedia.org/wiki/International_Joint_Conference_on_Artificial_Intelligence)
- [Interval (mathematics)](https://en.wikipedia.org/wiki/Interval_(mathematics))
- [Thermodynamic beta](https://en.wikipedia.org/wiki/Thermodynamic_beta)
- [Isolation forest](https://en.wikipedia.org/wiki/Isolation_forest)
- [John Hopfield](https://en.wikipedia.org/wiki/John_Hopfield)
- [John McCarthy (computer scientist)](https://en.wikipedia.org/wiki/John_McCarthy_(computer_scientist))
- [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann)
- [Joseph Weizenbaum](https://en.wikipedia.org/wiki/Joseph_Weizenbaum)
- [Josiah Willard Gibbs](https://en.wikipedia.org/wiki/Josiah_Willard_Gibbs)
- [Journal of Machine Learning Research](https://en.wikipedia.org/wiki/Journal_of_Machine_Learning_Research)
- [Classification of discontinuities](https://en.wikipedia.org/wiki/Classification_of_discontinuities)
- [Jürgen Schmidhuber](https://en.wikipedia.org/wiki/J%C3%BCrgen_Schmidhuber)
- [K-means clustering](https://en.wikipedia.org/wiki/K-means_clustering)
- [K-nearest neighbors algorithm](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
- [Kernel method](https://en.wikipedia.org/wiki/Kernel_method)
- [Kuaishou](https://en.wikipedia.org/wiki/Kuaishou)
- [Kronecker delta](https://en.wikipedia.org/wiki/Kronecker_delta)
- [LaMDA](https://en.wikipedia.org/wiki/LaMDA)
- [Language model](https://en.wikipedia.org/wiki/Language_model)
- [Large language model](https://en.wikipedia.org/wiki/Large_language_model)
- [Latent diffusion model](https://en.wikipedia.org/wiki/Latent_diffusion_model)
- [Latent and observable variables](https://en.wikipedia.org/wiki/Latent_and_observable_variables)
- [LeNet](https://en.wikipedia.org/wiki/LeNet)
- [Learning curve (machine learning)](https://en.wikipedia.org/wiki/Learning_curve_(machine_learning))
- [Learning to rank](https://en.wikipedia.org/wiki/Learning_to_rank)
- [Linear equation](https://en.wikipedia.org/wiki/Linear_equation)
- [Linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)
- [Linear function](https://en.wikipedia.org/wiki/Linear_function)
- [Linear regression](https://en.wikipedia.org/wiki/Linear_regression)
- [List of artificial intelligence companies](https://en.wikipedia.org/wiki/List_of_artificial_intelligence_companies)
- [List of artificial intelligence projects](https://en.wikipedia.org/wiki/List_of_artificial_intelligence_projects)
- [List of datasets for machine-learning research](https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research)
- [List of datasets in computer vision and image processing](https://en.wikipedia.org/wiki/List_of_datasets_in_computer_vision_and_image_processing)
- [Llama (language model)](https://en.wikipedia.org/wiki/Llama_(language_model))
- [Local outlier factor](https://en.wikipedia.org/wiki/Local_outlier_factor)
- [LogSumExp](https://en.wikipedia.org/wiki/LogSumExp)
- [Log semiring](https://en.wikipedia.org/wiki/Log_semiring)
- [Logistic function](https://en.wikipedia.org/wiki/Logistic_function)
- [Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression)
- [Long short-term memory](https://en.wikipedia.org/wiki/Long_short-term_memory)
- [Loss functions for classification](https://en.wikipedia.org/wiki/Loss_functions_for_classification)
- [Lotfi A. Zadeh](https://en.wikipedia.org/wiki/Lotfi_A._Zadeh)
- [Luce's choice axiom](https://en.wikipedia.org/wiki/Luce%27s_choice_axiom)
- [Ludwig Boltzmann](https://en.wikipedia.org/wiki/Ludwig_Boltzmann)
- [Machine Learning (journal)](https://en.wikipedia.org/wiki/Machine_Learning_(journal))
- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
- [Mamba (deep learning architecture)](https://en.wikipedia.org/wiki/Mamba_(deep_learning_architecture))
- [Marvin Minsky](https://en.wikipedia.org/wiki/Marvin_Minsky)
- [Tropical semiring](https://en.wikipedia.org/wiki/Tropical_semiring)
- [Maximum and minimum](https://en.wikipedia.org/wiki/Maximum_and_minimum)
- [Mean shift](https://en.wikipedia.org/wiki/Mean_shift)
- [Medium (website)](https://en.wikipedia.org/wiki/Medium_(website))
- [Memtransistor](https://en.wikipedia.org/wiki/Memtransistor)
- [Meta-learning (computer science)](https://en.wikipedia.org/wiki/Meta-learning_(computer_science))
- [Microstate (statistical mechanics)](https://en.wikipedia.org/wiki/Microstate_(statistical_mechanics))
- [Midjourney](https://en.wikipedia.org/wiki/Midjourney)
- [Tropical semiring](https://en.wikipedia.org/wiki/Tropical_semiring)
- [MuZero](https://en.wikipedia.org/wiki/MuZero)
- [Multi-agent reinforcement learning](https://en.wikipedia.org/wiki/Multi-agent_reinforcement_learning)
- [Multiclass classification](https://en.wikipedia.org/wiki/Multiclass_classification)
- [Multilayer perceptron](https://en.wikipedia.org/wiki/Multilayer_perceptron)
- [Multimodal learning](https://en.wikipedia.org/wiki/Multimodal_learning)
- [Multinomial logistic regression](https://en.wikipedia.org/wiki/Multinomial_logistic_regression)
- [Multinomial logistic regression](https://en.wikipedia.org/wiki/Multinomial_logistic_regression)
- [Music and artificial intelligence](https://en.wikipedia.org/wiki/Music_and_artificial_intelligence)
- [Naive Bayes classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
- [Nathaniel Rochester (computer scientist)](https://en.wikipedia.org/wiki/Nathaniel_Rochester_(computer_scientist))
- [Neural Turing machine](https://en.wikipedia.org/wiki/Neural_Turing_machine)
- [Neural machine translation](https://en.wikipedia.org/wiki/Neural_machine_translation)
- [Neural network (machine learning)](https://en.wikipedia.org/wiki/Neural_network_(machine_learning))
- [Neural radiance field](https://en.wikipedia.org/wiki/Neural_radiance_field)
- [Neuro-symbolic AI](https://en.wikipedia.org/wiki/Neuro-symbolic_AI)
- [Neuromorphic computing](https://en.wikipedia.org/wiki/Neuromorphic_computing)
- [Non-negative matrix factorization](https://en.wikipedia.org/wiki/Non-negative_matrix_factorization)
- [Normalization (machine learning)](https://en.wikipedia.org/wiki/Normalization_(machine_learning))
- [OPTICS algorithm](https://en.wikipedia.org/wiki/OPTICS_algorithm)
- [Occam learning](https://en.wikipedia.org/wiki/Occam_learning)
- [Oliver Selfridge](https://en.wikipedia.org/wiki/Oliver_Selfridge)
- [One-hot](https://en.wikipedia.org/wiki/One-hot)
- [Online machine learning](https://en.wikipedia.org/wiki/Online_machine_learning)
- [Ontology learning](https://en.wikipedia.org/wiki/Ontology_learning)
- [OpenAI Five](https://en.wikipedia.org/wiki/OpenAI_Five)
- [OpenAI o1](https://en.wikipedia.org/wiki/OpenAI_o1)
- [Optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition)
- [Outline of machine learning](https://en.wikipedia.org/wiki/Outline_of_machine_learning)
- [Overfitting](https://en.wikipedia.org/wiki/Overfitting)
- [PaLM](https://en.wikipedia.org/wiki/PaLM)
- [Parameter](https://en.wikipedia.org/wiki/Parameter)
- [Partition function (statistical mechanics)](https://en.wikipedia.org/wiki/Partition_function_(statistical_mechanics))
- [Paul Werbos](https://en.wikipedia.org/wiki/Paul_Werbos)
- [Perceptron](https://en.wikipedia.org/wiki/Perceptron)
- [Pointwise convergence](https://en.wikipedia.org/wiki/Pointwise_convergence)
- [Principal component analysis](https://en.wikipedia.org/wiki/Principal_component_analysis)
- [Probability distribution](https://en.wikipedia.org/wiki/Probability_distribution)
- [Probability theory](https://en.wikipedia.org/wiki/Probability_theory)
- [Probably approximately correct learning](https://en.wikipedia.org/wiki/Probably_approximately_correct_learning)
- [Project Debater](https://en.wikipedia.org/wiki/Project_Debater)
- [Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering)
- [Proper generalized decomposition](https://en.wikipedia.org/wiki/Proper_generalized_decomposition)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Q-learning](https://en.wikipedia.org/wiki/Q-learning)
- [Quantum machine learning](https://en.wikipedia.org/wiki/Quantum_machine_learning)
- [Quasi-Newton method](https://en.wikipedia.org/wiki/Quasi-Newton_method)
- [R. Duncan Luce](https://en.wikipedia.org/wiki/R._Duncan_Luce)
- [Random forest](https://en.wikipedia.org/wiki/Random_forest)
- [Random sample consensus](https://en.wikipedia.org/wiki/Random_sample_consensus)
- [Rational choice model](https://en.wikipedia.org/wiki/Rational_choice_model)
- [Receiver operating characteristic](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
- [Rectifier (neural networks)](https://en.wikipedia.org/wiki/Rectifier_(neural_networks))
- [Recurrent neural network](https://en.wikipedia.org/wiki/Recurrent_neural_network)
- [Regression analysis](https://en.wikipedia.org/wiki/Regression_analysis)
- [Regularization (mathematics)](https://en.wikipedia.org/wiki/Regularization_(mathematics))
- [Reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning)
- [Reinforcement learning from human feedback](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback)
- [Relevance vector machine](https://en.wikipedia.org/wiki/Relevance_vector_machine)
- [Reparameterization trick](https://en.wikipedia.org/wiki/Reparameterization_trick)
- [Reservoir computing](https://en.wikipedia.org/wiki/Reservoir_computing)
- [Residual neural network](https://en.wikipedia.org/wiki/Residual_neural_network)
- [Restricted Boltzmann machine](https://en.wikipedia.org/wiki/Restricted_Boltzmann_machine)
- [Retrieval-augmented generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)
- [Robot control](https://en.wikipedia.org/wiki/Robot_control)
- [Rule-based machine learning](https://en.wikipedia.org/wiki/Rule-based_machine_learning)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Self-driving car](https://en.wikipedia.org/wiki/Self-driving_car)
- [Self-organizing map](https://en.wikipedia.org/wiki/Self-organizing_map)
- [Self-play](https://en.wikipedia.org/wiki/Self-play)
- [Self-supervised learning](https://en.wikipedia.org/wiki/Self-supervised_learning)
- [Semantic analysis (machine learning)](https://en.wikipedia.org/wiki/Semantic_analysis_(machine_learning))
- [Weak supervision](https://en.wikipedia.org/wiki/Weak_supervision)
- [Seppo Linnainmaa](https://en.wikipedia.org/wiki/Seppo_Linnainmaa)
- [Seq2seq](https://en.wikipedia.org/wiki/Seq2seq)
- [Seymour Papert](https://en.wikipedia.org/wiki/Seymour_Papert)
- [Sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function)
- [Singular point of an algebraic variety](https://en.wikipedia.org/wiki/Singular_point_of_an_algebraic_variety)
- [Smoothness](https://en.wikipedia.org/wiki/Smoothness)
- [Smooth maximum](https://en.wikipedia.org/wiki/Smooth_maximum)
- [Softmax function](https://en.wikipedia.org/wiki/Softmax_function)
- [Softplus](https://en.wikipedia.org/wiki/Softplus)
- [Sora (text-to-video model)](https://en.wikipedia.org/wiki/Sora_(text-to-video_model))
- [Sparse dictionary learning](https://en.wikipedia.org/wiki/Sparse_dictionary_learning)
- [Speech recognition](https://en.wikipedia.org/wiki/Speech_recognition)
- [Spiking neural network](https://en.wikipedia.org/wiki/Spiking_neural_network)
- [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion)
- [Logistic function](https://en.wikipedia.org/wiki/Logistic_function)
- [Simplex](https://en.wikipedia.org/wiki/Simplex)
- [State–action–reward–state–action](https://en.wikipedia.org/wiki/State%E2%80%93action%E2%80%93reward%E2%80%93state%E2%80%93action)
- [Statistical classification](https://en.wikipedia.org/wiki/Statistical_classification)
- [Statistical learning theory](https://en.wikipedia.org/wiki/Statistical_learning_theory)
- [Statistical mechanics](https://en.wikipedia.org/wiki/Statistical_mechanics)
- [Stephen Grossberg](https://en.wikipedia.org/wiki/Stephen_Grossberg)
- [Stochastic gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)
- [Structured prediction](https://en.wikipedia.org/wiki/Structured_prediction)
- [Suno AI](https://en.wikipedia.org/wiki/Suno_AI)
- [Supervised learning](https://en.wikipedia.org/wiki/Supervised_learning)
- [Support (mathematics)](https://en.wikipedia.org/wiki/Support_(mathematics))
- [Support vector machine](https://en.wikipedia.org/wiki/Support_vector_machine)
- [T-distributed stochastic neighbor embedding](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding)
- [T5 (language model)](https://en.wikipedia.org/wiki/T5_(language_model))
- [Temperature](https://en.wikipedia.org/wiki/Temperature)
- [Temporal difference learning](https://en.wikipedia.org/wiki/Temporal_difference_learning)
- [Text-to-image model](https://en.wikipedia.org/wiki/Text-to-image_model)
- [Text-to-video model](https://en.wikipedia.org/wiki/Text-to-video_model)
- [Thermodynamic beta](https://en.wikipedia.org/wiki/Thermodynamic_beta)
- [Training, validation, and test data sets](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets)
- [Transformer (deep learning architecture)](https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture))
- [Transformer (deep learning architecture)](https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture))
- [Tropical analysis](https://en.wikipedia.org/wiki/Tropical_analysis)
- [U-Net](https://en.wikipedia.org/wiki/U-Net)
- [Udio](https://en.wikipedia.org/wiki/Udio)
- [Uniform convergence](https://en.wikipedia.org/wiki/Uniform_convergence)
- [Unsupervised learning](https://en.wikipedia.org/wiki/Unsupervised_learning)
- [Vapnik–Chervonenkis theory](https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory)
- [Variational autoencoder](https://en.wikipedia.org/wiki/Variational_autoencoder)
- [Vector space](https://en.wikipedia.org/wiki/Vector_space)
- [VideoPoet](https://en.wikipedia.org/wiki/VideoPoet)
- [Vision transformer](https://en.wikipedia.org/wiki/Vision_transformer)
- [Walter Pitts](https://en.wikipedia.org/wiki/Walter_Pitts)
- [Warren Sturgis McCulloch](https://en.wikipedia.org/wiki/Warren_Sturgis_McCulloch)
- [WaveNet](https://en.wikipedia.org/wiki/WaveNet)
- [Weight initialization](https://en.wikipedia.org/wiki/Weight_initialization)
- [Whisper (speech recognition system)](https://en.wikipedia.org/wiki/Whisper_(speech_recognition_system))
- [Word2vec](https://en.wikipedia.org/wiki/Word2vec)
- [Word embedding](https://en.wikipedia.org/wiki/Word_embedding)
- [Yann LeCun](https://en.wikipedia.org/wiki/Yann_LeCun)
- [Yoshua Bengio](https://en.wikipedia.org/wiki/Yoshua_Bengio)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Template:Artificial intelligence navbox](https://en.wikipedia.org/wiki/Template:Artificial_intelligence_navbox)
- [Template:Machine learning](https://en.wikipedia.org/wiki/Template:Machine_learning)
- [Template talk:Artificial intelligence navbox](https://en.wikipedia.org/wiki/Template_talk:Artificial_intelligence_navbox)
- [Template talk:Machine learning](https://en.wikipedia.org/wiki/Template_talk:Machine_learning)
- [Category:Articles with unsourced statements from March 2024](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_March_2024)
- [Category:Artificial neural networks](https://en.wikipedia.org/wiki/Category:Artificial_neural_networks)
- [Category:Machine learning](https://en.wikipedia.org/wiki/Category:Machine_learning)
- [Portal:Technology](https://en.wikipedia.org/wiki/Portal:Technology)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:45:13.078112+00:00_