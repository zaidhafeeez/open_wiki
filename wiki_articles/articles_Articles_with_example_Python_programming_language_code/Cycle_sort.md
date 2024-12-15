# Cycle sort

## Article Metadata

- **Last Updated:** 2024-12-15T04:15:08.793554+00:00
- **Original Article:** [Cycle sort](https://en.wikipedia.org/wiki/Cycle_sort)
- **Language:** en
- **Page ID:** 29050607

## Summary

Cycle sort is an in-place, unstable sorting algorithm, a comparison sort that is theoretically optimal in terms of the total number of writes to the original array, unlike any other in-place sorting algorithm. It is based on the idea that the permutation to be sorted can be factored into cycles, which can individually be rotated to give a sorted result.
Unlike nearly every other sort, items are never written elsewhere in the array simply to push them out of the way of the action. Each value is e

## Categories

- Category:All articles lacking in-text citations
- Category:All articles lacking reliable references
- Category:All articles needing additional references
- Category:All articles with unsourced statements
- Category:Articles lacking in-text citations from July 2017
- Category:Articles lacking reliable references from February 2018
- Category:Articles needing additional references from July 2017
- Category:Articles with example C++ code
- Category:Articles with example Python (programming language) code
- Category:Articles with example pseudocode
- Category:Articles with multiple maintenance issues
- Category:Articles with short description
- Category:Articles with unsourced statements from September 2024
- Category:Comparison sorts
- Category:Short description is different from Wikidata

## Table of Contents

- Algorithm
- Situation-specific optimizations
- References
- External links

## Content

Cycle sort is an in-place, unstable sorting algorithm, a comparison sort that is theoretically optimal in terms of the total number of writes to the original array, unlike any other in-place sorting algorithm. It is based on the idea that the permutation to be sorted can be factored into cycles, which can individually be rotated to give a sorted result.
Unlike nearly every other sort, items are never written elsewhere in the array simply to push them out of the way of the action. Each value is either written zero times, if it's already in its correct position, or written one time to its correct position. This matches the minimal number of overwrites required for a completed in-place sort.
Minimizing the number of writes is useful when making writes to some huge data set is very expensive, such as with EEPROMs like Flash memory where each write reduces the lifespan of the memory.

Algorithm
To illustrate the idea of cycle sort, consider a list with distinct elements. Given an element 
  
    
      
        x
      
    
    {\displaystyle x}
  
, we can find the index at which it will occur in the sorted list by simply counting the number of elements in the entire list that are smaller than 
  
    
      
        x
      
    
    {\displaystyle x}
  
. Now

If the element is already at the correct position, do nothing.
If it is not, we will write it to its intended position. That position is inhabited by a different element 
  
    
      
        y
      
    
    {\displaystyle y}
  
, which we then have to move to its correct position. This process of displacing elements to their correct positions continues until an element is moved to the original position of 
  
    
      
        x
      
    
    {\displaystyle x}
  
. This completes a cycle.

Repeating this process for every element sorts the list, with a single writing operation if and only if an element is not already at its correct position. While computing the correct positions takes 
  
    
      
        O
        (
        n
        )
      
    
    {\displaystyle O(n)}
  
 time for every single element, thus resulting in a quadratic time algorithm, the number of writing operations is minimized.

Implementation
To create a working implementation from the above outline, two issues need to be addressed:

When computing the correct positions, we have to make sure not to double-count the first element of the cycle.
If there are duplicate elements present, when we try to move an element 
  
    
      
        x
      
    
    {\displaystyle x}
  
 to its correct position, that position might already be inhabited by an 
  
    
      
        x
      
    
    {\displaystyle x}
  
. Simply swapping these would cause the algorithm to cycle indefinitely. Instead, we have to insert the element after any of its duplicates.
The following Python implementation performs cycle sort on an array, counting the number of writes to that array that were needed to sort it.
Python

The next implementation written in C++ simply performs cyclic array sorting.

Situation-specific optimizations
When the array contains only duplicates of a relatively small number of items, a constant-time perfect hash function can greatly speed up finding where to put an item1, turning the sort from Θ(n2) time to Θ(n + k) time, where k is the total number of hashes. The array ends up sorted in the order of the hashes, so choosing a hash function that gives you the right ordering is important.
Before the sort, create a histogram, sorted by hash, counting the number of occurrences of each hash in the array. Then create a table with the cumulative sum of each entry in the histogram. The cumulative sum table will then contain the position in the array of each element. The proper place of elements can then be found by a constant-time hashing and cumulative sum table lookup rather than a linear search.

References
External links
^  "Cycle-Sort: A Linear Sorting Method", The Computer Journal (1990) 33 (4): 365-367.

Original source of unrestricted variant
Cyclesort - a curious little sorting algorithm

## Related Articles

### Internal Links

- [Adaptive sort](https://en.wikipedia.org/wiki/Adaptive_sort)
- [American flag sort](https://en.wikipedia.org/wiki/American_flag_sort)
- [Array (data structure)](https://en.wikipedia.org/wiki/Array_(data_structure))
- [Batcher odd–even mergesort](https://en.wikipedia.org/wiki/Batcher_odd%E2%80%93even_mergesort)
- [Bead sort](https://en.wikipedia.org/wiki/Bead_sort)
- [Best, worst and average case](https://en.wikipedia.org/wiki/Best,_worst_and_average_case)
- [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Bitonic sorter](https://en.wikipedia.org/wiki/Bitonic_sorter)
- [Block sort](https://en.wikipedia.org/wiki/Block_sort)
- [Bogosort](https://en.wikipedia.org/wiki/Bogosort)
- [Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort)
- [Bucket sort](https://en.wikipedia.org/wiki/Bucket_sort)
- [Burstsort](https://en.wikipedia.org/wiki/Burstsort)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [Cartesian tree](https://en.wikipedia.org/wiki/Cartesian_tree)
- [Cascade merge sort](https://en.wikipedia.org/wiki/Cascade_merge_sort)
- [Cocktail shaker sort](https://en.wikipedia.org/wiki/Cocktail_shaker_sort)
- [Comb sort](https://en.wikipedia.org/wiki/Comb_sort)
- [Comparison sort](https://en.wikipedia.org/wiki/Comparison_sort)
- [Computational complexity theory](https://en.wikipedia.org/wiki/Computational_complexity_theory)
- [Counting sort](https://en.wikipedia.org/wiki/Counting_sort)
- [Cyclic permutation](https://en.wikipedia.org/wiki/Cyclic_permutation)
- [EEPROM](https://en.wikipedia.org/wiki/EEPROM)
- [Flash memory](https://en.wikipedia.org/wiki/Flash_memory)
- [Flashsort](https://en.wikipedia.org/wiki/Flashsort)
- [Gnome sort](https://en.wikipedia.org/wiki/Gnome_sort)
- [Heapsort](https://en.wikipedia.org/wiki/Heapsort)
- [Histogram](https://en.wikipedia.org/wiki/Histogram)
- [Hybrid algorithm](https://en.wikipedia.org/wiki/Hybrid_algorithm)
- [In-place algorithm](https://en.wikipedia.org/wiki/In-place_algorithm)
- [Insertion sort](https://en.wikipedia.org/wiki/Insertion_sort)
- [Integer sorting](https://en.wikipedia.org/wiki/Integer_sorting)
- [Interpolation sort](https://en.wikipedia.org/wiki/Interpolation_sort)
- [Introsort](https://en.wikipedia.org/wiki/Introsort)
- [Kirkpatrick–Reisch sort](https://en.wikipedia.org/wiki/Kirkpatrick%E2%80%93Reisch_sort)
- [Library sort](https://en.wikipedia.org/wiki/Library_sort)
- [Linear search](https://en.wikipedia.org/wiki/Linear_search)
- [List (abstract data type)](https://en.wikipedia.org/wiki/List_(abstract_data_type))
- [Merge-insertion sort](https://en.wikipedia.org/wiki/Merge-insertion_sort)
- [Merge sort](https://en.wikipedia.org/wiki/Merge_sort)
- [Odd–even sort](https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort)
- [Oscillating merge sort](https://en.wikipedia.org/wiki/Oscillating_merge_sort)
- [Pairwise sorting network](https://en.wikipedia.org/wiki/Pairwise_sorting_network)
- [Pancake sorting](https://en.wikipedia.org/wiki/Pancake_sorting)
- [Patience sorting](https://en.wikipedia.org/wiki/Patience_sorting)
- [Perfect hash function](https://en.wikipedia.org/wiki/Perfect_hash_function)
- [Permutation](https://en.wikipedia.org/wiki/Permutation)
- [Pigeonhole sort](https://en.wikipedia.org/wiki/Pigeonhole_sort)
- [Polyphase merge sort](https://en.wikipedia.org/wiki/Polyphase_merge_sort)
- [Pre-topological order](https://en.wikipedia.org/wiki/Pre-topological_order)
- [Proportion extend sort](https://en.wikipedia.org/wiki/Proportion_extend_sort)
- [Proxmap sort](https://en.wikipedia.org/wiki/Proxmap_sort)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quantum sort](https://en.wikipedia.org/wiki/Quantum_sort)
- [Quicksort](https://en.wikipedia.org/wiki/Quicksort)
- [Radix sort](https://en.wikipedia.org/wiki/Radix_sort)
- [Samplesort](https://en.wikipedia.org/wiki/Samplesort)
- [Selection algorithm](https://en.wikipedia.org/wiki/Selection_algorithm)
- [Selection sort](https://en.wikipedia.org/wiki/Selection_sort)
- [Shellsort](https://en.wikipedia.org/wiki/Shellsort)
- [Slowsort](https://en.wikipedia.org/wiki/Slowsort)
- [Smoothsort](https://en.wikipedia.org/wiki/Smoothsort)
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
- [Weak heap](https://en.wikipedia.org/wiki/Weak_heap)
- [X + Y sorting](https://en.wikipedia.org/wiki/X_%2B_Y_sorting)
- [Talk:Cycle sort](https://en.wikipedia.org/wiki/Talk:Cycle_sort)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Wikipedia:When to cite](https://en.wikipedia.org/wiki/Wikipedia:When_to_cite)
- [Wikipedia:WikiProject Reliability](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Reliability)
- [Template:Sorting](https://en.wikipedia.org/wiki/Template:Sorting)
- [Template talk:Sorting](https://en.wikipedia.org/wiki/Template_talk:Sorting)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles lacking in-text citations from July 2017](https://en.wikipedia.org/wiki/Category:Articles_lacking_in-text_citations_from_July_2017)
- [Category:Articles lacking reliable references from February 2018](https://en.wikipedia.org/wiki/Category:Articles_lacking_reliable_references_from_February_2018)
- [Category:Articles needing additional references from July 2017](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_July_2017)
- [Category:Articles with unsourced statements from September 2024](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_September_2024)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:15:08.793554+00:00_