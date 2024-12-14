# Boyer–Moore string-search algorithm

## Article Metadata

- **Last Updated:** 2024-12-14T19:34:03.819389+00:00
- **Original Article:** [Boyer–Moore string-search algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm)
- **Language:** en
- **Page ID:** 684709

## Summary

In computer science, the Boyer–Moore string-search algorithm is an efficient string-searching algorithm that is the standard benchmark for practical string-search literature. It was developed by Robert S. Boyer and J Strother Moore in 1977. The original paper contained static tables for computing the pattern shifts without an explanation of how to produce them. The algorithm for producing the tables was published in a follow-on paper; this paper contained errors which were later corrected by Woj

## Categories

- Category:Articles with example C code
- Category:Articles with example Java code
- Category:Articles with example Python (programming language) code
- Category:Articles with imported Creative Commons Attribution-ShareAlike 3.0 text
- Category:Articles with short description
- Category:Commons category link from Wikidata
- Category:Computer-related introductions in 1977
- Category:Short description matches Wikidata
- Category:String matching algorithms

## Table of Contents

- Definitions
- Description
- Shift rules
- The Galil rule
- Performance
- Implementations
- Variants
- Notes
- References
- External links

## Content

In computer science, the Boyer–Moore string-search algorithm is an efficient string-searching algorithm that is the standard benchmark for practical string-search literature. It was developed by Robert S. Boyer and J Strother Moore in 1977. The original paper contained static tables for computing the pattern shifts without an explanation of how to produce them. The algorithm for producing the tables was published in a follow-on paper; this paper contained errors which were later corrected by Wojciech Rytter in 1980.
The algorithm preprocesses the string being searched for (the pattern), but not the string being searched in (the text). It is thus well-suited for applications in which the pattern is much shorter than the text or where it persists across multiple searches. The Boyer–Moore algorithm uses information gathered during the preprocess step to skip sections of the text, resulting in a lower constant factor than many other string search algorithms. In general, the algorithm runs faster as the pattern length increases. The key features of the algorithm are to match on the tail of the pattern rather than the head, and to skip along the text in jumps of multiple characters rather than searching every single character in the text.

Definitions
T denotes the input text to be searched. Its length is n.
P denotes the string to be searched for, called the pattern. Its length is m.
S[i] denotes the character at index i of string S, counting from 1.
S[i..j] denotes the substring of string S starting at index i and ending at j, inclusive.
A prefix of S is a substring S[1..i] for some i in range [1, l], where l is the length of S.
A suffix of S is a substring S[i..l] for some i in range [1, l], where l is the length of S.
An alignment of P to T is an index k in T such that the last character of P is aligned with index k of T.
A match or occurrence of P occurs at an alignment k if P is equivalent to T[(k-m+1)..k].

Description
The Boyer–Moore algorithm searches for occurrences of P in T by performing explicit character comparisons at different alignments. Instead of a brute-force search of all alignments (of which there are ⁠
  
    
      
        n
        −
        m
        +
        1
      
    
    {\displaystyle n-m+1}
  
⁠), Boyer–Moore uses information gained by preprocessing P to skip as many alignments as possible.
Previous to the introduction of this algorithm, the usual way to search within text was to examine each character of the text for the first character of the pattern. Once that was found the subsequent characters of the text would be compared to the characters of the pattern. If no match occurred then the text would again be checked character by character in an effort to find a match. Thus almost every character in the text needs to be examined.
The key insight in this algorithm is that if the end of the pattern is compared to the text, then jumps along the text can be made rather than checking every character of the text. The reason that this works is that in lining up the pattern against the text, the last character of the pattern is compared to the character in the text. If the characters do not match, there is no need to continue searching backwards along the text. If the character in the text does not match any of the characters in the pattern, then the next character in the text to check is located m characters farther along the text, where m is the length of the pattern. If the character in the text is in the pattern, then a partial shift of the pattern along the text is done to line up along the matching character and the process is repeated. Jumping along the text to make comparisons rather than checking every character in the text decreases the number of comparisons that have to be made, which is the key to the efficiency of the algorithm.
More formally, the algorithm begins at alignment ⁠
  
    
      
        k
        =
        m
      
    
    {\displaystyle k=m}
  
