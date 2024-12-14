# Automatic differentiation

## Article Metadata

- **Last Updated:** 2024-12-14T19:32:44.582676+00:00
- **Original Article:** [Automatic differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation)
- **Language:** en
- **Page ID:** 734787

## Summary

In mathematics and computer algebra, automatic differentiation (auto-differentiation, autodiff, or AD), also called algorithmic differentiation, computational differentiation, is a set of techniques to evaluate the partial derivative of a function specified by a computer program.
Automatic differentiation exploits the fact that every computer calculation, no matter how complicated, executes a sequence of elementary arithmetic operations (addition, subtraction, multiplication, division, etc.) and

## Categories

- Category:Articles with example C++ code
- Category:Articles with example Python (programming language) code
- Category:Articles with example pseudocode
- Category:Articles with short description
- Category:CS1: long volume value
- Category:CS1 maint: multiple names: authors list
- Category:Computer algebra
- Category:Differential calculus
- Category:Short description is different from Wikidata
- Category:Webarchive template wayback links

## Table of Contents

- Difference from other differentiation methods
- Applications
- Forward and reverse accumulation
- Automatic differentiation using dual numbers
- Implementation
- See also
- Notes
- References
- Further reading
- External links

## Content

In mathematics and computer algebra, automatic differentiation (auto-differentiation, autodiff, or AD), also called algorithmic differentiation, computational differentiation, is a set of techniques to evaluate the partial derivative of a function specified by a computer program.
Automatic differentiation exploits the fact that every computer calculation, no matter how complicated, executes a sequence of elementary arithmetic operations (addition, subtraction, multiplication, division, etc.) and elementary functions (exp, log, sin, cos, etc.). By applying the chain rule repeatedly to these operations, partial derivatives of arbitrary order can be computed automatically, accurately to working precision, and using at most a small constant factor of more arithmetic operations than the original program.

Difference from other differentiation methods
Automatic differentiation is distinct from symbolic differentiation and numerical differentiation. 
Symbolic differentiation faces the difficulty of converting a computer program into a single mathematical expression and can lead to inefficient code. Numerical differentiation (the method of finite differences) can introduce round-off errors in the discretization process and cancellation. Both of these classical methods have problems with calculating higher derivatives, where complexity and errors increase. Finally, both of these classical methods are slow at computing partial derivatives of a function with respect to many inputs, as is needed for gradient-based optimization algorithms. Automatic differentiation solves all of these problems.

Applications
Automatic differentiation is particularly important in the field of machine learning. For example, it allows one to implement backpropagation in a neural network without a manually-computed derivative.

Forward and reverse accumulation
Chain rule of partial derivatives of composite functions
Fundamental to automatic differentiation is the decomposition of differentials provided by the chain rule of partial derivatives of composite functions. For the simple composition

  
    
      
        
          
            
              
                y
              
              
                
                =
                f
                (
                g
                (
                h
                (
                x
                )
                )
                )
                =
                f
                (
                g
                (
                h
                (
                
                  w
                  
                    0
                  
                
                )
                )
                )
                =
                f
                (
                g
                (
                
                  w
                  
                    1
                  
                
                )
                )
                =
                f
                (
                
                  w
                  
                    2
                  
                
                )
                =
                
                  w
                  
                    3
                  
                
              
            
            
              
                
                  w
                  
                    0
                  
                
              
              
                
                =
                x
              
            
            
              
                
                  w
                  
                    1
                  
                
              
              
                
                =
                h
                (
                
                  w
                  
                    0
                  
                
                )
              
            
            
              
                
                  w
                  
                    2
                  
                
              
              
                
                =
                g
                (
                
                  w
                  
                    1
                  
                
                )
              
            
            
              
                
                  w
                  
                    3
                  
                
              
              
                
                =
                f
                (
                
                  w
                  
                    2
                  
                
                )
                =
                y
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}y&=f(g(h(x)))=f(g(h(w_{0})))=f(g(w_{1}))=f(w_{2})=w_{3}\\w_{0}&=x\\w_{1}&=h(w_{0})\\w_{2}&=g(w_{1})\\w_{3}&=f(w_{2})=y\end{aligned}}}
  

the chain rule gives

  
    
      
        
          
            
              ∂
              y
            
            
              ∂
              x
            
          
        
        =
        
          
            
              ∂
              y
            
            
              ∂
              
                w
                
                  2
                
              
            
          
        
        
          
            
              ∂
              
                w
                
                  2
                
              
            
            
              ∂
              
                w
                
                  1
                
              
            
          
        
        
          
            
              ∂
              
                w
                
                  1
                
              
            
            
              ∂
              x
            
          
        
        =
        
          
            
              ∂
              f
              (
              
                w
                
                  2
                
              
              )
            
            
              ∂
              
                w
                
                  2
                
              
            
          
        
        
          
            
              ∂
              g
              (
              
                w
                
                  1
                
              
              )
            
            
              ∂
              
                w
                
                  1
                
              
            
          
        
        
          
            
              ∂
              h
              (
              
                w
                
                  0
                
              
              )
            
            
              ∂
              x
            
          
        
      
    
    {\displaystyle {\frac {\partial y}{\partial x}}={\frac {\partial y}{\partial w_{2}}}{\frac {\partial w_{2}}{\partial w_{1}}}{\frac {\partial w_{1}}{\partial x}}={\frac {\partial f(w_{2})}{\partial w_{2}}}{\frac {\partial g(w_{1})}{\partial w_{1}}}{\frac {\partial h(w_{0})}{\partial x}}}

Two types of automatic differentiation
Usually, two distinct modes of automatic differentiation are presented.

forward accumulation (also called bottom-up, forward mode, or tangent mode)
reverse accumulation (also called top-down, reverse mode, or adjoint mode)
Forward accumulation specifies that one traverses the chain rule from inside to outside (that is, first compute 
  
    
      
        ∂
        
          w
          
            1
          
        
        
          /
        
        ∂
        x
      
    
    {\displaystyle \partial w_{1}/\partial x}
  
 and then 
  
    
      
        ∂
        
          w
          
            2
          
        
        
          /
        
        ∂
        
          w
          
            1
          
        
      
    
    {\displaystyle \partial w_{2}/\partial w_{1}}
  
 and at last 
  
    
      
        ∂
        y
        
          /
        
        ∂
        
          w
          
            2
          
        
      
    
    {\displaystyle \partial y/\partial w_{2}}
  
), while reverse accumulation has the traversal from outside to inside (first compute 
  
    
      
        ∂
        y
        
          /
        
        ∂
        
          w
          
            2
          
        
      
    
    {\displaystyle \partial y/\partial w_{2}}
  
 and then 
  
    
      
        ∂
        
          w
          
            2
          
        
        
          /
        
        ∂
        
          w
          
            1
          
        
      
    
    {\displaystyle \partial w_{2}/\partial w_{1}}
  
 and at last 
  
    
      
        ∂
        
          w
          
            1
          
        
        
          /
        
        ∂
        x
      
    
    {\displaystyle \partial w_{1}/\partial x}
  
). More succinctly,

