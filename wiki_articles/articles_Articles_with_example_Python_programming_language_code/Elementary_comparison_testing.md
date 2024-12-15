# Elementary comparison testing

## Metadata
- **Last Updated:** 2024-11-16 23:52:09 UTC
- **Original Article:** [Elementary comparison testing](https://en.wikipedia.org/wiki/Elementary_comparison_testing)
- **Language:** en
- **Page ID:** 56119486

## Summary
Elementary comparison testing (ECT) is a white-box, control-flow, test-design methodology used in software development. The purpose of ECT is to enable detailed testing of complex software. Software code or pseudocode is tested to assess the proper handling of all decision outcomes. As with multiple-condition coverage and basis path testing, coverage of all independent and isolated conditions is accomplished through modified condition/decision coverage (MC/DC). Isolated conditions are aggregated into connected situations creating formal test cases. The independence of a condition is shown by changing the condition value in isolation. Each relevant condition value is covered by test cases.

## Categories
This article belongs to the following categories:

- Category:Articles with example Python (programming language) code
- Category:Articles with example pseudocode
- Category:Pages that use a deprecated format of the math tags
- Category:Software testing

## Table of Contents

- Test case
- Test case graph
- Inductive proof of a number of condition paths
- Test-case design steps
- Example
- See also

## Content

Elementary comparison testing (ECT) is a white-box, control-flow, test-design methodology used in software development. The purpose of ECT is to enable detailed testing of complex software. Software code or pseudocode is tested to assess the proper handling of all decision outcomes. As with multiple-condition coverage and basis path testing, coverage of all independent and isolated conditions is accomplished through modified condition/decision coverage (MC/DC). Isolated conditions are aggregated into connected situations creating formal test cases. The independence of a condition is shown by changing the condition value in isolation. Each relevant condition value is covered by test cases.

Test case
A test case consists of a logical path through one or many decisions from start to end of a process. Contradictory situations are deduced from the test case matrix and excluded. The MC/DC approach isolates every condition, neglecting all possible subpath combinations and path coverage.

  
    
      
        T
        =
        n
        +
        1
      
    
    {\displaystyle T=n+1}
  

where

T is the number of test cases per decision and
n the number of conditions.
The decision 
  
    
      
        
          d
          
            i
          
        
      
    
    {\displaystyle d_{i}}
  
 consists of a combination of elementary conditions

  
    
      
        
          
            
              
                Σ
              
              
                
                =
                {
                0
                ,
                1
                }
              
            
            
              
                C
              
              
                
                =
                {
                
                  c
                  
                    0
                  
                
                ,
                
                  c
                  
                    1
                  
                
                ,
                
                  c
                  
                    2
                  
                
                ,
                
                  c
                  
                    3
                  
                
                ,
                .
                .
                .
                ,
                
                  c
                  
                    n
                  
                
                }
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\Sigma &=\{0,1\}\\C&=\{c_{0},c_{1},c_{2},c_{3},...,c_{n}\}\end{aligned}}}
  

  
    
      
        ϵ
        :
        C
        →
        Σ
        ×
        C
      
    
    {\displaystyle \epsilon :C\to \Sigma \times C}
  

  
    
      
        D
        ⊆
        
          C
          
            ∗
          
        
        
        ;
        
        
          d
          
            i
          
        
        ∈
        D
      
    
    {\displaystyle D\subseteq C^{*}\,;\;d_{i}\in D}
  

The transition function 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 is defined as

  
    
      
        α
        :
        D
        ×
        
          Σ
          
            ∗
          
        
        →
        Σ
        ×
        D
      
    
    {\displaystyle \alpha :D\times \Sigma ^{*}\to \Sigma \times D}
  

