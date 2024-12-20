---
title: Maximum subarray problem
url: https://en.wikipedia.org/wiki/Maximum_subarray_problem
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Dynamic programming", "Category:Optimization algorithms and methods", "Category:Short description is different from Wikidata"]
references: 0
last_modified: 2024-12-19T14:02:54Z
---

# Maximum subarray problem

## Summary

In computer science, the maximum sum subarray problem, also known as the maximum segment sum problem, is the task of finding a contiguous subarray with the largest sum, within a given one-dimensional array A[1...n] of numbers. It can be solved in 
  
    
      
        O
        (
        n
        )
      
    
    {\displaystyle O(n)}
  
 time and 
  
    
      
        O
        (
        1
        )
      
    
    {\displaystyle O(1)}
  
 space.
Formally, the task is to find indices 
  
 

## Full Content

In computer science, the maximum sum subarray problem, also known as the maximum segment sum problem, is the task of finding a contiguous subarray with the largest sum, within a given one-dimensional array A[1...n] of numbers. It can be solved in 
  
    
      
        O
        (
        n
        )
      
    
    {\displaystyle O(n)}
  
 time and 
  
    
      
        O
        (
        1
        )
      
    
    {\displaystyle O(1)}
  
 space.
Formally, the task is to find indices 
  
    
      
        i
      
    
    {\displaystyle i}
  
 and 
  
    
      
        j
      
    
    {\displaystyle j}
  
 with 
  
    
      
        1
        ≤
        i
        ≤
        j
        ≤
        n
      
    
    {\displaystyle 1\leq i\leq j\leq n}
  
, such that the sum

  
    
      
        
          ∑
          
            x
            =
            i
          
          
            j
          
        
        A
        [
        x
        ]
      
    
    {\displaystyle \sum _{x=i}^{j}A[x]}
  

is as large as possible. (Some formulations of the problem also allow the empty subarray to be considered; by convention, the sum of all values of the empty subarray is zero.)  Each number in the input array A could be positive, negative, or zero.
For example, for the array of values [−2, 1, −3, 4, −1, 2, 1, −5, 4], the contiguous subarray with the largest sum is [4, −1, 2, 1], with sum 6.
Some properties of this problem are: 

If the array contains all non-negative numbers, then the problem is trivial; a maximum subarray is the entire array.
If the array contains all non-positive numbers, then a solution is any subarray of size 1 containing the maximal value of the array (or the empty subarray, if it is permitted).
Several different sub-arrays may have the same maximum sum.
Although this problem can be solved using several different algorithmic techniques, including brute force, divide and conquer, dynamic programming, and reduction to shortest paths, a simple single-pass algorithm known as Kadane's algorithm solves it efficiently.

History
The maximum subarray problem was proposed by Ulf Grenander in 1977 as a simplified model for maximum likelihood estimation of patterns in digitized images.
Grenander was looking to find a rectangular subarray with maximum sum, in a two-dimensional array of real numbers.  A brute-force algorithm for the two-dimensional problem runs in O(n6) time; because this was prohibitively slow, Grenander proposed the one-dimensional problem to gain insight into its structure.  Grenander derived an algorithm that solves the one-dimensional problem in O(n2) time,
improving the brute force running time of O(n3). When Michael Shamos heard about the problem, he overnight devised an O(n log n) divide-and-conquer algorithm for it.
Soon after, Shamos described the one-dimensional problem and its history at a Carnegie Mellon University seminar attended by Jay Kadane, who designed within a minute an O(n)-time algorithm, which is as fast as possible. In 1982, David Gries obtained the same O(n)-time algorithm by applying Dijkstra's "standard strategy"; in 1989, Richard Bird derived it by purely algebraic manipulation of the brute-force algorithm using the Bird–Meertens formalism.
Grenander's two-dimensional generalization can be solved in O(n3) time either by using Kadane's algorithm as a subroutine, or through a divide-and-conquer approach.  Slightly faster algorithms based on distance matrix multiplication have been proposed by Tamaki & Tokuyama (1998) and by Takaoka (2002). There is some evidence that no significantly faster algorithm exists; an algorithm that solves the two-dimensional maximum subarray problem in O(n3−ε) time, for any ε>0, would imply a similarly fast algorithm for the all-pairs shortest paths problem.

