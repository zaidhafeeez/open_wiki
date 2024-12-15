# Normalization (machine learning)

## Article Metadata

- **Last Updated:** 2024-12-15T04:37:36.784780+00:00
- **Original Article:** [Normalization (machine learning)](https://en.wikipedia.org/wiki/Normalization_(machine_learning))
- **Language:** en
- **Page ID:** 77557393

## Summary

In machine learning, normalization is a statistical technique with various applications. There are two main forms of normalization, namely data normalization and activation normalization. Data normalization (or feature scaling) includes methods that rescale input data so that the features have the same range, mean, variance, or other statistical properties. For instance, a popular choice of feature scaling method is min-max normalization, where each feature is transformed to have the same range 

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:CS1 errors: missing periodical
- Category:Deep learning
- Category:Machine learning
- Category:Neural networks
- Category:Short description with empty Wikidata description
- Category:Statistical data transformation

## Table of Contents

- Batch normalization
- Layer normalization
- Weight normalization
- CNN-specific normalization
- Transformers
- Miscellaneous
- See also
- References
- Further reading

## Content

In machine learning, normalization is a statistical technique with various applications. There are two main forms of normalization, namely data normalization and activation normalization. Data normalization (or feature scaling) includes methods that rescale input data so that the features have the same range, mean, variance, or other statistical properties. For instance, a popular choice of feature scaling method is min-max normalization, where each feature is transformed to have the same range (typically 
  
    
      
        [
        0
        ,
        1
        ]
      
    
    {\displaystyle [0,1]}
  
 or 
  
    
      
        [
        −
        1
        ,
        1
        ]
      
    
    {\displaystyle [-1,1]}
  
). This solves the problem of different features having vastly different scales, for example if one feature is measured in kilometers and another in nanometers.
Activation normalization, on the other hand, is specific to deep learning, and includes methods that rescale the activation of hidden neurons inside neural networks.
Normalization is often used to:

increase the speed of training convergence,
reduce sensitivity to variations and feature scales in input data,
reduce overfitting,
and produce better model generalization to unseen data.
Normalization techniques are often theoretically justified as reducing covariance shift, smoothing optimization landscapes, and increasing regularization, though they are mainly justified by empirical success.

Batch normalization
Batch normalization (BatchNorm) operates on the activations of a layer for each mini-batch.
Consider a simple feedforward network, defined by chaining together modules:

  
    
      
        
          x
          
            (
            0
            )
          
        
        ↦
        
          x
          
            (
            1
            )
          
        
        ↦
        
          x
          
            (
            2
            )
          
        
        ↦
        ⋯
      
    
    {\displaystyle x^{(0)}\mapsto x^{(1)}\mapsto x^{(2)}\mapsto \cdots }
  

where each network module can be a linear transform, a nonlinear activation function, a convolution, etc. 
  
    
      
        
          x
          
            (
            0
            )
          
        
      
    
    {\displaystyle x^{(0)}}
  
 is the input vector, 
  
    
      
        
          x
          
            (
            1
            )
          
        
      
    
    {\displaystyle x^{(1)}}
  
 is the output vector from the first module, etc.
BatchNorm is a module that can be inserted at any point in the feedforward network. For example, suppose it is inserted just after 
  
    
      
        
          x
          
            (
            l
            )
          
        
      
    
    {\displaystyle x^{(l)}}
  
, then the network would operate accordingly:

  
    
      
        ⋯
        ↦
        
          x
          
            (
            l
            )
          
        
        ↦
        
          B
          N
        
        (
        
          x
          
            (
            l
            )
          
        
        )
        ↦
        
          x
          
            (
            l
            +
            1
            )
          
        
        ↦
        ⋯
      
    
    {\displaystyle \cdots \mapsto x^{(l)}\mapsto \mathrm {BN} (x^{(l)})\mapsto x^{(l+1)}\mapsto \cdots }
  

The BatchNorm module does not operate over individual inputs. Instead, it must operate over one batch of inputs at a time.
Concretely, suppose we have a batch of inputs 
  
    
      
        
          x
          
            (
            1
            )
          
          
            (
            0
            )
          
        
        ,
        
          x
          
            (
            2
            )
          
          
            (
            0
            )
          
        
        ,
        …
        ,
        
          x
          
            (
            B
            )
          
          
            (
            0
            )
          
        
      
    
    {\displaystyle x_{(1)}^{(0)},x_{(2)}^{(0)},\dots ,x_{(B)}^{(0)}}
  
, fed all at once into the network. We would obtain in the middle of the network some vectors:

  
    
      
        
          x
          
            (
            1
            )
          
          
            (
            l
            )
          
        
        ,
        
          x
          
            (
            2
            )
          
          
            (
            l
            )
          
        
        ,
        …
        ,
        
          x
          
            (
            B
            )
          
          
            (
            l
            )
          
        
      
    
    {\displaystyle x_{(1)}^{(l)},x_{(2)}^{(l)},\dots ,x_{(B)}^{(l)}}
  

The BatchNorm module computes the coordinate-wise mean and variance of these vectors:

  
    
      
        
          
            
              
                
                  μ
                  
                    i
                  
                  
                    (
                    l
                    )
                  
                
              
              
                
                =
                
                  
                    1
                    B
                  
                
                
                  ∑
                  
                    b
                    =
                    1
                  
                  
                    B
                  
                
                
                  x
                  
                    (
                    b
                    )
                    ,
                    i
                  
                  
                    (
                    l
                    )
                  
                
              
            
            
              
                (
                
                  σ
                  
                    i
                  
                  
                    (
                    l
                    )
                  
                
                
                  )
                  
                    2
                  
                
              
              
                
                =
                
                  
                    1
                    B
                  
                
                
                  ∑
                  
                    b
                    =
                    1
                  
                  
                    B
                  
                
                (
                
                  x
                  
                    (
                    b
                    )
                    ,
                    i
                  
                  
                    (
                    l
                    )
                  
                
                −
                
                  μ
                  
                    i
                  
                  
                    (
                    l
                    )
                  
                
                
                  )
                  
                    2
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\mu _{i}^{(l)}&={\frac {1}{B}}\sum _{b=1}^{B}x_{(b),i}^{(l)}\\(\sigma _{i}^{(l)})^{2}&={\frac {1}{B}}\sum _{b=1}^{B}(x_{(b),i}^{(l)}-\mu _{i}^{(l)})^{2}\end{aligned}}}
  

where 
  
    
      
        i
      
    
    {\displaystyle i}
  
 indexes the coordinates of the vectors, and 
  
    
      
        b
      
    
    {\displaystyle b}
  
 indexes the elements of the batch. In other words, we are considering the 
  
    
      
        i
      
    
    {\displaystyle i}
  
-th coordinate of each vector in the batch, and computing the mean and variance of these numbers.
It then normalizes each coordinate to have zero mean and unit variance:

  
    
      
        
          
            
              
                x
                ^
              
            
          
          
            (
            b
            )
            ,
            i
          
          
            (
            l
            )
          
        
        =
        
          
            
              
                x
                
                  (
                  b
                  )
                  ,
                  i
                
                
                  (
                  l
                  )
                
              
              −
              
                μ
                
                  i
                
                
                  (
                  l
                  )
                
              
            
            
              (
              
                σ
                
                  i
                
                
                  (
                  l
                  )
                
              
              
                )
                
                  2
                
              
              +
              ϵ
            
          
        
      
    
    {\displaystyle {\hat {x}}_{(b),i}^{(l)}={\frac {x_{(b),i}^{(l)}-\mu _{i}^{(l)}}{\sqrt {(\sigma _{i}^{(l)})^{2}+\epsilon }}}}
  

The 
  
    
      
        ϵ
      
    
    {\displaystyle \epsilon }
  
 is a small positive constant such as 
  
    
      
        
          10
          
            −
            9
          
        
      
    
    {\displaystyle 10^{-9}}
  
 added to the variance for numerical stability, to avoid division by zero.
Finally, it applies a linear transformation:

  
    
      
        
          y
          
            (
            b
            )
            ,
            i
          
          
            (
            l
            )
          
        
        =
        
          γ
          
            i
          
        
        
          
            
              
                x
                ^
              
            
          
          
            (
            b
            )
            ,
            i
          
          
            (
            l
            )
          
        
        +
        
          β
          
            i
          
        
      
    
    {\displaystyle y_{(b),i}^{(l)}=\gamma _{i}{\hat {x}}_{(b),i}^{(l)}+\beta _{i}}
  

