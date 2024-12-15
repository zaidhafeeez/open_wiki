# Gauss–Seidel method

## Metadata
- **Last Updated:** 2024-12-06 05:13:42 UTC
- **Original Article:** [Gauss–Seidel method](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method)
- **Language:** en
- **Page ID:** 4046824

## Summary
In numerical linear algebra, the Gauss–Seidel method, also known as the Liebmann method or the method of successive displacement,  is an iterative method used to solve a system of linear equations. It is named after the German mathematicians Carl Friedrich Gauss and Philipp Ludwig von Seidel. Though it can be applied to any matrix with non-zero elements on the diagonals, convergence is only guaranteed if the matrix is either strictly diagonally dominant, or symmetric and positive definite. It was only mentioned in a private letter from Gauss to his student Gerling in 1823. A publication was not delivered before 1874 by Seidel.

## Categories
This article belongs to the following categories:

- Category:Articles with example MATLAB/Octave code
- Category:Articles with example Python (programming language) code
- Category:Articles with example pseudocode
- Category:Articles with short description
- Category:CS1 German-language sources (de)
- Category:Numerical linear algebra
- Category:Relaxation (iterative methods)
- Category:Short description matches Wikidata
- Category:Wikipedia articles licensed under the GNU Free Document License

## Table of Contents

- Description
- Convergence
- Algorithm
- Examples
- See also
- Notes
- References
- External links

## Content

In numerical linear algebra, the Gauss–Seidel method, also known as the Liebmann method or the method of successive displacement,  is an iterative method used to solve a system of linear equations. It is named after the German mathematicians Carl Friedrich Gauss and Philipp Ludwig von Seidel. Though it can be applied to any matrix with non-zero elements on the diagonals, convergence is only guaranteed if the matrix is either strictly diagonally dominant, or symmetric and positive definite. It was only mentioned in a private letter from Gauss to his student Gerling in 1823. A publication was not delivered before 1874 by Seidel.

Description
Let 
  
    
      
        
          A
        
        
          x
        
        =
        
          b
        
      
    
    {\textstyle \mathbf {A} \mathbf {x} =\mathbf {b} }
  
 be a square system of n linear equations, where:

  
    
      
        
          A
        
        =
        
          
            [
            
              
                
                  
                    a
                    
                      11
                    
                  
                
                
                  
                    a
                    
                      12
                    
                  
                
                
                  ⋯
                
                
                  
                    a
                    
                      1
                      n
                    
                  
                
              
              
                
                  
                    a
                    
                      21
                    
                  
                
                
                  
                    a
                    
                      22
                    
                  
                
                
                  ⋯
                
                
                  
                    a
                    
                      2
                      n
                    
                  
                
              
              
                
                  ⋮
                
                
                  ⋮
                
                
                  ⋱
                
                
                  ⋮
                
              
              
                
                  
                    a
                    
                      n
                      1
                    
                  
                
                
                  
                    a
                    
                      n
                      2
                    
                  
                
                
                  ⋯
                
                
                  
                    a
                    
                      n
                      n
                    
                  
                
              
            
            ]
          
        
        ,
        
        
          x
        
        =
        
          
            [
            
              
                
                  
                    x
                    
                      1
                    
                  
                
              
              
                
                  
                    x
                    
                      2
                    
                  
                
              
              
                
                  ⋮
                
              
              
                
                  
                    x
                    
                      n
                    
                  
                
              
            
            ]
          
        
        ,
        
        
          b
        
        =
        
          
            [
            
              
                
                  
                    b
                    
                      1
                    
                  
                
              
              
                
                  
                    b
                    
                      2
                    
                  
                
              
              
                
                  ⋮
                
              
              
                
                  
                    b
                    
                      n
                    
                  
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle \mathbf {A} ={\begin{bmatrix}a_{11}&a_{12}&\cdots &a_{1n}\\a_{21}&a_{22}&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\a_{n1}&a_{n2}&\cdots &a_{nn}\end{bmatrix}},\qquad \mathbf {x} ={\begin{bmatrix}x_{1}\\x_{2}\\\vdots \\x_{n}\end{bmatrix}},\qquad \mathbf {b} ={\begin{bmatrix}b_{1}\\b_{2}\\\vdots \\b_{n}\end{bmatrix}}.}
  

When 
  
    
      
        
          A
        
      
    
    {\displaystyle \mathbf {A} }
  
 and 
  
    
      
        
          b
        
      
    
    {\displaystyle \mathbf {b} }
  
 are known, and 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
 is unknown, the Gauss–Seidel method can be used to iteratively approximate 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
. The vector 
  
    
      
        
          
            x
          
          
            (
            0
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(0)}}
  
 denotes the initial guess for 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
, often 
  
    
      
        
          
            x
          
          
            i
          
          
            (
            0
            )
          
        
        =
        0
      
    
    {\displaystyle \mathbf {x} _{i}^{(0)}=0}
  
 for 
  
    
      
        i
        =
        1
        ,
        2
        ,
        .
        .
        .
        ,
        n
      
    
    {\displaystyle i=1,2,...,n}
  
. Denote by 
  
    
      
        
          
            x
          
          
            (
            k
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(k)}}
  
 the 
  
    
      
        k
      
    
    {\displaystyle k}
  
-th approximation or iteration of 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
, and by 
  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}}
  
 the approximation of 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
 at the next (or 
  
    
      
        k
        +
        1
      
    
    {\displaystyle k+1}
  
-th) iteration.

Matrix-based formula
The solution is obtained iteratively via

  
    
      
        
          L
        
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
        =
        
          b
        
        −
        
          U
        
        
          
            x
          
          
            (
            k
            )
          
        
        ,
      
    
    {\displaystyle \mathbf {L} \mathbf {x} ^{(k+1)}=\mathbf {b} -\mathbf {U} \mathbf {x} ^{(k)},}
  

where the matrix 
  
    
      
        
          A
        
      
    
    {\displaystyle \mathbf {A} }
  
 is decomposed into a lower triangular component 
  
    
      
        
          L
        
      
    
    {\displaystyle \mathbf {L} }
  