⁠, so the start of P is aligned with the start of T. Characters in P and T are then compared starting at index m in P and k in T, moving backward. The strings are matched from the end of P to the start of P. The comparisons continue until either the beginning of P is reached (which means there is a match) or a mismatch occurs upon which the alignment is shifted forward (to the right) according to the maximum value permitted by a number of rules. The comparisons are performed again at the new alignment, and the process repeats until the alignment is shifted past the end of T, which means no further matches will be found.
The shift rules are implemented as constant-time table lookups, using tables generated during the preprocessing of P.

Shift rules
A shift is calculated by applying two rules: the bad-character rule and the good-suffix rule. The actual shifting offset is the maximum of the shifts calculated by these rules.

The bad-character rule
Description
The bad-character rule considers the character in T at which the comparison process failed (assuming such a failure occurred). The next occurrence of that character to the left in P is found, and a shift which brings that occurrence in line with the mismatched occurrence in T is proposed. If the mismatched character does not occur to the left in P, a shift is proposed that moves the entirety of P past the point of mismatch.

Preprocessing
Methods vary on the exact form the table for the bad-character rule should take, but a simple constant-time lookup solution is as follows: create a 2D table which is indexed first by the index of the character c in the alphabet and second by the index i in the pattern. This lookup will return the occurrence of c in P with the next-highest index ⁠
  
    
      
        j
        <
        i
      
    
    {\displaystyle j<i}
  
⁠ or -1 if there is no such occurrence. The proposed shift will then be ⁠
  
    
      
        i
        −
        j
      
    
    {\displaystyle i-j}
  
⁠, with ⁠
  
    
      
        O
        (
        1
        )
      
    
    {\displaystyle O(1)}
  
⁠ lookup time and ⁠
  
    
      
        O
        (
        k
        m
        )
      
    
    {\displaystyle O(km)}
  
⁠ space, assuming a finite alphabet of length k.
The C and Java implementations below have a ⁠
  
    
      
        O
        (
        k
        )
      
    
    {\displaystyle O(k)}
  
⁠ space complexity (make_delta1, makeCharTable). This is the same as the original delta1 and the BMH bad-character table. This table maps a character at position ⁠
  
    
      
        i
      
    
    {\displaystyle i}
  
⁠ to shift by ⁠
  
    
      
        len
        ⁡
        (
        p
        )
        −
        1
        −
        i
      
    
    {\displaystyle \operatorname {len} (p)-1-i}
  
⁠, with the last instance—the least shift amount—taking precedence. All unused characters are set as ⁠
  
    
      
        len
        ⁡
        (
        p
        )
      
    
    {\displaystyle \operatorname {len} (p)}
  
⁠ as a sentinel value.

The good-suffix rule
Description
The good-suffix rule is markedly more complex in both concept and implementation than the bad-character rule. Like the bad-character rule, it also exploits the algorithm's feature of comparisons beginning at the end of the pattern and proceeding towards the pattern's start. It can be described as follows:

Suppose for a given alignment of P and T, a substring t of T matches a suffix of P and suppose t is the largest such substring for the given alignment.

Then find, if it exists, the right-most copy t′ of t in P such that t′ is not a suffix of P and the character to the left of t′ in P differs from the character to the left of t in P. Shift P to the right so that substring t′ in P aligns with substring t in T.
If t′ does not exist, then shift the left end of P to the right by the least amount (past the left end of t in T) so that a prefix of the shifted pattern matches a suffix of t in T. This includes cases where t is an exact match of P.
If no such shift is possible, then shift P by m (length of P) places to the right.

Preprocessing
The good-suffix rule requires two tables: one for use in the general case (where a copy t′ is found), and another for use when the general case returns no meaningful result. These tables will be designated L and H respectively. Their definitions are as follows:

For each i, ⁠
  
    
      
        L
        [
        i
        ]
      
    
    {\displaystyle L[i]}
  
⁠ is the largest position less than m such that string ⁠
  
    
      
        P
        [
        i
        .
        .
        m
        ]
      
    
    {\displaystyle P[i..m]}
  
