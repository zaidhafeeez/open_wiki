# Commutation matrix

## Metadata
- **Last Updated:** 2024-11-18 13:40:26 UTC
- **Original Article:** [Commutation matrix](https://en.wikipedia.org/wiki/Commutation_matrix)
- **Language:** en
- **Page ID:** 7133473

## Summary
In mathematics, especially in linear algebra and matrix theory, the commutation matrix is used for transforming the vectorized form of a matrix into the vectorized form of its transpose. Specifically, the commutation matrix K(m,n) is the nm × mn matrix which, for any m × n matrix A, transforms vec(A) into vec(AT):

K(m,n) vec(A) = vec(AT) .
Here vec(A) is the mn × 1 column vector obtain by stacking the columns of A on top of one another:

  
    
      
        vec
        ⁡
        (
        
          A
        
        )
        =
        [
        
          
            A
          
          
            1
            ,
            1
          
        
        ,
        …
        ,
        
          
            A
          
          
            m
            ,
            1
          
        
        ,
        
          
            A
          
          
            1
            ,
            2
          
        
        ,
        …
        ,
        
          
            A
          
          
            m
            ,
            2
          
        
        ,
        …
        ,
        
          
            A
          
          
            1
            ,
            n
          
        
        ,
        …
        ,
        
          
            A
          
          
            m
            ,
            n
          
        
        
          ]
          
            
              T
            
          
        
      
    
    {\displaystyle \operatorname {vec} (\mathbf {A} )=[\mathbf {A} _{1,1},\ldots ,\mathbf {A} _{m,1},\mathbf {A} _{1,2},\ldots ,\mathbf {A} _{m,2},\ldots ,\mathbf {A} _{1,n},\ldots ,\mathbf {A} _{m,n}]^{\mathrm {T} }}
  

where A = [Ai,j]. In other words, vec(A) is the vector obtained by vectorizing A in column-major order. Similarly, vec(AT) is the vector obtaining by vectorizing A in row-major order.
In the context of quantum information theory, the commutation matrix is sometimes referred to as the swap matrix or swap operator

## Categories
This article belongs to the following categories:

- Category:Articles with example MATLAB/Octave code
- Category:Articles with example Python (programming language) code
- Category:Linear algebra
- Category:Matrices

## Table of Contents

- Properties
- Code
- Example
- References

## Content

In mathematics, especially in linear algebra and matrix theory, the commutation matrix is used for transforming the vectorized form of a matrix into the vectorized form of its transpose. Specifically, the commutation matrix K(m,n) is the nm × mn matrix which, for any m × n matrix A, transforms vec(A) into vec(AT):

K(m,n) vec(A) = vec(AT) .
Here vec(A) is the mn × 1 column vector obtain by stacking the columns of A on top of one another:

  
    
      
        vec
        ⁡
        (
        
          A
        
        )
        =
        [
        
          
            A
          
          
            1
            ,
            1
          
        
        ,
        …
        ,
        
          
            A
          
          
            m
            ,
            1
          
        
        ,
        
          
            A
          
          
            1
            ,
            2
          
        
        ,
        …
        ,
        
          
            A
          
          
            m
            ,
            2
          
        
        ,
        …
        ,
        
          
            A
          
          
            1
            ,
            n
          
        
        ,
        …
        ,
        
          
            A
          
          
            m
            ,
            n
          
        
        
          ]
          
            
              T
            
          
        
      
    
    {\displaystyle \operatorname {vec} (\mathbf {A} )=[\mathbf {A} _{1,1},\ldots ,\mathbf {A} _{m,1},\mathbf {A} _{1,2},\ldots ,\mathbf {A} _{m,2},\ldots ,\mathbf {A} _{1,n},\ldots ,\mathbf {A} _{m,n}]^{\mathrm {T} }}
  

where A = [Ai,j]. In other words, vec(A) is the vector obtained by vectorizing A in column-major order. Similarly, vec(AT) is the vector obtaining by vectorizing A in row-major order.
In the context of quantum information theory, the commutation matrix is sometimes referred to as the swap matrix or swap operator

Properties
The commutation matrix is a special type of permutation matrix, and is therefore orthogonal.  In particular, K(m,n) is equal to 
  
    
      
        
          
            P
          
          
            π
          
        
      
    
    {\displaystyle \mathbf {P} _{\pi }}
  
, where 
  
    
      
        π
      
    
    {\displaystyle \pi }
  
 is the permutation over 
  
    
      
        {
        1
        ,
        …
        ,
        m
        n
        }
      
    
    {\displaystyle \{1,\dots ,mn\}}
  
 for which

  
    
      
        π
        (
        i
        +
        m
        (
        j
        −
        1
        )
        )
        =
        j
        +
        n
        (
        i
        −
        1
        )
        ,
        
        i
        =
        1
        ,
        …
        ,
        m
        ,
        
        j
        =
        1
        ,
        …
        ,
        n
        .
      
    
    {\displaystyle \pi (i+m(j-1))=j+n(i-1),\quad i=1,\dots ,m,\quad j=1,\dots ,n.}
  

The determinant of K(m,n) is 
  
    
      
        (
        −
        1
        
          )
          
            
              
                1
                4
              
            
            n
            (
            n
            −
            1
            )
            m
            (
            m
            −
            1
            )
          
        
      
    
    {\displaystyle (-1)^{{\frac {1}{4}}n(n-1)m(m-1)}}
  
.
Replacing A with AT in the definition of the commutation matrix shows that K(m,n) = (K(n,m))T.  Therefore, in the special case of m = n the commutation matrix is an involution and symmetric.
The main use of the commutation matrix, and the source of its name, is to commute the Kronecker product: for every m × n matrix A and every r × q matrix B,

  
    
      
        
          
            K
          
          
            (
            r
            ,
            m
            )
          
        
        (
        
          A
        
        ⊗
        
          B
        
        )
        
          
            K
          
          
            (
            n
            ,
            q
            )
          
        
        =
        
          B
        
        ⊗
        
          A
        
        .
      
    
    {\displaystyle \mathbf {K} ^{(r,m)}(\mathbf {A} \otimes \mathbf {B} )\mathbf {K} ^{(n,q)}=\mathbf {B} \otimes \mathbf {A} .}
  

This property is often used in developing the higher order statistics of Wishart covariance matrices.
The case of n=q=1 for the above equation states that for any column vectors v,w of sizes m,r respectively,

  
    
      
        
          
            K
          
          
            (
            r
            ,
            m
            )
          
        
        (
        
          v
        
        ⊗
        
          w
        
        )
        =
        
          w
        
        ⊗
        
          v
        
        .
      
    
    {\displaystyle \mathbf {K} ^{(r,m)}(\mathbf {v} \otimes \mathbf {w} )=\mathbf {w} \otimes \mathbf {v} .}
  

This property is the reason that this matrix is referred to as the "swap operator" in the context of quantum information theory.
Two explicit forms for the commutation matrix are as follows: if er,j denotes the j-th canonical vector of dimension r (i.e. the vector with 1 in the j-th coordinate and 0 elsewhere) then

  
    
      
        
          
            K
          
          
            (
            r
            ,
            m
            )
          
        
        =
        
          ∑
          
            i
            =
            1
          
          
            r
          
        
        
          ∑
          
            j
            =
            1
          
          
            m
          
        
        
          (
          
            
              
                e
              
              
                r
                ,
                i
              
            
            
              
                
                  
                    e
                  
                  
                    m
                    ,
                    j
                  
                
              
              
                
                  T
                
              
            
          
          )
        
        ⊗
        
          (
          
            
              
                e
              
              
                m
                ,
                j
              
            
            
              
                
                  
                    e
                  
                  
                    r
                    ,
                    i
                  
                
              
              
                
                  T
                
              
            
          
          )
        
        =
        
          ∑
          
            i
            =
            1
          
          
            r
          
        
        
          ∑
          
            j
            =
            1
          
          
            m
          
        
        
          (
          
            
              
                e
              
              
                r
                ,
                i
              
            
            ⊗
            
              
                e
              
              
                m
                ,
                j
              
            
          
          )
        
        
          
            (
            
              
                
                  e
                
                
                  m
                  ,
                  j
                
              
              ⊗
              
                
                  e
                
                
                  r
                  ,
                  i
                
              
            
            )
          
          
            
              T
            
          
        
        .
      
    
    {\displaystyle \mathbf {K} ^{(r,m)}=\sum _{i=1}^{r}\sum _{j=1}^{m}\left(\mathbf {e} _{r,i}{\mathbf {e} _{m,j}}^{\mathrm {T} }\right)\otimes \left(\mathbf {e} _{m,j}{\mathbf {e} _{r,i}}^{\mathrm {T} }\right)=\sum _{i=1}^{r}\sum _{j=1}^{m}\left(\mathbf {e} _{r,i}\otimes \mathbf {e} _{m,j}\right)\left(\mathbf {e} _{m,j}\otimes \mathbf {e} _{r,i}\right)^{\mathrm {T} }.}
  

The commutation matrix may be expressed as the following block matrix:

  
    
      
        
          
            K
          
          
            (
            m
            ,
            n
            )
          
        
        =
        
          
            [
            
              
                
                  
                    
                      K
                    
                    
                      1
                      ,
                      1
                    
                  
                
                
                  ⋯
                
                
                  
                    
                      K
                    
                    
                      1
                      ,
                      n
                    
                  
                
              
              
                
                  ⋮
                
                
                  ⋱
                
                
                  ⋮
                
              
              
                
                  
                    
                      K
                    
                    
                      m
                      ,
                      1
                    
                  
                
                
                  ⋯
                
                
                  
                    
                      K
                    
                    
                      m
                      ,
                      n
                    
                  
                  ,
                
              
            
            ]
          
        
        ,
      
    
    {\displaystyle \mathbf {K} ^{(m,n)}={\begin{bmatrix}\mathbf {K} _{1,1}&\cdots &\mathbf {K} _{1,n}\\\vdots &\ddots &\vdots \\\mathbf {K} _{m,1}&\cdots &\mathbf {K} _{m,n},\end{bmatrix}},}
  

Where the p,q entry of n x m block-matrix Ki,j is given by

  
    
      
        
          
            K
          
          
            i
            j
          
        
        (
        p
        ,
        q
        )
        =
        
          
            {
            
              
                
                  1
                
                
                  i
                  =
                  q
                  
                     and 
                  
                  j
                  =
                  p
                  ,
                
              
              
                
                  0
                
                
                  
                    otherwise
                  
                  .
                
              
            
            
          
        
      
    
    {\displaystyle \mathbf {K} _{ij}(p,q)={\begin{cases}1&i=q{\text{ and }}j=p,\\0&{\text{otherwise}}.\end{cases}}}
  

For example,

  
    
      
        
          
            K
          
          
            (
            3
            ,
            4
            )
          
        
        =
        
          [
          
            
              
                
                  1
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
              
              
                
                  0
                
                
                  0
                
                
                  0
                
                
                  1
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
              
              
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  1
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
              
              
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  1
                
                
                  0
                
                
                  0
                
              
              
                
                  0
                
                
                  1
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
              
              
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  1
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
              
              
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  1
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
              
              
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  1
                
                
                  0
                
              
              
                
                  0
                
                
                  0
                
                
                  1
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
              
              
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  1
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
              
              
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  1
                
                
                  0
                
                
                  0
                
                
                  0
                
              
              
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  0
                
                
                  1
                
              
            
          
          ]
        
        .
      
    
    {\displaystyle \mathbf {K} ^{(3,4)}=\left[{\begin{array}{ccc|ccc|ccc|ccc}1&0&0&0&0&0&0&0&0&0&0&0\\0&0&0&1&0&0&0&0&0&0&0&0\\0&0&0&0&0&0&1&0&0&0&0&0\\0&0&0&0&0&0&0&0&0&1&0&0\\\hline 0&1&0&0&0&0&0&0&0&0&0&0\\0&0&0&0&1&0&0&0&0&0&0&0\\0&0&0&0&0&0&0&1&0&0&0&0\\0&0&0&0&0&0&0&0&0&0&1&0\\\hline 0&0&1&0&0&0&0&0&0&0&0&0\\0&0&0&0&0&1&0&0&0&0&0&0\\0&0&0&0&0&0&0&0&1&0&0&0\\0&0&0&0&0&0&0&0&0&0&0&1\end{array}}\right].}

Code
For both square and rectangular matrices of m rows and n columns, the commutation matrix can be generated by the code below.

Python
Alternatively, a version without imports:

MATLAB
R
Example
Let 
  
    
      
        A
      
    
    {\displaystyle A}
  
 denote the following 
  
    
      
        3
        ×
        2
      
    
    {\displaystyle 3\times 2}
  
 matrix:

  
    
      
        A
        =
        
          
            [
            
              
                
                  1
                
                
                  4
                
              
              
                
                  2
                
                
                  5
                
              
              
                
                  3
                
                
                  6
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle A={\begin{bmatrix}1&4\\2&5\\3&6\\\end{bmatrix}}.}
  

  
    
      
        A
      
    
    {\displaystyle A}
  
 has the following column-major and row-major vectorizations (respectively):

  
    
      
        
          
            v
          
          
            col
          
        
        =
        vec
        ⁡
        (
        A
        )
        =
        
          
            [
            
              
                
                  1
                
              
              
                
                  2
                
              
              
                
                  3
                
              
              
                
                  4
                
              
              
                
                  5
                
              
              
                
                  6
                
              
            
            ]
          
        
        ,
        
        
          
            v
          
          
            row
          
        
        =
        vec
        ⁡
        (
        
          A
          
            
              T
            
          
        
        )
        =
        
          
            [
            
              
                
                  1
                
              
              
                
                  4
                
              
              
                
                  2
                
              
              
                
                  5
                
              
              
                
                  3
                
              
              
                
                  6
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle \mathbf {v} _{\text{col}}=\operatorname {vec} (A)={\begin{bmatrix}1\\2\\3\\4\\5\\6\\\end{bmatrix}},\quad \mathbf {v} _{\text{row}}=\operatorname {vec} (A^{\mathrm {T} })={\begin{bmatrix}1\\4\\2\\5\\3\\6\\\end{bmatrix}}.}
  

The associated commutation matrix is

  
    
      
        K
        =
        
          
            K
          
          
            (
            3
            ,
            2
            )
          
        
        =
        
          
            [
            
              
                
                  1
                
                
                  ⋅
                
                
                  ⋅
                
                
                  ⋅
                
                
                  ⋅
                
                
                  ⋅
                
              
              
                
                  ⋅
                
                
                  ⋅
                
                
                  ⋅
                
                
                  1
                
                
                  ⋅
                
                
                  ⋅
                
              
              
                
                  ⋅
                
                
                  1
                
                
                  ⋅
                
                
                  ⋅
                
                
                  ⋅
                
                
                  ⋅
                
              
              
                
                  ⋅
                
                
                  ⋅
                
                
                  ⋅
                
                
                  ⋅
                
                
                  1
                
                
                  ⋅
                
              
              
                
                  ⋅
                
                
                  ⋅
                
                
                  1
                
                
                  ⋅
                
                
                  ⋅
                
                
                  ⋅
                
              
              
                
                  ⋅
                
                
                  ⋅
                
                
                  ⋅
                
                
                  ⋅
                
                
                  ⋅
                
                
                  1
                
              
            
            ]
          
        
        ,
      
    
    {\displaystyle K=\mathbf {K} ^{(3,2)}={\begin{bmatrix}1&\cdot &\cdot &\cdot &\cdot &\cdot \\\cdot &\cdot &\cdot &1&\cdot &\cdot \\\cdot &1&\cdot &\cdot &\cdot &\cdot \\\cdot &\cdot &\cdot &\cdot &1&\cdot \\\cdot &\cdot &1&\cdot &\cdot &\cdot \\\cdot &\cdot &\cdot &\cdot &\cdot &1\\\end{bmatrix}},}
  

(where each 
  
    
      
        ⋅
      
    
    {\displaystyle \cdot }
  
 denotes a zero). As expected, the following holds:

  
    
      
        
          K
          
            
              T
            
          
        
        K
        =
        K
        
          K
          
            
              T
            
          
        
        =
        
          
            I
          
          
            6
          
        
      
    
    {\displaystyle K^{\mathrm {T} }K=KK^{\mathrm {T} }=\mathbf {I} _{6}}
  

  
    
      
        K
        
          
            v
          
          
            col
          
        
        =
        
          
            v
          
          
            row
          
        
      
    
    {\displaystyle K\mathbf {v} _{\text{col}}=\mathbf {v} _{\text{row}}}

References

Jan R. Magnus and Heinz Neudecker (1988), Matrix Differential Calculus with Applications in Statistics and Econometrics, Wiley.

## Archive Info
- **Archived on:** 2024-12-15 21:03:58 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 27438 bytes
- **Word Count:** 1184 words
