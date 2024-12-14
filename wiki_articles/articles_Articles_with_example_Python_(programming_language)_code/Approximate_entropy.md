# Approximate entropy

_Last updated: 2024-12-14T15:39:15.385196_

**Original Article:** [Approximate entropy](https://en.wikipedia.org/wiki/Approximate_entropy)

**Summary:** In statistics, an approximate entropy (ApEn) is a technique used to quantify the amount of regularity and the unpredictability of fluctuations over time-series data. For example, consider two series of data:

Series A: (0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, ...), which alternates 0 and 1.
Series B: (0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, ...), which has either a value of 0 or 1, chosen randomly, each with probability 1/2.
Moment statistics, such as mean and variance, will not 

## Categories
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Entropy and information
- Category:Short description matches Wikidata
- Category:Time series

## Content

In statistics, an approximate entropy (ApEn) is a technique used to quantify the amount of regularity and the unpredictability of fluctuations over time-series data. For example, consider two series of data:

Series A: (0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, ...), which alternates 0 and 1.
Series B: (0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, ...), which has either a value of 0 or 1, chosen randomly, each with probability 1/2.
Moment statistics, such as mean and variance, will not distinguish between these two series. Nor will rank order statistics distinguish between these series. Yet series A is perfectly regular: knowing a term has the value of 1 enables one to predict with certainty that the next term will have the value of 0. In contrast, series B is randomly valued: knowing a term has the value of 1 gives no insight into what value the next term will have.
Regularity was originally measured by exact regularity statistics, which has mainly centered on various entropy measures.
However, accurate entropy calculation requires vast amounts of data, and the results will be greatly influenced by system noise, therefore it is not practical to apply these methods to experimental data. ApEn was first proposed (under a different name) by A. Cohen and I. Procaccia,
as an approximate algorithm to compute an exact regularity statistic, Kolmogorov–Sinai entropy, and later popularized by Steve M. Pincus. ApEn was initially used to analyze chaotic dynamics and medical data, such as heart rate, and later spread its applications in finance, physiology, human factors engineering, and climate sciences.

Algorithm
A comprehensive step-by-step tutorial with an explanation of the theoretical foundations of Approximate Entropy is available. The algorithm is:

Step 1
Assume a time series of data 
  
    
      
        u
        (
        1
        )
        ,
        u
        (
        2
        )
        ,
        …
        ,
        u
        (
        N
        )
      
    
    {\displaystyle u(1),u(2),\ldots ,u(N)}
  
. These are 
  
    
      
        N
      
    
    {\displaystyle N}
  
 raw data values from measurements equally spaced in time.
Step 2
Let 
  
    
      
        m
        ∈
        
          
            Z
          
          
            +
          
        
      
    
    {\displaystyle m\in \mathbb {Z} ^{+}}
  
 be a positive integer, with 
  
    
      
        m
        ≤
        N
      
    
    {\displaystyle m\leq N}
  
, which represents the length of a run of data (essentially a window).Let 
  
    
      
        r
        ∈
        
          
            R
          
          
            +
          
        
      
    
    {\displaystyle r\in \mathbb {R} ^{+}}
  
 be a positive real number, which specifies a filtering level.Let 
  
    
      
        n
        =
        N
        −
        m
        +
        1
      
    
    {\displaystyle n=N-m+1}
  
.
Step 3
Define 
  
    
      
        
          x
        
        (
        i
        )
        =
        
          
            [
          
        
        u
        (
        i
        )
        ,
        u
        (
        i
        +
        1
        )
        ,
        …
        ,
        u
        (
        i
        +
        m
        −
        1
        )
        
          
            ]
          
        
      
    
    {\displaystyle \mathbf {x} (i)={\big [}u(i),u(i+1),\ldots ,u(i+m-1){\big ]}}
  
 for each 
  
    
      
        i
      
    
    {\displaystyle i}
  
 where 
  
    
      
        1
        ≤
        i
        ≤
        n
      
    
    {\displaystyle 1\leq i\leq n}
  
. In other words, 
  
    
      
        
          x
        
        (
        i
        )
      
    
    {\displaystyle \mathbf {x} (i)}
  
 is an 
  
    
      
        m
      
    
    {\displaystyle m}
  
-dimensional vector that contains the run of data starting with 
  
    
      
        u
        (
        i
        )
      
    
    {\displaystyle u(i)}
  
.Define the distance between two vectors 
  
    
      
        
          x
        
        (
        i
        )
      
    
    {\displaystyle \mathbf {x} (i)}
  
 and 
  
    
      
        
          x
        
        (
        j
        )
      
    
    {\displaystyle \mathbf {x} (j)}
  
 as the maximum of the distances between their respective components, given by

  
    
      
        
          
            
              
                d
                [
                
                  x
                
                (
                i
                )
                ,
                
                  x
                
                (
                j
                )
                ]
              
              
                
                =
                
                  max
                  
                    k
                  
                
                
                  
                    (
                  
                
                
                  |
                
                
                  x
                
                (
                i
                
                  )
                  
                    k
                  
                
                −
                
                  x
                
                (
                j
                
                  )
                  
                    k
                  
                
                
                  |
                
                
                  
                    )
                  
                
              
            
            
              
              
                
                =
                
                  max
                  
                    k
                  
                
                
                  
                    (
                  
                
                
                  |
                
                u
                (
                i
                +
                k
                −
                1
                )
                −
                u
                (
                j
                +
                k
                −
                1
                )
                
                  |
                
                
                  
                    )
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}d[\mathbf {x} (i),\mathbf {x} (j)]&=\max _{k}{\big (}|\mathbf {x} (i)_{k}-\mathbf {x} (j)_{k}|{\big )}\\&=\max _{k}{\big (}|u(i+k-1)-u(j+k-1)|{\big )}\\\end{aligned}}}
  

