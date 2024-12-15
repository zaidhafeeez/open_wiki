# Successive over-relaxation

## Metadata
- **Last Updated:** 2024-12-03 07:01:37 UTC
- **Original Article:** [Successive over-relaxation](https://en.wikipedia.org/wiki/Successive_over-relaxation)
- **Language:** en
- **Page ID:** 4068447

## Summary
In numerical linear algebra, the method of successive over-relaxation (SOR) is a variant of the Gauss–Seidel method for solving a linear system of equations, resulting in faster convergence. A similar method can be used for any slowly converging iterative process.
It was devised simultaneously by David M. Young Jr. and by Stanley P. Frankel in 1950 for the purpose of automatically solving linear systems on digital computers. Over-relaxation methods had been used before the work of Young and Frankel. An example is the method of Lewis Fry Richardson, and the methods developed by R. V. Southwell. However, these methods were designed for computation by human calculators, requiring some expertise to ensure convergence to the solution which made them inapplicable for programming on digital computers. These aspects are discussed in the thesis of David M. Young Jr.

## Categories
This article belongs to the following categories:

- Category:Articles with example Python (programming language) code
- Category:Articles with example pseudocode
- Category:Articles with short description
- Category:Numerical linear algebra
- Category:Relaxation (iterative methods)
- Category:Short description matches Wikidata
- Category:Wikipedia articles licensed under the GNU Free Document License

## Table of Contents

- Formulation
- Convergence
- Algorithm
- Example
- Symmetric successive over-relaxation
- Other applications of the method
- See also
- Notes
- References
- External links

## Content

In numerical linear algebra, the method of successive over-relaxation (SOR) is a variant of the Gauss–Seidel method for solving a linear system of equations, resulting in faster convergence. A similar method can be used for any slowly converging iterative process.
It was devised simultaneously by David M. Young Jr. and by Stanley P. Frankel in 1950 for the purpose of automatically solving linear systems on digital computers. Over-relaxation methods had been used before the work of Young and Frankel. An example is the method of Lewis Fry Richardson, and the methods developed by R. V. Southwell. However, these methods were designed for computation by human calculators, requiring some expertise to ensure convergence to the solution which made them inapplicable for programming on digital computers. These aspects are discussed in the thesis of David M. Young Jr.

Formulation
Given a square system of n linear equations with unknown x:

  
    
      
        A
        
          x
        
        =
        
          b
        
      
    
    {\displaystyle A\mathbf {x} =\mathbf {b} }
  

where:

  
    
      
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
      
    
    {\displaystyle A={\begin{bmatrix}a_{11}&a_{12}&\cdots &a_{1n}\\a_{21}&a_{22}&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\a_{n1}&a_{n2}&\cdots &a_{nn}\end{bmatrix}},\qquad \mathbf {x} ={\begin{bmatrix}x_{1}\\x_{2}\\\vdots \\x_{n}\end{bmatrix}},\qquad \mathbf {b} ={\begin{bmatrix}b_{1}\\b_{2}\\\vdots \\b_{n}\end{bmatrix}}.}
  

Then A can be decomposed into a diagonal component D, and strictly lower and upper triangular components L and U:

  
    
      
        A
        =
        D
        +
        L
        +
        U
        ,
      
    
    {\displaystyle A=D+L+U,}
  

where

  
    
      
        D
        =
        
          
            [
            
              
                
                  
                    a
                    
                      11
                    
                  
                
                
                  0
                
                
                  ⋯
                
                
                  0
                
              
              
                
                  0
                
                
                  
                    a
                    
                      22
                    
                  
                
                
                  ⋯
                
                
                  0
                
              
              
                
                  ⋮
                
                
                  ⋮
                
                
                  ⋱
                
                
                  ⋮
                
              
              
                
                  0
                
                
                  0
                
                
                  ⋯
                
                
                  
                    a
                    
                      n
                      n
                    
                  
                
              
            
            ]
          
        
        ,
        
        L
        =
        
          
            [
            
              
                
                  0
                
                
                  0
                
                
                  ⋯
                
                
                  0
                
              
              
                
                  
                    a
                    
                      21
                    
                  
                
                
                  0
                
                
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
                
                
                  0
                
              
            
            ]
          
        
        ,
        
        U
        =
        
          
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
          
        
        .
      
    
    {\displaystyle D={\begin{bmatrix}a_{11}&0&\cdots &0\\0&a_{22}&\cdots &0\\\vdots &\vdots &\ddots &\vdots \\0&0&\cdots &a_{nn}\end{bmatrix}},\quad L={\begin{bmatrix}0&0&\cdots &0\\a_{21}&0&\cdots &0\\\vdots &\vdots &\ddots &\vdots \\a_{n1}&a_{n2}&\cdots &0\end{bmatrix}},\quad U={\begin{bmatrix}0&a_{12}&\cdots &a_{1n}\\0&0&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\0&0&\cdots &0\end{bmatrix}}.}
  

The system of linear equations may be rewritten as:

  
    
      
        (
        D
        +
        ω
        L
        )
        
          x
        
        =
        ω
        
          b
        
        −
        [
        ω
        U
        +
        (
        ω
        −
        1
        )
        D
        ]
        
          x
        
      
    
    {\displaystyle (D+\omega L)\mathbf {x} =\omega \mathbf {b} -[\omega U+(\omega -1)D]\mathbf {x} }
  

for a constant ω > 1, called the relaxation factor.
The method of successive over-relaxation is an iterative technique that solves the left hand side of this expression for x, using the previous value for x on the right hand side. Analytically, this may be written as:

  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
        =
        (
        D
        +
        ω
        L
        
          )
          
            −
            1
          
        
        
          
            (
          
        
        ω
        
          b
        
        −
        [
        ω
        U
        +
        (
        ω
        −
        1
        )
        D
        ]
        
          
            x
          
          
            (
            k
            )
          
        
        
          
            )
          
        
        =
        
          L
          
            ω
          
        
        
          
            x
          
          
            (
            k
            )
          
        
        +
        
          c
        
        ,
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}=(D+\omega L)^{-1}{\big (}\omega \mathbf {b} -[\omega U+(\omega -1)D]\mathbf {x} ^{(k)}{\big )}=L_{\omega }\mathbf {x} ^{(k)}+\mathbf {c} ,}
  

