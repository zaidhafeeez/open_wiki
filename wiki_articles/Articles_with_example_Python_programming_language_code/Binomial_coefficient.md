---
title: Binomial coefficient
url: https://en.wikipedia.org/wiki/Binomial_coefficient
language: en
categories: ["Category:Articles with example C code", "Category:Articles with example Python (programming language) code", "Category:Articles with example Scheme (programming language) code", "Category:Articles with short description", "Category:Combinatorics", "Category:Factorial and binomial topics", "Category:Integer sequences", "Category:Operations on numbers", "Category:Short description is different from Wikidata", "Category:Triangles of numbers", "Category:Wikipedia articles incorporating text from PlanetMath"]
references: 0
last_modified: 2024-12-20T17:32:29Z
---

# Binomial coefficient

## Summary

In mathematics, the binomial coefficients are the positive integers that occur as coefficients in the binomial theorem. Commonly, a binomial coefficient is indexed by a pair of integers n ≥ k ≥ 0 and is written 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
        .
      
    
    {\displaystyle {\tb

## Full Content

In mathematics, the binomial coefficients are the positive integers that occur as coefficients in the binomial theorem. Commonly, a binomial coefficient is indexed by a pair of integers n ≥ k ≥ 0 and is written 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
        .
      
    
    {\displaystyle {\tbinom {n}{k}}.}
  
 It is the coefficient of the xk term in the polynomial expansion of the binomial power (1 + x)n; this coefficient can be computed by the multiplicative formula

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        
          
            
              n
              ×
              (
              n
              −
              1
              )
              ×
              ⋯
              ×
              (
              n
              −
              k
              +
              1
              )
            
            
              k
              ×
              (
              k
              −
              1
              )
              ×
              ⋯
              ×
              1
            
          
        
        ,
      
    
    {\displaystyle {\binom {n}{k}}={\frac {n\times (n-1)\times \cdots \times (n-k+1)}{k\times (k-1)\times \cdots \times 1}},}
  

which using factorial notation can be compactly expressed as

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        
          
            
              n
              !
            
            
              k
              !
              (
              n
              −
              k
              )
              !
            
          
        
        .
      
    
    {\displaystyle {\binom {n}{k}}={\frac {n!}{k!(n-k)!}}.}
  

For example, the fourth power of 1 + x is

  
    
      
        
          
            
              
                (
                1
                +
                x
                
                  )
                  
                    4
                  
                
              
              
                
                =
                
                  
                    
                      
                        (
                      
                      
                        4
                        0
                      
                      
                        )
                      
                    
                  
                
                
                  x
                  
                    0
                  
                
                +
                
                  
                    
                      
                        (
                      
                      
                        4
                        1
                      
                      
                        )
                      
                    
                  
                
                
                  x
                  
                    1
                  
                
                +
                
                  
                    
                      
                        (
                      
                      
                        4
                        2
                      
                      
                        )
                      
                    
                  
                
                
                  x
                  
                    2
                  
                
                +
                
                  
                    
                      
                        (
                      
                      
                        4
                        3
                      
                      
                        )
                      
                    
                  
                
                
                  x
                  
                    3
                  
                
                +
                
                  
                    
                      
                        (
                      
                      
                        4
                        4
                      
                      
                        )
                      
                    
                  
                
                
                  x
                  
                    4
                  
                
              
            
            
              
              
                
                =
                1
                +
                4
                x
                +
                6
                
                  x
                  
                    2
                  
                
                +
                4
                
                  x
                  
                    3
                  
                
                +
                
                  x
                  
                    4
                  
                
                ,
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}(1+x)^{4}&={\tbinom {4}{0}}x^{0}+{\tbinom {4}{1}}x^{1}+{\tbinom {4}{2}}x^{2}+{\tbinom {4}{3}}x^{3}+{\tbinom {4}{4}}x^{4}\\&=1+4x+6x^{2}+4x^{3}+x^{4},\end{aligned}}}
  

and the binomial coefficient 
  
    
      
        
          
            
              
                (
              
              
                4
                2
              
              
                )
              
            
          
        
        =
        
          
            
              
                4
                ×
                3
              
              
                2
                ×
                1
              
            
          
        
        =
        
          
            
              
                4
                !
              
              
                2
                !
                2
                !
              
            
          
        
        =
        6
      
    
    {\displaystyle {\tbinom {4}{2}}={\tfrac {4\times 3}{2\times 1}}={\tfrac {4!}{2!2!}}=6}
  
 is the coefficient of the x2 term.
Arranging the numbers 
  
    
      
        
          
            
              
                (
              
              
                n
                0
              
              
                )
              
            
          
        
        ,
        
          
            
              
                (
              
              
                n
                1
              
              
                )
              
            
          
        
        ,
        …
        ,
        
          
            
              
                (
              
              
                n
                n
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{0}},{\tbinom {n}{1}},\ldots ,{\tbinom {n}{n}}}
  
 in successive rows for n = 0, 1, 2, ... gives a triangular array called Pascal's triangle, satisfying the recurrence relation

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              
                n
                −
                1
              
              
                k
                −
                1
              
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              
                n
                −
                1
              
              k
            
            
              )
            
          
        
        .
      
    
    {\displaystyle {\binom {n}{k}}={\binom {n-1}{k-1}}+{\binom {n-1}{k}}.}
  

The binomial coefficients occur in many areas of mathematics, and especially in combinatorics. In combinatorics the symbol 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
 is usually read as "n choose k" because there are 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
 ways to choose an (unordered) subset of k elements from a fixed set of n elements. For example, there are 
  
    
      
        
          
            
              
                (
              
              
                4
                2
              
              
                )
              
            
          
        
        =
        6
      
    
    {\displaystyle {\tbinom {4}{2}}=6}
  
 ways to choose 2 elements from {1, 2, 3, 4}, namely {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4} and {3, 4}.
The first form of the binomial coefficients can be generalized to 
  
    
      
        
          
            
              
                (
              
              
                z
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {z}{k}}}
  
 for any complex number z and integer k ≥ 0, and many of their properties continue to hold in this more general form.

History and notation
Andreas von Ettingshausen introduced the notation 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
 in 1826, although the numbers were known centuries earlier (see Pascal's triangle). In about 1150, the Indian mathematician Bhaskaracharya gave an exposition of binomial coefficients in his book Līlāvatī.
Alternative notations include C(n, k), nCk, nCk, Ckn, Cnk, and Cn,k, in all of which the C stands for combinations or choices; the C notation means the number of ways to choose k out of n objects. Many calculators use variants of the C notation because they can represent it on a single-line display. In this form the binomial coefficients are easily compared to the numbers of k-permutations of n, written as P(n, k), etc.

Definition and interpretations
For natural numbers (taken to include 0) n and k, the binomial coefficient 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
 can be defined as the coefficient of the monomial Xk in the expansion of (1 + X)n. The same coefficient also occurs (if k ≤ n) in the binomial formula

(valid for any elements x, y of a commutative ring),
which explains the name "binomial coefficient".
Another occurrence of this number is in combinatorics, where it gives the number of ways, disregarding order, that k objects can be chosen from among n objects; more formally, the number of k-element subsets (or k-combinations) of an n-element set. This number can be seen as equal to the one of the first definition, independently of any of the formulas below to compute it: if in each of the n factors of the power (1 + X)n one temporarily labels the term X with an index i (running from 1 to n), then each subset of k indices gives after expansion a contribution Xk, and the coefficient of that monomial in the result will be the number of such subsets. This shows in particular that 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
 is a natural number for any natural numbers n and k. There are many other combinatorial interpretations of binomial coefficients (counting problems for which the answer is given by a binomial coefficient expression), for instance the number of words formed of n bits (digits 0 or 1) whose sum is k is given by 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
, while the number of ways to write 
  
    
      
        k
        =
        
          a
          
            1
          
        
        +
        
          a
          
            2
          
        
        +
        ⋯
        +
        
          a
          
            n
          
        
      
    
    {\displaystyle k=a_{1}+a_{2}+\cdots +a_{n}}
  
 where every ai is a nonnegative integer is given by ⁠
  
    
      
        
          
            
              
                (
              
              
                
                  n
                  +
                  k
                  −
                  1
                
                
                  n
                  −
                  1
                
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n+k-1}{n-1}}}
  
⁠. Most of these interpretations can be shown to be equivalent to counting k-combinations.

Computing the value of binomial coefficients
Several methods exist to compute the value of 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
 without actually expanding a binomial power or counting k-combinations.

Recursive formula
One method uses the recursive, purely additive formula

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              
                n
                −
                1
              
              
                k
                −
                1
              
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              
                n
                −
                1
              
              k
            
            
              )
            
          
        
      
    
    {\displaystyle {\binom {n}{k}}={\binom {n-1}{k-1}}+{\binom {n-1}{k}}}
  
 for all integers 
  
    
      
        n
        ,
        k
      
    
    {\displaystyle n,k}
  
 such that 
  
    
      
        1
        ≤
        k
        <
        n
        ,
      
    
    {\displaystyle 1\leq k<n,}
  

with boundary values

  
    
      
        
          
            
              (
            
            
              n
              0
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              n
              n
            
            
              )
            
          
        
        =
        1
      
    
    {\displaystyle {\binom {n}{0}}={\binom {n}{n}}=1}
  

for all integers n ≥ 0.
The formula follows from considering the set {1, 2, 3, ..., n} and counting separately (a) the k-element groupings that include a particular set element, say "i", in every group (since "i" is already chosen to fill one spot in every group, we need only choose k − 1 from the remaining n − 1) and (b) all the k-groupings that don't include "i"; this enumerates all the possible k-combinations of n elements. It also follows from tracing the contributions to Xk in (1 + X)n−1(1 + X). As there is zero Xn+1 or X−1 in (1 + X)n, one might extend the definition beyond the above boundaries to include 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
        =
        0
      
    
    {\displaystyle {\tbinom {n}{k}}=0}
  
 when either k > n or k < 0. This recursive formula then allows the construction of Pascal's triangle, surrounded by white spaces where the zeros, or the trivial coefficients, would be.

Multiplicative formula
A more efficient method to compute individual binomial coefficients is given by the formula

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        
          
            
              n
              
                
                  k
                  _
                
              
            
            
              k
              !
            
          
        
        =
        
          
            
              n
              (
              n
              −
              1
              )
              (
              n
              −
              2
              )
              ⋯
              (
              n
              −
              (
              k
              −
              1
              )
              )
            
            
              k
              (
              k
              −
              1
              )
              (
              k
              −
              2
              )
              ⋯
              1
            
          
        
        =
        
          ∏
          
            i
            =
            1
          
          
            k
          
        
        
          
            
              n
              +
              1
              −
              i
            
            i
          
        
        ,
      
    
    {\displaystyle {\binom {n}{k}}={\frac {n^{\underline {k}}}{k!}}={\frac {n(n-1)(n-2)\cdots (n-(k-1))}{k(k-1)(k-2)\cdots 1}}=\prod _{i=1}^{k}{\frac {n+1-i}{i}},}
  

where the numerator of the first fraction, 
  
    
      
        
          n
          
            
              k
              _
            
          
        
      
    
    {\displaystyle n^{\underline {k}}}
  
, is a falling factorial.
This formula is easiest to understand for the combinatorial interpretation of binomial coefficients.
The numerator gives the number of ways to select a sequence of k distinct objects, retaining the order of selection, from a set of n objects. The denominator counts the number of distinct sequences that define the same k-combination when order is disregarded. This formula can also be stated in a recursive form. Using the "C" notation from above, 
  
    
      
        
          C
          
            n
            ,
            k
          
        
        =
        
          C
          
            n
            ,
            k
            −
            1
          
        
        ⋅
        (
        n
        −
        k
        +
        1
        )
        
          /
        
        k
      
    
    {\displaystyle C_{n,k}=C_{n,k-1}\cdot (n-k+1)/k}
  
, where 
  
    
      
        
          C
          
            n
            ,
            0
          
        
        =
        1
      
    
    {\displaystyle C_{n,0}=1}
  
. It is readily derived by evaluating 
  
    
      
        
          C
          
            n
            ,
            k
          
        
        
          /
        
        
          C
          
            n
            ,
            k
            −
            1
          
        
      
    
    {\displaystyle C_{n,k}/C_{n,k-1}}
  
 and can intuitively be understood as starting at the leftmost coefficient of the 
  
    
      
        n
      
    
    {\displaystyle n}
  
-th row of Pascal's triangle, whose value is always 
  
    
      
        1
      
    
    {\displaystyle 1}
  
, and recursively computing the next coefficient to its right until the 
  
    
      
        k
      
    
    {\displaystyle k}
  
-th one is reached.
Due to the symmetry of the binomial coefficients with regard to k and n − k, calculation of the above product, as well as the recursive relation, may be optimised by setting its upper limit to the smaller of k and n − k.

Factorial formula
Finally, though computationally unsuitable, there is the compact form, often used in proofs and derivations, which makes repeated use of the familiar factorial function:

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        
          
            
              n
              !
            
            
              k
              !
              
              (
              n
              −
              k
              )
              !
            
          
        
        
        
          for 
        
         
        0
        ≤
        k
        ≤
        n
        ,
      
    
    {\displaystyle {\binom {n}{k}}={\frac {n!}{k!\,(n-k)!}}\quad {\text{for }}\ 0\leq k\leq n,}
  

where n! denotes the factorial of n. This formula follows from the multiplicative formula above by multiplying numerator and denominator by (n − k)!; as a consequence it involves many factors common to numerator and denominator. It is less practical for explicit computation (in the case that k is small and n is large) unless common factors are first cancelled (in particular since factorial values grow very rapidly). The formula does exhibit a symmetry that is less evident from the multiplicative formula (though it is from the definitions)

