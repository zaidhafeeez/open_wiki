# Jacobi method

## Article Metadata

- **Last Updated:** 2024-12-14T19:39:14.182704+00:00
- **Original Article:** [Jacobi method](https://en.wikipedia.org/wiki/Jacobi_method)
- **Language:** en
- **Page ID:** 4047104

## Summary

In numerical linear algebra, the Jacobi method (a.k.a. the Jacobi iteration method) is an iterative algorithm for determining the solutions of a strictly diagonally dominant system of linear equations. Each diagonal element is solved for, and an approximate value is plugged in. The process is then iterated until it converges. This algorithm is a stripped-down version of the Jacobi transformation method of matrix diagonalization. The method is named after Carl Gustav Jacob Jacobi.

## Categories

- Category:All articles needing additional references
- Category:Articles needing additional references from September 2024
- Category:Articles with example Python (programming language) code
- Category:Articles with example pseudocode
- Category:Articles with short description
- Category:Numerical linear algebra
- Category:Relaxation (iterative methods)
- Category:Short description matches Wikidata
- Category:Wikipedia articles licensed under the GNU Free Document License

## Table of Contents

- Description
- Algorithm
- Convergence
- Examples
- Weighted Jacobi method
- See also
- References
- External links

## Content

In numerical linear algebra, the Jacobi method (a.k.a. the Jacobi iteration method) is an iterative algorithm for determining the solutions of a strictly diagonally dominant system of linear equations. Each diagonal element is solved for, and an approximate value is plugged in. The process is then iterated until it converges. This algorithm is a stripped-down version of the Jacobi transformation method of matrix diagonalization. The method is named after Carl Gustav Jacob Jacobi.

Description
Let 
  
    
      
        A
        
          x
        
        =
        
          b
        
      
    
    {\displaystyle A\mathbf {x} =\mathbf {b} }
  
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
      
    
    {\displaystyle A={\begin{bmatrix}a_{11}&a_{12}&\cdots &a_{1n}\\a_{21}&a_{22}&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\a_{n1}&a_{n2}&\cdots &a_{nn}\end{bmatrix}},\qquad \mathbf {x} ={\begin{bmatrix}x_{1}\\x_{2}\\\vdots \\x_{n}\end{bmatrix}},\qquad \mathbf {b} ={\begin{bmatrix}b_{1}\\b_{2}\\\vdots \\b_{n}\end{bmatrix}}.}
  

When 
  
    
      
        A
      
    
    {\displaystyle A}
  
 and 
  
    
      
        
          b
        
      
    
    {\displaystyle \mathbf {b} }
  
 are known, and 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
 is unknown, we can use the Jacobi method to approximate 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
. The vector 
  
    
      
        
          
            x
          
          
            (
            0
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(0)}}
  
 denotes our initial guess for 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
 (often 
  
    
      
        
          
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
  
). We denote 
  
    
      
        
          
            x
          
          
            (
            k
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(k)}}
  
 as the k-th approximation or iteration of 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
, and 
  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}}
  
 is the next (or k+1) iteration of 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
.

Matrix-based formula
Then A can be decomposed into a diagonal component D, a lower triangular part L and an upper triangular part U:
  
    
      
        A
        =
        D
        +
        L
        +
        U
        
        
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
          
        
        
           and 
        
        L
        +
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
                    
                  
                
              
              
                
                  
                    a
                    
                      21
                    
                  
                
                
                  0
                
                
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
                
                
                  0
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle A=D+L+U\qquad {\text{where}}\qquad D={\begin{bmatrix}a_{11}&0&\cdots &0\\0&a_{22}&\cdots &0\\\vdots &\vdots &\ddots &\vdots \\0&0&\cdots &a_{nn}\end{bmatrix}}{\text{ and }}L+U={\begin{bmatrix}0&a_{12}&\cdots &a_{1n}\\a_{21}&0&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\a_{n1}&a_{n2}&\cdots &0\end{bmatrix}}.}
  