where 
  
    
      
        
          
            x
          
          
            (
            k
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(k)}}
  
 is the kth approximation or iteration of 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
 and 
  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}}
  
 is the next or k + 1 iteration of 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
.
However, by taking advantage of the triangular form of (D+ωL), the elements of x(k+1) can be computed sequentially using forward substitution:

  
    
      
        
          x
          
            i
          
          
            (
            k
            +
            1
            )
          
        
        =
        (
        1
        −
        ω
        )
        
          x
          
            i
          
          
            (
            k
            )
          
        
        +
        
          
            ω
            
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
        .
      
    
    {\displaystyle x_{i}^{(k+1)}=(1-\omega )x_{i}^{(k)}+{\frac {\omega }{a_{ii}}}\left(b_{i}-\sum _{j<i}a_{ij}x_{j}^{(k+1)}-\sum _{j>i}a_{ij}x_{j}^{(k)}\right),\quad i=1,2,\ldots ,n.}
  

This can again be written analytically in matrix-vector form without the need of inverting the matrix 
  
    
      
        (
        D
        +
        ω
        L
        )
      
    
    {\displaystyle (D+\omega L)}
  
:

  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
        =
        (
        1
        −
        ω
        )
        
          
            x
          
          
            (
            k
            )
          
        
        +
        ω
        
          D
          
            −
            1
          
        
        
          
            (
          
        
        
          b
        
        −
        L
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
        −
        U
        
          
            x
          
          
            (
            k
            )
          
        
        
          
            )
          
        
        .
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}=(1-\omega )\mathbf {x} ^{(k)}+\omega D^{-1}{\big (}\mathbf {b} -L\mathbf {x} ^{(k+1)}-U\mathbf {x} ^{(k)}{\big )}.}

