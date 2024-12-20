---
title: Sample entropy
url: https://en.wikipedia.org/wiki/Sample_entropy
language: en
categories: ["Category:All articles with too many examples", "Category:Articles with example Python (programming language) code", "Category:Articles with too many examples from July 2024", "Category:Entropy", "Category:Statistical signal processing", "Category:Wikipedia articles with style issues from July 2024"]
references: 0
last_modified: 2024-12-04T12:33:31Z
---

# Sample entropy

## Summary

Sample entropy (SampEn; more appropriately K_2 entropy or Takens-Grassberger-Procaccia correlation entropy ) is a modification of approximate entropy (ApEn;  more appropriately "Procaccia-Cohen entropy"), used for assessing the complexity of physiological and other time-series signals, diagnosing e.g. diseased states. SampEn has two advantages over ApEn: data length independence and a relatively trouble-free implementation. Also, there is a small computational difference: In ApEn, the comparison

## Full Content

Sample entropy (SampEn; more appropriately K_2 entropy or Takens-Grassberger-Procaccia correlation entropy ) is a modification of approximate entropy (ApEn;  more appropriately "Procaccia-Cohen entropy"), used for assessing the complexity of physiological and other time-series signals, diagnosing e.g. diseased states. SampEn has two advantages over ApEn: data length independence and a relatively trouble-free implementation. Also, there is a small computational difference: In ApEn, the comparison between the template vector (see below) and the rest of the vectors also includes comparison with itself. This guarantees that probabilities 
  
    
      
        
          C
          
            i
          
          
            ′
            
              m
            
          
        
        (
        r
        )
      
    
    {\displaystyle C_{i}'^{m}(r)}
  
 are never zero. Consequently, it is always possible to take a logarithm of probabilities. Because template comparisons with itself lower ApEn values, the signals are interpreted to be more regular than they actually are. These self-matches are not included in SampEn. However, since SampEn makes direct use of the correlation integrals, it is not a real measure of information but an approximation. The foundations and differences with ApEn, as well as a step-by-step tutorial for its application is available at.
SampEn is indeed identical to the "correlation entropy" K_2 of Grassberger & Procaccia , except that it is suggested in the latter that certain limits should be taken in order to achieve a result invariant under changes of variables. No such limits and no invariance properties are considered in SampEn.
There is a multiscale version of SampEn as well, suggested by Costa and others. SampEn can be used in biomedical and biomechanical research, for example to evaluate postural control.

Definition
Like approximate entropy (ApEn), Sample entropy (SampEn) is a measure of complexity. But it does not include self-similar patterns as ApEn does. For a given embedding dimension 
  
    
      
        m
      
    
    {\displaystyle m}
  
, tolerance 
  
    
      
        r
      
    
    {\displaystyle r}
  
  and number of data points 
  
    
      
        N
      
    
    {\displaystyle N}
  
, SampEn is the negative natural logarithm of the probability that if two sets of simultaneous data points of length 
  
    
      
        m
      
    
    {\displaystyle m}
  
  have distance 
  
    
      
        <
        r
      
    
    {\displaystyle <r}
  
 then two sets of simultaneous data points of length 
  
    
      
        m
        +
        1
      
    
    {\displaystyle m+1}
  
  also have distance 
  
    
      
        <
        r
      
    
    {\displaystyle <r}
  
. And we represent it by 
  
    
      
        S
        a
        m
        p
        E
        n
        (
        m
        ,
        r
        ,
        N
        )
      
    
    {\displaystyle SampEn(m,r,N)}
  
 (or by 
  
    
      
        S
        a
        m
        p
        E
        n
        (
        m
        ,
        r
        ,
        τ
        ,
        N
        )
      
    
    {\displaystyle SampEn(m,r,\tau ,N)}
  
 including sampling time 
  
    
      
        τ
      
    
    {\displaystyle \tau }
  
).
Now assume we have a time-series data set of length 
  
    
      
        N
        =
        
          {
          
            x
            
              1
            
          
          ,
          
            x
            
              2
            
          
          ,
          
            x
            
              3
            
          
          ,
          .
          .
          .
          ,
          
            x
            
              N
            
          
          }
        
      
    
    {\displaystyle N={\{x_{1},x_{2},x_{3},...,x_{N}\}}}
  
 with a constant time interval 
  
    
      
        τ
      
    
    {\displaystyle \tau }
  
. We define a template vector of length 
  
    
      
        m
      
    
    {\displaystyle m}
  
, such that 
  
    
      
        
          X
          
            m
          
        
        (
        i
        )
        =
        
          {
          
            x
            
              i
            
          
          ,
          
            x
            
              i
              +
              1
            
          
          ,
          
            x
            
              i
              +
              2
            
          
          ,
          .
          .
          .
          ,
          
            x
            
              i
              +
              m
              −
              1
            
          
          }
        
      
    
    {\displaystyle X_{m}(i)={\{x_{i},x_{i+1},x_{i+2},...,x_{i+m-1}\}}}
  
 and the distance  function 
  
    
      
        d
        [
        
          X
          
            m
          
        
        (
        i
        )
        ,
        
          X
          
            m
          
        
        (
        j
        )
        ]
      
    
    {\displaystyle d[X_{m}(i),X_{m}(j)]}
  
 (i≠j) is to be the Chebyshev distance (but it could be any distance function, including Euclidean distance). We define the sample entropy to be

  
    
      
        S
        a
        m
        p
        E
        n
        =
        −
        ln
        ⁡
        
          
            A
            B
          
        
      
    
    {\displaystyle SampEn=-\ln {A \over B}}
  

Where

  
    
      
        A
      
    
    {\displaystyle A}
  
 = number of template vector pairs having 
  
    
      
        d
        [
        
          X
          
            m
            +
            1
          
        
        (
        i
        )
        ,
        
          X
          
            m
            +
            1
          
        
        (
        j
        )
        ]
        <
        r
      
    
    {\displaystyle d[X_{m+1}(i),X_{m+1}(j)]<r}
  

  
    
      
        B
      
    
    {\displaystyle B}
  
 = number of template vector pairs having 
  
    
      
        d
        [
        
          X
          
            m
          
        
        (
        i
        )
        ,
        
          X
          
            m
          
        
        (
        j
        )
        ]
        <
        r
      
    
    {\displaystyle d[X_{m}(i),X_{m}(j)]<r}
  

It is clear from the definition that 
  
    
      
        A
      
    
    {\displaystyle A}
  
 will always have a value smaller or equal to 
  
    
      
        B
      
    
    {\displaystyle B}
  
. Therefore, 
  
    
      
        S
        a
        m
        p
        E
        n
        (
        m
        ,
        r
        ,
        τ
        )
      
    
    {\displaystyle SampEn(m,r,\tau )}
  
 will be always either be zero or positive value. A smaller value of 
  
    
      
        S
        a
        m
        p
        E
        n
      
    
    {\displaystyle SampEn}
  
 also indicates more self-similarity in data set or less noise.
Generally we take the value of 
  
    
      
        m
      
    
    {\displaystyle m}
  
 to be 
  
    
      
        2
      
    
    {\displaystyle 2}
  
 and the value of 
  
    
      
        r
      
    
    {\displaystyle r}
  
 to be 
  
    
      
        0.2
        ×
        s
        t
        d
      
    
    {\displaystyle 0.2\times std}
  
.
Where std stands for standard deviation which should be taken over a very large dataset.  For instance, the r value of 6 ms is appropriate for sample entropy calculations of heart rate intervals, since this corresponds to 
  
    
      
        0.2
        ×
        s
        t
        d
      
    
    {\displaystyle 0.2\times std}
  
 for a very large population.

Multiscale SampEn
The definition mentioned above is a special case of multi scale sampEn with 
  
    
      
        δ
        =
        1
      
    
    {\displaystyle \delta =1}
  
, where 
  
    
      
        δ
      
    
    {\displaystyle \delta }
  
 is called skipping parameter.  In multiscale SampEn template vectors are defined with a certain interval between its elements, specified by the value of 
  
    
      
        δ
      
    
    {\displaystyle \delta }
  
. And modified template vector is defined as

  
    
      
        
          X
          
            m
            ,
            δ
          
        
        (
        i
        )
        =
        
          
            x
            
              i
            
          
          ,
          
            x
            
              i
              +
              δ
            
          
          ,
          
            x
            
              i
              +
              2
              ×
              δ
            
          
          ,
          .
          .
          .
          ,
          
            x
            
              i
              +
              (
              m
              −
              1
              )
              ×
              δ
            
          
        
      
    
    {\displaystyle X_{m,\delta }(i)={x_{i},x_{i+\delta },x_{i+2\times \delta },...,x_{i+(m-1)\times \delta }}}
  

and sampEn can be written as

  
    
      
        S
        a
        m
        p
        E
        n
        
          (
          
            m
            ,
            r
            ,
            δ
          
          )
        
        =
        −
        ln
        ⁡
        
          
            
              A
              
                δ
              
            
            
              B
              
                δ
              
            
          
        
      
    
    {\displaystyle SampEn\left(m,r,\delta \right)=-\ln {A_{\delta } \over B_{\delta }}}
  

And we calculate 
  
    
      
        
          A
          
            δ
          
        
      
    
    {\displaystyle A_{\delta }}
  
 and 
  
    
      
        
          B
          
            δ
          
        
      
    
    {\displaystyle B_{\delta }}
  
 like before.

Implementation
Sample entropy can be implemented easily in many different programming languages. Below lies an example written in Python. 

An equivalent example in numerical Python. 

An example written in other languages can be found:

Matlab
R.
Rust

See also
Kolmogorov complexity
Approximate entropy


== References ==