Forward accumulation computes the recursive relation: 
  
    
      
        
          
            
              ∂
              
                w
                
                  i
                
              
            
            
              ∂
              x
            
          
        
        =
        
          
            
              ∂
              
                w
                
                  i
                
              
            
            
              ∂
              
                w
                
                  i
                  −
                  1
                
              
            
          
        
        
          
            
              ∂
              
                w
                
                  i
                  −
                  1
                
              
            
            
              ∂
              x
            
          
        
      
    
    {\displaystyle {\frac {\partial w_{i}}{\partial x}}={\frac {\partial w_{i}}{\partial w_{i-1}}}{\frac {\partial w_{i-1}}{\partial x}}}
  
 with 
  
    
      
        
          w
          
            3
          
        
        =
        y
      
    
    {\displaystyle w_{3}=y}
  
, and,
Reverse accumulation computes the recursive relation: 
  
    
      
        
          
            
              ∂
              y
            
            
              ∂
              
                w
                
                  i
                
              
            
          
        
        =
        
          
            
              ∂
              y
            
            
              ∂
              
                w
                
                  i
                  +
                  1
                
              
            
          
        
        
          
            
              ∂
              
                w
                
                  i
                  +
                  1
                
              
            
            
              ∂
              
                w
                
                  i
                
              
            
          
        
      
    
    {\displaystyle {\frac {\partial y}{\partial w_{i}}}={\frac {\partial y}{\partial w_{i+1}}}{\frac {\partial w_{i+1}}{\partial w_{i}}}}
  
 with 
  
    
      
        
          w
          
            0
          
        
        =
        x
      
    
    {\displaystyle w_{0}=x}
  
.
The value of the partial derivative, called seed, is propagated forward or backward and is initially 
  
    
      
        
          
            
              ∂
              x
            
            
              ∂
              x
            
          
        
        =
        1
      
    
    {\displaystyle {\frac {\partial x}{\partial x}}=1}
  
 or 
  
    
      
        
          
            
              ∂
              y
            
            
              ∂
              y
            
          
        
        =
        1
      
    
    {\displaystyle {\frac {\partial y}{\partial y}}=1}
  
. Forward accumulation evaluates the function and calculates the derivative with respect to one independent variable in one pass. For each independent variable 
  
    
      
        
          x
          
            1
          
        
        ,
        
          x
          
            2
          
        
        ,
        …
        ,
        
          x
          
            n
          
        
      
    
    {\displaystyle x_{1},x_{2},\dots ,x_{n}}
  
 a separate pass is therefore necessary in which the derivative with respect to that independent variable is set to one (
  
    
      
        
          
            
              ∂
              
                x
                
                  1
                
              
            
            
              ∂
              
                x
                
                  1
                
              
            
          
        
        =
        1
      
    
    {\displaystyle {\frac {\partial x_{1}}{\partial x_{1}}}=1}
  
) and of all others to zero (
  
    
      
        
          
            
              ∂
              
                x
                
                  2
                
              
            
            
              ∂
              
                x
                
                  1
                
              
            
          
        
        =
        ⋯
        =
        
          
            
              ∂
              
                x
                
                  n
                
              
            
            
              ∂
              
                x
                
                  1
                
              
            
          
        
        =
        0
      
    
    {\displaystyle {\frac {\partial x_{2}}{\partial x_{1}}}=\dots ={\frac {\partial x_{n}}{\partial x_{1}}}=0}
  
). In contrast, reverse accumulation requires the evaluated partial functions for the partial derivatives. Reverse accumulation therefore evaluates the function first and calculates the derivatives with respect to all independent variables in an additional pass.
Which of these two types should be used depends on the sweep count. The computational complexity of one sweep is proportional to the complexity of the original code.

Forward accumulation is more efficient than reverse accumulation for functions f : Rn → Rm with n ≪ m as only n sweeps are necessary, compared to m sweeps for reverse accumulation.
Reverse accumulation is more efficient than forward accumulation for functions f : Rn → Rm with n ≫ m as only m sweeps are necessary, compared to n sweeps for forward accumulation.
Backpropagation of errors in multilayer perceptrons, a technique used in machine learning, is a special case of reverse accumulation.
Forward accumulation was introduced by R.E. Wengert in 1964. According to Andreas Griewank, reverse accumulation has been suggested since the late 1960s, but the inventor is unknown. Seppo Linnainmaa published reverse accumulation in 1976.

Forward accumulation
In forward accumulation AD, one first fixes the independent variable with respect to which differentiation is performed and computes the derivative of each sub-expression recursively. In a pen-and-paper calculation, this involves repeatedly substituting the derivative of the inner functions in the chain rule:

  
    
      
        
          
            
              
                
                  
                    
                      ∂
                      y
                    
                    
                      ∂
                      x
                    
                  
                
              
              
                
                =
                
                  
                    
                      ∂
                      y
                    
                    
                      ∂
                      
                        w
                        
                          n
                          −
                          1
                        
                      
                    
                  
                
                
                  
                    
                      ∂
                      
                        w
                        
                          n
                          −
                          1
                        
                      
                    
                    
                      ∂
                      x
                    
                  
                
              
            
            
              
              
                
                =
                
                  
                    
                      ∂
                      y
                    
                    
                      ∂
                      
                        w
                        
                          n
                          −
                          1
                        
                      
                    
                  
                
                
                  (
                  
                    
                      
                        
                          ∂
                          
                            w
                            
                              n
                              −
                              1
                            
                          
                        
                        
                          ∂
                          
                            w
                            
                              n
                              −
                              2
                            
                          
                        
                      
                    
                    
                      
                        
                          ∂
                          
                            w
                            
                              n
                              −
                              2
                            
                          
                        
                        
                          ∂
                          x
                        
                      
                    
                  
                  )
                
              
            
            
              
              
                
                =
                
                  
                    
                      ∂
                      y
                    
                    
                      ∂
                      
                        w
                        
                          n
                          −
                          1
                        
                      
                    
                  
                
                
                  (
                  
                    
                      
                        
                          ∂
                          
                            w
                            
                              n
                              −
                              1
                            
                          
                        
                        
                          ∂
                          
                            w
                            
                              n
                              −
                              2
                            
                          
                        
                      
                    
                    
                      (
                      
                        
                          
                            
                              ∂
                              
                                w
                                
                                  n
                                  −
                                  2
                                
                              
                            
                            
                              ∂
                              
                                w
                                
                                  n
                                  −
                                  3
                                
                              
                            
                          
                        
                        
                          
                            
                              ∂
                              
                                w
                                
                                  n
                                  −
                                  3
                                
                              
                            
                            
                              ∂
                              x
                            
                          
                        
                      
                      )
                    
                  
                  )
                
              
            
            
              
              
                
                =
                ⋯
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\frac {\partial y}{\partial x}}&={\frac {\partial y}{\partial w_{n-1}}}{\frac {\partial w_{n-1}}{\partial x}}\\[6pt]&={\frac {\partial y}{\partial w_{n-1}}}\left({\frac {\partial w_{n-1}}{\partial w_{n-2}}}{\frac {\partial w_{n-2}}{\partial x}}\right)\\[6pt]&={\frac {\partial y}{\partial w_{n-1}}}\left({\frac {\partial w_{n-1}}{\partial w_{n-2}}}\left({\frac {\partial w_{n-2}}{\partial w_{n-3}}}{\frac {\partial w_{n-3}}{\partial x}}\right)\right)\\[6pt]&=\cdots \end{aligned}}}
  