for 
  
    
      
        1
        ≤
        k
        ≤
        m
      
    
    {\displaystyle 1\leq k\leq m}
  
.
Step 4
Define a count 
  
    
      
        
          C
          
            i
          
          
            m
          
        
      
    
    {\displaystyle C_{i}^{m}}
  
 as

  
    
      
        
          C
          
            i
          
          
            m
          
        
        (
        r
        )
        =
        
          
            
              (
              
                number of 
              
              j
              
                 such that 
              
              d
              [
              
                x
              
              (
              i
              )
              ,
              
                x
              
              (
              j
              )
              ]
              ≤
              r
              )
            
            n
          
        
      
    
    {\displaystyle C_{i}^{m}(r)={({\text{number of }}j{\text{ such that }}d[\mathbf {x} (i),\mathbf {x} (j)]\leq r) \over n}}
  

for each 
  
    
      
        i
      
    
    {\displaystyle i}
  
 where 
  
    
      
        1
        ≤
        i
        ,
        j
        ≤
        n
      
    
    {\displaystyle 1\leq i,j\leq n}
  
. Note that since 
  
    
      
        j
      
    
    {\displaystyle j}
  
 takes on all values between 1 and 
  
    
      
        n
      
    
    {\displaystyle n}
  
, the match will be counted when 
  
    
      
        j
        =
        i
      
    
    {\displaystyle j=i}
  
 (i.e. when the test subsequence, 
  
    
      
        
          x
        
        (
        j
        )
      
    
    {\displaystyle \mathbf {x} (j)}
  
, is matched against itself, 
  
    
      
        
          x
        
        (
        i
        )
      
    
    {\displaystyle \mathbf {x} (i)}
  
).
Step 5
Define

  
    
      
        
          ϕ
          
            m
          
        
        (
        r
        )
        =
        
          
            1
            n
          
        
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        log
        ⁡
        (
        
          C
          
            i
          
          
            m
          
        
        (
        r
        )
        )
      
    
    {\displaystyle \phi ^{m}(r)={1 \over n}\sum _{i=1}^{n}\log(C_{i}^{m}(r))}
  

where 
  
    
      
        log
      
    
    {\displaystyle \log }
  
 is the natural logarithm, and for a fixed 
  
    
      
        m
      
    
    {\displaystyle m}
  
, 
  
    
      
        r
      
    
    {\displaystyle r}
  
, and 
  
    
      
        n
      
    
    {\displaystyle n}
  
 as set in Step 2.
