# Pancake sorting

## Article Metadata

- **Last Updated:** 2024-12-14T19:42:39.161404+00:00
- **Original Article:** [Pancake sorting](https://en.wikipedia.org/wiki/Pancake_sorting)
- **Language:** en
- **Page ID:** 478065

## Summary

Pancake sorting is the mathematical problem of sorting a disordered stack of pancakes in order of size when a spatula can be inserted at any point in the stack and used to flip all pancakes above it.  A pancake number is the minimum number of flips required for a given number of pancakes. In this form, the problem was first discussed by American geometer Jacob E. Goodman. A variant of the problem is concerned with burnt pancakes, where each pancake has a burnt side and all pancakes must, in addi

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Pancakes
- Category:Short description matches Wikidata
- Category:Sorting algorithms
- Category:Use mdy dates from October 2014

## Table of Contents

- The pancake problems
- The pancake problem on strings
- History
- Pancake graphs
- Algorithm
- Related integer sequences
- References
- Further reading
- External links

## Content

Pancake sorting is the mathematical problem of sorting a disordered stack of pancakes in order of size when a spatula can be inserted at any point in the stack and used to flip all pancakes above it.  A pancake number is the minimum number of flips required for a given number of pancakes. In this form, the problem was first discussed by American geometer Jacob E. Goodman. A variant of the problem is concerned with burnt pancakes, where each pancake has a burnt side and all pancakes must, in addition, end up with the burnt side on bottom.
All sorting methods require pairs of elements to be compared. For the traditional sorting problem, the usual problem studied is to minimize the number of comparisons required to sort a list. The number of actual operations, such as swapping two elements, is then irrelevant. For pancake sorting problems, in contrast, the aim is to minimize the number of operations, where the only allowed operations are reversals of the elements of some prefix of the sequence. Now, the number of comparisons is irrelevant.

The pancake problems
The original pancake problem
The minimum number of flips required to sort any stack of n pancakes has been shown to lie between ⁠15/14⁠n and ⁠18/11⁠n (approximately 1.07n and 1.64n), but the exact value is not known.
The simplest pancake sorting algorithm performs at most 2n − 3 flips. In this algorithm, a kind of selection sort, we bring the largest pancake not yet sorted to the top with one flip; take it down to its final position with one more flip; and repeat this process for the remaining pancakes.
In 1979, Bill Gates and Christos Papadimitriou gave a lower bound of ⁠17/16⁠n (approximately 1.06n) flips and an upper bound of ⁠(5n+5)/3⁠. The upper bound was improved, thirty years later, to  ⁠18/11⁠n by a team of researchers at the University of Texas at Dallas, led by Founders Professor Hal Sudborough.
In 2011, Laurent Bulteau, Guillaume Fertin, and Irena Rusu proved that the problem of finding the shortest sequence of flips for a given stack of pancakes is NP-hard, thereby answering a question that had been open for over three decades.

The burnt pancake problem
In a variation called the burnt pancake problem, the bottom of each pancake in the pile is burnt, and the sort must be completed with the burnt side of every pancake down. It is a signed permutation, and if a pancake i is "burnt side up" a negative element i` is put in place of i in the permutation. In 2008, a group of undergraduates built a bacterial computer that can solve a simple example of the burnt pancake problem by programming E. coli to flip segments of DNA which are analogous to burnt pancakes. DNA has an orientation (5' and 3') and an order (promoter before coding). Even though the processing power expressed by DNA flips is low, the high number of bacteria in a culture provides a large parallel computing platform. The bacteria report when they have solved the problem by becoming antibiotic resistant.

The pancake problem on strings
The discussion above presumes that each pancake is unique, that is, the sequence on which the prefix reversals are performed is a permutation. However, "strings" are sequences in which a symbol can repeat, and this repetition may reduce the number of prefix reversals required to sort. Chitturi and Sudborough (2010) and Hurkens et al. (2007) independently showed that the complexity of transforming a compatible string into another with the minimum number of prefix reversals is NP-complete. They also gave bounds for the same. Hurkens et al. gave an exact algorithm to sort binary and ternary strings. Chitturi  (2011) proved that the complexity of transforming a compatible signed string into another with the minimum number of signed prefix reversals—the burnt pancake problem on strings—is NP-complete.

History
The pancake sorting problem was first posed by Jacob E. Goodman, writing under the pseudonym "Harry Dweighter" ("harried waiter").
Although seen more often as an educational device, pancake sorting also appears in applications in parallel processor networks, in which it can provide an effective routing algorithm between processors.
The problem is notable as the topic of the only well-known mathematics paper by Microsoft founder Bill Gates (as William Gates), entitled "Bounds for Sorting by Prefix Reversal" and co-authored with Christos Papadimitriou. Published in 1979, it describes an efficient algorithm for pancake sorting. In addition, the most notable paper published by Futurama co-creator David X. Cohen (as David S. Cohen), co-authored with Manuel Blum, concerned the burnt pancake problem.
The connected problems of signed sorting by reversals and sorting by reversals were also studied more recently. Whereas efficient exact algorithms have been found for the signed sorting by reversals, the problem of sorting by reversals has been proven to be hard even to approximate to within certain constant factor, and also proven to be approximable in polynomial time to within the approximation factor 1.375.

Pancake graphs
An n-pancake graph is a graph whose vertices are the permutations of n symbols from 1 to n and its edges are given between permutations transitive by prefix reversals. It is a regular graph with n! vertices, its degree is n−1. The pancake sorting problem and the problem to obtain the diameter of the pancake graph are equivalent.
The pancake graph of dimension n, Pn can be constructed recursively from n copies of Pn−1, by assigning a different element from the set {1, 2, …, n} as a suffix to each copy.
Their girth:

  
    
      
        g
        (
        
          P
          
            n
          
        
        )
        =
        6
        
          , if 
        
        n
        >
        2
      
    
    {\displaystyle g(P_{n})=6{\text{, if }}n>2}
  
.
The γ(Pn) genus of Pn is:

  
    
      
        n
        !
        
          (
          
            
              
                n
                −
                4
              
              6
            
          
          )
        
        +
        1
        ≤
        γ
        (
        
          P
          
            n
          
        
        )
        ≤
        n
        !
        
          (
          
            
              
                n
                −
                3
              
              4
            
          
          )
        
        −
        
          
            n
            2
          
        
        +
        1
      
    
    {\displaystyle n!\left({\frac {n-4}{6}}\right)+1\leq \gamma (P_{n})\leq n!\left({\frac {n-3}{4}}\right)-{\frac {n}{2}}+1}
  

Since pancake graphs have many interesting properties such as symmetric and recursive structures, small degrees and diameters compared against the size of the graph, much attention is paid to them as a model of interconnection networks for parallel computers. When we regard the pancake graphs as the model of the interconnection networks, the diameter of the graph is a measure that represents the delay of communication.
The pancake graphs are Cayley graphs (thus are vertex-transitive) and are especially attractive for parallel processing. They have sublogarithmic degree and diameter, and are relatively sparse (compared to e.g. hypercubes).

Algorithm
An example of the pancake sorting algorithm is given below in Python. The code is similar to bubble sort or selection sort.

Related integer sequences
Sequences from The Online Encyclopedia of Integer Sequences:

OEIS: A058986 – maximum number of flips
OEIS: A067607 – number of stacks requiring the maximum number of flips (above)
OEIS: A078941 – maximum number of flips for a "burnt" stack
OEIS: A078942 – the number of flips for a sorted "burnt-side-on-top" stack
OEIS: A092113 – the above triangle, read by rows

References
Further reading
External links
Cut-the-Knot: Flipping pancakes puzzle, including a Java applet for the pancake problem and some discussion.
Douglas B. West's "The Pancake Problems"
Weisstein, Eric W. "Pancake Sorting". MathWorld.

## Related Articles

### Internal Links

- [Adaptive sort](https://en.wikipedia.org/wiki/Adaptive_sort)
- [American flag sort](https://en.wikipedia.org/wiki/American_flag_sort)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Batcher odd–even mergesort](https://en.wikipedia.org/wiki/Batcher_odd%E2%80%93even_mergesort)
- [Bead sort](https://en.wikipedia.org/wiki/Bead_sort)
- [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Bill Gates](https://en.wikipedia.org/wiki/Bill_Gates)
- [Bitonic sorter](https://en.wikipedia.org/wiki/Bitonic_sorter)
- [Block sort](https://en.wikipedia.org/wiki/Block_sort)
- [Bogosort](https://en.wikipedia.org/wiki/Bogosort)
- [Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort)
- [Bucket sort](https://en.wikipedia.org/wiki/Bucket_sort)
- [Burstsort](https://en.wikipedia.org/wiki/Burstsort)
- [Cartesian tree](https://en.wikipedia.org/wiki/Cartesian_tree)
- [Cascade merge sort](https://en.wikipedia.org/wiki/Cascade_merge_sort)
- [Cayley graph](https://en.wikipedia.org/wiki/Cayley_graph)
- [Christos Papadimitriou](https://en.wikipedia.org/wiki/Christos_Papadimitriou)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Cocktail shaker sort](https://en.wikipedia.org/wiki/Cocktail_shaker_sort)
- [Colva Roney-Dougal](https://en.wikipedia.org/wiki/Colva_Roney-Dougal)
- [Comb sort](https://en.wikipedia.org/wiki/Comb_sort)
- [Comparison sort](https://en.wikipedia.org/wiki/Comparison_sort)
- [Computational complexity theory](https://en.wikipedia.org/wiki/Computational_complexity_theory)
- [Counting sort](https://en.wikipedia.org/wiki/Counting_sort)
- [Cycle sort](https://en.wikipedia.org/wiki/Cycle_sort)
- [DNA computing](https://en.wikipedia.org/wiki/DNA_computing)
- [David X. Cohen](https://en.wikipedia.org/wiki/David_X._Cohen)
- [Dense graph](https://en.wikipedia.org/wiki/Dense_graph)
- [Discrete Mathematics (journal)](https://en.wikipedia.org/wiki/Discrete_Mathematics_(journal))
- [Distance (graph theory)](https://en.wikipedia.org/wiki/Distance_(graph_theory))
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Eric W. Weisstein](https://en.wikipedia.org/wiki/Eric_W._Weisstein)
- [Escherichia coli](https://en.wikipedia.org/wiki/Escherichia_coli)
- [Flashsort](https://en.wikipedia.org/wiki/Flashsort)
- [Futurama](https://en.wikipedia.org/wiki/Futurama)
- [Girth (graph theory)](https://en.wikipedia.org/wiki/Girth_(graph_theory))
- [Gnome sort](https://en.wikipedia.org/wiki/Gnome_sort)
- [Graph embedding](https://en.wikipedia.org/wiki/Graph_embedding)
- [Heapsort](https://en.wikipedia.org/wiki/Heapsort)
- [Hybrid algorithm](https://en.wikipedia.org/wiki/Hybrid_algorithm)
- [Hypercube graph](https://en.wikipedia.org/wiki/Hypercube_graph)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [In-place algorithm](https://en.wikipedia.org/wiki/In-place_algorithm)
- [Insertion sort](https://en.wikipedia.org/wiki/Insertion_sort)
- [Integer sorting](https://en.wikipedia.org/wiki/Integer_sorting)
- [Interpolation sort](https://en.wikipedia.org/wiki/Interpolation_sort)
- [Introsort](https://en.wikipedia.org/wiki/Introsort)
- [JSTOR](https://en.wikipedia.org/wiki/JSTOR)
- [Jacob E. Goodman](https://en.wikipedia.org/wiki/Jacob_E._Goodman)
- [Kirkpatrick–Reisch sort](https://en.wikipedia.org/wiki/Kirkpatrick%E2%80%93Reisch_sort)
- [Laurie Heyer](https://en.wikipedia.org/wiki/Laurie_Heyer)
- [Library sort](https://en.wikipedia.org/wiki/Library_sort)
- [List (abstract data type)](https://en.wikipedia.org/wiki/List_(abstract_data_type))
- [Mathematical Reviews](https://en.wikipedia.org/wiki/Mathematical_Reviews)
- [Manuel Blum](https://en.wikipedia.org/wiki/Manuel_Blum)
- [Marek Karpinski](https://en.wikipedia.org/wiki/Marek_Karpinski)
- [MathWorld](https://en.wikipedia.org/wiki/MathWorld)
- [Merge-insertion sort](https://en.wikipedia.org/wiki/Merge-insertion_sort)
- [Merge sort](https://en.wikipedia.org/wiki/Merge_sort)
- [Microsoft](https://en.wikipedia.org/wiki/Microsoft)
- [NP-completeness](https://en.wikipedia.org/wiki/NP-completeness)
- [NP-hardness](https://en.wikipedia.org/wiki/NP-hardness)
- [Odd–even sort](https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort)
- [On-Line Encyclopedia of Integer Sequences](https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences)
- [Oscillating merge sort](https://en.wikipedia.org/wiki/Oscillating_merge_sort)
- [PubMed Central](https://en.wikipedia.org/wiki/PubMed_Central)
- [PubMed](https://en.wikipedia.org/wiki/PubMed)
- [Pairwise sorting network](https://en.wikipedia.org/wiki/Pairwise_sorting_network)
- [Pancake graph](https://en.wikipedia.org/wiki/Pancake_graph)
- [Parallel computing](https://en.wikipedia.org/wiki/Parallel_computing)
- [Patience sorting](https://en.wikipedia.org/wiki/Patience_sorting)
- [Permutation](https://en.wikipedia.org/wiki/Permutation)
- [Pigeonhole sort](https://en.wikipedia.org/wiki/Pigeonhole_sort)
- [Polyphase merge sort](https://en.wikipedia.org/wiki/Polyphase_merge_sort)
- [Pre-topological order](https://en.wikipedia.org/wiki/Pre-topological_order)
- [Substring](https://en.wikipedia.org/wiki/Substring)
- [Proportion extend sort](https://en.wikipedia.org/wiki/Proportion_extend_sort)
- [Proxmap sort](https://en.wikipedia.org/wiki/Proxmap_sort)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quantum sort](https://en.wikipedia.org/wiki/Quantum_sort)
- [Quicksort](https://en.wikipedia.org/wiki/Quicksort)
- [Radix sort](https://en.wikipedia.org/wiki/Radix_sort)
- [Regular graph](https://en.wikipedia.org/wiki/Regular_graph)
- [Robert Tarjan](https://en.wikipedia.org/wiki/Robert_Tarjan)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Samplesort](https://en.wikipedia.org/wiki/Samplesort)
- [Selection algorithm](https://en.wikipedia.org/wiki/Selection_algorithm)
- [Selection sort](https://en.wikipedia.org/wiki/Selection_sort)
- [Shellsort](https://en.wikipedia.org/wiki/Shellsort)
- [Simon Singh](https://en.wikipedia.org/wiki/Simon_Singh)
- [Slowsort](https://en.wikipedia.org/wiki/Slowsort)
- [Smoothsort](https://en.wikipedia.org/wiki/Smoothsort)
- [Sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)
- [Sorting network](https://en.wikipedia.org/wiki/Sorting_network)
- [Sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)
- [Spaghetti sort](https://en.wikipedia.org/wiki/Spaghetti_sort)
- [Spatula](https://en.wikipedia.org/wiki/Spatula)
- [Splaysort](https://en.wikipedia.org/wiki/Splaysort)
- [Spreadsort](https://en.wikipedia.org/wiki/Spreadsort)
- [Stooge sort](https://en.wikipedia.org/wiki/Stooge_sort)
- [The Guardian](https://en.wikipedia.org/wiki/The_Guardian)
- [Timsort](https://en.wikipedia.org/wiki/Timsort)
- [Topological sorting](https://en.wikipedia.org/wiki/Topological_sorting)
- [Total order](https://en.wikipedia.org/wiki/Total_order)
- [Tournament sort](https://en.wikipedia.org/wiki/Tournament_sort)
- [Transdichotomous model](https://en.wikipedia.org/wiki/Transdichotomous_model)
- [Tree sort](https://en.wikipedia.org/wiki/Tree_sort)
- [University of Texas at Dallas](https://en.wikipedia.org/wiki/University_of_Texas_at_Dallas)
- [Vertex-transitive graph](https://en.wikipedia.org/wiki/Vertex-transitive_graph)
- [Weak heap](https://en.wikipedia.org/wiki/Weak_heap)
- [X + Y sorting](https://en.wikipedia.org/wiki/X_%2B_Y_sorting)
- [Template:Sorting](https://en.wikipedia.org/wiki/Template:Sorting)
- [Template talk:Sorting](https://en.wikipedia.org/wiki/Template_talk:Sorting)
- [Category:Use mdy dates from October 2014](https://en.wikipedia.org/wiki/Category:Use_mdy_dates_from_October_2014)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:42:39.161404+00:00_