Here, 
  
    
      
        γ
      
    
    {\displaystyle \gamma }
  
 and 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
 are parameters inside the BatchNorm module. They are learnable parameters, typically trained by gradient descent.
The following is a Python implementation of BatchNorm:

Interpretation
γ
      
    
    {\displaystyle \gamma }
  
 and 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
 allow the network to learn to undo the normalization, if this is beneficial. BatchNorm can be interpreted as removing the purely linear transformations, so that its layers focus solely on modelling the nonlinear aspects of data, which may be beneficial, as a neural network can always be augmented with a linear transformation layer on top.
It is claimed in the original publication that BatchNorm works by reducing internal covariance shift, though the claim has both supporters and detractors.

Special cases
The original paper recommended to only use BatchNorms after a linear transform, not after a nonlinear activation. That is, 
  
    
      
        ϕ
        (
        
          B
          N
        
        (
        W
        x
        +
        b
        )
        )
      
    
    {\displaystyle \phi (\mathrm {BN} (Wx+b))}
  
, not 
  
    
      
        
          B
          N
        
        (
        ϕ
        (
        W
        x
        +
        b
        )
        )
      
    
    {\displaystyle \mathrm {BN} (\phi (Wx+b))}
  
. Also, the bias 
  
    
      
        b
      
    
    {\displaystyle b}
  
 does not matter, since it would be canceled by the subsequent mean subtraction, so it is of the form 
  
    
      
        
          B
          N
        
        (
        W
        x
        )
      
    
    {\displaystyle \mathrm {BN} (Wx)}
  
. That is, if a BatchNorm is preceded by a linear transform, then that linear transform's bias term is set to zero.
For convolutional neural networks (CNNs), BatchNorm must preserve the translation-invariance of these models, meaning that it must treat all outputs of the same kernel as if they are different data points within a batch. This is sometimes called Spatial BatchNorm, or BatchNorm2D, or per-channel BatchNorm.
Concretely, suppose we have a 2-dimensional convolutional layer defined by:

  
    
      
        
          x
          
            h
            ,
            w
            ,
            c
          
          
            (
            l
            )
          
        
        =
        
          ∑
          
            
              h
              ′
            
            ,
            
              w
              ′
            
            ,
            
              c
              ′
            
          
        
        
          K
          
            
              h
              ′
            
            −
            h
            ,
            
              w
              ′
            
            −
            w
            ,
            c
            ,
            
              c
              ′
            
          
          
            (
            l
            )
          
        
        
          x
          
            
              h
              ′
            
            ,
            
              w
              ′
            
            ,
            
              c
              ′
            
          
          
            (
            l
            −
            1
            )
          
        
        +
        
          b
          
            c
          
          
            (
            l
            )
          
        
      
    
    {\displaystyle x_{h,w,c}^{(l)}=\sum _{h',w',c'}K_{h'-h,w'-w,c,c'}^{(l)}x_{h',w',c'}^{(l-1)}+b_{c}^{(l)}}
  

where:

  
    
      
        
          x
          
            h
            ,
            w
            ,
            c
          
          
            (
            l
            )
          
        
      
    
    {\displaystyle x_{h,w,c}^{(l)}}
  
 is the activation of the neuron at position 
  
    
      
        (
        h
        ,
        w
        )
      
    
    {\displaystyle (h,w)}
  
 in the 
  
    
      
        c
      
    
    {\displaystyle c}
  
-th channel of the 
  
    
      
        l
      
    
    {\displaystyle l}
  
-th layer.

  
    
      
        
          K
          
            Δ
            h
            ,
            Δ
            w
            ,
            c
            ,
            
              c
              ′
            
          
          
            (
            l
            )
          
        
      
    
    {\displaystyle K_{\Delta h,\Delta w,c,c'}^{(l)}}
  
 is a kernel tensor. Each channel 
  
    
      
        c
      
    
    {\displaystyle c}
  
 corresponds to a kernel 
  
    
      
        
          K
          
            
              h
              ′
            
            −
            h
            ,
            
              w
              ′
            
            −
            w
            ,
            c
            ,
            
              c
              ′
            
          
          
            (
            l
            )
          
        
      
    
    {\displaystyle K_{h'-h,w'-w,c,c'}^{(l)}}
  
, with indices 
  
    
      
        Δ
        h
        ,
        Δ
        w
        ,
        
          c
          ′
        
      
    
    {\displaystyle \Delta h,\Delta w,c'}
  
.

  
    
      
        
          b
          
            c
          
          
            (
            l
            )
          
        
      
    
    {\displaystyle b_{c}^{(l)}}
  
 is the bias term for the 
  
    
      
        c
      
    
    {\displaystyle c}
  
-th channel of the 
  
    
      
        l
      
    
    {\displaystyle l}
  
-th layer.
In order to preserve the translational invariance, BatchNorm treats all outputs from the same kernel in the same batch as more data in a batch. That is, it is applied once per kernel 
  
    
      
        c
      
    
    {\displaystyle c}
  
 (equivalently, once per channel 
  
    
      
        c
      
    
    {\displaystyle c}
  
), not per activation 
  
    
      
        
          x
          
            h
            ,
            w
            ,
            c
          
          
            (
            l
            +
            1
            )
          
        
      
    
    {\displaystyle x_{h,w,c}^{(l+1)}}
  
:

  
    
      
        
          
            
              
                
                  μ
                  
                    c
                  
                  
                    (
                    l
                    )
                  
                
              
              
                
                =
                
                  
                    1
                    
                      B
                      H
                      W
                    
                  
                
                
                  ∑
                  
                    b
                    =
                    1
                  
                  
                    B
                  
                
                
                  ∑
                  
                    h
                    =
                    1
                  
                  
                    H
                  
                
                
                  ∑
                  
                    w
                    =
                    1
                  
                  
                    W
                  
                
                
                  x
                  
                    (
                    b
                    )
                    ,
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
              
            
            
              
                (
                
                  σ
                  
                    c
                  
                  
                    (
                    l
                    )
                  
                
                
                  )
                  
                    2
                  
                
              
              
                
                =
                
                  
                    1
                    
                      B
                      H
                      W
                    
                  
                
                
                  ∑
                  
                    b
                    =
                    1
                  
                  
                    B
                  
                
                
                  ∑
                  
                    h
                    =
                    1
                  
                  
                    H
                  
                
                
                  ∑
                  
                    w
                    =
                    1
                  
                  
                    W
                  
                
                (
                
                  x
                  
                    (
                    b
                    )
                    ,
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
                −
                
                  μ
                  
                    c
                  
                  
                    (
                    l
                    )
                  
                
                
                  )
                  
                    2
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\mu _{c}^{(l)}&={\frac {1}{BHW}}\sum _{b=1}^{B}\sum _{h=1}^{H}\sum _{w=1}^{W}x_{(b),h,w,c}^{(l)}\\(\sigma _{c}^{(l)})^{2}&={\frac {1}{BHW}}\sum _{b=1}^{B}\sum _{h=1}^{H}\sum _{w=1}^{W}(x_{(b),h,w,c}^{(l)}-\mu _{c}^{(l)})^{2}\end{aligned}}}
  

where 
  
    
      
        B
      
    
    {\displaystyle B}
  
 is the batch size, 
  
    
      
        H
      
    
    {\displaystyle H}
  
 is the height of the feature map, and 
  
    
      
        W
      
    
    {\displaystyle W}
  
 is the width of the feature map.
That is, even though there are only 
  
    
      
        B
      
    
    {\displaystyle B}
  
 data points in a batch, all 
  
    
      
        B
        H
        W
      
    
    {\displaystyle BHW}
  
 outputs from the kernel in this batch are treated equally.
Subsequently, normalization and the linear transform is also done per kernel:

  
    
      
        
          
            
              
                
                  
                    
                      
                        x
                        ^
                      
                    
                  
                  
                    (
                    b
                    )
                    ,
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
              
              
                
                =
                
                  
                    
                      
                        x
                        
                          (
                          b
                          )
                          ,
                          h
                          ,
                          w
                          ,
                          c
                        
                        
                          (
                          l
                          )
                        
                      
                      −
                      
                        μ
                        
                          c
                        
                        
                          (
                          l
                          )
                        
                      
                    
                    
                      (
                      
                        σ
                        
                          c
                        
                        
                          (
                          l
                          )
                        
                      
                      
                        )
                        
                          2
                        
                      
                      +
                      ϵ
                    
                  
                
              
            
            
              
                
                  y
                  
                    (
                    b
                    )
                    ,
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
              
              
                
                =
                
                  γ
                  
                    c
                  
                
                
                  
                    
                      
                        x
                        ^
                      
                    
                  
                  
                    (
                    b
                    )
                    ,
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
                +
                
                  β
                  
                    c
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\hat {x}}_{(b),h,w,c}^{(l)}&={\frac {x_{(b),h,w,c}^{(l)}-\mu _{c}^{(l)}}{\sqrt {(\sigma _{c}^{(l)})^{2}+\epsilon }}}\\y_{(b),h,w,c}^{(l)}&=\gamma _{c}{\hat {x}}_{(b),h,w,c}^{(l)}+\beta _{c}\end{aligned}}}
  

Similar considerations apply for BatchNorm for n-dimensional convolutions.
The following is a Python implementation of BatchNorm for 2D convolutions:

Improvements
BatchNorm has been very popular and there were many attempted improvements. Some examples include:

ghost batching: randomly partition a batch into sub-batches and perform BatchNorm separately on each;
weight decay on 
  
    
      
        γ
      
    
    {\displaystyle \gamma }
  
 and 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
;
and combining BatchNorm with GroupNorm.
A particular problem with BatchNorm is that during training, the mean and variance are calculated on the fly for each batch (usually as an exponential moving average), but during inference, the mean and variance were frozen from those calculated during training. This train-test disparity degrades performance. The disparity can be decreased by simulating the moving average during inference:: Eq. 3 

  
    
      
        
          
            
              
                μ
              
              
                
                =
                α
                E
                [
                x
                ]
                +
                (
                1
                −
                α
                )
                
                  μ
                  
                    x
                    ,
                    
                       train
                    
                  
                
              
            
            
              
                
                  σ
                  
                    2
                  
                
              
              
                
                =
                (
                α
                E
                [
                x
                
                  ]
                  
                    2
                  
                
                +
                (
                1
                −
                α
                )
                
                  μ
                  
                    
                      x
                      
                        2
                      
                    
                    ,
                    
                       train
                    
                  
                
                )
                −
                
                  μ
                  
                    2
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\mu &=\alpha E[x]+(1-\alpha )\mu _{x,{\text{ train}}}\\\sigma ^{2}&=(\alpha E[x]^{2}+(1-\alpha )\mu _{x^{2},{\text{ train}}})-\mu ^{2}\end{aligned}}}
  