Step 6
Define approximate entropy (
  
    
      
        
          A
          p
          E
          n
        
      
    
    {\displaystyle \mathrm {ApEn} }
  
) as

  
    
      
        
          A
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
        (
        u
        )
        =
        
          ϕ
          
            m
          
        
        (
        r
        )
        −
        
          ϕ
          
            m
            +
            1
          
        
        (
        r
        )
      
    
    {\displaystyle \mathrm {ApEn} (m,r,N)(u)=\phi ^{m}(r)-\phi ^{m+1}(r)}
  

Parameter selection
Typically, choose 
  
    
      
        m
        =
        2
      
    
    {\displaystyle m=2}
  
 or 
  
    
      
        m
        =
        3
      
    
    {\displaystyle m=3}
  
, whereas 
  
    
      
        r
      
    
    {\displaystyle r}
  
 depends greatly on the application.
An implementation on Physionet, which is based on Pincus, use 
  
    
      
        d
        [
        
          x
        
        (
        i
        )
        ,
        
          x
        
        (
        j
        )
        ]
        <
        r
      
    
    {\displaystyle d[\mathbf {x} (i),\mathbf {x} (j)]<r}
  
 instead of 
  
    
      
        d
        [
        
          x
        
        (
        i
        )
        ,
        
          x
        
        (
        j
        )
        ]
        ≤
        r
      
    
    {\displaystyle d[\mathbf {x} (i),\mathbf {x} (j)]\leq r}
  
 in Step 4. While a concern for artificially constructed examples, it is usually not a concern in practice.

Example
Consider a sequence of 
  
    
      
        N
        =
        51
      
    
    {\displaystyle N=51}
  
 samples of heart rate equally spaced in time:

  
    
      
         
        
          S
          
            N
          
        
        =
        {
        85
        ,
        80
        ,
        89
        ,
        85
        ,
        80
        ,
        89
        ,
        …
        }
      
    
    {\displaystyle \ S_{N}=\{85,80,89,85,80,89,\ldots \}}
  

Note the sequence is periodic with a period of 3. Let's choose 
  
    
      
        m
        =
        2
      
    
    {\displaystyle m=2}
  
 and 
  
    
      
        r
        =
        3
      
    
    {\displaystyle r=3}
  
 (the values of 
  
    
      
        m
      
    
    {\displaystyle m}
  
 and 
  
    
      
        r
      
    
    {\displaystyle r}
  
 can be varied without affecting the result).
Form a sequence of vectors: 

  
    
      
        
          
            
              
                
                  x
                
                (
                1
                )
              
              
                
                =
                [
                u
                (
                1
                )
                 
                u
                (
                2
                )
                ]
                =
                [
                85
                 
                80
                ]
              
            
            
              
                
                  x
                
                (
                2
                )
              
              
                
                =
                [
                u
                (
                2
                )
                 
                u
                (
                3
                )
                ]
                =
                [
                80
                 
                89
                ]
              
            
            
              
                
                  x
                
                (
                3
                )
              
              
                
                =
                [
                u
                (
                3
                )
                 
                u
                (
                4
                )
                ]
                =
                [
                89
                 
                85
                ]
              
            
            
              
                
                  x
                
                (
                4
                )
              
              
                
                =
                [
                u
                (
                4
                )
                 
                u
                (
                5
                )
                ]
                =
                [
                85
                 
                80
                ]
              
            
            
              
              
                 
                 
                ⋮
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\mathbf {x} (1)&=[u(1)\ u(2)]=[85\ 80]\\\mathbf {x} (2)&=[u(2)\ u(3)]=[80\ 89]\\\mathbf {x} (3)&=[u(3)\ u(4)]=[89\ 85]\\\mathbf {x} (4)&=[u(4)\ u(5)]=[85\ 80]\\&\ \ \vdots \end{aligned}}}
  

Distance is calculated repeatedly as follows. In the first calculation,

  
    
      
         
        d
        [
        
          x
        
        (
        1
        )
        ,
        
          x
        
        (
        1
        )
        ]
        =
        
          max
          
            k
          
        
        
          |
        
        
          x
        
        (
        1
        
          )
          
            k
          
        
        −
        
          x
        
        (
        1
        
          )
          
            k
          
        
        
          |
        
        =
        0
      
    
    {\displaystyle \ d[\mathbf {x} (1),\mathbf {x} (1)]=\max _{k}|\mathbf {x} (1)_{k}-\mathbf {x} (1)_{k}|=0}
  
 which is less than 
  
    
      
        r
      
    
    {\displaystyle r}
  