Convergence
The choice of relaxation factor ω is not necessarily easy, and depends upon the properties of the coefficient matrix.  
In 1947, Ostrowski proved that if 
  
    
      
        A
      
    
    {\displaystyle A}
  
 is symmetric and positive-definite then 
  
    
      
        ρ
        (
        
          L
          
            ω
          
        
        )
        <
        1
      
    
    {\displaystyle \rho (L_{\omega })<1}
  
 for 
  
    
      
        0
        <
        ω
        <
        2
      
    
    {\displaystyle 0<\omega <2}
  
. 
Thus, convergence of the iteration process follows, but we are generally interested in faster convergence rather than just convergence.

Convergence Rate
The convergence rate for the SOR method can be analytically derived.
One needs to assume the following

the relaxation parameter is appropriate: 
  
    
      
        ω
        ∈
        (
        0
        ,
        2
        )
      
    
    {\displaystyle \omega \in (0,2)}
  

Jacobi's iteration matrix 
  
    
      
        
          C
          
            Jac
          
        
        :=
        I
        −
        
          D
          
            −
            1
          
        
        A
      
    
    {\displaystyle C_{\text{Jac}}:=I-D^{-1}A}
  
 has only real eigenvalues
Jacobi's method is convergent: 
  
    
      
        μ
        :=
        ρ
        (
        
          C
          
            Jac
          
        
        )
        <
        1
      
    
    {\displaystyle \mu :=\rho (C_{\text{Jac}})<1}
  

the matrix decomposition 
  
    
      
        A
        =
        D
        +
        L
        +
        U
      
    
    {\displaystyle A=D+L+U}
  
 satisfies the property that 
  
    
      
        det
        ⁡
        (
        λ
        D
        +
        z
        L
        +
        
          
            
              1
              z
            
          
        
        U
        )
        =
        det
        ⁡
        (
        λ
        D
        +
        L
        +
        U
        )
      
    
    {\displaystyle \operatorname {det} (\lambda D+zL+{\tfrac {1}{z}}U)=\operatorname {det} (\lambda D+L+U)}
  
 for any 
  
    
      
        z
        ∈
        
          C
        
        ∖
        {
        0
        }
      
    
    {\displaystyle z\in \mathbb {C} \setminus \{0\}}
  
 and 
  
    
      
        λ
        ∈
        
          C
        
      
    
    {\displaystyle \lambda \in \mathbb {C} }
  