Applications
Maximum subarray problems arise in many fields, such as genomic sequence analysis and computer vision.
Genomic sequence analysis employs maximum subarray algorithms to identify important biological segments of protein sequences that have unusual properties, by assigning scores to points within the sequence that are positive when a motif to be recognized is present, and negative when it is not, and then seeking the maximum subarray among these scores. These problems include conserved segments, GC-rich regions, tandem repeats, low-complexity filter, DNA binding domains, and regions of high charge.
In computer vision, bitmap images generally consist only of positive values, for which the maximum subarray problem is trivial: the result is always the whole array. However, after subtracting a threshold value (such as the average pixel value) from each pixel, so that above-average pixels will be positive and below-average pixels will be negative, the maximum subarray problem can be applied to the modified image to detect bright areas within it.

Kadane's algorithm
No empty subarrays admitted
Kadane's algorithm scans the given array 
  
    
      
        A
        [
        1
        …
        n
        ]
      
    
    {\displaystyle A[1\ldots n]}
  
 from left to right. 
In the 
  
    
      
        j
      
    
    {\displaystyle j}
  
th step, it computes the subarray with the largest sum ending at 
  
    
      
        j
      
    
    {\displaystyle j}
  
; this sum is maintained in variable current_sum.
Moreover, it computes the subarray with the largest sum anywhere in 
  
    
      
        A
        [
        1
        …
        j
        ]
      
    
    {\displaystyle A[1\ldots j]}
  
, maintained in variable best_sum,
and easily obtained as the maximum of all values of current_sum seen so far, cf. line 7 of the algorithm.
As a loop invariant, in the 
  
    
      
        j
      
    
    {\displaystyle j}
  
th step, the old value of current_sum holds the maximum over all 
  
    
      
        i
        ∈
        {
        1
        ,
        …
        ,
        j
        −
        1
        }
      
    
    {\displaystyle i\in \{1,\ldots ,j-1\}}
  
 of the sum 
  
    
      
        A
        [
        i
        ]
        +
        ⋯
        +
        A
        [
        j
        −
        1
        ]
      
    
    {\displaystyle A[i]+\cdots +A[j-1]}
  
.
Therefore, current_sum
  
    
      
        +
        A
        [
        j
        ]
      
    
    {\displaystyle +A[j]}
  

is the maximum over all 
  
    
      
        i
        ∈
        {
        1
        ,
        …
        ,
        j
        −
        1
        }
      
    
    {\displaystyle i\in \{1,\ldots ,j-1\}}
  
 of the sum 
  
    
      
        A
        [
        i
        ]
        +
        ⋯
        +
        A
        [
        j
        ]
      
    
    {\displaystyle A[i]+\cdots +A[j]}
  
. To extend the latter maximum to cover also the case 
  
    
      
        i
        =
        j
      
    
    {\displaystyle i=j}
  
, it is sufficient to consider also the singleton subarray 
  
    
      
        A
        [
        j
        
        …
        
        j
        ]
      
    
    {\displaystyle A[j\;\ldots \;j]}
  
. This is done in line 6 by assigning 
  
    
      
        max
        (
        A
        [
        j
        ]
        ,
      
    
    {\displaystyle \max(A[j],}
  
current_sum
  
    
      
        +
        A
        [
        j
        ]
        )
      
    
    {\displaystyle +A[j])}
  
 as the new value of current_sum, which after that holds the maximum over all 
  
    
      
        i
        ∈
        {
        1
        ,
        …
        ,
        j
        }
      
    
    {\displaystyle i\in \{1,\ldots ,j\}}
  
 of the sum 
  
    
      
        A
        [
        i
        ]
        +
        ⋯
        +
        A
        [
        j
        ]
      
    
    {\displaystyle A[i]+\cdots +A[j]}
  
.
Thus, the problem can be solved with the following code, expressed in Python. 

If the input contains no positive element, the returned value is that of the largest element (i.e., the value closest to 0), or negative infinity if the input was empty. For correctness, an exception should be raised when the input array is empty, since an empty array has no maximum nonempty subarray. If the array is nonempty, its first element could be used in place of negative infinity, if needed to avoid mixing numeric and non-numeric values.
The algorithm can be adapted to the case which allows empty subarrays or to keep track of the starting and ending indices of the maximum subarray.
This algorithm calculates the maximum subarray ending at each position from the maximum subarray ending at the previous position, so it can be viewed as a case of dynamic programming.

