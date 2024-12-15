# Commutation matrix

## Article Metadata

- **Last Updated:** 2024-12-15T04:08:28.017891+00:00
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
        
 

## Categories

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

## Related Articles

### Internal Links

- [Adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix)
- [Adjugate matrix](https://en.wikipedia.org/wiki/Adjugate_matrix)
- [Alternant matrix](https://en.wikipedia.org/wiki/Alternant_matrix)
- [Alternating sign matrix](https://en.wikipedia.org/wiki/Alternating_sign_matrix)
- [Anti-diagonal matrix](https://en.wikipedia.org/wiki/Anti-diagonal_matrix)
- [Arrowhead matrix](https://en.wikipedia.org/wiki/Arrowhead_matrix)
- [Augmented matrix](https://en.wikipedia.org/wiki/Augmented_matrix)
- [Band matrix](https://en.wikipedia.org/wiki/Band_matrix)
- [Adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix)
- [Bidiagonal matrix](https://en.wikipedia.org/wiki/Bidiagonal_matrix)
- [Bisymmetric matrix](https://en.wikipedia.org/wiki/Bisymmetric_matrix)
- [Block matrix](https://en.wikipedia.org/wiki/Block_matrix)
- [Block matrix](https://en.wikipedia.org/wiki/Block_matrix)
- [Block matrix](https://en.wikipedia.org/wiki/Block_matrix)
- [Boolean matrix](https://en.wikipedia.org/wiki/Boolean_matrix)
- [Bézout matrix](https://en.wikipedia.org/wiki/B%C3%A9zout_matrix)
- [Cabibbo–Kobayashi–Maskawa matrix](https://en.wikipedia.org/wiki/Cabibbo%E2%80%93Kobayashi%E2%80%93Maskawa_matrix)
- [Carleman matrix](https://en.wikipedia.org/wiki/Carleman_matrix)
- [Cartan matrix](https://en.wikipedia.org/wiki/Cartan_matrix)
- [Cauchy matrix](https://en.wikipedia.org/wiki/Cauchy_matrix)
- [Centering matrix](https://en.wikipedia.org/wiki/Centering_matrix)
- [Centrosymmetric matrix](https://en.wikipedia.org/wiki/Centrosymmetric_matrix)
- [Circulant matrix](https://en.wikipedia.org/wiki/Circulant_matrix)
- [Minor (linear algebra)](https://en.wikipedia.org/wiki/Minor_(linear_algebra))
- [Row and column vectors](https://en.wikipedia.org/wiki/Row_and_column_vectors)
- [Commutator](https://en.wikipedia.org/wiki/Commutator)
- [Companion matrix](https://en.wikipedia.org/wiki/Companion_matrix)
- [Complex Hadamard matrix](https://en.wikipedia.org/wiki/Complex_Hadamard_matrix)
- [Conference matrix](https://en.wikipedia.org/wiki/Conference_matrix)
- [Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix)
- [Convergent matrix](https://en.wikipedia.org/wiki/Convergent_matrix)
- [Copositive matrix](https://en.wikipedia.org/wiki/Copositive_matrix)
- [Correlation](https://en.wikipedia.org/wiki/Correlation)
- [Covariance matrix](https://en.wikipedia.org/wiki/Covariance_matrix)
- [Coxeter group](https://en.wikipedia.org/wiki/Coxeter_group)
- [DFT matrix](https://en.wikipedia.org/wiki/DFT_matrix)
- [Defective matrix](https://en.wikipedia.org/wiki/Defective_matrix)
- [Definite matrix](https://en.wikipedia.org/wiki/Definite_matrix)
- [Degree matrix](https://en.wikipedia.org/wiki/Degree_matrix)
- [Density matrix](https://en.wikipedia.org/wiki/Density_matrix)
- [Design matrix](https://en.wikipedia.org/wiki/Design_matrix)
- [Diagonal matrix](https://en.wikipedia.org/wiki/Diagonal_matrix)
- [Diagonalizable matrix](https://en.wikipedia.org/wiki/Diagonalizable_matrix)
- [Diagonally dominant matrix](https://en.wikipedia.org/wiki/Diagonally_dominant_matrix)
- [Distance matrix](https://en.wikipedia.org/wiki/Distance_matrix)
- [Doubly stochastic matrix](https://en.wikipedia.org/wiki/Doubly_stochastic_matrix)
- [Duplication and elimination matrices](https://en.wikipedia.org/wiki/Duplication_and_elimination_matrices)
- [Edmonds matrix](https://en.wikipedia.org/wiki/Edmonds_matrix)
- [Eigenvalues and eigenvectors](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)
- [Elementary matrix](https://en.wikipedia.org/wiki/Elementary_matrix)
- [Matrix equivalence](https://en.wikipedia.org/wiki/Matrix_equivalence)
- [Euclidean distance matrix](https://en.wikipedia.org/wiki/Euclidean_distance_matrix)
- [Exchange matrix](https://en.wikipedia.org/wiki/Exchange_matrix)
- [Fisher information](https://en.wikipedia.org/wiki/Fisher_information)
- [Frobenius matrix](https://en.wikipedia.org/wiki/Frobenius_matrix)
- [Fundamental matrix (computer vision)](https://en.wikipedia.org/wiki/Fundamental_matrix_(computer_vision))
- [Fundamental matrix (linear differential equation)](https://en.wikipedia.org/wiki/Fundamental_matrix_(linear_differential_equation))
- [Fuzzy associative matrix](https://en.wikipedia.org/wiki/Fuzzy_associative_matrix)
- [Gamma matrices](https://en.wikipedia.org/wiki/Gamma_matrices)
- [Gell-Mann matrices](https://en.wikipedia.org/wiki/Gell-Mann_matrices)
- [Generalized permutation matrix](https://en.wikipedia.org/wiki/Generalized_permutation_matrix)
- [Generator matrix](https://en.wikipedia.org/wiki/Generator_matrix)
- [Gram matrix](https://en.wikipedia.org/wiki/Gram_matrix)
- [Graph theory](https://en.wikipedia.org/wiki/Graph_theory)
- [Hadamard matrix](https://en.wikipedia.org/wiki/Hadamard_matrix)
- [Hamiltonian matrix](https://en.wikipedia.org/wiki/Hamiltonian_matrix)
- [Hankel matrix](https://en.wikipedia.org/wiki/Hankel_matrix)
- [Hermitian matrix](https://en.wikipedia.org/wiki/Hermitian_matrix)
- [Hessenberg matrix](https://en.wikipedia.org/wiki/Hessenberg_matrix)
- [Hessian matrix](https://en.wikipedia.org/wiki/Hessian_matrix)
- [Hilbert matrix](https://en.wikipedia.org/wiki/Hilbert_matrix)
- [Hollow matrix](https://en.wikipedia.org/wiki/Hollow_matrix)
- [Householder transformation](https://en.wikipedia.org/wiki/Householder_transformation)
- [Hurwitz-stable matrix](https://en.wikipedia.org/wiki/Hurwitz-stable_matrix)
- [Idempotent matrix](https://en.wikipedia.org/wiki/Idempotent_matrix)
- [Identity matrix](https://en.wikipedia.org/wiki/Identity_matrix)
- [Incidence matrix](https://en.wikipedia.org/wiki/Incidence_matrix)
- [Integer matrix](https://en.wikipedia.org/wiki/Integer_matrix)
- [Invertible matrix](https://en.wikipedia.org/wiki/Invertible_matrix)
- [Invertible matrix](https://en.wikipedia.org/wiki/Invertible_matrix)
- [Involution (mathematics)](https://en.wikipedia.org/wiki/Involution_(mathematics))
- [Involutory matrix](https://en.wikipedia.org/wiki/Involutory_matrix)
- [Irregular matrix](https://en.wikipedia.org/wiki/Irregular_matrix)
- [Jacobian matrix and determinant](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant)
- [Jordan normal form](https://en.wikipedia.org/wiki/Jordan_normal_form)
- [Kronecker product](https://en.wikipedia.org/wiki/Kronecker_product)
- [Laplacian matrix](https://en.wikipedia.org/wiki/Laplacian_matrix)
- [Lehmer matrix](https://en.wikipedia.org/wiki/Lehmer_matrix)
- [Linear algebra](https://en.wikipedia.org/wiki/Linear_algebra)
- [Linear independence](https://en.wikipedia.org/wiki/Linear_independence)
- [List of named matrices](https://en.wikipedia.org/wiki/List_of_named_matrices)
- [Logical matrix](https://en.wikipedia.org/wiki/Logical_matrix)
- [Mathematics](https://en.wikipedia.org/wiki/Mathematics)
- [Matrix (mathematics)](https://en.wikipedia.org/wiki/Matrix_(mathematics))
- [Matrix congruence](https://en.wikipedia.org/wiki/Matrix_congruence)
- [Matrix exponential](https://en.wikipedia.org/wiki/Matrix_exponential)
- [Matrix of ones](https://en.wikipedia.org/wiki/Matrix_of_ones)
- [Matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication)
- [Matrix representation of conic sections](https://en.wikipedia.org/wiki/Matrix_representation_of_conic_sections)
- [Matrix unit](https://en.wikipedia.org/wiki/Matrix_unit)
- [Metzler matrix](https://en.wikipedia.org/wiki/Metzler_matrix)
- [Moment matrix](https://en.wikipedia.org/wiki/Moment_matrix)
- [Moore matrix](https://en.wikipedia.org/wiki/Moore_matrix)
- [Nilpotent matrix](https://en.wikipedia.org/wiki/Nilpotent_matrix)
- [Nonnegative matrix](https://en.wikipedia.org/wiki/Nonnegative_matrix)
- [Normal matrix](https://en.wikipedia.org/wiki/Normal_matrix)
- [Orthogonal matrix](https://en.wikipedia.org/wiki/Orthogonal_matrix)
- [Orbital overlap](https://en.wikipedia.org/wiki/Orbital_overlap)
- [Pascal matrix](https://en.wikipedia.org/wiki/Pascal_matrix)
- [Pauli matrices](https://en.wikipedia.org/wiki/Pauli_matrices)
- [Normal-form game](https://en.wikipedia.org/wiki/Normal-form_game)
- [Band matrix](https://en.wikipedia.org/wiki/Band_matrix)
- [Perfect matrix](https://en.wikipedia.org/wiki/Perfect_matrix)
- [Permutation matrix](https://en.wikipedia.org/wiki/Permutation_matrix)
- [Persymmetric matrix](https://en.wikipedia.org/wiki/Persymmetric_matrix)
- [Nevanlinna–Pick interpolation](https://en.wikipedia.org/wiki/Nevanlinna%E2%80%93Pick_interpolation)
- [Polynomial matrix](https://en.wikipedia.org/wiki/Polynomial_matrix)
- [Definite matrix](https://en.wikipedia.org/wiki/Definite_matrix)
- [Precision (statistics)](https://en.wikipedia.org/wiki/Precision_(statistics))
- [Projection (linear algebra)](https://en.wikipedia.org/wiki/Projection_(linear_algebra))
- [Projection matrix](https://en.wikipedia.org/wiki/Projection_matrix)
- [Generalized inverse](https://en.wikipedia.org/wiki/Generalized_inverse)
- [Quantum information](https://en.wikipedia.org/wiki/Quantum_information)
- [Quantum logic gate](https://en.wikipedia.org/wiki/Quantum_logic_gate)
- [Quaternionic matrix](https://en.wikipedia.org/wiki/Quaternionic_matrix)
- [Random matrix](https://en.wikipedia.org/wiki/Random_matrix)
- [Redheffer matrix](https://en.wikipedia.org/wiki/Redheffer_matrix)
- [Rotation matrix](https://en.wikipedia.org/wiki/Rotation_matrix)
- [Routh–Hurwitz matrix](https://en.wikipedia.org/wiki/Routh%E2%80%93Hurwitz_matrix)
- [Row- and column-major order](https://en.wikipedia.org/wiki/Row-_and_column-major_order)
- [Row echelon form](https://en.wikipedia.org/wiki/Row_echelon_form)
- [S-matrix](https://en.wikipedia.org/wiki/S-matrix)
- [Seidel adjacency matrix](https://en.wikipedia.org/wiki/Seidel_adjacency_matrix)
- [Seifert surface](https://en.wikipedia.org/wiki/Seifert_surface)
- [Shear mapping](https://en.wikipedia.org/wiki/Shear_mapping)
- [Shift matrix](https://en.wikipedia.org/wiki/Shift_matrix)
- [Signature matrix](https://en.wikipedia.org/wiki/Signature_matrix)
- [Similarity measure](https://en.wikipedia.org/wiki/Similarity_measure)
- [Skew-Hermitian matrix](https://en.wikipedia.org/wiki/Skew-Hermitian_matrix)
- [Skew-symmetric matrix](https://en.wikipedia.org/wiki/Skew-symmetric_matrix)
- [Skyline matrix](https://en.wikipedia.org/wiki/Skyline_matrix)
- [Sparse matrix](https://en.wikipedia.org/wiki/Sparse_matrix)
- [State-transition matrix](https://en.wikipedia.org/wiki/State-transition_matrix)
- [Statistics](https://en.wikipedia.org/wiki/Statistics)
- [Stieltjes matrix](https://en.wikipedia.org/wiki/Stieltjes_matrix)
- [Stochastic matrix](https://en.wikipedia.org/wiki/Stochastic_matrix)
- [Substitution matrix](https://en.wikipedia.org/wiki/Substitution_matrix)
- [Sylvester matrix](https://en.wikipedia.org/wiki/Sylvester_matrix)
- [Symmetric matrix](https://en.wikipedia.org/wiki/Symmetric_matrix)
- [Symplectic matrix](https://en.wikipedia.org/wiki/Symplectic_matrix)
- [Toeplitz matrix](https://en.wikipedia.org/wiki/Toeplitz_matrix)
- [Totally positive matrix](https://en.wikipedia.org/wiki/Totally_positive_matrix)
- [Unimodular matrix](https://en.wikipedia.org/wiki/Unimodular_matrix)
- [Transformation matrix](https://en.wikipedia.org/wiki/Transformation_matrix)
- [Transpose](https://en.wikipedia.org/wiki/Transpose)
- [Triangular matrix](https://en.wikipedia.org/wiki/Triangular_matrix)
- [Tridiagonal matrix](https://en.wikipedia.org/wiki/Tridiagonal_matrix)
- [Tutte matrix](https://en.wikipedia.org/wiki/Tutte_matrix)
- [Unimodular matrix](https://en.wikipedia.org/wiki/Unimodular_matrix)
- [Unipotent](https://en.wikipedia.org/wiki/Unipotent)
- [Unitary matrix](https://en.wikipedia.org/wiki/Unitary_matrix)
- [Vandermonde matrix](https://en.wikipedia.org/wiki/Vandermonde_matrix)
- [Vectorization (mathematics)](https://en.wikipedia.org/wiki/Vectorization_(mathematics))
- [Walsh matrix](https://en.wikipedia.org/wiki/Walsh_matrix)
- [Weighing matrix](https://en.wikipedia.org/wiki/Weighing_matrix)
- [Wronskian](https://en.wikipedia.org/wiki/Wronskian)
- [Z-matrix (chemistry)](https://en.wikipedia.org/wiki/Z-matrix_(chemistry))
- [Z-matrix (mathematics)](https://en.wikipedia.org/wiki/Z-matrix_(mathematics))
- [Zero matrix](https://en.wikipedia.org/wiki/Zero_matrix)
- [Template:Matrix classes](https://en.wikipedia.org/wiki/Template:Matrix_classes)
- [Template talk:Matrix classes](https://en.wikipedia.org/wiki/Template_talk:Matrix_classes)
- [Category:Matrices](https://en.wikipedia.org/wiki/Category:Matrices)
- [Portal:Mathematics](https://en.wikipedia.org/wiki/Portal:Mathematics)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:08:28.017891+00:00_