which leads to a more efficient multiplicative computational routine. Using the falling factorial notation,

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        
          
            {
            
              
                
                  
                    n
                    
                      
                        k
                        _
                      
                    
                  
                  
                    /
                  
                  k
                  !
                
                
                  
                    if 
                  
                   
                  k
                  ≤
                  
                    
                      n
                      2
                    
                  
                
              
              
                
                  
                    n
                    
                      
                        
                          n
                          −
                          k
                        
                        _
                      
                    
                  
                  
                    /
                  
                  (
                  n
                  −
                  k
                  )
                  !
                
                
                  
                    if 
                  
                   
                  k
                  >
                  
                    
                      n
                      2
                    
                  
                
              
            
            
          
        
        .
      
    
    {\displaystyle {\binom {n}{k}}={\begin{cases}n^{\underline {k}}/k!&{\text{if }}\ k\leq {\frac {n}{2}}\\n^{\underline {n-k}}/(n-k)!&{\text{if }}\ k>{\frac {n}{2}}\end{cases}}.}

Generalization and connection to the binomial series
The multiplicative formula allows the definition of binomial coefficients to be extended by replacing n by an arbitrary number α (negative, real, complex) or even an element of any commutative ring in which all positive integers are invertible:

  
    
      
        
          
            
              (
            
            
              α
              k
            
            
              )
            
          
        
        =
        
          
            
              α
              
                
                  k
                  _
                
              
            
            
              k
              !
            
          
        
        =
        
          
            
              α
              (
              α
              −
              1
              )
              (
              α
              −
              2
              )
              ⋯
              (
              α
              −
              k
              +
              1
              )
            
            
              k
              (
              k
              −
              1
              )
              (
              k
              −
              2
              )
              ⋯
              1
            
          
        
        
        
          for 
        
        k
        ∈
        
          N
        
        
           and arbitrary 
        
        α
        .
      
    
    {\displaystyle {\binom {\alpha }{k}}={\frac {\alpha ^{\underline {k}}}{k!}}={\frac {\alpha (\alpha -1)(\alpha -2)\cdots (\alpha -k+1)}{k(k-1)(k-2)\cdots 1}}\quad {\text{for }}k\in \mathbb {N} {\text{ and arbitrary }}\alpha .}
  

With this definition one has a generalization of the binomial formula (with one of the variables set to 1), which justifies still calling the 
  
    
      
        
          
            
              
                (
              
              
                α
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {\alpha }{k}}}
  
 binomial coefficients:

This formula is valid for all complex numbers α and X with |X| < 1. It can also be interpreted as an identity of formal power series in X, where it actually can serve as definition of arbitrary powers of power series with constant coefficient equal to 1; the point is that with this definition all identities hold that one expects for exponentiation, notably

  
    
      
        (
        1
        +
        X
        
          )
          
            α
          
        
        (
        1
        +
        X
        
          )
          
            β
          
        
        =
        (
        1
        +
        X
        
          )
          
            α
            +
            β
          
        
        
        
          and
        
        
        (
        (
        1
        +
        X
        
          )
          
            α
          
        
        
          )
          
            β
          
        
        =
        (
        1
        +
        X
        
          )
          
            α
            β
          
        
        .
      
    
    {\displaystyle (1+X)^{\alpha }(1+X)^{\beta }=(1+X)^{\alpha +\beta }\quad {\text{and}}\quad ((1+X)^{\alpha })^{\beta }=(1+X)^{\alpha \beta }.}
  

If α is a nonnegative integer n, then all terms with k > n are zero, and the infinite series becomes a finite sum, thereby recovering the binomial formula. However, for other values of α, including negative integers and rational numbers, the series is really infinite.

Pascal's triangle
Pascal's rule is the important recurrence relation

which can be used to prove by mathematical induction that 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
 is a natural number for all integer n ≥ 0 and all integer k, a fact that is not immediately obvious from formula (1). To the left and right of Pascal's triangle, the entries (shown as blanks) are all zero.
Pascal's rule also gives rise to Pascal's triangle:

Row number n contains the numbers 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
 for k = 0, …, n. It is constructed by first placing 1s in the outermost positions, and then filling each inner position with the sum of the two numbers directly above. This method allows the quick calculation of binomial coefficients without the need for fractions or multiplications. For instance, by looking at row number 5 of the triangle, one can quickly read off that

  
    
      
        (
        x
        +
        y
        
          )
          
            5
          
        
        =
        
          
            1
            _
          
        
        
          x
          
            5
          
        
        +
        
          
            5
            _
          
        
        
          x
          
            4
          
        
        y
        +
        
          
            10
            _
          
        
        
          x
          
            3
          
        
        
          y
          
            2
          
        
        +
        
          
            10
            _
          
        
        
          x
          
            2
          
        
        
          y
          
            3
          
        
        +
        
          
            5
            _
          
        
        x
        
          y
          
            4
          
        
        +
        
          
            1
            _
          
        
        
          y
          
            5
          
        
        .
      
    
    {\displaystyle (x+y)^{5}={\underline {1}}x^{5}+{\underline {5}}x^{4}y+{\underline {10}}x^{3}y^{2}+{\underline {10}}x^{2}y^{3}+{\underline {5}}xy^{4}+{\underline {1}}y^{5}.}

Combinatorics and statistics
Binomial coefficients are of importance in combinatorics because they provide ready formulas for certain frequent counting problems:

There are 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
 ways to choose k elements from a set of n elements. See Combination.
There are 
  
    
      
        
          
            
              
                (
              
              
                
                  n
                  +
                  k
                  −
                  1
                
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n+k-1}{k}}}
  
 ways to choose k elements from a set of n elements if repetitions are allowed. See Multiset.
There are 
  
    
      
        
          
            
              
                (
              
              
                
                  n
                  +
                  k
                
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n+k}{k}}}
  
 strings containing k ones and n zeros.
There are 
  
    
      
        
          
            
              
                (
              
              
                
                  n
                  +
                  1
                
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n+1}{k}}}
  
 strings consisting of k ones and n zeros such that no two ones are adjacent.
The Catalan numbers are 
  
    
      
        
          
            
              1
              
                n
                +
                1
              
            
          
        
        
          
            
              
                (
              
              
                
                  2
                  n
                
                n
              
              
                )
              
            
          
        
        .
      
    
    {\displaystyle {\tfrac {1}{n+1}}{\tbinom {2n}{n}}.}
  

The binomial distribution in statistics is 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
        
          p
          
            k
          
        
        (
        1
        −
        p
        
          )
          
            n
            −
            k
          
        
        .
      
    
    {\displaystyle {\tbinom {n}{k}}p^{k}(1-p)^{n-k}.}

Binomial coefficients as polynomials
For any nonnegative integer k, the expression 
  
    
      
        
          
            
              (
            
            
              t
              k
            
            
              )
            
          
        
      
    
    {\textstyle {\binom {t}{k}}}
  
 can be written as a polynomial with denominator k!:

  
    
      
        
          
            
              (
            
            
              t
              k
            
            
              )
            
          
        
        =
        
          
            
              t
              
                
                  k
                  _
                
              
            
            
              k
              !
            
          
        
        =
        
          
            
              t
              (
              t
              −
              1
              )
              (
              t
              −
              2
              )
              ⋯
              (
              t
              −
              k
              +
              1
              )
            
            
              k
              (
              k
              −
              1
              )
              (
              k
              −
              2
              )
              ⋯
              2
              ⋅
              1
            
          
        
        ;
      
    
    {\displaystyle {\binom {t}{k}}={\frac {t^{\underline {k}}}{k!}}={\frac {t(t-1)(t-2)\cdots (t-k+1)}{k(k-1)(k-2)\cdots 2\cdot 1}};}
  

this presents a polynomial in t with rational coefficients.
As such, it can be evaluated at any real or complex number t to define binomial coefficients with such first arguments. These "generalized binomial coefficients" appear in Newton's generalized binomial theorem.
For each k, the polynomial 
  
    
      
        
          
            
              
                (
              
              
                t
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {t}{k}}}
  
 can be characterized as the unique degree k polynomial p(t) satisfying p(0) = p(1) = ⋯ = p(k − 1) = 0 and p(k) = 1.
Its coefficients are expressible in terms of Stirling numbers of the first kind:

  
    
      
        
          
            
              (
            
            
              t
              k
            
            
              )
            
          
        
        =
        
          ∑
          
            i
            =
            0
          
          
            k
          
        
        s
        (
        k
        ,
        i
        )
        
          
            
              t
              
                i
              
            
            
              k
              !
            
          
        
        .
      
    
    {\displaystyle {\binom {t}{k}}=\sum _{i=0}^{k}s(k,i){\frac {t^{i}}{k!}}.}
  

The derivative of 
  
    
      
        
          
            
              
                (
              
              
                t
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {t}{k}}}
  
 can be calculated by logarithmic differentiation:

  
    
      
        
          
            
              d
            
            
              
                d
              
              t
            
          
        
        
          
            
              (
            
            
              t
              k
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              t
              k
            
            
              )
            
          
        
        
          ∑
          
            i
            =
            0
          
          
            k
            −
            1
          
        
        
          
            1
            
              t
              −
              i
            
          
        
        .
      
    
    {\displaystyle {\frac {\mathrm {d} }{\mathrm {d} t}}{\binom {t}{k}}={\binom {t}{k}}\sum _{i=0}^{k-1}{\frac {1}{t-i}}.}
  

This can cause a problem when evaluated at integers from 
  
    
      
        0
      
    
    {\displaystyle 0}
  
 to 
  
    
      
        t
        −
        1
      
    
    {\displaystyle t-1}
  
, but using identities below we can compute the derivative as:

  
    
      
        
          
            
              d
            
            
              
                d
              
              t
            
          
        
        
          
            
              (
            
            
              t
              k
            
            
              )
            
          
        
        =
        
          ∑
          
            i
            =
            0
          
          
            k
            −
            1
          
        
        
          
            
              (
              −
              1
              
                )
                
                  k
                  −
                  i
                  −
                  1
                
              
            
            
              k
              −
              i
            
          
        
        
          
            
              (
            
            
              t
              i
            
            
              )
            
          
        
        .
      
    
    {\displaystyle {\frac {\mathrm {d} }{\mathrm {d} t}}{\binom {t}{k}}=\sum _{i=0}^{k-1}{\frac {(-1)^{k-i-1}}{k-i}}{\binom {t}{i}}.}

Binomial coefficients as a basis for the space of polynomials
Over any field of characteristic 0 (that is, any field that contains the rational numbers), each polynomial p(t) of degree at most d is uniquely expressible as a linear combination 
  
    
      
        
          ∑
          
            k
            =
            0
          
          
            d
          
        
        
          a
          
            k
          
        
        
          
            
              (
            
            
              t
              k
            
            
              )
            
          
        
      
    
    {\textstyle \sum _{k=0}^{d}a_{k}{\binom {t}{k}}}
  
 of binomial coefficients, because the binomial coefficients consist of one polynomial of each degree. The coefficient ak is the kth difference of the sequence p(0), p(1), ..., p(k). Explicitly,

Integer-valued polynomials
Each polynomial 
  
    
      
        
          
            
              
                (
              
              
                t
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {t}{k}}}
  
 is integer-valued: it has an integer value at all integer inputs 
  
    
      
        t
      
    
    {\displaystyle t}
  
. (One way to prove this is by induction on k using Pascal's identity.) Therefore, any integer linear combination of binomial coefficient polynomials is integer-valued too. Conversely, (4) shows that any integer-valued polynomial is an integer linear combination of these binomial coefficient polynomials. More generally, for any subring R of a characteristic 0 field K, a polynomial in K[t] takes values in R at all integers if and only if it is an R-linear combination of binomial coefficient polynomials.

Example
The integer-valued polynomial 3t(3t + 1) / 2 can be rewritten as

  
    
      
        9
        
          
            
              (
            
            
              t
              2
            
            
              )
            
          
        
        +
        6
        
          
            
              (
            
            
              t
              1
            
            
              )
            
          
        
        +
        0
        
          
            
              (
            
            
              t
              0
            
            
              )
            
          
        
        .
      
    
    {\displaystyle 9{\binom {t}{2}}+6{\binom {t}{1}}+0{\binom {t}{0}}.}

Identities involving binomial coefficients
The factorial formula facilitates relating nearby binomial coefficients. For instance, if k is a positive integer and n is arbitrary, then

and, with a little more work,

  
    
      
        
          
            
              (
            
            
              
                n
                −
                1
              
              k
            
            
              )
            
          
        
        −
        
          
            
              (
            
            
              
                n
                −
                1
              
              
                k
                −
                1
              
            
            
              )
            
          
        
        =
        
          
            
              n
              −
              2
              k
            
            n
          
        
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        .
      
    
    {\displaystyle {\binom {n-1}{k}}-{\binom {n-1}{k-1}}={\frac {n-2k}{n}}{\binom {n}{k}}.}
  

We can also get

  
    
      
        
          
            
              (
            
            
              
                n
                −
                1
              
              k
            
            
              )
            
          
        
        =
        
          
            
              n
              −
              k
            
            n
          
        
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        .
      
    
    {\displaystyle {\binom {n-1}{k}}={\frac {n-k}{n}}{\binom {n}{k}}.}
  

Moreover, the iteration formula  may be useful:

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        
          
            
              (
            
            
              k
              j
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              n
              j
            
            
              )
            
          
        
        
          
            
              (
            
            
              
                n
                −
                j
              
              
                k
                −
                j
              
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              n
              
                k
                −
                j
              
            
            
              )
            
          
        
        
          
            
              (
            
            
              
                n
                −
                k
                +
                j
              
              j
            
            
              )
            
          
        
        .
      
    
    {\displaystyle {\binom {n}{k}}{\binom {k}{j}}={\binom {n}{j}}{\binom {n-j}{k-j}}={\binom {n}{k-j}}{\binom {n-k+j}{j}}.}
  

For constant n, we have the following recurrence:

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        
          
            
              n
              −
              k
              +
              1
            
            k
          
        
        
          
            
              (
            
            
              n
              
                k
                −
                1
              
            
            
              )
            
          
        
        .
      
    
    {\displaystyle {\binom {n}{k}}={\frac {n-k+1}{k}}{\binom {n}{k-1}}.}
  

To sum up, we have

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              n
              
                n
                −
                k
              
            
            
              )
            
          
        
        =
        
          
            
              n
              −
              k
              +
              1
            
            k
          
        
        
          
            
              (
            
            
              n
              
                k
                −
                1
              
            
            
              )
            
          
        
        =
        
          
            n
            
              n
              −
              k
            
          
        
        
          
            
              (
            
            
              
                n
                −
                1
              
              k
            
            
              )
            
          
        
      
    
    {\displaystyle {\binom {n}{k}}={\binom {n}{n-k}}={\frac {n-k+1}{k}}{\binom {n}{k-1}}={\frac {n}{n-k}}{\binom {n-1}{k}}}
  

  
    
      
        =
        
          
            n
            k
          
        
        
          
            
              (
            
            
              
                n
                −
                1
              
              
                k
                −
                1
              
            
            
              )
            
          
        
        =
        
          
            n
            
              n
              −
              2
              k
            
          
        
        
          
            (
          
        
        
          
            
              (
            
            
              
                n
                −
                1
              
              k
            
            
              )
            
          
        
        −
        
          
            
              (
            
            
              
                n
                −
                1
              
              
                k
                −
                1
              
            
            
              )
            
          
        
        
          
            )
          
        
        =
        
          
            
              (
            
            
              
                n
                −
                1
              
              k
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              
                n
                −
                1
              
              
                k
                −
                1
              
            
            
              )
            
          
        
        .
      
    
    {\displaystyle ={\frac {n}{k}}{\binom {n-1}{k-1}}={\frac {n}{n-2k}}{\Bigg (}{\binom {n-1}{k}}-{\binom {n-1}{k-1}}{\Bigg )}={\binom {n-1}{k}}+{\binom {n-1}{k-1}}.}