where 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 is a hyperparameter to be optimized on a validation set.
Other works attempt to eliminate BatchNorm, such as the Normalizer-Free ResNet.

Layer normalization
Layer normalization (LayerNorm) is a popular alternative to BatchNorm. Unlike BatchNorm, which normalizes activations across the batch dimension for a given feature, LayerNorm normalizes across all the features within a single data sample. Compared to BatchNorm, LayerNorm's performance is not affected by batch size. It is a key component of transformer models.
For a given data input and layer, LayerNorm computes the mean 
  
    
      
        μ
      
    
    {\displaystyle \mu }
  
 and variance 
  
    
      
        
          σ
          
            2
          
        
      
    
    {\displaystyle \sigma ^{2}}
  
 over all the neurons in the layer. Similar to BatchNorm, learnable parameters 
  
    
      
        γ
      
    
    {\displaystyle \gamma }
  
 (scale) and 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
 (shift) are applied. It is defined by:

  
    
      
        
          
            
              
                x
                
                  i
                
              
              ^
            
          
        
        =
        
          
            
              
                x
                
                  i
                
              
              −
              μ
            
            
              
                σ
                
                  2
                
              
              +
              ϵ
            
          
        
        ,
        
        
          y
          
            i
          
        
        =
        
          γ
          
            i
          
        
        
          
            
              
                x
                
                  i
                
              
              ^
            
          
        
        +
        
          β
          
            i
          
        
      
    
    {\displaystyle {\hat {x_{i}}}={\frac {x_{i}-\mu }{\sqrt {\sigma ^{2}+\epsilon }}},\quad y_{i}=\gamma _{i}{\hat {x_{i}}}+\beta _{i}}
  

where:

  
    
      
        μ
        =
        
          
            1
            D
          
        
        
          ∑
          
            i
            =
            1
          
          
            D
          
        
        
          x
          
            i
          
        
        ,
        
        
          σ
          
            2
          
        
        =
        
          
            1
            D
          
        
        
          ∑
          
            i
            =
            1
          
          
            D
          
        
        (
        
          x
          
            i
          
        
        −
        μ
        
          )
          
            2
          
        
      
    
    {\displaystyle \mu ={\frac {1}{D}}\sum _{i=1}^{D}x_{i},\quad \sigma ^{2}={\frac {1}{D}}\sum _{i=1}^{D}(x_{i}-\mu )^{2}}
  

and the index 
  
    
      
        i
      
    
    {\displaystyle i}
  
 ranges over the neurons in that layer.

Examples
For example, in CNN, a LayerNorm applies to all activations in a layer. In the previous notation, we have:

  
    
      
        
          
            
              
                
                  μ
                  
                    (
                    l
                    )
                  
                
              
              
                
                =
                
                  
                    1
                    
                      H
                      W
                      C
                    
                  
                
                
                  ∑
                  
                    h
                    =
                    1
                  
                  
                    H
                  
                
                
                  ∑
                  
                    w
                    =
                    1
                  
                  
                    W
                  
                
                
                  ∑
                  
                    c
                    =
                    1
                  
                  
                    C
                  
                
                
                  x
                  
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
              
            
            
              
                (
                
                  σ
                  
                    (
                    l
                    )
                  
                
                
                  )
                  
                    2
                  
                
              
              
                
                =
                
                  
                    1
                    
                      H
                      W
                      C
                    
                  
                
                
                  ∑
                  
                    h
                    =
                    1
                  
                  
                    H
                  
                
                
                  ∑
                  
                    w
                    =
                    1
                  
                  
                    W
                  
                
                
                  ∑
                  
                    c
                    =
                    1
                  
                  
                    C
                  
                
                (
                
                  x
                  
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
                −
                
                  μ
                  
                    (
                    l
                    )
                  
                
                
                  )
                  
                    2
                  
                
              
            
            
              
                
                  
                    
                      
                        x
                        ^
                      
                    
                  
                  
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
              
              
                
                =
                
                  
                    
                      
                        
                          
                            
                              x
                              ^
                            
                          
                        
                        
                          h
                          ,
                          w
                          ,
                          c
                        
                        
                          (
                          l
                          )
                        
                      
                      −
                      
                        μ
                        
                          (
                          l
                          )
                        
                      
                    
                    
                      (
                      
                        σ
                        
                          (
                          l
                          )
                        
                      
                      
                        )
                        
                          2
                        
                      
                      +
                      ϵ
                    
                  
                
              
            
            
              
                
                  y
                  
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
              
              
                
                =
                
                  γ
                  
                    (
                    l
                    )
                  
                
                
                  
                    
                      
                        x
                        ^
                      
                    
                  
                  
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
                +
                
                  β
                  
                    (
                    l
                    )
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\mu ^{(l)}&={\frac {1}{HWC}}\sum _{h=1}^{H}\sum _{w=1}^{W}\sum _{c=1}^{C}x_{h,w,c}^{(l)}\\(\sigma ^{(l)})^{2}&={\frac {1}{HWC}}\sum _{h=1}^{H}\sum _{w=1}^{W}\sum _{c=1}^{C}(x_{h,w,c}^{(l)}-\mu ^{(l)})^{2}\\{\hat {x}}_{h,w,c}^{(l)}&={\frac {{\hat {x}}_{h,w,c}^{(l)}-\mu ^{(l)}}{\sqrt {(\sigma ^{(l)})^{2}+\epsilon }}}\\y_{h,w,c}^{(l)}&=\gamma ^{(l)}{\hat {x}}_{h,w,c}^{(l)}+\beta ^{(l)}\end{aligned}}}
  

