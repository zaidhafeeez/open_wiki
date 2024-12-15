# Hamming distance

## Article Metadata

- **Last Updated:** 2024-12-15T04:26:51.856015+00:00
- **Original Article:** [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance)
- **Language:** en
- **Page ID:** 41227

## Summary

In information theory, the Hamming distance between two strings or vectors of equal length is the number of positions at which the corresponding symbols are different. In other words, it measures the minimum number of substitutions required to change one string into the other, or equivalently, the minimum number of errors that could have transformed one string into the other. In a more general context, the Hamming distance is one of several string metrics for measuring the edit distance between 

## Categories

- Category:All Wikipedia articles written in American English
- Category:All articles lacking in-text citations
- Category:Articles lacking in-text citations from May 2015
- Category:Articles with example C++ code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Coding theory
- Category:Cubes
- Category:Metric geometry
- Category:Short description matches Wikidata
- Category:String metrics
- Category:Use American English from March 2019
- Category:Wikipedia articles incorporating text from the Federal Standard 1037C
- Category:Wikipedia articles needing clarification from June 2020

## Table of Contents

- Definition
- Examples
- Properties
- Error detection and error correction
- History and applications
- Algorithm example
- See also
- References
- Further reading

## Content

In information theory, the Hamming distance between two strings or vectors of equal length is the number of positions at which the corresponding symbols are different. In other words, it measures the minimum number of substitutions required to change one string into the other, or equivalently, the minimum number of errors that could have transformed one string into the other. In a more general context, the Hamming distance is one of several string metrics for measuring the edit distance between two sequences. It is named after the American mathematician Richard Hamming.
A major application is in coding theory, more specifically to block codes, in which the equal-length strings are vectors over a finite field.

Definition
The Hamming distance between two equal-length strings of symbols is the number of positions at which the corresponding symbols are different.

Examples
The symbols may be letters, bits, or decimal digits, among other possibilities.  For example, the Hamming distance between:

"karolin"  and  "kathrin"  is 3.
"karolin"  and  "kerstin"  is 3.
"kathrin"  and  "kerstin"  is 4.
0000  and  1111 is 4.
2173896  and  2233796  is 3.

Properties
For a fixed length n, the Hamming distance is a metric on the set of the words of length n (also known as a Hamming space), as it fulfills the conditions of non-negativity, symmetry, the Hamming distance of two words is 0 if and only if the two words are identical, and it satisfies the triangle inequality as well: Indeed, if we fix three words a, b and c, then whenever there is a difference between the ith letter of a and the ith letter of c, then there must be a difference between the ith letter of a and ith letter of b, or between the ith letter of b and the ith letter of c. Hence the Hamming distance between a and c is not larger than the sum of the Hamming distances between a and b and between b and c. The Hamming distance between two words a and b can also be seen as the Hamming weight of a − b for an appropriate choice of the − operator, much as the difference between two integers can be seen as a distance from zero on the number line.
For binary strings a and b the Hamming distance is equal to the number of ones (population count) in a XOR b. The metric space of length-n binary strings, with the Hamming distance, is known as the Hamming cube; it is equivalent as a metric space to the set of distances between vertices in a hypercube graph. One can also view a binary string of length n as a vector in 
  
    
      
        
          
            R
          
          
            n
          
        
      
    
    {\displaystyle \mathbb {R} ^{n}}
  
 by treating each symbol in the string as a real coordinate; with this embedding, the strings form the vertices of an n-dimensional hypercube, and the Hamming distance of the strings is equivalent to the Manhattan distance between the vertices.

Error detection and error correction
The minimum Hamming distance or minimum distance (usually denoted by dmin) is used to define some essential notions in coding theory, such as error detecting and error correcting codes. In particular, a code C is said to be k error detecting if, and only if, the minimum Hamming distance between any two of its codewords is at least k+1.
For example, consider a code consisting of two codewords "000" and "111". The Hamming distance between these two words is 3, and therefore it is k=2 error detecting. This means that if one bit is flipped or two bits are flipped, the error can be detected. If three bits are flipped, then "000" becomes "111" and the error cannot be detected.
A code C is said to be k-error correcting if, for every word w in the underlying Hamming space H, there exists at most one codeword c (from C) such that the Hamming distance between w and c is at most k. In other words, a code is k-errors correcting if the minimum Hamming distance between any two of its codewords is at least 2k+1. This is also understood geometrically as any closed balls of radius k centered on distinct codewords being disjoint. These balls are also called Hamming spheres in this context.
For example, consider the same 3-bit code consisting of the two codewords "000" and "111". The Hamming space consists of 8 words 000, 001, 010, 011, 100, 101, 110 and 111. The codeword "000" and the single bit error words "001","010","100" are all less than or equal to the Hamming distance of 1 to "000". Likewise, codeword "111" and its single bit error words "110","101" and "011" are all within 1 Hamming distance of the original "111". In this code, a single bit error is always within 1 Hamming distance of the original codes, and the code can be 1-error correcting, that is k=1. Since the Hamming distance between "000" and "111" is 3, and those comprise the entire set of codewords in the code, the minimum Hamming distance is 3, which satisfies 2k+1 = 3.
Thus a code with minimum Hamming distance d between its codewords can detect at most d-1 errors and can correct ⌊(d-1)/2⌋ errors. The latter number is also called the packing radius or the error-correcting capability of the code.