Sums of the binomial coefficients
The formula

says that the elements in the nth row of Pascal's triangle always add up to 2 raised to the nth power. This is obtained from the binomial theorem (∗) by setting x = 1 and y = 1. The formula also has a natural combinatorial interpretation: the left side sums the number of subsets of {1, ..., n} of sizes k = 0, 1, ..., n, giving the total number of subsets. (That is, the left side counts the power set of {1, ..., n}.) However, these subsets can also be generated by successively choosing or excluding each element 1, ..., n; the n independent binary choices (bit-strings) allow a total of 
  
    
      
        
          2
          
            n
          
        
      
    
    {\displaystyle 2^{n}}
  
 choices. The left and right sides are two ways to count the same collection of subsets, so they are equal.
The formulas

and

  
    
      
        
          ∑
          
            k
            =
            0
          
          
            n
          
        
        
          k
          
            2
          
        
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        (
        n
        +
        
          n
          
            2
          
        
        )
        
          2
          
            n
            −
            2
          
        
      
    
    {\displaystyle \sum _{k=0}^{n}k^{2}{\binom {n}{k}}=(n+n^{2})2^{n-2}}
  

follow from the binomial theorem after differentiating with respect to x (twice for the latter) and then substituting x = y = 1.
The Chu–Vandermonde identity, which holds for any complex values m and n and any non-negative integer k, is

and can be found by examination of the coefficient of 
  
    
      
        
          x
          
            k
          
        
      
    
    {\displaystyle x^{k}}
  
 in the expansion of (1 + x)m(1 + x)n−m = (1 + x)n using equation (2). When m = 1, equation (7) reduces to equation (3). In the special case n = 2m, k = m, using (1), the expansion (7) becomes (as seen in Pascal's triangle at right)

where the term on the right side is a central binomial coefficient.
Another form of the Chu–Vandermonde identity, which applies for any integers j, k, and n satisfying 0 ≤ j ≤ k ≤ n, is

The proof is similar, but uses the binomial series expansion (2) with negative integer exponents.
When j = k, equation (9) gives the hockey-stick identity

  
    
      
        
          ∑
          
            m
            =
            k
          
          
            n
          
        
        
          
            
              (
            
            
              m
              k
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              
                n
                +
                1
              
              
                k
                +
                1
              
            
            
              )
            
          
        
      
    
    {\displaystyle \sum _{m=k}^{n}{\binom {m}{k}}={\binom {n+1}{k+1}}}
  

and its relative

  
    
      
        
          ∑
          
            r
            =
            0
          
          
            m
          
        
        
          
            
              (
            
            
              
                n
                +
                r
              
              r
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              
                n
                +
                m
                +
                1
              
              m
            
            
              )
            
          
        
        .
      
    
    {\displaystyle \sum _{r=0}^{m}{\binom {n+r}{r}}={\binom {n+m+1}{m}}.}
  

Let F(n) denote the n-th Fibonacci number.
Then

  
    
      
        
          ∑
          
            k
            =
            0
          
          
            ⌊
            n
            
              /
            
            2
            ⌋
          
        
        
          
            
              (
            
            
              
                n
                −
                k
              
              k
            
            
              )
            
          
        
        =
        F
        (
        n
        +
        1
        )
        .
      
    
    {\displaystyle \sum _{k=0}^{\lfloor n/2\rfloor }{\binom {n-k}{k}}=F(n+1).}
  

This can be proved by induction using (3) or by Zeckendorf's representation. A combinatorial proof is given below.

Multisections of sums
For integers s and t such that 
  
    
      
        0
        ≤
        t
        <
        s
        ,
      
    
    {\displaystyle 0\leq t<s,}
  
 series multisection gives the following identity for the sum of binomial coefficients:

  
    
      
        
          
            
              (
            
            
              n
              t
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              
                t
                +
                s
              
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              
                t
                +
                2
                s
              
            
            
              )
            
          
        
        +
        …
        =
        
          
            1
            s
          
        
        
          ∑
          
            j
            =
            0
          
          
            s
            −
            1
          
        
        
          
            (
            
              2
              cos
              ⁡
              
                
                  
                    π
                    j
                  
                  s
                
              
            
            )
          
          
            n
          
        
        cos
        ⁡
        
          
            
              π
              (
              n
              −
              2
              t
              )
              j
            
            s
          
        
        .
      
    
    {\displaystyle {\binom {n}{t}}+{\binom {n}{t+s}}+{\binom {n}{t+2s}}+\ldots ={\frac {1}{s}}\sum _{j=0}^{s-1}\left(2\cos {\frac {\pi j}{s}}\right)^{n}\cos {\frac {\pi (n-2t)j}{s}}.}
  

For small s, these series have particularly nice forms; for example,

  
    
      
        
          
            
              (
            
            
              n
              0
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              3
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              6
            
            
              )
            
          
        
        +
        ⋯
        =
        
          
            1
            3
          
        
        
          (
          
            
              2
              
                n
              
            
            +
            2
            cos
            ⁡
            
              
                
                  n
                  π
                
                3
              
            
          
          )
        
      
    
    {\displaystyle {\binom {n}{0}}+{\binom {n}{3}}+{\binom {n}{6}}+\cdots ={\frac {1}{3}}\left(2^{n}+2\cos {\frac {n\pi }{3}}\right)}
  

  
    
      
        
          
            
              (
            
            
              n
              1
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              4
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              7
            
            
              )
            
          
        
        +
        ⋯
        =
        
          
            1
            3
          
        
        
          (
          
            
              2
              
                n
              
            
            +
            2
            cos
            ⁡
            
              
                
                  (
                  n
                  −
                  2
                  )
                  π
                
                3
              
            
          
          )
        
      
    
    {\displaystyle {\binom {n}{1}}+{\binom {n}{4}}+{\binom {n}{7}}+\cdots ={\frac {1}{3}}\left(2^{n}+2\cos {\frac {(n-2)\pi }{3}}\right)}
  

  
    
      
        
          
            
              (
            
            
              n
              2
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              5
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              8
            
            
              )
            
          
        
        +
        ⋯
        =
        
          
            1
            3
          
        
        
          (
          
            
              2
              
                n
              
            
            +
            2
            cos
            ⁡
            
              
                
                  (
                  n
                  −
                  4
                  )
                  π
                
                3
              
            
          
          )
        
      
    
    {\displaystyle {\binom {n}{2}}+{\binom {n}{5}}+{\binom {n}{8}}+\cdots ={\frac {1}{3}}\left(2^{n}+2\cos {\frac {(n-4)\pi }{3}}\right)}
  

  
    
      
        
          
            
              (
            
            
              n
              0
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              4
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              8
            
            
              )
            
          
        
        +
        ⋯
        =
        
          
            1
            2
          
        
        
          (
          
            
              2
              
                n
                −
                1
              
            
            +
            
              2
              
                
                  n
                  2
                
              
            
            cos
            ⁡
            
              
                
                  n
                  π
                
                4
              
            
          
          )
        
      
    
    {\displaystyle {\binom {n}{0}}+{\binom {n}{4}}+{\binom {n}{8}}+\cdots ={\frac {1}{2}}\left(2^{n-1}+2^{\frac {n}{2}}\cos {\frac {n\pi }{4}}\right)}
  

  
    
      
        
          
            
              (
            
            
              n
              1
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              5
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              9
            
            
              )
            
          
        
        +
        ⋯
        =
        
          
            1
            2
          
        
        
          (
          
            
              2
              
                n
                −
                1
              
            
            +
            
              2
              
                
                  n
                  2
                
              
            
            sin
            ⁡
            
              
                
                  n
                  π
                
                4
              
            
          
          )
        
      
    
    {\displaystyle {\binom {n}{1}}+{\binom {n}{5}}+{\binom {n}{9}}+\cdots ={\frac {1}{2}}\left(2^{n-1}+2^{\frac {n}{2}}\sin {\frac {n\pi }{4}}\right)}
  

  
    
      
        
          
            
              (
            
            
              n
              2
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              6
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              10
            
            
              )
            
          
        
        +
        ⋯
        =
        
          
            1
            2
          
        
        
          (
          
            
              2
              
                n
                −
                1
              
            
            −
            
              2
              
                
                  n
                  2
                
              
            
            cos
            ⁡
            
              
                
                  n
                  π
                
                4
              
            
          
          )
        
      
    
    {\displaystyle {\binom {n}{2}}+{\binom {n}{6}}+{\binom {n}{10}}+\cdots ={\frac {1}{2}}\left(2^{n-1}-2^{\frac {n}{2}}\cos {\frac {n\pi }{4}}\right)}
  

  
    
      
        
          
            
              (
            
            
              n
              3
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              7
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              n
              11
            
            
              )
            
          
        
        +
        ⋯
        =
        
          
            1
            2
          
        
        
          (
          
            
              2
              
                n
                −
                1
              
            
            −
            
              2
              
                
                  n
                  2
                
              
            
            sin
            ⁡
            
              
                
                  n
                  π
                
                4
              
            
          
          )
        
      
    
    {\displaystyle {\binom {n}{3}}+{\binom {n}{7}}+{\binom {n}{11}}+\cdots ={\frac {1}{2}}\left(2^{n-1}-2^{\frac {n}{2}}\sin {\frac {n\pi }{4}}\right)}

Partial sums
Although there is no closed formula for partial sums

  
    
      
        
          ∑
          
            j
            =
            0
          
          
            k
          
        
        
          
            
              (
            
            
              n
              j
            
            
              )
            
          
        
      
    
    {\displaystyle \sum _{j=0}^{k}{\binom {n}{j}}}
  

of binomial coefficients, one can again use (3) and induction to show that for k = 0, …, n − 1,

  
    
      
        
          ∑
          
            j
            =
            0
          
          
            k
          
        
        (
        −
        1
        
          )
          
            j
          
        
        
          
            
              (
            
            
              n
              j
            
            
              )
            
          
        
        =
        (
        −
        1
        
          )
          
            k
          
        
        
          
            
              (
            
            
              
                n
                −
                1
              
              k
            
            
              )
            
          
        
        ,
      
    
    {\displaystyle \sum _{j=0}^{k}(-1)^{j}{\binom {n}{j}}=(-1)^{k}{\binom {n-1}{k}},}
  

with special case

  
    
      
        
          ∑
          
            j
            =
            0
          
          
            n
          
        
        (
        −
        1
        
          )
          
            j
          
        
        
          
            
              (
            
            
              n
              j
            
            
              )
            
          
        
        =
        0
      
    
    {\displaystyle \sum _{j=0}^{n}(-1)^{j}{\binom {n}{j}}=0}
  

for n > 0. This latter result is also a special case of the result from the theory of finite differences that for any polynomial P(x) of degree less than n,

  
    
      
        
          ∑
          
            j
            =
            0
          
          
            n
          
        
        (
        −
        1
        
          )
          
            j
          
        
        
          
            
              (
            
            
              n
              j
            
            
              )
            
          
        
        P
        (
        j
        )
        =
        0.
      
    
    {\displaystyle \sum _{j=0}^{n}(-1)^{j}{\binom {n}{j}}P(j)=0.}
  

Differentiating (2) k times and setting x = −1 yields this for

  
    
      
        P
        (
        x
        )
        =
        x
        (
        x
        −
        1
        )
        ⋯
        (
        x
        −
        k
        +
        1
        )
      
    
    {\displaystyle P(x)=x(x-1)\cdots (x-k+1)}
  
,
when 0 ≤ k < n,
and the general case follows by taking linear combinations of these.
When P(x) is of degree less than or equal to n,

where 
  
    
      
        
          a
          
            n
          
        
      
    
    {\displaystyle a_{n}}
  
 is the coefficient of degree n in P(x).
More generally for (10),

  
    
      
        
          ∑
          
            j
            =
            0
          
          
            n
          
        
        (
        −
        1
        
          )
          
            j
          
        
        
          
            
              (
            
            
              n
              j
            
            
              )
            
          
        
        P
        (
        m
        +
        (
        n
        −
        j
        )
        d
        )
        =
        
          d
          
            n
          
        
        n
        !
        
          a
          
            n
          
        
      
    
    {\displaystyle \sum _{j=0}^{n}(-1)^{j}{\binom {n}{j}}P(m+(n-j)d)=d^{n}n!a_{n}}
  

where m and d are complex numbers. This follows immediately applying (10) to the polynomial ⁠
  
    
      
        Q
        (
        x
        )
        :=
        P
        (
        m
        +
        d
        x
        )
      
    
    {\displaystyle Q(x):=P(m+dx)}
  
⁠ instead of ⁠
  
    
      
        P
        (
        x
        )
      
    
    {\displaystyle P(x)}
  
⁠, and observing that ⁠
  
    
      
        Q
        (
        x
        )
      
    
    {\displaystyle Q(x)}
  
⁠ still has degree less than or equal to n, and that its coefficient of degree n is dnan.
The series 
  
    
      
        
          
            
              k
              −
              1
            
            k
          
        
        
          ∑
          
            j
            =
            0
          
          
            ∞
          
        
        
          
            1
            
              
                (
              
              
                
                  j
                  +
                  x
                
                k
              
              
                )
              
            
          
        
        =
        
          
            1
            
              
                (
              
              
                
                  x
                  −
                  1
                
                
                  k
                  −
                  1
                
              
              
                )
              
            
          
        
      
    
    {\textstyle {\frac {k-1}{k}}\sum _{j=0}^{\infty }{\frac {1}{\binom {j+x}{k}}}={\frac {1}{\binom {x-1}{k-1}}}}
  
 is convergent for k ≥ 2. This formula is used in the analysis of the German tank problem. It follows from 
  
    
      
        
          
            
              k
              −
              1
            
            k
          
        
        
          ∑
          
            j
            =
            0
          
          
            M
          
        
        
          
            1
            
              
                (
              
              
                
                  j
                  +
                  x
                
                k
              
              
                )
              
            
          
        
        =
        
          
            1
            
              
                (
              
              
                
                  x
                  −
                  1
                
                
                  k
                  −
                  1
                
              
              
                )
              
            
          
        
        −
        
          
            1
            
              
                (
              
              
                
                  M
                  +
                  x
                
                
                  k
                  −
                  1
                
              
              
                )
              
            
          
        
      
    
    {\textstyle {\frac {k-1}{k}}\sum _{j=0}^{M}{\frac {1}{\binom {j+x}{k}}}={\frac {1}{\binom {x-1}{k-1}}}-{\frac {1}{\binom {M+x}{k-1}}}}
  
 which is proved by induction on M.

Identities with combinatorial proofs
Many identities involving binomial coefficients can be proved by combinatorial means. For example, for nonnegative integers 
  
    
      
        
          n
        
        ≥
        
          q
        
      
    
    {\displaystyle {n}\geq {q}}
  
, the identity

  
    
      
        
          ∑
          
            k
            =
            q
          
          
            n
          
        
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        
          
            
              (
            
            
              k
              q
            
            
              )
            
          
        
        =
        
          2
          
            n
            −
            q
          
        
        
          
            
              (
            
            
              n
              q
            
            
              )
            
          
        
      
    
    {\displaystyle \sum _{k=q}^{n}{\binom {n}{k}}{\binom {k}{q}}=2^{n-q}{\binom {n}{q}}}
  

(which reduces to (6) when q = 1) can be given a double counting proof, as follows. The left side counts the number of ways of selecting a subset of [n] = {1, 2, ..., n} with at least q elements, and marking q elements among those selected. The right side counts the same thing, because there are 
  
    
      
        
          
            
              
                (
              
              
                n
                q
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{q}}}
  
 ways of choosing a set of q elements to mark, and 
  
    
      
        
          2
          
            n
            −
            q
          
        
      
    
    {\displaystyle 2^{n-q}}
  
 to choose which of the remaining elements of [n] also belong to the subset.
