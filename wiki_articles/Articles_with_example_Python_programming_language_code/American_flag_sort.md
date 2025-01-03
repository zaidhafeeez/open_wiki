---
title: American flag sort
url: https://en.wikipedia.org/wiki/American_flag_sort
language: en
categories: ["Category:Accuracy disputes from November 2023", "Category:All Wikipedia articles needing clarification", "Category:All accuracy disputes", "Category:All articles needing additional references", "Category:All articles with unsourced statements", "Category:Articles needing additional references from July 2017", "Category:Articles with example Python (programming language) code", "Category:Articles with example pseudocode", "Category:Articles with short description", "Category:Articles with unsourced statements from October 2020", "Category:Short description matches Wikidata", "Category:String sorting algorithms", "Category:Wikipedia articles needing clarification from October 2020"]
references: 0
last_modified: 2024-12-20T21:32:06Z
---

# American flag sort

## Summary

An American flag sort is an efficient, in-place variant of radix sort that distributes items into buckets.  Non-comparative sorting algorithms such as radix sort and American flag sort are typically used to sort large objects such as strings, for which comparison is not a unit-time operation.
American flag sort iterates through the bits of the objects, considering several bits of each object at a time.  For each set of bits, American flag sort makes two passes through the array of objects: first

## Full Content

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
