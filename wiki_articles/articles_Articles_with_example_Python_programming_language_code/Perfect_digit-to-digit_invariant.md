# Perfect digit-to-digit invariant

## Metadata
- **Last Updated:** 2024-12-03 07:23:41 UTC
- **Original Article:** [Perfect digit-to-digit invariant](https://en.wikipedia.org/wiki/Perfect_digit-to-digit_invariant)
- **Language:** en
- **Page ID:** 24356530

## Summary
In number theory, a perfect digit-to-digit invariant (PDDI; also known as a Munchausen number) is a natural number in a given number base 
  
    
      
        b
      
    
    {\displaystyle b}
  
 that is equal to the sum of its digits each raised to the power of itself. An example in base 10 is 3435, because 
  
    
      
        3435
        =
        
          3
          
            3
          
        
        +
        
          4
          
            4
          
        
        +
        
          3
          
            3
          
        
        +
        
          5
          
            5
          
        
      
    
    {\displaystyle 3435=3^{3}+4^{4}+3^{3}+5^{5}}
  
. The term "Munchausen number" was coined by Dutch mathematician and software engineer Daan van Berkel in 2009, as this evokes the story of Baron Munchausen raising himself up by his own ponytail because each digit is raised to the power of itself.

## Categories
This article belongs to the following categories:

- Category:Arithmetic dynamics
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Base-dependent integer sequences
- Category:Short description is different from Wikidata

## Table of Contents

- Definition
- Perfect digit-to-digit invariants and cycles of Fb for specific b
- Programming examples
- See also
- References
- External links

## Content

In number theory, a perfect digit-to-digit invariant (PDDI; also known as a Munchausen number) is a natural number in a given number base 
  
    
      
        b
      
    
    {\displaystyle b}
  
 that is equal to the sum of its digits each raised to the power of itself. An example in base 10 is 3435, because 
  
    
      
        3435
        =
        
          3
          
            3
          
        
        +
        
          4
          
            4
          
        
        +
        
          3
          
            3
          
        
        +
        
          5
          
            5
          
        
      
    
    {\displaystyle 3435=3^{3}+4^{4}+3^{3}+5^{5}}
  
. The term "Munchausen number" was coined by Dutch mathematician and software engineer Daan van Berkel in 2009, as this evokes the story of Baron Munchausen raising himself up by his own ponytail because each digit is raised to the power of itself.

Definition
Let 
  
    
      
        n
      
    
    {\displaystyle n}
  
 be a natural number which can be written in base 
  
    
      
        b
      
    
    {\displaystyle b}
  
 as the k-digit number 
  
    
      
        
          d
          
            k
            −
            1
          
        
        
          d
          
            k
            −
            2
          
        
        .
        .
        .
        
          d
          
            1
          
        
        
          d
          
            0
          
        
      
    
    {\displaystyle d_{k-1}d_{k-2}...d_{1}d_{0}}
  
 where each digit 
  
    
      
        
          d
          
            i
          
        
      
    
    {\displaystyle d_{i}}
  
 is between 
  
    
      
        0
      
    
    {\displaystyle 0}
  
 and 
  
    
      
        b
        −
        1
      
    
    {\displaystyle b-1}
  
 inclusive, and 
  
    
      
        n
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
          
        
        
          b
          
            i
          
        
      
    
    {\displaystyle n=\sum _{i=0}^{k-1}d_{i}b^{i}}
  
. We define the function 
  
    
      
        
          F
          
            b
          
        
        :
        
          N
        
        →
        
          N
        
      
    
    {\displaystyle F_{b}:\mathbb {N} \rightarrow \mathbb {N} }
  
 as 
  
    
      
        
          F
          
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
              
            
          
          
            
              d
              
                i
              
            
          
        
      
    
    {\displaystyle F_{b}(n)=\sum _{i=0}^{k-1}{d_{i}}^{d_{i}}}
  
. (As 00 is usually undefined, there are typically two conventions used, one where it is taken to be equal to one, and another where it is taken to be equal to zero.) A natural number 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is defined to be a perfect digit-to-digit invariant in base b if 
  
    
      
        
          F
          
            b
          
        
        (
        n
        )
        =
        n
      
    
    {\displaystyle F_{b}(n)=n}
  
. For example, the number 3435 is a perfect digit-to-digit invariant in base 10 because 
  
    
      
        
          3
          
            3
          
        
        +
        
          4
          
            4
          
        
        +
        
          3
          
            3
          
        
        +
        
          5
          
            5
          
        
        =
        27
        +
        256
        +
        27
        +
        3125
        =
        3435
      
    
    {\displaystyle 3^{3}+4^{4}+3^{3}+5^{5}=27+256+27+3125=3435}
  
. 

  
    
      
        
          F
          
            b
          
        
        (
        1
        )
        =
        1
      
    
    {\displaystyle F_{b}(1)=1}
  
 for all 
  
    
      
        b
      
    
    {\displaystyle b}
  
, and thus 1 is a trivial perfect digit-to-digit invariant in all bases, and all other perfect digit-to-digit invariants are nontrivial. For the second convention where 
  
    
      
        
          0
          
            0
          
        
        =
        0
      
    
    {\displaystyle 0^{0}=0}
  
, both 
  
    
      
        0
      
    
    {\displaystyle 0}
  
 and 
  
    
      
        1
      
    
    {\displaystyle 1}
  
 are trivial perfect digit-to-digit invariants.
A natural number 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is a sociable digit-to-digit invariant if it is a periodic point for 
  
    
      
        
          F
          
            b
          
        
      
    
    {\displaystyle F_{b}}
  
, where 
  
    
      
        
          F
          
            b
          
          
            k
          
        
        (
        n
        )
        =
        n
      
    
    {\displaystyle F_{b}^{k}(n)=n}
  
 for a positive integer 
  
    
      
        k
      
    
    {\displaystyle k}
  
, and forms a cycle of period 
  
    
      
        k
      
    
    {\displaystyle k}
  
. A perfect digit-to-digit invariant is a sociable digit-to-digit invariant with 
  
    
      
        k
        =
        1
      
    
    {\displaystyle k=1}
  
. An amicable digit-to-digit invariant is a sociable digit-to-digit invariant with 
  
    
      
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
          
            b
          
        
      
    
    {\displaystyle F_{b}}
  
, regardless of the base. This is because all natural numbers of base 
  
    
      
        b
      
    
    {\displaystyle b}
  
 with 
  
    
      
        k
      
    
    {\displaystyle k}
  
 digits satisfy 
  
    
      
        
          b
          
            k
            −
            1
          
        
        ≤
        n
        ≤
        (
        k
        )
        
          
            (
            b
            −
            1
            )
          
          
            b
            −
            1
          
        
      
    
    {\displaystyle b^{k-1}\leq n\leq (k){(b-1)}^{b-1}}
  
. However, when 
  
    
      
        k
        ≥
        b
        +
        1
      
    
    {\displaystyle k\geq b+1}
  
, then 
  
    
      
        
          b
          
            k
            −
            1
          
        
        >
        (
        k
        )
        
          
            (
            b
            −
            1
            )
          
          
            b
            −
            1
          
        
      
    
    {\displaystyle b^{k-1}>(k){(b-1)}^{b-1}}
  
, so any 
  
    
      
        n
      
    
    {\displaystyle n}
  
 will satisfy 
  
    
      
        n
        >
        
          F
          
            b
          
        
        (
        n
        )
      
    
    {\displaystyle n>F_{b}(n)}
  
 until 
  
    
      
        n
        <
        
          b
          
            b
            +
            1
          
        
      
    
    {\displaystyle n<b^{b+1}}
  
. There are a finite number of natural numbers less than 
  
    
      
        
          b
          
            b
            +
            1
          
        
      
    
    {\displaystyle b^{b+1}}
  
, so the number is guaranteed to reach a periodic point or a fixed point less than 
  
    
      
        
          b
          
            b
            +
            1
          
        
      
    
    {\displaystyle b^{b+1}}
  
, making it a preperiodic point. This means also that there are a finite number of perfect digit-to-digit invariant and cycles for any given base 
  
    
      
        b
      
    
    {\displaystyle b}
  
.
The number of iterations 
  
    
      
        i
      
    
    {\displaystyle i}
  
 needed for 
  
    
      
        
          F
          
            b
          
          
            i
          
        
        (
        n
        )
      
    
    {\displaystyle F_{b}^{i}(n)}
  
 to reach a fixed point is the 
  
    
      
        b
      
    
    {\displaystyle b}
  
-factorion function's persistence of 
  
    
      
        n
      
    
    {\displaystyle n}
  
, and undefined if it never reaches a fixed point.

Perfect digit-to-digit invariants and cycles of Fb for specific b
All numbers are represented in base 
  
    
      
        b
      
    
    {\displaystyle b}
  
.

Convention 00 = 1
Convention 00 = 0
Programming examples
The following program in Python determines whether an integer number is a Munchausen Number / Perfect Digit to Digit Invariant or not, following the convention 
  
    
      
        
          0
          
            0
          
        
        =
        1
      
    
    {\displaystyle 0^{0}=1}
  
.

The examples below implement the perfect digit-to-digit invariant function described in the definition above to search for perfect digit-to-digit invariants and cycles in Python for the two conventions.

Convention 00 = 1
Convention 00 = 0
See also
Arithmetic dynamics
Dudeney number
Factorion
Happy number
Kaprekar's constant
Kaprekar number
Meertens number
Narcissistic number
Perfect digital invariant
Sum-product number

References
External links
Parker, Matt. "3435". Numberphile. Brady Haran. Archived from the original on 2017-04-13. Retrieved 2013-04-01.

## Archive Info
- **Archived on:** 2024-12-15 21:05:39 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 10191 bytes
- **Word Count:** 830 words
