# Bogosort

## Metadata
- **Last Updated:** 2024-12-07 15:58:14 UTC
- **Original Article:** [Bogosort](https://en.wikipedia.org/wiki/Bogosort)
- **Language:** en
- **Page ID:** 99870

## Summary
In computer science, bogosort (also known as permutation sort and stupid sort) is a sorting algorithm based on the generate and test paradigm. The function successively generates permutations of its input until it finds one that is sorted. It is not considered useful for sorting, but may be used for educational purposes, to contrast it with more efficient algorithms.
Two versions of this algorithm exist: a deterministic version that enumerates all permutations until it hits a sorted one, and a randomized version that randomly permutes its input. An analogy for the working of the latter version is to sort a deck of cards by throwing the deck into the air, picking the cards up at random, and repeating the process until the deck is sorted. In a worst-case scenario with this version, the random source is of low quality and happens to make the sorted permutation unlikely to occur. The algorithm's name is a portmanteau of the words bogus and sort.

## Categories
This article belongs to the following categories:

- Category:All articles with dead external links
- Category:Articles with dead external links from July 2020
- Category:Articles with example Python (programming language) code
- Category:Articles with permanently dead external links
- Category:Articles with short description
- Category:Comparison sorts
- Category:Short description is different from Wikidata
- Category:Use dmy dates from December 2021

## Table of Contents

- Description of the algorithm
- Running time and termination
- Related algorithms
- See also
- References
- External links

## Content

In computer science, bogosort (also known as permutation sort and stupid sort) is a sorting algorithm based on the generate and test paradigm. The function successively generates permutations of its input until it finds one that is sorted. It is not considered useful for sorting, but may be used for educational purposes, to contrast it with more efficient algorithms.
Two versions of this algorithm exist: a deterministic version that enumerates all permutations until it hits a sorted one, and a randomized version that randomly permutes its input. An analogy for the working of the latter version is to sort a deck of cards by throwing the deck into the air, picking the cards up at random, and repeating the process until the deck is sorted. In a worst-case scenario with this version, the random source is of low quality and happens to make the sorted permutation unlikely to occur. The algorithm's name is a portmanteau of the words bogus and sort.

Description of the algorithm
Pseudocode
The following is a description of the randomized algorithm in pseudocode:

while deck is not sorted:
    shuffle(deck)

C
An implementation in C:

Python
An implementation in Python 3:

This code assumes that data is a simple, mutable, array-like data structure—like Python's built-in list—whose elements can be compared without issue.

Running time and termination
If all elements to be sorted are distinct, the expected number of comparisons performed in the average case by randomized bogosort is asymptotically equivalent to (e − 1)n!, and the expected number of swaps in the average case equals (n − 1)n!. The expected number of swaps grows faster than the expected number of comparisons, because if the elements are not in order, this will usually be discovered after only a few comparisons, no matter how many elements there are; but the work of shuffling the collection is proportional to its size. In the worst case, the number of comparisons and swaps are both unbounded, for the same reason that a tossed coin might turn up heads any number of times in a row.
The best case occurs if the list as given is already sorted; in this case the expected number of comparisons is n − 1, and no swaps at all are carried out.
For any collection of fixed size, the expected running time of the algorithm is finite for much the same reason that the infinite monkey theorem holds: there is some probability of getting the right permutation, so given an unbounded number of tries it will almost surely eventually be chosen.

Related algorithms
Gorosort
A sorting algorithm introduced in the 2011 Google Code Jam. As long as the list is not in order, a subset of all elements is randomly permuted. If this subset is optimally chosen each time this is performed, the expected value of the total number of times this operation needs to be done is equal to the number of misplaced elements.

Bogobogosort
An algorithm that recursively calls itself with smaller and smaller copies of the beginning of the list to see if they are sorted.  The base case is a single element, which is always sorted. For other cases, it compares the last element to the maximum element from the previous elements in the list.  If the last element is greater or equal, it checks if the order of the copy matches the previous version, and if so returns. Otherwise, it reshuffles the current copy of the list and restarts its recursive check.

Bozosort
Another sorting algorithm based on random numbers. If the list is not in order, it picks two items at random and swaps them, then checks to see if the list is sorted. The running time analysis of a bozosort is more difficult, but some estimates are found in H. Gruber's analysis of "perversely awful" randomized sorting algorithms. O(n!) is found to be the expected average case.

Worstsort
A pessimal sorting algorithm that is guaranteed to complete in finite time; however, its efficiency can be arbitrarily bad, depending on its configuration. The worstsort algorithm is based on a bad sorting algorithm, badsort. The badsort algorithm accepts two parameters: L, which is the list to be sorted, and k, which is a recursion depth. At recursion level k = 0, badsort merely uses a common sorting algorithm, such as bubblesort, to sort its inputs and return the sorted list. That is to say, badsort(L, 0) = bubblesort(L). Therefore, badsort's time complexity is O(n2) if k = 0. However, for any k > 0, badsort(L, k) first generates P, the list of all permutations of L. Then, badsort calculates badsort(P, k − 1), and returns the first element of the sorted P. To make worstsort truly pessimal, k may be assigned to the value of a computable increasing function such as 
  
    
      
        f
        :
        
          N
        
        →
        
          N
        
      
    
    {\displaystyle f\colon \mathbb {N} \to \mathbb {N} }
  
 (e.g. f(n) = A(n, n), where A is Ackermann's function).  Therefore, to sort a list arbitrarily badly, one would execute worstsort(L, f) = badsort(L, f(length(L))), where length(L) is the number of elements in L. The resulting algorithm has complexity 
  
    
      
        Ω
        
          (
          
            
              (
              
                n
                
                  !
                  
                    (
                    f
                    (
                    n
                    )
                    )
                  
                
              
              )
            
            
              2
            
          
          )
        
      
    
    {\textstyle \Omega \left(\left(n!^{(f(n))}\right)^{2}\right)}
  
, where 
  
    
      
        n
        
          !
          
            (
            m
            )
          
        
        =
        (
        …
        (
        (
        n
        !
        )
        !
        )
        !
        …
        )
        !
      
    
    {\displaystyle n!^{(m)}=(\dotso ((n!)!)!\dotso )!}
  
 = factorial of n iterated m times. This algorithm can be made as inefficient as one wishes by picking a fast enough growing function f.
Slowsort
A different humorous sorting algorithm that employs a misguided divide-and-conquer strategy to achieve massive complexity.
Quantum bogosort
A hypothetical sorting algorithm based on bogosort, created as an in-joke among computer scientists. The algorithm generates a random permutation of its input using a quantum source of entropy, checks if the list is sorted, and, if it is not, destroys the universe. Assuming that the many-worlds interpretation holds, the use of this algorithm will result in at least one surviving universe where the input was successfully sorted in O(n) time.
Miracle sort
A sorting algorithm that checks if the array is sorted until a miracle occurs. It continually checks the array until it is sorted, never changing the order of the array. Because the order is never altered, the algorithm has a hypothetical time complexity of O(∞), but it can still sort through events such as miracles or single-event upsets. Particular care must be taken in the implementation of this algorithm as optimizing compilers may simply transform it into a while(true) loop. However, the best case is O(n), which happens on a sorted list. Since it only makes comparisons, it is both strictly in-place and stable.
Bozobogo sort
A sorting algorithm that only works if the list is already in order, otherwise, the conditions of miracle sort are applied.
Divine sort
A sorting algorithm that takes a list and decides that because there is such a low probability that the list randomly  occurred in its current permutation (a probability of 1/n!, where n is the number of elements), there must have been a reason for the list's order. Therefore, it should be considered sorted in a way we don't understand, and we do not have any right to sort it to our beliefs, as if it were sorted "as God intended." Also known as Intelligent Design sort.

See also
Las Vegas algorithm
Stooge sort

References
External links

BogoSort on WikiWikiWeb
Inefficient sort algorithms
Bogosort: an implementation that runs on Unix-like systems, similar to the standard sort program.
Bogosort and jmmcg::bogosort: Simple, yet perverse, C++ implementations of the bogosort algorithm.
Bogosort NPM package: bogosort implementation for Node.js ecosystem.
Max Sherman Bogo-sort is Sort of Slow, June 2013

## Archive Info
- **Archived on:** 2024-12-15 21:03:42 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 8447 bytes
- **Word Count:** 1283 words