The solution is then obtained iteratively via

  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
        =
        
          D
          
            −
            1
          
        
        (
        
          b
        
        −
        (
        L
        +
        U
        )
        
          
            x
          
          
            (
            k
            )
          
        
        )
        .
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}=D^{-1}(\mathbf {b} -(L+U)\mathbf {x} ^{(k)}).}

Element-based formula
The element-based formula for each row 
  
    
      
        i
      
    
    {\displaystyle i}
  
 is thus:
  
    
      
        
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
                ≠
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
      
    
    {\displaystyle x_{i}^{(k+1)}={\frac {1}{a_{ii}}}\left(b_{i}-\sum _{j\neq i}a_{ij}x_{j}^{(k)}\right),\quad i=1,2,\ldots ,n.}
  
The computation of 
  
    
      
        
          x
          
            i
          
          
            (
            k
            +
            1
            )
          
        
      
    
    {\displaystyle x_{i}^{(k+1)}}
  
 requires each element in 
  
    
      
        
          
            x
          
          
            (
            k
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(k)}}
  
 except itself. Unlike the Gauss–Seidel method, we can't overwrite 
  
    
      
        
          x
          
            i
          
          
            (
            k
            )
          
        
      
    
    {\displaystyle x_{i}^{(k)}}
  
 with 
  
    
      
        
          x
          
            i
          
          
            (
            k
            +
            1
            )
          
        
      
    
    {\displaystyle x_{i}^{(k+1)}}
  
, as that value will be needed by the rest of the computation. The minimum amount of storage is two vectors of size n.

Algorithm
Input: initial guess x(0) to the solution, (diagonal dominant) matrix A, right-hand side vector b, convergence criterion
Output: solution when convergence is reached
Comments: pseudocode based on the element-based formula above

k = 0
while convergence not reached do
    for i := 1 step until n do
        σ = 0
        for j := 1 step until n do
            if j ≠ i then
                σ = σ + aij xj(k)
            end
        end
        xi(k+1) = (bi − σ) / aii
    end
    increment k
end

Convergence
The standard convergence condition (for any iterative method) is when the spectral radius of the iteration matrix is less than 1:

  
    
      
        ρ
        (
        
          D
          
            −
            1
          
        
        (
        L
        +
        U
        )
        )
        <
        1.
      
    
    {\displaystyle \rho (D^{-1}(L+U))<1.}
  

A sufficient (but not necessary) condition for the method to converge is that the matrix A is strictly or irreducibly diagonally dominant. Strict row diagonal dominance means that for each row, the absolute value of the diagonal term is greater than the sum of absolute values of other terms:

  
    
      
        
          |
          
            a
            
              i
              i
            
          
          |
        
        >
        
          ∑
          
            j
            ≠
            i
          
        
        
          
            |
            
              a
              
                i
                j
              
            
            |
          
        
        .
      
    
    {\displaystyle \left|a_{ii}\right|>\sum _{j\neq i}{\left|a_{ij}\right|}.}
  

The Jacobi method sometimes converges even if these conditions are not satisfied.
Note that the Jacobi method does not converge for every symmetric positive-definite matrix. For example,

  
    
      
        A
        =
        
          
            (
            
              
                
                  29
                
                
                  2
                
                
                  1
                
              
              
                
                  2
                
                
                  6
                
                
                  1
                
              
              
                
                  1
                
                
                  1
                
                
                  
                    
                      1
                      5
                    
                  
                
              
            
            )
          
        
        
        ⇒
        
        
          D
          
            −
            1
          
        
        (
        L
        +
        U
        )
        =
        
          
            (
            
              
                
                  0
                
                
                  
                    
                      2
                      29
                    
                  
                
                
                  
                    
                      1
                      29
                    
                  
                
              
              
                
                  
                    
                      1
                      3
                    
                  
                
                
                  0
                
                
                  
                    
                      1
                      6
                    
                  
                
              
              
                
                  5
                
                
                  5
                
                
                  0
                
              
            
            )
          
        
        
        ⇒
        
        ρ
        (
        
          D
          
            −
            1
          
        
        (
        L
        +
        U
        )
        )
        ≈
        1.0661
        
        .
      
    
    {\displaystyle A={\begin{pmatrix}29&2&1\\2&6&1\\1&1&{\frac {1}{5}}\end{pmatrix}}\quad \Rightarrow \quad D^{-1}(L+U)={\begin{pmatrix}0&{\frac {2}{29}}&{\frac {1}{29}}\\{\frac {1}{3}}&0&{\frac {1}{6}}\\5&5&0\end{pmatrix}}\quad \Rightarrow \quad \rho (D^{-1}(L+U))\approx 1.0661\,.}