⁠ matches a suffix of ⁠
  
    
      
        P
        [
        1..
        L
        [
        i
        ]
        ]
      
    
    {\displaystyle P[1..L[i]]}
  
⁠ and such that the character preceding that suffix is not equal to ⁠
  
    
      
        P
        [
        i
        −
        1
        ]
      
    
    {\displaystyle P[i-1]}
  
⁠. ⁠
  
    
      
        L
        [
        i
        ]
      
    
    {\displaystyle L[i]}
  
⁠ is defined to be zero if there is no position satisfying the condition.

Let ⁠
  
    
      
        H
        [
        i
        ]
      
    
    {\displaystyle H[i]}
  
⁠ denote the length of the largest suffix of ⁠
  
    
      
        P
        [
        i
        .
        .
        m
        ]
      
    
    {\displaystyle P[i..m]}
  
⁠ that is also a prefix of P, if one exists. If none exists, let ⁠
  
    
      
        H
        [
        i
        ]
      
    
    {\displaystyle H[i]}
  
⁠ be zero.

Both of these tables are constructible in ⁠
  
    
      
        O
        (
        m
        )
      
    
    {\displaystyle O(m)}
  
⁠ time and use ⁠
  
    
      
        O
        (
        m
        )
      
    
    {\displaystyle O(m)}
  
⁠ space. The alignment shift for index i in P is given by ⁠
  
    
      
        m
        −
        L
        [
        i
        ]
      
    
    {\displaystyle m-L[i]}
  
⁠ or ⁠
  
    
      
        m
        −
        H
        [
        i
        ]
      
    
    {\displaystyle m-H[i]}
  
⁠. H should only be used if ⁠
  
    
      
        L
        [
        i
        ]
      
    
    {\displaystyle L[i]}
  
⁠ is zero or a match has been found.

Shift Example using pattern ANPANMAN
Index| Mismatch | Shift   
 0   |         N|   1    
 1   |        AN|   8    
 2   |       MAN|   3    
 3   |      NMAN|   6   
 4   |     ANMAN|   6   
 5   |    PANMAN|   6  
 6   |   NPANMAN|   6  
 7   |  ANPANMAN|   6  

Explanation:
Index 0, no characters matched, the character read was not an N. The good-suffix length is zero. Since there are plenty of letters in the pattern that are also not N, we have minimal information here - shifting by 1 is the least interesting result.
Index 1, we matched the N, and it was preceded by something other than A. Now look at the pattern starting from the end, where do we have N preceded by something other than A? There are two other N's, but both are preceded by A. That means no part of the good suffix can be useful to us -- shift by the full pattern length 8.
Index 2: We matched the AN, and it was preceded by not M. In the middle of the pattern there is a AN preceded by P, so it becomes the shift candidate. Shifting that AN to the right to line up with our match is a shift of 3.
Index 3 & up: the matched suffixes do not match anything else in the pattern, but the trailing suffix AN matches the start of the pattern, so the shifts here are all 6.

The Galil rule
A simple but important optimization of Boyer–Moore was put forth by Zvi Galil in 1979.
As opposed to shifting, the Galil rule deals with speeding up the actual comparisons done at each alignment by skipping sections that are known to match. Suppose that at an alignment k1, P is compared with T down to character c of T. Then if P is shifted to k2 such that its left end is between c and k1, in the next comparison phase a prefix of P must match the substring T[(k2 - n)..k1]. Thus if the comparisons get down to position k1 of T, an occurrence of P can be recorded without explicitly comparing past k1. In addition to increasing the efficiency of Boyer–Moore, the Galil rule is required for proving linear-time execution in the worst case.
The Galil rule, in its original version, is only effective for versions that output multiple matches. It updates the substring range only on c = 0, i.e. a full match. A generalized version for dealing with submatches was reported in 1985 as the Apostolico–Giancarlo algorithm.

Performance
The Boyer–Moore algorithm as presented in the original paper has worst-case running time of ⁠
  
    
      
        O
        (
        n
        +
        m
        )
      
    
    {\displaystyle O(n+m)}
  