History and applications
The Hamming distance is named after Richard Hamming, who introduced the concept in his fundamental paper on Hamming codes, Error detecting and error correcting codes, in 1950. Hamming weight analysis of bits is used in several disciplines including information theory, coding theory, and cryptography.
It is used in telecommunication to count the number of flipped bits in a fixed-length binary word as an estimate of error, and therefore is sometimes called the signal distance. For q-ary strings over an alphabet of size q ≥ 2 the Hamming distance is applied in case of the q-ary symmetric channel, while the Lee distance is used for phase-shift keying or more generally channels susceptible to synchronization errors because the Lee distance accounts for errors of ±1. If 
  
    
      
        q
        =
        2
      
    
    {\displaystyle q=2}
  
 or 
  
    
      
        q
        =
        3
      
    
    {\displaystyle q=3}
  
 both distances coincide because any pair of elements from 
  
    
      
        
          Z
        
        
          /
        
        2
        
          Z
        
      
    
    {\textstyle \mathbb {Z} /2\mathbb {Z} }
  
 or 
  
    
      
        
          Z
        
        
          /
        
        3
        
          Z
        
      
    
    {\textstyle \mathbb {Z} /3\mathbb {Z} }
  
 differ by 1, but the distances are different for larger 
  
    
      
        q
      
    
    {\displaystyle q}
  
.
The Hamming distance is also used in systematics as a measure of genetic distance.
However, for comparing strings of different lengths, or strings where not just substitutions but also insertions or deletions have to be expected, a more sophisticated metric like the Levenshtein distance is more appropriate.

Algorithm example
The following function, written in Python 3, returns the Hamming distance between two strings:

Or, in a shorter expression:

The function hamming_distance(), implemented in Python 3, computes the Hamming distance between two strings (or other iterable objects) of equal length by creating a sequence of Boolean values indicating mismatches and matches between corresponding positions in the two inputs, then summing the sequence with True and False values, interpreted as one and zero, respectively.

where the zip() function merges two equal-length collections in pairs.
The following C function will compute the Hamming distance of two integers (considered as binary values, that is, as sequences of bits). The running time of this procedure is proportional to the Hamming distance rather than to the number of bits in the inputs. It computes the bitwise exclusive or of the two inputs, and then finds the Hamming weight of the result (the number of nonzero bits) using an algorithm of Wegner (1960) that repeatedly finds and clears the lowest-order nonzero bit.  Some compilers support the __builtin_popcount function which can calculate this using specialized processor hardware where available.

A faster alternative is to use the population count (popcount) assembly instruction. Certain compilers such as GCC and Clang make it available via an intrinsic function:

See also
Closest string
Damerau–Levenshtein distance
Euclidean distance
Gap-Hamming problem
Gray code
Jaccard index
Jaro–Winkler distance
Levenshtein distance
Mahalanobis distance
Mannheim distance
Sørensen similarity index
Sparse distributed memory
Word ladder

References
Further reading
 This article incorporates public domain material from Federal Standard 1037C. General Services Administration. Archived from the original on 2022-01-22.
Wegner, Peter (1960). "A technique for counting ones in a binary computer". Communications of the ACM. 3 (5): 322. doi:10.1145/367236.367286. S2CID 31683715.
MacKay, David J. C. (2003). Information Theory, Inference, and Learning Algorithms. Cambridge: Cambridge University Press. ISBN 0-521-64298-1.

## Related Articles

### Internal Links