Given the transition 
  
    
      
        ⊢
      
    
    {\displaystyle \vdash }
  

  
    
      
        ⊢⊆
        (
        Σ
        ×
        D
        ×
        
          Σ
          
            ∗
          
        
        )
        ×
        (
        Σ
        ×
        D
        ×
        
          Σ
          
            ∗
          
        
        )
      
    
    {\displaystyle \vdash \subseteq (\Sigma \times D\times \Sigma ^{*})\times (\Sigma \times D\times \Sigma ^{*})}
  

  
    
      
        
          S
          
            j
          
        
        =
        (
        
          b
          
            j
          
        
        ,
        
          d
          
            m
          
        
        ,
        
          v
          
            j
          
        
        )
        ⊢
        (
        
          b
          
            j
            +
            1
          
        
        ,
        
          d
          
            n
          
        
        ,
        
          v
          
            j
            +
            1
          
        
        )
      
    
    {\displaystyle S_{j}=(b_{j},d_{m},v_{j})\vdash (b_{j+1},d_{n},v_{j+1})}
  

  
    
      
        
          E
          
            j
          
        
        =
        (
        
          a
          
            j
          
        
        ,
        
          c
          
            j
          
        
        )
        ⊢
        (
        
          a
          
            j
            +
            1
          
        
        ,
        
          c
          
            k
          
        
        )
      
    
    {\displaystyle E_{j}=(a_{j},c_{j})\vdash (a_{j+1},c_{k})}
  

  
    
      
        (
        
          b
          
            j
            +
            1
          
        
        ,
        
          d
          
            n
          
        
        )
        =
        α
        (
        
          d
          
            m
          
        
        ,
        
          v
          
            j
          
        
        )
        ;
        (
        
          b
          
            j
            +
            1
          
        
        ,
        
          c
          
            k
          
        
        )
        =
        ϵ
        (
        
          c
          
            j
          
        
        )
        ;
        
          a
          
            j
          
        
        ∈
        Σ
        ,
      
    
    {\displaystyle (b_{j+1},d_{n})=\alpha (d_{m},v_{j});(b_{j+1},c_{k})=\epsilon (c_{j});a_{j}\in \Sigma ,}
  

the isolated test path 
  
    
      
        
          P
          
            m
          
        
      
    
    {\displaystyle P_{m}}
  
 consists of

  
    
      
        
          
            
              
                
                  P
                  
                    m
                  
                
              
              
                
                =
                (
                
                  b
                  
                    0
                  
                
                ,
                
                  d
                  
                    0
                  
                
                ,
                
                  v
                  
                    0
                  
                
                )
                ⊢
                .
                .
                .
                ⊢
                (
                
                  b
                  
                    i
                  
                
                ,
                
                  d
                  
                    i
                  
                
                ,
                
                  v
                  
                    i
                  
                
                )
                
                  ⊢
                  
                    ∗
                  
                
                (
                
                  b
                  
                    n
                  
                
                ,
                
                  d
                  
                    n
                  
                
                ,
                
                  v
                  
                    n
                  
                
                )
              
            
            
              
              
                
                =
                (
                
                  b
                  
                    0
                  
                
                ,
                
                  c
                  
                    0
                  
                
                )
                ⊢
                .
                .
                .
                ⊢
                (
                
                  b
                  
                    m
                  
                
                ,
                
                  c
                  
                    m
                  
                
                )
                
                  ⊢
                  
                    ∗
                  
                
                (
                
                  b
                  
                    n
                  
                
                ,
                
                  c
                  
                    n
                  
                
                )
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}P_{m}&=(b_{0},d_{0},v_{0})\vdash ...\vdash (b_{i},d_{i},v_{i})\vdash ^{*}(b_{n},d_{n},v_{n})\\&=(b_{0},c_{0})\vdash ...\vdash (b_{m},c_{m})\vdash ^{*}(b_{n},c_{n})\end{aligned}}}
  

  
    
      
        
          b
          
            i
          
        
        ∈
        Σ
        ;
        
          c
          
            m
          
        
        ∈
        
          d
          
            i
          
        
        ;
        v
        ∈
        
          C
          
            ∗
          
        
        ;
        
          d
          
            0
          
        
        =
        S
        ;
        
          d
          
            n
          
        
        =
        E
        .
      
    
    {\displaystyle b_{i}\in \Sigma ;c_{m}\in d_{i};v\in C^{*};d_{0}=S;d_{n}=E.}

Test case graph
A test case graph illustrates all the necessary independent paths (test cases) to cover all isolated conditions. Conditions are represented by nodes, and condition values (situations) by edges. An edge addresses all program situations. Each situation is connected to one preceding and successive condition. Test cases might overlap due to isolated conditions.

Inductive proof of a number of condition paths
The elementary comparison testing method can be used to determine the number of condition paths by inductive proof.

There are 
  
    
      
        r
        =
        
          2
          
            n
          
        
      
    
    {\displaystyle r=2^{n}}
  
 possible condition value combinations

  
    
      
        ∀
        
          i
        
        ∈
        {
        1
        ,
        .
        .
        .
        ,
        n
        }
        ,
         
        
          c
          
            i
          
        
        ↦
        {
        0
        ,
         
        1
        }
        .
      
    
    {\displaystyle \forall {i}\in \{1,...,n\},\ c_{i}\mapsto \{0,\ 1\}.}
  