⁠ only if the pattern does not appear in the text. This was first proved by Knuth, Morris, and Pratt in 1977, followed by Guibas and Odlyzko in 1980 with an upper bound of 5n comparisons in the worst case. Richard Cole gave a proof with an upper bound of 3n comparisons in the worst case in 1991.
When the pattern does occur in the text, running time of the original algorithm is ⁠
  
    
      
        O
        (
        n
        m
        )
      
    
    {\displaystyle O(nm)}
  
⁠ in the worst case. This is easy to see when both pattern and text consist solely of the same repeated character. However, inclusion of the Galil rule results in linear runtime across all cases.

Implementations
Various implementations exist in different programming languages. In C++ it is part of the Standard Library since C++17 and Boost provides the generic Boyer–Moore search implementation under the Algorithm library. In Go (programming language) there is an implementation in search.go. D (programming language) uses a BoyerMooreFinder for predicate based matching within ranges as a part of the Phobos Runtime Library.
The Boyer–Moore algorithm is also used in GNU's grep.

Variants
The Boyer–Moore–Horspool algorithm is a simplification of the Boyer–Moore algorithm using only the bad-character rule.
The Apostolico–Giancarlo algorithm speeds up the process of checking whether a match has occurred at the given alignment by skipping explicit character comparisons. This uses information gleaned during the pre-processing of the pattern in conjunction with suffix match lengths recorded at each match attempt. Storing suffix match lengths requires an additional table equal in size to the text being searched.
The Raita algorithm improves the performance of Boyer–Moore–Horspool algorithm. The searching pattern of particular sub-string in a given string is different from Boyer–Moore–Horspool algorithm.

Notes
References
External links

Original paper on the Boyer-Moore algorithm
An example of the Boyer-Moore algorithm from the homepage of J Strother Moore, co-inventor of the algorithm
Richard Cole's 1991 paper proving runtime linearity

## Related Articles

### Internal Links