.
In the second calculation, note that 
  
    
      
        
          |
        
        u
        (
        2
        )
        −
        u
        (
        3
        )
        
          |
        
        >
        
          |
        
        u
        (
        1
        )
        −
        u
        (
        2
        )
        
          |
        
      
    
    {\displaystyle |u(2)-u(3)|>|u(1)-u(2)|}
  
, so

  
    
      
         
        d
        [
        
          x
        
        (
        1
        )
        ,
        
          x
        
        (
        2
        )
        ]
        =
        
          max
          
            k
          
        
        
          |
        
        
          x
        
        (
        1
        
          )
          
            k
          
        
        −
        
          x
        
        (
        2
        
          )
          
            k
          
        
        
          |
        
        =
        
          |
        
        u
        (
        2
        )
        −
        u
        (
        3
        )
        
          |
        
        =
        9
      
    
    {\displaystyle \ d[\mathbf {x} (1),\mathbf {x} (2)]=\max _{k}|\mathbf {x} (1)_{k}-\mathbf {x} (2)_{k}|=|u(2)-u(3)|=9}
  
 which is greater than 
  
    
      
        r
      
    
    {\displaystyle r}
  
.
Similarly,

  
    
      
        
          
            
              
                d
                [
                
                  x
                
                (
                1
                )
              
              
                
                ,
                
                  x
                
                (
                3
                )
                ]
                =
                
                  |
                
                u
                (
                2
                )
                −
                u
                (
                4
                )
                
                  |
                
                =
                5
                >
                r
              
            
            
              
                d
                [
                
                  x
                
                (
                1
                )
              
              
                
                ,
                
                  x
                
                (
                4
                )
                ]
                =
                
                  |
                
                u
                (
                1
                )
                −
                u
                (
                4
                )
                
                  |
                
                =
                
                  |
                
                u
                (
                2
                )
                −
                u
                (
                5
                )
                
                  |
                
                =
                0
                <
                r
              
            
            
              
              
                
                ⋮
              
            
            
              
                d
                [
                
                  x
                
                (
                1
                )
              
              
                
                ,
                
                  x
                
                (
                j
                )
                ]
                =
                ⋯
              
            
            
              
              
                
                ⋮
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}d[\mathbf {x} (1)&,\mathbf {x} (3)]=|u(2)-u(4)|=5>r\\d[\mathbf {x} (1)&,\mathbf {x} (4)]=|u(1)-u(4)|=|u(2)-u(5)|=0<r\\&\vdots \\d[\mathbf {x} (1)&,\mathbf {x} (j)]=\cdots \\&\vdots \\\end{aligned}}}
  

The result is a total of 17 terms 
  
    
      
        
          x
        
        (
        j
        )
      
    
    {\displaystyle \mathbf {x} (j)}
  
 such that 
  
    
      
        d
        [
        
          x
        
        (
        1
        )
        ,
        
          x
        
        (
        j
        )
        ]
        ≤
        r
      
    
    {\displaystyle d[\mathbf {x} (1),\mathbf {x} (j)]\leq r}
  
. These include 
  
    
      
        
          x
        
        (
        1
        )
        ,
        
          x
        
        (
        4
        )
        ,
        
          x
        
        (
        7
        )
        ,
        …
        ,
        
          x
        
        (
        49
        )
      
    
    {\displaystyle \mathbf {x} (1),\mathbf {x} (4),\mathbf {x} (7),\ldots ,\mathbf {x} (49)}
  