Examples
Example question
A linear system of the form 
  
    
      
        A
        x
        =
        b
      
    
    {\displaystyle Ax=b}
  
 with initial estimate 
  
    
      
        
          x
          
            (
            0
            )
          
        
      
    
    {\displaystyle x^{(0)}}
  
 is given by

  
    
      
        A
        =
        
          
            [
            
              
                
                  2
                
                
                  1
                
              
              
                
                  5
                
                
                  7
                
              
            
            ]
          
        
        ,
         
        b
        =
        
          
            [
            
              
                
                  11
                
              
              
                
                  13
                
              
            
            ]
          
        
        
        
          and
        
        
        
          x
          
            (
            0
            )
          
        
        =
        
          
            [
            
              
                
                  1
                
              
              
                
                  1
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle A={\begin{bmatrix}2&1\\5&7\\\end{bmatrix}},\ b={\begin{bmatrix}11\\13\\\end{bmatrix}}\quad {\text{and}}\quad x^{(0)}={\begin{bmatrix}1\\1\\\end{bmatrix}}.}
  

We use the equation 
  
    
      
        
          x
          
            (
            k
            +
            1
            )
          
        
        =
        
          D
          
            −
            1
          
        
        (
        b
        −
        (
        L
        +
        U
        )
        
          x
          
            (
            k
            )
          
        
        )
      
    
    {\displaystyle x^{(k+1)}=D^{-1}(b-(L+U)x^{(k)})}
  
, described above, to estimate 
  
    
      
        x
      
    
    {\displaystyle x}
  
. First, we rewrite the equation in a more convenient form 
  
    
      
        
          D
          
            −
            1
          
        
        (
        b
        −
        (
        L
        +
        U
        )
        
          x
          
            (
            k
            )
          
        
        )
        =
        T
        
          x
          
            (
            k
            )
          
        
        +
        C
      
    
    {\displaystyle D^{-1}(b-(L+U)x^{(k)})=Tx^{(k)}+C}
  
, where 
  
    
      
        T
        =
        −
        
          D
          
            −
            1
          
        
        (
        L
        +
        U
        )
      
    
    {\displaystyle T=-D^{-1}(L+U)}
  
 and 
  
    
      
        C
        =
        
          D
          
            −
            1
          
        
        b
      
    
    {\displaystyle C=D^{-1}b}
  
. From the known values

  
    
      
        
          D
          
            −
            1
          
        
        =
        
          
            [
            
              
                
                  1
                  
                    /
                  
                  2
                
                
                  0
                
              
              
                
                  0
                
                
                  1
                  
                    /
                  
                  7
                
              
            
            ]
          
        
        ,
         
        L
        =
        
          
            [
            
              
                
                  0
                
                
                  0
                
              
              
                
                  5
                
                
                  0
                
              
            
            ]
          
        
        
        
          and
        
        
        U
        =
        
          
            [
            
              
                
                  0
                
                
                  1
                
              
              
                
                  0
                
                
                  0
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle D^{-1}={\begin{bmatrix}1/2&0\\0&1/7\\\end{bmatrix}},\ L={\begin{bmatrix}0&0\\5&0\\\end{bmatrix}}\quad {\text{and}}\quad U={\begin{bmatrix}0&1\\0&0\\\end{bmatrix}}.}
  