Notice that the batch index 
  
    
      
        b
      
    
    {\displaystyle b}
  
 is removed, while the channel index 
  
    
      
        c
      
    
    {\displaystyle c}
  
 is added.
In recurrent neural networks and transformers, LayerNorm is applied individually to each timestep. For example, if the hidden vector in an RNN at timestep 
  
    
      
        t
      
    
    {\displaystyle t}
  
 is 
  
    
      
        
          x
          
            (
            t
            )
          
        
        ∈
        
          
            R
          
          
            D
          
        
      
    
    {\displaystyle x^{(t)}\in \mathbb {R} ^{D}}
  
, where 
  
    
      
        D
      
    
    {\displaystyle D}
  
 is the dimension of the hidden vector, then LayerNorm will be applied with:

  
    
      
        
          
            
              
                
                  x
                  
                    i
                  
                
                ^
              
            
          
          
            (
            t
            )
          
        
        =
        
          
            
              
                x
                
                  i
                
                
                  (
                  t
                  )
                
              
              −
              
                μ
                
                  (
                  t
                  )
                
              
            
            
              (
              
                σ
                
                  (
                  t
                  )
                
              
              
                )
                
                  2
                
              
              +
              ϵ
            
          
        
        ,
        
        
          y
          
            i
          
          
            (
            t
            )
          
        
        =
        
          γ
          
            i
          
        
        
          
            
              
                
                  x
                  
                    i
                  
                
                ^
              
            
          
          
            (
            t
            )
          
        
        +
        
          β
          
            i
          
        
      
    
    {\displaystyle {\hat {x_{i}}}^{(t)}={\frac {x_{i}^{(t)}-\mu ^{(t)}}{\sqrt {(\sigma ^{(t)})^{2}+\epsilon }}},\quad y_{i}^{(t)}=\gamma _{i}{\hat {x_{i}}}^{(t)}+\beta _{i}}
  

where:

  
    
      
        
          μ
          
            (
            t
            )
          
        
        =
        
          
            1
            D
          
        
        
          ∑
          
            i
            =
            1
          
          
            D
          
        
        
          x
          
            i
          
          
            (
            t
            )
          
        
        ,
        
        (
        
          σ
          
            (
            t
            )
          
        
        
          )
          
            2
          
        
        =
        
          
            1
            D
          
        
        
          ∑
          
            i
            =
            1
          
          
            D
          
        
        (
        
          x
          
            i
          
          
            (
            t
            )
          
        
        −
        
          μ
          
            (
            t
            )
          
        
        
          )
          
            2
          
        
      
    
    {\displaystyle \mu ^{(t)}={\frac {1}{D}}\sum _{i=1}^{D}x_{i}^{(t)},\quad (\sigma ^{(t)})^{2}={\frac {1}{D}}\sum _{i=1}^{D}(x_{i}^{(t)}-\mu ^{(t)})^{2}}

Root mean square layer normalization
Root mean square layer normalization (RMSNorm) changes LayerNorm by:

  
    
      
        
          
            
              
                x
                
                  i
                
              
              ^
            
          
        
        =
        
          
            
              x
              
                i
              
            
            
              
                
                  1
                  D
                
              
              
                ∑
                
                  i
                  =
                  1
                
                
                  D
                
              
              
                x
                
                  i
                
                
                  2
                
              
            
          
        
        ,
        
        
          y
          
            i
          
        
        =
        γ
        
          
            
              
                x
                
                  i
                
              
              ^
            
          
        
        +
        β
      
    
    {\displaystyle {\hat {x_{i}}}={\frac {x_{i}}{\sqrt {{\frac {1}{D}}\sum _{i=1}^{D}x_{i}^{2}}}},\quad y_{i}=\gamma {\hat {x_{i}}}+\beta }
  

Essentially, it is LayerNorm where we enforce 
  
    
      
        μ
        ,
        ϵ
        =
        0
      
    
    {\displaystyle \mu ,\epsilon =0}
  
.

Adaptive
Adaptive layer norm (adaLN) computes the 
  
    
      
        γ
        ,
        β
      
    
    {\displaystyle \gamma ,\beta }
  
 in a LayerNorm not from the layer activation itself, but from other data. It was first proposed for CNNs, and has been used effectively in diffusion transformers (DiTs). For example, in a DiT, the conditioning information (such as a text encoding vector) is processed by a multilayer perceptron into 
  
    
      
        γ
        ,
        β
      
    
    {\displaystyle \gamma ,\beta }
  
, which is then applied in the LayerNorm module of a transformer.

Weight normalization
Weight normalization (WeightNorm) is a technique inspired by BatchNorm that normalizes weight matrices in a neural network, rather than its activations.
One example is spectral normalization, which divides weight matrices by their spectral norm. The spectral normalization is used in generative adversarial networks (GANs) such as the Wasserstein GAN. The spectral radius can be efficiently computed by the following algorithm:

INPUT matrix 
  
    
      
        W
      
    
    {\displaystyle W}
  
 and initial guess 
  
    
      
        x
      
    
    {\displaystyle x}
  

Iterate 
  
    
      
        x
        ↦
        
          
            1
            
              ‖
              W
              x
              
                ‖
                
                  2
                
              
            
          
        
        W
        x
      
    
    {\displaystyle x\mapsto {\frac {1}{\|Wx\|_{2}}}Wx}
  
 to convergence 
  
    
      
        
          x
          
            ∗
          
        
      
    
    {\displaystyle x^{*}}
  
. This is the eigenvector of 
  
    
      
        W
      
    
    {\displaystyle W}
  
 with eigenvalue 
  
    
      
        ‖
        W
        
          ‖
          
            s
          
        
      
    
    {\displaystyle \|W\|_{s}}
  
.

RETURN 
  
    
      
        
          x
          
            ∗
          
        
        ,
        ‖
        W
        
          x
          
            ∗
          
        
        
          ‖
          
            2
          
        
      
    
    {\displaystyle x^{*},\|Wx^{*}\|_{2}}
  

By reassigning 
  
    
      
        
          W
          
            i
          
        
        ←
        
          
            
              W
              
                i
              
            
            
              ‖
              
                W
                
                  i
                
              
              
                ‖
                
                  s
                
              
            
          
        
      
    
    {\displaystyle W_{i}\leftarrow {\frac {W_{i}}{\|W_{i}\|_{s}}}}
  
 after each update of the discriminator, we can upper-bound 
  
    
      
        ‖
        
          W
          
            i
          
        
        
          ‖
          
            s
          
        
        ≤
        1
      
    
    {\displaystyle \|W_{i}\|_{s}\leq 1}
  
, and thus upper-bound 
  
    
      
        ‖
        D
        
          ‖
          
            L
          
        
      
    
    {\displaystyle \|D\|_{L}}
  
.
The algorithm can be further accelerated by memoization: at step 
  
    
      
        t
      
    
    {\displaystyle t}
  
, store 
  
    
      
        
          x
          
            i
          
          
            ∗
          
        
        (
        t
        )
      
    
    {\displaystyle x_{i}^{*}(t)}
  
. Then, at step 
  
    
      
        t
        +
        1
      
    
    {\displaystyle t+1}
  
, use 
  
    
      
        
          x
          
            i
          
          
            ∗
          
        
        (
        t
        )
      
    
    {\displaystyle x_{i}^{*}(t)}
  
 as the initial guess for the algorithm. Since 
  
    
      
        
          W
          
            i
          
        
        (
        t
        +
        1
        )
      
    
    {\displaystyle W_{i}(t+1)}
  
 is very close to 
  
    
      
        
          W
          
            i
          
        
        (
        t
        )
      
    
    {\displaystyle W_{i}(t)}
  
, so is 
  
    
      
        
          x
          
            i
          
          
            ∗
          
        
        (
        t
        )
      
    
    {\displaystyle x_{i}^{*}(t)}
  
 to 
  
    
      
        
          x
          
            i
          
          
            ∗
          
        
        (
        t
        +
        1
        )
      
    
    {\displaystyle x_{i}^{*}(t+1)}
  
, thus allowing rapid convergence.

CNN-specific normalization
There are some activation normalization techniques that are only used for CNNs.