.
Then the convergence rate can be expressed as

  
    
      
        ρ
        (
        
          C
          
            ω
          
        
        )
        =
        
          
            {
            
              
                
                  
                    
                      1
                      4
                    
                  
                  
                    
                      (
                      
                        ω
                        μ
                        +
                        
                          
                            
                              ω
                              
                                2
                              
                            
                            
                              μ
                              
                                2
                              
                            
                            −
                            4
                            (
                            ω
                            −
                            1
                            )
                          
                        
                      
                      )
                    
                    
                      2
                    
                  
                  
                  ,
                
                
                  0
                  <
                  ω
                  ≤
                  
                    ω
                    
                      opt
                    
                  
                
              
              
                
                  ω
                  −
                  1
                  
                  ,
                
                
                  
                    ω
                    
                      opt
                    
                  
                  <
                  ω
                  <
                  2
                
              
            
            
          
        
      
    
    {\displaystyle \rho (C_{\omega })={\begin{cases}{\frac {1}{4}}\left(\omega \mu +{\sqrt {\omega ^{2}\mu ^{2}-4(\omega -1)}}\right)^{2}\,,&0<\omega \leq \omega _{\text{opt}}\\\omega -1\,,&\omega _{\text{opt}}<\omega <2\end{cases}}}
  

where the optimal relaxation parameter is given by

  
    
      
        
          ω
          
            opt
          
        
        :=
        1
        +
        
          
            (
            
              
                μ
                
                  1
                  +
                  
                    
                      1
                      −
                      
                        μ
                        
                          2
                        
                      
                    
                  
                
              
            
            )
          
          
            2
          
        
        =
        1
        +
        
          
            
              μ
              
                2
              
            
            4
          
        
        +
        O
        (
        
          μ
          
            3
          
        
        )
        
        .
      
    
    {\displaystyle \omega _{\text{opt}}:=1+\left({\frac {\mu }{1+{\sqrt {1-\mu ^{2}}}}}\right)^{2}=1+{\frac {\mu ^{2}}{4}}+O(\mu ^{3})\,.}
  

In particular, for 
  
    
      
        ω
        =
        1
      
    
    {\displaystyle \omega =1}
  
 (Gauss-Seidel) it holds that 
  
    
      
        ρ
        (
        
          C
          
            ω
          
        
        )
        =
        
          μ
          
            2
          
        
        =
        ρ
        (
        
          C
          
            Jac
          
        
        
          )
          
            2
          
        
      
    
    {\displaystyle \rho (C_{\omega })=\mu ^{2}=\rho (C_{\text{Jac}})^{2}}
  
.
For the optimal 
  
    
      
        ω
      
    
    {\displaystyle \omega }
  
 we get 
  
    
      
        ρ
        (
        
          C
          
            ω
          
        
        )
        =
        
          
            
              1
              −
              
                
                  1
                  −
                  
                    μ
                    
                      2
                    
                  
                
              
            
            
              1
              +
              
                
                  1
                  −
                  
                    μ
                    
                      2
                    
                  
                
              
            
          
        
        =
        
          
            
              μ
              
                2
              
            
            4
          
        
        +
        O
        (
        
          μ
          
            3
          
        
        )
      
    
    {\displaystyle \rho (C_{\omega })={\frac {1-{\sqrt {1-\mu ^{2}}}}{1+{\sqrt {1-\mu ^{2}}}}}={\frac {\mu ^{2}}{4}}+O(\mu ^{3})}
  
, which shows SOR is roughly four times more efficient than Gauss–Seidel.  
The last assumption is satisfied for tridiagonal matrices since 
  
    
      
        Z
        (
        λ
        D
        +
        L
        +
        U
        )
        
          Z
          
            −
            1
          
        
        =
        λ
        D
        +
        z
        L
        +
        
          
            
              1
              z
            
          
        
        U
      
    
    {\displaystyle Z(\lambda D+L+U)Z^{-1}=\lambda D+zL+{\tfrac {1}{z}}U}
  
 for diagonal 
  
    
      
        Z
      
    
    {\displaystyle Z}
  
 with entries 
  
    
      
        
          Z
          
            i
            i
          
        
        =
        
          z
          
            i
            −
            1
          
        
      
    
    {\displaystyle Z_{ii}=z^{i-1}}
  
 and 
  
    
      
        det
        ⁡
        (
        λ
        D
        +
        L
        +
        U
        )
        =
        det
        ⁡
        (
        Z
        (
        λ
        D
        +
        L
        +
        U
        )
        
          Z
          
            −
            1
          
        
        )
      
    
    {\displaystyle \operatorname {det} (\lambda D+L+U)=\operatorname {det} (Z(\lambda D+L+U)Z^{-1})}
  
.

Algorithm
Since elements can be overwritten as they are computed in this algorithm, only one storage vector is needed, and vector indexing is omitted. The algorithm goes as follows:

Inputs: A, b, ω
Output: φ

Choose an initial guess φ to the solution
repeat until convergence
    for i from 1 until n do
        set σ to 0
        for j from 1 until n do
            if j ≠ i then
                set σ to σ + aij φj
            end if
        end (j-loop)
        set φi to (1 − ω)φi + ω(bi − σ) / aii
    end (i-loop)
    check if convergence is reached
end (repeat)

Note

  
    
      
        (
        1
        −
        ω
        )
        
          ϕ
          
            i
          
        
        +
        
          
            ω
            
              a
              
                i
                i
              
            
          
        
        (
        
          b
          
            i
          
        
        −
        σ
        )
      
    
    {\displaystyle (1-\omega )\phi _{i}+{\frac {\omega }{a_{ii}}}(b_{i}-\sigma )}
  
 can also be written 
  
    
      
        
          ϕ
          
            i
          
        
        +
        ω
        
          (
          
            
              
                
                  
                    b
                    
                      i
                    
                  
                  −
                  σ
                
                
                  a
                  
                    i
                    i
                  
                
              
            
            −
            
              ϕ
              
                i
              
            
          
          )
        
      
    
    {\displaystyle \phi _{i}+\omega \left({\frac {b_{i}-\sigma }{a_{ii}}}-\phi _{i}\right)}
  
, thus saving one multiplication in each iteration of the outer for-loop.

Example
We are presented the linear system

  
    
      
        
          
            
              
                4
                
                  x
                  
                    1
                  
                
                −
                
                  x
                  
                    2
                  
                
                −
                6
                
                  x
                  
                    3
                  
                
                +
                0
                
                  x
                  
                    4
                  
                
              
              
                
                =
                2
                ,
              
            
            
              
                −
                5
                
                  x
                  
                    1
                  
                
                −
                4
                
                  x
                  
                    2
                  
                
                +
                10
                
                  x
                  
                    3
                  
                
                +
                8
                
                  x
                  
                    4
                  
                
              
              
                
                =
                21
                ,
              
            
            
              
                0
                
                  x
                  
                    1
                  
                
                +
                9
                
                  x
                  
                    2
                  
                
                +
                4
                
                  x
                  
                    3
                  
                
                −
                2
                
                  x
                  
                    4
                  
                
              
              
                
                =
                −
                12
                ,
              
            
            
              
                1
                
                  x
                  
                    1
                  
                
                +
                0
                
                  x
                  
                    2
                  
                
                −
                7
                
                  x
                  
                    3
                  
                
                +
                5
                
                  x
                  
                    4
                  
                
              
              
                
                =
                −
                6.
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}4x_{1}-x_{2}-6x_{3}+0x_{4}&=2,\\-5x_{1}-4x_{2}+10x_{3}+8x_{4}&=21,\\0x_{1}+9x_{2}+4x_{3}-2x_{4}&=-12,\\1x_{1}+0x_{2}-7x_{3}+5x_{4}&=-6.\end{aligned}}}
  