we determine 
  
    
      
        T
        =
        −
        
          D
          
            −
            1
          
        
        (
        L
        +
        U
        )
      
    
    {\displaystyle T=-D^{-1}(L+U)}
  
 as

  
    
      
        T
        =
        
          
            [
            
              
                
                  1
                  
                    /
                  
                  2
                
                
                  0
                
              
              
                
                  0
                
                
                  1
                  
                    /
                  
                  7
                
              
            
            ]
          
        
        
          {
          
            
              
                [
                
                  
                    
                      0
                    
                    
                      0
                    
                  
                  
                    
                      −
                      5
                    
                    
                      0
                    
                  
                
                ]
              
            
            +
            
              
                [
                
                  
                    
                      0
                    
                    
                      −
                      1
                    
                  
                  
                    
                      0
                    
                    
                      0
                    
                  
                
                ]
              
            
          
          }
        
        =
        
          
            [
            
              
                
                  0
                
                
                  −
                  1
                  
                    /
                  
                  2
                
              
              
                
                  −
                  5
                  
                    /
                  
                  7
                
                
                  0
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle T={\begin{bmatrix}1/2&0\\0&1/7\\\end{bmatrix}}\left\{{\begin{bmatrix}0&0\\-5&0\\\end{bmatrix}}+{\begin{bmatrix}0&-1\\0&0\\\end{bmatrix}}\right\}={\begin{bmatrix}0&-1/2\\-5/7&0\\\end{bmatrix}}.}
  

Further, 
  
    
      
        C
      
    
    {\displaystyle C}
  
 is found as

  
    
      
        C
        =
        
          
            [
            
              
                
                  1
                  
                    /
                  
                  2
                
                
                  0
                
              
              
                
                  0
                
                
                  1
                  
                    /
                  
                  7
                
              
            
            ]
          
        
        
          
            [
            
              
                
                  11
                
              
              
                
                  13
                
              
            
            ]
          
        
        =
        
          
            [
            
              
                
                  11
                  
                    /
                  
                  2
                
              
              
                
                  13
                  
                    /
                  
                  7
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle C={\begin{bmatrix}1/2&0\\0&1/7\\\end{bmatrix}}{\begin{bmatrix}11\\13\\\end{bmatrix}}={\begin{bmatrix}11/2\\13/7\\\end{bmatrix}}.}
  

With 
  
    
      
        T
      
    
    {\displaystyle T}
  
 and 
  
    
      
        C
      
    
    {\displaystyle C}
  
 calculated, we estimate 
  
    
      
        x
      
    
    {\displaystyle x}
  
 as 
  
    
      
        
          x
          
            (
            1
            )
          
        
        =
        T
        
          x
          
            (
            0
            )
          
        
        +
        C
      
    
    {\displaystyle x^{(1)}=Tx^{(0)}+C}
  
:

  
    
      
        
          x
          
            (
            1
            )
          
        
        =
        
          
            [
            
              
                
                  0
                
                
                  −
                  1
                  
                    /
                  
                  2
                
              
              
                
                  −
                  5
                  
                    /
                  
                  7
                
                
                  0
                
              
            
            ]
          
        
        
          
            [
            
              
                
                  1
                
              
              
                
                  1
                
              
            
            ]
          
        
        +
        
          
            [
            
              
                
                  11
                  
                    /
                  
                  2
                
              
              
                
                  13
                  
                    /
                  
                  7
                
              
            
            ]
          
        
        =
        
          
            [
            
              
                
                  5.0
                
              
              
                
                  8
                  
                    /
                  
                  7
                
              
            
            ]
          
        
        ≈
        
          
            [
            
              
                
                  5
                
              
              
                
                  1.143
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle x^{(1)}={\begin{bmatrix}0&-1/2\\-5/7&0\\\end{bmatrix}}{\begin{bmatrix}1\\1\\\end{bmatrix}}+{\begin{bmatrix}11/2\\13/7\\\end{bmatrix}}={\begin{bmatrix}5.0\\8/7\\\end{bmatrix}}\approx {\begin{bmatrix}5\\1.143\\\end{bmatrix}}.}
  