Response normalization
Local response normalization was used in AlexNet. It was applied in a convolutional layer, just after a nonlinear activation function. It was defined by:

  
    
      
        
          b
          
            x
            ,
            y
          
          
            i
          
        
        =
        
          
            
              a
              
                x
                ,
                y
              
              
                i
              
            
            
              
                (
                
                  k
                  +
                  α
                  
                    ∑
                    
                      j
                      =
                      max
                      (
                      0
                      ,
                      i
                      −
                      n
                      
                        /
                      
                      2
                      )
                    
                    
                      min
                      (
                      N
                      −
                      1
                      ,
                      i
                      +
                      n
                      
                        /
                      
                      2
                      )
                    
                  
                  
                    
                      (
                      
                        a
                        
                          x
                          ,
                          y
                        
                        
                          j
                        
                      
                      )
                    
                    
                      2
                    
                  
                
                )
              
              
                β
              
            
          
        
      
    
    {\displaystyle b_{x,y}^{i}={\frac {a_{x,y}^{i}}{\left(k+\alpha \sum _{j=\max(0,i-n/2)}^{\min(N-1,i+n/2)}\left(a_{x,y}^{j}\right)^{2}\right)^{\beta }}}}
  

where 
  
    
      
        
          a
          
            x
            ,
            y
          
          
            i
          
        
      
    
    {\displaystyle a_{x,y}^{i}}
  
 is the activation of the neuron at location 
  
    
      
        (
        x
        ,
        y
        )
      
    
    {\displaystyle (x,y)}
  
 and channel 
  
    
      
        i
      
    
    {\displaystyle i}
  
. I.e., each pixel in a channel is suppressed by the activations of the same pixel in its adjacent channels.

  
    
      
        k
        ,
        n
        ,
        α
        ,
        β
      
    
    {\displaystyle k,n,\alpha ,\beta }
  
 are hyperparameters picked by using a validation set.
It was a variant of the earlier local contrast normalization.

  
    
      
        
          b
          
            x
            ,
            y
          
          
            i
          
        
        =
        
          
            
              a
              
                x
                ,
                y
              
              
                i
              
            
            
              
                (
                
                  k
                  +
                  α
                  
                    ∑
                    
                      j
                      =
                      max
                      (
                      0
                      ,
                      i
                      −
                      n
                      
                        /
                      
                      2
                      )
                    
                    
                      min
                      (
                      N
                      −
                      1
                      ,
                      i
                      +
                      n
                      
                        /
                      
                      2
                      )
                    
                  
                  
                    
                      (
                      
                        
                          a
                          
                            x
                            ,
                            y
                          
                          
                            j
                          
                        
                        −
                        
                          
                            
                              
                                a
                                ¯
                              
                            
                          
                          
                            x
                            ,
                            y
                          
                          
                            j
                          
                        
                      
                      )
                    
                    
                      2
                    
                  
                
                )
              
              
                β
              
            
          
        
      
    
    {\displaystyle b_{x,y}^{i}={\frac {a_{x,y}^{i}}{\left(k+\alpha \sum _{j=\max(0,i-n/2)}^{\min(N-1,i+n/2)}\left(a_{x,y}^{j}-{\bar {a}}_{x,y}^{j}\right)^{2}\right)^{\beta }}}}
  

where 
  
    
      
        
          
            
              
                a
                ¯
              
            
          
          
            x
            ,
            y
          
          
            j
          
        
      
    
    {\displaystyle {\bar {a}}_{x,y}^{j}}
  
 is the average activation in a small window centered on location 
  
    
      
        (
        x
        ,
        y
        )
      
    
    {\displaystyle (x,y)}
  
 and channel 
  
    
      
        i
      
    
    {\displaystyle i}
  
. The hyperparameters 
  
    
      
        k
        ,
        n
        ,
        α
        ,
        β
      
    
    {\displaystyle k,n,\alpha ,\beta }
  
, and the size of the small window, are picked by using a validation set.
Similar methods were called divisive normalization, as they divide activations by a number depending on the activations. They were originally inspired by biology, where it was used to explain nonlinear responses of cortical neurons and nonlinear masking in visual perception.
Both kinds of local normalization were obviated by batch normalization, which is a more global form of normalization.
Response normalization reappeared in ConvNeXT-2 as global response normalization.

Group normalization
Group normalization (GroupNorm) is a technique also solely used for CNNs. It can be understood as the LayerNorm for CNN applied once per channel group.
Suppose at a layer 
  
    
      
        l
      
    
    {\displaystyle l}
  
, there are channels 
  
    
      
        1
        ,
        2
        ,
        …
        ,
        C
      
    
    {\displaystyle 1,2,\dots ,C}
  
, then it is partitioned into groups 
  
    
      
        
          g
          
            1
          
        
        ,
        
          g
          
            2
          
        
        ,
        …
        ,
        
          g
          
            G
          
        
      
    
    {\displaystyle g_{1},g_{2},\dots ,g_{G}}
  
. Then, LayerNorm is applied to each group.

Instance normalization
Instance normalization (InstanceNorm), or contrast normalization, is a technique first developed for neural style transfer, and is also only used for CNNs. It can be understood as the LayerNorm for CNN applied once per channel, or equivalently, as group normalization where each group consists of a single channel:

  
    
      
        
          
            
              
                
                  μ
                  
                    c
                  
                  
                    (
                    l
                    )
                  
                
              
              
                
                =
                
                  
                    1
                    
                      H
                      W
                    
                  
                
                
                  ∑
                  
                    h
                    =
                    1
                  
                  
                    H
                  
                
                
                  ∑
                  
                    w
                    =
                    1
                  
                  
                    W
                  
                
                
                  x
                  
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
              
            
            
              
                (
                
                  σ
                  
                    c
                  
                  
                    (
                    l
                    )
                  
                
                
                  )
                  
                    2
                  
                
              
              
                
                =
                
                  
                    1
                    
                      H
                      W
                    
                  
                
                
                  ∑
                  
                    h
                    =
                    1
                  
                  
                    H
                  
                
                
                  ∑
                  
                    w
                    =
                    1
                  
                  
                    W
                  
                
                (
                
                  x
                  
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
                −
                
                  μ
                  
                    c
                  
                  
                    (
                    l
                    )
                  
                
                
                  )
                  
                    2
                  
                
              
            
            
              
                
                  
                    
                      
                        x
                        ^
                      
                    
                  
                  
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
              
              
                
                =
                
                  
                    
                      
                        
                          
                            
                              x
                              ^
                            
                          
                        
                        
                          h
                          ,
                          w
                          ,
                          c
                        
                        
                          (
                          l
                          )
                        
                      
                      −
                      
                        μ
                        
                          c
                        
                        
                          (
                          l
                          )
                        
                      
                    
                    
                      (
                      
                        σ
                        
                          c
                        
                        
                          (
                          l
                          )
                        
                      
                      
                        )
                        
                          2
                        
                      
                      +
                      ϵ
                    
                  
                
              
            
            
              
                
                  y
                  
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
              
              
                
                =
                
                  γ
                  
                    c
                  
                  
                    (
                    l
                    )
                  
                
                
                  
                    
                      
                        x
                        ^
                      
                    
                  
                  
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                  
                
                +
                
                  β
                  
                    c
                  
                  
                    (
                    l
                    )
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\mu _{c}^{(l)}&={\frac {1}{HW}}\sum _{h=1}^{H}\sum _{w=1}^{W}x_{h,w,c}^{(l)}\\(\sigma _{c}^{(l)})^{2}&={\frac {1}{HW}}\sum _{h=1}^{H}\sum _{w=1}^{W}(x_{h,w,c}^{(l)}-\mu _{c}^{(l)})^{2}\\{\hat {x}}_{h,w,c}^{(l)}&={\frac {{\hat {x}}_{h,w,c}^{(l)}-\mu _{c}^{(l)}}{\sqrt {(\sigma _{c}^{(l)})^{2}+\epsilon }}}\\y_{h,w,c}^{(l)}&=\gamma _{c}^{(l)}{\hat {x}}_{h,w,c}^{(l)}+\beta _{c}^{(l)}\end{aligned}}}

