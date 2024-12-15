# Comb sort

## Metadata
- **Last Updated:** 2024-12-03 06:51:57 UTC
- **Original Article:** [Comb sort](https://en.wikipedia.org/wiki/Comb_sort)
- **Language:** en
- **Page ID:** 159439

## Summary
Comb sort is a relatively simple sorting algorithm originally designed by Włodzimierz Dobosiewicz and Artur Borowy in 1980, later rediscovered (and given the name "Combsort") by Stephen Lacey and Richard Box in 1991. Comb sort improves on bubble sort in the same way that Shellsort improves on insertion sort, in that they both allow elements that start far away from their intended position to move more than one space per swap.
nist.gov's "diminishing increment sort" definition mentions the term 'comb sort' as visualizing iterative passes of the data, "where the teeth of a comb touch;" the former term is linked to Don Knuth.

## Categories
This article belongs to the following categories:

- Category:Articles with example Python (programming language) code
- Category:Articles with example pseudocode
- Category:Articles with short description
- Category:Comparison sorts
- Category:Short description is different from Wikidata

## Table of Contents

- Algorithm
- See also

## Content

Comb sort is a relatively simple sorting algorithm originally designed by Włodzimierz Dobosiewicz and Artur Borowy in 1980, later rediscovered (and given the name "Combsort") by Stephen Lacey and Richard Box in 1991. Comb sort improves on bubble sort in the same way that Shellsort improves on insertion sort, in that they both allow elements that start far away from their intended position to move more than one space per swap.
nist.gov's "diminishing increment sort" definition mentions the term 'comb sort' as visualizing iterative passes of the data, "where the teeth of a comb touch;" the former term is linked to Don Knuth.

Algorithm
The basic idea is to eliminate turtles, or small values near the end of the list, since in a bubble sort these slow the sorting down tremendously. Rabbits, large values around the beginning of the list, do not pose a problem in bubble sort.
In bubble sort, when any two elements are compared, they always have a gap (distance from each other) of 1. The basic idea of comb sort is that the gap can be much larger than 1. The inner loop of bubble sort, which does the actual swap, is modified such that the gap between swapped elements goes down (for each iteration of outer loop) in steps of a "shrink factor" k: [⁠n/k⁠, ⁠n/k2⁠, ⁠n/k3⁠, ..., 1].
The gap starts out as the length of the list n being sorted divided by the shrink factor k (generally 1.3; see below) and one pass of the aforementioned modified bubble sort is applied with that gap. Then the gap is divided by the shrink factor again, the list is sorted with this new gap, and the process repeats until the gap is 1. At this point, comb sort continues using a gap of 1 until the list is fully sorted. The final stage of the sort is thus equivalent to a bubble sort, but by this time most turtles have been dealt with, so a bubble sort will be efficient.
The shrink factor has a great effect on the efficiency of comb sort. Dobosiewicz suggested k = 4/3 = 1.333…, while Lacey and Box suggest 1.3 as an ideal shrink factor after empirical testing on over 200,000 random lists of length approximately 1000. A value too small slows the algorithm down by making unnecessarily many comparisons, whereas a value too large fails to effectively deal with turtles, making it require many passes with a gap of 1.
The pattern of repeated sorting passes with decreasing gaps is similar to Shellsort, but in Shellsort the array is sorted completely each pass before going on to the next-smallest gap.  Comb sort's passes do not completely sort the elements.  This is the reason that Shellsort gap sequences have a larger optimal shrink factor of about 2.25.
One additional refinement suggested by Lacey and Box is the "rule of 11": always use a gap size of 11, rounding up gap sizes of 9 or 10 (reached by dividing gaps of 12, 13 or 14 by 1.3) to 11.  This eliminates turtles surviving until the final gap-1 pass.

Pseudocode
function combsort(array input) is

    gap := input.size // Initialize gap size
    shrink := 1.3 // Set the gap shrink factor
    sorted := false

    loop while sorted = false
        // Update the gap value for a next comb
        gap := floor(gap / shrink)
        if gap ≤ 1 then
            gap := 1
            sorted := true // If there are no swaps this pass, we are done
        else if gap = 9 or gap = 10 then
            gap := 11      // The "rule of 11"
        end if

        // A single "comb" over the input list
        i := 0
        loop while i + gap < input.size // See Shell sort for a similar idea
            if input[i] > input[i+gap] then
                swap(input[i], input[i+gap])
                sorted := false
                // If this assignment never happens within the loop,
                // then there have been no swaps and the list is sorted.
             end if
    
             i := i + 1
         end loop
     end loop
end function

See also

Bubble sort, a generally slower algorithm, is the basis of comb sort.
Cocktail sort, or bidirectional bubble sort, is a variation of bubble sort that also addresses the problem of turtles, albeit less effectively.


== References ==

## Archive Info
- **Archived on:** 2024-12-15 21:04:00 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 4157 bytes
- **Word Count:** 712 words