In Pascal's identity

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              
                n
                −
                1
              
              
                k
                −
                1
              
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              
                n
                −
                1
              
              k
            
            
              )
            
          
        
        ,
      
    
    {\displaystyle {n \choose k}={n-1 \choose k-1}+{n-1 \choose k},}
  

both sides count the number of k-element subsets of [n]: the two terms on the right side group them into those that contain element n and those that do not.
The identity (8) also has a combinatorial proof. The identity reads

  
    
      
        
          ∑
          
            k
            =
            0
          
          
            n
          
        
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
          
            2
          
        
        =
        
          
            
              (
            
            
              
                2
                n
              
              n
            
            
              )
            
          
        
        .
      
    
    {\displaystyle \sum _{k=0}^{n}{\binom {n}{k}}^{2}={\binom {2n}{n}}.}
  

Suppose you have 
  
    
      
        2
        n
      
    
    {\displaystyle 2n}
  
 empty squares arranged in a row and you want to mark (select) n of them. There are 
  
    
      
        
          
            
              
                (
              
              
                
                  2
                  n
                
                n
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {2n}{n}}}
  
 ways to do this. On the other hand, you may select your n squares by selecting k squares from among the first n and 
  
    
      
        n
        −
        k
      
    
    {\displaystyle n-k}
  
 squares from the remaining n squares; any k from 0 to n will work. This gives

  
    
      
        
          ∑
          
            k
            =
            0
          
          
            n
          
        
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        
          
            
              (
            
            
              n
              
                n
                −
                k
              
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              
                2
                n
              
              n
            
            
              )
            
          
        
        .
      
    
    {\displaystyle \sum _{k=0}^{n}{\binom {n}{k}}{\binom {n}{n-k}}={\binom {2n}{n}}.}
  

Now apply (1) to get the result.
If one denotes by F(i) the sequence of Fibonacci numbers, indexed so that F(0) = F(1) = 1, then the identity

  
    
      
        
          ∑
          
            k
            =
            0
          
          
            
              ⌊
              
                
                  n
                  2
                
              
              ⌋
            
          
        
        
          
            
              (
            
            
              
                n
                −
                k
              
              k
            
            
              )
            
          
        
        =
        F
        (
        n
        )
      
    
    {\displaystyle \sum _{k=0}^{\left\lfloor {\frac {n}{2}}\right\rfloor }{\binom {n-k}{k}}=F(n)}
  

has the following combinatorial proof. One may show by induction that F(n) counts the number of ways that a n × 1 strip of squares may be covered by 2 × 1 and 1 × 1 tiles. On the other hand, if such a tiling uses exactly k of the 2 × 1 tiles, then it uses n − 2k of the 1 × 1 tiles, and so uses n − k tiles total. There are 
  
    
      
        
          
            
              
                (
              
              
                
                  n
                  −
                  k
                
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n-k}{k}}}
  
 ways to order these tiles, and so summing this coefficient over all possible values of k gives the identity.

Sum of coefficients row
The number of k-combinations for all k, 
  
    
      
        
          ∑
          
            0
            ≤
            
              k
            
            ≤
            
              n
            
          
        
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        
          2
          
            n
          
        
      
    
    {\textstyle \sum _{0\leq {k}\leq {n}}{\binom {n}{k}}=2^{n}}
  
, is the sum of the nth row (counting from 0) of the binomial coefficients. These combinations are enumerated by the 1 digits of the set of base 2 numbers counting from 0 to 
  
    
      
        
          2
          
            n
          
        
        −
        1
      
    
    {\displaystyle 2^{n}-1}
  
, where each digit position is an item from the set of n.

Dixon's identity
Dixon's identity is

  
    
      
        
          ∑
          
            k
            =
            −
            a
          
          
            a
          
        
        (
        −
        1
        
          )
          
            k
          
        
        
          
            
              
                (
              
              
                
                  2
                  a
                
                
                  k
                  +
                  a
                
              
              
                )
              
            
          
          
            3
          
        
        =
        
          
            
              (
              3
              a
              )
              !
            
            
              (
              a
              !
              
                )
                
                  3
                
              
            
          
        
      
    
    {\displaystyle \sum _{k=-a}^{a}(-1)^{k}{2a \choose k+a}^{3}={\frac {(3a)!}{(a!)^{3}}}}
  

or, more generally,

  
    
      
        
          ∑
          
            k
            =
            −
            a
          
          
            a
          
        
        (
        −
        1
        
          )
          
            k
          
        
        
          
            
              (
            
            
              
                a
                +
                b
              
              
                a
                +
                k
              
            
            
              )
            
          
        
        
          
            
              (
            
            
              
                b
                +
                c
              
              
                b
                +
                k
              
            
            
              )
            
          
        
        
          
            
              (
            
            
              
                c
                +
                a
              
              
                c
                +
                k
              
            
            
              )
            
          
        
        =
        
          
            
              (
              a
              +
              b
              +
              c
              )
              !
            
            
              a
              !
              
              b
              !
              
              c
              !
            
          
        
        
        ,
      
    
    {\displaystyle \sum _{k=-a}^{a}(-1)^{k}{a+b \choose a+k}{b+c \choose b+k}{c+a \choose c+k}={\frac {(a+b+c)!}{a!\,b!\,c!}}\,,}
  

where a, b, and c are non-negative integers.

Continuous identities
Certain trigonometric integrals have values expressible in terms of binomial coefficients: For any 
  
    
      
        m
        ,
        n
        ∈
        
          N
        
        ,
      
    
    {\displaystyle m,n\in \mathbb {N} ,}
  

  
    
      
        
          ∫
          
            −
            π
          
          
            π
          
        
        cos
        ⁡
        (
        (
        2
        m
        −
        n
        )
        x
        )
        
          cos
          
            n
          
        
        ⁡
        (
        x
        )
         
        d
        x
        =
        
          
            π
            
              2
              
                n
                −
                1
              
            
          
        
        
          
            
              (
            
            
              n
              m
            
            
              )
            
          
        
      
    
    {\displaystyle \int _{-\pi }^{\pi }\cos((2m-n)x)\cos ^{n}(x)\ dx={\frac {\pi }{2^{n-1}}}{\binom {n}{m}}}
  

  
    
      
        
          ∫
          
            −
            π
          
          
            π
          
        
        sin
        ⁡
        (
        (
        2
        m
        −
        n
        )
        x
        )
        
          sin
          
            n
          
        
        ⁡
        (
        x
        )
         
        d
        x
        =
        
          
            {
            
              
                
                  (
                  −
                  1
                  
                    )
                    
                      m
                      +
                      (
                      n
                      +
                      1
                      )
                      
                        /
                      
                      2
                    
                  
                  
                    
                      π
                      
                        2
                        
                          n
                          −
                          1
                        
                      
                    
                  
                  
                    
                      
                        (
                      
                      
                        n
                        m
                      
                      
                        )
                      
                    
                  
                  ,
                
                
                  n
                  
                     odd
                  
                
              
              
                
                  0
                  ,
                
                
                  
                    otherwise
                  
                
              
            
            
          
        
      
    
    {\displaystyle \int _{-\pi }^{\pi }\sin((2m-n)x)\sin ^{n}(x)\ dx={\begin{cases}(-1)^{m+(n+1)/2}{\frac {\pi }{2^{n-1}}}{\binom {n}{m}},&n{\text{ odd}}\\0,&{\text{otherwise}}\end{cases}}}
  

  
    
      
        
          ∫
          
            −
            π
          
          
            π
          
        
        cos
        ⁡
        (
        (
        2
        m
        −
        n
        )
        x
        )
        
          sin
          
            n
          
        
        ⁡
        (
        x
        )
         
        d
        x
        =
        
          
            {
            
              
                
                  (
                  −
                  1
                  
                    )
                    
                      m
                      +
                      (
                      n
                      
                        /
                      
                      2
                      )
                    
                  
                  
                    
                      π
                      
                        2
                        
                          n
                          −
                          1
                        
                      
                    
                  
                  
                    
                      
                        (
                      
                      
                        n
                        m
                      
                      
                        )
                      
                    
                  
                  ,
                
                
                  n
                  
                     even
                  
                
              
              
                
                  0
                  ,
                
                
                  
                    otherwise
                  
                
              
            
            
          
        
      
    
    {\displaystyle \int _{-\pi }^{\pi }\cos((2m-n)x)\sin ^{n}(x)\ dx={\begin{cases}(-1)^{m+(n/2)}{\frac {\pi }{2^{n-1}}}{\binom {n}{m}},&n{\text{ even}}\\0,&{\text{otherwise}}\end{cases}}}
  

These can be proved by using Euler's formula to convert trigonometric functions to complex exponentials, expanding using the binomial theorem, and integrating term by term.

Congruences
If n is prime, then 
  
    
      
        
          
            
              (
            
            
              
                n
                −
                1
              
              k
            
            
              )
            
          
        
        ≡
        (
        −
        1
        
          )
          
            k
          
        
        
        mod
        
        
        n
      
    
    {\displaystyle {\binom {n-1}{k}}\equiv (-1)^{k}\mod n}
  
 for every k with 
  
    
      
        0
        ≤
        k
        ≤
        n
        −
        1.
      
    
    {\displaystyle 0\leq k\leq n-1.}
  

More generally, this remains true if n is any number and k is such that all the numbers between 1 and k are coprime to n.
Indeed, we have

  
    
      
        
          
            
              (
            
            
              
                n
                −
                1
              
              k
            
            
              )
            
          
        
        =
        
          
            
              (
              n
              −
              1
              )
              (
              n
              −
              2
              )
              ⋯
              (
              n
              −
              k
              )
            
            
              1
              ⋅
              2
              ⋯
              k
            
          
        
        =
        
          ∏
          
            i
            =
            1
          
          
            k
          
        
        
          
            
              n
              −
              i
            
            i
          
        
        ≡
        
          ∏
          
            i
            =
            1
          
          
            k
          
        
        
          
            
              −
              i
            
            i
          
        
        =
        (
        −
        1
        
          )
          
            k
          
        
        
        mod
        
        
        n
        .
      
    
    {\displaystyle {\binom {n-1}{k}}={(n-1)(n-2)\cdots (n-k) \over 1\cdot 2\cdots k}=\prod _{i=1}^{k}{n-i \over i}\equiv \prod _{i=1}^{k}{-i \over i}=(-1)^{k}\mod n.}

Generating functions
Ordinary generating functions
For a fixed n, the ordinary generating function of the sequence 
  
    
      
        
          
            
              
                (
              
              
                n
                0
              
              
                )
              
            
          
        
        ,
        
          
            
              
                (
              
              
                n
                1
              
              
                )
              
            
          
        
        ,
        
          
            
              
                (
              
              
                n
                2
              
              
                )
              
            
          
        
        ,
        …
      
    
    {\displaystyle {\tbinom {n}{0}},{\tbinom {n}{1}},{\tbinom {n}{2}},\ldots }
  
 is

  
    
      
        
          ∑
          
            k
            =
            0
          
          
            ∞
          
        
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        
          x
          
            k
          
        
        =
        (
        1
        +
        x
        
          )
          
            n
          
        
        .
      
    
    {\displaystyle \sum _{k=0}^{\infty }{n \choose k}x^{k}=(1+x)^{n}.}
  

For a fixed k, the ordinary generating function of the sequence 
  
    
      
        
          
            
              
                (
              
              
                0
                k
              
              
                )
              
            
          
        
        ,
        
          
            
              
                (
              
              
                1
                k
              
              
                )
              
            
          
        
        ,
        
          
            
              
                (
              
              
                2
                k
              
              
                )
              
            
          
        
        ,
        …
        ,
      
    
    {\displaystyle {\tbinom {0}{k}},{\tbinom {1}{k}},{\tbinom {2}{k}},\ldots ,}
  
 is

  
    
      
        
          ∑
          
            n
            =
            0
          
          
            ∞
          
        
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        
          y
          
            n
          
        
        =
        
          
            
              y
              
                k
              
            
            
              (
              1
              −
              y
              
                )
                
                  k
                  +
                  1
                
              
            
          
        
        .
      
    
    {\displaystyle \sum _{n=0}^{\infty }{n \choose k}y^{n}={\frac {y^{k}}{(1-y)^{k+1}}}.}
  

The bivariate generating function of the binomial coefficients is

  
    
      
        
          ∑
          
            n
            =
            0
          
          
            ∞
          
        
        
          ∑
          
            k
            =
            0
          
          
            n
          
        
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        
          x
          
            k
          
        
        
          y
          
            n
          
        
        =
        
          
            1
            
              1
              −
              y
              −
              x
              y
            
          
        
        .
      
    
    {\displaystyle \sum _{n=0}^{\infty }\sum _{k=0}^{n}{n \choose k}x^{k}y^{n}={\frac {1}{1-y-xy}}.}
  

A symmetric bivariate generating function of the binomial coefficients is

  
    
      
        
          ∑
          
            n
            =
            0
          
          
            ∞
          
        
        
          ∑
          
            k
            =
            0
          
          
            ∞
          
        
        
          
            
              (
            
            
              
                n
                +
                k
              
              k
            
            
              )
            
          
        
        
          x
          
            k
          
        
        
          y
          
            n
          
        
        =
        
          
            1
            
              1
              −
              x
              −
              y
            
          
        
        .
      
    
    {\displaystyle \sum _{n=0}^{\infty }\sum _{k=0}^{\infty }{n+k \choose k}x^{k}y^{n}={\frac {1}{1-x-y}}.}
  

which is the same as the previous generating function after the substitution 
  
    
      
        x
        →
        x
        y
      
    
    {\displaystyle x\to xy}
  
.

Exponential generating function
A symmetric exponential bivariate generating function of the binomial coefficients is:

  
    
      
        
          ∑
          
            n
            =
            0
          
          
            ∞
          
        
        
          ∑
          
            k
            =
            0
          
          
            ∞
          
        
        
          
            
              (
            
            
              
                n
                +
                k
              
              k
            
            
              )
            
          
        
        
          
            
              
                x
                
                  k
                
              
              
                y
                
                  n
                
              
            
            
              (
              n
              +
              k
              )
              !
            
          
        
        =
        
          e
          
            x
            +
            y
          
        
        .
      
    
    {\displaystyle \sum _{n=0}^{\infty }\sum _{k=0}^{\infty }{n+k \choose k}{\frac {x^{k}y^{n}}{(n+k)!}}=e^{x+y}.}

Divisibility properties
In 1852, Kummer proved that if m and n are nonnegative integers and p is a prime number, then the largest power of p dividing 
  
    
      
        
          
            
              
                (
              
              
                
                  m
                  +
                  n
                
                m
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {m+n}{m}}}
  
 equals pc, where c is the number of carries when m and n are added in base p.
Equivalently, the exponent of a prime p in 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  

equals the number of nonnegative integers j such that the fractional part of k/pj is greater than the fractional part of n/pj. It can be deduced from this that 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
 is divisible by n/gcd(n,k). In particular therefore it follows that p divides 
  
    
      
        
          
            
              
                (
              
              
                
                  p
                  
                    r
                  
                
                s
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {p^{r}}{s}}}
  
 for all positive integers r and s such that s < pr. However this is not true of higher powers of p: for example 9 does not divide 
  
    
      
        
          
            
              
                (
              
              
                9
                6
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {9}{6}}}
  