To solve the equations, we choose a relaxation factor 
  
    
      
        ω
        =
        0.5
      
    
    {\displaystyle \omega =0.5}
  
 and an initial guess vector 
  
    
      
        ϕ
        =
        (
        0
        ,
        0
        ,
        0
        ,
        0
        )
      
    
    {\displaystyle \phi =(0,0,0,0)}
  
. According to the successive over-relaxation algorithm, the following table is obtained, representing an exemplary iteration with approximations, which ideally, but not necessarily, finds the exact solution, (3, −2, 2, 1), in 38 steps.

A simple implementation of the algorithm in Common Lisp is offered below.

A simple Python implementation of the pseudo-code provided above.

Symmetric successive over-relaxation
The version for symmetric matrices A, in which

  
    
      
        U
        =
        
          L
          
            T
          
        
        ,
        
      
    
    {\displaystyle U=L^{T},\,}
  

is referred to as Symmetric Successive Over-Relaxation, or (SSOR), in which

  
    
      
        P
        =
        
          (
          
            
              
                D
                ω
              
            
            +
            L
          
          )
        
        
          
            ω
            
              2
              −
              ω
            
          
        
        
          D
          
            −
            1
          
        
        
          (
          
            
              
                D
                ω
              
            
            +
            U
          
          )
        
        ,
      
    
    {\displaystyle P=\left({\frac {D}{\omega }}+L\right){\frac {\omega }{2-\omega }}D^{-1}\left({\frac {D}{\omega }}+U\right),}
  

