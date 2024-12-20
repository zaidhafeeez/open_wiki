---
title: Cycle sort
url: https://en.wikipedia.org/wiki/Cycle_sort
language: en
categories: ["Category:All articles lacking in-text citations", "Category:All articles lacking reliable references", "Category:All articles needing additional references", "Category:All articles with unsourced statements", "Category:Articles lacking in-text citations from July 2017", "Category:Articles lacking reliable references from February 2018", "Category:Articles needing additional references from July 2017", "Category:Articles with example C++ code", "Category:Articles with example Python (programming language) code", "Category:Articles with example pseudocode", "Category:Articles with multiple maintenance issues", "Category:Articles with short description", "Category:Articles with unsourced statements from September 2024", "Category:Comparison sorts", "Category:Short description is different from Wikidata"]
references: 0
last_modified: 2024-12-19T14:23:54Z
---

# Cycle sort

## Summary

Cycle sort is an in-place, unstable sorting algorithm, a comparison sort that is theoretically optimal in terms of the total number of writes to the original array, unlike any other in-place sorting algorithm. It is based on the idea that the permutation to be sorted can be factored into cycles, which can individually be rotated to give a sorted result.
Unlike nearly every other sort, items are never written elsewhere in the array simply to push them out of the way of the action. Each value is e

## Full Content

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