.
A somewhat surprising result by David Singmaster (1974) is that any integer divides almost all binomial coefficients. More precisely, fix an integer d and let f(N) denote the number of binomial coefficients 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
 with n < N such that d divides 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
. Then

  
    
      
        
          lim
          
            N
            →
            ∞
          
        
        
          
            
              f
              (
              N
              )
            
            
              N
              (
              N
              +
              1
              )
              
                /
              
              2
            
          
        
        =
        1.
      
    
    {\displaystyle \lim _{N\to \infty }{\frac {f(N)}{N(N+1)/2}}=1.}
  

Since the number of binomial coefficients 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
 with n < N is N(N + 1) / 2, this implies that the density of binomial coefficients divisible by d goes to 1.
Binomial coefficients have divisibility properties related to least common multiples of consecutive integers. For example:

  
    
      
        
          
            
              (
            
            
              
                n
                +
                k
              
              k
            
            
              )
            
          
        
      
    
    {\displaystyle {\binom {n+k}{k}}}
  
 divides 
  
    
      
        
          
            
              lcm
              ⁡
              (
              n
              ,
              n
              +
              1
              ,
              …
              ,
              n
              +
              k
              )
            
            n
          
        
      
    
    {\displaystyle {\frac {\operatorname {lcm} (n,n+1,\ldots ,n+k)}{n}}}
  
.

  
    
      
        
          
            
              (
            
            
              
                n
                +
                k
              
              k
            
            
              )
            
          
        
      
    
    {\displaystyle {\binom {n+k}{k}}}
  
 is a multiple of 
  
    
      
        
          
            
              lcm
              ⁡
              (
              n
              ,
              n
              +
              1
              ,
              …
              ,
              n
              +
              k
              )
            
            
              n
              ⋅
              lcm
              ⁡
              (
              
                
                  
                    (
                  
                  
                    k
                    0
                  
                  
                    )
                  
                
              
              ,
              
                
                  
                    (
                  
                  
                    k
                    1
                  
                  
                    )
                  
                
              
              ,
              …
              ,
              
                
                  
                    (
                  
                  
                    k
                    k
                  
                  
                    )
                  
                
              
              )
            
          
        
      
    
    {\displaystyle {\frac {\operatorname {lcm} (n,n+1,\ldots ,n+k)}{n\cdot \operatorname {lcm} ({\binom {k}{0}},{\binom {k}{1}},\ldots ,{\binom {k}{k}})}}}
  
.
Another fact:
An integer n ≥ 2 is prime if and only if
all the intermediate binomial coefficients

  
    
      
        
          
            
              (
            
            
              n
              1
            
            
              )
            
          
        
        ,
        
          
            
              (
            
            
              n
              2
            
            
              )
            
          
        
        ,
        …
        ,
        
          
            
              (
            
            
              n
              
                n
                −
                1
              
            
            
              )
            
          
        
      
    
    {\displaystyle {\binom {n}{1}},{\binom {n}{2}},\ldots ,{\binom {n}{n-1}}}
  

are divisible by n.
Proof:
When p is prime, p divides

  
    
      
        
          
            
              (
            
            
              p
              k
            
            
              )
            
          
        
        =
        
          
            
              p
              ⋅
              (
              p
              −
              1
              )
              ⋯
              (
              p
              −
              k
              +
              1
              )
            
            
              k
              ⋅
              (
              k
              −
              1
              )
              ⋯
              1
            
          
        
      
    
    {\displaystyle {\binom {p}{k}}={\frac {p\cdot (p-1)\cdots (p-k+1)}{k\cdot (k-1)\cdots 1}}}
  
 for all 0 < k < p
because 
  
    
      
        
          
            
              
                (
              
              
                p
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {p}{k}}}
  
 is a natural number and p divides the numerator but not the denominator.
When n is composite, let p be the smallest prime factor of n and let k = n/p. Then 0 < p < n and

  
    
      
        
          
            
              (
            
            
              n
              p
            
            
              )
            
          
        
        =
        
          
            
              n
              (
              n
              −
              1
              )
              (
              n
              −
              2
              )
              ⋯
              (
              n
              −
              p
              +
              1
              )
            
            
              p
              !
            
          
        
        =
        
          
            
              k
              (
              n
              −
              1
              )
              (
              n
              −
              2
              )
              ⋯
              (
              n
              −
              p
              +
              1
              )
            
            
              (
              p
              −
              1
              )
              !
            
          
        
        ≢
        0
        
          
          (
          mod
          
          n
          )
        
      
    
    {\displaystyle {\binom {n}{p}}={\frac {n(n-1)(n-2)\cdots (n-p+1)}{p!}}={\frac {k(n-1)(n-2)\cdots (n-p+1)}{(p-1)!}}\not \equiv 0{\pmod {n}}}
  

otherwise the numerator k(n − 1)(n − 2)⋯(n − p + 1) has to be divisible by n = k×p, this can only be the case when (n − 1)(n − 2)⋯(n − p + 1) is divisible by p. But n is divisible by p, so p does not divide n − 1, n − 2, …, n − p + 1 and because p is prime, we know that p does not divide (n − 1)(n − 2)⋯(n − p + 1) and so the numerator cannot be divisible by n.

Bounds and asymptotic formulas
The following bounds for 
  
    
      
        
          
            
              
                (
              
              
                n
                k
              
              
                )
              
            
          
        
      
    
    {\displaystyle {\tbinom {n}{k}}}
  
 hold for all values of n and k such that 1 ≤ k ≤ n:

  
    
      
        
          
            
              n
              
                k
              
            
            
              k
              
                k
              
            
          
        
        ≤
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        ≤
        
          
            
              n
              
                k
              
            
            
              k
              !
            
          
        
        <
        
          
            (
            
              
                
                  n
                  ⋅
                  e
                
                k
              
            
            )
          
          
            k
          
        
        .
      
    
    {\displaystyle {\frac {n^{k}}{k^{k}}}\leq {n \choose k}\leq {\frac {n^{k}}{k!}}<\left({\frac {n\cdot e}{k}}\right)^{k}.}
  

The first inequality follows from the fact that

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        
          
            n
            k
          
        
        ⋅
        
          
            
              n
              −
              1
            
            
              k
              −
              1
            
          
        
        ⋯
        
          
            
              n
              −
              (
              k
              −
              1
              )
            
            1
          
        
      
    
    {\displaystyle {n \choose k}={\frac {n}{k}}\cdot {\frac {n-1}{k-1}}\cdots {\frac {n-(k-1)}{1}}}
  

and each of these 
  
    
      
        k
      
    
    {\displaystyle k}
  
 terms in this product is 
  
    
      
        ≥
        
          
            n
            k
          
        
      
    
    {\textstyle \geq {\frac {n}{k}}}
  
. A similar argument can be made to show the second inequality. The final strict inequality is equivalent to 
  
    
      
        
          e
          
            k
          
        
        >
        
          k
          
            k
          
        
        
          /
        
        k
        !
      
    
    {\textstyle e^{k}>k^{k}/k!}
  
, that is clear since the RHS is a term of the exponential series 
  
    
      
        
          e
          
            k
          
        
        =
        
          ∑
          
            j
            =
            0
          
          
            ∞
          
        
        
          k
          
            j
          
        
        
          /
        
        j
        !
      
    
    {\textstyle e^{k}=\sum _{j=0}^{\infty }k^{j}/j!}
  
.
From the divisibility properties we can infer that

  
    
      
        
          
            
              lcm
              ⁡
              (
              n
              −
              k
              ,
              …
              ,
              n
              )
            
            
              (
              n
              −
              k
              )
              ⋅
              lcm
              ⁡
              
                (
                
                  
                    
                      
                        (
                      
                      
                        k
                        0
                      
                      
                        )
                      
                    
                  
                  ,
                  …
                  ,
                  
                    
                      
                        (
                      
                      
                        k
                        k
                      
                      
                        )
                      
                    
                  
                
                )
              
            
          
        
        ≤
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        ≤
        
          
            
              lcm
              ⁡
              (
              n
              −
              k
              ,
              …
              ,
              n
              )
            
            
              n
              −
              k
            
          
        
        ,
      
    
    {\displaystyle {\frac {\operatorname {lcm} (n-k,\ldots ,n)}{(n-k)\cdot \operatorname {lcm} \left({\binom {k}{0}},\ldots ,{\binom {k}{k}}\right)}}\leq {\binom {n}{k}}\leq {\frac {\operatorname {lcm} (n-k,\ldots ,n)}{n-k}},}
  

where both equalities can be achieved.
The following bounds are useful in information theory:: 353 

  
    
      
        
          
            1
            
              n
              +
              1
            
          
        
        
          2
          
            n
            H
            (
            k
            
              /
            
            n
            )
          
        
        ≤
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        ≤
        
          2
          
            n
            H
            (
            k
            
              /
            
            n
            )
          
        
      
    
    {\displaystyle {\frac {1}{n+1}}2^{nH(k/n)}\leq {n \choose k}\leq 2^{nH(k/n)}}
  

where 
  
    
      
        H
        (
        p
        )
        =
        −
        p
        
          log
          
            2
          
        
        ⁡
        (
        p
        )
        −
        (
        1
        −
        p
        )
        
          log
          
            2
          
        
        ⁡
        (
        1
        −
        p
        )
      
    
    {\displaystyle H(p)=-p\log _{2}(p)-(1-p)\log _{2}(1-p)}
  
 is the binary entropy function. It can be further tightened to

  
    
      
        
          
            
              n
              
                8
                k
                (
                n
                −
                k
                )
              
            
          
        
        
          2
          
            n
            H
            (
            k
            
              /
            
            n
            )
          
        
        ≤
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        ≤
        
          
            
              n
              
                2
                π
                k
                (
                n
                −
                k
                )
              
            
          
        
        
          2
          
            n
            H
            (
            k
            
              /
            
            n
            )
          
        
      
    
    {\displaystyle {\sqrt {\frac {n}{8k(n-k)}}}2^{nH(k/n)}\leq {n \choose k}\leq {\sqrt {\frac {n}{2\pi k(n-k)}}}2^{nH(k/n)}}
  

for all 
  
    
      
        1
        ≤
        k
        ≤
        n
        −
        1
      
    
    {\displaystyle 1\leq k\leq n-1}
  