, and a strictly upper triangular component 
  
    
      
        
          U
        
      
    
    {\displaystyle \mathbf {U} }
  
 such that 
  
    
      
        
          A
        
        =
        
          L
        
        +
        
          U
        
      
    
    {\displaystyle \mathbf {A} =\mathbf {L} +\mathbf {U} }
  
. More specifically, the decomposition of 
  
    
      
        A
      
    
    {\displaystyle A}
  
 into 
  
    
      
        
          L
          
            ∗
          
        
      
    
    {\displaystyle L_{*}}
  
 and 
  
    
      
        U
      
    
    {\displaystyle U}
  
 is given by:

  
    
      
        
          A
        
        =
        
          
            
              
                [
                
                  
                    
                      
                        a
                        
                          11
                        
                      
                    
                    
                      0
                    
                    
                      ⋯
                    
                    
                      0
                    
                  
                  
                    
                      
                        a
                        
                          21
                        
                      
                    
                    
                      
                        a
                        
                          22
                        
                      
                    
                    
                      ⋯
                    
                    
                      0
                    
                  
                  
                    
                      ⋮
                    
                    
                      ⋮
                    
                    
                      ⋱
                    
                    
                      ⋮
                    
                  
                  
                    
                      
                        a
                        
                          n
                          1
                        
                      
                    
                    
                      
                        a
                        
                          n
                          2
                        
                      
                    
                    
                      ⋯
                    
                    
                      
                        a
                        
                          n
                          n
                        
                      
                    
                  
                
                ]
              
              ⏟
            
          
          
            
              
                L
              
            
          
        
        +
        
          
            
              
                [
                
                  
                    
                      0
                    
                    
                      
                        a
                        
                          12
                        
                      
                    
                    
                      ⋯
                    
                    
                      
                        a
                        
                          1
                          n
                        
                      
                    
                  
                  
                    
                      0
                    
                    
                      0
                    
                    
                      ⋯
                    
                    
                      
                        a
                        
                          2
                          n
                        
                      
                    
                  
                  
                    
                      ⋮
                    
                    
                      ⋮
                    
                    
                      ⋱
                    
                    
                      ⋮
                    
                  
                  
                    
                      0
                    
                    
                      0
                    
                    
                      ⋯
                    
                    
                      0
                    
                  
                
                ]
              
              ⏟
            
          
          
            
              
                U
              
            
          
        
        .
      
    
    {\displaystyle \mathbf {A} =\underbrace {\begin{bmatrix}a_{11}&0&\cdots &0\\a_{21}&a_{22}&\cdots &0\\\vdots &\vdots &\ddots &\vdots \\a_{n1}&a_{n2}&\cdots &a_{nn}\end{bmatrix}} _{\textstyle \mathbf {L} }+\underbrace {\begin{bmatrix}0&a_{12}&\cdots &a_{1n}\\0&0&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\0&0&\cdots &0\end{bmatrix}} _{\textstyle \mathbf {U} }.}

Why the matrix-based formula works
The system of linear equations may be rewritten as:

  
    
      
        
          
            
              
                
                  A
                
                
                  x
                
              
              
                
                =
                
                  b
                
              
            
            
              
                (
                
                  L
                
                +
                
                  U
                
                )
                
                  x
                
              
              
                
                =
                
                  b
                
              
            
            
              
                
                  L
                
                
                  x
                
                +
                
                  U
                
                
                  x
                
              
              
                
                =
                
                  b
                
              
            
            
              
                
                  L
                
                
                  x
                
              
              
                
                =
                
                  b
                
                −
                
                  U
                
                
                  x
                
              
            
          
        
      
    
    {\displaystyle {\begin{alignedat}{1}\mathbf {A} \mathbf {x} &=\mathbf {b} \\(\mathbf {L} +\mathbf {U} )\mathbf {x} &=\mathbf {b} \\\mathbf {L} \mathbf {x} +\mathbf {U} \mathbf {x} &=\mathbf {b} \\\mathbf {L} \mathbf {x} &=\mathbf {b} -\mathbf {U} \mathbf {x} \end{alignedat}}}
  

The Gauss–Seidel method now solves the left hand side of this expression for 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
, using the previous value for 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
 on the right hand side. Analytically, this may be written as

  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
        =
        
          
            L
          
          
            −
            1
          
        
        
          (
          
            
              b
            
            −
            
              U
            
            
              
                x
              
              
                (
                k
                )
              
            
          
          )
        
        .
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}=\mathbf {L} ^{-1}\left(\mathbf {b} -\mathbf {U} \mathbf {x} ^{(k)}\right).}

Element-based formula
However, by taking advantage of the triangular form of 
  
    
      
        
          L
        
      
    
    {\displaystyle \mathbf {L} }
  
, the elements of 
  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}}
  
 can be computed sequentially for each row 
  
    
      
        i
      
    
    {\displaystyle i}
  
 using forward substitution:

  
    
      
        
          x
          
            i
          
          
            (
            k
            +
            1
            )
          
        
        =
        
          
            1
            
              a
              
                i
                i
              
            
          
        
        
          (
          
            
              b
              
                i
              
            
            −
            
              ∑
              
                j
                =
                1
              
              
                i
                −
                1
              
            
            
              a
              
                i
                j
              
            
            
              x
              
                j
              
              
                (
                k
                +
                1
                )
              
            
            −
            
              ∑
              
                j
                =
                i
                +
                1
              
              
                n
              
            
            
              a
              
                i
                j
              
            
            
              x
              
                j
              
              
                (
                k
                )
              
            
          
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
        .
      
    
    {\displaystyle x_{i}^{(k+1)}={\frac {1}{a_{ii}}}\left(b_{i}-\sum _{j=1}^{i-1}a_{ij}x_{j}^{(k+1)}-\sum _{j=i+1}^{n}a_{ij}x_{j}^{(k)}\right),\quad i=1,2,\dots ,n.}
  

Notice that the formula uses two summations per iteration which can be expressed as one summation 
  
    
      
        
          ∑
          
            j
            ≠
            i
          
        
        
          a
          
            i
            j
          
        
        
          x
          
            j
          
        
      
    
    {\displaystyle \sum _{j\neq i}a_{ij}x_{j}}
  
 that uses the most recently calculated iteration of 
  
    
      
        
          x
          
            j
          
        
      
    
    {\displaystyle x_{j}}
  
. The procedure is generally continued until the changes made by an iteration are below some tolerance, such as a sufficiently small residual.

Discussion
The element-wise formula for the Gauss–Seidel method is related to that of the (iterative) Jacobi method, with an important difference:
In Gauss-Seidel, the computation of 
  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}}
  
 uses the elements of 
  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}}
  
 that have already been computed, and only the elements of 
  
    
      
        
          
            x
          
          
            (
            k
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(k)}}
  
 that have not been computed in the 
  
    
      
        (
        k
        +
        1
        )
      
    
    {\displaystyle (k+1)}
  
