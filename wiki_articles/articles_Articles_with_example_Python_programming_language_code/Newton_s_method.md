# Newton's method

## Article Metadata

- **Last Updated:** 2024-12-15T04:37:36.400787+00:00
- **Original Article:** [Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method)
- **Language:** en
- **Page ID:** 22145

## Summary

In numerical analysis, the Newton–Raphson method, also known simply as Newton's method, named after Isaac Newton and Joseph Raphson, is a root-finding algorithm which produces successively better approximations to the roots (or zeroes) of a real-valued function. The most basic version starts with a real-valued function  f, its derivative f′, and an initial guess x0 for a root of f. If f satisfies certain assumptions and the initial guess is close, then

  
    
      
        
          x
      

## Categories

- Category:All articles lacking reliable references
- Category:All articles to be expanded
- Category:All articles with unsourced statements
- Category:Articles lacking reliable references from February 2019
- Category:Articles to be expanded from February 2019
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from June 2024
- Category:CS1 Latin-language sources (la)
- Category:Commons category link is on Wikidata
- Category:Isaac Newton
- Category:Optimization algorithms and methods
- Category:Root-finding algorithms
- Category:Short description is different from Wikidata
- Category:Use dmy dates from January 2020
- Category:Wikipedia articles needing page number citations from June 2024

## Table of Contents

- Description
- History
- Practical considerations
- Analysis
- Examples
- Multidimensional formulations
- Modifications
- Applications
- Code
- See also
- Notes
- References
- Further reading
- External links

## Content

