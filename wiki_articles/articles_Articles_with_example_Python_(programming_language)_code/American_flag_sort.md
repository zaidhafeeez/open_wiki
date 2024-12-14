# American flag sort

## Article Metadata

- **Last Updated:** 2024-12-14T17:14:55.382891+00:00
- **Original Article:** [American flag sort](https://en.wikipedia.org/wiki/American_flag_sort)
- **Language:** en
- **Page ID:** 9080565

## Summary

An American flag sort is an efficient, in-place variant of radix sort that distributes items into buckets.  Non-comparative sorting algorithms such as radix sort and American flag sort are typically used to sort large objects such as strings, for which comparison is not a unit-time operation.
American flag sort iterates through the bits of the objects, considering several bits of each object at a time.  For each set of bits, American flag sort makes two passes through the array of objects: first

## Categories

- Category:Accuracy disputes from November 2023
- Category:All Wikipedia articles needing clarification
- Category:All accuracy disputes
- Category:All articles needing additional references
- Category:All articles with unsourced statements
- Category:Articles needing additional references from July 2017
- Category:Articles with example Python (programming language) code
- Category:Articles with example pseudocode
- Category:Articles with short description
- Category:Articles with unsourced statements from October 2020
- Category:Short description matches Wikidata
- Category:String sorting algorithms
- Category:Wikipedia articles needing clarification from October 2020

## Table of Contents

- Algorithm
- See also
- References

## Content

An American flag sort is an efficient, in-place variant of radix sort that distributes items into buckets.  Non-comparative sorting algorithms such as radix sort and American flag sort are typically used to sort large objects such as strings, for which comparison is not a unit-time operation.
American flag sort iterates through the bits of the objects, considering several bits of each object at a time.  For each set of bits, American flag sort makes two passes through the array of objects: first to count the number of objects that will fall in each bin, and second to place each object in its bucket.  This works especially well when sorting a byte at a time, using 256 buckets. With some optimizations, it is twice as fast as quicksort for large sets of strings.
The name American flag sort comes by analogy with the Dutch national flag problem in the last step: efficiently partition the array into many "stripes".

Algorithm
Sorting algorithms in general sort a list of objects according to some ordering scheme. In contrast to comparison-based sorting algorithms, such as quicksort, American flag sort  is based on directly comparing the bytes (numerical representation) of the underlying objects. In-place sorting algorithms, including American flag sort, run without allocating a significant amount of memory beyond that used by the original array. This is a significant advantage, both in memory savings and in time saved copying the array.
American flag sort works by successively dividing a list of objects into buckets based on the first digit of their base-N representation (the base used is referred to as the radix). When N is 3, each object can be swapped into the correct bucket by using the Dutch national flag algorithm. When N is larger, however, objects cannot be immediately swapped into place, because it is unknown where each bucket should begin and end. American flag sort gets around this problem by making two passes through the array. The first pass counts the number of objects that belong in each of the N buckets. The beginning of each bucket is then computed as the sum of sizes of the preceding buckets. The second pass puts each object into the correct bucket.
American flag sort is most efficient with a radix that is a power of 2, because bit-shifting operations can be used instead of expensive exponentiations to compute the value of each digit. When sorting strings using 8- or 7-bit encodings such as ASCII, it is typical to use a radix of 256 or 128, which amounts to sorting character-by-character.

Performance considerations
For pure English alphabet text, the counts histogram is always sparse. Depending on the hardware, it may be worth clearing the counts in correspondence with completing a bucket (as in the original paper); or it may be worth maintaining a max and min active bucket, or a more complex data structure suitable for sparse arrays. It is also important to use a more basic sorting method for very small data sets, except in pathological cases where keys may share very long prefixes.
Most critically, this algorithm follows a random permutation, and is thus particularly cache-unfriendly for large datasets. It is a suitable algorithm in conjunction with a k-way merge algorithm. (The original paper was written before cached memory was in common use.)

Pseudocode
american_flag_sort(Array, Radix)
    for each digit D:
        # first pass: compute counts
        Counts <- zeros(Radix)
        for object X in Array:
            Counts[digit D of object X in base Radix] += 1
        # compute bucket offsets
        Offsets <- [ sum(Counts[0..i]) for i in 1..Radix]
        # swap objects into place
        for object X in Array:
            swap X to the bucket starting at Offsets[digit D of X in base Radix]
        for each Bucket:
            american_flag_sort(Bucket, Radix)

Sample implementation in Python
This example written in the Python programming language will perform American flag sort for any radix of 2 or greater. Simplicity of exposition is chosen over clever programming, and so the log function is used instead of bit shifting techniques.

See also
Bucket sort
Multi-key quicksort
Radix sort
Dutch national flag problem

References
General
 This article incorporates public domain material from Paul E. Black. "American flag sort". Dictionary of Algorithms and Data Structures. NIST.

## Related Articles

### Internal Links

- [ASCII](https://en.wikipedia.org/wiki/ASCII)
- [Adaptive sort](https://en.wikipedia.org/wiki/Adaptive_sort)
- [Analogy](https://en.wikipedia.org/wiki/Analogy)
- [Batcher odd–even mergesort](https://en.wikipedia.org/wiki/Batcher_odd%E2%80%93even_mergesort)
- [Bead sort](https://en.wikipedia.org/wiki/Bead_sort)
- [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Bitonic sorter](https://en.wikipedia.org/wiki/Bitonic_sorter)
- [Block sort](https://en.wikipedia.org/wiki/Block_sort)
- [Bogosort](https://en.wikipedia.org/wiki/Bogosort)
- [Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort)
- [Bucket sort](https://en.wikipedia.org/wiki/Bucket_sort)
- [Burstsort](https://en.wikipedia.org/wiki/Burstsort)
- [Cartesian tree](https://en.wikipedia.org/wiki/Cartesian_tree)
- [Cascade merge sort](https://en.wikipedia.org/wiki/Cascade_merge_sort)
- [Cocktail shaker sort](https://en.wikipedia.org/wiki/Cocktail_shaker_sort)
- [Comb sort](https://en.wikipedia.org/wiki/Comb_sort)
- [Comparison sort](https://en.wikipedia.org/wiki/Comparison_sort)
- [Computational complexity theory](https://en.wikipedia.org/wiki/Computational_complexity_theory)
- [Copyright status of works by the federal government of the United States](https://en.wikipedia.org/wiki/Copyright_status_of_works_by_the_federal_government_of_the_United_States)
- [Counting sort](https://en.wikipedia.org/wiki/Counting_sort)
- [Cycle sort](https://en.wikipedia.org/wiki/Cycle_sort)
- [List of terms relating to algorithms and data structures](https://en.wikipedia.org/wiki/List_of_terms_relating_to_algorithms_and_data_structures)
- [Dutch national flag problem](https://en.wikipedia.org/wiki/Dutch_national_flag_problem)
- [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)
- [Flag of the United States](https://en.wikipedia.org/wiki/Flag_of_the_United_States)
- [Flashsort](https://en.wikipedia.org/wiki/Flashsort)
- [Gnome sort](https://en.wikipedia.org/wiki/Gnome_sort)
- [Heapsort](https://en.wikipedia.org/wiki/Heapsort)
- [Hybrid algorithm](https://en.wikipedia.org/wiki/Hybrid_algorithm)
- [In-place algorithm](https://en.wikipedia.org/wiki/In-place_algorithm)
- [In-place algorithm](https://en.wikipedia.org/wiki/In-place_algorithm)
- [Insertion sort](https://en.wikipedia.org/wiki/Insertion_sort)
- [Integer sorting](https://en.wikipedia.org/wiki/Integer_sorting)
- [Interpolation sort](https://en.wikipedia.org/wiki/Interpolation_sort)
- [Introsort](https://en.wikipedia.org/wiki/Introsort)
- [K-way merge algorithm](https://en.wikipedia.org/wiki/K-way_merge_algorithm)
- [Kirkpatrick–Reisch sort](https://en.wikipedia.org/wiki/Kirkpatrick%E2%80%93Reisch_sort)
- [Library sort](https://en.wikipedia.org/wiki/Library_sort)
- [List (abstract data type)](https://en.wikipedia.org/wiki/List_(abstract_data_type))
- [Merge-insertion sort](https://en.wikipedia.org/wiki/Merge-insertion_sort)
- [Merge sort](https://en.wikipedia.org/wiki/Merge_sort)
- [Multi-key quicksort](https://en.wikipedia.org/wiki/Multi-key_quicksort)
- [National Institute of Standards and Technology](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)
- [Odd–even sort](https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort)
- [Oscillating merge sort](https://en.wikipedia.org/wiki/Oscillating_merge_sort)
- [Pairwise sorting network](https://en.wikipedia.org/wiki/Pairwise_sorting_network)
- [Pancake sorting](https://en.wikipedia.org/wiki/Pancake_sorting)
- [Partition of a set](https://en.wikipedia.org/wiki/Partition_of_a_set)
- [Patience sorting](https://en.wikipedia.org/wiki/Patience_sorting)
- [Pigeonhole sort](https://en.wikipedia.org/wiki/Pigeonhole_sort)
- [Polyphase merge sort](https://en.wikipedia.org/wiki/Polyphase_merge_sort)
- [Pre-topological order](https://en.wikipedia.org/wiki/Pre-topological_order)
- [Proportion extend sort](https://en.wikipedia.org/wiki/Proportion_extend_sort)
- [Proxmap sort](https://en.wikipedia.org/wiki/Proxmap_sort)
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
- [Spaghetti sort](https://en.wikipedia.org/wiki/Spaghetti_sort)
- [Splaysort](https://en.wikipedia.org/wiki/Splaysort)
- [Spreadsort](https://en.wikipedia.org/wiki/Spreadsort)
- [Stooge sort](https://en.wikipedia.org/wiki/Stooge_sort)
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [Timsort](https://en.wikipedia.org/wiki/Timsort)
- [Topological sorting](https://en.wikipedia.org/wiki/Topological_sorting)
- [Total order](https://en.wikipedia.org/wiki/Total_order)
- [Tournament sort](https://en.wikipedia.org/wiki/Tournament_sort)
- [Transdichotomous model](https://en.wikipedia.org/wiki/Transdichotomous_model)
- [Tree sort](https://en.wikipedia.org/wiki/Tree_sort)
- [Weak heap](https://en.wikipedia.org/wiki/Weak_heap)
- [X + Y sorting](https://en.wikipedia.org/wiki/X_%2B_Y_sorting)
- [Talk:American flag sort](https://en.wikipedia.org/wiki/Talk:American_flag_sort)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Please clarify](https://en.wikipedia.org/wiki/Wikipedia:Please_clarify)
- [Wikipedia:Reliable sources](https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources)
- [Wikipedia:Vagueness](https://en.wikipedia.org/wiki/Wikipedia:Vagueness)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Sorting](https://en.wikipedia.org/wiki/Template:Sorting)
- [Template talk:Sorting](https://en.wikipedia.org/wiki/Template_talk:Sorting)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Accuracy disputes from November 2023](https://en.wikipedia.org/wiki/Category:Accuracy_disputes_from_November_2023)
- [Category:Articles needing additional references from July 2017](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_July_2017)
- [Category:Articles with unsourced statements from October 2020](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_October_2020)
- [Category:Wikipedia articles needing clarification from October 2020](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_needing_clarification_from_October_2020)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T17:14:55.382891+00:00_