-th iteration. This means that, unlike the Jacobi method, only one storage vector is required as elements can be overwritten as they are computed, which can be advantageous for very large problems.
However, unlike the Jacobi method, the computations for each element are generally much harder to implement in parallel, since they can have a very long critical path, and are thus most feasible for sparse matrices. Furthermore, the values at each iteration are dependent on the order of the original equations.
Gauss-Seidel is the same as successive over-relaxation with 
  
    
      
        ω
        =
        1
      
    
    {\displaystyle \omega =1}
  
.

Convergence
The convergence properties of the Gauss–Seidel method are dependent on the matrix 
  
    
      
        
          A
        
      
    
    {\displaystyle \mathbf {A} }
  
. Namely, the procedure is known to converge if either:

  
    
      
        
          A
        
      
    
    {\displaystyle \mathbf {A} }
  
 is symmetric positive-definite, or

  
    
      
        
          A
        
      
    
    {\displaystyle \mathbf {A} }
  
 is strictly or irreducibly diagonally dominant.
The Gauss–Seidel method may converge even if these conditions are not satisfied.
Golub and Van Loan give a theorem for an algorithm that splits 
  
    
      
        
          A
        
      
    
    {\displaystyle \mathbf {A} }
  
 into two parts. Suppose 
  
    
      
        
          A
        
        =
        
          M
        
        −
        
          N
        
      
    
    {\displaystyle \mathbf {A} =\mathbf {M} -\mathbf {N} }
  
 is nonsingular. Let 
  
    
      
        r
        =
        ρ
        (
        
          
            M
          
          
            −
            1
          
        
        
          N
        
        )
      
    
    {\displaystyle r=\rho (\mathbf {M} ^{-1}\mathbf {N} )}
  
 be the spectral radius of 
  
    
      
        
          
            M
          
          
            −
            1
          
        
        
          N
        
      
    
    {\displaystyle \mathbf {M} ^{-1}\mathbf {N} }
  
. Then the iterates 
  
    
      
        
          
            x
          
          
            (
            k
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(k)}}
  
 defined by 
  
    
      
        
          M
        
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
        =
        
          N
        
        
          
            x
          
          
            (
            k
            )
          
        
        +
        
          b
        
      
    
    {\displaystyle \mathbf {M} \mathbf {x} ^{(k+1)}=\mathbf {N} \mathbf {x} ^{(k)}+\mathbf {b} }
  
 converge to 
  
    
      
        
          x
        
        =
        
          
            A
          
          
            −
            1
          
        
        
          b
        
      
    
    {\displaystyle \mathbf {x} =\mathbf {A} ^{-1}\mathbf {b} }
  
 for any starting vector 
  
    
      
        
          
            x
          
          
            (
            0
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(0)}}
  
 if 
  
    
      
        
          M
        
      
    
    {\displaystyle \mathbf {M} }
  
 is nonsingular and 
  
    
      
        r
        <
        1
      
    
    {\displaystyle r<1}
  
.

Algorithm
Since elements can be overwritten as they are computed in this algorithm, only one storage vector is needed, and vector indexing is omitted. The algorithm goes as follows:

algorithm Gauss–Seidel method is
    inputs: A, b
    output: φ

    Choose an initial guess φ to the solution
    repeat until convergence
        for i from 1 until n do
            σ ← 0
            for j from 1 until n do
                if j ≠ i then
                    σ ← σ + aijφj
                end if
            end (j-loop)
            φi ← (bi − σ) / aii
        end (i-loop)
        check if convergence is reached
    end (repeat)

Examples
An example for the matrix version
A linear system shown as 
  
    
      
        
          A
        
        
          x
        
        =
        
          b
        
      
    
    {\displaystyle \mathbf {A} \mathbf {x} =\mathbf {b} }
  
 is given by:

  
    
      
        
          A
        
        =
        
          
            [
            
              
                
                  16
                
                
                  3
                
              
              
                
                  7
                
                
                  −
                  11
                
              
            
            ]
          
        
        
        
          and
        
        
        
          b
        
        =
        
          
            [
            
              
                
                  11
                
              
              
                
                  13
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle \mathbf {A} ={\begin{bmatrix}16&3\\7&-11\\\end{bmatrix}}\quad {\text{and}}\quad \mathbf {b} ={\begin{bmatrix}11\\13\end{bmatrix}}.}
  

Use the equation

  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
        =
        
          
            L
          
          
            −
            1
          
        
        (
        
          b
        
        −
        
          U
        
        
          
            x
          
          
            (
            k
            )
          
        
        )
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}=\mathbf {L} ^{-1}(\mathbf {b} -\mathbf {U} \mathbf {x} ^{(k)})}
  

in the form

  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
        =
        
          T
        
        
          
            x
          
          
            (
            k
            )
          
        
        +
        
          c
        
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}=\mathbf {T} \mathbf {x} ^{(k)}+\mathbf {c} }
  

where:

  
    
      
        
          T
        
        =
        −
        
          
            L
          
          
            −
            1
          
        
        
          U
        
        
        
          and
        
        
        
          c
        
        =
        
          
            L
          
          
            −
            1
          
        
        
          b
        
        .
      
    
    {\displaystyle \mathbf {T} =-\mathbf {L} ^{-1}\mathbf {U} \quad {\text{and}}\quad \mathbf {c} =\mathbf {L} ^{-1}\mathbf {b} .}
  

