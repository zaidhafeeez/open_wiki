# Pancake sorting

## Metadata
- **Last Updated:** 2024-12-03 06:53:22 UTC
- **Original Article:** [Pancake sorting](https://en.wikipedia.org/wiki/Pancake_sorting)
- **Language:** en
- **Page ID:** 478065

## Summary
Pancake sorting is the mathematical problem of sorting a disordered stack of pancakes in order of size when a spatula can be inserted at any point in the stack and used to flip all pancakes above it.  A pancake number is the minimum number of flips required for a given number of pancakes. In this form, the problem was first discussed by American geometer Jacob E. Goodman. A variant of the problem is concerned with burnt pancakes, where each pancake has a burnt side and all pancakes must, in addition, end up with the burnt side on bottom.
All sorting methods require pairs of elements to be compared. For the traditional sorting problem, the usual problem studied is to minimize the number of comparisons required to sort a list. The number of actual operations, such as swapping two elements, is then irrelevant. For pancake sorting problems, in contrast, the aim is to minimize the number of operations, where the only allowed operations are reversals of the elements of some prefix of the sequence. Now, the number of comparisons is irrelevant.

## Categories
This article belongs to the following categories:

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Pancakes
- Category:Short description matches Wikidata
- Category:Sorting algorithms
- Category:Use mdy dates from October 2014

## Table of Contents

- The pancake problems
- The pancake problem on strings
- History
- Pancake graphs
- Algorithm
- Related integer sequences
- References
- Further reading
- External links

## Content

Pancake sorting is the mathematical problem of sorting a disordered stack of pancakes in order of size when a spatula can be inserted at any point in the stack and used to flip all pancakes above it.  A pancake number is the minimum number of flips required for a given number of pancakes. In this form, the problem was first discussed by American geometer Jacob E. Goodman. A variant of the problem is concerned with burnt pancakes, where each pancake has a burnt side and all pancakes must, in addition, end up with the burnt side on bottom.
All sorting methods require pairs of elements to be compared. For the traditional sorting problem, the usual problem studied is to minimize the number of comparisons required to sort a list. The number of actual operations, such as swapping two elements, is then irrelevant. For pancake sorting problems, in contrast, the aim is to minimize the number of operations, where the only allowed operations are reversals of the elements of some prefix of the sequence. Now, the number of comparisons is irrelevant.

The pancake problems
The original pancake problem
The minimum number of flips required to sort any stack of n pancakes has been shown to lie between ⁠15/14⁠n and ⁠18/11⁠n (approximately 1.07n and 1.64n), but the exact value is not known.
The simplest pancake sorting algorithm performs at most 2n − 3 flips. In this algorithm, a kind of selection sort, we bring the largest pancake not yet sorted to the top with one flip; take it down to its final position with one more flip; and repeat this process for the remaining pancakes.
In 1979, Bill Gates and Christos Papadimitriou gave a lower bound of ⁠17/16⁠n (approximately 1.06n) flips and an upper bound of ⁠(5n+5)/3⁠. The upper bound was improved, thirty years later, to  ⁠18/11⁠n by a team of researchers at the University of Texas at Dallas, led by Founders Professor Hal Sudborough.
In 2011, Laurent Bulteau, Guillaume Fertin, and Irena Rusu proved that the problem of finding the shortest sequence of flips for a given stack of pancakes is NP-hard, thereby answering a question that had been open for over three decades.

The burnt pancake problem
In a variation called the burnt pancake problem, the bottom of each pancake in the pile is burnt, and the sort must be completed with the burnt side of every pancake down. It is a signed permutation, and if a pancake i is "burnt side up" a negative element i` is put in place of i in the permutation. In 2008, a group of undergraduates built a bacterial computer that can solve a simple example of the burnt pancake problem by programming E. coli to flip segments of DNA which are analogous to burnt pancakes. DNA has an orientation (5' and 3') and an order (promoter before coding). Even though the processing power expressed by DNA flips is low, the high number of bacteria in a culture provides a large parallel computing platform. The bacteria report when they have solved the problem by becoming antibiotic resistant.

The pancake problem on strings
The discussion above presumes that each pancake is unique, that is, the sequence on which the prefix reversals are performed is a permutation. However, "strings" are sequences in which a symbol can repeat, and this repetition may reduce the number of prefix reversals required to sort. Chitturi and Sudborough (2010) and Hurkens et al. (2007) independently showed that the complexity of transforming a compatible string into another with the minimum number of prefix reversals is NP-complete. They also gave bounds for the same. Hurkens et al. gave an exact algorithm to sort binary and ternary strings. Chitturi  (2011) proved that the complexity of transforming a compatible signed string into another with the minimum number of signed prefix reversals—the burnt pancake problem on strings—is NP-complete.

History
The pancake sorting problem was first posed by Jacob E. Goodman, writing under the pseudonym "Harry Dweighter" ("harried waiter").
Although seen more often as an educational device, pancake sorting also appears in applications in parallel processor networks, in which it can provide an effective routing algorithm between processors.
The problem is notable as the topic of the only well-known mathematics paper by Microsoft founder Bill Gates (as William Gates), entitled "Bounds for Sorting by Prefix Reversal" and co-authored with Christos Papadimitriou. Published in 1979, it describes an efficient algorithm for pancake sorting. In addition, the most notable paper published by Futurama co-creator David X. Cohen (as David S. Cohen), co-authored with Manuel Blum, concerned the burnt pancake problem.
The connected problems of signed sorting by reversals and sorting by reversals were also studied more recently. Whereas efficient exact algorithms have been found for the signed sorting by reversals, the problem of sorting by reversals has been proven to be hard even to approximate to within certain constant factor, and also proven to be approximable in polynomial time to within the approximation factor 1.375.

Pancake graphs
An n-pancake graph is a graph whose vertices are the permutations of n symbols from 1 to n and its edges are given between permutations transitive by prefix reversals. It is a regular graph with n! vertices, its degree is n−1. The pancake sorting problem and the problem to obtain the diameter of the pancake graph are equivalent.
The pancake graph of dimension n, Pn can be constructed recursively from n copies of Pn−1, by assigning a different element from the set {1, 2, …, n} as a suffix to each copy.
Their girth:

  
    
      
        g
        (
        
          P
          
            n
          
        
        )
        =
        6
        
          , if 
        
        n
        >
        2
      
    
    {\displaystyle g(P_{n})=6{\text{, if }}n>2}
  
.
The γ(Pn) genus of Pn is:

  
    
      
        n
        !
        
          (
          
            
              
                n
                −
                4
              
              6
            
          
          )
        
        +
        1
        ≤
        γ
        (
        
          P
          
            n
          
        
        )
        ≤
        n
        !
        
          (
          
            
              
                n
                −
                3
              
              4
            
          
          )
        
        −
        
          
            n
            2
          
        
        +
        1
      
    
    {\displaystyle n!\left({\frac {n-4}{6}}\right)+1\leq \gamma (P_{n})\leq n!\left({\frac {n-3}{4}}\right)-{\frac {n}{2}}+1}
  

Since pancake graphs have many interesting properties such as symmetric and recursive structures, small degrees and diameters compared against the size of the graph, much attention is paid to them as a model of interconnection networks for parallel computers. When we regard the pancake graphs as the model of the interconnection networks, the diameter of the graph is a measure that represents the delay of communication.
The pancake graphs are Cayley graphs (thus are vertex-transitive) and are especially attractive for parallel processing. They have sublogarithmic degree and diameter, and are relatively sparse (compared to e.g. hypercubes).

Algorithm
An example of the pancake sorting algorithm is given below in Python. The code is similar to bubble sort or selection sort.

Related integer sequences
Sequences from The Online Encyclopedia of Integer Sequences:

OEIS: A058986 – maximum number of flips
OEIS: A067607 – number of stacks requiring the maximum number of flips (above)
OEIS: A078941 – maximum number of flips for a "burnt" stack
OEIS: A078942 – the number of flips for a sorted "burnt-side-on-top" stack
OEIS: A092113 – the above triangle, read by rows

References
Further reading
External links
Cut-the-Knot: Flipping pancakes puzzle, including a Java applet for the pancake problem and some discussion.
Douglas B. West's "The Pancake Problems"
Weisstein, Eric W. "Pancake Sorting". MathWorld.

## Archive Info
- **Archived on:** 2024-12-15 21:05:37 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 8153 bytes
- **Word Count:** 1197 words