Adaptive instance normalization
Adaptive instance normalization (AdaIN) is a variant of instance normalization, designed specifically for neural style transfer with CNNs, rather than just CNNs in general.
In the AdaIN method of style transfer, we take a CNN and two input images, one for content and one for style. Each image is processed through the same CNN, and at a certain layer 
  
    
      
        l
      
    
    {\displaystyle l}
  
, AdaIn is applied.
Let 
  
    
      
        
          x
          
            (
            l
            )
            ,
            
               content
            
          
        
      
    
    {\displaystyle x^{(l),{\text{ content}}}}
  
 be the activation in the content image, and 
  
    
      
        
          x
          
            (
            l
            )
            ,
            
               style
            
          
        
      
    
    {\displaystyle x^{(l),{\text{ style}}}}
  
 be the activation in the style image. Then, AdaIn first computes the mean and variance of the activations of the content image 
  
    
      
        
          x
          
            ′
            
              (
              l
              )
            
          
        
      
    
    {\displaystyle x'^{(l)}}
  
, then uses those as the 
  
    
      
        γ
        ,
        β
      
    
    {\displaystyle \gamma ,\beta }
  
 for InstanceNorm on 
  
    
      
        
          x
          
            (
            l
            )
            ,
            
               content
            
          
        
      
    
    {\displaystyle x^{(l),{\text{ content}}}}
  
. Note that 
  
    
      
        
          x
          
            (
            l
            )
            ,
            
               style
            
          
        
      
    
    {\displaystyle x^{(l),{\text{ style}}}}
  
 itself remains unchanged. Explicitly, we have:

  
    
      
        
          
            
              
                
                  y
                  
                    h
                    ,
                    w
                    ,
                    c
                  
                  
                    (
                    l
                    )
                    ,
                    
                       content
                    
                  
                
              
              
                
                =
                
                  σ
                  
                    c
                  
                  
                    (
                    l
                    )
                    ,
                    
                       style
                    
                  
                
                
                  (
                  
                    
                      
                        
                          x
                          
                            h
                            ,
                            w
                            ,
                            c
                          
                          
                            (
                            l
                            )
                            ,
                            
                               content
                            
                          
                        
                        −
                        
                          μ
                          
                            c
                          
                          
                            (
                            l
                            )
                            ,
                            
                               content
                            
                          
                        
                      
                      
                        (
                        
                          σ
                          
                            c
                          
                          
                            (
                            l
                            )
                            ,
                            
                               content
                            
                          
                        
                        
                          )
                          
                            2
                          
                        
                        +
                        ϵ
                      
                    
                  
                  )
                
                +
                
                  μ
                  
                    c
                  
                  
                    (
                    l
                    )
                    ,
                    
                       style
                    
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}y_{h,w,c}^{(l),{\text{ content}}}&=\sigma _{c}^{(l),{\text{ style}}}\left({\frac {x_{h,w,c}^{(l),{\text{ content}}}-\mu _{c}^{(l),{\text{ content}}}}{\sqrt {(\sigma _{c}^{(l),{\text{ content}}})^{2}+\epsilon }}}\right)+\mu _{c}^{(l),{\text{ style}}}\end{aligned}}}

Transformers
Some normalization methods were designed for use in transformers.
The original 2017 transformer used the "post-LN" configuration for its LayerNorms. It was difficult to train, and required careful hyperparameter tuning and a "warm-up" in learning rate, where it starts small and gradually increases. The pre-LN convention, proposed several times in 2018, was found to be easier to train, requiring no warm-up, leading to faster convergence.
FixNorm and ScaleNorm both normalize activation vectors in a transformer. The FixNorm method divides the output vectors from a transformer by their L2 norms, then multiplies by a learned parameter 
  
    
      
        g
      
    
    {\displaystyle g}
  