Decompose 
  
    
      
        
          A
        
      
    
    {\displaystyle \mathbf {A} }
  
 into the sum of a lower triangular component 
  
    
      
        
          L
        
      
    
    {\displaystyle \mathbf {L} }
  
 and a strict upper triangular component 
  
    
      
        U
      
    
    {\displaystyle U}
  
:

  
    
      
        
          L
        
        =
        
          
            [
            
              
                
                  16
                
                
                  0
                
              
              
                
                  7
                
                
                  −
                  11
                
              
            
            ]
          
        
        
        
          and
        
        
        
          U
        
        =
        
          
            [
            
              
                
                  0
                
                
                  3
                
              
              
                
                  0
                
                
                  0
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle \mathbf {L} ={\begin{bmatrix}16&0\\7&-11\\\end{bmatrix}}\quad {\text{and}}\quad \mathbf {U} ={\begin{bmatrix}0&3\\0&0\end{bmatrix}}.}
  

The inverse of 
  
    
      
        
          L
        
      
    
    {\displaystyle \mathbf {L} }
  
 is:

  
    
      
        
          
            L
          
          
            −
            1
          
        
        =
        
          
            
              [
              
                
                  
                    16
                  
                  
                    0
                  
                
                
                  
                    7
                  
                  
                    −
                    11
                  
                
              
              ]
            
          
          
            −
            1
          
        
        =
        
          
            [
            
              
                
                  0.0625
                
                
                  0.0000
                
              
              
                
                  0.0398
                
                
                  −
                  0.0909
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle \mathbf {L} ^{-1}={\begin{bmatrix}16&0\\7&-11\end{bmatrix}}^{-1}={\begin{bmatrix}0.0625&0.0000\\0.0398&-0.0909\\\end{bmatrix}}.}
  

Now find:

  
    
      
        
          
            
              
                
                  T
                
              
              
                
                =
                −
                
                  
                    [
                    
                      
                        
                          0.0625
                        
                        
                          0.0000
                        
                      
                      
                        
                          0.0398
                        
                        
                          −
                          0.0909
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          0
                        
                        
                          3
                        
                      
                      
                        
                          0
                        
                        
                          0
                        
                      
                    
                    ]
                  
                
                =
                
                  
                    [
                    
                      
                        
                          0.000
                        
                        
                          −
                          0.1875
                        
                      
                      
                        
                          0.000
                        
                        
                          −
                          0.1194
                        
                      
                    
                    ]
                  
                
                ,
              
            
            
              
                
                  c
                
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.0625
                        
                        
                          0.0000
                        
                      
                      
                        
                          0.0398
                        
                        
                          −
                          0.0909
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          11
                        
                      
                      
                        
                          13
                        
                      
                    
                    ]
                  
                
                =
                
                  
                    [
                    
                      
                        
                          0.6875
                        
                      
                      
                        
                          −
                          0.7439
                        
                      
                    
                    ]
                  
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\mathbf {T} &=-{\begin{bmatrix}0.0625&0.0000\\0.0398&-0.0909\end{bmatrix}}{\begin{bmatrix}0&3\\0&0\end{bmatrix}}={\begin{bmatrix}0.000&-0.1875\\0.000&-0.1194\end{bmatrix}},\\[1ex]\mathbf {c} &={\begin{bmatrix}0.0625&0.0000\\0.0398&-0.0909\end{bmatrix}}{\begin{bmatrix}11\\13\end{bmatrix}}={\begin{bmatrix}0.6875\\-0.7439\end{bmatrix}}.\end{aligned}}}
  

With 
  
    
      
        
          T
        
      
    
    {\displaystyle \mathbf {T} }
  
 and 
  
    
      
        
          c
        
      
    
    {\displaystyle \mathbf {c} }
  
 the vectors 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
 can be obtained iteratively.
First of all, choose 
  
    
      
        
          
            x
          
          
            (
            0
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(0)}}
  
, for example 
  
    
      
        
          
            x
          
          
            (
            0
            )
          
        
        =
        
          
            [
            
              
                
                  1.0
                
              
              
                
                  1.0
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle \mathbf {x} ^{(0)}={\begin{bmatrix}1.0\\1.0\end{bmatrix}}.}
  
 The closer the guess to the final solution, the fewer iterations the algorithm will need.