This can be generalized to multiple variables as a matrix product of Jacobians.
Compared to reverse accumulation, forward accumulation is natural and easy to implement as the flow of derivative information coincides with the order of evaluation. Each variable 
  
    
      
        
          w
          
            i
          
        
      
    
    {\displaystyle w_{i}}
  
 is augmented with its derivative 
  
    
      
        
          
            
              
                w
                ˙
              
            
          
          
            i
          
        
      
    
    {\displaystyle {\dot {w}}_{i}}
  
 (stored as a numerical value, not a symbolic expression),

  
    
      
        
          
            
              
                w
                ˙
              
            
          
          
            i
          
        
        =
        
          
            
              ∂
              
                w
                
                  i
                
              
            
            
              ∂
              x
            
          
        
      
    
    {\displaystyle {\dot {w}}_{i}={\frac {\partial w_{i}}{\partial x}}}
  

as denoted by the dot. The derivatives are then computed in sync with the evaluation steps and combined with other derivatives via the chain rule.
Using the chain rule, if 
  
    
      
        
          w
          
            i
          
        
      
    
    {\displaystyle w_{i}}
  
 has predecessors in the computational graph:

  
    
      
        
          
            
              
                w
                ˙
              
            
          
          
            i
          
        
        =
        
          ∑
          
            j
            ∈
            {
            
              predecessors of i
            
            }
          
        
        
          
            
              ∂
              
                w
                
                  i
                
              
            
            
              ∂
              
                w
                
                  j
                
              
            
          
        
        
          
            
              
                w
                ˙
              
            
          
          
            j
          
        
      
    
    {\displaystyle {\dot {w}}_{i}=\sum _{j\in \{{\text{predecessors of i}}\}}{\frac {\partial w_{i}}{\partial w_{j}}}{\dot {w}}_{j}}
  

As an example, consider the function:

  
    
      
        
          
            
              
                y
              
              
                
                =
                f
                (
                
                  x
                  
                    1
                  
                
                ,
                
                  x
                  
                    2
                  
                
                )
              
            
            
              
              
                
                =
                
                  x
                  
                    1
                  
                
                
                  x
                  
                    2
                  
                
                +
                sin
                ⁡
                
                  x
                  
                    1
                  
                
              
            
            
              
              
                
                =
                
                  w
                  
                    1
                  
                
                
                  w
                  
                    2
                  
                
                +
                sin
                ⁡
                
                  w
                  
                    1
                  
                
              
            
            
              
              
                
                =
                
                  w
                  
                    3
                  
                
                +
                
                  w
                  
                    4
                  
                
              
            
            
              
              
                
                =
                
                  w
                  
                    5
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}y&=f(x_{1},x_{2})\\&=x_{1}x_{2}+\sin x_{1}\\&=w_{1}w_{2}+\sin w_{1}\\&=w_{3}+w_{4}\\&=w_{5}\end{aligned}}}
  

For clarity, the individual sub-expressions have been labeled with the variables 
  
    
      
        
          w
          
            i
          
        
      
    
    {\displaystyle w_{i}}
  
.
The choice of the independent variable to which differentiation is performed affects the seed values ẇ1 and ẇ2. Given interest in the derivative of this function with respect to x1, the seed values should be set to:

  
    
      
        
          
            
              
                
                  
                    
                      
                        w
                        ˙
                      
                    
                  
                  
                    1
                  
                
                =
                
                  
                    
                      ∂
                      
                        w
                        
                          1
                        
                      
                    
                    
                      ∂
                      
                        x
                        
                          1
                        
                      
                    
                  
                
                =
                
                  
                    
                      ∂
                      
                        x
                        
                          1
                        
                      
                    
                    
                      ∂
                      
                        x
                        
                          1
                        
                      
                    
                  
                
                =
                1
              
            
            
              
                
                  
                    
                      
                        w
                        ˙
                      
                    
                  
                  
                    2
                  
                
                =
                
                  
                    
                      ∂
                      
                        w
                        
                          2
                        
                      
                    
                    
                      ∂
                      
                        x
                        
                          1
                        
                      
                    
                  
                
                =
                
                  
                    
                      ∂
                      
                        x
                        
                          2
                        
                      
                    
                    
                      ∂
                      
                        x
                        
                          1
                        
                      
                    
                  
                
                =
                0
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\dot {w}}_{1}={\frac {\partial w_{1}}{\partial x_{1}}}={\frac {\partial x_{1}}{\partial x_{1}}}=1\\{\dot {w}}_{2}={\frac {\partial w_{2}}{\partial x_{1}}}={\frac {\partial x_{2}}{\partial x_{1}}}=0\end{aligned}}}
  

With the seed values set, the values propagate using the chain rule as shown. Figure 2 shows a pictorial depiction of this process as a computational graph.

To compute the gradient of this example function, which requires not only 
  
    
      
        
          
            
              
                ∂
                y
              
              
                ∂
                
                  x
                  
                    1
                  
                
              
            
          
        
      
    
    {\displaystyle {\tfrac {\partial y}{\partial x_{1}}}}
  
 but also 
  
    
      
        
          
            
              
                ∂
                y
              
              
                ∂
                
                  x
                  
                    2
                  
                
              
            
          
        
      
    
    {\displaystyle {\tfrac {\partial y}{\partial x_{2}}}}
  
, an additional sweep is performed over the computational graph using the seed values 
  
    
      
        
          
            
              
                w
                ˙
              
            
          
          
            1
          
        
        =
        0
        ;
        
          
            
              
                w
                ˙
              
            
          
          
            2
          
        
        =
        1
      
    
    {\displaystyle {\dot {w}}_{1}=0;{\dot {w}}_{2}=1}
  
.

Implementation
Pseudocode
Forward accumulation calculates the function and the derivative (but only for one independent variable each) in one pass. The associated method call expects the expression Z to be derived with regard to a variable V. The method returns a pair of the evaluated function and its derivative. The method traverses the expression tree recursively until a variable is reached. If the derivative with respect to this variable is requested, its derivative is 1, 0 otherwise. Then the partial function as well as the partial derivative are evaluated.