Empty subarrays admitted
Kadane's original algorithm solves the problem variant when empty subarrays are admitted. 
This variant will return 0 if the input contains no positive elements (including when the input is empty).
It is obtained by two changes in code: in line 3, best_sum should be initialized to 0 to account for the empty subarray 
  
    
      
        A
        [
        0
        …
        −
        1
        ]
      
    
    {\displaystyle A[0\ldots -1]}
  

and line 6 in the for loop current_sum should be updated as max(0, current_sum + x).

As a loop invariant, in the 
  
    
      
        j
      
    
    {\displaystyle j}
  
th step, the old value of current_sum holds the maximum over all 
  
    
      
        i
        ∈
        {
        1
        ,
        …
        ,
        j
        }
      
    
    {\displaystyle i\in \{1,\ldots ,j\}}
  
 of the sum 
  
    
      
        A
        [
        i
        ]
        +
        ⋯
        +
        A
        [
        j
        −
        1
        ]
      
    
    {\displaystyle A[i]+\cdots +A[j-1]}
  
.
Therefore, current_sum
  
    
      
        +
        A
        [
        j
        ]
      
    
    {\displaystyle +A[j]}
  

is the maximum over all 
  
    
      
        i
        ∈
        {
        1
        ,
        …
        ,
        j
        }
      
    
    {\displaystyle i\in \{1,\ldots ,j\}}
  
 of the sum 
  
    
      
        A
        [
        i
        ]
        +
        ⋯
        +
        A
        [
        j
        ]
      
    
    {\displaystyle A[i]+\cdots +A[j]}
  
. To extend the latter maximum to cover also the case 
  
    
      
        i
        =
        j
        +
        1
      
    
    {\displaystyle i=j+1}
  
, it is sufficient to consider also the empty subarray 
  
    
      
        A
        [
        j
        +
        1
        
        …
        
        j
        ]
      
    
    {\displaystyle A[j+1\;\ldots \;j]}
  
. This is done in line 6 by assigning 
  
    
      
        max
        (
        0
        ,
      
    
    {\displaystyle \max(0,}
  
current_sum
  
    
      
        +
        A
        [
        j
        ]
        )
      
    
    {\displaystyle +A[j])}
  
 as the new value of current_sum, which after that holds the maximum over all 
  
    
      
        i
        ∈
        {
        1
        ,
        …
        ,
        j
        +
        1
        }
      
    
    {\displaystyle i\in \{1,\ldots ,j+1\}}
  
 of the sum 
  
    
      
        A
        [
        i
        ]
        +
        ⋯
        +
        A
        [
        j
        ]
      
    
    {\displaystyle A[i]+\cdots +A[j]}
  
. Machine-verified C / Frama-C code of both variants can be found here.

Computing the best subarray's position
The algorithm can be modified to keep track of the starting and ending indices of the maximum subarray as well.
Because of the way this algorithm uses optimal substructures (the maximum subarray ending at each position is calculated in a simple way from a related but smaller and overlapping subproblem: the maximum subarray ending at the previous position) this algorithm can be viewed as a simple/trivial example of dynamic programming.

Complexity
The runtime complexity of Kadane's algorithm is 
  
    
      
        O
        (
        n
        )
      
    
    {\displaystyle O(n)}
  
 and its space complexity is 
  
    
      
        O
        (
        1
        )
      
    
    {\displaystyle O(1)}
  
.

Generalizations
Similar problems may be posed for higher-dimensional arrays, but their solutions are more complicated; see, e.g., Takaoka (2002). Brodal & Jørgensen (2007) showed how to find the k largest subarray sums in a one-dimensional array, in the optimal time bound 
  
    
      
        O
        (
        n
        +
        k
        )
      
    
    {\displaystyle O(n+k)}
  
.
The Maximum sum k-disjoint subarrays can also be computed in the optimal time bound 
  
    
      
        O
        (
        n
        +
        k
        )
      
    
    {\displaystyle O(n+k)}
  
 
.

See also
Subset sum problem