.: 309

Both n and k large
Stirling's approximation yields the following approximation, valid when 
  
    
      
        n
        −
        k
        ,
        k
      
    
    {\displaystyle n-k,k}
  
 both tend to infinity:

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        ∼
        
          
            
              n
              
                2
                π
                k
                (
                n
                −
                k
                )
              
            
          
        
        ⋅
        
          
            
              n
              
                n
              
            
            
              
                k
                
                  k
                
              
              (
              n
              −
              k
              
                )
                
                  n
                  −
                  k
                
              
            
          
        
      
    
    {\displaystyle {n \choose k}\sim {\sqrt {n \over 2\pi k(n-k)}}\cdot {n^{n} \over k^{k}(n-k)^{n-k}}}
  

Because the inequality forms of Stirling's formula also bound the factorials, slight variants on the above asymptotic approximation give exact bounds.
In particular, when 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is sufficiently large, one has

  
    
      
        
          
            
              (
            
            
              
                2
                n
              
              n
            
            
              )
            
          
        
        ∼
        
          
            
              2
              
                2
                n
              
            
            
              n
              π
            
          
        
      
    
    {\displaystyle {2n \choose n}\sim {\frac {2^{2n}}{\sqrt {n\pi }}}}
  
 and 
  
    
      
        
          
            n
          
        
        
          
            
              (
            
            
              
                2
                n
              
              n
            
            
              )
            
          
        
        ≥
        
          2
          
            2
            n
            −
            1
          
        
      
    
    {\displaystyle {\sqrt {n}}{2n \choose n}\geq 2^{2n-1}}
  
. More generally, for m ≥ 2 and n ≥ 1 (again, by applying Stirling's formula to the factorials in the binomial coefficient),

  
    
      
        
          
            n
          
        
        
          
            
              (
            
            
              
                m
                n
              
              n
            
            
              )
            
          
        
        ≥
        
          
            
              m
              
                m
                (
                n
                −
                1
                )
                +
                1
              
            
            
              (
              m
              −
              1
              
                )
                
                  (
                  m
                  −
                  1
                  )
                  (
                  n
                  −
                  1
                  )
                
              
            
          
        
        .
      
    
    {\displaystyle {\sqrt {n}}{mn \choose n}\geq {\frac {m^{m(n-1)+1}}{(m-1)^{(m-1)(n-1)}}}.}
  

If n is large and k is linear in n, various precise asymptotic estimates exist for the binomial coefficient 
  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
      
    
    {\textstyle {\binom {n}{k}}}
  
. For example, if 
  
    
      
        
          |
        
        n
        
          /
        
        2
        −
        k
        
          |
        
        =
        o
        (
        
          n
          
            2
            
              /
            
            3
          
        
        )
      
    
    {\displaystyle |n/2-k|=o(n^{2/3})}
  
 then

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        ∼
        
          
            
              (
            
            
              n
              
                n
                2
              
            
            
              )
            
          
        
        
          e
          
            −
            
              d
              
                2
              
            
            
              /
            
            (
            2
            n
            )
          
        
        ∼
        
          
            
              2
              
                n
              
            
            
              
                
                  1
                  2
                
              
              n
              π
            
          
        
        
          e
          
            −
            
              d
              
                2
              
            
            
              /
            
            (
            2
            n
            )
          
        
      
    
    {\displaystyle {\binom {n}{k}}\sim {\binom {n}{\frac {n}{2}}}e^{-d^{2}/(2n)}\sim {\frac {2^{n}}{\sqrt {{\frac {1}{2}}n\pi }}}e^{-d^{2}/(2n)}}
  

where d = n − 2k.

n much larger than k
If n is large and k is o(n) (that is, if  k/n → 0), then

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        ∼
        
          
            (
            
              
                
                  n
                  e
                
                k
              
            
            )
          
          
            k
          
        
        ⋅
        (
        2
        π
        k
        
          )
          
            −
            1
            
              /
            
            2
          
        
        ⋅
        exp
        ⁡
        
          (
          
            −
            
              
                
                  k
                  
                    2
                  
                
                
                  2
                  n
                
              
            
            (
            1
            +
            o
            (
            1
            )
            )
          
          )
        
      
    
    {\displaystyle {\binom {n}{k}}\sim \left({\frac {ne}{k}}\right)^{k}\cdot (2\pi k)^{-1/2}\cdot \exp \left(-{\frac {k^{2}}{2n}}(1+o(1))\right)}
  

where again o is the little o notation.

Sums of binomial coefficients
A simple and rough upper bound for the sum of binomial coefficients can be obtained using the binomial theorem:

  
    
      
        
          ∑
          
            i
            =
            0
          
          
            k
          
        
        
          
            
              (
            
            
              n
              i
            
            
              )
            
          
        
        ≤
        
          ∑
          
            i
            =
            0
          
          
            k
          
        
        
          n
          
            i
          
        
        ⋅
        
          1
          
            k
            −
            i
          
        
        ≤
        (
        1
        +
        n
        
          )
          
            k
          
        
      
    
    {\displaystyle \sum _{i=0}^{k}{n \choose i}\leq \sum _{i=0}^{k}n^{i}\cdot 1^{k-i}\leq (1+n)^{k}}
  

More precise bounds are given by

  
    
      
        
          
            1
            
              8
              n
              ε
              (
              1
              −
              ε
              )
            
          
        
        ⋅
        
          2
          
            H
            (
            ε
            )
            ⋅
            n
          
        
        ≤
        
          ∑
          
            i
            =
            0
          
          
            k
          
        
        
          
            
              (
            
            
              n
              i
            
            
              )
            
          
        
        ≤
        
          2
          
            H
            (
            ε
            )
            ⋅
            n
          
        
        ,
      
    
    {\displaystyle {\frac {1}{\sqrt {8n\varepsilon (1-\varepsilon )}}}\cdot 2^{H(\varepsilon )\cdot n}\leq \sum _{i=0}^{k}{\binom {n}{i}}\leq 2^{H(\varepsilon )\cdot n},}
  

valid for all integers 
  
    
      
        n
        >
        k
        ≥
        1
      
    
    {\displaystyle n>k\geq 1}
  
 with 
  
    
      
        ε
        ≐
        k
        
          /
        
        n
        ≤
        1
        
          /
        
        2
      
    
    {\displaystyle \varepsilon \doteq k/n\leq 1/2}
  
.

Generalized binomial coefficients
The infinite product formula for the gamma function also gives an expression for binomial coefficients

  
    
      
        (
        −
        1
        
          )
          
            k
          
        
        
          
            
              (
            
            
              z
              k
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              
                −
                z
                +
                k
                −
                1
              
              k
            
            
              )
            
          
        
        =
        
          
            1
            
              Γ
              (
              −
              z
              )
            
          
        
        
          
            1
            
              (
              k
              +
              1
              
                )
                
                  z
                  +
                  1
                
              
            
          
        
        
          ∏
          
            j
            =
            k
            +
            1
          
        
        
          
            
              
                (
                
                  1
                  +
                  
                    
                      1
                      j
                    
                  
                
                )
              
              
                −
                z
                −
                1
              
            
            
              1
              −
              
                
                  
                    z
                    +
                    1
                  
                  j
                
              
            
          
        
      
    
    {\displaystyle (-1)^{k}{z \choose k}={-z+k-1 \choose k}={\frac {1}{\Gamma (-z)}}{\frac {1}{(k+1)^{z+1}}}\prod _{j=k+1}{\frac {\left(1+{\frac {1}{j}}\right)^{-z-1}}{1-{\frac {z+1}{j}}}}}
  

which yields the asymptotic formulas

  
    
      
        
          
            
              (
            
            
              z
              k
            
            
              )
            
          
        
        ≈
        
          
            
              (
              −
              1
              
                )
                
                  k
                
              
            
            
              Γ
              (
              −
              z
              )
              
                k
                
                  z
                  +
                  1
                
              
            
          
        
        
        
          and
        
        
        
          
            
              (
            
            
              
                z
                +
                k
              
              k
            
            
              )
            
          
        
        =
        
          
            
              k
              
                z
              
            
            
              Γ
              (
              z
              +
              1
              )
            
          
        
        
          (
          
            1
            +
            
              
                
                  z
                  (
                  z
                  +
                  1
                  )
                
                
                  2
                  k
                
              
            
            +
            
              
                O
              
            
            
              (
              
                k
                
                  −
                  2
                
              
              )
            
          
          )
        
      
    
    {\displaystyle {z \choose k}\approx {\frac {(-1)^{k}}{\Gamma (-z)k^{z+1}}}\qquad {\text{and}}\qquad {z+k \choose k}={\frac {k^{z}}{\Gamma (z+1)}}\left(1+{\frac {z(z+1)}{2k}}+{\mathcal {O}}\left(k^{-2}\right)\right)}
  

as 
  
    
      
        k
        →
        ∞
      
    
    {\displaystyle k\to \infty }
  
.
This asymptotic behaviour is contained in the approximation

  
    
      
        
          
            
              (
            
            
              
                z
                +
                k
              
              k
            
            
              )
            
          
        
        ≈
        
          
            
              e
              
                z
                (
                
                  H
                  
                    k
                  
                
                −
                γ
                )
              
            
            
              Γ
              (
              z
              +
              1
              )
            
          
        
      
    
    {\displaystyle {z+k \choose k}\approx {\frac {e^{z(H_{k}-\gamma )}}{\Gamma (z+1)}}}
  

as well. (Here 
  
    
      
        
          H
          
            k
          
        
      
    
    {\displaystyle H_{k}}
  
 is the k-th harmonic number and 
  
    
      
        γ
      
    
    {\displaystyle \gamma }
  
 is the Euler–Mascheroni constant.)
Further, the asymptotic formula

  
    
      
        
          
            
              
                (
              
              
                
                  z
                  +
                  k
                
                j
              
              
                )
              
            
            
              
                (
              
              
                k
                j
              
              
                )
              
            
          
        
        →
        
          
            (
            
              1
              −
              
                
                  j
                  k
                
              
            
            )
          
          
            −
            z
          
        
        
        
          and
        
        
        
          
            
              
                (
              
              
                j
                
                  j
                  −
                  k
                
              
              
                )
              
            
            
              
                (
              
              
                
                  j
                  −
                  z
                
                
                  j
                  −
                  k
                
              
              
                )
              
            
          
        
        →
        
          
            (
            
              
                j
                k
              
            
            )
          
          
            z
          
        
      
    
    {\displaystyle {\frac {z+k \choose j}{k \choose j}}\to \left(1-{\frac {j}{k}}\right)^{-z}\quad {\text{and}}\quad {\frac {j \choose j-k}{j-z \choose j-k}}\to \left({\frac {j}{k}}\right)^{z}}
  

hold true, whenever 
  
    
      
        k
        →
        ∞
      
    
    {\displaystyle k\to \infty }
  
 and 
  
    
      
        j
        
          /
        
        k
        →
        x
      
    
    {\displaystyle j/k\to x}
  
 for some complex number 
  
    
      
        x
      
    
    {\displaystyle x}
  
.

Generalizations
Generalization to multinomials
Binomial coefficients can be generalized to multinomial coefficients defined to be the number:

  
    
      
        
          
            
              (
            
            
              n
              
                
                  k
                  
                    1
                  
                
                ,
                
                  k
                  
                    2
                  
                
                ,
                …
                ,
                
                  k
                  
                    r
                  
                
              
            
            
              )
            
          
        
        =
        
          
            
              n
              !
            
            
              
                k
                
                  1
                
              
              !
              
                k
                
                  2
                
              
              !
              ⋯
              
                k
                
                  r
                
              
              !
            
          
        
      
    
    {\displaystyle {n \choose k_{1},k_{2},\ldots ,k_{r}}={\frac {n!}{k_{1}!k_{2}!\cdots k_{r}!}}}
  

where

  
    
      
        
          ∑
          
            i
            =
            1
          
          
            r
          
        
        
          k
          
            i
          
        
        =
        n
        .
      
    
    {\displaystyle \sum _{i=1}^{r}k_{i}=n.}
  

While the binomial coefficients represent the coefficients of (x + y)n, the multinomial coefficients
represent the coefficients of the polynomial

  
    
      
        (
        
          x
          
            1
          
        
        +
        
          x
          
            2
          
        
        +
        ⋯
        +
        
          x
          
            r
          
        
        
          )
          
            n
          
        
        .
      
    
    {\displaystyle (x_{1}+x_{2}+\cdots +x_{r})^{n}.}
  

The case r = 2 gives binomial coefficients:

  
    
      
        
          
            
              (
            
            
              n
              
                
                  k
                  
                    1
                  
                
                ,
                
                  k
                  
                    2
                  
                
              
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              n
              
                
                  k
                  
                    1
                  
                
                ,
                n
                −
                
                  k
                  
                    1
                  
                
              
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              n
              
                k
                
                  1
                
              
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              n
              
                k
                
                  2
                
              
            
            
              )
            
          
        
        .
      
    
    {\displaystyle {n \choose k_{1},k_{2}}={n \choose k_{1},n-k_{1}}={n \choose k_{1}}={n \choose k_{2}}.}
  

The combinatorial interpretation of multinomial coefficients is distribution of n distinguishable elements over r (distinguishable) containers, each containing exactly ki elements, where i is the index of the container.
Multinomial coefficients have many properties similar to those of binomial coefficients, for example the recurrence relation:

  
    
      
        
          
            
              (
            
            
              n
              
                
                  k
                  
                    1
                  
                
                ,
                
                  k
                  
                    2
                  
                
                ,
                …
                ,
                
                  k
                  
                    r
                  
                
              
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              
                n
                −
                1
              
              
                
                  k
                  
                    1
                  
                
                −
                1
                ,
                
                  k
                  
                    2
                  
                
                ,
                …
                ,
                
                  k
                  
                    r
                  
                
              
            
            
              )
            
          
        
        +
        
          
            
              (
            
            
              
                n
                −
                1
              
              
                
                  k
                  
                    1
                  
                
                ,
                
                  k
                  
                    2
                  
                
                −
                1
                ,
                …
                ,
                
                  k
                  
                    r
                  
                
              
            
            
              )
            
          
        
        +
        …
        +
        
          
            
              (
            
            
              
                n
                −
                1
              
              
                
                  k
                  
                    1
                  
                
                ,
                
                  k
                  
                    2
                  
                
                ,
                …
                ,
                
                  k
                  
                    r
                  
                
                −
                1
              
            
            
              )
            
          
        
      
    
    {\displaystyle {n \choose k_{1},k_{2},\ldots ,k_{r}}={n-1 \choose k_{1}-1,k_{2},\ldots ,k_{r}}+{n-1 \choose k_{1},k_{2}-1,\ldots ,k_{r}}+\ldots +{n-1 \choose k_{1},k_{2},\ldots ,k_{r}-1}}
  

and symmetry:

  
    
      
        
          
            
              (
            
            
              n
              
                
                  k
                  
                    1
                  
                
                ,
                
                  k
                  
                    2
                  
                
                ,
                …
                ,
                
                  k
                  
                    r
                  
                
              
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              n
              
                
                  k
                  
                    
                      σ
                      
                        1
                      
                    
                  
                
                ,
                
                  k
                  
                    
                      σ
                      
                        2
                      
                    
                  
                
                ,
                …
                ,
                
                  k
                  
                    
                      σ
                      
                        r
                      
                    
                  
                
              
            
            
              )
            
          
        
      
    
    {\displaystyle {n \choose k_{1},k_{2},\ldots ,k_{r}}={n \choose k_{\sigma _{1}},k_{\sigma _{2}},\ldots ,k_{\sigma _{r}}}}
  

where 
  
    
      
        (
        
          σ
          
            i
          
        
        )
      
    
    {\displaystyle (\sigma _{i})}
  
 is a permutation of (1, 2, ..., r).

Taylor series
Using Stirling numbers of the first kind the series expansion around any arbitrarily chosen point 
  
    
      
        
          z
          
            0
          
        
      
    
    {\displaystyle z_{0}}
  
 is

  
    
      
        
          
            
              
                
                  
                    
                      (
                    
                    
                      z
                      k
                    
                    
                      )
                    
                  
                
                =
                
                  
                    1
                    
                      k
                      !
                    
                  
                
                
                  ∑
                  
                    i
                    =
                    0
                  
                  
                    k
                  
                
                
                  z
                  
                    i
                  
                
                
                  s
                  
                    k
                    ,
                    i
                  
                
              
              
                
                =
                
                  ∑
                  
                    i
                    =
                    0
                  
                  
                    k
                  
                
                (
                z
                −
                
                  z
                  
                    0
                  
                
                
                  )
                  
                    i
                  
                
                
                  ∑
                  
                    j
                    =
                    i
                  
                  
                    k
                  
                
                
                  
                    
                      (
                    
                    
                      
                        z
                        
                          0
                        
                      
                      
                        j
                        −
                        i
                      
                    
                    
                      )
                    
                  
                
                
                  
                    
                      s
                      
                        k
                        +
                        i
                        −
                        j
                        ,
                        i
                      
                    
                    
                      (
                      k
                      +
                      i
                      −
                      j
                      )
                      !
                    
                  
                
              
            
            
              
              
                
                =
                
                  ∑
                  
                    i
                    =
                    0
                  
                  
                    k
                  
                
                (
                z
                −
                
                  z
                  
                    0
                  
                
                
                  )
                  
                    i
                  
                
                
                  ∑
                  
                    j
                    =
                    i
                  
                  
                    k
                  
                
                
                  z
                  
                    0
                  
                  
                    j
                    −
                    i
                  
                
                
                  
                    
                      (
                    
                    
                      j
                      i
                    
                    
                      )
                    
                  
                
                
                  
                    
                      s
                      
                        k
                        ,
                        j
                      
                    
                    
                      k
                      !
                    
                  
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{z \choose k}={\frac {1}{k!}}\sum _{i=0}^{k}z^{i}s_{k,i}&=\sum _{i=0}^{k}(z-z_{0})^{i}\sum _{j=i}^{k}{z_{0} \choose j-i}{\frac {s_{k+i-j,i}}{(k+i-j)!}}\\&=\sum _{i=0}^{k}(z-z_{0})^{i}\sum _{j=i}^{k}z_{0}^{j-i}{j \choose i}{\frac {s_{k,j}}{k!}}.\end{aligned}}}