C++
Reverse accumulation
In reverse accumulation AD, the dependent variable to be differentiated is fixed and the derivative is computed with respect to each sub-expression recursively. In a pen-and-paper calculation, the derivative of the outer functions is repeatedly substituted in the chain rule:

  
    
      
        
          
            
              
                
                  
                    
                      ∂
                      y
                    
                    
                      ∂
                      x
                    
                  
                
              
              
                
                =
                
                  
                    
                      ∂
                      y
                    
                    
                      ∂
                      
                        w
                        
                          1
                        
                      
                    
                  
                
                
                  
                    
                      ∂
                      
                        w
                        
                          1
                        
                      
                    
                    
                      ∂
                      x
                    
                  
                
              
            
            
              
              
                
                =
                
                  (
                  
                    
                      
                        
                          ∂
                          y
                        
                        
                          ∂
                          
                            w
                            
                              2
                            
                          
                        
                      
                    
                    
                      
                        
                          ∂
                          
                            w
                            
                              2
                            
                          
                        
                        
                          ∂
                          
                            w
                            
                              1
                            
                          
                        
                      
                    
                  
                  )
                
                
                  
                    
                      ∂
                      
                        w
                        
                          1
                        
                      
                    
                    
                      ∂
                      x
                    
                  
                
              
            
            
              
              
                
                =
                
                  (
                  
                    
                      (
                      
                        
                          
                            
                              ∂
                              y
                            
                            
                              ∂
                              
                                w
                                
                                  3
                                
                              
                            
                          
                        
                        
                          
                            
                              ∂
                              
                                w
                                
                                  3
                                
                              
                            
                            
                              ∂
                              
                                w
                                
                                  2
                                
                              
                            
                          
                        
                      
                      )
                    
                    
                      
                        
                          ∂
                          
                            w
                            
                              2
                            
                          
                        
                        
                          ∂
                          
                            w
                            
                              1
                            
                          
                        
                      
                    
                  
                  )
                
                
                  
                    
                      ∂
                      
                        w
                        
                          1
                        
                      
                    
                    
                      ∂
                      x
                    
                  
                
              
            
            
              
              
                
                =
                ⋯
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\frac {\partial y}{\partial x}}&={\frac {\partial y}{\partial w_{1}}}{\frac {\partial w_{1}}{\partial x}}\\&=\left({\frac {\partial y}{\partial w_{2}}}{\frac {\partial w_{2}}{\partial w_{1}}}\right){\frac {\partial w_{1}}{\partial x}}\\&=\left(\left({\frac {\partial y}{\partial w_{3}}}{\frac {\partial w_{3}}{\partial w_{2}}}\right){\frac {\partial w_{2}}{\partial w_{1}}}\right){\frac {\partial w_{1}}{\partial x}}\\&=\cdots \end{aligned}}}
  

In reverse accumulation, the quantity of interest is the adjoint, denoted with a bar 
  
    
      
        
          
            
              
                w
                ¯
              
            
          
          
            i
          
        
      
    
    {\displaystyle {\bar {w}}_{i}}
  
; it is a derivative of a chosen dependent variable with respect to a subexpression 
  
    
      
        
          w
          
            i
          
        
      
    
    {\displaystyle w_{i}}
  
:

  
    
      
        
          
            
              
                w
                ¯
              
            
          
          
            i
          
        
        =
        
          
            
              ∂
              y
            
            
              ∂
              
                w
                
                  i
                
              
            
          
        
      
    
    {\displaystyle {\bar {w}}_{i}={\frac {\partial y}{\partial w_{i}}}}
  

Using the chain rule, if 
  
    
      
        
          w
          
            i
          
        
      
    
    {\displaystyle w_{i}}
  
 has successors in the computational graph:

  
    
      
        
          
            
              
                w
                ¯
              
            
          
          
            i
          
        
        =
        
          ∑
          
            j
            ∈
            {
            
              successors of i
            
            }
          
        
        
          
            
              
                w
                ¯
              
            
          
          
            j
          
        
        
          
            
              ∂
              
                w
                
                  j
                
              
            
            
              ∂
              
                w
                
                  i
                
              
            
          
        
      
    
    {\displaystyle {\bar {w}}_{i}=\sum _{j\in \{{\text{successors of i}}\}}{\bar {w}}_{j}{\frac {\partial w_{j}}{\partial w_{i}}}}
  

Reverse accumulation traverses the chain rule from outside to inside, or in the case of the computational graph in Figure 3, from top to bottom. The example function is scalar-valued, and thus there is only one seed for the derivative computation, and only one sweep of the computational graph is needed to calculate the (two-component) gradient. This is only half the work when compared to forward accumulation, but reverse accumulation requires the storage of the intermediate variables wi as well as the instructions that produced them in a data structure known as a "tape" or a Wengert list (however, Wengert published forward accumulation, not reverse accumulation), which may consume significant memory if the computational graph is large. This can be mitigated to some extent by storing only a subset of the intermediate variables and then reconstructing the necessary work variables by repeating the evaluations, a technique known as rematerialization. Checkpointing is also used to save intermediary states.

The operations to compute the derivative using reverse accumulation are shown in the table below (note the reversed order):

The data flow graph of a computation can be manipulated to calculate the gradient of its original calculation. This is done by adding an adjoint node for each primal node, connected by adjoint edges which parallel the primal edges but flow in the opposite direction. The nodes in the adjoint graph represent multiplication by the derivatives of the functions calculated by the nodes in the primal. For instance, addition in the primal causes fanout in the adjoint; fanout in the primal causes addition in the adjoint; a unary function y = f(x) in the primal causes x̄ = ȳ f′(x) in the adjoint; etc.

Implementation
Pseudo code
Reverse accumulation requires two passes: In the forward pass, the function is evaluated first and the partial results are cached. In the reverse pass, the partial derivatives are calculated and the previously derived value is backpropagated. The corresponding method call expects the expression Z to be derived and seed with the derived value of the parent expression. For the top expression, Z derived with regard to Z, this is 1. The method traverses the expression tree recursively until a variable is reached and adds the current seed value to the derivative expression.

C++
Beyond forward and reverse accumulation
Forward and reverse accumulation are just two (extreme) ways of traversing the chain rule. The problem of computing a full Jacobian of f : Rn → Rm with a minimum number of arithmetic operations is known as the optimal Jacobian accumulation (OJA) problem, which is NP-complete. Central to this proof is the idea that algebraic dependencies may exist between the local partials that label the edges of the graph. In particular, two or more edge labels may be recognized as equal. The complexity of the problem is still open if it is assumed that all edge labels are unique and algebraically independent.