Then calculate:

  
    
      
        
          
            
              
                
                  
                    x
                  
                  
                    (
                    1
                    )
                  
                
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.000
                        
                        
                          −
                          0.1875
                        
                      
                      
                        
                          0.000
                        
                        
                          −
                          0.1193
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          1.0
                        
                      
                      
                        
                          1.0
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          0.6875
                        
                      
                      
                        
                          −
                          0.7443
                        
                      
                    
                    ]
                  
                
                =
                
                  
                    [
                    
                      
                        
                          0.5000
                        
                      
                      
                        
                          −
                          0.8636
                        
                      
                    
                    ]
                  
                
                .
              
            
            
              
                
                  
                    x
                  
                  
                    (
                    2
                    )
                  
                
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.000
                        
                        
                          −
                          0.1875
                        
                      
                      
                        
                          0.000
                        
                        
                          −
                          0.1193
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          0.5000
                        
                      
                      
                        
                          −
                          0.8636
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          0.6875
                        
                      
                      
                        
                          −
                          0.7443
                        
                      
                    
                    ]
                  
                
                =
                
                  
                    [
                    
                      
                        
                          0.8494
                        
                      
                      
                        
                          −
                          0.6413
                        
                      
                    
                    ]
                  
                
                .
              
            
            
              
                
                  
                    x
                  
                  
                    (
                    3
                    )
                  
                
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.000
                        
                        
                          −
                          0.1875
                        
                      
                      
                        
                          0.000
                        
                        
                          −
                          0.1193
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          0.8494
                        
                      
                      
                        
                          −
                          0.6413
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          0.6875
                        
                      
                      
                        
                          −
                          0.7443
                        
                      
                    
                    ]
                  
                
                =
                
                  
                    [
                    
                      
                        
                          0.8077
                        
                      
                      
                        
                          −
                          0.6678
                        
                      
                    
                    ]
                  
                
                .
              
            
            
              
                
                  
                    x
                  
                  
                    (
                    4
                    )
                  
                
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.000
                        
                        
                          −
                          0.1875
                        
                      
                      
                        
                          0.000
                        
                        
                          −
                          0.1193
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          0.8077
                        
                      
                      
                        
                          −
                          0.6678
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          0.6875
                        
                      
                      
                        
                          −
                          0.7443
                        
                      
                    
                    ]
                  
                
                =
                
                  
                    [
                    
                      
                        
                          0.8127
                        
                      
                      
                        
                          −
                          0.6646
                        
                      
                    
                    ]
                  
                
                .
              
            
            
              
                
                  
                    x
                  
                  
                    (
                    5
                    )
                  
                
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.000
                        
                        
                          −
                          0.1875
                        
                      
                      
                        
                          0.000
                        
                        
                          −
                          0.1193
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          0.8127
                        
                      
                      
                        
                          −
                          0.6646
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          0.6875
                        
                      
                      
                        
                          −
                          0.7443
                        
                      
                    
                    ]
                  
                
                =
                
                  
                    [
                    
                      
                        
                          0.8121
                        
                      
                      
                        
                          −
                          0.6650
                        
                      
                    
                    ]
                  
                
                .
              
            
            
              
                
                  
                    x
                  
                  
                    (
                    6
                    )
                  
                
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.000
                        
                        
                          −
                          0.1875
                        
                      
                      
                        
                          0.000
                        
                        
                          −
                          0.1193
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          0.8121
                        
                      
                      
                        
                          −
                          0.6650
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          0.6875
                        
                      
                      
                        
                          −
                          0.7443
                        
                      
                    
                    ]
                  
                
                =
                
                  
                    [
                    
                      
                        
                          0.8122
                        
                      
                      
                        
                          −
                          0.6650
                        
                      
                    
                    ]
                  
                
                .
              
            
            
              
                
                  
                    x
                  
                  
                    (
                    7
                    )
                  
                
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.000
                        
                        
                          −
                          0.1875
                        
                      
                      
                        
                          0.000
                        
                        
                          −
                          0.1193
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          0.8122
                        
                      
                      
                        
                          −
                          0.6650
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          0.6875
                        
                      
                      
                        
                          −
                          0.7443
                        
                      
                    
                    ]
                  
                
                =
                
                  
                    [
                    
                      
                        
                          0.8122
                        
                      
                      
                        
                          −
                          0.6650
                        
                      
                    
                    ]
                  
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\mathbf {x} ^{(1)}&={\begin{bmatrix}0.000&-0.1875\\0.000&-0.1193\end{bmatrix}}{\begin{bmatrix}1.0\\1.0\end{bmatrix}}+{\begin{bmatrix}0.6875\\-0.7443\end{bmatrix}}={\begin{bmatrix}0.5000\\-0.8636\end{bmatrix}}.\\[1ex]\mathbf {x} ^{(2)}&={\begin{bmatrix}0.000&-0.1875\\0.000&-0.1193\end{bmatrix}}{\begin{bmatrix}0.5000\\-0.8636\end{bmatrix}}+{\begin{bmatrix}0.6875\\-0.7443\end{bmatrix}}={\begin{bmatrix}0.8494\\-0.6413\end{bmatrix}}.\\[1ex]\mathbf {x} ^{(3)}&={\begin{bmatrix}0.000&-0.1875\\0.000&-0.1193\end{bmatrix}}{\begin{bmatrix}0.8494\\-0.6413\\\end{bmatrix}}+{\begin{bmatrix}0.6875\\-0.7443\end{bmatrix}}={\begin{bmatrix}0.8077\\-0.6678\end{bmatrix}}.\\[1ex]\mathbf {x} ^{(4)}&={\begin{bmatrix}0.000&-0.1875\\0.000&-0.1193\end{bmatrix}}{\begin{bmatrix}0.8077\\-0.6678\end{bmatrix}}+{\begin{bmatrix}0.6875\\-0.7443\end{bmatrix}}={\begin{bmatrix}0.8127\\-0.6646\end{bmatrix}}.\\[1ex]\mathbf {x} ^{(5)}&={\begin{bmatrix}0.000&-0.1875\\0.000&-0.1193\end{bmatrix}}{\begin{bmatrix}0.8127\\-0.6646\end{bmatrix}}+{\begin{bmatrix}0.6875\\-0.7443\end{bmatrix}}={\begin{bmatrix}0.8121\\-0.6650\end{bmatrix}}.\\[1ex]\mathbf {x} ^{(6)}&={\begin{bmatrix}0.000&-0.1875\\0.000&-0.1193\end{bmatrix}}{\begin{bmatrix}0.8121\\-0.6650\end{bmatrix}}+{\begin{bmatrix}0.6875\\-0.7443\end{bmatrix}}={\begin{bmatrix}0.8122\\-0.6650\end{bmatrix}}.\\[1ex]\mathbf {x} ^{(7)}&={\begin{bmatrix}0.000&-0.1875\\0.000&-0.1193\end{bmatrix}}{\begin{bmatrix}0.8122\\-0.6650\end{bmatrix}}+{\begin{bmatrix}0.6875\\-0.7443\end{bmatrix}}={\begin{bmatrix}0.8122\\-0.6650\end{bmatrix}}.\end{aligned}}}
  

As expected, the algorithm converges to the solution:

  
    
      
        
          x
        
        =
        
          
            A
          
          
            −
            1
          
        
        
          b
        
        ≈
        
          
            [
            
              
                
                  0.8122
                
              
              
                
                  −
                  0.6650
                
              
            
            ]
          
        
      
    
    {\displaystyle \mathbf {x} =\mathbf {A} ^{-1}\mathbf {b} \approx {\begin{bmatrix}0.8122\\-0.6650\end{bmatrix}}}
  
.
In fact, the matrix A is strictly diagonally dominant, but not positive definite.