Binomial coefficient with n = 1/2
The definition of the binomial coefficients can be extended to the case where 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is real and 
  
    
      
        k
      
    
    {\displaystyle k}
  
 is integer.
In particular, the following identity holds for any non-negative integer 
  
    
      
        k
      
    
    {\displaystyle k}
  
:

  
    
      
        
          
            
              (
            
            
              
                1
                
                  /
                
                2
              
              
                k
              
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              
                2
                k
              
              
                k
              
            
            
              )
            
          
        
        
          
            
              (
              −
              1
              
                )
                
                  k
                  +
                  1
                
              
            
            
              
                2
                
                  2
                  k
                
              
              (
              2
              k
              −
              1
              )
            
          
        
        .
      
    
    {\displaystyle {{1/2} \choose {k}}={{2k} \choose {k}}{\frac {(-1)^{k+1}}{2^{2k}(2k-1)}}.}
  

This shows up when expanding 
  
    
      
        
          
            1
            +
            x
          
        
      
    
    {\displaystyle {\sqrt {1+x}}}
  
 into a power series using the Newton binomial series :

  
    
      
        
          
            1
            +
            x
          
        
        =
        
          ∑
          
            k
            ≥
            0
          
        
        
          
            
              (
            
            
              
                1
                
                  /
                
                2
              
              k
            
            
              )
            
          
        
        
          x
          
            k
          
        
        .
      
    
    {\displaystyle {\sqrt {1+x}}=\sum _{k\geq 0}{\binom {1/2}{k}}x^{k}.}

Products of binomial coefficients
One can express the product of two binomial coefficients as a linear combination of binomial coefficients:

  
    
      
        
          
            
              (
            
            
              z
              m
            
            
              )
            
          
        
        
          
            
              (
            
            
              z
              n
            
            
              )
            
          
        
        =
        
          ∑
          
            k
            =
            0
          
          
            min
            (
            m
            ,
            n
            )
          
        
        
          
            
              (
            
            
              
                m
                +
                n
                −
                k
              
              
                k
                ,
                m
                −
                k
                ,
                n
                −
                k
              
            
            
              )
            
          
        
        
          
            
              (
            
            
              z
              
                m
                +
                n
                −
                k
              
            
            
              )
            
          
        
        ,
      
    
    {\displaystyle {z \choose m}{z \choose n}=\sum _{k=0}^{\min(m,n)}{m+n-k \choose k,m-k,n-k}{z \choose m+n-k},}
  

where the connection coefficients are multinomial coefficients. In terms of labelled combinatorial objects, the connection coefficients represent the number of ways to assign m + n − k labels to a pair of labelled combinatorial objects—of weight m and n respectively—that have had their first k labels identified, or glued together to get a new labelled combinatorial object of weight m + n − k. (That is, to separate the labels into three portions to apply to the glued part, the unglued part of the first object, and the unglued part of the second object.) In this regard, binomial coefficients are to exponential generating series what falling factorials are to ordinary generating series.
The product of all binomial coefficients in the nth row of the Pascal triangle is given by the formula:

  
    
      
        
          ∏
          
            k
            =
            0
          
          
            n
          
        
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        
          ∏
          
            k
            =
            1
          
          
            n
          
        
        
          k
          
            2
            k
            −
            n
            −
            1
          
        
        .
      
    
    {\displaystyle \prod _{k=0}^{n}{\binom {n}{k}}=\prod _{k=1}^{n}k^{2k-n-1}.}

Partial fraction decomposition
The partial fraction decomposition of the reciprocal is given by

  
    
      
        
          
            1
            
              
                (
              
              
                z
                n
              
              
                )
              
            
          
        
        =
        
          ∑
          
            i
            =
            0
          
          
            n
            −
            1
          
        
        (
        −
        1
        
          )
          
            n
            −
            1
            −
            i
          
        
        
          
            
              (
            
            
              n
              i
            
            
              )
            
          
        
        
          
            
              n
              −
              i
            
            
              z
              −
              i
            
          
        
        ,
        
        
          
            1
            
              
                (
              
              
                
                  z
                  +
                  n
                
                n
              
              
                )
              
            
          
        
        =
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        (
        −
        1
        
          )
          
            i
            −
            1
          
        
        
          
            
              (
            
            
              n
              i
            
            
              )
            
          
        
        
          
            i
            
              z
              +
              i
            
          
        
        .
      
    
    {\displaystyle {\frac {1}{z \choose n}}=\sum _{i=0}^{n-1}(-1)^{n-1-i}{n \choose i}{\frac {n-i}{z-i}},\qquad {\frac {1}{z+n \choose n}}=\sum _{i=1}^{n}(-1)^{i-1}{n \choose i}{\frac {i}{z+i}}.}

Newton's binomial series
Newton's binomial series, named after Sir Isaac Newton, is a generalization of the binomial theorem to infinite series:

  
    
      
        (
        1
        +
        z
        
          )
          
            α
          
        
        =
        
          ∑
          
            n
            =
            0
          
          
            ∞
          
        
        
          
            
              (
            
            
              α
              n
            
            
              )
            
          
        
        
          z
          
            n
          
        
        =
        1
        +
        
          
            
              (
            
            
              α
              1
            
            
              )
            
          
        
        z
        +
        
          
            
              (
            
            
              α
              2
            
            
              )
            
          
        
        
          z
          
            2
          
        
        +
        ⋯
        .
      
    
    {\displaystyle (1+z)^{\alpha }=\sum _{n=0}^{\infty }{\alpha  \choose n}z^{n}=1+{\alpha  \choose 1}z+{\alpha  \choose 2}z^{2}+\cdots .}
  

The identity can be obtained by showing that both sides satisfy the differential equation (1 + z) f'(z) = α f(z).
The radius of convergence of this series is 1. An alternative expression is

  
    
      
        
          
            1
            
              (
              1
              −
              z
              
                )
                
                  α
                  +
                  1
                
              
            
          
        
        =
        
          ∑
          
            n
            =
            0
          
          
            ∞
          
        
        
          
            
              (
            
            
              
                n
                +
                α
              
              n
            
            
              )
            
          
        
        
          z
          
            n
          
        
      
    
    {\displaystyle {\frac {1}{(1-z)^{\alpha +1}}}=\sum _{n=0}^{\infty }{n+\alpha  \choose n}z^{n}}
  

where the identity

  
    
      
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        =
        (
        −
        1
        
          )
          
            k
          
        
        
          
            
              (
            
            
              
                k
                −
                n
                −
                1
              
              k
            
            
              )
            
          
        
      
    
    {\displaystyle {n \choose k}=(-1)^{k}{k-n-1 \choose k}}
  

is applied.

Multiset (rising) binomial coefficient
Binomial coefficients count subsets of prescribed size from a given set. A related combinatorial problem is to count multisets of prescribed size with elements drawn from a given set, that is, to count the number of ways to select a certain number of elements from a given set with the possibility of selecting the same element repeatedly. The resulting numbers are called multiset coefficients; the number of ways to "multichoose" (i.e., choose with replacement) k items from an n element set is denoted 
  
    
      
        
          (
          
            
            
            
              
                
                  (
                
                
                  n
                  k
                
                
                  )
                
              
            
            
            
          
          )
        
      
    
    {\textstyle \left(\!\!{\binom {n}{k}}\!\!\right)}
  
.
To avoid ambiguity and confusion with n's main denotation in this article, let f = n = r + (k − 1) and r = f − (k − 1).
Multiset coefficients may be expressed in terms of binomial coefficients by the rule

  
    
      
        
          
            
              (
            
            
              f
              k
            
            
              )
            
          
        
        =
        
          (
          
            
            
            
              
                
                  (
                
                
                  r
                  k
                
                
                  )
                
              
            
            
            
          
          )
        
        =
        
          
            
              (
            
            
              
                r
                +
                k
                −
                1
              
              k
            
            
              )
            
          
        
        .
      
    
    {\displaystyle {\binom {f}{k}}=\left(\!\!{\binom {r}{k}}\!\!\right)={\binom {r+k-1}{k}}.}
  

One possible alternative characterization of this identity is as follows:
We may define the falling factorial as

  
    
      
        (
        f
        
          )
          
            k
          
        
        =
        
          f
          
            
              k
              _
            
          
        
        =
        (
        f
        −
        k
        +
        1
        )
        ⋯
        (
        f
        −
        3
        )
        ⋅
        (
        f
        −
        2
        )
        ⋅
        (
        f
        −
        1
        )
        ⋅
        f
        ,
      
    
    {\displaystyle (f)_{k}=f^{\underline {k}}=(f-k+1)\cdots (f-3)\cdot (f-2)\cdot (f-1)\cdot f,}
  

and the corresponding rising factorial as

  
    
      
        
          r
          
            (
            k
            )
          
        
        =
        
        
          r
          
            
              k
              ¯
            
          
        
        =
        
        r
        ⋅
        (
        r
        +
        1
        )
        ⋅
        (
        r
        +
        2
        )
        ⋅
        (
        r
        +
        3
        )
        ⋯
        (
        r
        +
        k
        −
        1
        )
        ;
      
    
    {\displaystyle r^{(k)}=\,r^{\overline {k}}=\,r\cdot (r+1)\cdot (r+2)\cdot (r+3)\cdots (r+k-1);}
  

so, for example,

  
    
      
        17
        ⋅
        18
        ⋅
        19
        ⋅
        20
        ⋅
        21
        =
        (
        21
        
          )
          
            5
          
        
        =
        
          21
          
            
              5
              _
            
          
        
        =
        
          17
          
            
              5
              ¯
            
          
        
        =
        
          17
          
            (
            5
            )
          
        
        .
      
    
    {\displaystyle 17\cdot 18\cdot 19\cdot 20\cdot 21=(21)_{5}=21^{\underline {5}}=17^{\overline {5}}=17^{(5)}.}
  