Automatic differentiation using dual numbers
Forward mode automatic differentiation is accomplished by augmenting the algebra of real numbers and obtaining a new arithmetic. An additional component is added to every number to represent the derivative of a function at the number, and all arithmetic operators are extended for the augmented algebra. The augmented algebra is the algebra of dual numbers.
Replace every number 
  
    
      
        
        x
      
    
    {\displaystyle \,x}
  
 with the number 
  
    
      
        x
        +
        
          x
          ′
        
        ε
      
    
    {\displaystyle x+x'\varepsilon }
  
, where 
  
    
      
        
          x
          ′
        
      
    
    {\displaystyle x'}
  
 is a real number, but 
  
    
      
        ε
      
    
    {\displaystyle \varepsilon }
  
 is an abstract number with the property 
  
    
      
        
          ε
          
            2
          
        
        =
        0
      
    
    {\displaystyle \varepsilon ^{2}=0}
  
 (an infinitesimal; see Smooth infinitesimal analysis). Using only this, regular arithmetic gives

  
    
      
        
          
            
              
                (
                x
                +
                
                  x
                  ′
                
                ε
                )
                +
                (
                y
                +
                
                  y
                  ′
                
                ε
                )
              
              
                
                =
                x
                +
                y
                +
                (
                
                  x
                  ′
                
                +
                
                  y
                  ′
                
                )
                ε
              
            
            
              
                (
                x
                +
                
                  x
                  ′
                
                ε
                )
                −
                (
                y
                +
                
                  y
                  ′
                
                ε
                )
              
              
                
                =
                x
                −
                y
                +
                (
                
                  x
                  ′
                
                −
                
                  y
                  ′
                
                )
                ε
              
            
            
              
                (
                x
                +
                
                  x
                  ′
                
                ε
                )
                ⋅
                (
                y
                +
                
                  y
                  ′
                
                ε
                )
              
              
                
                =
                x
                y
                +
                x
                
                  y
                  ′
                
                ε
                +
                y
                
                  x
                  ′
                
                ε
                +
                
                  x
                  ′
                
                
                  y
                  ′
                
                
                  ε
                  
                    2
                  
                
                =
                x
                y
                +
                (
                x
                
                  y
                  ′
                
                +
                y
                
                  x
                  ′
                
                )
                ε
              
            
            
              
                (
                x
                +
                
                  x
                  ′
                
                ε
                )
                
                  /
                
                (
                y
                +
                
                  y
                  ′
                
                ε
                )
              
              
                
                =
                (
                x
                
                  /
                
                y
                +
                
                  x
                  ′
                
                ε
                
                  /
                
                y
                )
                
                  /
                
                (
                1
                +
                
                  y
                  ′
                
                ε
                
                  /
                
                y
                )
                =
                (
                x
                
                  /
                
                y
                +
                
                  x
                  ′
                
                ε
                
                  /
                
                y
                )
                ⋅
                (
                1
                −
                
                  y
                  ′
                
                ε
                
                  /
                
                y
                )
                =
                x
                
                  /
                
                y
                +
                (
                
                  x
                  ′
                
                
                  /
                
                y
                −
                x
                
                  y
                  ′
                
                
                  /
                
                
                  y
                  
                    2
                  
                
                )
                ε
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}(x+x'\varepsilon )+(y+y'\varepsilon )&=x+y+(x'+y')\varepsilon \\(x+x'\varepsilon )-(y+y'\varepsilon )&=x-y+(x'-y')\varepsilon \\(x+x'\varepsilon )\cdot (y+y'\varepsilon )&=xy+xy'\varepsilon +yx'\varepsilon +x'y'\varepsilon ^{2}=xy+(xy'+yx')\varepsilon \\(x+x'\varepsilon )/(y+y'\varepsilon )&=(x/y+x'\varepsilon /y)/(1+y'\varepsilon /y)=(x/y+x'\varepsilon /y)\cdot (1-y'\varepsilon /y)=x/y+(x'/y-xy'/y^{2})\varepsilon \end{aligned}}}
  

using 
  
    
      
        (
        1
        +
        
          y
          ′
        
        ε
        
          /
        
        y
        )
        ⋅
        (
        1
        −
        
          y
          ′
        
        ε
        
          /
        
        y
        )
        =
        1
      
    
    {\displaystyle (1+y'\varepsilon /y)\cdot (1-y'\varepsilon /y)=1}
  
.
Now, polynomials can be calculated in this augmented arithmetic. If 
  
    
      
        P
        (
        x
        )
        =
        
          p
          
            0
          
        
        +
        
          p
          
            1
          
        
        x
        +
        
          p
          
            2
          
        
        
          x
          
            2
          
        
        +
        ⋯
        +
        
          p
          
            n
          
        
        
          x
          
            n
          
        
      
    
    {\displaystyle P(x)=p_{0}+p_{1}x+p_{2}x^{2}+\cdots +p_{n}x^{n}}
  