. In these cases, 
  
    
      
        
          C
          
            i
          
          
            m
          
        
        (
        r
        )
      
    
    {\displaystyle C_{i}^{m}(r)}
  
 is

  
    
      
         
        
          C
          
            1
          
          
            2
          
        
        (
        3
        )
        =
        
          
            17
            50
          
        
      
    
    {\displaystyle \ C_{1}^{2}(3)={\frac {17}{50}}}
  

  
    
      
         
        
          C
          
            2
          
          
            2
          
        
        (
        3
        )
        =
        
          
            17
            50
          
        
      
    
    {\displaystyle \ C_{2}^{2}(3)={\frac {17}{50}}}
  

  
    
      
         
        
          C
          
            3
          
          
            2
          
        
        (
        3
        )
        =
        
          
            16
            50
          
        
      
    
    {\displaystyle \ C_{3}^{2}(3)={\frac {16}{50}}}
  

  
    
      
         
        
          C
          
            4
          
          
            2
          
        
        (
        3
        )
        =
        
          
            17
            50
          
        
         
        ⋯
      
    
    {\displaystyle \ C_{4}^{2}(3)={\frac {17}{50}}\ \cdots }
  

Note in Step 4, 
  
    
      
        1
        ≤
        i
        ≤
        n
      
    
    {\displaystyle 1\leq i\leq n}
  
 for 
  
    
      
        
          x
        
        (
        i
        )
      
    
    {\displaystyle \mathbf {x} (i)}
  
. So the terms 
  
    
      
        
          x
        
        (
        j
        )
      
    
    {\displaystyle \mathbf {x} (j)}
  
 such that 
  
    
      
        d
        [
        
          x
        
        (
        3
        )
        ,
        
          x
        
        (
        j
        )
        ]
        ≤
        r
      
    
    {\displaystyle d[\mathbf {x} (3),\mathbf {x} (j)]\leq r}
  
 include 
  
    
      
        
          x
        
        (
        3
        )
        ,
        
          x
        
        (
        6
        )
        ,
        
          x
        
        (
        9
        )
        ,
        …
        ,
        
          x
        
        (
        48
        )
      
    
    {\displaystyle \mathbf {x} (3),\mathbf {x} (6),\mathbf {x} (9),\ldots ,\mathbf {x} (48)}
  
, and the total number is 16.
At the end of these calculations, we have

  
    
      
        
          ϕ
          
            2
          
        
        (
        3
        )
        =
        
          
            1
            50
          
        
        
          ∑
          
            i
            =
            1
          
          
            50
          
        
        log
        ⁡
        (
        
          C
          
            i
          
          
            2
          
        
        (
        3
        )
        )
        ≈
        −
        1.0982
      
    
    {\displaystyle \phi ^{2}(3)={1 \over 50}\sum _{i=1}^{50}\log(C_{i}^{2}(3))\approx -1.0982}
  

Then we repeat the above steps for 
  
    
      
        m
        =
        3
      
    
    {\displaystyle m=3}
  
. First form a sequence of vectors: 

  
    
      
        
          
            
              
                
                  x
                
                (
                1
                )
              
              
                
                =
                [
                u
                (
                1
                )
                 
                u
                (
                2
                )
                 
                u
                (
                3
                )
                ]
                =
                [
                85
                 
                80
                 
                89
                ]
              
            
            
              
                
                  x
                
                (
                2
                )
              
              
                
                =
                [
                u
                (
                2
                )
                 
                u
                (
                3
                )
                 
                u
                (
                4
                )
                ]
                =
                [
                80
                 
                89
                 
                85
                ]
              
            
            
              
                
                  x
                
                (
                3
                )
              
              
                
                =
                [
                u
                (
                3
                )
                 
                u
                (
                4
                )
                 
                u
                (
                5
                )
                ]
                =
                [
                89
                 
                85
                 
                80
                ]
              
            
            
              
                
                  x
                
                (
                4
                )
              
              
                
                =
                [
                u
                (
                4
                )
                 
                u
                (
                5
                )
                 
                u
                (
                6
                )
                ]
                =
                [
                85
                 
                80
                 
                89
                ]
              
            
            
              
              
                 
                 
                ⋮
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\mathbf {x} (1)&=[u(1)\ u(2)\ u(3)]=[85\ 80\ 89]\\\mathbf {x} (2)&=[u(2)\ u(3)\ u(4)]=[80\ 89\ 85]\\\mathbf {x} (3)&=[u(3)\ u(4)\ u(5)]=[89\ 85\ 80]\\\mathbf {x} (4)&=[u(4)\ u(5)\ u(6)]=[85\ 80\ 89]\\&\ \ \vdots \end{aligned}}}
  