When each condition 
  
    
      
        
          c
          
            i
          
        
      
    
    {\displaystyle c_{i}}
  
 is isolated, the number of required test cases 
  
    
      
        T
      
    
    {\displaystyle T}
  
 per decision is:

  
    
      
        T
        =
        
          log
          
            2
          
        
        ⁡
        (
        r
        )
        +
        1
        =
        n
        +
        1.
      
    
    {\displaystyle T=\log _{2}(r)+1=n+1.}
  

  
    
      
        ∀
        
          i
        
        ∈
        {
        1
        ,
        .
        .
        .
        ,
        n
        }
      
    
    {\displaystyle \forall {i}\in \{1,...,n\}}
  
 there are 
  
    
      
        0
        <
        e
        <
        i
        +
        1
      
    
    {\displaystyle 0<e<i+1}
  
 edges from parent nodes 
  
    
      
        
          c
          
            i
          
        
      
    
    {\displaystyle c_{i}}
  
 and 
  
    
      
        s
        =
        2
      
    
    {\displaystyle s=2}
  
 edges to child nodes from 
  
    
      
        
          c
          
            i
          
        
      
    
    {\displaystyle c_{i}}
  
.
Each individual condition 
  
    
      
        
          c
          
            i
          
        
      
    
    {\displaystyle c_{i}}
  
 connects to at least one path

  
    
      
        ∀
        
          i
        
        ∈
        {
        1
        ,
        .
        .
        .
        ,
        n
        −
        1
        }
        ,
         
        
          c
          
            i
          
        
        ↦
        {
        0
        ,
         
        1
        }
      
    
    {\displaystyle \forall {i}\in \{1,...,n-1\},\ c_{i}\mapsto \{0,\ 1\}}
  

from the maximal possible 
  
    
      
        n
      
    
    {\displaystyle n}
  
 connecting to 
  
    
      
        
          c
          
            n
          
        
      
    
    {\displaystyle c_{n}}
  
 isolating 
  
    
      
        
          c
          
            n
          
        
      
    
    {\displaystyle c_{n}}
  
.
All predecessor conditions 
  
    
      
        
          c
          
            i
          
        
        ;
         
        i
        <
        n
      
    
    {\displaystyle c_{i};\ i<n}
  
 and respective paths are isolated. Therefore, when one node (condition) is added, the total number of paths, and required test cases, from start to finish increases by:

  
    
      
        T
        =
        n
        −
        1
        +
        2
        =
        n
        +
        1.
      
    
    {\displaystyle T=n-1+2=n+1.}
  

Q.E.D.

Test-case design steps
Identify decisions
Determine test situations per decision point (Modified Condition / Decision Coverage)
Create logical test-case matrix
Create physical test-case matrix

Example
This example shows ETC applied to a holiday booking system. The discount system offers reduced-price vacations. The offered discounts are 
  
    
      
        −
        20
        %
      
    
    {\displaystyle -20\%}
  
 for members or for expensive vacations, 
  
    
      
        −
        10
        %
      
    
    {\displaystyle -10\%}
  
 for moderate vacations with workday departures, and 
  
    
      
        0
        %
      
    
    {\displaystyle 0\%}
  
 otherwise. The example shows the creation of logical and physical test cases for all isolated conditions.
Pseudocode

if days > 15 or price > 1000 or member then
    return −0.2
else if (days > 8 and days ≤ 15 or price ≥ 500 and price ≤ 1000) and workday then
    return −0.1
else
    return 0.0

Factors

Number of days: 
  
    
      
        <
        8
        ;
         
        8
        −
        15
        ;
         
        >
        15
      
    
    {\displaystyle <8;\ 8-15;\ >15}
  

Price (euros): 
  
    
      
        <
        500
        ;
         
        500
        −
        1000
        ;
         
        >
        1000
      
    
    {\displaystyle <500;\ 500-1000;\ >1000}
  

Membership card: none; silver; gold; platinum
Departure date: workday; weekend; holiday

  
    
      
        T
        =
        3
        ×
        3
        ×
        4
        ×
        3
        =
        108
      
    
    {\displaystyle T=3\times 3\times 4\times 3=108}
  
 possible combinations (test cases).

Example in Python:

