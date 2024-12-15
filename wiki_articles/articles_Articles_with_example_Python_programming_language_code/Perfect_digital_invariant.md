# Perfect digital invariant

## Article Metadata

- **Last Updated:** 2024-12-15T04:42:30.555926+00:00
- **Original Article:** [Perfect digital invariant](https://en.wikipedia.org/wiki/Perfect_digital_invariant)
- **Language:** en
- **Page ID:** 61883319

## Summary

In number theory, a perfect digital invariant (PDI) is a number in a given number base (
  
    
      
        b
      
    
    {\displaystyle b}
  
) that is the sum of its own digits each raised to a given power (
  
    
      
        p
      
    
    {\displaystyle p}
  
).

## Categories

- Category:Arithmetic dynamics
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Base-dependent integer sequences
- Category:Diophantine equations
- Category:Short description with empty Wikidata description
- Category:Webarchive template wayback links

## Table of Contents

- Definition
- F2,b
- F3,b
- Fp,b
- Extension to negative integers
- Relation to happy numbers
- Programming example
- See also
- References
- External links

## Content

In number theory, a perfect digital invariant (PDI) is a number in a given number base (
  
    
      
        b
      
    
    {\displaystyle b}
  
) that is the sum of its own digits each raised to a given power (
  
    
      
        p
      
    
    {\displaystyle p}
  
).

Definition
Let 
  
    
      
        n
      
    
    {\displaystyle n}
  
 be a natural number. The perfect digital invariant function (also known as a happy function, from happy numbers) for base 
  
    
      
        b
        >
        1
      
    
    {\displaystyle b>1}
  
 and power 
  
    
      
        p
        >
        0
      
    
    {\displaystyle p>0}
  
 
  
    
      
        
          F
          
            p
            ,
            b
          
        
        :
        
          N
        
        →
        
          N
        
      
    
    {\displaystyle F_{p,b}:\mathbb {N} \rightarrow \mathbb {N} }
  
 is defined as:

  
    
      
        
          F
          
            p
            ,
            b
          
        
        (
        n
        )
        =
        
          ∑
          
            i
            =
            0
          
          
            k
            −
            1
          
        
        
          d
          
            i
          
          
            p
          
        
        .
      
    
    {\displaystyle F_{p,b}(n)=\sum _{i=0}^{k-1}d_{i}^{p}.}
  

where 
  
    
      
        k
        =
        ⌊
        
          log
          
            b
          
        
        ⁡
        
          n
        
        ⌋
        +
        1
      
    
    {\displaystyle k=\lfloor \log _{b}{n}\rfloor +1}
  
 is the number of digits in the number in base 
  
    
      
        b
      
    
    {\displaystyle b}
  
, and 

  
    
      
        
          d
          
            i
          
        
        =
        
          
            
              n
              
                mod
                
                  
                    b
                    
                      i
                      +
                      1
                    
                  
                
              
              −
              n
              
                
                  mod
                  
                    b
                  
                
                
                  i
                
              
            
            
              b
              
                i
              
            
          
        
      
    
    {\displaystyle d_{i}={\frac {n{\bmod {b^{i+1}}}-n{\bmod {b}}^{i}}{b^{i}}}}
  

is the value of each digit of the number. A natural number 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is a perfect digital invariant if it is a fixed point for 
  
    
      
        
          F
          
            p
            ,
            b
          
        
      
    
    {\displaystyle F_{p,b}}
  
, which occurs if 
  
    
      
        
          F
          
            p
            ,
            b
          
        
        (
        n
        )
        =
        n
      
    
    {\displaystyle F_{p,b}(n)=n}
  
. 
  
    
      
        0
      
    
    {\displaystyle 0}
  
 and 
  
    
      
        1
      
    
    {\displaystyle 1}
  
 are trivial perfect digital invariants for all 
  
    
      
        b
      
    
    {\displaystyle b}
  
 and 
  
    
      
        p
      
    
    {\displaystyle p}
  
, all other perfect digital invariants are nontrivial perfect digital invariants.
For example, the number 4150 in base 
  
    
      
        b
        =
        10
      
    
    {\displaystyle b=10}
  
 is a perfect digital invariant with 
  
    
      
        p
        =
        5
      
    
    {\displaystyle p=5}
  
, because 
  
    
      
        4150
        =
        
          4
          
            5
          
        
        +
        
          1
          
            5
          
        
        +
        
          5
          
            5
          
        
        +
        
          0
          
            5
          
        
      
    
    {\displaystyle 4150=4^{5}+1^{5}+5^{5}+0^{5}}
  
.
A natural number 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is a sociable digital invariant if it is a periodic point for 
  
    
      
        
          F
          
            p
            ,
            b
          
        
      
    
    {\displaystyle F_{p,b}}
  
, where 
  
    
      
        
          F
          
            p
            ,
            b
          
          
            k
          
        
        (
        n
        )
        =
        n
      
    
    {\displaystyle F_{p,b}^{k}(n)=n}
  
 for a positive integer 
  
    
      
        k
      
    
    {\displaystyle k}
  
 (here 
  
    
      
        
          F
          
            p
            ,
            b
          
          
            k
          
        
      
    
    {\displaystyle F_{p,b}^{k}}
  
 is the 
  
    
      
        k
      
    
    {\displaystyle k}
  
th iterate of 
  
    
      
        
          F
          
            p
            ,
            b
          
        
      
    
    {\displaystyle F_{p,b}}
  
), and forms a cycle of period 
  
    
      
        k
      
    
    {\displaystyle k}
  
. A perfect digital invariant is a sociable digital invariant with 
  
    
      
        k
        =
        1
      
    
    {\displaystyle k=1}
  
, and a amicable digital invariant is a sociable digital invariant with 
  
    
      
        k
        =
        2
      
    
    {\displaystyle k=2}
  
.
All natural numbers 
  
    
      
        n
      
    
    {\displaystyle n}
  
 are preperiodic points for 
  
    
      
        
          F
          
            p
            ,
            b
          
        
      
    
    {\displaystyle F_{p,b}}
  
, regardless of the base. This is because if 
  
    
      
        k
        ≥
        p
        +
        2
      
    
    {\displaystyle k\geq p+2}
  
, 
  
    
      
        n
        ≥
        
          b
          
            k
            −
            1
          
        
        >
        
          b
          
            p
          
        
        k
      
    
    {\displaystyle n\geq b^{k-1}>b^{p}k}
  
, so any 
  
    
      
        n
      
    
    {\displaystyle n}
  
 will satisfy 
  
    
      
        n
        >
        
          F
          
            b
            ,
            p
          
        
        (
        n
        )
      
    
    {\displaystyle n>F_{b,p}(n)}
  
 until 
  
    
      
        n
        <
        
          b
          
            p
            +
            1
          
        
      
    
    {\displaystyle n<b^{p+1}}
  
. There are a finite number of natural numbers less than 
  
    
      
        
          b
          
            p
            +
            1
          
        
      
    
    {\displaystyle b^{p+1}}
  
, so the number is guaranteed to reach a periodic point or a fixed point less than 
  
    
      
        
          b
          
            p
            +
            1
          
        
      
    
    {\displaystyle b^{p+1}}
  
, making it a preperiodic point.
Numbers in base 
  
    
      
        b
        >
        p
      
    
    {\displaystyle b>p}
  
 lead to fixed or periodic points of numbers 
  
    
      
        n
        ≤
        (
        p
        −
        2
        
          )
          
            p
          
        
        +
        p
        (
        b
        −
        1
        
          )
          
            p
          
        
      
    
    {\displaystyle n\leq (p-2)^{p}+p(b-1)^{p}}
  
.

The number of iterations 
  
    
      
        i
      
    
    {\displaystyle i}
  
 needed for 
  
    
      
        
          F
          
            p
            ,
            b
          
          
            i
          
        
        (
        n
        )
      
    
    {\displaystyle F_{p,b}^{i}(n)}
  
 to reach a fixed point is the perfect digital invariant function's persistence of 
  
    
      
        n
      
    
    {\displaystyle n}
  
, and undefined if it never reaches a fixed point.

  
    
      
        
          F
          
            1
            ,
            b
          
        
      
    
    {\displaystyle F_{1,b}}
  
 is the digit sum. The only perfect digital invariants are the single-digit numbers in base 
  
    
      
        b
      
    
    {\displaystyle b}
  
, and there are no periodic points with prime period greater than 1.

  
    
      
        
          F
          
            p
            ,
            2
          
        
      
    
    {\displaystyle F_{p,2}}
  
 reduces to 
  
    
      
        
          F
          
            1
            ,
            2
          
        
      
    
    {\displaystyle F_{1,2}}
  
, as for any power 
  
    
      
        p
      
    
    {\displaystyle p}
  
, 
  
    
      
        
          0
          
            p
          
        
        =
        0
      
    
    {\displaystyle 0^{p}=0}
  
 and 
  
    
      
        
          1
          
            p
          
        
        =
        1
      
    
    {\displaystyle 1^{p}=1}
  
.
For every natural number 
  
    
      
        k
        >
        1
      
    
    {\displaystyle k>1}
  
, if 
  
    
      
        p
        <
        b
      
    
    {\displaystyle p<b}
  
, 
  
    
      
        (
        b
        −
        1
        )
        ≡
        0
        
          mod
          
            k
          
        
      
    
    {\displaystyle (b-1)\equiv 0{\bmod {k}}}
  
 and 
  
    
      
        (
        p
        −
        1
        )
        ≡
        0
        
          mod
          
            ϕ
          
        
        (
        k
        )
      
    
    {\displaystyle (p-1)\equiv 0{\bmod {\phi }}(k)}
  
, then for every natural number 
  
    
      
        n
      
    
    {\displaystyle n}
  
, if 
  
    
      
        n
        ≡
        m
        
          mod
          
            k
          
        
      
    
    {\displaystyle n\equiv m{\bmod {k}}}
  
, then 
  
    
      
        
          F
          
            p
            ,
            b
          
        
        (
        n
        )
        ≡
        m
        
          mod
          
            k
          
        
      
    
    {\displaystyle F_{p,b}(n)\equiv m{\bmod {k}}}
  
, where 
  
    
      
        ϕ
        (
        k
        )
      
    
    {\displaystyle \phi (k)}
  
 is Euler's totient function.

No upper bound can be determined for the size of perfect digital invariants in a given base and arbitrary power, and it is not currently known whether or not the number of perfect digital invariants for an arbitrary base is finite or infinite.

F2,b
By definition, any three-digit perfect digital invariant 
  
    
      
        n
        =
        
          d
          
            2
          
        
        
          d
          
            1
          
        
        
          d
          
            0
          
        
      
    
    {\displaystyle n=d_{2}d_{1}d_{0}}
  
 for 
  
    
      
        
          F
          
            2
            ,
            b
          
        
      
    
    {\displaystyle F_{2,b}}
  
 with natural number digits 
  
    
      
        0
        ≤
        
          d
          
            0
          
        
        <
        b
      
    
    {\displaystyle 0\leq d_{0}<b}
  
, 
  
    
      
        0
        ≤
        
          d
          
            1
          
        
        <
        b
      
    
    {\displaystyle 0\leq d_{1}<b}
  
, 
  
    
      
        0
        ≤
        
          d
          
            2
          
        
        <
        b
      
    
    {\displaystyle 0\leq d_{2}<b}
  
 has to satisfy the cubic Diophantine equation 
  
    
      
        
          d
          
            0
          
          
            2
          
        
        +
        
          d
          
            1
          
          
            2
          
        
        +
        
          d
          
            2
          
          
            2
          
        
        =
        
          d
          
            2
          
        
        
          b
          
            2
          
        
        +
        
          d
          
            1
          
        
        b
        +
        
          d
          
            0
          
        
      
    
    {\displaystyle d_{0}^{2}+d_{1}^{2}+d_{2}^{2}=d_{2}b^{2}+d_{1}b+d_{0}}
  
. 
  
    
      
        
          d
          
            2
          
        
      
    
    {\displaystyle d_{2}}
  
 has to be equal to 0 or 1 for any 
  
    
      
        b
        >
        2
      
    
    {\displaystyle b>2}
  
, because the maximum value 
  
    
      
        n
      
    
    {\displaystyle n}
  
 can take is 
  
    
      
        n
        =
        (
        2
        −
        1
        
          )
          
            2
          
        
        +
        2
        (
        b
        −
        1
        
          )
          
            2
          
        
        =
        1
        +
        2
        (
        b
        −
        1
        
          )
          
            2
          
        
        <
        2
        
          b
          
            2
          
        
      
    
    {\displaystyle n=(2-1)^{2}+2(b-1)^{2}=1+2(b-1)^{2}<2b^{2}}
  
. As a result, there are actually two related quadratic Diophantine equations to solve:

  
    
      
        
          d
          
            0
          
          
            2
          
        
        +
        
          d
          
            1
          
          
            2
          
        
        =
        
          d
          
            1
          
        
        b
        +
        
          d
          
            0
          
        
      
    
    {\displaystyle d_{0}^{2}+d_{1}^{2}=d_{1}b+d_{0}}
  
 when 
  
    
      
        
          d
          
            2
          
        
        =
        0
      
    
    {\displaystyle d_{2}=0}
  
, and

  
    
      
        
          d
          
            0
          
          
            2
          
        
        +
        
          d
          
            1
          
          
            2
          
        
        +
        1
        =
        
          b
          
            2
          
        
        +
        
          d
          
            1
          
        
        b
        +
        
          d
          
            0
          
        
      
    
    {\displaystyle d_{0}^{2}+d_{1}^{2}+1=b^{2}+d_{1}b+d_{0}}
  
 when 
  
    
      
        
          d
          
            2
          
        
        =
        1
      
    
    {\displaystyle d_{2}=1}
  
.
The two-digit natural number 
  
    
      
        n
        =
        
          d
          
            1
          
        
        
          d
          
            0
          
        
      
    
    {\displaystyle n=d_{1}d_{0}}
  
 is a perfect digital invariant in base 

  
    
      
        b
        =
        
          d
          
            1
          
        
        +
        
          
            
              
                d
                
                  0
                
              
              (
              
                d
                
                  0
                
              
              −
              1
              )
            
            
              d
              
                1
              
            
          
        
        .
      
    
    {\displaystyle b=d_{1}+{\frac {d_{0}(d_{0}-1)}{d_{1}}}.}
  

This can be proven by taking the first case, where 
  
    
      
        
          d
          
            2
          
        
        =
        0
      
    
    {\displaystyle d_{2}=0}
  
, and solving for 
  
    
      
        b
      
    
    {\displaystyle b}
  
. This means that for some values of 
  
    
      
        
          d
          
            0
          
        
      
    
    {\displaystyle d_{0}}
  
 and 
  
    
      
        
          d
          
            1
          
        
      
    
    {\displaystyle d_{1}}
  
, 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is not a perfect digital invariant in any base, as 
  
    
      
        
          d
          
            1
          
        
      
    
    {\displaystyle d_{1}}
  
 is not a divisor of 
  
    
      
        
          d
          
            0
          
        
        (
        
          d
          
            0
          
        
        −
        1
        )
      
    
    {\displaystyle d_{0}(d_{0}-1)}
  
. Moreover, 
  
    
      
        
          d
          
            0
          
        
        >
        1
      
    
    {\displaystyle d_{0}>1}
  
, because if 
  
    
      
        
          d
          
            0
          
        
        =
        0
      
    
    {\displaystyle d_{0}=0}
  
 or 
  
    
      
        
          d
          
            0
          
        
        =
        1
      
    
    {\displaystyle d_{0}=1}
  
, then 
  
    
      
        b
        =
        
          d
          
            1
          
        
      
    
    {\displaystyle b=d_{1}}
  
, which contradicts the earlier statement that 
  
    
      
        0
        ≤
        
          d
          
            1
          
        
        <
        b
      
    
    {\displaystyle 0\leq d_{1}<b}
  
.
There are no three-digit perfect digital invariants for 
  
    
      
        
          F
          
            2
            ,
            b
          
        
      
    
    {\displaystyle F_{2,b}}
  
, which can be proven by taking the second case, where 
  
    
      
        
          d
          
            2
          
        
        =
        1
      
    
    {\displaystyle d_{2}=1}
  
, and letting 
  
    
      
        
          d
          
            0
          
        
        =
        b
        −
        
          a
          
            0
          
        
      
    
    {\displaystyle d_{0}=b-a_{0}}
  
 and 
  
    
      
        
          d
          
            1
          
        
        =
        b
        −
        
          a
          
            1
          
        
      
    
    {\displaystyle d_{1}=b-a_{1}}
  
. Then the Diophantine equation for the three-digit perfect digital invariant becomes 

  
    
      
        (
        b
        −
        
          a
          
            0
          
        
        
          )
          
            2
          
        
        +
        (
        b
        −
        
          a
          
            1
          
        
        
          )
          
            2
          
        
        +
        1
        =
        
          b
          
            2
          
        
        +
        (
        b
        −
        
          a
          
            1
          
        
        )
        b
        +
        (
        b
        −
        
          a
          
            0
          
        
        )
      
    
    {\displaystyle (b-a_{0})^{2}+(b-a_{1})^{2}+1=b^{2}+(b-a_{1})b+(b-a_{0})}
  

  
    
      
        
          b
          
            2
          
        
        −
        2
        
          a
          
            0
          
        
        b
        +
        
          a
          
            0
          
          
            2
          
        
        +
        
          b
          
            2
          
        
        −
        2
        
          a
          
            1
          
        
        b
        +
        
          a
          
            1
          
          
            2
          
        
        +
        1
        =
        
          b
          
            2
          
        
        +
        (
        b
        −
        
          a
          
            1
          
        
        )
        b
        +
        (
        b
        −
        
          a
          
            0
          
        
        )
      
    
    {\displaystyle b^{2}-2a_{0}b+a_{0}^{2}+b^{2}-2a_{1}b+a_{1}^{2}+1=b^{2}+(b-a_{1})b+(b-a_{0})}
  

  
    
      
        2
        
          b
          
            2
          
        
        −
        2
        (
        
          a
          
            0
          
        
        +
        
          a
          
            1
          
        
        )
        b
        +
        
          a
          
            0
          
          
            2
          
        
        +
        
          a
          
            1
          
          
            2
          
        
        +
        1
        =
        
          b
          
            2
          
        
        +
        (
        b
        −
        
          a
          
            1
          
        
        )
        b
        +
        (
        b
        −
        
          a
          
            0
          
        
        )
      
    
    {\displaystyle 2b^{2}-2(a_{0}+a_{1})b+a_{0}^{2}+a_{1}^{2}+1=b^{2}+(b-a_{1})b+(b-a_{0})}
  

  
    
      
        
          b
          
            2
          
        
        +
        (
        b
        −
        2
        (
        
          a
          
            0
          
        
        +
        
          a
          
            1
          
        
        )
        )
        b
        +
        
          a
          
            0
          
          
            2
          
        
        +
        
          a
          
            1
          
          
            2
          
        
        +
        1
        =
        
          b
          
            2
          
        
        +
        (
        b
        −
        
          a
          
            1
          
        
        )
        b
        +
        (
        b
        −
        
          a
          
            0
          
        
        )
      
    
    {\displaystyle b^{2}+(b-2(a_{0}+a_{1}))b+a_{0}^{2}+a_{1}^{2}+1=b^{2}+(b-a_{1})b+(b-a_{0})}
  

  
    
      
        2
        (
        
          a
          
            0
          
        
        +
        
          a
          
            1
          
        
        )
        >
        
          a
          
            1
          
        
      
    
    {\displaystyle 2(a_{0}+a_{1})>a_{1}}
  
 for all values of 
  
    
      
        0
        <
        
          a
          
            1
          
        
        ≤
        b
      
    
    {\displaystyle 0<a_{1}\leq b}
  
. Thus, there are no solutions to the Diophantine equation, and there are no three-digit perfect digital invariants for 
  
    
      
        
          F
          
            2
            ,
            b
          
        
      
    
    {\displaystyle F_{2,b}}
  
.

F3,b
By definition, any four-digit perfect digital invariant 
  
    
      
        n
      
    
    {\displaystyle n}
  
 for 
  
    
      
        
          F
          
            3
            ,
            b
          
        
      
    
    {\displaystyle F_{3,b}}
  
 with natural number digits 
  
    
      
        0
        ≤
        
          d
          
            0
          
        
        <
        b
      
    
    {\displaystyle 0\leq d_{0}<b}
  
, 
  
    
      
        0
        ≤
        
          d
          
            1
          
        
        <
        b
      
    
    {\displaystyle 0\leq d_{1}<b}
  
, 
  
    
      
        0
        ≤
        
          d
          
            2
          
        
        <
        b
      
    
    {\displaystyle 0\leq d_{2}<b}
  
, 
  
    
      
        0
        ≤
        
          d
          
            3
          
        
        <
        b
      
    
    {\displaystyle 0\leq d_{3}<b}
  
 has to satisfy the quartic Diophantine equation 
  
    
      
        
          d
          
            0
          
          
            3
          
        
        +
        
          d
          
            1
          
          
            3
          
        
        +
        
          d
          
            2
          
          
            3
          
        
        +
        
          d
          
            3
          
          
            3
          
        
        =
        
          d
          
            3
          
        
        
          b
          
            3
          
        
        +
        
          d
          
            2
          
        
        
          b
          
            2
          
        
        +
        
          d
          
            1
          
        
        b
        +
        
          d
          
            0
          
        
      
    
    {\displaystyle d_{0}^{3}+d_{1}^{3}+d_{2}^{3}+d_{3}^{3}=d_{3}b^{3}+d_{2}b^{2}+d_{1}b+d_{0}}
  
. 
  
    
      
        
          d
          
            3
          
        
      
    
    {\displaystyle d_{3}}
  
 has to be equal to 0, 1, 2 for any 
  
    
      
        b
        >
        3
      
    
    {\displaystyle b>3}
  
, because the maximum value 
  
    
      
        n
      
    
    {\displaystyle n}
  
 can take is 
  
    
      
        n
        =
        (
        3
        −
        2
        
          )
          
            3
          
        
        +
        3
        (
        b
        −
        1
        
          )
          
            3
          
        
        =
        1
        +
        3
        (
        b
        −
        1
        
          )
          
            3
          
        
        <
        3
        
          b
          
            3
          
        
      
    
    {\displaystyle n=(3-2)^{3}+3(b-1)^{3}=1+3(b-1)^{3}<3b^{3}}
  
. As a result, there are actually three related cubic Diophantine equations to solve

  
    
      
        
          d
          
            0
          
          
            3
          
        
        +
        
          d
          
            1
          
          
            3
          
        
        +
        
          d
          
            2
          
          
            3
          
        
        =
        
          d
          
            2
          
        
        
          b
          
            2
          
        
        +
        
          d
          
            1
          
        
        b
        +
        
          d
          
            0
          
        
      
    
    {\displaystyle d_{0}^{3}+d_{1}^{3}+d_{2}^{3}=d_{2}b^{2}+d_{1}b+d_{0}}
  
 when 
  
    
      
        
          d
          
            3
          
        
        =
        0
      
    
    {\displaystyle d_{3}=0}
  

  
    
      
        
          d
          
            0
          
          
            3
          
        
        +
        
          d
          
            1
          
          
            3
          
        
        +
        
          d
          
            2
          
          
            3
          
        
        +
        1
        =
        
          b
          
            3
          
        
        +
        
          d
          
            2
          
        
        
          b
          
            2
          
        
        +
        
          d
          
            1
          
        
        b
        +
        
          d
          
            0
          
        
      
    
    {\displaystyle d_{0}^{3}+d_{1}^{3}+d_{2}^{3}+1=b^{3}+d_{2}b^{2}+d_{1}b+d_{0}}
  
 when 
  
    
      
        
          d
          
            3
          
        
        =
        1
      
    
    {\displaystyle d_{3}=1}
  

  
    
      
        
          d
          
            0
          
          
            3
          
        
        +
        
          d
          
            1
          
          
            3
          
        
        +
        
          d
          
            2
          
          
            3
          
        
        +
        8
        =
        2
        
          b
          
            3
          
        
        +
        
          d
          
            2
          
        
        
          b
          
            2
          
        
        +
        
          d
          
            1
          
        
        b
        +
        
          d
          
            0
          
        
      
    
    {\displaystyle d_{0}^{3}+d_{1}^{3}+d_{2}^{3}+8=2b^{3}+d_{2}b^{2}+d_{1}b+d_{0}}
  
 when 
  
    
      
        
          d
          
            3
          
        
        =
        2
      
    
    {\displaystyle d_{3}=2}
  

We take the first case, where 
  
    
      
        
          d
          
            3
          
        
        =
        0
      
    
    {\displaystyle d_{3}=0}
  
.

b = 3k + 1
Let 
  
    
      
        k
      
    
    {\displaystyle k}
  
 be a positive integer and the number base 
  
    
      
        b
        =
        3
        k
        +
        1
      
    
    {\displaystyle b=3k+1}
  
. Then:

  
    
      
        
          n
          
            1
          
        
        =
        k
        
          b
          
            2
          
        
        +
        (
        2
        k
        +
        1
        )
        b
      
    
    {\displaystyle n_{1}=kb^{2}+(2k+1)b}
  
 is a perfect digital invariant for 
  
    
      
        
          F
          
            3
            ,
            b
          
        
      
    
    {\displaystyle F_{3,b}}
  
 for all 
  
    
      
        k
      
    
    {\displaystyle k}
  
.

  
    
      
        
          n
          
            2
          
        
        =
        k
        
          b
          
            2
          
        
        +
        (
        2
        k
        +
        1
        )
        b
        +
        1
      
    
    {\displaystyle n_{2}=kb^{2}+(2k+1)b+1}
  
 is a perfect digital invariant for 
  
    
      
        
          F
          
            3
            ,
            b
          
        
      
    
    {\displaystyle F_{3,b}}
  
 for all 
  
    
      
        k
      
    
    {\displaystyle k}
  
.

  
    
      
        
          n
          
            3
          
        
        =
        (
        k
        +
        1
        )
        
          b
          
            2
          
        
        +
        (
        2
        k
        +
        1
        )
      
    
    {\displaystyle n_{3}=(k+1)b^{2}+(2k+1)}
  
 is a perfect digital invariant for 
  
    
      
        
          F
          
            3
            ,
            b
          
        
      
    
    {\displaystyle F_{3,b}}
  
 for all 
  
    
      
        k
      
    
    {\displaystyle k}
  
.

b = 3k + 2
Let 
  
    
      
        k
      
    
    {\displaystyle k}
  
 be a positive integer and the number base 
  
    
      
        b
        =
        3
        k
        +
        2
      
    
    {\displaystyle b=3k+2}
  
. Then:

  
    
      
        
          n
          
            1
          
        
        =
        k
        
          b
          
            2
          
        
        +
        (
        2
        k
        +
        1
        )
      
    
    {\displaystyle n_{1}=kb^{2}+(2k+1)}
  
 is a perfect digital invariant for 
  
    
      
        
          F
          
            3
            ,
            b
          
        
      
    
    {\displaystyle F_{3,b}}
  
 for all 
  
    
      
        k
      
    
    {\displaystyle k}
  
.

b = 6k + 4
Let 
  
    
      
        k
      
    
    {\displaystyle k}
  
 be a positive integer and the number base 
  
    
      
        b
        =
        6
        k
        +
        4
      
    
    {\displaystyle b=6k+4}
  
. Then:

  
    
      
        
          n
          
            4
          
        
        =
        k
        
          b
          
            2
          
        
        +
        (
        3
        k
        +
        2
        )
        b
        +
        (
        2
        k
        +
        1
        )
      
    
    {\displaystyle n_{4}=kb^{2}+(3k+2)b+(2k+1)}
  
 is a perfect digital invariant for 
  
    
      
        
          F
          
            3
            ,
            b
          
        
      
    
    {\displaystyle F_{3,b}}
  
 for all 
  
    
      
        k
      
    
    {\displaystyle k}
  
.

Fp,b
All numbers are represented in base 
  
    
      
        b
      
    
    {\displaystyle b}
  
.

Extension to negative integers
Perfect digital invariants can be extended to the negative integers by use of a signed-digit representation to represent each integer.

Balanced ternary
In balanced ternary, the digits are 1, −1 and 0. This results in the following:

With odd powers 
  
    
      
        p
        ≡
        1
        
          mod
          
            2
          
        
      
    
    {\displaystyle p\equiv 1{\bmod {2}}}
  
, 
  
    
      
        
          F
          
            p
            ,
            
              bal
            
            3
          
        
      
    
    {\displaystyle F_{p,{\text{bal}}3}}
  
 reduces down to digit sum iteration, as 
  
    
      
        (
        −
        1
        
          )
          
            p
          
        
        =
        −
        1
      
    
    {\displaystyle (-1)^{p}=-1}
  
, 
  
    
      
        
          0
          
            p
          
        
        =
        0
      
    
    {\displaystyle 0^{p}=0}
  
 and 
  
    
      
        
          1
          
            p
          
        
        =
        1
      
    
    {\displaystyle 1^{p}=1}
  
.
With even powers 
  
    
      
        p
        ≡
        0
        
          mod
          
            2
          
        
      
    
    {\displaystyle p\equiv 0{\bmod {2}}}
  
, 
  
    
      
        
          F
          
            p
            ,
            
              bal
            
            3
          
        
      
    
    {\displaystyle F_{p,{\text{bal}}3}}
  
 indicates whether the number is even or odd, as the sum of each digit will indicate divisibility by 2 if and only if the sum of digits ends in 0. As 
  
    
      
        
          0
          
            p
          
        
        =
        0
      
    
    {\displaystyle 0^{p}=0}
  
 and 
  
    
      
        (
        −
        1
        
          )
          
            p
          
        
        =
        
          1
          
            p
          
        
        =
        1
      
    
    {\displaystyle (-1)^{p}=1^{p}=1}
  
, for every pair of digits 1 or −1, their sum is 0 and the sum of their squares is 2.

Relation to happy numbers
A happy number 
  
    
      
        n
      
    
    {\displaystyle n}
  
 for a given base 
  
    
      
        b
      
    
    {\displaystyle b}
  
 and a given power 
  
    
      
        p
      
    
    {\displaystyle p}
  
 is a preperiodic point for the perfect digital invariant function 
  
    
      
        
          F
          
            p
            ,
            b
          
        
      
    
    {\displaystyle F_{p,b}}
  
 such that the 
  
    
      
        m
      
    
    {\displaystyle m}
  
-th iteration of 
  
    
      
        
          F
          
            p
            ,
            b
          
        
      
    
    {\displaystyle F_{p,b}}
  
 is equal to the trivial perfect digital invariant 
  
    
      
        1
      
    
    {\displaystyle 1}
  
, and an unhappy number is one such that there exists no such 
  
    
      
        m
      
    
    {\displaystyle m}
  
.

Programming example
The example below implements the perfect digital invariant function described in the definition above to search for perfect digital invariants and cycles in Python. This can be used to find happy numbers.

See also
Arithmetic dynamics
Dudeney number
Factorion
Happy number
Kaprekar's constant
Kaprekar number
Meertens number
Narcissistic number
Perfect digit-to-digit invariant
Sum-product number

References
External links
Digital Invariants

## Related Articles

### Internal Links

- [3](https://en.wikipedia.org/wiki/3)
- [A Mathematician's Apology](https://en.wikipedia.org/wiki/A_Mathematician%27s_Apology)
- [Abundant number](https://en.wikipedia.org/wiki/Abundant_number)
- [Achilles number](https://en.wikipedia.org/wiki/Achilles_number)
- [Persistence of a number](https://en.wikipedia.org/wiki/Persistence_of_a_number)
- [Aliquot sequence](https://en.wikipedia.org/wiki/Aliquot_sequence)
- [Almost perfect number](https://en.wikipedia.org/wiki/Almost_perfect_number)
- [Almost prime](https://en.wikipedia.org/wiki/Almost_prime)
- [Amenable number](https://en.wikipedia.org/wiki/Amenable_number)
- [Amicable numbers](https://en.wikipedia.org/wiki/Amicable_numbers)
- [Arithmetic dynamics](https://en.wikipedia.org/wiki/Arithmetic_dynamics)
- [Arithmetic function](https://en.wikipedia.org/wiki/Arithmetic_function)
- [Arithmetic number](https://en.wikipedia.org/wiki/Arithmetic_number)
- [Aronson's sequence](https://en.wikipedia.org/wiki/Aronson%27s_sequence)
- [Automorphic number](https://en.wikipedia.org/wiki/Automorphic_number)
- [Balanced ternary](https://en.wikipedia.org/wiki/Balanced_ternary)
- [Ban number](https://en.wikipedia.org/wiki/Ban_number)
- [Decimal](https://en.wikipedia.org/wiki/Decimal)
- [Duodecimal](https://en.wikipedia.org/wiki/Duodecimal)
- [Hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal)
- [Vigesimal](https://en.wikipedia.org/wiki/Vigesimal)
- [Ternary numeral system](https://en.wikipedia.org/wiki/Ternary_numeral_system)
- [Quaternary numeral system](https://en.wikipedia.org/wiki/Quaternary_numeral_system)
- [Quinary](https://en.wikipedia.org/wiki/Quinary)
- [Senary](https://en.wikipedia.org/wiki/Senary)
- [Octal](https://en.wikipedia.org/wiki/Octal)
- [Ternary numeral system](https://en.wikipedia.org/wiki/Ternary_numeral_system)
- [Bell number](https://en.wikipedia.org/wiki/Bell_number)
- [Betrothed numbers](https://en.wikipedia.org/wiki/Betrothed_numbers)
- [Binary number](https://en.wikipedia.org/wiki/Binary_number)
- [Blum integer](https://en.wikipedia.org/wiki/Blum_integer)
- [Cake number](https://en.wikipedia.org/wiki/Cake_number)
- [Carmichael number](https://en.wikipedia.org/wiki/Carmichael_number)
- [Catalan number](https://en.wikipedia.org/wiki/Catalan_number)
- [Catalan pseudoprime](https://en.wikipedia.org/wiki/Catalan_pseudoprime)
- [Centered cube number](https://en.wikipedia.org/wiki/Centered_cube_number)
- [Centered decagonal number](https://en.wikipedia.org/wiki/Centered_decagonal_number)
- [Centered dodecahedral number](https://en.wikipedia.org/wiki/Centered_dodecahedral_number)
- [Centered heptagonal number](https://en.wikipedia.org/wiki/Centered_heptagonal_number)
- [Centered hexagonal number](https://en.wikipedia.org/wiki/Centered_hexagonal_number)
- [Centered icosahedral number](https://en.wikipedia.org/wiki/Centered_icosahedral_number)
- [Centered nonagonal number](https://en.wikipedia.org/wiki/Centered_nonagonal_number)
- [Centered octagonal number](https://en.wikipedia.org/wiki/Centered_octagonal_number)
- [Centered octahedral number](https://en.wikipedia.org/wiki/Centered_octahedral_number)
- [Centered pentagonal number](https://en.wikipedia.org/wiki/Centered_pentagonal_number)
- [Centered polygonal number](https://en.wikipedia.org/wiki/Centered_polygonal_number)
- [Centered polyhedral number](https://en.wikipedia.org/wiki/Centered_polyhedral_number)
- [Centered square number](https://en.wikipedia.org/wiki/Centered_square_number)
- [Centered tetrahedral number](https://en.wikipedia.org/wiki/Centered_tetrahedral_number)
- [Centered triangular number](https://en.wikipedia.org/wiki/Centered_triangular_number)
- [Colossally abundant number](https://en.wikipedia.org/wiki/Colossally_abundant_number)
- [Congruent number](https://en.wikipedia.org/wiki/Congruent_number)
- [Cube (algebra)](https://en.wikipedia.org/wiki/Cube_(algebra))
- [Cubic equation](https://en.wikipedia.org/wiki/Cubic_equation)
- [Cullen number](https://en.wikipedia.org/wiki/Cullen_number)
- [Cycle detection](https://en.wikipedia.org/wiki/Cycle_detection)
- [Cyclic number](https://en.wikipedia.org/wiki/Cyclic_number)
- [Cyclic number (group theory)](https://en.wikipedia.org/wiki/Cyclic_number_(group_theory))
- [Decagonal number](https://en.wikipedia.org/wiki/Decagonal_number)
- [Dedekind number](https://en.wikipedia.org/wiki/Dedekind_number)
- [Deficient number](https://en.wikipedia.org/wiki/Deficient_number)
- [Delannoy number](https://en.wikipedia.org/wiki/Delannoy_number)
- [Descartes number](https://en.wikipedia.org/wiki/Descartes_number)
- [Digit-reassembly number](https://en.wikipedia.org/wiki/Digit-reassembly_number)
- [Digit sum](https://en.wikipedia.org/wiki/Digit_sum)
- [Digital root](https://en.wikipedia.org/wiki/Digital_root)
- [Divisibility rule](https://en.wikipedia.org/wiki/Divisibility_rule)
- [Divisor](https://en.wikipedia.org/wiki/Divisor)
- [Divisor function](https://en.wikipedia.org/wiki/Divisor_function)
- [Dodecagonal number](https://en.wikipedia.org/wiki/Dodecagonal_number)
- [Dodecahedral number](https://en.wikipedia.org/wiki/Dodecahedral_number)
- [Double Mersenne number](https://en.wikipedia.org/wiki/Double_Mersenne_number)
- [Dudeney number](https://en.wikipedia.org/wiki/Dudeney_number)
- [Eighth power](https://en.wikipedia.org/wiki/Eighth_power)
- [Elliptic pseudoprime](https://en.wikipedia.org/wiki/Elliptic_pseudoprime)
- [Equidigital number](https://en.wikipedia.org/wiki/Equidigital_number)
- [Erdős–Nicolas number](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Nicolas_number)
- [Erdős–Woods number](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Woods_number)
- [Euclid number](https://en.wikipedia.org/wiki/Euclid_number)
- [Euler's theorem](https://en.wikipedia.org/wiki/Euler%27s_theorem)
- [Euler's totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function)
- [Euler numbers](https://en.wikipedia.org/wiki/Euler_numbers)
- [Euler pseudoprime](https://en.wikipedia.org/wiki/Euler_pseudoprime)
- [Eulerian number](https://en.wikipedia.org/wiki/Eulerian_number)
- [Euler–Jacobi pseudoprime](https://en.wikipedia.org/wiki/Euler%E2%80%93Jacobi_pseudoprime)
- [Evil number](https://en.wikipedia.org/wiki/Evil_number)
- [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)
- [Extravagant number](https://en.wikipedia.org/wiki/Extravagant_number)
- [Factorion](https://en.wikipedia.org/wiki/Factorion)
- [Fermat number](https://en.wikipedia.org/wiki/Fermat_number)
- [Fermat pseudoprime](https://en.wikipedia.org/wiki/Fermat_pseudoprime)
- [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)
- [Fifth power (algebra)](https://en.wikipedia.org/wiki/Fifth_power_(algebra))
- [Figurate number](https://en.wikipedia.org/wiki/Figurate_number)
- [Fixed point (mathematics)](https://en.wikipedia.org/wiki/Fixed_point_(mathematics))
- [Fortunate number](https://en.wikipedia.org/wiki/Fortunate_number)
- [Four-dimensional space](https://en.wikipedia.org/wiki/Four-dimensional_space)
- [Fourth power](https://en.wikipedia.org/wiki/Fourth_power)
- [Friedman number](https://en.wikipedia.org/wiki/Friedman_number)
- [Friendly number](https://en.wikipedia.org/wiki/Friendly_number)
- [Frobenius pseudoprime](https://en.wikipedia.org/wiki/Frobenius_pseudoprime)
- [Frugal number](https://en.wikipedia.org/wiki/Frugal_number)
- [Fuss–Catalan number](https://en.wikipedia.org/wiki/Fuss%E2%80%93Catalan_number)
- [G. H. Hardy](https://en.wikipedia.org/wiki/G._H._Hardy)
- [Generation of primes](https://en.wikipedia.org/wiki/Generation_of_primes)
- [Giuga number](https://en.wikipedia.org/wiki/Giuga_number)
- [Graphemics](https://en.wikipedia.org/wiki/Graphemics)
- [Happy number](https://en.wikipedia.org/wiki/Happy_number)
- [Happy number](https://en.wikipedia.org/wiki/Happy_number)
- [Harmonic divisor number](https://en.wikipedia.org/wiki/Harmonic_divisor_number)
- [Harshad number](https://en.wikipedia.org/wiki/Harshad_number)
- [Hemiperfect number](https://en.wikipedia.org/wiki/Hemiperfect_number)
- [Heptagonal number](https://en.wikipedia.org/wiki/Heptagonal_number)
- [Hexagonal number](https://en.wikipedia.org/wiki/Hexagonal_number)
- [Highly abundant number](https://en.wikipedia.org/wiki/Highly_abundant_number)
- [Highly composite number](https://en.wikipedia.org/wiki/Highly_composite_number)
- [Highly cototient number](https://en.wikipedia.org/wiki/Highly_cototient_number)
- [Highly totient number](https://en.wikipedia.org/wiki/Highly_totient_number)
- [Hilbert number](https://en.wikipedia.org/wiki/Hilbert_number)
- [Hyperperfect number](https://en.wikipedia.org/wiki/Hyperperfect_number)
- [Icosahedral number](https://en.wikipedia.org/wiki/Icosahedral_number)
- [Idoneal number](https://en.wikipedia.org/wiki/Idoneal_number)
- [If and only if](https://en.wikipedia.org/wiki/If_and_only_if)
- [Integer](https://en.wikipedia.org/wiki/Integer)
- [Iterated function](https://en.wikipedia.org/wiki/Iterated_function)
- [Jacobsthal number](https://en.wikipedia.org/wiki/Jacobsthal_number)
- [Jordan–Pólya number](https://en.wikipedia.org/wiki/Jordan%E2%80%93P%C3%B3lya_number)
- [Kaprekar's routine](https://en.wikipedia.org/wiki/Kaprekar%27s_routine)
- [Kaprekar number](https://en.wikipedia.org/wiki/Kaprekar_number)
- [Keith number](https://en.wikipedia.org/wiki/Keith_number)
- [Knödel number](https://en.wikipedia.org/wiki/Kn%C3%B6del_number)
- [Lah number](https://en.wikipedia.org/wiki/Lah_number)
- [Lazy caterer's sequence](https://en.wikipedia.org/wiki/Lazy_caterer%27s_sequence)
- [Leonardo number](https://en.wikipedia.org/wiki/Leonardo_number)
- [Leyland number](https://en.wikipedia.org/wiki/Leyland_number)
- [Lobb number](https://en.wikipedia.org/wiki/Lobb_number)
- [Löschian number](https://en.wikipedia.org/wiki/L%C3%B6schian_number)
- [Lucas number](https://en.wikipedia.org/wiki/Lucas_number)
- [Lucas pseudoprime](https://en.wikipedia.org/wiki/Lucas_pseudoprime)
- [Lucas–Carmichael number](https://en.wikipedia.org/wiki/Lucas%E2%80%93Carmichael_number)
- [Lucky number](https://en.wikipedia.org/wiki/Lucky_number)
- [Lucky numbers of Euler](https://en.wikipedia.org/wiki/Lucky_numbers_of_Euler)
- [Lychrel number](https://en.wikipedia.org/wiki/Lychrel_number)
- [Meertens number](https://en.wikipedia.org/wiki/Meertens_number)
- [Mersenne prime](https://en.wikipedia.org/wiki/Mersenne_prime)
- [Motzkin number](https://en.wikipedia.org/wiki/Motzkin_number)
- [Multiplicative digital root](https://en.wikipedia.org/wiki/Multiplicative_digital_root)
- [Multiplicative digital root](https://en.wikipedia.org/wiki/Multiplicative_digital_root)
- [Multiply perfect number](https://en.wikipedia.org/wiki/Multiply_perfect_number)
- [Narayana number](https://en.wikipedia.org/wiki/Narayana_number)
- [Narcissistic number](https://en.wikipedia.org/wiki/Narcissistic_number)
- [Natural language](https://en.wikipedia.org/wiki/Natural_language)
- [Natural number](https://en.wikipedia.org/wiki/Natural_number)
- [Nonagonal number](https://en.wikipedia.org/wiki/Nonagonal_number)
- [Noncototient](https://en.wikipedia.org/wiki/Noncototient)
- [Nonhypotenuse number](https://en.wikipedia.org/wiki/Nonhypotenuse_number)
- [Nontotient](https://en.wikipedia.org/wiki/Nontotient)
- [Radix](https://en.wikipedia.org/wiki/Radix)
- [Number theory](https://en.wikipedia.org/wiki/Number_theory)
- [Numeral system](https://en.wikipedia.org/wiki/Numeral_system)
- [Numerical digit](https://en.wikipedia.org/wiki/Numerical_digit)
- [Octagonal number](https://en.wikipedia.org/wiki/Octagonal_number)
- [Octahedral number](https://en.wikipedia.org/wiki/Octahedral_number)
- [Odious number](https://en.wikipedia.org/wiki/Odious_number)
- [On-Line Encyclopedia of Integer Sequences](https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences)
- [Ordered Bell number](https://en.wikipedia.org/wiki/Ordered_Bell_number)
- [P-adic number](https://en.wikipedia.org/wiki/P-adic_number)
- [Padovan sequence](https://en.wikipedia.org/wiki/Padovan_sequence)
- [Palindromic number](https://en.wikipedia.org/wiki/Palindromic_number)
- [Pancake sorting](https://en.wikipedia.org/wiki/Pancake_sorting)
- [Pandigital number](https://en.wikipedia.org/wiki/Pandigital_number)
- [Parasitic number](https://en.wikipedia.org/wiki/Parasitic_number)
- [Parity (mathematics)](https://en.wikipedia.org/wiki/Parity_(mathematics))
- [Pell number](https://en.wikipedia.org/wiki/Pell_number)
- [Pentagonal number](https://en.wikipedia.org/wiki/Pentagonal_number)
- [Pentatope number](https://en.wikipedia.org/wiki/Pentatope_number)
- [Perfect digit-to-digit invariant](https://en.wikipedia.org/wiki/Perfect_digit-to-digit_invariant)
- [Perfect number](https://en.wikipedia.org/wiki/Perfect_number)
- [Perfect power](https://en.wikipedia.org/wiki/Perfect_power)
- [Perfect totient number](https://en.wikipedia.org/wiki/Perfect_totient_number)
- [Periodic point](https://en.wikipedia.org/wiki/Periodic_point)
- [Periodic sequence](https://en.wikipedia.org/wiki/Periodic_sequence)
- [Permutation](https://en.wikipedia.org/wiki/Permutation)
- [Pernicious number](https://en.wikipedia.org/wiki/Pernicious_number)
- [Perrin number](https://en.wikipedia.org/wiki/Perrin_number)
- [Persistence of a number](https://en.wikipedia.org/wiki/Persistence_of_a_number)
- [Plane (mathematics)](https://en.wikipedia.org/wiki/Plane_(mathematics))
- [Polite number](https://en.wikipedia.org/wiki/Polite_number)
- [Polydivisible number](https://en.wikipedia.org/wiki/Polydivisible_number)
- [Polygonal number](https://en.wikipedia.org/wiki/Polygonal_number)
- [Figurate number](https://en.wikipedia.org/wiki/Figurate_number)
- [Power of 10](https://en.wikipedia.org/wiki/Power_of_10)
- [Power of three](https://en.wikipedia.org/wiki/Power_of_three)
- [Power of two](https://en.wikipedia.org/wiki/Power_of_two)
- [Powerful number](https://en.wikipedia.org/wiki/Powerful_number)
- [Practical number](https://en.wikipedia.org/wiki/Practical_number)
- [Primary pseudoperfect number](https://en.wikipedia.org/wiki/Primary_pseudoperfect_number)
- [Prime number](https://en.wikipedia.org/wiki/Prime_number)
- [Prime number](https://en.wikipedia.org/wiki/Prime_number)
- [Prime omega function](https://en.wikipedia.org/wiki/Prime_omega_function)
- [Prime power](https://en.wikipedia.org/wiki/Prime_power)
- [Primeval number](https://en.wikipedia.org/wiki/Primeval_number)
- [Primitive abundant number](https://en.wikipedia.org/wiki/Primitive_abundant_number)
- [Primorial](https://en.wikipedia.org/wiki/Primorial)
- [Pronic number](https://en.wikipedia.org/wiki/Pronic_number)
- [Proth prime](https://en.wikipedia.org/wiki/Proth_prime)
- [Pseudoprime](https://en.wikipedia.org/wiki/Pseudoprime)
- [Pyramidal number](https://en.wikipedia.org/wiki/Pyramidal_number)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quadratic equation](https://en.wikipedia.org/wiki/Quadratic_equation)
- [Quartic equation](https://en.wikipedia.org/wiki/Quartic_equation)
- [Quasiperfect number](https://en.wikipedia.org/wiki/Quasiperfect_number)
- [Recursion](https://en.wikipedia.org/wiki/Recursion)
- [Refactorable number](https://en.wikipedia.org/wiki/Refactorable_number)
- [Regular number](https://en.wikipedia.org/wiki/Regular_number)
- [Repdigit](https://en.wikipedia.org/wiki/Repdigit)
- [Repunit](https://en.wikipedia.org/wiki/Repunit)
- [Riesel number](https://en.wikipedia.org/wiki/Riesel_number)
- [Rough number](https://en.wikipedia.org/wiki/Rough_number)
- [Schröder number](https://en.wikipedia.org/wiki/Schr%C3%B6der_number)
- [Schröder–Hipparchus number](https://en.wikipedia.org/wiki/Schr%C3%B6der%E2%80%93Hipparchus_number)
- [Self-descriptive number](https://en.wikipedia.org/wiki/Self-descriptive_number)
- [Self number](https://en.wikipedia.org/wiki/Self_number)
- [Semiperfect number](https://en.wikipedia.org/wiki/Semiperfect_number)
- [Semiprime](https://en.wikipedia.org/wiki/Semiprime)
- [Seventh power](https://en.wikipedia.org/wiki/Seventh_power)
- [Sierpiński number](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_number)
- [Sieve theory](https://en.wikipedia.org/wiki/Sieve_theory)
- [Signed-digit representation](https://en.wikipedia.org/wiki/Signed-digit_representation)
- [Sixth power](https://en.wikipedia.org/wiki/Sixth_power)
- [Smarandache–Wellin number](https://en.wikipedia.org/wiki/Smarandache%E2%80%93Wellin_number)
- [Smith number](https://en.wikipedia.org/wiki/Smith_number)
- [Smooth number](https://en.wikipedia.org/wiki/Smooth_number)
- [Sociable number](https://en.wikipedia.org/wiki/Sociable_number)
- [Somer–Lucas pseudoprime](https://en.wikipedia.org/wiki/Somer%E2%80%93Lucas_pseudoprime)
- [Sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)
- [Sorting number](https://en.wikipedia.org/wiki/Sorting_number)
- [Sparsely totient number](https://en.wikipedia.org/wiki/Sparsely_totient_number)
- [Sphenic number](https://en.wikipedia.org/wiki/Sphenic_number)
- [Square number](https://en.wikipedia.org/wiki/Square_number)
- [Square pyramidal number](https://en.wikipedia.org/wiki/Square_pyramidal_number)
- [Square triangular number](https://en.wikipedia.org/wiki/Square_triangular_number)
- [Squared triangular number](https://en.wikipedia.org/wiki/Squared_triangular_number)
- [Star number](https://en.wikipedia.org/wiki/Star_number)
- [Stella octangula number](https://en.wikipedia.org/wiki/Stella_octangula_number)
- [Stirling numbers of the first kind](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind)
- [Stirling numbers of the second kind](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind)
- [Strobogrammatic number](https://en.wikipedia.org/wiki/Strobogrammatic_number)
- [Strong pseudoprime](https://en.wikipedia.org/wiki/Strong_pseudoprime)
- [Størmer number](https://en.wikipedia.org/wiki/St%C3%B8rmer_number)
- [Sublime number](https://en.wikipedia.org/wiki/Sublime_number)
- [Sum-product number](https://en.wikipedia.org/wiki/Sum-product_number)
- [Super-Poulet number](https://en.wikipedia.org/wiki/Super-Poulet_number)
- [Superabundant number](https://en.wikipedia.org/wiki/Superabundant_number)
- [Supergolden ratio](https://en.wikipedia.org/wiki/Supergolden_ratio)
- [Superior highly composite number](https://en.wikipedia.org/wiki/Superior_highly_composite_number)
- [Superperfect number](https://en.wikipedia.org/wiki/Superperfect_number)
- [Telephone number (mathematics)](https://en.wikipedia.org/wiki/Telephone_number_(mathematics))
- [Tetrahedral number](https://en.wikipedia.org/wiki/Tetrahedral_number)
- [Thabit number](https://en.wikipedia.org/wiki/Thabit_number)
- [Three-dimensional space](https://en.wikipedia.org/wiki/Three-dimensional_space)
- [Transposable integer](https://en.wikipedia.org/wiki/Transposable_integer)
- [Triangular number](https://en.wikipedia.org/wiki/Triangular_number)
- [Automorphic number](https://en.wikipedia.org/wiki/Automorphic_number)
- [Ulam number](https://en.wikipedia.org/wiki/Ulam_number)
- [Undulating number](https://en.wikipedia.org/wiki/Undulating_number)
- [Untouchable number](https://en.wikipedia.org/wiki/Untouchable_number)
- [Vampire number](https://en.wikipedia.org/wiki/Vampire_number)
- [Wall–Sun–Sun prime](https://en.wikipedia.org/wiki/Wall%E2%80%93Sun%E2%80%93Sun_prime)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Wedderburn–Etherington number](https://en.wikipedia.org/wiki/Wedderburn%E2%80%93Etherington_number)
- [Wieferich prime](https://en.wikipedia.org/wiki/Wieferich_prime)
- [Wilson prime](https://en.wikipedia.org/wiki/Wilson_prime)
- [Wolstenholme number](https://en.wikipedia.org/wiki/Wolstenholme_number)
- [Wolstenholme prime](https://en.wikipedia.org/wiki/Wolstenholme_prime)
- [Woodall number](https://en.wikipedia.org/wiki/Woodall_number)
- [Template:Classes of natural numbers](https://en.wikipedia.org/wiki/Template:Classes_of_natural_numbers)
- [Template talk:Classes of natural numbers](https://en.wikipedia.org/wiki/Template_talk:Classes_of_natural_numbers)
- [Portal:Mathematics](https://en.wikipedia.org/wiki/Portal:Mathematics)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:42:30.555926+00:00_