Another example for the matrix version
Another linear system shown as 
  
    
      
        
          A
        
        
          x
        
        =
        
          b
        
      
    
    {\displaystyle \mathbf {A} \mathbf {x} =\mathbf {b} }
  
 is given by:

  
    
      
        
          A
        
        =
        
          
            [
            
              
                
                  2
                
                
                  3
                
              
              
                
                  5
                
                
                  7
                
              
            
            ]
          
        
        
        
          and
        
        
        
          b
        
        =
        
          
            [
            
              
                
                  11
                
              
              
                
                  13
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle \mathbf {A} ={\begin{bmatrix}2&3\\5&7\\\end{bmatrix}}\quad {\text{and}}\quad \mathbf {b} ={\begin{bmatrix}11\\13\\\end{bmatrix}}.}
  

Use the equation

  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
        =
        
          
            L
          
          
            −
            1
          
        
        (
        
          b
        
        −
        
          U
        
        
          
            x
          
          
            (
            k
            )
          
        
        )
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}=\mathbf {L} ^{-1}(\mathbf {b} -\mathbf {U} \mathbf {x} ^{(k)})}
  

in the form

  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
        =
        
          T
        
        
          
            x
          
          
            (
            k
            )
          
        
        +
        
          c
        
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}=\mathbf {T} \mathbf {x} ^{(k)}+\mathbf {c} }
  

where:

  
    
      
        
          T
        
        =
        −
        
          
            L
          
          
            −
            1
          
        
        
          U
        
        
        
          and
        
        
        
          c
        
        =
        
          
            L
          
          
            −
            1
          
        
        
          b
        
        .
      
    
    {\displaystyle \mathbf {T} =-\mathbf {L} ^{-1}\mathbf {U} \quad {\text{and}}\quad \mathbf {c} =\mathbf {L} ^{-1}\mathbf {b} .}
  

Decompose 
  
    
      
        
          A
        
      
    
    {\displaystyle \mathbf {A} }
  
 into the sum of a lower triangular component 
  
    
      
        
          L
        
      
    
    {\displaystyle \mathbf {L} }
  
 and a strict upper triangular component 
  
    
      
        
          U
        
      
    
    {\displaystyle \mathbf {U} }
  
:

  
    
      
        
          L
        
        =
        
          
            [
            
              
                
                  2
                
                
                  0
                
              
              
                
                  5
                
                
                  7
                
              
            
            ]
          
        
        
        
          and
        
        
        
          U
        
        =
        
          
            [
            
              
                
                  0
                
                
                  3
                
              
              
                
                  0
                
                
                  0
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle \mathbf {L} ={\begin{bmatrix}2&0\\5&7\\\end{bmatrix}}\quad {\text{and}}\quad \mathbf {U} ={\begin{bmatrix}0&3\\0&0\\\end{bmatrix}}.}
  

The inverse of 
  
    
      
        
          L
        
      
    
    {\displaystyle \mathbf {L} }
  
 is:

  
    
      
        
          
            L
          
          
            −
            1
          
        
        =
        
          
            
              [
              
                
                  
                    2
                  
                  
                    0
                  
                
                
                  
                    5
                  
                  
                    7
                  
                
              
              ]
            
          
          
            −
            1
          
        
        =
        
          
            [
            
              
                
                  0.500
                
                
                  0.000
                
              
              
                
                  −
                  0.357
                
                
                  0.143
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle \mathbf {L} ^{-1}={\begin{bmatrix}2&0\\5&7\\\end{bmatrix}}^{-1}={\begin{bmatrix}0.500&0.000\\-0.357&0.143\\\end{bmatrix}}.}
  

Now find:

  
    
      
        
          
            
              
                
                  T
                
              
              
                
                =
                −
                
                  
                    [
                    
                      
                        
                          0.500
                        
                        
                          0.000
                        
                      
                      
                        
                          −
                          0.357
                        
                        
                          0.143
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          0
                        
                        
                          3
                        
                      
                      
                        
                          0
                        
                        
                          0
                        
                      
                    
                    ]
                  
                
                =
                
                  
                    [
                    
                      
                        
                          0.000
                        
                        
                          −
                          1.500
                        
                      
                      
                        
                          0.000
                        
                        
                          1.071
                        
                      
                    
                    ]
                  
                
                ,
              
            
            
              
                
                  c
                
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.500
                        
                        
                          0.000
                        
                      
                      
                        
                          −
                          0.357
                        
                        
                          0.143
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          11
                        
                      
                      
                        
                          13
                        
                      
                    
                    ]
                  
                
                =
                
                  
                    [
                    
                      
                        
                          5.500
                        
                      
                      
                        
                          −
                          2.071
                        
                      
                    
                    ]
                  
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\mathbf {T} &=-{\begin{bmatrix}0.500&0.000\\-0.357&0.143\\\end{bmatrix}}{\begin{bmatrix}0&3\\0&0\\\end{bmatrix}}={\begin{bmatrix}0.000&-1.500\\0.000&1.071\\\end{bmatrix}},\\[1ex]\mathbf {c} &={\begin{bmatrix}0.500&0.000\\-0.357&0.143\\\end{bmatrix}}{\begin{bmatrix}11\\13\\\end{bmatrix}}={\begin{bmatrix}5.500\\-2.071\\\end{bmatrix}}.\end{aligned}}}
  

With 
  
    
      
        
          T
        
      
    
    {\displaystyle \mathbf {T} }
  
 and 
  
    
      
        
          c
        
      
    
    {\displaystyle \mathbf {c} }
  
 the vectors 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
 can be obtained iteratively.
First of all, we have to choose 
  
    
      
        
          
            x
          
          
            (
            0
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(0)}}
  
, for example 
  
    
      
        
          
            x
          
          
            (
            0
            )
          
        
        =
        
          
            [
            
              
                
                  1.1
                
              
              
                
                  2.3
                
              
            
            ]
          
        
      
    
    {\displaystyle \mathbf {x} ^{(0)}={\begin{bmatrix}1.1\\2.3\end{bmatrix}}}
  