Step 1: Decisions
d
                  
                    1
                  
                
              
              
                
                =
                
                  days
                
                >
                15
                 
                
                  or
                
                 
                
                  price
                
                >
                1000
                 
                
                  Eur
                
                 
                
                  or
                
                 
                
                  member
                
              
            
            
              
                
                  c
                  
                    1
                  
                
              
              
                
                =
                
                  days
                
                >
                15
              
            
            
              
                
                  c
                  
                    2
                  
                
              
              
                
                =
                
                  price
                
                >
                1000
              
            
            
              
                
                  c
                  
                    3
                  
                
              
              
                
                =
                
                  member
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}d_{1}&={\text{days}}>15\ {\text{or}}\ {\text{price}}>1000\ {\text{Eur}}\ {\text{or}}\ {\text{member}}\\c_{1}&={\text{days}}>15\\c_{2}&={\text{price}}>1000\\c_{3}&={\text{member}}\\\end{aligned}}}
  

  
    
      
        
          
            
              
                
                  d
                  
                    2
                  
                
              
              
                
                =
                (
                8
                <
                
                  days
                
                <
                15
                 
                
                  or
                
                 
                500
                <
                
                  price
                
                <
                1000
                 
                
                  Eur
                
                )
                 
                
                  and
                
                 
                
                  workday
                
              
            
            
              
                
                  c
                  
                    4
                  
                
              
              
                
                =
                8
                <
                
                  days
                
                <
                15
              
            
            
              
                
                  c
                  
                    5
                  
                
              
              
                
                =
                500
                <
                
                  price
                
                <
                1000
                 
                
                  Eur
                
              
            
            
              
                
                  c
                  
                    6
                  
                
              
              
                
                =
                
                  workday
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}d_{2}&=(8<{\text{days}}<15\ {\text{or}}\ 500<{\text{price}}<1000\ {\text{Eur}})\ {\text{and}}\ {\text{workday}}\\c_{4}&=8<{\text{days}}<15\\c_{5}&=500<{\text{price}}<1000\ {\text{Eur}}\\c_{6}&={\text{workday}}\\\end{aligned}}}

Step 2: MC/DC Matrix
The highlighted diagonals in the MC/DC Matrix are describing the isolated conditions:

  
    
      
        (
        
          c
          
            i
          
        
        ,
        
          c
          
            i
          
        
        )
        ↦
        {
        1
        ,
        0
        }
      
    
    {\displaystyle (c_{i},c_{i})\mapsto \{1,0\}}
  

all duplicate situations are regarded as proven and removed.

Step 3: Logical test-Case matrix
Test cases are formed by tracing decision paths. For every decision 
  
    
      
        
          d
          
            i
          
        
        ;
         
        0
        <
        i
        <
        n
        +
        1
      
    
    {\displaystyle d_{i};\ 0<i<n+1}
  
 a succeeding and preceding subpath is searched until every connected path has a start 
  
    
      
        S
      
    
    {\displaystyle S}
  
 and an end 
  
    
      
        E
      
    
    {\displaystyle E}
  
:

  
    
      
        
          
            
              
                
                  T
                  
                    1
                  
                
              
              
                
                =
                (
                
                  d
                  
                    1
                  
                
                ,
                100
                )
                ⊢
                (
                1
                ,
                E
                )
              
            
            
              
                
                  T
                  
                    2
                  
                
              
              
                
                =
                (
                
                  d
                  
                    1
                  
                
                ,
                000
                )
                ⊢
                (
                0
                ,
                
                  d
                  
                    2
                  
                
                ,
                100
                )
                ⊢
                (
                1
                ,
                E
                )
              
            
            
              
                
                  T
                  
                    3
                  
                
              
              
                
                =
                (
                
                  d
                  
                    1
                  
                
                ,
                010
                )
                ⊢
                (
                1
                ,
                E
                )
              
            
            
              
                ⋮
              
            
            
              
                
                  T
                  
                    n
                    +
                    1
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}T_{1}&=(d_{1},100)\vdash (1,E)\\T_{2}&=(d_{1},000)\vdash (0,d_{2},100)\vdash (1,E)\\T_{3}&=(d_{1},010)\vdash (1,E)\\\vdots \\T_{n+1}\end{aligned}}}

Step 4: Physical test-case matrix
Physical test cases are created from logical test cases by filling in actual value representations and their respective results.

Test-case graph
In the example test case graph, all test cases and their isolated conditions are marked by colors, and the remaining paths are implicitly passed.

See also
Code coverage § Multiple condition coverage
Control-flow graph
Decision-to-decision path


== References ==

## Archive Info
- **Archived on:** 2024-12-15 21:04:17 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 23946 bytes
- **Word Count:** 1354 words
