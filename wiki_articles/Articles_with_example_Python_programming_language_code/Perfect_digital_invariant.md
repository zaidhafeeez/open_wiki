---
title: Perfect digital invariant
url: https://en.wikipedia.org/wiki/Perfect_digital_invariant
language: en
categories: ["Category:Arithmetic dynamics", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Base-dependent integer sequences", "Category:Diophantine equations", "Category:Short description with empty Wikidata description", "Category:Webarchive template wayback links"]
references: 0
last_modified: 2024-12-19T14:56:15Z
---

# Perfect digital invariant

## Summary

In number theory, a perfect digital invariant (PDI) is a number in a given number base (
  
    
      
        b
      
    
    {\displaystyle b}
  
) that is the sum of its own digits each raised to a given power (
  
    
      
        p
      
    
    {\displaystyle p}
  
).

## Full Content

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