- [Aho–Corasick algorithm](https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm)
- [Andrew Odlyzko](https://en.wikipedia.org/wiki/Andrew_Odlyzko)
- [Apostolico–Giancarlo algorithm](https://en.wikipedia.org/wiki/Apostolico%E2%80%93Giancarlo_algorithm)
- [Approximate string matching](https://en.wikipedia.org/wiki/Approximate_string_matching)
- [BLAST (biotechnology)](https://en.wikipedia.org/wiki/BLAST_(biotechnology))
- [Best, worst and average case](https://en.wikipedia.org/wiki/Best,_worst_and_average_case)
- [Bitap algorithm](https://en.wikipedia.org/wiki/Bitap_algorithm)
- [Boost (C++ libraries)](https://en.wikipedia.org/wiki/Boost_(C%2B%2B_libraries))
- [Boyer–Moore–Horspool algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore%E2%80%93Horspool_algorithm)
- [Brute-force search](https://en.wikipedia.org/wiki/Brute-force_search)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Commentz-Walter algorithm](https://en.wikipedia.org/wiki/Commentz-Walter_algorithm)
- [Comparison of regular expression engines](https://en.wikipedia.org/wiki/Comparison_of_regular_expression_engines)
- [Compressed pattern matching](https://en.wikipedia.org/wiki/Compressed_pattern_matching)
- [Compressed suffix array](https://en.wikipedia.org/wiki/Compressed_suffix_array)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Damerau–Levenshtein distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Data structure](https://en.wikipedia.org/wiki/Data_structure)
- [Deterministic acyclic finite state automaton](https://en.wikipedia.org/wiki/Deterministic_acyclic_finite_state_automaton)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Donald Knuth](https://en.wikipedia.org/wiki/Donald_Knuth)
- [Edit distance](https://en.wikipedia.org/wiki/Edit_distance)
- [FM-index](https://en.wikipedia.org/wiki/FM-index)
- [GNU](https://en.wikipedia.org/wiki/GNU)
- [Boyer–Moore string-search algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm)
- [Generalized suffix tree](https://en.wikipedia.org/wiki/Generalized_suffix_tree)
- [Gestalt pattern matching](https://en.wikipedia.org/wiki/Gestalt_pattern_matching)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [Grep](https://en.wikipedia.org/wiki/Grep)
- [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance)
- [Hirschberg's algorithm](https://en.wikipedia.org/wiki/Hirschberg%27s_algorithm)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [J Strother Moore](https://en.wikipedia.org/wiki/J_Strother_Moore)
- [James H. Morris](https://en.wikipedia.org/wiki/James_H._Morris)
- [Jaro–Winkler distance](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance)
- [Knuth–Morris–Pratt algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)
- [LCP array](https://en.wikipedia.org/wiki/LCP_array)
- [Lee distance](https://en.wikipedia.org/wiki/Lee_distance)
- [Leonidas J. Guibas](https://en.wikipedia.org/wiki/Leonidas_J._Guibas)
- [Levenshtein automaton](https://en.wikipedia.org/wiki/Levenshtein_automaton)
- [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
- [Longest common subsequence](https://en.wikipedia.org/wiki/Longest_common_subsequence)
- [Longest common substring](https://en.wikipedia.org/wiki/Longest_common_substring)
- [Needleman–Wunsch algorithm](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm)
- [Nondeterministic finite automaton](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton)
- [Nqthm](https://en.wikipedia.org/wiki/Nqthm)
- [Parsing](https://en.wikipedia.org/wiki/Parsing)
- [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching)
- [Preprocessor](https://en.wikipedia.org/wiki/Preprocessor)
- [Rabin–Karp algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm)
- [Raita algorithm](https://en.wikipedia.org/wiki/Raita_algorithm)
- [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Regular grammar](https://en.wikipedia.org/wiki/Regular_grammar)
- [Richard J. Cole](https://en.wikipedia.org/wiki/Richard_J._Cole)
- [Robert S. Boyer](https://en.wikipedia.org/wiki/Robert_S._Boyer)
- [Rope (data structure)](https://en.wikipedia.org/wiki/Rope_(data_structure))
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Semi-Thue system](https://en.wikipedia.org/wiki/Semi-Thue_system)
- [Sequence alignment](https://en.wikipedia.org/wiki/Sequence_alignment)
- [Sequential pattern mining](https://en.wikipedia.org/wiki/Sequential_pattern_mining)
- [Smith–Waterman algorithm](https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm)
- [Space complexity](https://en.wikipedia.org/wiki/Space_complexity)
- [String-searching algorithm](https://en.wikipedia.org/wiki/String-searching_algorithm)
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [String metric](https://en.wikipedia.org/wiki/String_metric)
- [String operations](https://en.wikipedia.org/wiki/String_operations)
- [Substring](https://en.wikipedia.org/wiki/Substring)
- [Substring index](https://en.wikipedia.org/wiki/Substring_index)
- [Suffix array](https://en.wikipedia.org/wiki/Suffix_array)
- [Suffix automaton](https://en.wikipedia.org/wiki/Suffix_automaton)
- [Suffix tree](https://en.wikipedia.org/wiki/Suffix_tree)
- [Ternary search tree](https://en.wikipedia.org/wiki/Ternary_search_tree)
- [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction)
- [Time complexity](https://en.wikipedia.org/wiki/Time_complexity)
- [Trie](https://en.wikipedia.org/wiki/Trie)
- [Trigram search](https://en.wikipedia.org/wiki/Trigram_search)
- [Two-way string-matching algorithm](https://en.wikipedia.org/wiki/Two-way_string-matching_algorithm)
- [Vaughan Pratt](https://en.wikipedia.org/wiki/Vaughan_Pratt)
- [Wagner–Fischer algorithm](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm)
- [Wojciech Rytter](https://en.wikipedia.org/wiki/Wojciech_Rytter)
- [Zhu–Takaoka string matching algorithm](https://en.wikipedia.org/wiki/Zhu%E2%80%93Takaoka_string_matching_algorithm)
- [Zvi Galil](https://en.wikipedia.org/wiki/Zvi_Galil)
- [Template:Strings](https://en.wikipedia.org/wiki/Template:Strings)
- [Template talk:Strings](https://en.wikipedia.org/wiki/Template_talk:Strings)
- [Category:String sorting algorithms](https://en.wikipedia.org/wiki/Category:String_sorting_algorithms)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:34:03.819389+00:00_