. The ScaleNorm replaces all LayerNorms inside a transformer by division with L2 norm, then multiplying by a learned parameter 
  
    
      
        
          g
          ′
        
      
    
    {\displaystyle g'}
  
 (shared by all ScaleNorm modules of a transformer). Query-Key normalization (QKNorm) normalizes query and key vectors to have unit L2 norm.
In nGPT, many vectors are normalized to have unit L2 norm: hidden state vectors, input and output embedding vectors, weight matrix columns, and query and key vectors.

Miscellaneous
Gradient normalization (GradNorm) normalizes gradient vectors during backpropagation.

See also
Data preprocessing
Feature scaling

References
Further reading
"Normalization Layers". labml.ai Deep Learning Paper Implementations. Retrieved 2024-08-07.

## Related Articles

### Internal Links

- [Action selection](https://en.wikipedia.org/wiki/Action_selection)
- [Activation function](https://en.wikipedia.org/wiki/Activation_function)
- [Active learning (machine learning)](https://en.wikipedia.org/wiki/Active_learning_(machine_learning))
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
- [Online machine learning](https://en.wikipedia.org/wiki/Online_machine_learning)
- [Batch normalization](https://en.wikipedia.org/wiki/Batch_normalization)
- [Bayesian network](https://en.wikipedia.org/wiki/Bayesian_network)
- [Bernard Widrow](https://en.wikipedia.org/wiki/Bernard_Widrow)
- [Bias–variance tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff)
- [Boltzmann machine](https://en.wikipedia.org/wiki/Boltzmann_machine)
- [Boosting (machine learning)](https://en.wikipedia.org/wiki/Boosting_(machine_learning))
- [Bootstrap aggregating](https://en.wikipedia.org/wiki/Bootstrap_aggregating)
- [CURE algorithm](https://en.wikipedia.org/wiki/CURE_algorithm)
- [Canonical correlation](https://en.wikipedia.org/wiki/Canonical_correlation)
- [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT)
- [Chinchilla (language model)](https://en.wikipedia.org/wiki/Chinchilla_(language_model))
- [Claude (language model)](https://en.wikipedia.org/wiki/Claude_(language_model))
- [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon)
- [Cliff Shaw](https://en.wikipedia.org/wiki/Cliff_Shaw)
- [Cluster analysis](https://en.wikipedia.org/wiki/Cluster_analysis)
- [Coefficient of determination](https://en.wikipedia.org/wiki/Coefficient_of_determination)
- [Computational learning theory](https://en.wikipedia.org/wiki/Computational_learning_theory)
- [Conditional random field](https://en.wikipedia.org/wiki/Conditional_random_field)
- [Conference on Neural Information Processing Systems](https://en.wikipedia.org/wiki/Conference_on_Neural_Information_Processing_Systems)
- [Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix)
- [Conjugate gradient method](https://en.wikipedia.org/wiki/Conjugate_gradient_method)
- [Convolution](https://en.wikipedia.org/wiki/Convolution)
- [Convolutional neural network](https://en.wikipedia.org/wiki/Convolutional_neural_network)
- [Crowdsourcing](https://en.wikipedia.org/wiki/Crowdsourcing)
- [Curriculum learning](https://en.wikipedia.org/wiki/Curriculum_learning)
- [DALL-E](https://en.wikipedia.org/wiki/DALL-E)
- [DBSCAN](https://en.wikipedia.org/wiki/DBSCAN)
- [Data augmentation](https://en.wikipedia.org/wiki/Data_augmentation)
- [Data cleansing](https://en.wikipedia.org/wiki/Data_cleansing)
- [Data mining](https://en.wikipedia.org/wiki/Data_mining)
- [Data preprocessing](https://en.wikipedia.org/wiki/Data_preprocessing)
- [David Silver (computer scientist)](https://en.wikipedia.org/wiki/David_Silver_(computer_scientist))
- [Decision tree learning](https://en.wikipedia.org/wiki/Decision_tree_learning)
- [DeepDream](https://en.wikipedia.org/wiki/DeepDream)
- [Deep learning](https://en.wikipedia.org/wiki/Deep_learning)
- [Deep learning speech synthesis](https://en.wikipedia.org/wiki/Deep_learning_speech_synthesis)
- [Demis Hassabis](https://en.wikipedia.org/wiki/Demis_Hassabis)
- [Density estimation](https://en.wikipedia.org/wiki/Density_estimation)
- [Differentiable neural computer](https://en.wikipedia.org/wiki/Differentiable_neural_computer)
- [Diffusion model](https://en.wikipedia.org/wiki/Diffusion_model)
- [Diffusion process](https://en.wikipedia.org/wiki/Diffusion_process)
- [Dimensionality reduction](https://en.wikipedia.org/wiki/Dimensionality_reduction)
- [Division by zero](https://en.wikipedia.org/wiki/Division_by_zero)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Double descent](https://en.wikipedia.org/wiki/Double_descent)
- [Dream Machine (text-to-video model)](https://en.wikipedia.org/wiki/Dream_Machine_(text-to-video_model))
- [ECML PKDD](https://en.wikipedia.org/wiki/ECML_PKDD)
- [Echo state network](https://en.wikipedia.org/wiki/Echo_state_network)
- [Electrochemical RAM](https://en.wikipedia.org/wiki/Electrochemical_RAM)
- [ElevenLabs](https://en.wikipedia.org/wiki/ElevenLabs)
- [Empirical risk minimization](https://en.wikipedia.org/wiki/Empirical_risk_minimization)
- [Ensemble learning](https://en.wikipedia.org/wiki/Ensemble_learning)
- [Expectation–maximization algorithm](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm)
- [Moving average](https://en.wikipedia.org/wiki/Moving_average)
- [Facial recognition system](https://en.wikipedia.org/wiki/Facial_recognition_system)
- [Factor analysis](https://en.wikipedia.org/wiki/Factor_analysis)
- [Feature (machine learning)](https://en.wikipedia.org/wiki/Feature_(machine_learning))
- [Feature engineering](https://en.wikipedia.org/wiki/Feature_engineering)
- [Feature learning](https://en.wikipedia.org/wiki/Feature_learning)
- [Feature scaling](https://en.wikipedia.org/wiki/Feature_scaling)
- [Feedforward neural network](https://en.wikipedia.org/wiki/Feedforward_neural_network)
- [Fei-Fei Li](https://en.wikipedia.org/wiki/Fei-Fei_Li)
- [Flux (text-to-image model)](https://en.wikipedia.org/wiki/Flux_(text-to-image_model))
- [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt)
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
- [GloVe](https://en.wikipedia.org/wiki/GloVe)
- [Glossary of artificial intelligence](https://en.wikipedia.org/wiki/Glossary_of_artificial_intelligence)
- [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent)
- [Grammar induction](https://en.wikipedia.org/wiki/Grammar_induction)
- [Graph neural network](https://en.wikipedia.org/wiki/Graph_neural_network)
- [Graphical model](https://en.wikipedia.org/wiki/Graphical_model)
- [Grok (chatbot)](https://en.wikipedia.org/wiki/Grok_(chatbot))
- [Hallucination (artificial intelligence)](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))
- [Handwriting recognition](https://en.wikipedia.org/wiki/Handwriting_recognition)
- [Herbert A. Simon](https://en.wikipedia.org/wiki/Herbert_A._Simon)
- [Hidden Markov model](https://en.wikipedia.org/wiki/Hidden_Markov_model)
- [Hidden layer](https://en.wikipedia.org/wiki/Hidden_layer)
- [Hierarchical clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering)
- [Highway network](https://en.wikipedia.org/wiki/Highway_network)
- [Huawei PanGu](https://en.wikipedia.org/wiki/Huawei_PanGu)
- [Human-in-the-loop](https://en.wikipedia.org/wiki/Human-in-the-loop)
- [Human image synthesis](https://en.wikipedia.org/wiki/Human_image_synthesis)
- [Hyperparameter (machine learning)](https://en.wikipedia.org/wiki/Hyperparameter_(machine_learning))
- [Hyperparameter optimization](https://en.wikipedia.org/wiki/Hyperparameter_optimization)
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
- [Independent component analysis](https://en.wikipedia.org/wiki/Independent_component_analysis)
- [International Conference on Learning Representations](https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations)
- [International Conference on Machine Learning](https://en.wikipedia.org/wiki/International_Conference_on_Machine_Learning)
- [International Joint Conference on Artificial Intelligence](https://en.wikipedia.org/wiki/International_Joint_Conference_on_Artificial_Intelligence)
- [Isolation forest](https://en.wikipedia.org/wiki/Isolation_forest)
- [John Hopfield](https://en.wikipedia.org/wiki/John_Hopfield)
- [John McCarthy (computer scientist)](https://en.wikipedia.org/wiki/John_McCarthy_(computer_scientist))
- [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann)
- [Joseph Weizenbaum](https://en.wikipedia.org/wiki/Joseph_Weizenbaum)
- [Journal of Machine Learning Research](https://en.wikipedia.org/wiki/Journal_of_Machine_Learning_Research)
- [Jürgen Schmidhuber](https://en.wikipedia.org/wiki/J%C3%BCrgen_Schmidhuber)
- [K-means clustering](https://en.wikipedia.org/wiki/K-means_clustering)
- [K-nearest neighbors algorithm](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
- [Kernel (image processing)](https://en.wikipedia.org/wiki/Kernel_(image_processing))
- [Kernel method](https://en.wikipedia.org/wiki/Kernel_method)
- [Kuaishou](https://en.wikipedia.org/wiki/Kuaishou)
- [LaMDA](https://en.wikipedia.org/wiki/LaMDA)
- [Language model](https://en.wikipedia.org/wiki/Language_model)
- [Large language model](https://en.wikipedia.org/wiki/Large_language_model)
- [Latent diffusion model](https://en.wikipedia.org/wiki/Latent_diffusion_model)
- [LeNet](https://en.wikipedia.org/wiki/LeNet)
- [Learning curve (machine learning)](https://en.wikipedia.org/wiki/Learning_curve_(machine_learning))
- [Learning rate](https://en.wikipedia.org/wiki/Learning_rate)
- [Learning to rank](https://en.wikipedia.org/wiki/Learning_to_rank)
- [Linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)
- [Linear regression](https://en.wikipedia.org/wiki/Linear_regression)
- [List of artificial intelligence companies](https://en.wikipedia.org/wiki/List_of_artificial_intelligence_companies)
- [List of artificial intelligence projects](https://en.wikipedia.org/wiki/List_of_artificial_intelligence_projects)
- [List of datasets for machine-learning research](https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research)
- [List of datasets in computer vision and image processing](https://en.wikipedia.org/wiki/List_of_datasets_in_computer_vision_and_image_processing)
- [Llama (language model)](https://en.wikipedia.org/wiki/Llama_(language_model))
- [Local outlier factor](https://en.wikipedia.org/wiki/Local_outlier_factor)
- [Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression)
- [Long short-term memory](https://en.wikipedia.org/wiki/Long_short-term_memory)
- [Loss functions for classification](https://en.wikipedia.org/wiki/Loss_functions_for_classification)
- [Lotfi A. Zadeh](https://en.wikipedia.org/wiki/Lotfi_A._Zadeh)
- [Machine Learning (journal)](https://en.wikipedia.org/wiki/Machine_Learning_(journal))
- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
- [Mamba (deep learning architecture)](https://en.wikipedia.org/wiki/Mamba_(deep_learning_architecture))
- [Marvin Minsky](https://en.wikipedia.org/wiki/Marvin_Minsky)
- [Mean shift](https://en.wikipedia.org/wiki/Mean_shift)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)
- [Memtransistor](https://en.wikipedia.org/wiki/Memtransistor)
- [Meta-learning (computer science)](https://en.wikipedia.org/wiki/Meta-learning_(computer_science))
- [Midjourney](https://en.wikipedia.org/wiki/Midjourney)
- [MuZero](https://en.wikipedia.org/wiki/MuZero)
- [Multi-agent reinforcement learning](https://en.wikipedia.org/wiki/Multi-agent_reinforcement_learning)
- [Multilayer perceptron](https://en.wikipedia.org/wiki/Multilayer_perceptron)
- [Multimodal learning](https://en.wikipedia.org/wiki/Multimodal_learning)
- [Music and artificial intelligence](https://en.wikipedia.org/wiki/Music_and_artificial_intelligence)
- [Naive Bayes classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
- [Nathaniel Rochester (computer scientist)](https://en.wikipedia.org/wiki/Nathaniel_Rochester_(computer_scientist))
- [Neural Turing machine](https://en.wikipedia.org/wiki/Neural_Turing_machine)
- [Neural machine translation](https://en.wikipedia.org/wiki/Neural_machine_translation)
- [Neural network (machine learning)](https://en.wikipedia.org/wiki/Neural_network_(machine_learning))
- [Neural radiance field](https://en.wikipedia.org/wiki/Neural_radiance_field)
- [Neural style transfer](https://en.wikipedia.org/wiki/Neural_style_transfer)
- [Neuro-symbolic AI](https://en.wikipedia.org/wiki/Neuro-symbolic_AI)
- [Neuromorphic computing](https://en.wikipedia.org/wiki/Neuromorphic_computing)
- [Non-negative matrix factorization](https://en.wikipedia.org/wiki/Non-negative_matrix_factorization)
- [OPTICS algorithm](https://en.wikipedia.org/wiki/OPTICS_algorithm)
- [Occam learning](https://en.wikipedia.org/wiki/Occam_learning)
- [Oliver Selfridge](https://en.wikipedia.org/wiki/Oliver_Selfridge)
- [Online machine learning](https://en.wikipedia.org/wiki/Online_machine_learning)
- [Ontology learning](https://en.wikipedia.org/wiki/Ontology_learning)
- [OpenAI Five](https://en.wikipedia.org/wiki/OpenAI_Five)
- [OpenAI o1](https://en.wikipedia.org/wiki/OpenAI_o1)
- [Optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition)
- [Outline of machine learning](https://en.wikipedia.org/wiki/Outline_of_machine_learning)
- [Overfitting](https://en.wikipedia.org/wiki/Overfitting)
- [PubMed Central](https://en.wikipedia.org/wiki/PubMed_Central)
- [PubMed](https://en.wikipedia.org/wiki/PubMed)
- [PaLM](https://en.wikipedia.org/wiki/PaLM)
- [Parameter](https://en.wikipedia.org/wiki/Parameter)
- [Paul Werbos](https://en.wikipedia.org/wiki/Paul_Werbos)
- [Perceptron](https://en.wikipedia.org/wiki/Perceptron)
- [Principal component analysis](https://en.wikipedia.org/wiki/Principal_component_analysis)
- [Probably approximately correct learning](https://en.wikipedia.org/wiki/Probably_approximately_correct_learning)
- [Project Debater](https://en.wikipedia.org/wiki/Project_Debater)
- [Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering)
- [Proper generalized decomposition](https://en.wikipedia.org/wiki/Proper_generalized_decomposition)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Q-learning](https://en.wikipedia.org/wiki/Q-learning)
- [Quantum machine learning](https://en.wikipedia.org/wiki/Quantum_machine_learning)
- [Quasi-Newton method](https://en.wikipedia.org/wiki/Quasi-Newton_method)
- [Random forest](https://en.wikipedia.org/wiki/Random_forest)
- [Random sample consensus](https://en.wikipedia.org/wiki/Random_sample_consensus)
- [Receiver operating characteristic](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
- [Rectifier (neural networks)](https://en.wikipedia.org/wiki/Rectifier_(neural_networks))
- [Recurrent neural network](https://en.wikipedia.org/wiki/Recurrent_neural_network)
- [Regression analysis](https://en.wikipedia.org/wiki/Regression_analysis)
- [Regularization (mathematics)](https://en.wikipedia.org/wiki/Regularization_(mathematics))
- [Reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning)
- [Reinforcement learning from human feedback](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback)
- [Relevance vector machine](https://en.wikipedia.org/wiki/Relevance_vector_machine)
- [Reservoir computing](https://en.wikipedia.org/wiki/Reservoir_computing)
- [Residual neural network](https://en.wikipedia.org/wiki/Residual_neural_network)
- [Restricted Boltzmann machine](https://en.wikipedia.org/wiki/Restricted_Boltzmann_machine)
- [Retrieval-augmented generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)
- [Robot control](https://en.wikipedia.org/wiki/Robot_control)
- [Rule-based machine learning](https://en.wikipedia.org/wiki/Rule-based_machine_learning)
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
- [Softmax function](https://en.wikipedia.org/wiki/Softmax_function)
- [Sora (text-to-video model)](https://en.wikipedia.org/wiki/Sora_(text-to-video_model))
- [Sparse dictionary learning](https://en.wikipedia.org/wiki/Sparse_dictionary_learning)
- [Matrix norm](https://en.wikipedia.org/wiki/Matrix_norm)
- [Speech recognition](https://en.wikipedia.org/wiki/Speech_recognition)
- [Spiking neural network](https://en.wikipedia.org/wiki/Spiking_neural_network)
- [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion)
- [State–action–reward–state–action](https://en.wikipedia.org/wiki/State%E2%80%93action%E2%80%93reward%E2%80%93state%E2%80%93action)
- [Statistical classification](https://en.wikipedia.org/wiki/Statistical_classification)
- [Statistical learning theory](https://en.wikipedia.org/wiki/Statistical_learning_theory)
- [Stephen Grossberg](https://en.wikipedia.org/wiki/Stephen_Grossberg)
- [Stochastic gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)
- [Structured prediction](https://en.wikipedia.org/wiki/Structured_prediction)
- [Suno AI](https://en.wikipedia.org/wiki/Suno_AI)
- [Supervised learning](https://en.wikipedia.org/wiki/Supervised_learning)
- [Support vector machine](https://en.wikipedia.org/wiki/Support_vector_machine)
- [T-distributed stochastic neighbor embedding](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding)
- [T5 (language model)](https://en.wikipedia.org/wiki/T5_(language_model))
- [Temporal difference learning](https://en.wikipedia.org/wiki/Temporal_difference_learning)
- [Text-to-image model](https://en.wikipedia.org/wiki/Text-to-image_model)
- [Text-to-video model](https://en.wikipedia.org/wiki/Text-to-video_model)
- [Training, validation, and test data sets](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets)
- [Transformer (deep learning architecture)](https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture))
- [Transformer (deep learning architecture)](https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture))
- [U-Net](https://en.wikipedia.org/wiki/U-Net)
- [Udio](https://en.wikipedia.org/wiki/Udio)
- [Unsupervised learning](https://en.wikipedia.org/wiki/Unsupervised_learning)
- [Vapnik–Chervonenkis theory](https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory)
- [Variational autoencoder](https://en.wikipedia.org/wiki/Variational_autoencoder)
- [VideoPoet](https://en.wikipedia.org/wiki/VideoPoet)
- [Vision transformer](https://en.wikipedia.org/wiki/Vision_transformer)
- [Walter Pitts](https://en.wikipedia.org/wiki/Walter_Pitts)
- [Warren Sturgis McCulloch](https://en.wikipedia.org/wiki/Warren_Sturgis_McCulloch)
- [Wasserstein GAN](https://en.wikipedia.org/wiki/Wasserstein_GAN)
- [WaveNet](https://en.wikipedia.org/wiki/WaveNet)
- [Weight initialization](https://en.wikipedia.org/wiki/Weight_initialization)
- [Whisper (speech recognition system)](https://en.wikipedia.org/wiki/Whisper_(speech_recognition_system))
- [Word2vec](https://en.wikipedia.org/wiki/Word2vec)
- [Word embedding](https://en.wikipedia.org/wiki/Word_embedding)
- [Yann LeCun](https://en.wikipedia.org/wiki/Yann_LeCun)
- [Yoshua Bengio](https://en.wikipedia.org/wiki/Yoshua_Bengio)
- [Template:Artificial intelligence navbox](https://en.wikipedia.org/wiki/Template:Artificial_intelligence_navbox)
- [Template:Cite journal](https://en.wikipedia.org/wiki/Template:Cite_journal)
- [Template:Machine learning](https://en.wikipedia.org/wiki/Template:Machine_learning)
- [Template talk:Artificial intelligence navbox](https://en.wikipedia.org/wiki/Template_talk:Artificial_intelligence_navbox)
- [Template talk:Machine learning](https://en.wikipedia.org/wiki/Template_talk:Machine_learning)
- [Help:CS1 errors](https://en.wikipedia.org/wiki/Help:CS1_errors)
- [Category:Artificial neural networks](https://en.wikipedia.org/wiki/Category:Artificial_neural_networks)
- [Category:Machine learning](https://en.wikipedia.org/wiki/Category:Machine_learning)
- [Portal:Technology](https://en.wikipedia.org/wiki/Portal:Technology)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:37:36.784780+00:00_