, then

  
    
      
        
          
            
              
                P
                (
                x
                +
                
                  x
                  ′
                
                ε
                )
              
              
                
                =
                
                  p
                  
                    0
                  
                
                +
                
                  p
                  
                    1
                  
                
                (
                x
                +
                
                  x
                  ′
                
                ε
                )
                +
                ⋯
                +
                
                  p
                  
                    n
                  
                
                (
                x
                +
                
                  x
                  ′
                
                ε
                
                  )
                  
                    n
                  
                
              
            
            
              
              
                
                =
                
                  p
                  
                    0
                  
                
                +
                
                  p
                  
                    1
                  
                
                x
                +
                ⋯
                +
                
                  p
                  
                    n
                  
                
                
                  x
                  
                    n
                  
                
                +
                
                  p
                  
                    1
                  
                
                
                  x
                  ′
                
                ε
                +
                2
                
                  p
                  
                    2
                  
                
                x
                
                  x
                  ′
                
                ε
                +
                ⋯
                +
                n
                
                  p
                  
                    n
                  
                
                
                  x
                  
                    n
                    −
                    1
                  
                
                
                  x
                  ′
                
                ε
              
            
            
              
              
                
                =
                P
                (
                x
                )
                +
                
                  P
                  
                    (
                    1
                    )
                  
                
                (
                x
                )
                
                  x
                  ′
                
                ε
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}P(x+x'\varepsilon )&=p_{0}+p_{1}(x+x'\varepsilon )+\cdots +p_{n}(x+x'\varepsilon )^{n}\\&=p_{0}+p_{1}x+\cdots +p_{n}x^{n}+p_{1}x'\varepsilon +2p_{2}xx'\varepsilon +\cdots +np_{n}x^{n-1}x'\varepsilon \\&=P(x)+P^{(1)}(x)x'\varepsilon \end{aligned}}}
  

where 
  
    
      
        
          P
          
            (
            1
            )
          
        
      
    
    {\displaystyle P^{(1)}}
  
 denotes the derivative of 
  
    
      
        P
      
    
    {\displaystyle P}
  
 with respect to its first argument, and 
  
    
      
        
          x
          ′
        
      
    
    {\displaystyle x'}
  
, called a seed, can be chosen arbitrarily.
The new arithmetic consists of ordered pairs, elements written 
  
    
      
        ⟨
        x
        ,
        
          x
          ′
        
        ⟩
      
    
    {\displaystyle \langle x,x'\rangle }
  
, with ordinary arithmetics on the first component, and first order differentiation arithmetic on the second component, as described above. Extending the above results on polynomials to analytic functions gives a list of the basic arithmetic and some standard functions for the new arithmetic:

  
    
      
        
          
            
              
                
                  ⟨
                  
                    u
                    ,
                    
                      u
                      ′
                    
                  
                  ⟩
                
                +
                
                  ⟨
                  
                    v
                    ,
                    
                      v
                      ′
                    
                  
                  ⟩
                
              
              
                
                =
                
                  ⟨
                  
                    u
                    +
                    v
                    ,
                    
                      u
                      ′
                    
                    +
                    
                      v
                      ′
                    
                  
                  ⟩
                
              
            
            
              
                
                  ⟨
                  
                    u
                    ,
                    
                      u
                      ′
                    
                  
                  ⟩
                
                −
                
                  ⟨
                  
                    v
                    ,
                    
                      v
                      ′
                    
                  
                  ⟩
                
              
              
                
                =
                
                  ⟨
                  
                    u
                    −
                    v
                    ,
                    
                      u
                      ′
                    
                    −
                    
                      v
                      ′
                    
                  
                  ⟩
                
              
            
            
              
                
                  ⟨
                  
                    u
                    ,
                    
                      u
                      ′
                    
                  
                  ⟩
                
                ∗
                
                  ⟨
                  
                    v
                    ,
                    
                      v
                      ′
                    
                  
                  ⟩
                
              
              
                
                =
                
                  ⟨
                  
                    u
                    v
                    ,
                    
                      u
                      ′
                    
                    v
                    +
                    u
                    
                      v
                      ′
                    
                  
                  ⟩
                
              
            
            
              
                
                  ⟨
                  
                    u
                    ,
                    
                      u
                      ′
                    
                  
                  ⟩
                
                
                  /
                
                
                  ⟨
                  
                    v
                    ,
                    
                      v
                      ′
                    
                  
                  ⟩
                
              
              
                
                =
                
                  ⟨
                  
                    
                      
                        u
                        v
                      
                    
                    ,
                    
                      
                        
                          
                            u
                            ′
                          
                          v
                          −
                          u
                          
                            v
                            ′
                          
                        
                        
                          v
                          
                            2
                          
                        
                      
                    
                  
                  ⟩
                
                
                (
                v
                ≠
                0
                )
              
            
            
              
                sin
                ⁡
                
                  ⟨
                  
                    u
                    ,
                    
                      u
                      ′
                    
                  
                  ⟩
                
              
              
                
                =
                
                  ⟨
                  
                    sin
                    ⁡
                    (
                    u
                    )
                    ,
                    
                      u
                      ′
                    
                    cos
                    ⁡
                    (
                    u
                    )
                  
                  ⟩
                
              
            
            
              
                cos
                ⁡
                
                  ⟨
                  
                    u
                    ,
                    
                      u
                      ′
                    
                  
                  ⟩
                
              
              
                
                =
                
                  ⟨
                  
                    cos
                    ⁡
                    (
                    u
                    )
                    ,
                    −
                    
                      u
                      ′
                    
                    sin
                    ⁡
                    (
                    u
                    )
                  
                  ⟩
                
              
            
            
              
                exp
                ⁡
                
                  ⟨
                  
                    u
                    ,
                    
                      u
                      ′
                    
                  
                  ⟩
                
              
              
                
                =
                
                  ⟨
                  
                    exp
                    ⁡
                    u
                    ,
                    
                      u
                      ′
                    
                    exp
                    ⁡
                    u
                  
                  ⟩
                
              
            
            
              
                log
                ⁡
                
                  ⟨
                  
                    u
                    ,
                    
                      u
                      ′
                    
                  
                  ⟩
                
              
              
                
                =
                
                  ⟨
                  
                    log
                    ⁡
                    (
                    u
                    )
                    ,
                    
                      u
                      ′
                    
                    
                      /
                    
                    u
                  
                  ⟩
                
                
                (
                u
                >
                0
                )
              
            
            
              
                
                  
                    ⟨
                    
                      u
                      ,
                      
                        u
                        ′
                      
                    
                    ⟩
                  
                  
                    k
                  
                
              
              
                
                =
                
                  ⟨
                  
                    
                      u
                      
                        k
                      
                    
                    ,
                    
                      u
                      ′
                    
                    k
                    
                      u
                      
                        k
                        −
                        1
                      
                    
                  
                  ⟩
                
                
                (
                u
                ≠
                0
                )
              
            
            
              
                
                  |
                  
                    ⟨
                    
                      u
                      ,
                      
                        u
                        ′
                      
                    
                    ⟩
                  
                  |
                
              
              
                
                =
                
                  ⟨
                  
                    
                      |
                      u
                      |
                    
                    ,
                    
                      u
                      ′
                    
                    sign
                    ⁡
                    u
                  
                  ⟩
                
                
                (
                u
                ≠
                0
                )
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\left\langle u,u'\right\rangle +\left\langle v,v'\right\rangle &=\left\langle u+v,u'+v'\right\rangle \\\left\langle u,u'\right\rangle -\left\langle v,v'\right\rangle &=\left\langle u-v,u'-v'\right\rangle \\\left\langle u,u'\right\rangle *\left\langle v,v'\right\rangle &=\left\langle uv,u'v+uv'\right\rangle \\\left\langle u,u'\right\rangle /\left\langle v,v'\right\rangle &=\left\langle {\frac {u}{v}},{\frac {u'v-uv'}{v^{2}}}\right\rangle \quad (v\neq 0)\\\sin \left\langle u,u'\right\rangle &=\left\langle \sin(u),u'\cos(u)\right\rangle \\\cos \left\langle u,u'\right\rangle &=\left\langle \cos(u),-u'\sin(u)\right\rangle \\\exp \left\langle u,u'\right\rangle &=\left\langle \exp u,u'\exp u\right\rangle \\\log \left\langle u,u'\right\rangle &=\left\langle \log(u),u'/u\right\rangle \quad (u>0)\\\left\langle u,u'\right\rangle ^{k}&=\left\langle u^{k},u'ku^{k-1}\right\rangle \quad (u\neq 0)\\\left|\left\langle u,u'\right\rangle \right|&=\left\langle \left|u\right|,u'\operatorname {sign} u\right\rangle \quad (u\neq 0)\end{aligned}}}
  

and in general for the primitive function 
  
    
      
        g
      
    
    {\displaystyle g}
  
,

  
    
      
        g
        (
        ⟨
        u
        ,
        
          u
          ′
        
        ⟩
        ,
        ⟨
        v
        ,
        
          v
          ′
        
        ⟩
        )
        =
        ⟨
        g
        (
        u
        ,
        v
        )
        ,
        
          g
          
            u
          
        
        (
        u
        ,
        v
        )
        
          u
          ′
        
        +
        
          g
          
            v
          
        
        (
        u
        ,
        v
        )
        
          v
          ′
        
        ⟩
      
    
    {\displaystyle g(\langle u,u'\rangle ,\langle v,v'\rangle )=\langle g(u,v),g_{u}(u,v)u'+g_{v}(u,v)v'\rangle }
  

where 
  
    
      
        
          g
          
            u
          
        
      
    
    {\displaystyle g_{u}}
  
 and 
  
    
      
        
          g
          
            v
          
        
      
    
    {\displaystyle g_{v}}
  
 are the derivatives of 
  
    
      
        g
      
    
    {\displaystyle g}
  
 with respect to its first and second arguments, respectively.
When a binary basic arithmetic operation is applied to mixed arguments—the pair 
  
    
      
        ⟨
        u
        ,
        
          u
          ′
        
        ⟩
      
    
    {\displaystyle \langle u,u'\rangle }
  
 and the real number 
  
    
      
        c
      
    
    {\displaystyle c}
  
—the real number is first lifted to 
  
    
      
        ⟨
        c
        ,
        0
        ⟩
      
    
    {\displaystyle \langle c,0\rangle }
  
. The derivative of a function 
  
    
      
        f
        :
        
          R
        
        →
        
          R
        
      
    
    {\displaystyle f:\mathbb {R} \to \mathbb {R} }
  
 at the point 
  
    
      
        
          x
          
            0
          
        
      
    
    {\displaystyle x_{0}}
  
 is now found by calculating 
  
    
      
        f
        (
        ⟨
        
          x
          
            0
          
        
        ,
        1
        ⟩
        )
      
    
    {\displaystyle f(\langle x_{0},1\rangle )}
  
 using the above arithmetic, which gives 
  
    
      
        ⟨
        f
        (
        
          x
          
            0
          
        
        )
        ,
        
          f
          ′
        
        (
        
          x
          
            0
          
        
        )
        ⟩
      
    
    {\displaystyle \langle f(x_{0}),f'(x_{0})\rangle }
  
 as the result.

Implementation
An example implementation based on the dual number approach follows.

Pseudo code
Dual plus(Dual A, Dual B) {
  return {
    realPartOf(A) + realPartOf(B),
    infinitesimalPartOf(A) + infinitesimalPartOf(B)
  };
}
Dual minus(Dual A, Dual B) {
  return {
    realPartOf(A) - realPartOf(B),
    infinitesimalPartOf(A) - infinitesimalPartOf(B)
  };
}
Dual multiply(Dual A, Dual B) {
  return {
    realPartOf(A) * realPartOf(B),
    realPartOf(B) * infinitesimalPartOf(A) + realPartOf(A) * infinitesimalPartOf(B)
  };
}
X = {x, 0};
Y = {y, 0};
Epsilon = {0, 1};
xPartial = infinitesimalPartOf(f(X + Epsilon, Y));
yPartial = infinitesimalPartOf(f(X, Y + Epsilon));

C++
Vector arguments and functions
Multivariate functions can be handled with the same efficiency and mechanisms as univariate functions by adopting a directional derivative operator. That is, if it is sufficient to compute 
  
    
      
        
          y
          ′
        
        =
        ∇
        f
        (
        x
        )
        ⋅
        
          x
          ′
        
      
    
    {\displaystyle y'=\nabla f(x)\cdot x'}
  
, the directional derivative 
  
    
      
        
          y
          ′
        
        ∈
        
          
            R
          
          
            m
          
        
      
    
    {\displaystyle y'\in \mathbb {R} ^{m}}
  
 of 
  
    
      
        f
        :
        
          
            R
          
          
            n
          
        
        →
        
          
            R
          
          
            m
          
        
      
    
    {\displaystyle f:\mathbb {R} ^{n}\to \mathbb {R} ^{m}}
  
 at 
  
    
      
        x
        ∈
        
          
            R
          
          
            n
          
        
      
    
    {\displaystyle x\in \mathbb {R} ^{n}}
  
 in the direction 
  
    
      
        
          x
          ′
        
        ∈
        
          
            R
          
          
            n
          
        
      
    
    {\displaystyle x'\in \mathbb {R} ^{n}}
  
 may be calculated as 
  
    
      
        (
        ⟨
        
          y
          
            1
          
        
        ,
        
          y
          
            1
          
          ′
        
        ⟩
        ,
        …
        ,
        ⟨
        
          y
          
            m
          
        
        ,
        
          y
          
            m
          
          ′
        
        ⟩
        )
        =
        f
        (
        ⟨
        
          x
          
            1
          
        
        ,
        
          x
          
            1
          
          ′
        
        ⟩
        ,
        …
        ,
        ⟨
        
          x
          
            n
          
        
        ,
        
          x
          
            n
          
          ′
        
        ⟩
        )
      
    
    {\displaystyle (\langle y_{1},y'_{1}\rangle ,\ldots ,\langle y_{m},y'_{m}\rangle )=f(\langle x_{1},x'_{1}\rangle ,\ldots ,\langle x_{n},x'_{n}\rangle )}
  
 using the same arithmetic as above. If all the elements of 
  
    
      
        ∇
        f
      
    
    {\displaystyle \nabla f}
  
 are desired, then 
  
    
      
        n
      
    
    {\displaystyle n}
  
 function evaluations are required. Note that in many optimization applications, the directional derivative is indeed sufficient.

High order and many variables
The above arithmetic can be generalized to calculate second order and higher derivatives of multivariate functions. However, the arithmetic rules quickly grow complicated: complexity is quadratic in the highest derivative degree. Instead, truncated Taylor polynomial algebra can be used. The resulting arithmetic, defined on generalized dual numbers, allows efficient computation using functions as if they were a data type. Once the Taylor polynomial of a function is known, the derivatives are easily extracted.

Implementation
Forward-mode AD is implemented by a nonstandard interpretation of the program in which real numbers are replaced by dual numbers, constants are lifted to dual numbers with a zero epsilon coefficient, and the numeric primitives are lifted to operate on dual numbers. This nonstandard interpretation is generally implemented using one of two strategies: source code transformation or operator overloading.

Source code transformation (SCT)
The source code for a function is replaced by an automatically generated source code that includes statements for calculating the derivatives interleaved with the original instructions.
Source code transformation can be implemented for all programming languages, and it is also easier for the compiler to do compile time optimizations. However, the implementation of the AD tool itself is more difficult and the build system is more complex.

Operator overloading (OO)
Operator overloading is a possibility for source code written in a language supporting it. Objects for real numbers and elementary mathematical operations must be overloaded to cater for the augmented arithmetic depicted above. This requires no change in the form or sequence of operations in the original source code for the function to be differentiated, but often requires changes in basic data types for numbers and vectors to support overloading and often also involves the insertion of special flagging operations. Due to the inherent operator overloading overhead on each loop, this approach usually demonstrates weaker speed performance.

Operator overloading and source code transformation
Overloaded Operators can be used to extract the valuation graph, followed by automatic generation of the AD-version of the primal function at run-time. Unlike the classic OO AAD, such AD-function does not change from one iteration to the next one. Hence there is any OO or tape interpretation run-time overhead per Xi sample.
With the AD-function being generated at runtime, it can be optimised to take into account the current state of the program and precompute certain values. In addition, it can be generated in a way to consistently utilize native CPU vectorization to process 4(8)-double chunks of user data (AVX2\AVX512 speed up x4-x8). With multithreading added into account, such approach can lead to a final acceleration of order 8 × #Cores compared to the traditional AAD tools. A reference implementation is available on GitHub.

See also
Differentiable programming

Notes
References
Further reading
Rall, Louis B. (1981). Automatic Differentiation: Techniques and Applications. Lecture Notes in Computer Science. Vol. 120. Springer. ISBN 978-3-540-10861-0.
Griewank, Andreas; Walther, Andrea (2008). Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation. Other Titles in Applied Mathematics. Vol. 105 (2nd ed.). SIAM. doi:10.1137/1.9780898717761. ISBN 978-0-89871-659-7.
Neidinger, Richard (2010). "Introduction to Automatic Differentiation and MATLAB Object-Oriented Programming" (PDF). SIAM Review. 52 (3): 545–563. CiteSeerX 10.1.1.362.6580. doi:10.1137/080743627. S2CID 17134969. Retrieved 2013-03-15.
Naumann, Uwe (2012). The Art of Differentiating Computer Programs. Software-Environments-tools. SIAM. ISBN 978-1-611972-06-1.
Henrard, Marc (2017). Algorithmic Differentiation in Finance Explained. Financial Engineering Explained. Palgrave Macmillan. ISBN 978-3-319-53978-2.

External links
www.autodiff.org, An "entry site to everything you want to know about automatic differentiation"
Automatic Differentiation of Parallel OpenMP Programs
Automatic Differentiation, C++ Templates and Photogrammetry
Automatic Differentiation, Operator Overloading Approach
Compute analytic derivatives of any Fortran77, Fortran95, or C program through a web-based interface Automatic Differentiation of Fortran programs
Description and example code for forward Automatic Differentiation in Scala Archived 2016-08-03 at the Wayback Machine
finmath-lib stochastic automatic differentiation, Automatic differentiation for random variables (Java implementation of the stochastic automatic differentiation).
Adjoint Algorithmic Differentiation: Calibration and Implicit Function Theorem
C++ Template-based automatic differentiation article and implementation
Tangent Source-to-Source Debuggable Derivatives
Exact First- and Second-Order Greeks by Algorithmic Differentiation
Adjoint Algorithmic Differentiation of a GPU Accelerated Application
Adjoint Methods in Computational Finance Software Tool Support for Algorithmic Differentiationop
More than a Thousand Fold Speed Up for xVA Pricing Calculations with Intel Xeon Scalable Processors
Sparse truncated Taylor series implementation with VBIC95 example for higher order derivatives

## Related Articles

### Internal Links

- [Concrete number](https://en.wikipedia.org/wiki/Concrete_number)
- [Alfons Kemper](https://en.wikipedia.org/wiki/Alfons_Kemper)
- [Algebra over a field](https://en.wikipedia.org/wiki/Algebra_over_a_field)
- [Analytic function](https://en.wikipedia.org/wiki/Analytic_function)
- [Andrea Walther](https://en.wikipedia.org/wiki/Andrea_Walther)
- [Arithmetic](https://en.wikipedia.org/wiki/Arithmetic)
- [Backpropagation](https://en.wikipedia.org/wiki/Backpropagation)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Chain rule](https://en.wikipedia.org/wiki/Chain_rule)
- [Checkpointing scheme](https://en.wikipedia.org/wiki/Checkpointing_scheme)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Computational complexity theory](https://en.wikipedia.org/wiki/Computational_complexity_theory)
- [Computational learning theory](https://en.wikipedia.org/wiki/Computational_learning_theory)
- [Computer algebra](https://en.wikipedia.org/wiki/Computer_algebra)
- [Sine and cosine](https://en.wikipedia.org/wiki/Sine_and_cosine)
- [Linear form](https://en.wikipedia.org/wiki/Linear_form)
- [Differentiable function](https://en.wikipedia.org/wiki/Differentiable_function)
- [Differentiable programming](https://en.wikipedia.org/wiki/Differentiable_programming)
- [Discretization](https://en.wikipedia.org/wiki/Discretization)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Dual number](https://en.wikipedia.org/wiki/Dual_number)
- [Exponential function](https://en.wikipedia.org/wiki/Exponential_function)
- [Expression (mathematics)](https://en.wikipedia.org/wiki/Expression_(mathematics))
- [Flux (machine-learning framework)](https://en.wikipedia.org/wiki/Flux_(machine-learning_framework))
- [Function composition](https://en.wikipedia.org/wiki/Function_composition)
- [Google JAX](https://en.wikipedia.org/wiki/Google_JAX)
- [Gradient](https://en.wikipedia.org/wiki/Gradient)
- [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent)
- [Graphcore](https://en.wikipedia.org/wiki/Graphcore)
- [Handle System](https://en.wikipedia.org/wiki/Handle_System)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Inductive bias](https://en.wikipedia.org/wiki/Inductive_bias)
- [Infinitesimal](https://en.wikipedia.org/wiki/Infinitesimal)
- [Information geometry](https://en.wikipedia.org/wiki/Information_geometry)
- [Jacobian matrix and determinant](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant)
- [Keras](https://en.wikipedia.org/wiki/Keras)
- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
- [Expression (mathematics)](https://en.wikipedia.org/wiki/Expression_(mathematics))
- [Mathematics](https://en.wikipedia.org/wiki/Mathematics)
- [Memristor](https://en.wikipedia.org/wiki/Memristor)
- [MindSpore](https://en.wikipedia.org/wiki/MindSpore)
- [NP-completeness](https://en.wikipedia.org/wiki/NP-completeness)
- [Natural logarithm](https://en.wikipedia.org/wiki/Natural_logarithm)
- [Neuromorphic computing](https://en.wikipedia.org/wiki/Neuromorphic_computing)
- [Numerical differentiation](https://en.wikipedia.org/wiki/Numerical_differentiation)
- [Operator overloading](https://en.wikipedia.org/wiki/Operator_overloading)
- [Mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization)
- [Ordered pair](https://en.wikipedia.org/wiki/Ordered_pair)
- [Palgrave Macmillan](https://en.wikipedia.org/wiki/Palgrave_Macmillan)
- [Partial derivative](https://en.wikipedia.org/wiki/Partial_derivative)
- [Pattern recognition](https://en.wikipedia.org/wiki/Pattern_recognition)
- [Polynomial](https://en.wikipedia.org/wiki/Polynomial)
- [PyTorch](https://en.wikipedia.org/wiki/PyTorch)
- [Real number](https://en.wikipedia.org/wiki/Real_number)
- [Rematerialization](https://en.wikipedia.org/wiki/Rematerialization)
- [Ricci calculus](https://en.wikipedia.org/wiki/Ricci_calculus)
- [Round-off error](https://en.wikipedia.org/wiki/Round-off_error)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Scikit-learn](https://en.wikipedia.org/wiki/Scikit-learn)
- [Seppo Linnainmaa](https://en.wikipedia.org/wiki/Seppo_Linnainmaa)
- [Sine and cosine](https://en.wikipedia.org/wiki/Sine_and_cosine)
- [Smooth infinitesimal analysis](https://en.wikipedia.org/wiki/Smooth_infinitesimal_analysis)
- [Society for Industrial and Applied Mathematics](https://en.wikipedia.org/wiki/Society_for_Industrial_and_Applied_Mathematics)
- [Program transformation](https://en.wikipedia.org/wiki/Program_transformation)
- [Space–time tradeoff](https://en.wikipedia.org/wiki/Space%E2%80%93time_tradeoff)
- [SpiNNaker](https://en.wikipedia.org/wiki/SpiNNaker)
- [Springer Science+Business Media](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Statistical manifold](https://en.wikipedia.org/wiki/Statistical_manifold)
- [Computer algebra](https://en.wikipedia.org/wiki/Computer_algebra)
- [Taylor series](https://en.wikipedia.org/wiki/Taylor_series)
- [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow)
- [Tensor Processing Unit](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)
- [Theano (software)](https://en.wikipedia.org/wiki/Theano_(software))
- [Thomas Neumann](https://en.wikipedia.org/wiki/Thomas_Neumann)
- [Transpose](https://en.wikipedia.org/wiki/Transpose)
- [Unary operation](https://en.wikipedia.org/wiki/Unary_operation)
- [Vision processing unit](https://en.wikipedia.org/wiki/Vision_processing_unit)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Template:Cite book](https://en.wikipedia.org/wiki/Template:Cite_book)
- [Template:Cite journal](https://en.wikipedia.org/wiki/Template:Cite_journal)
- [Template:Differentiable computing](https://en.wikipedia.org/wiki/Template:Differentiable_computing)
- [Template talk:Differentiable computing](https://en.wikipedia.org/wiki/Template_talk:Differentiable_computing)
- [Help:Authority control](https://en.wikipedia.org/wiki/Help:Authority_control)
- [Category:CS1 maint: multiple names: authors list](https://en.wikipedia.org/wiki/Category:CS1_maint:_multiple_names:_authors_list)
- [Portal:Computer programming](https://en.wikipedia.org/wiki/Portal:Computer_programming)
- [Portal:Technology](https://en.wikipedia.org/wiki/Portal:Technology)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:32:44.582676+00:00_