Then calculate:

  
    
      
        
          
            
              
                
                  
                    x
                  
                  
                    (
                    1
                    )
                  
                
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0
                        
                        
                          −
                          1.500
                        
                      
                      
                        
                          0
                        
                        
                          1.071
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          1.1
                        
                      
                      
                        
                          2.3
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          5.500
                        
                      
                      
                        
                          −
                          2.071
                        
                      
                    
                    ]
                  
                
                =
                
                  
                    [
                    
                      
                        
                          2.050
                        
                      
                      
                        
                          0.393
                        
                      
                    
                    ]
                  
                
                .
              
            
            
              
                
                  
                    x
                  
                  
                    (
                    2
                    )
                  
                
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0
                        
                        
                          −
                          1.500
                        
                      
                      
                        
                          0
                        
                        
                          1.071
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          2.050
                        
                      
                      
                        
                          0.393
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          5.500
                        
                      
                      
                        
                          −
                          2.071
                        
                      
                    
                    ]
                  
                
                =
                
                  
                    [
                    
                      
                        
                          4.911
                        
                      
                      
                        
                          −
                          1.651
                        
                      
                    
                    ]
                  
                
                .
              
            
            
              
                
                  
                    x
                  
                  
                    (
                    3
                    )
                  
                
              
              
                
                =
                ⋯
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\mathbf {x} ^{(1)}&={\begin{bmatrix}0&-1.500\\0&1.071\\\end{bmatrix}}{\begin{bmatrix}1.1\\2.3\\\end{bmatrix}}+{\begin{bmatrix}5.500\\-2.071\\\end{bmatrix}}={\begin{bmatrix}2.050\\0.393\\\end{bmatrix}}.\\[1ex]\mathbf {x} ^{(2)}&={\begin{bmatrix}0&-1.500\\0&1.071\\\end{bmatrix}}{\begin{bmatrix}2.050\\0.393\\\end{bmatrix}}+{\begin{bmatrix}5.500\\-2.071\\\end{bmatrix}}={\begin{bmatrix}4.911\\-1.651\end{bmatrix}}.\\[1ex]\mathbf {x} ^{(3)}&=\cdots .\end{aligned}}}
  

In a test for convergence we find that the algorithm diverges. In fact, the matrix 
  
    
      
        
          A
        
      
    
    {\displaystyle \mathbf {A} }
  
 is neither diagonally dominant nor positive definite.
Then, convergence to the exact solution

  
    
      
        
          x
        
        =
        
          
            A
          
          
            −
            1
          
        
        
          b
        
        =
        
          
            [
            
              
                
                  −
                  38
                
              
              
                
                  29
                
              
            
            ]
          
        
      
    
    {\displaystyle \mathbf {x} =\mathbf {A} ^{-1}\mathbf {b} ={\begin{bmatrix}-38\\29\end{bmatrix}}}
  

is not guaranteed and, in this case, will not occur.

An example for the equation version
Suppose given 
  
    
      
        n
      
    
    {\displaystyle n}
  
 equations and a starting point 
  
    
      
        
          
            x
          
          
            0
          
        
      
    
    {\displaystyle \mathbf {x} _{0}}
  
.
At any step in a Gauss-Seidel iteration, solve the first equation for 
  
    
      
        
          x
          
            1
          
        
      
    
    {\displaystyle x_{1}}
  
 in terms of 
  
    
      
        
          x
          
            2
          
        
        ,
        …
        ,
        
          x
          
            n
          
        
      
    
    {\displaystyle x_{2},\dots ,x_{n}}
  
; then solve the second equation for 
  
    
      
        
          x
          
            2
          
        
      
    
    {\displaystyle x_{2}}
  
 in terms of 
  
    
      
        
          x
          
            1
          
        
      
    
    {\displaystyle x_{1}}
  
 just found and the remaining 
  
    
      
        
          x
          
            3
          
        
        ,
        …
        ,
        
          x
          
            n
          
        
      
    
    {\displaystyle x_{3},\dots ,x_{n}}
  
; and continue to 
  
    
      
        
          x
          
            n
          
        
      
    
    {\displaystyle x_{n}}
  
. Then, repeat iterations until convergence is achieved, or break if the divergence in the solutions start to diverge beyond a predefined level.
Consider an example:

  
    
      
        
          
            
              
                10
                
                  x
                  
                    1
                  
                
              
              
                −
                
                  x
                  
                    2
                  
                
              
              
                +
                2
                
                  x
                  
                    3
                  
                
              
              
              
                =
                6
                ,
              
            
            
              
                −
                
                  x
                  
                    1
                  
                
              
              
                +
                11
                
                  x
                  
                    2
                  
                
              
              
                −
                
                  x
                  
                    3
                  
                
              
              
                +
                3
                
                  x
                  
                    4
                  
                
              
              
                =
                25
                ,
              
            
            
              
                2
                
                  x
                  
                    1
                  
                
              
              
                −
                
                  x
                  
                    2
                  
                
              
              
                +
                10
                
                  x
                  
                    3
                  
                
              
              
                −
                
                  x
                  
                    4
                  
                
              
              
                =
                −
                11
                ,
              
            
            
              
              
                3
                
                  x
                  
                    2
                  
                
              
              
                −
                
                  x
                  
                    3
                  
                
              
              
                +
                8
                
                  x
                  
                    4
                  
                
              
              
                =
                15.
              
            
          
        
      
    
    {\displaystyle {\begin{array}{rrrrl}10x_{1}&-x_{2}&+2x_{3}&&=6,\\-x_{1}&+11x_{2}&-x_{3}&+3x_{4}&=25,\\2x_{1}&-x_{2}&+10x_{3}&-x_{4}&=-11,\\&3x_{2}&-x_{3}&+8x_{4}&=15.\end{array}}}
  

