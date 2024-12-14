# Bogosort

## Article Metadata

- **Last Updated:** 2024-12-14T19:34:02.046673+00:00
- **Original Article:** [Bogosort](https://en.wikipedia.org/wiki/Bogosort)
- **Language:** en
- **Page ID:** 99870

## Summary

In computer science, bogosort (also known as permutation sort and stupid sort) is a sorting algorithm based on the generate and test paradigm. The function successively generates permutations of its input until it finds one that is sorted. It is not considered useful for sorting, but may be used for educational purposes, to contrast it with more efficient algorithms.
Two versions of this algorithm exist: a deterministic version that enumerates all permutations until it hits a sorted one, and a r

## Categories

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

## Related Articles

### Internal Links

- [Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function)
- [Adaptive sort](https://en.wikipedia.org/wiki/Adaptive_sort)
- [Almost surely](https://en.wikipedia.org/wiki/Almost_surely)
- [American flag sort](https://en.wikipedia.org/wiki/American_flag_sort)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Array (data structure)](https://en.wikipedia.org/wiki/Array_(data_structure))
- [Asymptotic analysis](https://en.wikipedia.org/wiki/Asymptotic_analysis)
- [Batcher odd–even mergesort](https://en.wikipedia.org/wiki/Batcher_odd%E2%80%93even_mergesort)
- [Bead sort](https://en.wikipedia.org/wiki/Bead_sort)
- [Best, worst and average case](https://en.wikipedia.org/wiki/Best,_worst_and_average_case)
- [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Bitonic sorter](https://en.wikipedia.org/wiki/Bitonic_sorter)
- [Block sort](https://en.wikipedia.org/wiki/Block_sort)
- [Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort)
- [Bucket sort](https://en.wikipedia.org/wiki/Bucket_sort)
- [Burstsort](https://en.wikipedia.org/wiki/Burstsort)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Cartesian tree](https://en.wikipedia.org/wiki/Cartesian_tree)
- [Cascade merge sort](https://en.wikipedia.org/wiki/Cascade_merge_sort)
- [Cocktail shaker sort](https://en.wikipedia.org/wiki/Cocktail_shaker_sort)
- [Comb sort](https://en.wikipedia.org/wiki/Comb_sort)
- [Comparison sort](https://en.wikipedia.org/wiki/Comparison_sort)
- [Computational complexity theory](https://en.wikipedia.org/wiki/Computational_complexity_theory)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Counting sort](https://en.wikipedia.org/wiki/Counting_sort)
- [Cycle sort](https://en.wikipedia.org/wiki/Cycle_sort)
- [Playing card](https://en.wikipedia.org/wiki/Playing_card)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Expected value](https://en.wikipedia.org/wiki/Expected_value)
- [Flashsort](https://en.wikipedia.org/wiki/Flashsort)
- [Trial and error](https://en.wikipedia.org/wiki/Trial_and_error)
- [Gnome sort](https://en.wikipedia.org/wiki/Gnome_sort)
- [Google Code Jam](https://en.wikipedia.org/wiki/Google_Code_Jam)
- [Heapsort](https://en.wikipedia.org/wiki/Heapsort)
- [Hybrid algorithm](https://en.wikipedia.org/wiki/Hybrid_algorithm)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [In-joke](https://en.wikipedia.org/wiki/In-joke)
- [In-place algorithm](https://en.wikipedia.org/wiki/In-place_algorithm)
- [Infinite monkey theorem](https://en.wikipedia.org/wiki/Infinite_monkey_theorem)
- [Insertion sort](https://en.wikipedia.org/wiki/Insertion_sort)
- [Integer sorting](https://en.wikipedia.org/wiki/Integer_sorting)
- [Interpolation sort](https://en.wikipedia.org/wiki/Interpolation_sort)
- [Introsort](https://en.wikipedia.org/wiki/Introsort)
- [Kirkpatrick–Reisch sort](https://en.wikipedia.org/wiki/Kirkpatrick%E2%80%93Reisch_sort)
- [Las Vegas algorithm](https://en.wikipedia.org/wiki/Las_Vegas_algorithm)
- [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science)
- [Library sort](https://en.wikipedia.org/wiki/Library_sort)
- [List (abstract data type)](https://en.wikipedia.org/wiki/List_(abstract_data_type))
- [Many-worlds interpretation](https://en.wikipedia.org/wiki/Many-worlds_interpretation)
- [Merge-insertion sort](https://en.wikipedia.org/wiki/Merge-insertion_sort)
- [Merge sort](https://en.wikipedia.org/wiki/Merge_sort)
- [Miracle](https://en.wikipedia.org/wiki/Miracle)
- [Odd–even sort](https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort)
- [Optimizing compiler](https://en.wikipedia.org/wiki/Optimizing_compiler)
- [Oscillating merge sort](https://en.wikipedia.org/wiki/Oscillating_merge_sort)
- [Pairwise sorting network](https://en.wikipedia.org/wiki/Pairwise_sorting_network)
- [Pancake sorting](https://en.wikipedia.org/wiki/Pancake_sorting)
- [Patience sorting](https://en.wikipedia.org/wiki/Patience_sorting)
- [Permutation](https://en.wikipedia.org/wiki/Permutation)
- [Pigeonhole sort](https://en.wikipedia.org/wiki/Pigeonhole_sort)
- [Polyphase merge sort](https://en.wikipedia.org/wiki/Polyphase_merge_sort)
- [Blend word](https://en.wikipedia.org/wiki/Blend_word)
- [Pre-topological order](https://en.wikipedia.org/wiki/Pre-topological_order)
- [Proportion extend sort](https://en.wikipedia.org/wiki/Proportion_extend_sort)
- [Proxmap sort](https://en.wikipedia.org/wiki/Proxmap_sort)
- [Pseudocode](https://en.wikipedia.org/wiki/Pseudocode)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quantum sort](https://en.wikipedia.org/wiki/Quantum_sort)
- [Quicksort](https://en.wikipedia.org/wiki/Quicksort)
- [Radix sort](https://en.wikipedia.org/wiki/Radix_sort)
- [Randomized algorithm](https://en.wikipedia.org/wiki/Randomized_algorithm)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Samplesort](https://en.wikipedia.org/wiki/Samplesort)
- [Selection algorithm](https://en.wikipedia.org/wiki/Selection_algorithm)
- [Selection sort](https://en.wikipedia.org/wiki/Selection_sort)
- [Shellsort](https://en.wikipedia.org/wiki/Shellsort)
- [Single-event upset](https://en.wikipedia.org/wiki/Single-event_upset)
- [Slowsort](https://en.wikipedia.org/wiki/Slowsort)
- [Smoothsort](https://en.wikipedia.org/wiki/Smoothsort)
- [Sort (Unix)](https://en.wikipedia.org/wiki/Sort_(Unix))
- [Sorting](https://en.wikipedia.org/wiki/Sorting)
- [Sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)
- [Sorting network](https://en.wikipedia.org/wiki/Sorting_network)
- [Space complexity](https://en.wikipedia.org/wiki/Space_complexity)
- [Spaghetti sort](https://en.wikipedia.org/wiki/Spaghetti_sort)
- [Splaysort](https://en.wikipedia.org/wiki/Splaysort)
- [Spreadsort](https://en.wikipedia.org/wiki/Spreadsort)
- [Stooge sort](https://en.wikipedia.org/wiki/Stooge_sort)
- [Time complexity](https://en.wikipedia.org/wiki/Time_complexity)
- [Timsort](https://en.wikipedia.org/wiki/Timsort)
- [Topological sorting](https://en.wikipedia.org/wiki/Topological_sorting)
- [Total order](https://en.wikipedia.org/wiki/Total_order)
- [Tournament sort](https://en.wikipedia.org/wiki/Tournament_sort)
- [Transdichotomous model](https://en.wikipedia.org/wiki/Transdichotomous_model)
- [Tree sort](https://en.wikipedia.org/wiki/Tree_sort)
- [Unix-like](https://en.wikipedia.org/wiki/Unix-like)
- [Weak heap](https://en.wikipedia.org/wiki/Weak_heap)
- [Infinite loop](https://en.wikipedia.org/wiki/Infinite_loop)
- [WikiWikiWeb](https://en.wikipedia.org/wiki/WikiWikiWeb)
- [X + Y sorting](https://en.wikipedia.org/wiki/X_%2B_Y_sorting)
- [Wikipedia:Link rot](https://en.wikipedia.org/wiki/Wikipedia:Link_rot)
- [Template:Sorting](https://en.wikipedia.org/wiki/Template:Sorting)
- [Template talk:Sorting](https://en.wikipedia.org/wiki/Template_talk:Sorting)
- [Category:Articles with dead external links from July 2020](https://en.wikipedia.org/wiki/Category:Articles_with_dead_external_links_from_July_2020)
- [Category:Use dmy dates from December 2021](https://en.wikipedia.org/wiki/Category:Use_dmy_dates_from_December_2021)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:34:02.046673+00:00_