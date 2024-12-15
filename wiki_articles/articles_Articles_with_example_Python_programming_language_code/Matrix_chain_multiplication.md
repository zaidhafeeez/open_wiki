# Matrix chain multiplication

## Metadata
- **Last Updated:** 2024-12-15 19:51:41 UTC
- **Original Article:** [Matrix chain multiplication](https://en.wikipedia.org/wiki/Matrix_chain_multiplication)
- **Language:** en
- **Page ID:** 1538007

## Summary
Matrix chain multiplication (or the matrix chain ordering problem) is an optimization problem concerning the most efficient way to multiply a given sequence of matrices.  The problem is not actually to perform the multiplications, but merely to decide the sequence of the matrix multiplications involved.  The problem may be solved using dynamic programming.
There are many options because matrix multiplication is associative. In other words, no matter how the product is parenthesized, the result obtained will remain the same. For example, for four matrices A, B, C, and D, there are five possible options:

((AB)C)D = (A(BC))D = (AB)(CD) = A((BC)D) = A(B(CD)).
Although it does not affect the product, the order in which the terms are parenthesized affects the number of simple arithmetic operations needed to compute the product, that is, the computational complexity. The straightforward multiplication of a matrix that is X × Y by a matrix that is Y × Z requires XYZ ordinary multiplications and X(Y − 1)Z ordinary additions.  In this context, it is typical to use the number of ordinary multiplications as a measure of the runtime complexity.
If A is a 10 × 30 matrix, B is a 30 × 5 matrix, and C is a 5 × 60 matrix, then

computing (AB)C needs (10×30×5) + (10×5×60)  = 1500 + 3000 = 4500 operations, while
computing A(BC) needs (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.
Clearly the first method is more efficient. With this information, the problem statement can be refined as "how to determine the optimal parenthesization of a product of n matrices?" The number of possible parenthesizations is given by the (n–1)th Catalan  number, which is O(4n / n3/2), so checking each possible parenthesization (brute force) would require a run-time that is exponential in the number of matrices, which is very slow and impractical for large n. A quicker solution to this problem can be achieved by breaking up the problem into a set of related subproblems.

## Categories
This article belongs to the following categories:

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:CS1: long volume value
- Category:Dynamic programming
- Category:Matrices
- Category:Optimization algorithms and methods
- Category:Short description is different from Wikidata
- Category:Webarchive template wayback links

## Table of Contents

- A dynamic programming algorithm
- More efficient algorithms
- Generalizations
- See also

## Content

Matrix chain multiplication (or the matrix chain ordering problem) is an optimization problem concerning the most efficient way to multiply a given sequence of matrices.  The problem is not actually to perform the multiplications, but merely to decide the sequence of the matrix multiplications involved.  The problem may be solved using dynamic programming.
There are many options because matrix multiplication is associative. In other words, no matter how the product is parenthesized, the result obtained will remain the same. For example, for four matrices A, B, C, and D, there are five possible options:

((AB)C)D = (A(BC))D = (AB)(CD) = A((BC)D) = A(B(CD)).
Although it does not affect the product, the order in which the terms are parenthesized affects the number of simple arithmetic operations needed to compute the product, that is, the computational complexity. The straightforward multiplication of a matrix that is X × Y by a matrix that is Y × Z requires XYZ ordinary multiplications and X(Y − 1)Z ordinary additions.  In this context, it is typical to use the number of ordinary multiplications as a measure of the runtime complexity.
If A is a 10 × 30 matrix, B is a 30 × 5 matrix, and C is a 5 × 60 matrix, then

computing (AB)C needs (10×30×5) + (10×5×60)  = 1500 + 3000 = 4500 operations, while
computing A(BC) needs (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.
Clearly the first method is more efficient. With this information, the problem statement can be refined as "how to determine the optimal parenthesization of a product of n matrices?" The number of possible parenthesizations is given by the (n–1)th Catalan  number, which is O(4n / n3/2), so checking each possible parenthesization (brute force) would require a run-time that is exponential in the number of matrices, which is very slow and impractical for large n. A quicker solution to this problem can be achieved by breaking up the problem into a set of related subproblems.

A dynamic programming algorithm
To begin, let us assume that all we really want to know is the minimum cost, or minimum number of arithmetic operations needed to multiply out the matrices. If we are only multiplying two matrices, there is only one way to multiply them, so the minimum cost is the cost of doing this. In general, we can find the minimum cost using the following recursive algorithm:

Take the sequence of matrices and separate it into two subsequences.
Find the minimum cost of multiplying out each subsequence.
Add these costs together, and add in the cost of multiplying the two result matrices.
Do this for each possible position at which the sequence of matrices can be split, and take the minimum over all of them.
For example, if we have four matrices ABCD, we compute the cost required to find each of (A)(BCD), (AB)(CD), and (ABC)(D), making recursive calls to find the minimum cost to compute ABC, AB, CD, and BCD. We then choose the best one. Better still, this yields not only the minimum cost, but also demonstrates the best way of doing the multiplication: group it the way that yields the lowest total cost, and do the same for each factor.
However, this algorithm has exponential runtime complexity making it as inefficient as the naive approach of trying all permutations. The reason is that the algorithm does a lot of redundant work. For example, above we made a recursive call to find the best cost for computing both ABC and AB. But finding the best cost for computing ABC also requires finding the best cost for AB. As the recursion grows deeper, more and more of this type of unnecessary repetition occurs.
One simple solution is called memoization: each time we compute the minimum cost needed to multiply out a specific subsequence, we save it. If we are ever asked to compute it again, we simply give the saved answer, and do not recompute it. Since there are about n2/2 different subsequences, where n is the number of matrices, the space required to do this is reasonable. It can be shown that this simple trick brings the runtime down to O(n3) from O(2n), which is more than efficient enough for real applications. This is top-down dynamic programming.
The following bottom-up approach computes, for each 2 ≤ k ≤ n, the minimum costs of all subsequences of length k using the costs of smaller subsequences already computed.
It has the same asymptotic runtime and requires no recursion.
Pseudocode:

Note : The first index for dims is 0 and the first index for m and s is 1.
A  Python implementation using the memoization decorator from the standard library:

More efficient algorithms
There are algorithms that are more efficient than the O(n3) dynamic programming algorithm, though they are more complex.

Hu & Shing
An algorithm published by T. C. Hu and M.-T. Shing achieves O(n log n) computational complexity.
They showed how the matrix chain multiplication problem can be transformed (or reduced) into the problem of triangulation of a regular polygon.  The polygon is oriented such that there is a horizontal bottom side, called the base, which represents the final result. The other n sides of the polygon, in the clockwise direction, represent the matrices. The vertices on each end of a side are the dimensions of the matrix represented by that side.  With n matrices in the multiplication chain there are n−1 binary operations and Cn−1 ways of placing parentheses, where Cn−1 is the (n−1)-th Catalan number. The algorithm exploits that there are also Cn−1 possible triangulations of a polygon with n+1 sides.
This image illustrates possible triangulations of a regular hexagon.  These correspond to the different ways that parentheses can be placed to order the multiplications for a product of 5 matrices.

For the example below, there are four sides: A, B, C and the final result ABC.  A is a 10×30 matrix, B is a 30×5 matrix, C is a 5×60 matrix, and the final result is a 10×60 matrix. The regular polygon for this example is a 4-gon, i.e. a square:

The matrix product AB is a 10x5 matrix and BC is a 30x60 matrix. The two possible triangulations in this example are:

		
			
			
		
		
			
			
		

The cost of a single triangle in terms of the number of multiplications needed is the product of its vertices. The total cost of a particular triangulation of the polygon is the sum of the costs of all its triangles:

(AB)C: (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 multiplications
A(BC): (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 multiplications
Hu & Shing developed an algorithm that finds an optimum solution for the minimum cost partition problem in O(n log n) time. Their proof of correctness of the algorithm relies on "Lemma 1" proved in a 1981 technical report and omitted from the published paper. The technical report's proof of the lemma is incorrect, but Shing has presented a corrected proof.

Other O(n log n) algorithms
Wang, Zhu and Tian have published a simplified O(n log m) algorithm, where n is the number of matrices in the chain and m is the number of local minimums in the dimension sequence of the given matrix chain.
Nimbark, Gohel, and Doshi have published a greedy O(n log n) algorithm, but their proof of optimality is incorrect and their algorithm fails to produce the most efficient parentheses assignment for some matrix chains.

Chin-Hu-Shing approximate solution
An algorithm created independently by Chin and Hu & Shing runs in O(n) and produces a parenthesization which is at most 15.47% worse than the optimal choice. In most cases the algorithm yields the optimal solution or a solution which is only 1-2 percent worse than the optimal one.
The algorithm starts by translating the problem to the polygon partitioning problem. To each vertex V of the polygon is associated a weight w. Suppose we have three consecutive vertices 
  
    
      
        
          V
          
            i
            −
            1
          
        
        ,
        
          V
          
            i
          
        
        ,
        
          V
          
            i
            +
            1
          
        
      
    
    {\displaystyle V_{i-1},V_{i},V_{i+1}}
  
, and that 
  
    
      
        
          V
          
            min
          
        
      
    
    {\displaystyle V_{\min }}
  
 is the vertex with minimum weight 
  
    
      
        
          w
          
            min
          
        
      
    
    {\displaystyle w_{\min }}
  
.
We look at the quadrilateral with vertices 
  
    
      
        
          V
          
            min
          
        
        ,
        
          V
          
            i
            −
            1
          
        
        ,
        
          V
          
            i
          
        
        ,
        
          V
          
            i
            +
            1
          
        
      
    
    {\displaystyle V_{\min },V_{i-1},V_{i},V_{i+1}}
  
 (in clockwise order).
We can triangulate it in two ways:

  
    
      
        (
        
          V
          
            min
          
        
        ,
        
          V
          
            i
            −
            1
          
        
        ,
        
          V
          
            i
          
        
        )
      
    
    {\displaystyle (V_{\min },V_{i-1},V_{i})}
  
 and 
  
    
      
        (
        
          V
          
            min
          
        
        ,
        
          V
          
            i
            +
            1
          
        
        ,
        
          V
          
            i
          
        
        )
      
    
    {\displaystyle (V_{\min },V_{i+1},V_{i})}
  
, with cost 
  
    
      
        
          w
          
            min
          
        
        
          w
          
            i
            −
            1
          
        
        
          w
          
            i
          
        
        +
        
          w
          
            min
          
        
        
          w
          
            i
            +
            1
          
        
        
          w
          
            i
          
        
      
    
    {\displaystyle w_{\min }w_{i-1}w_{i}+w_{\min }w_{i+1}w_{i}}
  

  
    
      
        (
        
          V
          
            min
          
        
        ,
        
          V
          
            i
            −
            1
          
        
        ,
        
          V
          
            i
            +
            1
          
        
        )
      
    
    {\displaystyle (V_{\min },V_{i-1},V_{i+1})}
  
 and 
  
    
      
        (
        
          V
          
            i
            −
            1
          
        
        ,
        
          V
          
            i
          
        
        ,
        
          V
          
            i
            +
            1
          
        
        )
      
    
    {\displaystyle (V_{i-1},V_{i},V_{i+1})}
  
 with cost 
  
    
      
        
          w
          
            min
          
        
        
          w
          
            i
            −
            1
          
        
        
          w
          
            i
            +
            1
          
        
        +
        
          w
          
            i
            −
            1
          
        
        
          w
          
            i
          
        
        
          w
          
            i
            +
            1
          
        
      
    
    {\displaystyle w_{\min }w_{i-1}w_{i+1}+w_{i-1}w_{i}w_{i+1}}
  
.
Therefore, if

  
    
      
        
          w
          
            min
          
        
        
          w
          
            i
            −
            1
          
        
        
          w
          
            i
            +
            1
          
        
        +
        
          w
          
            i
            −
            1
          
        
        
          w
          
            i
          
        
        
          w
          
            i
            +
            1
          
        
        <
        
          w
          
            min
          
        
        
          w
          
            i
            −
            1
          
        
        
          w
          
            i
          
        
        +
        
          w
          
            min
          
        
        
          w
          
            i
            +
            1
          
        
        
          w
          
            i
          
        
      
    
    {\displaystyle w_{\min }w_{i-1}w_{i+1}+w_{i-1}w_{i}w_{i+1}<w_{\min }w_{i-1}w_{i}+w_{\min }w_{i+1}w_{i}}
  

or equivalently

  
    
      
        
          
            1
            
              w
              
                i
              
            
          
        
        +
        
          
            1
            
              w
              
                min
              
            
          
        
        <
        
          
            1
            
              w
              
                i
                +
                1
              
            
          
        
        +
        
          
            1
            
              w
              
                i
                −
                1
              
            
          
        
      
    
    {\displaystyle {\frac {1}{w_{i}}}+{\frac {1}{w_{\min }}}<{\frac {1}{w_{i+1}}}+{\frac {1}{w_{i-1}}}}
  

we remove the vertex 
  
    
      
        
          V
          
            i
          
        
      
    
    {\displaystyle V_{i}}
  
 from the polygon and add the side 
  
    
      
        (
        
          V
          
            i
            −
            1
          
        
        ,
        
          V
          
            i
            +
            1
          
        
        )
      
    
    {\displaystyle (V_{i-1},V_{i+1})}
  
 to the triangulation.
We repeat this process until no 
  
    
      
        
          V
          
            i
          
        
      
    
    {\displaystyle V_{i}}
  
 satisfies the condition above.
For all the remaining vertices 
  
    
      
        
          V
          
            n
          
        
      
    
    {\displaystyle V_{n}}
  
, we add the side 
  
    
      
        (
        
          V
          
            min
          
        
        ,
        
          V
          
            n
          
        
        )
      
    
    {\displaystyle (V_{\min },V_{n})}
  
 to the triangulation. 
This gives us a nearly optimal triangulation.

Generalizations
The matrix chain multiplication problem generalizes to solving a more abstract problem: given a linear sequence of objects, an associative binary operation on those objects, and a way to compute the cost of performing that operation on any two given objects (as well as all partial results), compute the minimum cost way to group the objects to apply the operation over the sequence. A practical instance of this comes from the ordering of join operations in databases; see Query optimization § Join ordering.
Another somewhat contrived special case of this is string concatenation of a list of strings. In C, for example, the cost of concatenating two strings of length m and n using strcat is O(m + n), since we need O(m) time to find the end of the first string and O(n) time to copy the second string onto the end of it. Using this cost function, we can write a dynamic programming algorithm to find the fastest way to concatenate a sequence of strings. However, this optimization is rather useless because we can straightforwardly concatenate the strings in time proportional to the sum of their lengths. A similar problem exists for singly linked lists.
Another generalization is to solve the problem when parallel processors are available. In this case, instead of adding the costs of computing each factor of a matrix product, we take the maximum because we can do them simultaneously. This can drastically affect both the minimum cost and the final optimal grouping; more "balanced" groupings that keep all the processors busy are favored. There are even more sophisticated approaches.

See also
Associahedron
Tamari lattice


== References ==

## Archive Info
- **Archived on:** 2024-12-15 21:05:12 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 16507 bytes
- **Word Count:** 1934 words
