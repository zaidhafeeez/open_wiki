# Cycle sort

## Article Metadata

- **Last Updated:** 2024-12-15T15:04:48.893141+00:00
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

## Related Articles

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

*Note: Showing 50 out of 92 related articles*