The next iteration yields

  
    
      
        
          x
          
            (
            2
            )
          
        
        =
        
          
            [
            
              
                
                  0
                
                
                  −
                  1
                  
                    /
                  
                  2
                
              
              
                
                  −
                  5
                  
                    /
                  
                  7
                
                
                  0
                
              
            
            ]
          
        
        
          
            [
            
              
                
                  5.0
                
              
              
                
                  8
                  
                    /
                  
                  7
                
              
            
            ]
          
        
        +
        
          
            [
            
              
                
                  11
                  
                    /
                  
                  2
                
              
              
                
                  13
                  
                    /
                  
                  7
                
              
            
            ]
          
        
        =
        
          
            [
            
              
                
                  69
                  
                    /
                  
                  14
                
              
              
                
                  −
                  12
                  
                    /
                  
                  7
                
              
            
            ]
          
        
        ≈
        
          
            [
            
              
                
                  4.929
                
              
              
                
                  −
                  1.714
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle x^{(2)}={\begin{bmatrix}0&-1/2\\-5/7&0\\\end{bmatrix}}{\begin{bmatrix}5.0\\8/7\\\end{bmatrix}}+{\begin{bmatrix}11/2\\13/7\\\end{bmatrix}}={\begin{bmatrix}69/14\\-12/7\\\end{bmatrix}}\approx {\begin{bmatrix}4.929\\-1.714\\\end{bmatrix}}.}
  

This process is repeated until convergence (i.e., until 
  
    
      
        ‖
        A
        
          x
          
            (
            n
            )
          
        
        −
        b
        ‖
      
    
    {\displaystyle \|Ax^{(n)}-b\|}
  
 is small).  The solution after 25 iterations is

  
    
      
        x
        =
        
          
            [
            
              
                
                  7.111
                
              
              
                
                  −
                  3.222
                
              
            
            ]
          
        
        .
      
    
    {\displaystyle x={\begin{bmatrix}7.111\\-3.222\end{bmatrix}}.}

Example  question 2
Suppose we are given the following linear system:

  
    
      
        
          
            
              
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
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}10x_{1}-x_{2}+2x_{3}&=6,\\-x_{1}+11x_{2}-x_{3}+3x_{4}&=25,\\2x_{1}-x_{2}+10x_{3}-x_{4}&=-11,\\3x_{2}-x_{3}+8x_{4}&=15.\end{aligned}}}
  

If we choose (0, 0, 0, 0) as the initial approximation, then the first approximate solution is given by

  
    
      
        
          
            
              
                
                  x
                  
                    1
                  
                
              
              
                
                =
                (
                6
                +
                0
                −
                (
                2
                ∗
                0
                )
                )
                
                  /
                
                10
                =
                0.6
                ,
              
            
            
              
                
                  x
                  
                    2
                  
                
              
              
                
                =
                (
                25
                +
                0
                +
                0
                −
                (
                3
                ∗
                0
                )
                )
                
                  /
                
                11
                =
                25
                
                  /
                
                11
                =
                2.2727
                ,
              
            
            
              
                
                  x
                  
                    3
                  
                
              
              
                
                =
                (
                −
                11
                −
                (
                2
                ∗
                0
                )
                +
                0
                +
                0
                )
                
                  /
                
                10
                =
                −
                1.1
                ,
              
            
            
              
                
                  x
                  
                    4
                  
                
              
              
                
                =
                (
                15
                −
                (
                3
                ∗
                0
                )
                +
                0
                )
                
                  /
                
                8
                =
                1.875.
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}x_{1}&=(6+0-(2*0))/10=0.6,\\x_{2}&=(25+0+0-(3*0))/11=25/11=2.2727,\\x_{3}&=(-11-(2*0)+0+0)/10=-1.1,\\x_{4}&=(15-(3*0)+0)/8=1.875.\end{aligned}}}
  

Using the approximations obtained, the iterative procedure is repeated until the desired accuracy has been reached. The following are the approximated solutions after five iterations.

The exact solution of the system is (1, 2, −1, 1).