In numerical analysis, the Newton–Raphson method, also known simply as Newton's method, named after Isaac Newton and Joseph Raphson, is a root-finding algorithm which produces successively better approximations to the roots (or zeroes) of a real-valued function. The most basic version starts with a real-valued function  f, its derivative f′, and an initial guess x0 for a root of f. If f satisfies certain assumptions and the initial guess is close, then

  
    
      
        
          x
          
            1
          
        
        =
        
          x
          
            0
          
        
        −
        
          
            
              f
              (
              
                x
                
                  0
                
              
              )
            
            
              
                f
                ′
              
              (
              
                x
                
                  0
                
              
              )
            
          
        
      
    
    {\displaystyle x_{1}=x_{0}-{\frac {f(x_{0})}{f'(x_{0})}}}
  

is a better approximation of the root than x0. Geometrically, (x1, 0) is the x-intercept of the tangent of the graph of f at (x0, f(x0)): that is, the improved guess, x1, is the unique root of the linear approximation of f  at the initial guess, x0. The process is repeated as

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              f
              (
              
                x
                
                  n
                
              
              )
            
            
              
                f
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
      
    
    {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}}
  

until a sufficiently precise value is reached. The number of correct digits roughly doubles with each step. This algorithm is first in the class of Householder's methods, and was succeeded by Halley's method. The method can also be extended to complex functions and to systems of equations.

Description
The idea is to start with an initial guess, then to approximate the function by its tangent line, and finally to compute the x-intercept of this tangent line. This x-intercept will typically be a better approximation to the original function's root than the first guess, and the method can be iterated.

If the tangent line to the curve f(x) at x = xn intercepts the x-axis at xn+1 then the slope is

  
    
      
        
          f
          ′
        
        (
        
          x
          
            n
          
        
        )
        =
        
          
            
              
                f
                (
                
                  x
                  
                    n
                  
                
                )
                −
                0
              
              
                
                  x
                  
                    n
                  
                
                −
                
                  x
                  
                    n
                    +
                    1
                  
                
              
            
          
        
        .
      
    
    {\displaystyle f'(x_{n})={\dfrac {f(x_{n})-0}{x_{n}-x_{n+1}}}.}
  

Solving for xn+1 gives

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              f
              (
              
                x
                
                  n
                
              
              )
            
            
              
                f
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
        .
      
    
    {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}.}
  

We start the process with some arbitrary initial value x0. (The closer to the zero, the better. But, in the absence of any intuition about where the zero might lie, a "guess and check" method might narrow the possibilities to a reasonably small interval by appealing to the intermediate value theorem.) The method will usually converge, provided this initial guess is close enough to the unknown zero, and that f′(x0) ≠ 0. Furthermore, for a zero of multiplicity 1, the convergence is at least quadratic (see Rate of convergence) in a neighbourhood of the zero, which intuitively means that the number of correct digits roughly doubles in every step. More details can be found in § Analysis below.
Householder's methods are similar but have higher order for even faster convergence. However, the extra computations required for each step can slow down the overall performance relative to Newton's method, particularly if f or its derivatives are computationally expensive to evaluate.

History
The method first appeared roughly in Isaac Newton's work in De analysi per aequationes numero terminorum infinitas (written in 1669, published in 1711 by William Jones) and in De metodis fluxionum et serierum infinitarum (written in 1671, translated and published as Method of Fluxions in 1736 by John Colson). However, while Newton gave the basic ideas, his method differs from the modern method given above. He applied the method only to polynomials, starting with an initial root estimate and extracting a sequence of error corrections. He used each correction to rewrite the polynomial in terms of the remaining error, and then solved for a new correction by neglecting higher-degree terms. He did not explicitly connect the method with derivatives or present a general formula. Newton applied this method to both numerical and algebraic problems, producing Taylor series in the latter case.
Newton may have derived his method from a similar, less precise method by mathematician François Viète, however, the two methods are not the same. The essence of Viète's own method can be found in the work of the Persian mathematician Sharaf al-Din al-Tusi, while his successor Jamshīd al-Kāshī used a form of Newton's method to solve xP − N = 0 to find roots of N, a method that is algebraically equivalent to Newton's method, and in which a similar method was found in Trigonometria Britannica, published by Henry Briggs in 1633. The ancient Greeks and Babylonians had methods for extracting roots that matched the general idea of solving an equation by improving an estimate of the solution by the addition of a correction term.
The Japanese mathematician Seki Kōwa used Newton's method in the 1680s to solve single-variable equations, though the connection with calculus was missing.
Newton's method was first published in 1685 in A Treatise of Algebra both Historical and Practical by John Wallis. In 1690, Joseph Raphson published a simplified description in Analysis aequationum universalis. Raphson also applied the method only to polynomials, but he avoided Newton's tedious rewriting process by extracting each successive correction from the original polynomial. This allowed him to derive a reusable iterative expression for each problem. Finally, in 1740, Thomas Simpson described Newton's method as an iterative method for solving general nonlinear equations using calculus, essentially giving the description above. In the same publication, Simpson also gives the generalization to systems of two equations and notes that Newton's method can be used for solving optimization problems by setting the gradient to zero.
Arthur Cayley in 1879 in The Newton–Fourier imaginary problem was the first to notice the difficulties in generalizing Newton's method to complex roots of polynomials with degree greater than 2 and complex initial values. This opened the way to the study of the theory of iterations of rational functions.

Practical considerations
Newton's method is a powerful technique—in general the convergence is quadratic: as the method converges on the root, the difference between the root and the approximation is squared (the number of accurate digits roughly doubles) at each step. However, there are some difficulties with the method.

Difficulty in calculating the derivative of a function
Newton's method requires that the derivative can be calculated directly. An analytical expression for the derivative may not be easily obtainable or could be expensive to evaluate. In these situations, it may be appropriate to approximate the derivative by using the slope of a line through two nearby points on the function. Using this approximation would result in something like the secant method whose convergence is slower than that of Newton's method.

Failure of the method to converge to the root
It is important to review the proof of quadratic convergence of Newton's method before implementing it. Specifically, one should review the assumptions made in the proof. For situations where the method fails to converge, it is because the assumptions made in this proof are not met.
For example, in some cases, if the first derivative is not well behaved in the neighborhood of a particular root, then it is possible that Newton's method will fail to converge no matter where the initialization is set. In some cases, Newton's method can be stabilized by using successive over-relaxation, or the speed of convergence can be increased by using the same method.
In a robust implementation of Newton's method, it is common to place limits on the number of iterations, bound the solution to an interval known to contain the root, and combine the method with a more robust root finding method.

Slow convergence for roots of multiplicity greater than 1
If the root being sought has multiplicity greater than one, the convergence rate is merely linear (errors reduced by a constant factor at each step) unless special steps are taken. When there are two or more roots that are close together then it may take many iterations before the iterates get close enough to one of them for the quadratic convergence to be apparent. However, if the multiplicity m of the root is known, the following modified algorithm preserves the quadratic convergence rate:

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        
          x
          
            n
          
        
        −
        m
        
          
            
              f
              (
              
                x
                
                  n
                
              
              )
            
            
              
                f
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
        .
      
    
    {\displaystyle x_{n+1}=x_{n}-m{\frac {f(x_{n})}{f'(x_{n})}}.}
  

This is equivalent to using successive over-relaxation. On the other hand, if the multiplicity m of the root is not known, it is possible to estimate m after carrying out one or two iterations, and then use that value to increase the rate of convergence.
If the multiplicity m of the root is finite then g(x) = ⁠f(x)/f′(x)⁠ will have a root at the same location with multiplicity 1.  Applying Newton's method to find the root of g(x) recovers quadratic convergence in many cases although it generally involves the second derivative of f(x).  In a particularly simple case, if f(x) = xm then g(x) = ⁠x/m⁠ and Newton's method finds the root in a single iteration with

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              g
              (
              
                x
                
                  n
                
              
              )
            
            
              
                g
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              
              
                
                  
                    x
                    
                      n
                    
                  
                  m
                
              
              
            
            
              1
              m
            
          
        
        =
        0
        
        .
      
    
    {\displaystyle x_{n+1}=x_{n}-{\frac {g(x_{n})}{g'(x_{n})}}=x_{n}-{\frac {\;{\frac {x_{n}}{m}}\;}{\frac {1}{m}}}=0\,.}

Analysis
Suppose that the function f has a zero at α, i.e., f(α) = 0, and f is differentiable in a neighborhood of α.
If f is continuously differentiable and its derivative is nonzero at α, then there exists a neighborhood of α such that for all starting values x0 in that neighborhood, the sequence (xn) will converge to α.
If f is continuously differentiable, its derivative is nonzero at α, and it has a second derivative at α, then the convergence is quadratic or faster. If the second derivative is not 0 at α then the convergence is merely quadratic. If the third derivative exists and is bounded in a neighborhood of α, then:

  
    
      
        Δ
        
          x
          
            i
            +
            1
          
        
        =
        
          
            
              
                f
                ″
              
              (
              α
              )
            
            
              2
              
                f
                ′
              
              (
              α
              )
            
          
        
        
          
            (
            
              Δ
              
                x
                
                  i
                
              
            
            )
          
          
            2
          
        
        +
        O
        
          
            (
            
              Δ
              
                x
                
                  i
                
              
            
            )
          
          
            3
          
        
        
        ,
      
    
    {\displaystyle \Delta x_{i+1}={\frac {f''(\alpha )}{2f'(\alpha )}}\left(\Delta x_{i}\right)^{2}+O\left(\Delta x_{i}\right)^{3}\,,}
  

where

  
    
      
        Δ
        
          x
          
            i
          
        
        ≜
        
          x
          
            i
          
        
        −
        α
        
        .
      
    
    {\displaystyle \Delta x_{i}\triangleq x_{i}-\alpha \,.}
  

If the derivative is 0 at α, then the convergence is usually only linear. Specifically, if f is twice continuously differentiable, f′(α) = 0 and f″(α) ≠ 0, then there exists a neighborhood of α such that, for all starting values x0 in that neighborhood, the sequence of iterates converges linearly, with rate ⁠1/2⁠. Alternatively, if f′(α) = 0 and f′(x) ≠ 0 for x ≠ α, x in a neighborhood U of α, α being a zero of multiplicity r, and if f ∈ Cr(U), then there exists a neighborhood of α such that, for all starting values x0 in that neighborhood, the sequence of iterates converges linearly.
However, even linear convergence is not guaranteed in pathological situations.
In practice, these results are local, and the neighborhood of convergence is not known in advance. But there are also some results on global convergence: for instance, given a right neighborhood U+ of α, if f is twice differentiable in U+ and if f′ ≠ 0, f · f″ > 0 in U+, then, for each x0 in U+ the sequence xk is monotonically decreasing to α.

Proof of quadratic convergence for Newton's iterative method
According to Taylor's theorem, any function f(x) which has a continuous second derivative can be represented by an expansion about a point that is close to a root of f(x). Suppose this root is α. Then the expansion of f(α) about xn is:

where the Lagrange form of the Taylor series expansion remainder is

  
    
      
        
          R
          
            1
          
        
        =
        
          
            1
            
              2
              !
            
          
        
        
          f
          ″
        
        (
        
          ξ
          
            n
          
        
        )
        
          
            (
            
              α
              −
              
                x
                
                  n
                
              
            
            )
          
          
            2
          
        
        
        ,
      
    
    {\displaystyle R_{1}={\frac {1}{2!}}f''(\xi _{n})\left(\alpha -x_{n}\right)^{2}\,,}
  

where ξn is in between xn and α.
Since α is the root, (1) becomes:

Dividing equation (2) by f′(xn) and rearranging gives

Remembering that xn + 1 is defined by

one finds that

  
    
      
        
          
            
              
                α
                −
                
                  x
                  
                    n
                    +
                    1
                  
                
              
              ⏟
            
          
          
            
              ε
              
                n
                +
                1
              
            
          
        
        =
        
          
            
              −
              
                f
                ″
              
              (
              
                ξ
                
                  n
                
              
              )
            
            
              2
              
                f
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
        
          
            (
            
            
              
                
                  
                    α
                    −
                    
                      x
                      
                        n
                      
                    
                  
                  ⏟
                
              
              
                
                  ε
                  
                    n
                  
                
              
            
            
            )
          
          
            2
          
        
        
        .
      
    
    {\displaystyle \underbrace {\alpha -x_{n+1}} _{\varepsilon _{n+1}}={\frac {-f''(\xi _{n})}{2f'(x_{n})}}{(\,\underbrace {\alpha -x_{n}} _{\varepsilon _{n}}\,)}^{2}\,.}
  

That is,

Taking the absolute value of both sides gives

Equation (6) shows that the order of convergence is at least quadratic if the following conditions are satisfied:

f′(x) ≠ 0; for all x ∈ I, where I is the interval [α − |ε0|, α + |ε0|];
f″(x) is continuous, for all x ∈ I;
M |ε0| < 1
where M is given by

  
    
      
        M
        =
        
          
            1
            2
          
        
        
          (
          
            
              sup
              
                x
                ∈
                I
              
            
            |
            
              f
              ″
            
            (
            x
            )
            |
          
          )
        
        
          (
          
            
              sup
              
                x
                ∈
                I
              
            
            
              
                1
                
                  |
                  
                    f
                    ′
                  
                  (
                  x
                  )
                  |
                
              
            
          
          )
        
        .
        
      
    
    {\displaystyle M={\frac {1}{2}}\left(\sup _{x\in I}\vert f''(x)\vert \right)\left(\sup _{x\in I}{\frac {1}{\vert f'(x)\vert }}\right).\,}
  

If these conditions hold,

  
    
      
        |
        
          ε
          
            n
            +
            1
          
        
        |
        ≤
        M
        ⋅
        
          ε
          
            n
          
          
            2
          
        
        
        .
      
    
    {\displaystyle \vert \varepsilon _{n+1}\vert \leq M\cdot \varepsilon _{n}^{2}\,.}

Fourier conditions
Suppose that f(x) is a concave function on an interval, which is strictly increasing. If it is negative at the left endpoint and positive at the right endpoint, the intermediate value theorem guarantees that there is a zero ζ of f somewhere in the interval. From geometrical principles, it can be seen that the Newton iteration xi starting at the left endpoint is monotonically increasing and convergent, necessarily to ζ.
Joseph Fourier introduced a modification of Newton's method starting at the right endpoint:

  
    
      
        
          y
          
            i
            +
            1
          
        
        =
        
          y
          
            i
          
        
        −
        
          
            
              f
              (
              
                y
                
                  i
                
              
              )
            
            
              
                f
                ′
              
              (
              
                x
                
                  i
                
              
              )
            
          
        
        .
      
    
    {\displaystyle y_{i+1}=y_{i}-{\frac {f(y_{i})}{f'(x_{i})}}.}
  

This sequence is monotonically decreasing and convergent. By passing to the limit in this definition, it can be seen that the limit of yi must also be the zero ζ. 
So, in the case of a concave increasing function with a zero, initialization is largely irrelevant. Newton iteration starting anywhere left of the zero will converge, as will Fourier's modified Newton iteration starting anywhere right of the zero. The accuracy at any step of the iteration can be determined directly from the difference between the location of the iteration from the left and the location of the iteration from the right. If f is twice continuously differentiable, it can be proved using Taylor's theorem that

  
    
      
        
          lim
          
            i
            →
            ∞
          
        
        
          
            
              
                y
                
                  i
                  +
                  1
                
              
              −
              
                x
                
                  i
                  +
                  1
                
              
            
            
              (
              
                y
                
                  i
                
              
              −
              
                x
                
                  i
                
              
              
                )
                
                  2
                
              
            
          
        
        =
        −
        
          
            1
            2
          
        
        
          
            
              
                f
                ″
              
              (
              ζ
              )
            
            
              
                f
                ′
              
              (
              ζ
              )
            
          
        
        ,
      
    
    {\displaystyle \lim _{i\to \infty }{\frac {y_{i+1}-x_{i+1}}{(y_{i}-x_{i})^{2}}}=-{\frac {1}{2}}{\frac {f''(\zeta )}{f'(\zeta )}},}
  

showing that this difference in locations converges quadratically to zero.
All of the above can be extended to systems of equations in multiple variables, although in that context the relevant concepts of monotonicity and concavity are more subtle to formulate. In the case of single equations in a single variable, the above monotonic convergence of Newton's method can also be generalized to replace concavity by positivity or negativity conditions on an arbitrary higher-order derivative of f. However, in this generalization, Newton's iteration is modified so as to be based on Taylor polynomials rather than the tangent line. In the case of concavity, this modification coincides with the standard Newton method.

Examples
Use of Newton's method to compute square roots
Newton's method is one of many known methods of computing square roots. Given a positive number a, the problem of finding a number x such that x2 = a is equivalent to finding a root of the function f(x) = x2 − a. The Newton iteration defined by this function is given by

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              f
              (
              
                x
                
                  n
                
              
              )
            
            
              
                f
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              
                x
                
                  n
                
                
                  2
                
              
              −
              a
            
            
              2
              
                x
                
                  n
                
              
            
          
        
        =
        
          
            1
            2
          
        
        
          (
          
            
              x
              
                n
              
            
            +
            
              
                a
                
                  x
                  
                    n
                  
                
              
            
          
          )
        
        .
      
    
    {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=x_{n}-{\frac {x_{n}^{2}-a}{2x_{n}}}={\frac {1}{2}}\left(x_{n}+{\frac {a}{x_{n}}}\right).}
  

This happens to coincide with the "Babylonian" method of finding square roots, which consists of replacing an approximate root xn by the arithmetic mean of xn and a⁄xn. By performing this iteration, it is possible to evaluate a square root to any desired accuracy by only using the basic arithmetic operations.
The following three tables show examples of the result of this computation for finding the square root of 612, with the iteration initialized at the values of 1, 10, and −20. Each row in a "xn" column is obtained by applying the preceding formula to the entry above it, for instance

  
    
      
        306.5
        =
        
          
            1
            2
          
        
        
          (
          
            1
            +
            
              
                612
                1
              
            
          
          )
        
        .
      
    
    {\displaystyle 306.5={\frac {1}{2}}\left(1+{\frac {612}{1}}\right).}
  

The correct digits are underlined. It is seen that with only a few iterations one can obtain a solution accurate to many decimal places. The first table shows that this is true even if the Newton iteration were initialized by the very inaccurate guess of 1.
When computing any nonzero square root, the first derivative of f must be nonzero at the root, and that f is a smooth function. So, even before any computation, it is known that any convergent Newton iteration has a quadratic rate of convergence. This is reflected in the above tables by the fact that once a Newton iterate gets close to the root, the number of correct digits approximately doubles with each iteration.

Solution of cos(x) = x3 using Newton's method
Consider the problem of finding the positive number x with cos x = x3. We can rephrase that as finding the zero of f(x) = cos(x) − x3. We have f′(x) = −sin(x) − 3x2. Since cos(x) ≤ 1 for all x and x3 > 1 for x > 1, we know that our solution lies between 0 and 1. 
A starting value of 0 will lead to an undefined result which illustrates the importance of using a starting point close to the solution. For example, with an initial guess x0 = 0.5, the sequence given by Newton's method is:

  
    
      
        
          
            
              
                
                  x
                  
                    1
                  
                
              
              
                =
              
              
                
                  x
                  
                    0
                  
                
                −
                
                  
                    
                      
                        f
                        (
                        
                          x
                          
                            0
                          
                        
                        )
                      
                      
                        
                          f
                          ′
                        
                        (
                        
                          x
                          
                            0
                          
                        
                        )
                      
                    
                  
                
              
              
                =
              
              
                0.5
                −
                
                  
                    
                      
                        cos
                        ⁡
                        0.5
                        −
                        
                          0.5
                          
                            3
                          
                        
                      
                      
                        −
                        sin
                        ⁡
                        0.5
                        −
                        3
                        ×
                        
                          0.5
                          
                            2
                          
                        
                      
                    
                  
                
              
              
                =
              
              
                1.112
                
                141
                
                637
                
                097
                …
              
            
            
              
                
                  x
                  
                    2
                  
                
              
              
                =
              
              
                
                  x
                  
                    1
                  
                
                −
                
                  
                    
                      
                        f
                        (
                        
                          x
                          
                            1
                          
                        
                        )
                      
                      
                        
                          f
                          ′
                        
                        (
                        
                          x
                          
                            1
                          
                        
                        )
                      
                    
                  
                
              
              
                =
              
              
                ⋮
              
              
                =
              
              
                
                  
                    0.
                    _
                  
                
                909
                
                672
                
                693
                
                736
                …
              
            
            
              
                
                  x
                  
                    3
                  
                
              
              
                =
              
              
                ⋮
              
              
                =
              
              
                ⋮
              
              
                =
              
              
                
                  
                    0.86
                    _
                  
                
                7
                
                263
                
                818
                
                209
                …
              
            
            
              
                
                  x
                  
                    4
                  
                
              
              
                =
              
              
                ⋮
              
              
                =
              
              
                ⋮
              
              
                =
              
              
                
                  
                    
                      0.865
                      
                      47
                    
                    _
                  
                
                7
                
                135
                
                298
                …
              
            
            
              
                
                  x
                  
                    5
                  
                
              
              
                =
              
              
                ⋮
              
              
                =
              
              
                ⋮
              
              
                =
              
              
                
                  
                    
                      0.865
                      
                      474
                      
                      033
                      
                      1
                    
                    _
                  
                
                11
                …
              
            
            
              
                
                  x
                  
                    6
                  
                
              
              
                =
              
              
                ⋮
              
              
                =
              
              
                ⋮
              
              
                =
              
              
                
                  
                    
                      0.865
                      
                      474
                      
                      033
                      
                      102
                    
                    _
                  
                
                …
              
            
          
        
      
    
    {\displaystyle {\begin{matrix}x_{1}&=&x_{0}-{\dfrac {f(x_{0})}{f'(x_{0})}}&=&0.5-{\dfrac {\cos 0.5-0.5^{3}}{-\sin 0.5-3\times 0.5^{2}}}&=&1.112\,141\,637\,097\dots \\x_{2}&=&x_{1}-{\dfrac {f(x_{1})}{f'(x_{1})}}&=&\vdots &=&{\underline {0.}}909\,672\,693\,736\dots \\x_{3}&=&\vdots &=&\vdots &=&{\underline {0.86}}7\,263\,818\,209\dots \\x_{4}&=&\vdots &=&\vdots &=&{\underline {0.865\,47}}7\,135\,298\dots \\x_{5}&=&\vdots &=&\vdots &=&{\underline {0.865\,474\,033\,1}}11\dots \\x_{6}&=&\vdots &=&\vdots &=&{\underline {0.865\,474\,033\,102}}\dots \end{matrix}}}
  

The correct digits are underlined in the above example. In particular, x6 is correct to 12 decimal places. We see that the number of correct digits after the decimal point increases from 2 (for x3) to 5 and 10, illustrating the quadratic convergence.

Slow convergence
The function f(x) = x2 has a root at 0. Since f is continuously differentiable at its root, the theory guarantees that Newton's method as initialized sufficiently close to the root will converge. However, since the derivative f ′ is zero at the root, quadratic convergence is not ensured by the theory. In this particular example, the Newton iteration is given by

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              f
              (
              
                x
                
                  n
                
              
              )
            
            
              
                f
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
        =
        
          
            1
            2
          
        
        
          x
          
            n
          
        
        .
      
    
    {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}={\frac {1}{2}}x_{n}.}
  

It is visible from this that Newton's method could be initialized anywhere and converge to zero, but at only a linear rate. If initialized at 1, dozens of iterations would be required before ten digits of accuracy are achieved.
The function f(x) = x + x4/3 also has a root at 0, where it is continuously differentiable. Although the first derivative f ′ is nonzero at the root, the second derivative f ′′ is nonexistent there, so that quadratic convergence cannot be guaranteed. In fact the Newton iteration is given by

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              f
              (
              
                x
                
                  n
                
              
              )
            
            
              
                f
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
        =
        
          
            
              x
              
                4
                
                  /
                
                3
              
            
            
              3
              +
              4
              
                x
                
                  1
                  
                    /
                  
                  3
                
              
            
          
        
        .
      
    
    {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}={\frac {x^{4/3}}{3+4x^{1/3}}}.}
  

From this, it can be seen that the rate of convergence is superlinear but subquadratic. This can be seen in the following tables, the left of which shows Newton's method applied to the above f(x) = x + x4/3 and the right of which shows Newton's method applied to f(x) = x + x2. The quadratic convergence in iteration shown on the right is illustrated by the orders of magnitude in the distance from the iterate to the true root (0,1,2,3,5,10,20,39,...) being approximately doubled from row to row. While the convergence on the left is superlinear, the order of magnitude is only multiplied by about 4/3 from row to row (0,1,2,4,5,7,10,13,...).

The rate of convergence is distinguished from the number of iterations required to reach a given accuracy. For example, the function f(x) = x20 − 1 has a root at 1. Since f ′(1) ≠ 0 and f is smooth, it is known that any Newton iteration convergent to 1 will converge quadratically. However, if initialized at 0.5, the first few iterates of Newton's method are approximately 26214, 24904, 23658, 22476, decreasing slowly, with only the 200th iterate being 1.0371. The following iterates are 1.0103, 1.00093, 1.0000082, and 1.00000000065, illustrating quadratic convergence. This highlights that quadratic convergence of a Newton iteration does not mean that only few iterates are required; this only applies once the sequence of iterates is sufficiently close to the root.

Convergence dependent on initialization
The function f(x) = x(1 + x2)−1/2 has a root at 0. The Newton iteration is given by

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              f
              (
              
                x
                
                  n
                
              
              )
            
            
              
                f
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
        =
        −
        
          x
          
            n
          
          
            3
          
        
        .
      
    
    {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=-x_{n}^{3}.}
  

From this, it can be seen that there are three possible phenomena for a Newton iteration. If initialized strictly between ±1, the Newton iteration will converge (super-)quadratically to 0; if initialized exactly at 1 or −1, the Newton iteration will oscillate endlessly between ±1; if initialized anywhere else, the Newton iteration will diverge. This same trichotomy occurs for f(x) = arctan x.
In cases where the function in question has multiple roots, it can be difficult to control, via choice of initialization, which root (if any) is identified by Newton's method. For example, the function f(x) = x(x2 − 1)(x − 3)e−(x − 1)2/2 has roots at −1, 0, 1, and 3. If initialized at −1.488, the Newton iteration converges to 0; if initialized at −1.487, it diverges to ∞; if initialized at −1.486, it converges to −1; if initialized at −1.485, it diverges to −∞; if initialized at −1.4843, it converges to 3; if initialized at −1.484, it converges to 1. This kind of subtle dependence on initialization is not uncommon; it is frequently studied in the complex plane in the form of the Newton fractal.

Divergence even when initialization is close to the root
Consider the problem of finding a root of f(x) = x1/3. The Newton iteration is

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              f
              (
              
                x
                
                  n
                
              
              )
            
            
              
                f
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              x
              
                n
              
              
                1
                
                  /
                
                3
              
            
            
              
                
                  1
                  3
                
              
              
                x
                
                  n
                
                
                  −
                  2
                  
                    /
                  
                  3
                
              
            
          
        
        =
        −
        2
        
          x
          
            n
          
        
        .
      
    
    {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=x_{n}-{\frac {x_{n}^{1/3}}{{\frac {1}{3}}x_{n}^{-2/3}}}=-2x_{n}.}
  

Unless Newton's method is initialized at the exact root 0, it is seen that the sequence of iterates will fail to converge. For example, even if initialized at the reasonably accurate guess of 0.001, the first several iterates are −0.002, 0.004, −0.008, 0.016, reaching 1048.58, −2097.15, ... by the 20th iterate. This failure of convergence is not contradicted by the analytic theory, since in this case f is not differentiable at its root.
In the above example, failure of convergence is reflected by the failure of f(xn) to get closer to zero as n increases, as well as by the fact that successive iterates are growing further and further apart. However, the function f(x) = x1/3e−x2 also has a root at 0. The Newton iteration is given by

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              f
              (
              
                x
                
                  n
                
              
              )
            
            
              
                f
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
        =
        
          x
          
            n
          
        
        
          (
          
            1
            −
            
              
                3
                
                  1
                  −
                  6
                  
                    x
                    
                      n
                    
                    
                      2
                    
                  
                
              
            
          
          )
        
        .
      
    
    {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=x_{n}\left(1-{\frac {3}{1-6x_{n}^{2}}}\right).}
  

In this example, where again f is not differentiable at the root, any Newton iteration not starting exactly at the root will diverge, but with both xn + 1 − xn and f(xn) converging to zero. This is seen in the following table showing the iterates with initialization 1:

Although the convergence of xn + 1 − xn in this case is not very rapid, it can be proved from the iteration formula. This example highlights the possibility that a stopping criterion for Newton's method based only on the smallness of xn + 1 − xn and f(xn) might falsely identify a root.

Oscillatory behavior
It is easy to find situations for which Newton's method oscillates endlessly between two distinct values. For example, for Newton's method as applied to a function f to oscillate between 0 and 1, it is only necessary that the tangent line to f at 0 intersects the x-axis at 1 and that the tangent line to f at 1 intersects the x-axis at 0. This is the case, for example, if f(x) = x3 − 2x + 2. For this function, it is even the case that Newton's iteration as initialized sufficiently close to 0 or 1 will asymptotically oscillate between these values. For example, Newton's method as initialized at 0.99 yields iterates 0.99, −0.06317, 1.00628, 0.03651, 1.00196, 0.01162, 1.00020, 0.00120, 1.000002, and so on. This behavior is present despite the presence of a root of f approximately equal to −1.76929.

Undefinedness of Newton's method
In some cases, it is not even possible to perform the Newton iteration. For example, if f(x) = x2 − 1, then the Newton iteration is defined by

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              f
              (
              
                x
                
                  n
                
              
              )
            
            
              
                f
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
        =
        
          
            
              
                x
                
                  n
                
                
                  2
                
              
              −
              1
            
            
              2
              
                x
                
                  n
                
              
            
          
        
        .
      
    
    {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}={\frac {x_{n}^{2}-1}{2x_{n}}}.}
  

So Newton's method cannot be initialized at 0, since this would make x1 undefined. Geometrically, this is because the tangent line to f at 0 is horizontal (i.e. f ′(0) = 0), never intersecting the x-axis.
Even if the initialization is selected so that the Newton iteration can begin, the same phenomenon can block the iteration from being indefinitely continued.
If f has an incomplete domain, it is possible for Newton's method to send the iterates outside of the domain, so that it is impossible to continue the iteration. For example, the natural logarithm function f(x) = ln x has a root at 1, and is defined only for positive x. Newton's iteration in this case is given by

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              f
              (
              
                x
                
                  n
                
              
              )
            
            
              
                f
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
        =
        
          x
          
            n
          
        
        (
        1
        −
        ln
        ⁡
        
          x
          
            n
          
        
        )
        .
      
    
    {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=x_{n}(1-\ln x_{n}).}
  

So if the iteration is initialized at e, the next iterate is 0; if the iteration is initialized at a value larger than e, then the next iterate is negative. In either case, the method cannot be continued.

Multidimensional formulations
Systems of equations
k variables, k functions
One may also use Newton's method to solve systems of k equations, which amounts to finding the (simultaneous) zeroes of k continuously differentiable functions 
  
    
      
        f
        :
        
          
            R
          
          
            k
          
        
        →
        
          R
        
        .
      
    
    {\displaystyle f:\mathbb {R} ^{k}\to \mathbb {R} .}
  
 This is equivalent to finding the zeroes of a single vector-valued function 
  
    
      
        F
        :
        
          
            R
          
          
            k
          
        
        →
        
          
            R
          
          
            k
          
        
        .
      
    
    {\displaystyle F:\mathbb {R} ^{k}\to \mathbb {R} ^{k}.}
  
 In the formulation given above, the scalars xn are replaced by vectors xn and instead of dividing the function f(xn) by its derivative f′(xn) one instead has to left multiply the function F(xn) by the inverse of its k × k Jacobian matrix JF(xn). This results in the expression

  
    
      
        
          
            x
          
          
            n
            +
            1
          
        
        =
        
          
            x
          
          
            n
          
        
        −
        
          J
          
            F
          
        
        (
        
          
            x
          
          
            n
          
        
        
          )
          
            −
            1
          
        
        F
        (
        
          
            x
          
          
            n
          
        
        )
        .
      
    
    {\displaystyle \mathbf {x} _{n+1}=\mathbf {x} _{n}-J_{F}(\mathbf {x} _{n})^{-1}F(\mathbf {x} _{n}).}
  

or, by solving the system of linear equations

  
    
      
        
          J
          
            F
          
        
        (
        
          
            x
          
          
            n
          
        
        )
        (
        
          
            x
          
          
            n
            +
            1
          
        
        −
        
          
            x
          
          
            n
          
        
        )
        =
        −
        F
        (
        
          
            x
          
          
            n
          
        
        )
      
    
    {\displaystyle J_{F}(\mathbf {x} _{n})(\mathbf {x} _{n+1}-\mathbf {x} _{n})=-F(\mathbf {x} _{n})}
  

for the unknown xn + 1 − xn.

k variables, m equations, with m > k
The k-dimensional variant of Newton's method can be used to solve systems of greater than k (nonlinear) equations as well if the algorithm uses the generalized inverse of the non-square Jacobian matrix J+ = (JTJ)−1JT instead of the inverse of J. If the nonlinear system has no solution, the method attempts to find a solution in the non-linear least squares sense. See Gauss–Newton algorithm for more information.

Example
For example, the following set of equations needs to be solved for vector of points 
  
    
      
         
        [
         
        
          x
          
            1
          
        
        ,
        
          x
          
            2
          
        
         
        ]
         
        ,
      
    
    {\displaystyle \ [\ x_{1},x_{2}\ ]\ ,}
  
 given the vector of known values 
  
    
      
         
        [
         
        2
        ,
        3
         
        ]
         
        .
      
    
    {\displaystyle \ [\ 2,3\ ]~.}
  

  
    
      
        
          
            
              
                5
                 
                
                  x
                  
                    1
                  
                  
                    2
                  
                
                +
                
                  x
                  
                    1
                  
                
                 
                
                  x
                  
                    2
                  
                  
                    2
                  
                
                +
                
                  sin
                  
                    2
                  
                
                ⁡
                (
                2
                 
                
                  x
                  
                    2
                  
                
                )
              
              
                =
                
                2
              
            
            
              
                
                  e
                  
                    2
                     
                    
                      x
                      
                        1
                      
                    
                    −
                    
                      x
                      
                        2
                      
                    
                  
                
                +
                4
                 
                
                  x
                  
                    2
                  
                
              
              
                =
                
                3
              
            
          
        
      
    
    {\displaystyle {\begin{array}{lcr}5\ x_{1}^{2}+x_{1}\ x_{2}^{2}+\sin ^{2}(2\ x_{2})&=\quad 2\\e^{2\ x_{1}-x_{2}}+4\ x_{2}&=\quad 3\end{array}}}
  

the function vector, 
  
    
      
         
        F
        (
        
          X
          
            k
          
        
        )
         
        ,
      
    
    {\displaystyle \ F(X_{k})\ ,}
  
 and Jacobian Matrix, 
  
    
      
         
        J
        (
        
          X
          
            k
          
        
        )
         
      
    
    {\displaystyle \ J(X_{k})\ }
  
 for iteration k, and the vector of known values, 
  
    
      
         
        Y
         
        ,
      
    
    {\displaystyle \ Y\ ,}
  
 are defined below.

  
    
      
        
          
            
              
                 
              
              
                F
                (
                
                  X
                  
                    k
                  
                
                )
                 
                =
                 
                
                  
                    [
                    
                      
                        
                          
                            
                              
                                
                                   
                                
                                
                                  
                                    f
                                    
                                      1
                                    
                                  
                                  (
                                  
                                    X
                                    
                                      k
                                    
                                  
                                  )
                                
                              
                              
                                
                                   
                                
                                
                                  
                                    f
                                    
                                      2
                                    
                                  
                                  (
                                  
                                    X
                                    
                                      k
                                    
                                  
                                  )
                                
                              
                            
                          
                        
                      
                    
                    ]
                  
                
                 
                =
                 
                
                  
                    
                      [
                      
                        
                          
                            
                              
                                
                                  
                                     
                                  
                                  
                                    5
                                     
                                    
                                      x
                                      
                                        1
                                      
                                      
                                        2
                                      
                                    
                                    +
                                    
                                      x
                                      
                                        1
                                      
                                    
                                     
                                    
                                      x
                                      
                                        2
                                      
                                      
                                        2
                                      
                                    
                                    +
                                    
                                      sin
                                      
                                        2
                                      
                                    
                                    ⁡
                                    (
                                    2
                                     
                                    
                                      x
                                      
                                        2
                                      
                                    
                                    )
                                  
                                
                                
                                  
                                     
                                  
                                  
                                    
                                      e
                                      
                                        2
                                         
                                        
                                          x
                                          
                                            1
                                          
                                        
                                        −
                                        
                                          x
                                          
                                            2
                                          
                                        
                                      
                                    
                                    +
                                    4
                                     
                                    
                                      x
                                      
                                        2
                                      
                                    
                                  
                                
                              
                            
                          
                        
                      
                      ]
                    
                  
                  
                    k
                  
                
              
            
            
              
                 
              
              
                J
                (
                
                  X
                  
                    k
                  
                
                )
                =
                
                  
                    
                      [
                      
                        
                          
                             
                            
                              
                                
                                   
                                  ∂
                                  
                                    
                                      f
                                      
                                        1
                                      
                                    
                                    (
                                    X
                                    )
                                  
                                   
                                
                                
                                  ∂
                                  
                                    
                                      x
                                      
                                        1
                                      
                                    
                                  
                                
                              
                            
                             
                            ,
                          
                          
                             
                            
                              
                                
                                   
                                  ∂
                                  
                                    
                                      f
                                      
                                        1
                                      
                                    
                                    (
                                    X
                                    )
                                  
                                   
                                
                                
                                  ∂
                                  
                                    
                                      x
                                      
                                        2
                                      
                                    
                                  
                                
                              
                            
                             
                          
                        
                        
                          
                             
                            
                              
                                
                                   
                                  ∂
                                  
                                    
                                      f
                                      
                                        2
                                      
                                    
                                    (
                                    X
                                    )
                                  
                                   
                                
                                
                                  ∂
                                  
                                    
                                      x
                                      
                                        1
                                      
                                    
                                  
                                
                              
                            
                             
                            ,
                          
                          
                             
                            
                              
                                
                                   
                                  ∂
                                  
                                    
                                      f
                                      
                                        2
                                      
                                    
                                    (
                                    X
                                    )
                                  
                                   
                                
                                
                                  ∂
                                  
                                    
                                      x
                                      
                                        2
                                      
                                    
                                  
                                
                              
                            
                             
                          
                        
                      
                      ]
                    
                  
                  
                    k
                  
                
                 
                =
                 
                
                  
                    
                      [
                      
                        
                          
                            
                              
                                
                                  
                                     
                                  
                                  
                                    10
                                     
                                    
                                      x
                                      
                                        1
                                      
                                    
                                    +
                                    
                                      x
                                      
                                        2
                                      
                                      
                                        2
                                      
                                    
                                     
                                    ,
                                  
                                  
                                  
                                    2
                                     
                                    
                                      x
                                      
                                        1
                                      
                                    
                                     
                                    
                                      x
                                      
                                        2
                                      
                                    
                                    +
                                    4
                                     
                                    sin
                                    ⁡
                                    (
                                    2
                                     
                                    
                                      x
                                      
                                        2
                                      
                                    
                                    )
                                     
                                    cos
                                    ⁡
                                    (
                                    2
                                     
                                    
                                      x
                                      
                                        2
                                      
                                    
                                    )
                                  
                                
                                
                                  
                                     
                                  
                                  
                                    2
                                     
                                    
                                      e
                                      
                                        2
                                         
                                        
                                          x
                                          
                                            1
                                          
                                        
                                        −
                                        
                                          x
                                          
                                            2
                                          
                                        
                                      
                                    
                                     
                                    ,
                                  
                                  
                                  
                                    
                                    −
                                    
                                      e
                                      
                                        2
                                         
                                        
                                          x
                                          
                                            1
                                          
                                        
                                        −
                                        
                                          x
                                          
                                            2
                                          
                                        
                                      
                                    
                                    +
                                    4
                                  
                                
                              
                            
                          
                        
                      
                      ]
                    
                  
                  
                    k
                  
                
              
            
            
              
                 
              
              
                Y
                =
                
                  
                    [
                    
                      
                        
                           
                          2
                           
                        
                      
                      
                        
                           
                          3
                           
                        
                      
                    
                    ]
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}~&F(X_{k})~=~{\begin{bmatrix}{\begin{aligned}~&f_{1}(X_{k})\\~&f_{2}(X_{k})\end{aligned}}\end{bmatrix}}~=~{\begin{bmatrix}{\begin{aligned}~&5\ x_{1}^{2}+x_{1}\ x_{2}^{2}+\sin ^{2}(2\ x_{2})\\~&e^{2\ x_{1}-x_{2}}+4\ x_{2}\end{aligned}}\end{bmatrix}}_{k}\\~&J(X_{k})={\begin{bmatrix}~{\frac {\ \partial {f_{1}(X)}\ }{\partial {x_{1}}}}\ ,&~{\frac {\ \partial {f_{1}(X)}\ }{\partial {x_{2}}}}~\\~{\frac {\ \partial {f_{2}(X)}\ }{\partial {x_{1}}}}\ ,&~{\frac {\ \partial {f_{2}(X)}\ }{\partial {x_{2}}}}~\end{bmatrix}}_{k}~=~{\begin{bmatrix}{\begin{aligned}~&10\ x_{1}+x_{2}^{2}\ ,&&2\ x_{1}\ x_{2}+4\ \sin(2\ x_{2})\ \cos(2\ x_{2})\\~&2\ e^{2\ x_{1}-x_{2}}\ ,&&-e^{2\ x_{1}-x_{2}}+4\end{aligned}}\end{bmatrix}}_{k}\\~&Y={\begin{bmatrix}~2~\\~3~\end{bmatrix}}\end{aligned}}}
  

Note that 
  
    
      
         
        F
        (
        
          X
          
            k
          
        
        )
         
      
    
    {\displaystyle \ F(X_{k})\ }
  
 could have been rewritten to absorb 
  
    
      
         
        Y
         
        ,
      
    
    {\displaystyle \ Y\ ,}
  
 and thus eliminate  
  
    
      
        Y
      
    
    {\displaystyle Y}
  
 from the equations. The equation to solve for each iteration are

  
    
      
        
          
            
              
                
                  
                    
                      [
                      
                        
                          
                            
                              
                                
                                  
                                     
                                  
                                  
                                     
                                    10
                                     
                                    
                                      x
                                      
                                        1
                                      
                                    
                                    +
                                    
                                      x
                                      
                                        2
                                      
                                      
                                        2
                                      
                                    
                                     
                                    ,
                                  
                                  
                                  
                                    2
                                    
                                      x
                                      
                                        1
                                      
                                    
                                    
                                      x
                                      
                                        2
                                      
                                    
                                    +
                                    4
                                     
                                    sin
                                    ⁡
                                    (
                                    2
                                     
                                    
                                      x
                                      
                                        2
                                      
                                    
                                    )
                                     
                                    cos
                                    ⁡
                                    (
                                    2
                                     
                                    
                                      x
                                      
                                        2
                                      
                                    
                                    )
                                     
                                  
                                
                                
                                  
                                     
                                  
                                  
                                     
                                    2
                                     
                                    
                                      e
                                      
                                        2
                                         
                                        
                                          x
                                          
                                            1
                                          
                                        
                                        −
                                        
                                          x
                                          
                                            2
                                          
                                        
                                      
                                    
                                     
                                    ,
                                  
                                  
                                  
                                    
                                    −
                                    
                                      e
                                      
                                        2
                                         
                                        
                                          x
                                          
                                            1
                                          
                                        
                                        −
                                        
                                          x
                                          
                                            2
                                          
                                        
                                      
                                    
                                    +
                                    4
                                     
                                  
                                
                              
                            
                          
                        
                      
                      ]
                    
                  
                  
                    k
                  
                
                
                  
                    
                      [
                      
                        
                          
                             
                            
                              c
                              
                                1
                              
                            
                             
                          
                        
                        
                          
                             
                            
                              c
                              
                                2
                              
                            
                             
                          
                        
                      
                      ]
                    
                  
                  
                    k
                    +
                    1
                  
                
                =
                
                  
                    
                      [
                      
                        
                          
                             
                            5
                             
                            
                              x
                              
                                1
                              
                              
                                2
                              
                            
                            +
                            
                              x
                              
                                1
                              
                            
                             
                            
                              x
                              
                                2
                              
                              
                                2
                              
                            
                            +
                            
                              sin
                              
                                2
                              
                            
                            ⁡
                            (
                            2
                             
                            
                              x
                              
                                2
                              
                            
                            )
                            −
                            2
                             
                          
                        
                        
                          
                             
                            
                              e
                              
                                2
                                 
                                
                                  x
                                  
                                    1
                                  
                                
                                −
                                
                                  x
                                  
                                    2
                                  
                                
                              
                            
                            +
                            4
                             
                            
                              x
                              
                                2
                              
                            
                            −
                            3
                             
                          
                        
                      
                      ]
                    
                  
                  
                    k
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\begin{bmatrix}{\begin{aligned}~&~10\ x_{1}+x_{2}^{2}\ ,&&2x_{1}x_{2}+4\ \sin(2\ x_{2})\ \cos(2\ x_{2})~\\~&~2\ e^{2\ x_{1}-x_{2}}\ ,&&-e^{2\ x_{1}-x_{2}}+4~\end{aligned}}\end{bmatrix}}_{k}{\begin{bmatrix}~c_{1}~\\~c_{2}~\end{bmatrix}}_{k+1}={\begin{bmatrix}~5\ x_{1}^{2}+x_{1}\ x_{2}^{2}+\sin ^{2}(2\ x_{2})-2~\\~e^{2\ x_{1}-x_{2}}+4\ x_{2}-3~\end{bmatrix}}_{k}\end{aligned}}}
  

and

  
    
      
        
          X
          
            k
            +
            1
          
        
         
        =
         
        
          X
          
            k
          
        
        −
        
          C
          
            k
            +
            1
          
        
      
    
    {\displaystyle X_{k+1}~=~X_{k}-C_{k+1}}
  

The iterations should be repeated until 
  
    
      
         
        
          
            [
          
        
        
          ∑
          
            i
            =
            1
          
          
            i
            =
            2
          
        
        
          
            |
          
        
        f
        (
        
          x
          
            i
          
        
        
          )
          
            k
          
        
        −
        (
        
          y
          
            i
          
        
        
          )
          
            k
          
        
        
          
            |
          
        
        
          
            ]
          
        
        <
        E
         
        ,
      
    
    {\displaystyle \ {\Bigg [}\sum _{i=1}^{i=2}{\Bigl |}f(x_{i})_{k}-(y_{i})_{k}{\Bigr |}{\Bigg ]}<E\ ,}
  
 where 
  
    
      
         
        E
         
      
    
    {\displaystyle \ E\ }
  
 is a value acceptably small enough to meet application requirements.
If vector 
  
    
      
         
        
          X
          
            0
          
        
         
      
    
    {\displaystyle \ X_{0}\ }
  
 is initially chosen to be 
  
    
      
         
        
          
            [
            
              
                
                   
                  1
                   
                
                
                   
                  1
                   
                
              
            
            ]
          
        
         
        ,
      
    
    {\displaystyle \ {\begin{bmatrix}~1~&~1~\end{bmatrix}}\ ,}
  
 that is, 
  
    
      
         
        
          x
          
            1
          
        
        =
        1
         
        ,
      
    
    {\displaystyle \ x_{1}=1\ ,}
  
 and 
  
    
      
         
        
          x
          
            2
          
        
        =
        1
         
        ,
      
    
    {\displaystyle \ x_{2}=1\ ,}
  
 and 
  
    
      
         
        E
         
        ,
      
    
    {\displaystyle \ E\ ,}
  
 is chosen to be 1.10−3, then the example converges after four iterations to a value of 
  
    
      
         
        
          X
          
            4
          
        
        =
        
          [
          
             
            0.567297
            ,
             
            −
            0.309442
             
          
          ]
        
         
        .
      
    
    {\displaystyle \ X_{4}=\left[~0.567297,\ -0.309442~\right]~.}

Iterations
The following iterations were made during the course of the solution.

Complex functions
When dealing with complex functions, Newton's method can be directly applied to find their zeroes. Each zero has a basin of attraction in the complex plane, the set of all starting values that cause the method to converge to that particular zero. These sets can be mapped as in the image shown. For many complex functions, the boundaries of the basins of attraction are fractals.
In some cases there are regions in the complex plane which are not in any of these basins of attraction, meaning the iterates do not converge. For example, if one uses a real initial condition to seek a root of x2 + 1, all subsequent iterates will be real numbers and so the iterations cannot converge to either root, since both roots are non-real. In this case almost all real initial conditions lead to chaotic behavior, while some initial conditions iterate either to infinity or to repeating cycles of any finite length.
Curt McMullen has shown that for any possible purely iterative algorithm similar to Newton's method, the algorithm will diverge on some open regions of the complex plane when applied to some polynomial of degree 4 or higher. However, McMullen gave a generally convergent algorithm for polynomials of degree 3. Also, for any polynomial, Hubbard, Schleicher, and Sutherland gave a method for selecting a set of initial points such that  Newton's method will certainly converge at one of them at least.

In a Banach space
Another generalization is Newton's method to find a root of a functional F defined in a Banach space. In this case the formulation is

  
    
      
        
          X
          
            n
            +
            1
          
        
        =
        
          X
          
            n
          
        
        −
        
          
            (
          
        
        
          F
          ′
        
        (
        
          X
          
            n
          
        
        )
        
          
            
              )
            
          
          
            −
            1
          
        
        F
        (
        
          X
          
            n
          
        
        )
        ,
        
      
    
    {\displaystyle X_{n+1}=X_{n}-{\bigl (}F'(X_{n}){\bigr )}^{-1}F(X_{n}),\,}
  

where F′(Xn) is the Fréchet derivative computed at Xn. One needs the Fréchet derivative to be boundedly invertible at each Xn in order for the method to be applicable. A condition for existence of and convergence to a root is given by the Newton–Kantorovich theorem.

Nash–Moser iteration
In the 1950s, John Nash developed a version of the Newton's method to apply to the problem of constructing isometric embeddings of general Riemannian manifolds in Euclidean space. The loss of derivatives problem, present in this context, made the standard Newton iteration inapplicable, since it could not be continued indefinitely (much less converge). Nash's solution involved the introduction of smoothing operators into the iteration. He was able to prove the convergence of his smoothed Newton method, for the purpose of proving an implicit function theorem for isometric embeddings. In the 1960s, Jürgen Moser showed that Nash's methods were flexible enough to apply to problems beyond isometric embedding, particularly in celestial mechanics. Since then, a number of mathematicians, including Mikhael Gromov and Richard Hamilton, have found generalized abstract versions of the Nash–Moser theory. In Hamilton's formulation, the Nash–Moser theorem forms a generalization of the Banach space Newton method which takes place in certain Fréchet spaces.

Modifications
Quasi-Newton methods
When the Jacobian is unavailable or too expensive to compute at every iteration, a quasi-Newton method can be used.

Chebyshev's third-order method
Over p-adic numbers
In p-adic analysis, the standard method to show a polynomial equation in one variable has a p-adic root is Hensel's lemma, which uses the recursion from Newton's method on the p-adic numbers. Because of the more stable behavior of addition and multiplication in the p-adic numbers compared to the real numbers (specifically, the unit ball in the p-adics is a ring), convergence in Hensel's lemma can be guaranteed under much simpler hypotheses than in the classical Newton's method on the real line.

q-analog
Newton's method can be generalized with the q-analog of the usual derivative.

Modified Newton methods
Maehly's procedure
A nonlinear equation has multiple solutions in general. But if the initial value is not appropriate, Newton's method may not converge to the desired solution or may converge to the same solution found earlier. When we have already found N solutions of 
  
    
      
        f
        (
        x
        )
        =
        0
      
    
    {\displaystyle f(x)=0}
  
, then the next root can be found by applying Newton's method to the next equation:

  
    
      
        F
        (
        x
        )
        =
        
          
            
              f
              (
              x
              )
            
            
              
                ∏
                
                  i
                  =
                  1
                
                
                  N
                
              
              (
              x
              −
              
                x
                
                  i
                
              
              )
            
          
        
        =
        0.
      
    
    {\displaystyle F(x)={\frac {f(x)}{\prod _{i=1}^{N}(x-x_{i})}}=0.}
  

This method is applied to obtain zeros of the Bessel function of the second kind.

Hirano's modified Newton method
Hirano's modified Newton method is a modification conserving the convergence of Newton method and avoiding unstableness. It is developed to solve complex polynomials.

Interval Newton's method
Combining Newton's method with interval arithmetic is very useful in some contexts. This provides a stopping criterion that is more reliable than the usual ones (which are a small value of the function or a small variation of the variable between consecutive iterations). Also, this may detect cases where Newton's method converges theoretically but diverges numerically because of an insufficient floating-point precision (this is typically the case for polynomials of large degree, where a very small change of the variable may change dramatically the value of the function; see Wilkinson's polynomial).
Consider f → C1(X), where X is a real interval, and suppose that we have an interval extension F′ of f′, meaning that F′ takes as input an interval Y ⊆ X and outputs an interval F′(Y) such that:

  
    
      
        
          
            
              
                
                  F
                  ′
                
                (
                [
                y
                ,
                y
                ]
                )
              
              
                
                =
                {
                
                  f
                  ′
                
                (
                y
                )
                }
              
            
            
              
                
                  F
                  ′
                
                (
                Y
                )
              
              
                
                ⊇
                {
                
                  f
                  ′
                
                (
                y
                )
                ∣
                y
                ∈
                Y
                }
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}F'([y,y])&=\{f'(y)\}\\[5pt]F'(Y)&\supseteq \{f'(y)\mid y\in Y\}.\end{aligned}}}
  

We also assume that 0 ∉ F′(X), so in particular f has at most one root in X.
We then define the interval Newton operator by:

  
    
      
        N
        (
        Y
        )
        =
        m
        −
        
          
            
              f
              (
              m
              )
            
            
              
                F
                ′
              
              (
              Y
              )
            
          
        
        =
        
          {
          
            
              
              
                m
                −
                
                  
                    
                      f
                      (
                      m
                      )
                    
                    z
                  
                
                 
              
              |
            
             
            z
            ∈
            
              F
              ′
            
            (
            Y
            )
          
          }
        
      
    
    {\displaystyle N(Y)=m-{\frac {f(m)}{F'(Y)}}=\left\{\left.m-{\frac {f(m)}{z}}~\right|~z\in F'(Y)\right\}}
  

where m ∈ Y. Note that the hypothesis on F′ implies that N(Y) is well defined and is an interval (see interval arithmetic for further details on interval operations). This naturally leads to the following sequence:

  
    
      
        
          
            
              
                
                  X
                  
                    0
                  
                
              
              
                
                =
                X
              
            
            
              
                
                  X
                  
                    k
                    +
                    1
                  
                
              
              
                
                =
                N
                (
                
                  X
                  
                    k
                  
                
                )
                ∩
                
                  X
                  
                    k
                  
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}X_{0}&=X\\X_{k+1}&=N(X_{k})\cap X_{k}.\end{aligned}}}
  

The mean value theorem ensures that if there is a root of f in Xk, then it is also in Xk + 1. Moreover, the hypothesis on F′ ensures that Xk + 1 is at most half the size of Xk when m is the midpoint of Y, so this sequence converges towards [x*, x*], where x* is the root of f in X.
If F′(X) strictly contains 0, the use of extended interval division produces a union of two intervals for N(X); multiple roots are therefore automatically separated and bounded.

Applications
Minimization and maximization problems
Newton's method can be used to find a minimum or maximum of a function f(x). The derivative is zero at a minimum or maximum, so local minima and maxima can be found by applying Newton's method to the derivative. The iteration becomes:

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              
                f
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
            
              
                f
                ″
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
        .
      
    
    {\displaystyle x_{n+1}=x_{n}-{\frac {f'(x_{n})}{f''(x_{n})}}.}

Multiplicative inverses of numbers and power series
An important application is Newton–Raphson division, which can be used to quickly find the reciprocal of a number a, using only multiplication and subtraction, that is to say the number x such that ⁠1/x⁠ = a. We can rephrase that as finding the zero of f(x) = ⁠1/x⁠ − a. We have f′(x) = −⁠1/x2⁠.
Newton's iteration is

  
    
      
        
          x
          
            n
            +
            1
          
        
        =
        
          x
          
            n
          
        
        −
        
          
            
              f
              (
              
                x
                
                  n
                
              
              )
            
            
              
                f
                ′
              
              (
              
                x
                
                  n
                
              
              )
            
          
        
        =
        
          x
          
            n
          
        
        +
        
          
            
              
                
                  1
                  
                    x
                    
                      n
                    
                  
                
              
              −
              a
            
            
              1
              
                x
                
                  n
                
                
                  2
                
              
            
          
        
        =
        
          x
          
            n
          
        
        (
        2
        −
        a
        
          x
          
            n
          
        
        )
        .
      
    
    {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=x_{n}+{\frac {{\frac {1}{x_{n}}}-a}{\frac {1}{x_{n}^{2}}}}=x_{n}(2-ax_{n}).}
  

Therefore, Newton's iteration needs only two multiplications and one subtraction.
This method is also very efficient to compute the multiplicative inverse of a power series.

Solving transcendental equations
Many transcendental equations can be solved up to an arbitrary precision by using Newton's method. For example, finding the cumulative probability density function, such as a Normal distribution to fit a known probability generally involves integral functions with no known means to solve in closed form.  However, computing the derivatives needed to solve them numerically with Newton's method is generally known, making numerical solutions possible.  For an example, see the numerical solution to the inverse Normal cumulative distribution.

Numerical verification for solutions of nonlinear equations
A numerical verification for solutions of nonlinear equations has been established by using Newton's method multiple times and forming a set of solution candidates.

Code
The following is an example of a possible implementation of Newton's method in the Python (version 3.x) programming language for finding a root of a function f which has derivative f_prime.
The initial guess will be x0 = 1 and the function will be f(x) = x2 − 2 so that f′(x) = 2x.
Each new iteration of Newton's method will be denoted by x1. We will check during the computation whether the denominator (yprime) becomes too small (smaller than epsilon), which would be the case if f′(xn) ≈ 0, since otherwise a large amount of error could be introduced.

See also
Notes
References
Gil, A.; Segura, J.; Temme, N. M. (2007). Numerical methods for special functions. Society for Industrial and Applied Mathematics. ISBN 978-0-89871-634-4.
Süli, Endre; Mayers, David (2003). An Introduction to Numerical Analysis. Cambridge University Press. ISBN 0-521-00794-1.

Further reading
Kendall E. Atkinson, An Introduction to Numerical Analysis, (1989) John Wiley & Sons, Inc, ISBN 0-471-62489-6
Tjalling J. Ypma, Historical development of the Newton–Raphson method, SIAM Review 37 (4), 531–551, 1995. doi:10.1137/1037125.
Bonnans, J. Frédéric; Gilbert, J. Charles; Lemaréchal, Claude; Sagastizábal, Claudia A. (2006). Numerical optimization: Theoretical and practical aspects. Universitext (Second revised ed. of translation of 1997  French ed.). Berlin: Springer-Verlag. pp. xiv+490. doi:10.1007/978-3-540-35447-5. ISBN 3-540-35445-X. MR 2265882.
P. Deuflhard, Newton Methods for Nonlinear Problems. Affine Invariance and Adaptive Algorithms. Springer Series in Computational Mathematics, Vol. 35. Springer, Berlin, 2004. ISBN 3-540-21099-7.
C. T. Kelley, Solving Nonlinear Equations with Newton's Method, no 1 in Fundamentals of Algorithms, SIAM, 2003. ISBN 0-89871-546-6.
J. M. Ortega, W. C. Rheinboldt, Iterative Solution of Nonlinear Equations in Several Variables. Classics in Applied Mathematics, SIAM, 2000. ISBN 0-89871-461-3.
Press, W. H.; Teukolsky, S. A.; Vetterling, W. T.; Flannery, B. P. (2007). "Chapter 9. Root Finding and Nonlinear Sets of Equations Importance Sampling". Numerical Recipes: The Art of Scientific Computing (3rd ed.). New York: Cambridge University Press. ISBN 978-0-521-88068-8.. See especially Sections 9.4, 9.6, and 9.7.
Avriel, Mordecai (1976). Nonlinear Programming: Analysis and Methods. Prentice Hall. pp. 216–221. ISBN 0-13-623603-0.

External links

"Newton method", Encyclopedia of Mathematics, EMS Press, 2001 [1994]
Weisstein, Eric W. "Newton's Method". MathWorld.
Newton's method, Citizendium.
Mathews, J., The Accelerated and Modified Newton Methods, Course notes.
Wu, X., Roots of Equations, Course notes.

## Related Articles

### Internal Links

- [Aberth method](https://en.wikipedia.org/wiki/Aberth_method)
- [Abraham de Moivre](https://en.wikipedia.org/wiki/Abraham_de_Moivre)
- [Absolute space and time](https://en.wikipedia.org/wiki/Absolute_space_and_time)
- [Academic Press](https://en.wikipedia.org/wiki/Academic_Press)
- [Active-set method](https://en.wikipedia.org/wiki/Active-set_method)
- [Affine scaling](https://en.wikipedia.org/wiki/Affine_scaling)
- [Aitken's delta-squared process](https://en.wikipedia.org/wiki/Aitken%27s_delta-squared_process)
- [Alexander Ostrowski](https://en.wikipedia.org/wiki/Alexander_Ostrowski)
- [Almost all](https://en.wikipedia.org/wiki/Almost_all)
- [An Historical Account of Two Notable Corruptions of Scripture](https://en.wikipedia.org/wiki/An_Historical_Account_of_Two_Notable_Corruptions_of_Scripture)
- [Ancient Greece](https://en.wikipedia.org/wiki/Ancient_Greece)
- [Approximation algorithm](https://en.wikipedia.org/wiki/Approximation_algorithm)
- [Arithmetic mean](https://en.wikipedia.org/wiki/Arithmetic_mean)
- [Arithmetic](https://en.wikipedia.org/wiki/Arithmetic)
- [Arithmetica Universalis](https://en.wikipedia.org/wiki/Arithmetica_Universalis)
- [Arthur Cayley](https://en.wikipedia.org/wiki/Arthur_Cayley)
- [Astronomers Monument](https://en.wikipedia.org/wiki/Astronomers_Monument)
- [Augmented Lagrangian method](https://en.wikipedia.org/wiki/Augmented_Lagrangian_method)
- [Babylonia](https://en.wikipedia.org/wiki/Babylonia)
- [Bairstow's method](https://en.wikipedia.org/wiki/Bairstow%27s_method)
- [Banach space](https://en.wikipedia.org/wiki/Banach_space)
- [Barrier function](https://en.wikipedia.org/wiki/Barrier_function)
- [Attractor](https://en.wikipedia.org/wiki/Attractor)
- [Bellman–Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
- [Benjamin Pulleyn](https://en.wikipedia.org/wiki/Benjamin_Pulleyn)
- [Berndt–Hall–Hall–Hausman algorithm](https://en.wikipedia.org/wiki/Berndt%E2%80%93Hall%E2%80%93Hall%E2%80%93Hausman_algorithm)
- [Bessel function](https://en.wikipedia.org/wiki/Bessel_function)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Bisection method](https://en.wikipedia.org/wiki/Bisection_method)
- [Borůvka's algorithm](https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm)
- [Branch and bound](https://en.wikipedia.org/wiki/Branch_and_bound)
- [Branch and cut](https://en.wikipedia.org/wiki/Branch_and_cut)
- [Brent's method](https://en.wikipedia.org/wiki/Brent%27s_method)
- [Broyden's method](https://en.wikipedia.org/wiki/Broyden%27s_method)
- [Broyden–Fletcher–Goldfarb–Shanno algorithm](https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm)
- [Bucket argument](https://en.wikipedia.org/wiki/Bucket_argument)
- [Bulletin of the American Mathematical Society](https://en.wikipedia.org/wiki/Bulletin_of_the_American_Mathematical_Society)
- [Calculus](https://en.wikipedia.org/wiki/Calculus)
- [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press)
- [Catherine Barton](https://en.wikipedia.org/wiki/Catherine_Barton)
- [Celestial mechanics](https://en.wikipedia.org/wiki/Celestial_mechanics)
- [Chaos theory](https://en.wikipedia.org/wiki/Chaos_theory)
- [Chebyshev iteration](https://en.wikipedia.org/wiki/Chebyshev_iteration)
- [Classical mechanics](https://en.wikipedia.org/wiki/Classical_mechanics)
- [Claude Lemaréchal](https://en.wikipedia.org/wiki/Claude_Lemar%C3%A9chal)
- [Claudia Sagastizábal](https://en.wikipedia.org/wiki/Claudia_Sagastiz%C3%A1bal)
- [Combinatorial optimization](https://en.wikipedia.org/wiki/Combinatorial_optimization)
- [Comparison of optimization software](https://en.wikipedia.org/wiki/Comparison_of_optimization_software)
- [Complex analysis](https://en.wikipedia.org/wiki/Complex_analysis)
- [Complex analysis](https://en.wikipedia.org/wiki/Complex_analysis)
- [Complex plane](https://en.wikipedia.org/wiki/Complex_plane)
- [Concave function](https://en.wikipedia.org/wiki/Concave_function)
- [Convex optimization](https://en.wikipedia.org/wiki/Convex_optimization)
- [Convex optimization](https://en.wikipedia.org/wiki/Convex_optimization)
- [Copernican Revolution](https://en.wikipedia.org/wiki/Copernican_Revolution)
- [Corpuscular theory of light](https://en.wikipedia.org/wiki/Corpuscular_theory_of_light)
- [Cranbury Park](https://en.wikipedia.org/wiki/Cranbury_Park)
- [Criss-cross algorithm](https://en.wikipedia.org/wiki/Criss-cross_algorithm)
- [Cutting-plane method](https://en.wikipedia.org/wiki/Cutting-plane_method)
- [Davidon–Fletcher–Powell formula](https://en.wikipedia.org/wiki/Davidon%E2%80%93Fletcher%E2%80%93Powell_formula)
- [De analysi per aequationes numero terminorum infinitas](https://en.wikipedia.org/wiki/De_analysi_per_aequationes_numero_terminorum_infinitas)
- [De motu corporum in gyrum](https://en.wikipedia.org/wiki/De_motu_corporum_in_gyrum)
- [Derivative](https://en.wikipedia.org/wiki/Derivative)
- [Difference quotient](https://en.wikipedia.org/wiki/Difference_quotient)
- [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Dinic's algorithm](https://en.wikipedia.org/wiki/Dinic%27s_algorithm)
- [Division algorithm](https://en.wikipedia.org/wiki/Division_algorithm)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Durand–Kerner method](https://en.wikipedia.org/wiki/Durand%E2%80%93Kerner_method)
- [Dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming)
- [Early life of Isaac Newton](https://en.wikipedia.org/wiki/Early_life_of_Isaac_Newton)
- [Edmonds–Karp algorithm](https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm)
- [Ellipsoid method](https://en.wikipedia.org/wiki/Ellipsoid_method)
- [Encyclopedia of Mathematics](https://en.wikipedia.org/wiki/Encyclopedia_of_Mathematics)
- [Endre Süli](https://en.wikipedia.org/wiki/Endre_S%C3%BCli)
- [Eric W. Weisstein](https://en.wikipedia.org/wiki/Eric_W._Weisstein)
- [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space)
- [Euler method](https://en.wikipedia.org/wiki/Euler_method)
- [European Mathematical Society](https://en.wikipedia.org/wiki/European_Mathematical_Society)
- [Evolutionary algorithm](https://en.wikipedia.org/wiki/Evolutionary_algorithm)
- [Greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm)
- [Fast inverse square root](https://en.wikipedia.org/wiki/Fast_inverse_square_root)
- [Finite difference](https://en.wikipedia.org/wiki/Finite_difference)
- [Fixed-point iteration](https://en.wikipedia.org/wiki/Fixed-point_iteration)
- [Floating-point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic)
- [Flow network](https://en.wikipedia.org/wiki/Flow_network)
- [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)
- [Fluxion](https://en.wikipedia.org/wiki/Fluxion)
- [Ford–Fulkerson algorithm](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm)
- [Fractal](https://en.wikipedia.org/wiki/Fractal)
- [Frank–Wolfe algorithm](https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm)
- [François Viète](https://en.wikipedia.org/wiki/Fran%C3%A7ois_Vi%C3%A8te)
- [Fréchet derivative](https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative)
- [Fréchet space](https://en.wikipedia.org/wiki/Fr%C3%A9chet_space)
- [Function (mathematics)](https://en.wikipedia.org/wiki/Function_(mathematics))
- [Functional (mathematics)](https://en.wikipedia.org/wiki/Functional_(mathematics))
- [Gauss–Newton algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton_algorithm)
- [General Scholium](https://en.wikipedia.org/wiki/General_Scholium)
- [Generalized Gauss–Newton method](https://en.wikipedia.org/wiki/Generalized_Gauss%E2%80%93Newton_method)
- [Generalized inverse](https://en.wikipedia.org/wiki/Generalized_inverse)
- [Golden-section search](https://en.wikipedia.org/wiki/Golden-section_search)
- [Gradient](https://en.wikipedia.org/wiki/Gradient)
- [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent)
- [Graeffe's method](https://en.wikipedia.org/wiki/Graeffe%27s_method)
- [List of algorithms](https://en.wikipedia.org/wiki/List_of_algorithms)
- [Graph of a function](https://en.wikipedia.org/wiki/Graph_of_a_function)
- [Gravitational constant](https://en.wikipedia.org/wiki/Gravitational_constant)
- [Greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm)
- [Halley's method](https://en.wikipedia.org/wiki/Halley%27s_method)
- [Henry Briggs (mathematician)](https://en.wikipedia.org/wiki/Henry_Briggs_(mathematician))
- [Hensel's lemma](https://en.wikipedia.org/wiki/Hensel%27s_lemma)
- [Hessian matrix](https://en.wikipedia.org/wiki/Hessian_matrix)
- [Heuristic (computer science)](https://en.wikipedia.org/wiki/Heuristic_(computer_science))
- [Hill climbing](https://en.wikipedia.org/wiki/Hill_climbing)
- [Householder's method](https://en.wikipedia.org/wiki/Householder%27s_method)
- [Hypotheses non fingo](https://en.wikipedia.org/wiki/Hypotheses_non_fingo)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [ITP method](https://en.wikipedia.org/wiki/ITP_method)
- [Impact depth](https://en.wikipedia.org/wiki/Impact_depth)
- [Implicit function theorem](https://en.wikipedia.org/wiki/Implicit_function_theorem)
- [Inertia](https://en.wikipedia.org/wiki/Inertia)
- [Isaac Newton Medal](https://en.wikipedia.org/wiki/Isaac_Newton_Medal)
- [Integer programming](https://en.wikipedia.org/wiki/Integer_programming)
- [Integer square root](https://en.wikipedia.org/wiki/Integer_square_root)
- [Intermediate value theorem](https://en.wikipedia.org/wiki/Intermediate_value_theorem)
- [Interval arithmetic](https://en.wikipedia.org/wiki/Interval_arithmetic)
- [Inverse quadratic interpolation](https://en.wikipedia.org/wiki/Inverse_quadratic_interpolation)
- [Isaac Barrow](https://en.wikipedia.org/wiki/Isaac_Barrow)
- [Isaac Newton](https://en.wikipedia.org/wiki/Isaac_Newton)
- [Isaac Newton's apple tree](https://en.wikipedia.org/wiki/Isaac_Newton%27s_apple_tree)
- [Isaac Newton's occult studies](https://en.wikipedia.org/wiki/Isaac_Newton%27s_occult_studies)
- [Isaac Newton Gargoyle](https://en.wikipedia.org/wiki/Isaac_Newton_Gargoyle)
- [Isaac Newton Group of Telescopes](https://en.wikipedia.org/wiki/Isaac_Newton_Group_of_Telescopes)
- [Isaac Newton Institute](https://en.wikipedia.org/wiki/Isaac_Newton_Institute)
- [Isaac Newton Telescope](https://en.wikipedia.org/wiki/Isaac_Newton_Telescope)
- [Isaac Newton in popular culture](https://en.wikipedia.org/wiki/Isaac_Newton_in_popular_culture)
- [Embedding](https://en.wikipedia.org/wiki/Embedding)
- [Iterative method](https://en.wikipedia.org/wiki/Iterative_method)
- [JSTOR](https://en.wikipedia.org/wiki/JSTOR)
- [Jacobian matrix and determinant](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant)
- [Jacobian matrix and determinant](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant)
- [Jamshid al-Kashi](https://en.wikipedia.org/wiki/Jamshid_al-Kashi)
- [Jenkins–Traub algorithm](https://en.wikipedia.org/wiki/Jenkins%E2%80%93Traub_algorithm)
- [John Colson](https://en.wikipedia.org/wiki/John_Colson)
- [John Conduitt](https://en.wikipedia.org/wiki/John_Conduitt)
- [John Forbes Nash Jr.](https://en.wikipedia.org/wiki/John_Forbes_Nash_Jr.)
- [John Keill](https://en.wikipedia.org/wiki/John_Keill)
- [John Wallis](https://en.wikipedia.org/wiki/John_Wallis)
- [Joseph F. Traub](https://en.wikipedia.org/wiki/Joseph_F._Traub)
- [Joseph Fourier](https://en.wikipedia.org/wiki/Joseph_Fourier)
- [Joseph Raphson](https://en.wikipedia.org/wiki/Joseph_Raphson)
- [Julia set](https://en.wikipedia.org/wiki/Julia_set)
- [Jürgen Moser](https://en.wikipedia.org/wiki/J%C3%BCrgen_Moser)
- [Kantorovich theorem](https://en.wikipedia.org/wiki/Kantorovich_theorem)
- [Karmarkar's algorithm](https://en.wikipedia.org/wiki/Karmarkar%27s_algorithm)
- [Kepler's laws of planetary motion](https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion)
- [Kissing number](https://en.wikipedia.org/wiki/Kissing_number)
- [Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)
- [Taylor's theorem](https://en.wikipedia.org/wiki/Taylor%27s_theorem)
- [Laguerre's method](https://en.wikipedia.org/wiki/Laguerre%27s_method)
- [Later life of Isaac Newton](https://en.wikipedia.org/wiki/Later_life_of_Isaac_Newton)
- [Lehmer–Schur algorithm](https://en.wikipedia.org/wiki/Lehmer%E2%80%93Schur_algorithm)
- [Leibniz–Newton calculus controversy](https://en.wikipedia.org/wiki/Leibniz%E2%80%93Newton_calculus_controversy)
- [Lemke's algorithm](https://en.wikipedia.org/wiki/Lemke%27s_algorithm)
- [Levenberg–Marquardt algorithm](https://en.wikipedia.org/wiki/Levenberg%E2%80%93Marquardt_algorithm)
- [Limit of a sequence](https://en.wikipedia.org/wiki/Limit_of_a_sequence)
- [Limited-memory BFGS](https://en.wikipedia.org/wiki/Limited-memory_BFGS)
- [Line search](https://en.wikipedia.org/wiki/Line_search)
- [Linear approximation](https://en.wikipedia.org/wiki/Linear_approximation)
- [Linear programming](https://en.wikipedia.org/wiki/Linear_programming)
- [List of things named after Isaac Newton](https://en.wikipedia.org/wiki/List_of_things_named_after_Isaac_Newton)
- [Local convergence](https://en.wikipedia.org/wiki/Local_convergence)
- [Local search (optimization)](https://en.wikipedia.org/wiki/Local_search_(optimization))
- [Luminiferous aether](https://en.wikipedia.org/wiki/Luminiferous_aether)
- [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
- [Mathematical Reviews](https://en.wikipedia.org/wiki/Mathematical_Reviews)
- [MathWorld](https://en.wikipedia.org/wiki/MathWorld)
- [Mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization)
- [Mathematics in the medieval Islamic world](https://en.wikipedia.org/wiki/Mathematics_in_the_medieval_Islamic_world)
- [Matroid](https://en.wikipedia.org/wiki/Matroid)
- [Mean value theorem](https://en.wikipedia.org/wiki/Mean_value_theorem)
- [Metaheuristic](https://en.wikipedia.org/wiki/Metaheuristic)
- [Method of Fluxions](https://en.wikipedia.org/wiki/Method_of_Fluxions)
- [Methods of computing square roots](https://en.wikipedia.org/wiki/Methods_of_computing_square_roots)
- [Mikhael Gromov (mathematician)](https://en.wikipedia.org/wiki/Mikhael_Gromov_(mathematician))
- [Minimum spanning tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree)
- [Mirror descent](https://en.wikipedia.org/wiki/Mirror_descent)
- [Monotonic function](https://en.wikipedia.org/wiki/Monotonic_function)
- [Monotonic function](https://en.wikipedia.org/wiki/Monotonic_function)
- [Muller's method](https://en.wikipedia.org/wiki/Muller%27s_method)
- [Multiplicative inverse](https://en.wikipedia.org/wiki/Multiplicative_inverse)
- [Multiplicity (mathematics)](https://en.wikipedia.org/wiki/Multiplicity_(mathematics))
- [Nash–Moser theorem](https://en.wikipedia.org/wiki/Nash%E2%80%93Moser_theorem)
- [Natural logarithm](https://en.wikipedia.org/wiki/Natural_logarithm)
- [Neighbourhood (mathematics)](https://en.wikipedia.org/wiki/Neighbourhood_(mathematics))
- [Nelder–Mead method](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method)
- [Newton's cannonball](https://en.wikipedia.org/wiki/Newton%27s_cannonball)
- [Newton's cradle](https://en.wikipedia.org/wiki/Newton%27s_cradle)
- [Newton's identities](https://en.wikipedia.org/wiki/Newton%27s_identities)
- [Newton's inequalities](https://en.wikipedia.org/wiki/Newton%27s_inequalities)
- [Newton's law of cooling](https://en.wikipedia.org/wiki/Newton%27s_law_of_cooling)
- [Newton's law of universal gravitation](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation)
- [Newton's laws of motion](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion)
- [Newton's metal](https://en.wikipedia.org/wiki/Newton%27s_metal)
- [Newton's method in optimization](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization)
- [Notation for differentiation](https://en.wikipedia.org/wiki/Notation_for_differentiation)
- [Newton's reflector](https://en.wikipedia.org/wiki/Newton%27s_reflector)
- [Newton's rings](https://en.wikipedia.org/wiki/Newton%27s_rings)
- [Newton's theorem about ovals](https://en.wikipedia.org/wiki/Newton%27s_theorem_about_ovals)
- [Newton's theorem of revolving orbits](https://en.wikipedia.org/wiki/Newton%27s_theorem_of_revolving_orbits)
- [Newton (Blake)](https://en.wikipedia.org/wiki/Newton_(Blake))
- [Newton (Paolozzi)](https://en.wikipedia.org/wiki/Newton_(Paolozzi))
- [Newton (unit)](https://en.wikipedia.org/wiki/Newton_(unit))
- [Newton International Fellowship](https://en.wikipedia.org/wiki/Newton_International_Fellowship)
- [Newton disc](https://en.wikipedia.org/wiki/Newton_disc)
- [Newton fractal](https://en.wikipedia.org/wiki/Newton_fractal)
- [Newton polygon](https://en.wikipedia.org/wiki/Newton_polygon)
- [Newton polynomial](https://en.wikipedia.org/wiki/Newton_polynomial)
- [Newton scale](https://en.wikipedia.org/wiki/Newton_scale)
- [Newtonian dynamics](https://en.wikipedia.org/wiki/Newtonian_dynamics)
- [Newtonian fluid](https://en.wikipedia.org/wiki/Newtonian_fluid)
- [Newtonian potential](https://en.wikipedia.org/wiki/Newtonian_potential)
- [Newtonian telescope](https://en.wikipedia.org/wiki/Newtonian_telescope)
- [Newtonianism](https://en.wikipedia.org/wiki/Newtonianism)
- [Newton–Cartan theory](https://en.wikipedia.org/wiki/Newton%E2%80%93Cartan_theory)
- [Newton–Cotes formulas](https://en.wikipedia.org/wiki/Newton%E2%80%93Cotes_formulas)
- [Newton–Euler equations](https://en.wikipedia.org/wiki/Newton%E2%80%93Euler_equations)
- [Newton–Krylov method](https://en.wikipedia.org/wiki/Newton%E2%80%93Krylov_method)
- [Newton–Okounkov body](https://en.wikipedia.org/wiki/Newton%E2%80%93Okounkov_body)
- [Newton–Pepys problem](https://en.wikipedia.org/wiki/Newton%E2%80%93Pepys_problem)
- [Non-linear least squares](https://en.wikipedia.org/wiki/Non-linear_least_squares)
- [Nonlinear conjugate gradient method](https://en.wikipedia.org/wiki/Nonlinear_conjugate_gradient_method)
- [Nonlinear programming](https://en.wikipedia.org/wiki/Nonlinear_programming)
- [Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)
- [Notes on the Jewish Temple](https://en.wikipedia.org/wiki/Notes_on_the_Jewish_Temple)
- [Numerical analysis](https://en.wikipedia.org/wiki/Numerical_analysis)
- [OCLC](https://en.wikipedia.org/wiki/OCLC)
- [Opticks](https://en.wikipedia.org/wiki/Opticks)
- [Mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization)
- [Rate of convergence](https://en.wikipedia.org/wiki/Rate_of_convergence)
- [Parallel metaheuristic](https://en.wikipedia.org/wiki/Parallel_metaheuristic)
- [Parallelogram of force](https://en.wikipedia.org/wiki/Parallelogram_of_force)
- [Parameterized post-Newtonian formalism](https://en.wikipedia.org/wiki/Parameterized_post-Newtonian_formalism)
- [Penalty method](https://en.wikipedia.org/wiki/Penalty_method)
- [Peter Henrici (mathematician)](https://en.wikipedia.org/wiki/Peter_Henrici_(mathematician))
- [Philosophiæ Naturalis Principia Mathematica](https://en.wikipedia.org/wiki/Philosophi%C3%A6_Naturalis_Principia_Mathematica)
- [Polynomial root-finding algorithms](https://en.wikipedia.org/wiki/Polynomial_root-finding_algorithms)
- [Post-Newtonian expansion](https://en.wikipedia.org/wiki/Post-Newtonian_expansion)
- [Powell's dog leg method](https://en.wikipedia.org/wiki/Powell%27s_dog_leg_method)
- [Powell's method](https://en.wikipedia.org/wiki/Powell%27s_method)
- [Power number](https://en.wikipedia.org/wiki/Power_number)
- [Power series](https://en.wikipedia.org/wiki/Power_series)
- [Prentice Hall](https://en.wikipedia.org/wiki/Prentice_Hall)
- [Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm)
- [Probability density function](https://en.wikipedia.org/wiki/Probability_density_function)
- [Problem of Apollonius](https://en.wikipedia.org/wiki/Problem_of_Apollonius)
- [Puiseux series](https://en.wikipedia.org/wiki/Puiseux_series)
- [Push–relabel maximum flow algorithm](https://en.wikipedia.org/wiki/Push%E2%80%93relabel_maximum_flow_algorithm)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Q-analog](https://en.wikipedia.org/wiki/Q-analog)
- [Quadratic programming](https://en.wikipedia.org/wiki/Quadratic_programming)
- [Quaestiones quaedam philosophicae](https://en.wikipedia.org/wiki/Quaestiones_quaedam_philosophicae)
- [Quasi-Newton method](https://en.wikipedia.org/wiki/Quasi-Newton_method)
- [Rate of convergence](https://en.wikipedia.org/wiki/Rate_of_convergence)
- [Real-valued function](https://en.wikipedia.org/wiki/Real-valued_function)
- [Real number](https://en.wikipedia.org/wiki/Real_number)
- [Regula falsi](https://en.wikipedia.org/wiki/Regula_falsi)
- [Religious views of Isaac Newton](https://en.wikipedia.org/wiki/Religious_views_of_Isaac_Newton)
- [Revised simplex method](https://en.wikipedia.org/wiki/Revised_simplex_method)
- [Richard S. Hamilton](https://en.wikipedia.org/wiki/Richard_S._Hamilton)
- [Richardson extrapolation](https://en.wikipedia.org/wiki/Richardson_extrapolation)
- [Ridders' method](https://en.wikipedia.org/wiki/Ridders%27_method)
- [Riemannian manifold](https://en.wikipedia.org/wiki/Riemannian_manifold)
- [Roger Cotes](https://en.wikipedia.org/wiki/Roger_Cotes)
- [Root-finding algorithm](https://en.wikipedia.org/wiki/Root-finding_algorithm)
- [Root-finding algorithm](https://en.wikipedia.org/wiki/Root-finding_algorithm)
- [Zero of a function](https://en.wikipedia.org/wiki/Zero_of_a_function)
- [Rotating spheres](https://en.wikipedia.org/wiki/Rotating_spheres)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Schrödinger–Newton equation](https://en.wikipedia.org/wiki/Schr%C3%B6dinger%E2%80%93Newton_equation)
- [Scientific Revolution](https://en.wikipedia.org/wiki/Scientific_Revolution)
- [Scoring algorithm](https://en.wikipedia.org/wiki/Scoring_algorithm)
- [Secant method](https://en.wikipedia.org/wiki/Secant_method)
- [Second derivative](https://en.wikipedia.org/wiki/Second_derivative)
- [Seki Takakazu](https://en.wikipedia.org/wiki/Seki_Takakazu)
- [Sequence](https://en.wikipedia.org/wiki/Sequence)
- [Sequential quadratic programming](https://en.wikipedia.org/wiki/Sequential_quadratic_programming)
- [Sharaf al-Din al-Tusi](https://en.wikipedia.org/wiki/Sharaf_al-Din_al-Tusi)
- [Bellman–Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
- [Shortest path problem](https://en.wikipedia.org/wiki/Shortest_path_problem)
- [Sidi's generalized secant method](https://en.wikipedia.org/wiki/Sidi%27s_generalized_secant_method)
- [Simplex algorithm](https://en.wikipedia.org/wiki/Simplex_algorithm)
- [Simulated annealing](https://en.wikipedia.org/wiki/Simulated_annealing)
- [Sir Isaac Newton Sixth Form](https://en.wikipedia.org/wiki/Sir_Isaac_Newton_Sixth_Form)
- [Smoothing](https://en.wikipedia.org/wiki/Smoothing)
- [Spectrum](https://en.wikipedia.org/wiki/Spectrum)
- [Spiral optimization algorithm](https://en.wikipedia.org/wiki/Spiral_optimization_algorithm)
- [Splitting circle method](https://en.wikipedia.org/wiki/Splitting_circle_method)
- [Springer Science+Business Media](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Standing on the shoulders of giants](https://en.wikipedia.org/wiki/Standing_on_the_shoulders_of_giants)
- [Statal Institute of Higher Education Isaac Newton](https://en.wikipedia.org/wiki/Statal_Institute_of_Higher_Education_Isaac_Newton)
- [Steffensen's method](https://en.wikipedia.org/wiki/Steffensen%27s_method)
- [Stephen P. Boyd](https://en.wikipedia.org/wiki/Stephen_P._Boyd)
- [Monotonic function](https://en.wikipedia.org/wiki/Monotonic_function)
- [Structural coloration](https://en.wikipedia.org/wiki/Structural_coloration)
- [Subgradient method](https://en.wikipedia.org/wiki/Subgradient_method)
- [Successive linear programming](https://en.wikipedia.org/wiki/Successive_linear_programming)
- [Successive over-relaxation](https://en.wikipedia.org/wiki/Successive_over-relaxation)
- [Successive parabolic interpolation](https://en.wikipedia.org/wiki/Successive_parabolic_interpolation)
- [Symmetric rank-one](https://en.wikipedia.org/wiki/Symmetric_rank-one)
- [System of linear equations](https://en.wikipedia.org/wiki/System_of_linear_equations)
- [Nonlinear system](https://en.wikipedia.org/wiki/Nonlinear_system)
- [System of equations](https://en.wikipedia.org/wiki/System_of_equations)
- [Table of Newtonian series](https://en.wikipedia.org/wiki/Table_of_Newtonian_series)
- [Tabu search](https://en.wikipedia.org/wiki/Tabu_search)
- [Tangent](https://en.wikipedia.org/wiki/Tangent)
- [Tangent](https://en.wikipedia.org/wiki/Tangent)
- [Taylor's theorem](https://en.wikipedia.org/wiki/Taylor%27s_theorem)
- [Taylor series](https://en.wikipedia.org/wiki/Taylor_series)
- [Taylor series](https://en.wikipedia.org/wiki/Taylor_series)
- [The Chronology of Ancient Kingdoms Amended](https://en.wikipedia.org/wiki/The_Chronology_of_Ancient_Kingdoms_Amended)
- [The College Mathematics Journal](https://en.wikipedia.org/wiki/The_College_Mathematics_Journal)
- [Opticks](https://en.wikipedia.org/wiki/Opticks)
- [Thomas Simpson](https://en.wikipedia.org/wiki/Thomas_Simpson)
- [Neighbourhood (mathematics)](https://en.wikipedia.org/wiki/Neighbourhood_(mathematics))
- [Transcendental equation](https://en.wikipedia.org/wiki/Transcendental_equation)
- [Truncated Newton method](https://en.wikipedia.org/wiki/Truncated_Newton_method)
- [Trust region](https://en.wikipedia.org/wiki/Trust_region)
- [Wikibooks](https://en.wikipedia.org/wiki/Wikibooks)
- [Wilkinson's polynomial](https://en.wikipedia.org/wiki/Wilkinson%27s_polynomial)
- [William Clarke (apothecary)](https://en.wikipedia.org/wiki/William_Clarke_(apothecary))
- [William Jones (mathematician)](https://en.wikipedia.org/wiki/William_Jones_(mathematician))
- [William Stukeley](https://en.wikipedia.org/wiki/William_Stukeley)
- [William Whiston](https://en.wikipedia.org/wiki/William_Whiston)
- [Wolfe conditions](https://en.wikipedia.org/wiki/Wolfe_conditions)
- [Woolsthorpe Manor](https://en.wikipedia.org/wiki/Woolsthorpe_Manor)
- [Zero of a function](https://en.wikipedia.org/wiki/Zero_of_a_function)
- [XMM-Newton](https://en.wikipedia.org/wiki/XMM-Newton)
- [ZbMATH Open](https://en.wikipedia.org/wiki/ZbMATH_Open)
- [Zero of a function](https://en.wikipedia.org/wiki/Zero_of_a_function)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Isaac Newton](https://en.wikipedia.org/wiki/Template:Isaac_Newton)
- [Template:Optimization algorithms](https://en.wikipedia.org/wiki/Template:Optimization_algorithms)
- [Template:Root-finding algorithms](https://en.wikipedia.org/wiki/Template:Root-finding_algorithms)
- [Template talk:Isaac Newton](https://en.wikipedia.org/wiki/Template_talk:Isaac_Newton)
- [Template talk:Optimization algorithms](https://en.wikipedia.org/wiki/Template_talk:Optimization_algorithms)
- [Template talk:Root-finding algorithms](https://en.wikipedia.org/wiki/Template_talk:Root-finding_algorithms)
- [Help:Authority control](https://en.wikipedia.org/wiki/Help:Authority_control)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles lacking reliable references from February 2019](https://en.wikipedia.org/wiki/Category:Articles_lacking_reliable_references_from_February_2019)
- [Category:Articles to be expanded from February 2019](https://en.wikipedia.org/wiki/Category:Articles_to_be_expanded_from_February_2019)
- [Category:Articles with unsourced statements from June 2024](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_June_2024)
- [Category:Use dmy dates from January 2020](https://en.wikipedia.org/wiki/Category:Use_dmy_dates_from_January_2020)
- [Category:Wikipedia articles needing page number citations from June 2024](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_needing_page_number_citations_from_June_2024)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:37:36.400787+00:00_