- [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
- [Aho–Corasick algorithm](https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm)
- [Alphabet](https://en.wikipedia.org/wiki/Alphabet)
- [Apostolico–Giancarlo algorithm](https://en.wikipedia.org/wiki/Apostolico%E2%80%93Giancarlo_algorithm)
- [Approximate string matching](https://en.wikipedia.org/wiki/Approximate_string_matching)
- [BLAST (biotechnology)](https://en.wikipedia.org/wiki/BLAST_(biotechnology))
- [Ball (mathematics)](https://en.wikipedia.org/wiki/Ball_(mathematics))
- [Best, worst and average case](https://en.wikipedia.org/wiki/Best,_worst_and_average_case)
- [Binary symmetric channel](https://en.wikipedia.org/wiki/Binary_symmetric_channel)
- [Bitap algorithm](https://en.wikipedia.org/wiki/Bitap_algorithm)
- [Bitwise operation](https://en.wikipedia.org/wiki/Bitwise_operation)
- [Block code](https://en.wikipedia.org/wiki/Block_code)
- [Boyer–Moore string-search algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm)
- [Boyer–Moore–Horspool algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore%E2%80%93Horspool_algorithm)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press)
- [Closest string](https://en.wikipedia.org/wiki/Closest_string)
- [Hamming space](https://en.wikipedia.org/wiki/Hamming_space)
- [Coding theory](https://en.wikipedia.org/wiki/Coding_theory)
- [Commentz-Walter algorithm](https://en.wikipedia.org/wiki/Commentz-Walter_algorithm)
- [Communications of the ACM](https://en.wikipedia.org/wiki/Communications_of_the_ACM)
- [Comparison of regular expression engines](https://en.wikipedia.org/wiki/Comparison_of_regular_expression_engines)
- [Compressed pattern matching](https://en.wikipedia.org/wiki/Compressed_pattern_matching)
- [Compressed suffix array](https://en.wikipedia.org/wiki/Compressed_suffix_array)
- [Copyright status of works by the federal government of the United States](https://en.wikipedia.org/wiki/Copyright_status_of_works_by_the_federal_government_of_the_United_States)
- [Cryptography](https://en.wikipedia.org/wiki/Cryptography)
- [Cube](https://en.wikipedia.org/wiki/Cube)
- [Damerau–Levenshtein distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Data structure](https://en.wikipedia.org/wiki/Data_structure)
- [David J. C. MacKay](https://en.wikipedia.org/wiki/David_J._C._MacKay)
- [Deterministic acyclic finite state automaton](https://en.wikipedia.org/wiki/Deterministic_acyclic_finite_state_automaton)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Edit distance](https://en.wikipedia.org/wiki/Edit_distance)
- [Elsevier](https://en.wikipedia.org/wiki/Elsevier)
- [Error detection and correction](https://en.wikipedia.org/wiki/Error_detection_and_correction)
- [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance)
- [Exclusive or](https://en.wikipedia.org/wiki/Exclusive_or)
- [FM-index](https://en.wikipedia.org/wiki/FM-index)
- [Finite field](https://en.wikipedia.org/wiki/Finite_field)
- [Gap-Hamming problem](https://en.wikipedia.org/wiki/Gap-Hamming_problem)
- [General Services Administration](https://en.wikipedia.org/wiki/General_Services_Administration)
- [Generalized suffix tree](https://en.wikipedia.org/wiki/Generalized_suffix_tree)
- [Gestalt pattern matching](https://en.wikipedia.org/wiki/Gestalt_pattern_matching)
- [Gray code](https://en.wikipedia.org/wiki/Gray_code)
- [Gérard Denis Cohen](https://en.wikipedia.org/wiki/G%C3%A9rard_Denis_Cohen)
- [Hacker's Delight](https://en.wikipedia.org/wiki/Hacker%27s_Delight)
- [Hamming code](https://en.wikipedia.org/wiki/Hamming_code)
- [Hamming space](https://en.wikipedia.org/wiki/Hamming_space)
- [Sphere packing](https://en.wikipedia.org/wiki/Sphere_packing)
- [Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight)
- [Handle System](https://en.wikipedia.org/wiki/Handle_System)
- [Hirschberg's algorithm](https://en.wikipedia.org/wiki/Hirschberg%27s_algorithm)
- [Hypercube](https://en.wikipedia.org/wiki/Hypercube)
- [Hypercube graph](https://en.wikipedia.org/wiki/Hypercube_graph)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Information theory](https://en.wikipedia.org/wiki/Information_theory)
- [Iterator](https://en.wikipedia.org/wiki/Iterator)
- [Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index)
- [Jaro–Winkler distance](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance)
- [Knuth–Morris–Pratt algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)
- [LCP array](https://en.wikipedia.org/wiki/LCP_array)
- [Lee distance](https://en.wikipedia.org/wiki/Lee_distance)
- [Levenshtein automaton](https://en.wikipedia.org/wiki/Levenshtein_automaton)
- [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
- [Longest common subsequence](https://en.wikipedia.org/wiki/Longest_common_subsequence)
- [Longest common substring](https://en.wikipedia.org/wiki/Longest_common_substring)
- [Mahalanobis distance](https://en.wikipedia.org/wiki/Mahalanobis_distance)
- [Taxicab geometry](https://en.wikipedia.org/wiki/Taxicab_geometry)
- [Lee distance](https://en.wikipedia.org/wiki/Lee_distance)
- [Metric space](https://en.wikipedia.org/wiki/Metric_space)
- [Needleman–Wunsch algorithm](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm)
- [Nondeterministic finite automaton](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton)
- [PubMed Central](https://en.wikipedia.org/wiki/PubMed_Central)
- [PubMed](https://en.wikipedia.org/wiki/PubMed)
- [Parsing](https://en.wikipedia.org/wiki/Parsing)
- [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching)
- [Pearson Education](https://en.wikipedia.org/wiki/Pearson_Education)
- [Peter Wegner](https://en.wikipedia.org/wiki/Peter_Wegner)
- [Phase-shift keying](https://en.wikipedia.org/wiki/Phase-shift_keying)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Rabin–Karp algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm)
- [Raita algorithm](https://en.wikipedia.org/wiki/Raita_algorithm)
- [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Regular grammar](https://en.wikipedia.org/wiki/Regular_grammar)
- [Richard Hamming](https://en.wikipedia.org/wiki/Richard_Hamming)
- [Rope (data structure)](https://en.wikipedia.org/wiki/Rope_(data_structure))
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Semi-Thue system](https://en.wikipedia.org/wiki/Semi-Thue_system)
- [Sequence alignment](https://en.wikipedia.org/wiki/Sequence_alignment)
- [Sequential pattern mining](https://en.wikipedia.org/wiki/Sequential_pattern_mining)
- [Smith–Waterman algorithm](https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm)
- [Space complexity](https://en.wikipedia.org/wiki/Space_complexity)
- [Sparse distributed memory](https://en.wikipedia.org/wiki/Sparse_distributed_memory)
- [Sphere packing](https://en.wikipedia.org/wiki/Sphere_packing)
- [Springer Science+Business Media](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [String-searching algorithm](https://en.wikipedia.org/wiki/String-searching_algorithm)
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [String metric](https://en.wikipedia.org/wiki/String_metric)
- [String operations](https://en.wikipedia.org/wiki/String_operations)
- [Substring index](https://en.wikipedia.org/wiki/Substring_index)
- [Suffix array](https://en.wikipedia.org/wiki/Suffix_array)
- [Suffix automaton](https://en.wikipedia.org/wiki/Suffix_automaton)
- [Suffix tree](https://en.wikipedia.org/wiki/Suffix_tree)
- [Symbol](https://en.wikipedia.org/wiki/Symbol)
- [Systematics](https://en.wikipedia.org/wiki/Systematics)
- [Dice-Sørensen coefficient](https://en.wikipedia.org/wiki/Dice-S%C3%B8rensen_coefficient)
- [Telecommunications](https://en.wikipedia.org/wiki/Telecommunications)
- [Ternary search tree](https://en.wikipedia.org/wiki/Ternary_search_tree)
- [Tesseract](https://en.wikipedia.org/wiki/Tesseract)
- [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction)
- [Time complexity](https://en.wikipedia.org/wiki/Time_complexity)
- [Triangle inequality](https://en.wikipedia.org/wiki/Triangle_inequality)
- [Trie](https://en.wikipedia.org/wiki/Trie)
- [Trigram search](https://en.wikipedia.org/wiki/Trigram_search)
- [Two-way string-matching algorithm](https://en.wikipedia.org/wiki/Two-way_string-matching_algorithm)
- [Vector space](https://en.wikipedia.org/wiki/Vector_space)
- [Wagner–Fischer algorithm](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm)
- [De Gruyter](https://en.wikipedia.org/wiki/De_Gruyter)
- [Formal language](https://en.wikipedia.org/wiki/Formal_language)
- [Word ladder](https://en.wikipedia.org/wiki/Word_ladder)
- [Zhu–Takaoka string matching algorithm](https://en.wikipedia.org/wiki/Zhu%E2%80%93Takaoka_string_matching_algorithm)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:Please clarify](https://en.wikipedia.org/wiki/Wikipedia:Please_clarify)
- [Wikipedia:When to cite](https://en.wikipedia.org/wiki/Wikipedia:When_to_cite)
- [Wikipedia:WikiProject Reliability](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Reliability)
- [Template:Strings](https://en.wikipedia.org/wiki/Template:Strings)
- [Template talk:Strings](https://en.wikipedia.org/wiki/Template_talk:Strings)
- [Help:Authority control](https://en.wikipedia.org/wiki/Help:Authority_control)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles lacking in-text citations from May 2015](https://en.wikipedia.org/wiki/Category:Articles_lacking_in-text_citations_from_May_2015)
- [Category:String sorting algorithms](https://en.wikipedia.org/wiki/Category:String_sorting_algorithms)
- [Category:Use American English from March 2019](https://en.wikipedia.org/wiki/Category:Use_American_English_from_March_2019)
- [Category:Wikipedia articles needing clarification from June 2020](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_needing_clarification_from_June_2020)
- [Portal:Mathematics](https://en.wikipedia.org/wiki/Portal:Mathematics)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:26:51.856015+00:00_