Python example
Weighted Jacobi method
The weighted Jacobi iteration uses a parameter 
  
    
      
        ω
      
    
    {\displaystyle \omega }
  
 to compute the iteration as

  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
        =
        ω
        
          D
          
            −
            1
          
        
        (
        
          b
        
        −
        (
        L
        +
        U
        )
        
          
            x
          
          
            (
            k
            )
          
        
        )
        +
        
          (
          
            1
            −
            ω
          
          )
        
        
          
            x
          
          
            (
            k
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}=\omega D^{-1}(\mathbf {b} -(L+U)\mathbf {x} ^{(k)})+\left(1-\omega \right)\mathbf {x} ^{(k)}}
  

with 
  
    
      
        ω
        =
        2
        
          /
        
        3
      
    
    {\displaystyle \omega =2/3}
  
 being the usual choice.
From the relation 
  
    
      
        L
        +
        U
        =
        A
        −
        D
      
    
    {\displaystyle L+U=A-D}
  
, this may also be expressed as

  
    
      
        
          
            x
          
          
            (
            k
            +
            1
            )
          
        
        =
        ω
        
          D
          
            −
            1
          
        
        
          b
        
        +
        
          (
          
            I
            −
            ω
            
              D
              
                −
                1
              
            
            A
          
          )
        
        
          
            x
          
          
            (
            k
            )
          
        
      
    
    {\displaystyle \mathbf {x} ^{(k+1)}=\omega D^{-1}\mathbf {b} +\left(I-\omega D^{-1}A\right)\mathbf {x} ^{(k)}}
  
.

Convergence in the symmetric positive definite case
In case that the system matrix 
  
    
      
        A
      
    
    {\displaystyle A}
  
 is of symmetric positive-definite type one can show convergence.
Let 
  
    
      
        C
        =
        
          C
          
            ω
          
        
        =
        I
        −
        ω
        
          D
          
            −
            1
          
        
        A
      
    
    {\displaystyle C=C_{\omega }=I-\omega D^{-1}A}
  
 be the iteration matrix.
Then, convergence is guaranteed for

  
    
      
        ρ
        (
        
          C
          
            ω
          
        
        )
        <
        1
        
        ⟺
        
        0
        <
        ω
        <
        
          
            2
            
              
                λ
                
                  max
                
              
              (
              
                D
                
                  −
                  1
                
              
              A
              )
            
          
        
        
        ,
      
    
    {\displaystyle \rho (C_{\omega })<1\quad \Longleftrightarrow \quad 0<\omega <{\frac {2}{\lambda _{\text{max}}(D^{-1}A)}}\,,}
  

where 
  
    
      
        
          λ
          
            max
          
        
      
    
    {\displaystyle \lambda _{\text{max}}}
  
 is the maximal eigenvalue.
The spectral radius can be minimized for a particular choice of 
  
    
      
        ω
        =
        
          ω
          
            opt
          
        
      
    
    {\displaystyle \omega =\omega _{\text{opt}}}
  
 as follows

  
    
      
        
          min
          
            ω
          
        
        ρ
        (
        
          C
          
            ω
          
        
        )
        =
        ρ
        (
        
          C
          
            
              ω
              
                opt
              
            
          
        
        )
        =
        1
        −
        
          
            2
            
              κ
              (
              
                D
                
                  −
                  1
                
              
              A
              )
              +
              1
            
          
        
        
        
          for
        
        
        
          ω
          
            opt
          
        
        :=
        
          
            2
            
              
                λ
                
                  min
                
              
              (
              
                D
                
                  −
                  1
                
              
              A
              )
              +
              
                λ
                
                  max
                
              
              (
              
                D
                
                  −
                  1
                
              
              A
              )
            
          
        
        
        ,
      
    
    {\displaystyle \min _{\omega }\rho (C_{\omega })=\rho (C_{\omega _{\text{opt}}})=1-{\frac {2}{\kappa (D^{-1}A)+1}}\quad {\text{for}}\quad \omega _{\text{opt}}:={\frac {2}{\lambda _{\text{min}}(D^{-1}A)+\lambda _{\text{max}}(D^{-1}A)}}\,,}
  

where 
  
    
      
        κ
      
    
    {\displaystyle \kappa }
  
 is the matrix condition number.

See also
Gauss–Seidel method
Successive over-relaxation
Iterative method § Linear systems
Gaussian Belief Propagation
Matrix splitting

