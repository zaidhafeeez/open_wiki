# Seidel's algorithm

## Metadata
- **Last Updated:** 2024-11-26 20:30:40 UTC
- **Original Article:** [Seidel's algorithm](https://en.wikipedia.org/wiki/Seidel%27s_algorithm)
- **Language:** en
- **Page ID:** 55206702

## Summary
Seidel's algorithm is an algorithm designed by Raimund Seidel in 1992 for the all-pairs-shortest-path problem for undirected, unweighted, connected graphs. It solves the problem in 
  
    
      
        O
        (
        
          V
          
            ω
          
        
        log
        ⁡
        V
        )
      
    
    {\displaystyle O(V^{\omega }\log V)}
  
 expected time for a graph with 
  
    
      
        V
      
    
    {\displaystyle V}
  
 vertices, where 
  
    
      
        ω
        <
        2.373
      
    
    {\displaystyle \omega <2.373}
  
 is the exponent in the complexity 
  
    
      
        O
        (
        
          n
          
            ω
          
        
        )
      
    
    {\displaystyle O(n^{\omega })}
  
 of 
  
    
      
        n
        ×
        n
      
    
    {\displaystyle n\times n}
  
 matrix multiplication. If only the distances between each pair of vertices are sought, the same time bound can be achieved in the worst case. Even though the algorithm is designed for connected graphs, it can be applied individually to each connected component of a graph with the same running time overall. There is an exception to the expected running time given above for computing the paths: if 
  
    
      
        ω
        =
        2
      
    
    {\displaystyle \omega =2}
  
 the expected running time becomes 
  
    
      
        O
        (
        
          V
          
            2
          
        
        
          log
          
            2
          
        
        ⁡
        V
        )
      
    
    {\displaystyle O(V^{2}\log ^{2}V)}
  
.

## Categories
This article belongs to the following categories:

- Category:Articles with example Python (programming language) code
- Category:Computational problems in graph theory
- Category:Graph algorithms
- Category:Graph distance
- Category:Polynomial-time problems

## Table of Contents

- Details of the implementation
- Graphs with weights from finite universes

## Content

Seidel's algorithm is an algorithm designed by Raimund Seidel in 1992 for the all-pairs-shortest-path problem for undirected, unweighted, connected graphs. It solves the problem in 
  
    
      
        O
        (
        
          V
          
            ω
          
        
        log
        ⁡
        V
        )
      
    
    {\displaystyle O(V^{\omega }\log V)}
  
 expected time for a graph with 
  
    
      
        V
      
    
    {\displaystyle V}
  
 vertices, where 
  
    
      
        ω
        <
        2.373
      
    
    {\displaystyle \omega <2.373}
  
 is the exponent in the complexity 
  
    
      
        O
        (
        
          n
          
            ω
          
        
        )
      
    
    {\displaystyle O(n^{\omega })}
  
 of 
  
    
      
        n
        ×
        n
      
    
    {\displaystyle n\times n}
  
 matrix multiplication. If only the distances between each pair of vertices are sought, the same time bound can be achieved in the worst case. Even though the algorithm is designed for connected graphs, it can be applied individually to each connected component of a graph with the same running time overall. There is an exception to the expected running time given above for computing the paths: if 
  
    
      
        ω
        =
        2
      
    
    {\displaystyle \omega =2}
  
 the expected running time becomes 
  
    
      
        O
        (
        
          V
          
            2
          
        
        
          log
          
            2
          
        
        ⁡
        V
        )
      
    
    {\displaystyle O(V^{2}\log ^{2}V)}
  
.

Details of the implementation
The core of the algorithm is a procedure that computes the length of the shortest-paths between any pair of vertices.
In the worst case this can be done in 
  
    
      
        O
        (
        
          V
          
            ω
          
        
        log
        ⁡
        V
        )
      
    
    {\displaystyle O(V^{\omega }\log V)}
  
 time. Once the lengths are computed, the paths can be reconstructed using a Las Vegas algorithm whose expected running time is 
  
    
      
        O
        (
        
          V
          
            ω
          
        
        log
        ⁡
        V
        )
      
    
    {\displaystyle O(V^{\omega }\log V)}
  
 for 
  
    
      
        ω
        >
        2
      
    
    {\displaystyle \omega >2}
  
 and 
  
    
      
        O
        (
        
          V
          
            2
          
        
        
          log
          
            2
          
        
        ⁡
        V
        )
      
    
    {\displaystyle O(V^{2}\log ^{2}V)}
  
 for 
  
    
      
        ω
        =
        2
      
    
    {\displaystyle \omega =2}
  
.

Computing the shortest-paths lengths
The Python code below assumes the input graph is given as a 
  
    
      
        n
        ×
        n
      
    
    {\displaystyle n\times n}
  
 
  
    
      
        0
      
    
    {\displaystyle 0}
  
-
  
    
      
        1
      
    
    {\displaystyle 1}
  
 adjacency matrix 
  
    
      
        A
      
    
    {\displaystyle A}
  
 with zeros on the diagonal. It defines the function APD which returns a matrix with entries 
  
    
      
        
          D
          
            i
            ,
            j
          
        
      
    
    {\displaystyle D_{i,j}}
  
 such that 
  
    
      
        
          D
          
            i
            ,
            j
          
        
      
    
    {\displaystyle D_{i,j}}
  
 is the length of the shortest path between the vertices 
  
    
      
        i
      
    
    {\displaystyle i}
  
 and 
  
    
      
        j
      
    
    {\displaystyle j}
  
. The matrix class used can be any matrix class implementation supporting the multiplication, exponentiation, and indexing operators (for example numpy.matrix).

The base case tests whether the input adjacency matrix describes a complete graph, in which case all shortest paths have length 
  
    
      
        1
      
    
    {\displaystyle 1}
  
.

Graphs with weights from finite universes
Algorithms for undirected and directed graphs with weights from a finite universe 
  
    
      
        {
        1
        ,
        …
        ,
        M
        ,
        +
        ∞
        }
      
    
    {\displaystyle \{1,\ldots ,M,+\infty \}}
  
 also exist. The best known algorithm for the directed case is in time 
  
    
      
        
          
            
              O
              ~
            
          
        
        (
        
          M
          
            1
            
              /
            
            (
            4
            −
            ω
            )
          
        
        
          V
          
            2
            +
            1
            
              /
            
            (
            4
            −
            ω
            )
          
        
        )
      
    
    {\displaystyle {\tilde {O}}(M^{1/(4-\omega )}V^{2+1/(4-\omega )})}
  
 by Zwick in 1998. This algorithm uses rectangular matrix multiplication instead of square matrix multiplication. Better upper bounds can be obtained if one uses the best rectangular matrix multiplication algorithm available instead of achieving rectangular multiplication via multiple square matrix multiplications. The best known algorithm for the undirected case is in time 
  
    
      
        
          
            
              O
              ~
            
          
        
        (
        M
        
          V
          
            ω
          
        
        )
      
    
    {\displaystyle {\tilde {O}}(MV^{\omega })}
  
 by Shoshan and Zwick in 1999. The original implementation of this algorithm was erroneous and has been corrected by Eirinakis, Williamson, and Subramani in 2016.


== Notes ==

## Archive Info
- **Archived on:** 2024-12-15 20:26:55 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 6017 bytes
- **Word Count:** 562 words
