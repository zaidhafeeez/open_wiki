# Gestalt pattern matching

## Article Metadata

- **Last Updated:** 2024-12-14T19:37:43.293389+00:00
- **Original Article:** [Gestalt pattern matching](https://en.wikipedia.org/wiki/Gestalt_pattern_matching)
- **Language:** en
- **Page ID:** 61099017

## Summary

Gestalt pattern matching, also Ratcliff/Obershelp pattern recognition, is a string-matching algorithm for determining the similarity of two strings. It was developed in 1983 by John W. Ratcliff and John A. Obershelp and published in the Dr. Dobb's Journal in July 1988.

## Categories

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

## Related Articles

### Internal Links

- [Aho–Corasick algorithm](https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm)
- [Apostolico–Giancarlo algorithm](https://en.wikipedia.org/wiki/Apostolico%E2%80%93Giancarlo_algorithm)
- [Approximate string matching](https://en.wikipedia.org/wiki/Approximate_string_matching)
- [BLAST (biotechnology)](https://en.wikipedia.org/wiki/BLAST_(biotechnology))
- [Bitap algorithm](https://en.wikipedia.org/wiki/Bitap_algorithm)
- [Boyer–Moore string-search algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm)
- [Boyer–Moore–Horspool algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore%E2%80%93Horspool_algorithm)
- [Character (symbol)](https://en.wikipedia.org/wiki/Character_(symbol))
- [Commentz-Walter algorithm](https://en.wikipedia.org/wiki/Commentz-Walter_algorithm)
- [Commutative property](https://en.wikipedia.org/wiki/Commutative_property)
- [Comparison of regular expression engines](https://en.wikipedia.org/wiki/Comparison_of_regular_expression_engines)
- [Compressed pattern matching](https://en.wikipedia.org/wiki/Compressed_pattern_matching)
- [Compressed suffix array](https://en.wikipedia.org/wiki/Compressed_suffix_array)
- [Damerau–Levenshtein distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Data structure](https://en.wikipedia.org/wiki/Data_structure)
- [Deterministic acyclic finite state automaton](https://en.wikipedia.org/wiki/Deterministic_acyclic_finite_state_automaton)
- [Dr. Dobb's Journal](https://en.wikipedia.org/wiki/Dr._Dobb%27s_Journal)
- [Edit distance](https://en.wikipedia.org/wiki/Edit_distance)
- [FM-index](https://en.wikipedia.org/wiki/FM-index)
- [Generalized suffix tree](https://en.wikipedia.org/wiki/Generalized_suffix_tree)
- [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance)
- [Hirschberg's algorithm](https://en.wikipedia.org/wiki/Hirschberg%27s_algorithm)
- [Jaro–Winkler distance](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance)
- [John W. Ratcliff](https://en.wikipedia.org/wiki/John_W._Ratcliff)
- [Knuth–Morris–Pratt algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)
- [LCP array](https://en.wikipedia.org/wiki/LCP_array)
- [Lee distance](https://en.wikipedia.org/wiki/Lee_distance)
- [Levenshtein automaton](https://en.wikipedia.org/wiki/Levenshtein_automaton)
- [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
- [Longest common subsequence](https://en.wikipedia.org/wiki/Longest_common_subsequence)
- [Longest common substring](https://en.wikipedia.org/wiki/Longest_common_substring)
- [Needleman–Wunsch algorithm](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm)
- [Nondeterministic finite automaton](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton)
- [Parsing](https://en.wikipedia.org/wiki/Parsing)
- [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Rabin–Karp algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm)
- [Raita algorithm](https://en.wikipedia.org/wiki/Raita_algorithm)
- [Recursion (computer science)](https://en.wikipedia.org/wiki/Recursion_(computer_science))
- [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Regular grammar](https://en.wikipedia.org/wiki/Regular_grammar)
- [Rope (data structure)](https://en.wikipedia.org/wiki/Rope_(data_structure))
- [Semi-Thue system](https://en.wikipedia.org/wiki/Semi-Thue_system)
- [Sequence alignment](https://en.wikipedia.org/wiki/Sequence_alignment)
- [Sequential pattern mining](https://en.wikipedia.org/wiki/Sequential_pattern_mining)
- [Smith–Waterman algorithm](https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm)
- [String-searching algorithm](https://en.wikipedia.org/wiki/String-searching_algorithm)
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [String metric](https://en.wikipedia.org/wiki/String_metric)
- [String operations](https://en.wikipedia.org/wiki/String_operations)
- [Substring index](https://en.wikipedia.org/wiki/Substring_index)
- [Suffix array](https://en.wikipedia.org/wiki/Suffix_array)
- [Suffix automaton](https://en.wikipedia.org/wiki/Suffix_automaton)
- [Suffix tree](https://en.wikipedia.org/wiki/Suffix_tree)
- [Ternary search tree](https://en.wikipedia.org/wiki/Ternary_search_tree)
- [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction)
- [Trie](https://en.wikipedia.org/wiki/Trie)
- [Trigram search](https://en.wikipedia.org/wiki/Trigram_search)
- [Two-way string-matching algorithm](https://en.wikipedia.org/wiki/Two-way_string-matching_algorithm)
- [Upper and lower bounds](https://en.wikipedia.org/wiki/Upper_and_lower_bounds)
- [Wagner–Fischer algorithm](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm)
- [Zhu–Takaoka string matching algorithm](https://en.wikipedia.org/wiki/Zhu%E2%80%93Takaoka_string_matching_algorithm)
- [Wikipedia:Please clarify](https://en.wikipedia.org/wiki/Wikipedia:Please_clarify)
- [Template:Strings](https://en.wikipedia.org/wiki/Template:Strings)
- [Template talk:Strings](https://en.wikipedia.org/wiki/Template_talk:Strings)
- [Category:String sorting algorithms](https://en.wikipedia.org/wiki/Category:String_sorting_algorithms)
- [Category:Wikipedia articles needing clarification from April 2023](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_needing_clarification_from_April_2023)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:37:43.293389+00:00_