Solving for 
  
    
      
        
          x
          
            1
          
        
        ,
        
          x
          
            2
          
        
        ,
        
          x
          
            3
          
        
      
    
    {\displaystyle x_{1},x_{2},x_{3}}
  
 and 
  
    
      
        
          x
          
            4
          
        
      
    
    {\displaystyle x_{4}}
  
 gives:

  
    
      
        
          
            
              
                
                  x
                  
                    1
                  
                
              
              
                
                =
                
                  x
                  
                    2
                  
                
                
                  /
                
                10
                −
                
                  x
                  
                    3
                  
                
                
                  /
                
                5
                +
                3
                
                  /
                
                5
                ,
              
            
            
              
                
                  x
                  
                    2
                  
                
              
              
                
                =
                
                  x
                  
                    1
                  
                
                
                  /
                
                11
                +
                
                  x
                  
                    3
                  
                
                
                  /
                
                11
                −
                3
                
                  x
                  
                    4
                  
                
                
                  /
                
                11
                +
                25
                
                  /
                
                11
                ,
              
            
            
              
                
                  x
                  
                    3
                  
                
              
              
                
                =
                −
                
                  x
                  
                    1
                  
                
                
                  /
                
                5
                +
                
                  x
                  
                    2
                  
                
                
                  /
                
                10
                +
                
                  x
                  
                    4
                  
                
                
                  /
                
                10
                −
                11
                
                  /
                
                10
                ,
              
            
            
              
                
                  x
                  
                    4
                  
                
              
              
                
                =
                −
                3
                
                  x
                  
                    2
                  
                
                
                  /
                
                8
                +
                
                  x
                  
                    3
                  
                
                
                  /
                
                8
                +
                15
                
                  /
                
                8.
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}x_{1}&=x_{2}/10-x_{3}/5+3/5,\\x_{2}&=x_{1}/11+x_{3}/11-3x_{4}/11+25/11,\\x_{3}&=-x_{1}/5+x_{2}/10+x_{4}/10-11/10,\\x_{4}&=-3x_{2}/8+x_{3}/8+15/8.\end{aligned}}}
  

Suppose (0, 0, 0, 0) is the initial approximation, then the first approximate solution is given by:

  
    
      
        
          
            
              
                
                  x
                  
                    1
                  
                
              
              
                
                =
                3
                
                  /
                
                5
                =
                0.6
                ,
              
            
            
              
                
                  x
                  
                    2
                  
                
              
              
                
                =
                (
                3
                
                  /
                
                5
                )
                
                  /
                
                11
                +
                25
                
                  /
                
                11
                =
                3
                
                  /
                
                55
                +
                25
                
                  /
                
                11
                =
                2.3272
                ,
              
            
            
              
                
                  x
                  
                    3
                  
                
              
              
                
                =
                −
                (
                3
                
                  /
                
                5
                )
                
                  /
                
                5
                +
                (
                2.3272
                )
                
                  /
                
                10
                −
                11
                
                  /
                
                10
                =
                −
                3
                
                  /
                
                25
                +
                0.23272
                −
                1.1
                =
                −
                0.9873
                ,
              
            
            
              
                
                  x
                  
                    4
                  
                
              
              
                
                =
                −
                3
                (
                2.3272
                )
                
                  /
                
                8
                +
                (
                −
                0.9873
                )
                
                  /
                
                8
                +
                15
                
                  /
                
                8
                =
                0.8789.
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}x_{1}&=3/5=0.6,\\x_{2}&=(3/5)/11+25/11=3/55+25/11=2.3272,\\x_{3}&=-(3/5)/5+(2.3272)/10-11/10=-3/25+0.23272-1.1=-0.9873,\\x_{4}&=-3(2.3272)/8+(-0.9873)/8+15/8=0.8789.\end{aligned}}}
  

Using the approximations obtained, the iterative procedure is repeated until the desired accuracy has been reached. The following are the approximated solutions after four iterations.

The exact solution of the system is (1, 2, −1, 1).

An example using Python and NumPy
The following iterative procedure produces the solution vector of a linear system of equations:

Produces the output:

Program to solve arbitrary number of equations using Matlab
The following code uses the formula

  
    
      
        
          x
          
            i
          
          
            (
            k
            +
            1
            )
          
        
        =
        
          
            1
            
              a
              
                i
                i
              
            
          
        
        
          (
          
            
              b
              
                i
              
            
            −
            
              ∑
              
                j
                <
                i
              
            
            
              a
              
                i
                j
              
            
            
              x
              
                j
              
              
                (
                k
                +
                1
                )
              
            
            −
            
              ∑
              
                j
                >
                i
              
            
            
              a
              
                i
                j
              
            
            
              x
              
                j
              
              
                (
                k
                )
              
            
          
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
              
            
            
              
                k
                =
                0
                ,
                1
                ,
                2
                ,
                …
              
            
          
        
      
    
    {\displaystyle x_{i}^{(k+1)}={\frac {1}{a_{ii}}}\left(b_{i}-\sum _{j<i}a_{ij}x_{j}^{(k+1)}-\sum _{j>i}a_{ij}x_{j}^{(k)}\right),\quad {\begin{array}{l}i=1,2,\ldots ,n\\k=0,1,2,\ldots \end{array}}}

See also
Conjugate gradient method
Gaussian belief propagation
Iterative method: Linear systems
Kaczmarz method (a "row-oriented" method, whereas Gauss-Seidel is "column-oriented." See, for example, this paper.)
Matrix splitting
Richardson iteration

Notes
References
Gauss, Carl Friedrich (1903), Werke (in German), vol. 9, Göttingen: Köninglichen Gesellschaft der Wissenschaften.
Golub, Gene H.; Van Loan, Charles F. (1996), Matrix Computations (3rd ed.), Baltimore: Johns Hopkins, ISBN 978-0-8018-5414-9.
Black, Noel & Moore, Shirley. "Gauss-Seidel Method". MathWorld.
This article incorporates text from the article Gauss-Seidel_method on CFD-Wiki that is under the GFDL license.

External links
"Seidel method", Encyclopedia of Mathematics, EMS Press, 2001 [1994]
Gauss–Seidel from www.math-linux.com
Gauss–Seidel From Holistic Numerical Methods Institute
Gauss Siedel Iteration from www.geocities.com
The Gauss-Seidel Method
Bickson
Matlab code
C code example

## Archive Info
- **Archived on:** 2024-12-15 15:18:44 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 87976 bytes
- **Word Count:** 3114 words