Notes
Notes
References
Alves, Carlos E. R.; Cáceres, Edson; Song, Siang W. (2004), "BSP/CGM Algorithms for Maximum Subsequence and Maximum Subarray", in Kranzlmüller, Dieter; Kacsuk, Péter; Dongarra, Jack J. (eds.), Recent Advances in Parallel Virtual Machine and Message Passing Interface, 11th European PVM/MPI Users' Group Meeting, Budapest, Hungary, September 19-22, 2004, Proceedings, Lecture Notes in Computer Science, vol. 3241, Springer, pp. 139–146, doi:10.1007/978-3-540-30218-6_24, ISBN 978-3-540-23163-9
Backurs, Arturs; Dikkala, Nishanth; Tzamos, Christos (2016), "Tight Hardness Results for Maximum Weight Rectangles", Proc. 43rd International Colloquium on Automata, Languages, and Programming: 81:1–81:13, doi:10.4230/LIPIcs.ICALP.2016.81, S2CID 12720136
Bae, Sung Eun (2007), Sequential and Parallel Algorithms for the Generalized Maximum Subarray Problem (PDF) (Ph.D. thesis), University of Canterbury, S2CID 2681670, archived from the original (PDF) on 2017-10-26.
Bae, Sung Eun; Takaoka, Tadao (2006), "Improved Algorithms for the \emph{K}-Maximum Subarray Problem", The Computer Journal, 49 (3): 358–374, doi:10.1093/COMJNL/BXL007
Bengtsson, Fredrik; Chen, Jingsen (2007), Computing maximum-scoring segments optimally (PDF) (Research report), Luleå University of Technology
Bentley, Jon (1984), "Programming Pearls: Algorithm Design Techniques", Communications of the ACM, 27 (9): 865–873, doi:10.1145/358234.381162, S2CID 207565329
Bentley, Jon (May 1989), Programming Pearls (2nd? ed.), Reading, MA: Addison Wesley, ISBN 0-201-10331-1
Bird, Richard S. (1989), "Algebraic Identities for Program Calculation", The Computer Journal, 32 (2): 122–126, doi:10.1093/comjnl/32.2.122
Brodal, Gerth Stølting; Jørgensen, Allan Grønlund (2007), "A linear time algorithm for the k maximal sums problem", Mathematical Foundations of Computer Science 2007, Lecture Notes in Computer Science, vol. 4708, Springer-Verlag, pp. 442–453, doi:10.1007/978-3-540-74456-6_40, ISBN 978-3-540-74455-9.
Gries, David (1982), "A Note on the Standard Strategy for Developing Loop Invariants and Loops" (PDF), Science of Computer Programming, 2 (3): 207–241, doi:10.1016/0167-6423(83)90015-1, hdl:1813/6370
Ruzzo, Walter L.; Tompa, Martin (1999), "A Linear Time Algorithm for Finding All Maximal Scoring Subsequences", in Lengauer, Thomas; Schneider, Reinhard; Bork, Peer; Brutlag, Douglas L.; Glasgow, Janice I.; Mewes, Hans-Werner; Zimmer, Ralf (eds.), Proceedings of the Seventh International Conference on Intelligent Systems for Molecular Biology, August 6–10, 1999, Heidelberg, Germany, AAAI, pp. 234–241
Takaoka, Tadao (2002), "Efficient algorithms for the maximum subarray problem by distance matrix multiplication", Electronic Notes in Theoretical Computer Science, 61: 191–200, doi:10.1016/S1571-0661(04)00313-5.
Tamaki, Hisao; Tokuyama, Takeshi (1998), "Algorithms for the Maximum Subarray Problem Based on Matrix Multiplication", Proceedings of the 9th Symposium on Discrete Algorithms (SODA): 446–452, ISBN 978-0-89871-410-4, retrieved November 17, 2018
Weddell, Stephen John; Read, Tristan; Thaher, Mohammed; Takaoka, Tadao (2013), "Maximum subarray algorithms for use in astronomical imaging", Journal of Electronic Imaging, 22 (4): 043011, Bibcode:2013JEI....22d3011W, doi:10.1117/1.JEI.22.4.043011

External links
TAN, Lirong. "Maximum Contiguous Subarray Sum Problems" (PDF). Archived from the original (PDF) on 2015-10-10. Retrieved 2017-10-26.
Mu, Shin-Cheng (2010). "The Maximum Segment Sum Problem: Its Origin, and a Derivation".
"Notes on Maximum Subarray Problem". 2012.
www.algorithmist.com
alexeigor.wikidot.com
greatest subsequential sum problem on Rosetta Code
geeksforgeeks page on Kadane's Algorithm