and the iterative method is

  
    
      
        
          
            x
          
          
            k
            +
            1
          
        
        =
        
          
            x
          
          
            k
          
        
        −
        
          γ
          
            k
          
        
        
          P
          
            −
            1
          
        
        (
        A
        
          
            x
          
          
            k
          
        
        −
        
          b
        
        )
        ,
         
        k
        ≥
        0.
      
    
    {\displaystyle \mathbf {x} ^{k+1}=\mathbf {x} ^{k}-\gamma ^{k}P^{-1}(A\mathbf {x} ^{k}-\mathbf {b} ),\ k\geq 0.}
  

The SOR and SSOR methods are credited to David M. Young Jr.

Other applications of the method
A similar technique can be used for any iterative method. If the original iteration had the form

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        f
        (
        
          x
          
            n
          
        
        )
      
    
    {\displaystyle x_{n+1}=f(x_{n})}
  

then the modified version would use

  
    
      
        
          x
          
            n
            +
            1
          
          
            
              S
              O
              R
            
          
        
        =
        (
        1
        −
        ω
        )
        
          x
          
            n
          
          
            
              S
              O
              R
            
          
        
        +
        ω
        f
        (
        
          x
          
            n
          
          
            
              S
              O
              R
            
          
        
        )
        .
      
    
    {\displaystyle x_{n+1}^{\mathrm {SOR} }=(1-\omega )x_{n}^{\mathrm {SOR} }+\omega f(x_{n}^{\mathrm {SOR} }).}
  

However, the formulation presented above, used for solving systems of linear equations, is not a special case of this formulation if x is considered to be the complete vector. If this formulation is used instead, the equation for calculating the next vector will look like

  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
        =
        (
        1
        −
        ω
        )
        
          
            x
          
          
            (
            k
            )
          
        
        +
        ω
        
          L
          
            ∗
          
          
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
        ,
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}=(1-\omega )\mathbf {x} ^{(k)}+\omega L_{*}^{-1}(\mathbf {b} -U\mathbf {x} ^{(k)}),}
  

where 
  
    
      
        
          L
          
            ∗
          
        
        =
        L
        +
        D
      
    
    {\displaystyle L_{*}=L+D}
  
. Values of 
  
    
      
        ω
        >
        1
      
    
    {\displaystyle \omega >1}
  
 are used to speed up convergence of a slow-converging process, while values of 
  
    
      
        ω
        <
        1
      
    
    {\displaystyle \omega <1}
  
 are often used to help establish convergence of a diverging iterative process or speed up the convergence of an overshooting process.
There are various methods that adaptively set the relaxation parameter 
  
    
      
        ω
      
    
    {\displaystyle \omega }
  
 based on the observed behavior of the converging process. Usually they help to reach a super-linear convergence for some problems but fail for the others.

See also
Jacobi method
Gaussian Belief Propagation
Matrix splitting

Notes
References
This article incorporates text from the article Successive_over-relaxation_method_-_SOR on CFD-Wiki that is under the GFDL license.
Abraham Berman, Robert J. Plemmons, Nonnegative Matrices in the Mathematical Sciences, 1994, SIAM. ISBN 0-89871-321-8.
Black, Noel & Moore, Shirley. "Successive Overrelaxation Method". MathWorld.
A. Hadjidimos, Successive overrelaxation (SOR) and related methods, Journal of Computational and Applied Mathematics 123 (2000), 177–199.
Yousef Saad, Iterative Methods for Sparse Linear Systems, 1st edition, PWS, 1996.
Netlib's copy of  "Templates for the Solution of Linear Systems", by Barrett et al.
Richard S. Varga 2002 Matrix Iterative Analysis, Second ed. (of 1962 Prentice Hall edition), Springer-Verlag.
David M. Young Jr. Iterative Solution of Large Linear Systems, Academic Press, 1971. (reprinted by Dover, 2003)

External links
Module for the SOR Method
Tridiagonal linear system solver based on SOR, in C++

## Archive Info
- **Archived on:** 2024-12-15 20:27:01 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 37957 bytes
- **Word Count:** 2124 words