Then the binomial coefficients may be written as

  
    
      
        
          
            
              (
            
            
              f
              k
            
            
              )
            
          
        
        =
        
          
            
              (
              f
              
                )
                
                  k
                
              
            
            
              k
              !
            
          
        
        =
        
          
            
              (
              f
              −
              k
              +
              1
              )
              ⋯
              (
              f
              −
              2
              )
              ⋅
              (
              f
              −
              1
              )
              ⋅
              f
            
            
              1
              ⋅
              2
              ⋅
              3
              ⋅
              4
              ⋅
              5
              ⋯
              k
            
          
        
        ,
      
    
    {\displaystyle {\binom {f}{k}}={\frac {(f)_{k}}{k!}}={\frac {(f-k+1)\cdots (f-2)\cdot (f-1)\cdot f}{1\cdot 2\cdot 3\cdot 4\cdot 5\cdots k}},}
  

while the corresponding multiset coefficient is defined by replacing the falling with the rising factorial:

  
    
      
        
          (
          
            
            
            
              
                
                  (
                
                
                  r
                  k
                
                
                  )
                
              
            
            
            
          
          )
        
        =
        
          
            
              r
              
                (
                k
                )
              
            
            
              k
              !
            
          
        
        =
        
          
            
              r
              ⋅
              (
              r
              +
              1
              )
              ⋅
              (
              r
              +
              2
              )
              ⋯
              (
              r
              +
              k
              −
              1
              )
            
            
              1
              ⋅
              2
              ⋅
              3
              ⋅
              4
              ⋅
              5
              ⋯
              k
            
          
        
        .
      
    
    {\displaystyle \left(\!\!{\binom {r}{k}}\!\!\right)={\frac {r^{(k)}}{k!}}={\frac {r\cdot (r+1)\cdot (r+2)\cdots (r+k-1)}{1\cdot 2\cdot 3\cdot 4\cdot 5\cdots k}}.}

Generalization to negative integers n
For any n,

  
    
      
        
          
            
              
                
                  
                    
                      (
                    
                    
                      
                        −
                        n
                      
                      k
                    
                    
                      )
                    
                  
                
              
              
                
                =
                
                  
                    
                      −
                      n
                      ⋅
                      −
                      (
                      n
                      +
                      1
                      )
                      ⋯
                      −
                      (
                      n
                      +
                      k
                      −
                      2
                      )
                      ⋅
                      −
                      (
                      n
                      +
                      k
                      −
                      1
                      )
                    
                    
                      k
                      !
                    
                  
                
              
            
            
              
              
                
                =
                (
                −
                1
                
                  )
                  
                    k
                  
                
                
                
                  
                    
                      n
                      ⋅
                      (
                      n
                      +
                      1
                      )
                      ⋅
                      (
                      n
                      +
                      2
                      )
                      ⋯
                      (
                      n
                      +
                      k
                      −
                      1
                      )
                    
                    
                      k
                      !
                    
                  
                
              
            
            
              
              
                
                =
                (
                −
                1
                
                  )
                  
                    k
                  
                
                
                  
                    
                      (
                    
                    
                      
                        n
                        +
                        k
                        −
                        1
                      
                      k
                    
                    
                      )
                    
                  
                
              
            
            
              
              
                
                =
                (
                −
                1
                
                  )
                  
                    k
                  
                
                
                  (
                  
                    
                    
                    
                      
                        
                          (
                        
                        
                          n
                          k
                        
                        
                          )
                        
                      
                    
                    
                    
                  
                  )
                
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\binom {-n}{k}}&={\frac {-n\cdot -(n+1)\dots -(n+k-2)\cdot -(n+k-1)}{k!}}\\&=(-1)^{k}\;{\frac {n\cdot (n+1)\cdot (n+2)\cdots (n+k-1)}{k!}}\\&=(-1)^{k}{\binom {n+k-1}{k}}\\&=(-1)^{k}\left(\!\!{\binom {n}{k}}\!\!\right)\;.\end{aligned}}}
  

In particular, binomial coefficients evaluated at negative integers n are given by signed multiset coefficients. In the special case 
  
    
      
        n
        =
        −
        1
      
    
    {\displaystyle n=-1}
  
, this reduces to 
  
    
      
        (
        −
        1
        
          )
          
            k
          
        
        =
        
          
            
              (
            
            
              
                −
                1
              
              k
            
            
              )
            
          
        
        =
        
          (
          
            
            
            
              
                
                  (
                
                
                  
                    −
                    k
                  
                  k
                
                
                  )
                
              
            
            
            
          
          )
        
        .
      
    
    {\displaystyle (-1)^{k}={\binom {-1}{k}}=\left(\!\!{\binom {-k}{k}}\!\!\right).}
  

For example, if n = −4 and k = 7, then r = 4 and f = 10:

  
    
      
        
          
            
              
                
                  
                    
                      (
                    
                    
                      
                        −
                        4
                      
                      7
                    
                    
                      )
                    
                  
                
              
              
                
                =
                
                  
                    
                      −
                      10
                      ⋅
                      −
                      9
                      ⋅
                      −
                      8
                      ⋅
                      −
                      7
                      ⋅
                      −
                      6
                      ⋅
                      −
                      5
                      ⋅
                      −
                      4
                    
                    
                      1
                      ⋅
                      2
                      ⋅
                      3
                      ⋅
                      4
                      ⋅
                      5
                      ⋅
                      6
                      ⋅
                      7
                    
                  
                
              
            
            
              
              
                
                =
                (
                −
                1
                
                  )
                  
                    7
                  
                
                
                
                  
                    
                      4
                      ⋅
                      5
                      ⋅
                      6
                      ⋅
                      7
                      ⋅
                      8
                      ⋅
                      9
                      ⋅
                      10
                    
                    
                      1
                      ⋅
                      2
                      ⋅
                      3
                      ⋅
                      4
                      ⋅
                      5
                      ⋅
                      6
                      ⋅
                      7
                    
                  
                
              
            
            
              
              
                
                =
                
                  (
                  
                    
                    
                    
                      
                        
                          (
                        
                        
                          
                            −
                            7
                          
                          7
                        
                        
                          )
                        
                      
                    
                    
                    
                  
                  )
                
                
                  (
                  
                    
                    
                    
                      
                        
                          (
                        
                        
                          4
                          7
                        
                        
                          )
                        
                      
                    
                    
                    
                  
                  )
                
                =
                
                  
                    
                      (
                    
                    
                      
                        −
                        1
                      
                      7
                    
                    
                      )
                    
                  
                
                
                  
                    
                      (
                    
                    
                      10
                      7
                    
                    
                      )
                    
                  
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\binom {-4}{7}}&={\frac {-10\cdot -9\cdot -8\cdot -7\cdot -6\cdot -5\cdot -4}{1\cdot 2\cdot 3\cdot 4\cdot 5\cdot 6\cdot 7}}\\&=(-1)^{7}\;{\frac {4\cdot 5\cdot 6\cdot 7\cdot 8\cdot 9\cdot 10}{1\cdot 2\cdot 3\cdot 4\cdot 5\cdot 6\cdot 7}}\\&=\left(\!\!{\binom {-7}{7}}\!\!\right)\left(\!\!{\binom {4}{7}}\!\!\right)={\binom {-1}{7}}{\binom {10}{7}}.\end{aligned}}}

Two real or complex valued arguments
The binomial coefficient is generalized to two real or complex valued arguments using the gamma function or beta function via

  
    
      
        
          
            
              (
            
            
              x
              y
            
            
              )
            
          
        
        =
        
          
            
              Γ
              (
              x
              +
              1
              )
            
            
              Γ
              (
              y
              +
              1
              )
              Γ
              (
              x
              −
              y
              +
              1
              )
            
          
        
        =
        
          
            1
            
              (
              x
              +
              1
              )
              
                B
              
              (
              y
              +
              1
              ,
              x
              −
              y
              +
              1
              )
            
          
        
        .
      
    
    {\displaystyle {x \choose y}={\frac {\Gamma (x+1)}{\Gamma (y+1)\Gamma (x-y+1)}}={\frac {1}{(x+1)\mathrm {B} (y+1,x-y+1)}}.}
  

This definition inherits these following additional properties from 
  
    
      
        Γ
      
    
    {\displaystyle \Gamma }
  
:

  
    
      
        
          
            
              (
            
            
              x
              y
            
            
              )
            
          
        
        =
        
          
            
              sin
              ⁡
              (
              y
              π
              )
            
            
              sin
              ⁡
              (
              x
              π
              )
            
          
        
        
          
            
              (
            
            
              
                −
                y
                −
                1
              
              
                −
                x
                −
                1
              
            
            
              )
            
          
        
        =
        
          
            
              sin
              ⁡
              (
              (
              x
              −
              y
              )
              π
              )
            
            
              sin
              ⁡
              (
              x
              π
              )
            
          
        
        
          
            
              (
            
            
              
                y
                −
                x
                −
                1
              
              y
            
            
              )
            
          
        
        ;
      
    
    {\displaystyle {x \choose y}={\frac {\sin(y\pi )}{\sin(x\pi )}}{-y-1 \choose -x-1}={\frac {\sin((x-y)\pi )}{\sin(x\pi )}}{y-x-1 \choose y};}
  

moreover,

  
    
      
        
          
            
              (
            
            
              x
              y
            
            
              )
            
          
        
        ⋅
        
          
            
              (
            
            
              y
              x
            
            
              )
            
          
        
        =
        
          
            
              sin
              ⁡
              (
              (
              x
              −
              y
              )
              π
              )
            
            
              (
              x
              −
              y
              )
              π
            
          
        
        .
      
    
    {\displaystyle {x \choose y}\cdot {y \choose x}={\frac {\sin((x-y)\pi )}{(x-y)\pi }}.}
  

The resulting function has been little-studied, apparently first being graphed in (Fowler 1996). Notably, many binomial identities fail: 
  
    
      
        
          
            
              (
            
            
              n
              m
            
            
              )
            
          
        
        =
        
          
            
              (
            
            
              n
              
                n
                −
                m
              
            
            
              )
            
          
        
      
    
    {\textstyle {\binom {n}{m}}={\binom {n}{n-m}}}
  
 but 
  
    
      
        
          
            
              (
            
            
              
                −
                n
              
              m
            
            
              )
            
          
        
        ≠
        
          
            
              (
            
            
              
                −
                n
              
              
                −
                n
                −
                m
              
            
            
              )
            
          
        
      
    
    {\textstyle {\binom {-n}{m}}\neq {\binom {-n}{-n-m}}}
  
 for n positive (so 
  
    
      
        −
        n
      
    
    {\displaystyle -n}
  
 negative). The behavior is quite complex, and markedly different in various octants (that is, with respect to the x and y axes and the line 
  
    
      
        y
        =
        x
      
    
    {\displaystyle y=x}
  
), with the behavior for negative x having singularities at negative integer values and a checkerboard of positive and negative regions:

in the octant 
  
    
      
        0
        ≤
        y
        ≤
        x
      
    
    {\displaystyle 0\leq y\leq x}
  
 it is a smoothly interpolated form of the usual binomial, with a ridge ("Pascal's ridge").
in the octant 
  
    
      
        0
        ≤
        x
        ≤
        y
      
    
    {\displaystyle 0\leq x\leq y}
  
 and in the quadrant 
  
    
      
        x
        ≥
        0
        ,
        y
        ≤
        0
      
    
    {\displaystyle x\geq 0,y\leq 0}
  
 the function is close to zero.
in the quadrant 
  
    
      
        x
        ≤
        0
        ,
        y
        ≥
        0
      
    
    {\displaystyle x\leq 0,y\geq 0}
  
 the function is alternatingly very large positive and negative on the parallelograms with vertices 
  
    
      
        (
        −
        n
        ,
        m
        +
        1
        )
        ,
        (
        −
        n
        ,
        m
        )
        ,
        (
        −
        n
        −
        1
        ,
        m
        −
        1
        )
        ,
        (
        −
        n
        −
        1
        ,
        m
        )
      
    
    {\displaystyle (-n,m+1),(-n,m),(-n-1,m-1),(-n-1,m)}
  

in the octant 
  
    
      
        0
        >
        x
        >
        y
      
    
    {\displaystyle 0>x>y}
  
 the behavior is again alternatingly very large positive and negative, but on a square grid.
in the octant 
  
    
      
        −
        1
        >
        y
        >
        x
        +
        1
      
    
    {\displaystyle -1>y>x+1}
  
 it is close to zero, except for near the singularities.

Generalization to q-series
The binomial coefficient has a q-analog generalization known as the Gaussian binomial coefficient.

Generalization to infinite cardinals
The definition of the binomial coefficient can be generalized to infinite cardinals by defining:

  
    
      
        
          
            
              (
            
            
              α
              β
            
            
              )
            
          
        
        =
        
          |
          
            {
            
              B
              ⊆
              A
              :
              
                |
                B
                |
              
              =
              β
            
            }
          
          |
        
      
    
    {\displaystyle {\alpha  \choose \beta }=\left|\left\{B\subseteq A:\left|B\right|=\beta \right\}\right|}
  

where A is some set with cardinality 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
. One can show that the generalized binomial coefficient is well-defined, in the sense that no matter what set we choose to represent the cardinal number 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
, 
  
    
      
        
          
            
              (
            
            
              α
              β
            
            
              )
            
          
        
      
    
    {\textstyle {\alpha  \choose \beta }}
  
 will remain the same. For finite cardinals, this definition coincides with the standard definition of the binomial coefficient.
Assuming the Axiom of Choice, one can show that 
  
    
      
        
          
            
              (
            
            
              α
              α
            
            
              )
            
          
        
        =
        
          2
          
            α
          
        
      
    
    {\textstyle {\alpha  \choose \alpha }=2^{\alpha }}
  
 for any infinite cardinal 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
.

See also
Notes
References
External links
"Binomial coefficients", Encyclopedia of Mathematics, EMS Press, 2001 [1994]
Andrew Granville (1997). "Arithmetic Properties of Binomial Coefficients I. Binomial coefficients modulo prime powers". CMS Conf. Proc. 20: 151–162. Archived from the original on 2015-09-23. Retrieved 2013-09-03.
This article incorporates material from the following PlanetMath articles, which are licensed under the Creative Commons Attribution/Share-Alike License:  Binomial Coefficient,  Upper and lower bounds to binomial coefficient, Binomial coefficient is an integer, Generalized binomial coefficients.