By calculating distances between vector 
  
    
      
        
          x
        
        (
        i
        )
        ,
        
          x
        
        (
        j
        )
        ,
        1
        ≤
        i
        ≤
        49
      
    
    {\displaystyle \mathbf {x} (i),\mathbf {x} (j),1\leq i\leq 49}
  
, we find the vectors satisfying the filtering level have the following characteristic:

  
    
      
        d
        [
        
          x
        
        (
        i
        )
        ,
        
          x
        
        (
        i
        +
        3
        )
        ]
        =
        0
        <
        r
      
    
    {\displaystyle d[\mathbf {x} (i),\mathbf {x} (i+3)]=0<r}
  

Therefore,  

  
    
      
         
        
          C
          
            1
          
          
            3
          
        
        (
        3
        )
        =
        
          
            17
            49
          
        
      
    
    {\displaystyle \ C_{1}^{3}(3)={\frac {17}{49}}}
  

  
    
      
         
        
          C
          
            2
          
          
            3
          
        
        (
        3
        )
        =
        
          
            16
            49
          
        
      
    
    {\displaystyle \ C_{2}^{3}(3)={\frac {16}{49}}}
  

  
    
      
         
        
          C
          
            3
          
          
            3
          
        
        (
        3
        )
        =
        
          
            16
            49
          
        
      
    
    {\displaystyle \ C_{3}^{3}(3)={\frac {16}{49}}}
  

  
    
      
         
        
          C
          
            4
          
          
            3
          
        
        (
        3
        )
        =
        
          
            17
            49
          
        
         
        ⋯
      
    
    {\displaystyle \ C_{4}^{3}(3)={\frac {17}{49}}\ \cdots }
  

At the end of these calculations, we have

  
    
      
        
          ϕ
          
            3
          
        
        (
        3
        )
        =
        
          
            1
            49
          
        
        
          ∑
          
            i
            =
            1
          
          
            49
          
        
        log
        ⁡
        (
        
          C
          
            i
          
          
            3
          
        
        (
        3
        )
        )
        ≈
        −
        1.0982
      
    
    {\displaystyle \phi ^{3}(3)={1 \over 49}\sum _{i=1}^{49}\log(C_{i}^{3}(3))\approx -1.0982}
  

Finally,

  
    
      
        
          A
          p
          E
          n
        
        =
        
          ϕ
          
            2
          
        
        (
        3
        )
        −
        
          ϕ
          
            3
          
        
        (
        3
        )
        ≈
        0.000010997
      
    
    {\displaystyle \mathrm {ApEn} =\phi ^{2}(3)-\phi ^{3}(3)\approx 0.000010997}
  

The value is very small, so it implies the sequence is regular and predictable, which is consistent with the observation.

Python implementation
MATLAB implementation
Fast Approximate Entropy from MatLab Central
approximateEntropy

Interpretation
The presence of repetitive patterns of fluctuation in a time series renders it more predictable than a time series in which such patterns are absent. ApEn reflects the likelihood that similar patterns of observations will not be followed by additional similar observations. A time series containing many repetitive patterns has a relatively small ApEn; a less predictable process has a higher ApEn.

Advantages
The advantages of ApEn include:

Lower computational demand. ApEn can be designed to work for small data samples (
  
    
      
        N
        <
        50
      
    
    {\displaystyle N<50}
  
 points) and can be applied in real time.
Less effect from noise. If data is noisy, the ApEn measure can be compared to the noise level in the data to determine what quality of true information may be present in the data.

Limitations
The ApEn algorithm counts each sequence as matching itself to avoid the occurrence of 
  
    
      
        log
        ⁡
        (
        0
        )
      
    
    {\displaystyle \log(0)}
  
 in the calculations. This step might introduce bias in ApEn, which causes ApEn to have two poor properties in practice: 

ApEn is heavily dependent on the record length and is uniformly lower than expected for short records.
It lacks relative consistency. That is, if ApEn of one data set is higher than that of another, it should, but does not, remain higher for all conditions tested.

Applications
ApEn has been applied to classify electroencephalography (EEG) in psychiatric diseases, such as schizophrenia, epilepsy, and addiction.

See also
Recurrence quantification analysis
Sample entropy


== References ==