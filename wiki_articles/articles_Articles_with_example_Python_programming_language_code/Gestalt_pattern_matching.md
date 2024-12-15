# Gestalt pattern matching

## Metadata
- **Last Updated:** 2024-12-12 20:25:47 UTC
- **Original Article:** [Gestalt pattern matching](https://en.wikipedia.org/wiki/Gestalt_pattern_matching)
- **Language:** en
- **Page ID:** 61099017

## Summary
Gestalt pattern matching, also Ratcliff/Obershelp pattern recognition, is a string-matching algorithm for determining the similarity of two strings. It was developed in 1983 by John W. Ratcliff and John A. Obershelp and published in the Dr. Dobb's Journal in July 1988.

## Categories
This article belongs to the following categories:

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Information theory
- Category:Quantitative linguistics
- Category:Recursion
- Category:Search algorithms
- Category:Short description is different from Wikidata
- Category:String metrics
- Category:Wikipedia articles needing clarification from April 2023

## Table of Contents

- Algorithm
- Properties
- Applications
- References
- Further reading
- See also

## Content

Gestalt pattern matching, also Ratcliff/Obershelp pattern recognition, is a string-matching algorithm for determining the similarity of two strings. It was developed in 1983 by John W. Ratcliff and John A. Obershelp and published in the Dr. Dobb's Journal in July 1988.

Algorithm
The similarity of two strings 
  
    
      
        
          S
          
            1
          
        
      
    
    {\displaystyle S_{1}}
  
 and 
  
    
      
        
          S
          
            2
          
        
      
    
    {\displaystyle S_{2}}
  
 is determined by this formula: twice the number of matching characters 
  
    
      
        
          K
          
            m
          
        
      
    
    {\displaystyle K_{m}}
  
 divided by the total number of characters of both strings. The matching characters are defined as some longest common substring plus recursively the number of matching characters in the non-matching regions on both sides of the longest common substring:

  
    
      
        
          D
          
            r
            o
          
        
        =
        
          
            
              2
              
                K
                
                  m
                
              
            
            
              
                |
              
              
                S
                
                  1
                
              
              
                |
              
              +
              
                |
              
              
                S
                
                  2
                
              
              
                |
              
            
          
        
      
    
    {\displaystyle D_{ro}={\frac {2K_{m}}{|S_{1}|+|S_{2}|}}}
  

where the similarity metric can take a value between zero and one:

  
    
      
        0
        ≤
        
          D
          
            r
            o
          
        
        ≤
        1
      
    
    {\displaystyle 0\leq D_{ro}\leq 1}
  

The value of 1 stands for the complete match of the two strings, whereas the value of 0 means there is no match and not even one common letter.

Sample
The longest common substring is WIKIM (light grey) with 5 characters. There is no further substring on the left. The non-matching substrings on the right side are EDIA and ANIA. They again have a longest common substring IA (dark gray) with length 2.
The similarity metric is determined by:

  
    
      
        
          
            
              2
              
                K
                
                  m
                
              
            
            
              
                |
              
              
                S
                
                  1
                
              
              
                |
              
              +
              
                |
              
              
                S
                
                  2
                
              
              
                |
              
            
          
        
        =
        
          
            
              2
              ⋅
              (
              
                |
              
              
                “WIKIM”
              
              
                |
              
              +
              
                |
              
              
                “IA”
              
              
                |
              
              )
            
            
              
                |
              
              
                S
                
                  1
                
              
              
                |
              
              +
              
                |
              
              
                S
                
                  2
                
              
              
                |
              
            
          
        
        =
        
          
            
              2
              ⋅
              (
              5
              +
              2
              )
            
            
              9
              +
              9
            
          
        
        =
        
          
            14
            18
          
        
        =
        0.
        
          
            7
            ¯
          
        
      
    
    {\displaystyle {\frac {2K_{m}}{|S_{1}|+|S_{2}|}}={\frac {2\cdot (|{\text{“WIKIM”}}|+|{\text{“IA”}}|)}{|S_{1}|+|S_{2}|}}={\frac {2\cdot (5+2)}{9+9}}={\frac {14}{18}}=0.{\overline {7}}}

Properties
The Ratcliff/Obershelp matching characters can be substantially different from each longest common subsequence of the given strings. For example 
  
    
      
        
          S
          
            1
          
        
        =
        q
        
        c
        c
        c
        c
        c
        
        r
        
        d
        d
        d
        
        s
        
        b
        b
        b
        b
        
        t
        
        e
        e
        e
        
        u
      
    
    {\displaystyle S_{1}=q\;ccccc\;r\;ddd\;s\;bbbb\;t\;eee\;u}
  
 and 
  
    
      
        
          S
          
            2
          
        
        =
        v
        
        d
        d
        d
        
        w
        
        b
        b
        b
        b
        
        x
        
        e
        e
        e
        
        y
        
        c
        c
        c
        c
        c
        
        z
      
    
    {\displaystyle S_{2}=v\;ddd\;w\;bbbb\;x\;eee\;y\;ccccc\;z}
  
 have 
  
    
      
        c
        c
        c
        c
        c
      
    
    {\displaystyle ccccc}
  
 as their only longest common substring, and no common characters right of its occurrence, and likewise left, leading to 
  
    
      
        
          K
          
            m
          
        
        =
        5
      
    
    {\displaystyle K_{m}=5}
  
. However, the longest common subsequence of 
  
    
      
        
          S
          
            1
          
        
      
    
    {\displaystyle S_{1}}
  
 and 
  
    
      
        
          S
          
            2
          
        
      
    
    {\displaystyle S_{2}}
  
 is 
  
    
      
        (
        d
        d
        d
        )
        
        (
        b
        b
        b
        b
        )
        
        (
        e
        e
        e
        )
      
    
    {\displaystyle (ddd)\;(bbbb)\;(eee)}
  
, with a total length of 
  
    
      
        10
      
    
    {\displaystyle 10}
  
.

Complexity
The execution time of the algorithm is 
  
    
      
        O
        (
        
          n
          
            3
          
        
        )
      
    
    {\displaystyle O(n^{3})}
  
 in a worst case and 
  
    
      
        O
        (
        
          n
          
            2
          
        
        )
      
    
    {\displaystyle O(n^{2})}
  
 in an average case. By changing the computing method, the execution time can be improved significantly.

Commutative property
The Python library implementation of the gestalt pattern matching algorithm is not commutative:

  
    
      
        
          D
          
            r
            o
          
        
        (
        
          S
          
            1
          
        
        ,
        
          S
          
            2
          
        
        )
        ≠
        
          D
          
            r
            o
          
        
        (
        
          S
          
            2
          
        
        ,
        
          S
          
            1
          
        
        )
        .
      
    
    {\displaystyle D_{ro}(S_{1},S_{2})\neq D_{ro}(S_{2},S_{1}).}
  

Sample
For the two strings

  
    
      
        
          S
          
            1
          
        
        =
        
          GESTALT PATTERN MATCHING
        
      
    
    {\displaystyle S_{1}={\text{GESTALT PATTERN MATCHING}}}
  

and

  
    
      
        
          S
          
            2
          
        
        =
        
          GESTALT PRACTICE
        
      
    
    {\displaystyle S_{2}={\text{GESTALT PRACTICE}}}
  

the metric result for 

  
    
      
        
          D
          
            r
            o
          
        
        (
        
          S
          
            1
          
        
        ,
        
          S
          
            2
          
        
        )
      
    
    {\displaystyle D_{ro}(S_{1},S_{2})}
  
 is 
  
    
      
        
          
            24
            40
          
        
      
    
    {\displaystyle {\frac {24}{40}}}
  
 with the substrings GESTALT P, A, T, E and for

  
    
      
        
          D
          
            r
            o
          
        
        (
        
          S
          
            2
          
        
        ,
        
          S
          
            1
          
        
        )
      
    
    {\displaystyle D_{ro}(S_{2},S_{1})}
  
 the metric is 
  
    
      
        
          
            26
            40
          
        
      
    
    {\displaystyle {\frac {26}{40}}}
  
 with the substrings GESTALT P, R, A, C, I.

Applications
The Python difflib library, which was introduced in version 2.1, implements a similar algorithm that predates the Ratcliff-Obershelp algorithm. Due to the unfavourable runtime behaviour of this similarity metric, three methods have been implemented. Two of them return an upper bound in a faster execution time. The fastest variant only compares the length of the two substrings:

  
    
      
        
          D
          
            r
            q
            r
          
        
        =
        
          
            
              2
              ⋅
              min
              (
              
                |
              
              S
              1
              
                |
              
              ,
              
                |
              
              S
              2
              
                |
              
              )
            
            
              
                |
              
              S
              1
              
                |
              
              +
              
                |
              
              S
              2
              
                |
              
            
          
        
      
    
    {\displaystyle D_{rqr}={\frac {2\cdot \min(|S1|,|S2|)}{|S1|+|S2|}}}
  
,
The second upper bound calculates twice the sum of all used characters 
  
    
      
        
          S
          
            1
          
        
      
    
    {\displaystyle S_{1}}
  
 which occur in 
  
    
      
        
          S
          
            2
          
        
      
    
    {\displaystyle S_{2}}
  
 divided by the length of both strings but the sequence is ignored.

  
    
      
        
          D
          
            q
            r
          
        
        =
        
          
            
              2
              ⋅
              
                
                  |
                
              
              {
              
              |
              S
              1
              |
              
              }
              ∩
              {
              
              |
              S
              2
              |
              
              }
              
                
                  |
                
              
            
            
              
                |
              
              S
              1
              
                |
              
              +
              
                |
              
              S
              2
              
                |
              
            
          
        
      
    
    {\displaystyle D_{qr}={\frac {2\cdot {\big |}\{\!\vert S1\vert \!\}\cap \{\!\vert S2\vert \!\}{\big |}}{|S1|+|S2|}}}
  

Trivially the following applies:

  
    
      
        0
        ≤
        
          D
          
            r
            o
          
        
        ≤
        
          D
          
            q
            r
          
        
        ≤
        
          D
          
            r
            q
            r
          
        
        ≤
        1
      
    
    {\displaystyle 0\leq D_{ro}\leq D_{qr}\leq D_{rqr}\leq 1}
  
 and

  
    
      
        0
        ≤
        
          K
          
            m
          
        
        ≤
        
          |
        
        {
        
        |
        S
        1
        |
        
        }
        ∩
        {
        
        |
        S
        2
        |
        
        }
        
          
            |
          
        
        ≤
        min
        (
        
          |
        
        S
        1
        
          |
        
        ,
        
          |
        
        S
        2
        
          |
        
        )
        ≤
        
          
            
              
                |
              
              S
              1
              
                |
              
              +
              
                |
              
              S
              2
              
                |
              
            
            2
          
        
      
    
    {\displaystyle 0\leq K_{m}\leq |\{\!\vert S1\vert \!\}\cap \{\!\vert S2\vert \!\}{\big |}\leq \min(|S1|,|S2|)\leq {\frac {|S1|+|S2|}{2}}}
  
.

References
Further reading
Ratcliff, John W.; Metzener, David (July 1988). "Pattern Matching: The Gestalt Approach". Dr. Dobb's Journal (46).

See also
Pattern matching

## Archive Info
- **Archived on:** 2024-12-15 21:04:36 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 14003 bytes
- **Word Count:** 883 words