References
External links
This article incorporates text from the article Jacobi_method on CFD-Wiki that is under the GFDL license.
Black, Noel; Moore, Shirley & Weisstein, Eric W. "Jacobi method". MathWorld.
Jacobi Method from www.math-linux.com

## Related Articles

### Internal Links

- [Automatically Tuned Linear Algebra Software](https://en.wikipedia.org/wiki/Automatically_Tuned_Linear_Algebra_Software)
- [Basic Linear Algebra Subprograms](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms)
- [Belief propagation](https://en.wikipedia.org/wiki/Belief_propagation)
- [CPU cache](https://en.wikipedia.org/wiki/CPU_cache)
- [Cache-oblivious algorithm](https://en.wikipedia.org/wiki/Cache-oblivious_algorithm)
- [Carl Gustav Jacob Jacobi](https://en.wikipedia.org/wiki/Carl_Gustav_Jacob_Jacobi)
- [Comparison of linear algebra libraries](https://en.wikipedia.org/wiki/Comparison_of_linear_algebra_libraries)
- [Comparison of numerical-analysis software](https://en.wikipedia.org/wiki/Comparison_of_numerical-analysis_software)
- [Condition number](https://en.wikipedia.org/wiki/Condition_number)
- [Diagonal matrix](https://en.wikipedia.org/wiki/Diagonal_matrix)
- [Diagonally dominant matrix](https://en.wikipedia.org/wiki/Diagonally_dominant_matrix)
- [Floating-point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic)
- [GNU Free Documentation License](https://en.wikipedia.org/wiki/GNU_Free_Documentation_License)
- [Gauss–Seidel method](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Iterative method](https://en.wikipedia.org/wiki/Iterative_method)
- [Jacobi eigenvalue algorithm](https://en.wikipedia.org/wiki/Jacobi_eigenvalue_algorithm)
- [LAPACK](https://en.wikipedia.org/wiki/LAPACK)
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [MathWorld](https://en.wikipedia.org/wiki/MathWorld)
- [Matrix decomposition](https://en.wikipedia.org/wiki/Matrix_decomposition)
- [Matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication)
- [Matrix multiplication algorithm](https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm)
- [Matrix splitting](https://en.wikipedia.org/wiki/Matrix_splitting)
- [Multiprocessing](https://en.wikipedia.org/wiki/Multiprocessing)
- [Numerical linear algebra](https://en.wikipedia.org/wiki/Numerical_linear_algebra)
- [Numerical stability](https://en.wikipedia.org/wiki/Numerical_stability)
- [Definite matrix](https://en.wikipedia.org/wiki/Definite_matrix)
- [Single instruction, multiple data](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data)
- [Society for Industrial and Applied Mathematics](https://en.wikipedia.org/wiki/Society_for_Industrial_and_Applied_Mathematics)
- [Sparse matrix](https://en.wikipedia.org/wiki/Sparse_matrix)
- [Spectral radius](https://en.wikipedia.org/wiki/Spectral_radius)
- [Successive over-relaxation](https://en.wikipedia.org/wiki/Successive_over-relaxation)
- [System of linear equations](https://en.wikipedia.org/wiki/System_of_linear_equations)
- [Translation lookaside buffer](https://en.wikipedia.org/wiki/Translation_lookaside_buffer)
- [Yousef Saad](https://en.wikipedia.org/wiki/Yousef_Saad)
- [Talk:Jacobi method](https://en.wikipedia.org/wiki/Talk:Jacobi_method)
- [Wikipedia:Articles with a single source](https://en.wikipedia.org/wiki/Wikipedia:Articles_with_a_single_source)
- [Template:Numerical linear algebra](https://en.wikipedia.org/wiki/Template:Numerical_linear_algebra)
- [Template talk:Numerical linear algebra](https://en.wikipedia.org/wiki/Template_talk:Numerical_linear_algebra)
- [Help:Authority control](https://en.wikipedia.org/wiki/Help:Authority_control)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from September 2024](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_September_2024)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:39:14.182704+00:00_