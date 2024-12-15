# Trie

## Article Metadata

- **Last Updated:** 2024-12-15T04:52:35.422962+00:00
- **Original Article:** [Trie](https://en.wikipedia.org/wiki/Trie)
- **Language:** en
- **Page ID:** 31274

## Summary

In computer science, a trie (, ), also called digital tree or prefix tree, is a type of search tree: specifically, a k-ary tree data structure used for locating specific keys from within a set. These keys are most often strings, with links between nodes defined not by the entire key, but by individual characters. In order to access a key (to recover its value, change it, or remove it), the trie is traversed depth-first, following the links between nodes, which represent each character in the key

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Commons category link from Wikidata
- Category:Finite automata
- Category:Good articles
- Category:Short description is different from Wikidata
- Category:Trees (data structures)

## Table of Contents

- History, etymology, and pronunciation
- Overview
- Operations
- Replacing other data structures
- Implementation strategies
- Applications
- See also
- References
- External links

## Content

In computer science, a trie (, ), also called digital tree or prefix tree, is a type of search tree: specifically, a k-ary tree data structure used for locating specific keys from within a set. These keys are most often strings, with links between nodes defined not by the entire key, but by individual characters. In order to access a key (to recover its value, change it, or remove it), the trie is traversed depth-first, following the links between nodes, which represent each character in the key.
Unlike a binary search tree, nodes in the trie do not store their associated key. Instead, a node's position in the trie defines the key with which it is associated. This distributes the value of each key across the data structure, and means that not every node necessarily has an associated value.
All the children of a node have a common prefix of the string associated with that parent node, and the root is associated with the empty string. This task of storing data accessible by its prefix can be accomplished in a memory-optimized way by employing a radix tree.
Though tries can be keyed by character strings, they need not be. The same algorithms can be adapted for ordered lists of any underlying type, e.g. permutations of digits or shapes. In particular, a bitwise trie is keyed on the individual bits making up a piece of fixed-length binary data, such as an integer or memory address. The key lookup complexity of a trie remains proportional to the key size. Specialized trie implementations such as compressed tries are used to deal with the enormous space requirement of a trie in naive implementations.

History, etymology, and pronunciation
The idea of a trie for representing a set of strings was first abstractly described by Axel Thue in 1912. Tries were first described in a computer context by René de la Briandais in 1959.: 336 
The idea was independently described in 1960 by Edward Fredkin, who coined the term trie, pronouncing it  (as "tree"), after the middle syllable of retrieval. However, other authors pronounce it  (as "try"), in an attempt to distinguish it verbally from "tree".

Overview
Tries are a form of string-indexed look-up data structure, which is used to store a dictionary list of words that can be searched on in a manner that allows for efficient generation of completion lists.: 1  A prefix trie is an ordered tree data structure used in the representation of a set of strings over a finite alphabet set, which allows efficient storage of words with common prefixes.
Tries can be efficacious on string-searching algorithms such as predictive text, approximate string matching, and spell checking in comparison to binary search trees.: 358  A trie can be seen as a tree-shaped deterministic finite automaton.

Operations
Tries support various operations: insertion, deletion, and lookup of a string key. Tries are composed of nodes that contain links, which either point to other suffix child nodes or null. As for every tree, each node but the root is pointed to by only one other node, called its parent. Each node contains as many links as the number of characters in the applicable alphabet (although tries tend to have a substantial number of null links). In some cases, the alphabet used is simply that of the character encoding—resulting in, for example, a size of 256 in the case of (unsigned) ASCII.: 732 
The null links within the children of a node emphasize the following characteristics:: 734 : 336 

Characters and string keys are implicitly stored in the trie, and include a character sentinel value indicating string termination.
Each node contains one possible link to a prefix of strong keys of the set.
A basic structure type of nodes in the trie is as follows; 
  
    
      
        
          Node
        
      
    
    {\displaystyle {\text{Node}}}
  
 may contain an optional 
  
    
      
        
          Value
        
      
    
    {\displaystyle {\text{Value}}}
  
, which is associated with each key stored in the last character of string, or terminal node.

Searching
Searching for a value in a trie is guided by the characters in the search string key, as each node in the trie contains a corresponding link to each possible character in the given string. Thus, following the string within the trie yields the associated value for the given string key. A null link during the search indicates the inexistence of the key.: 732-733 
The following pseudocode implements the search procedure for a given string key in a rooted trie x.: 135 

In the above pseudocode, x and key correspond to the pointer of trie's root node and the string key respectively. The search operation, in a standard trie, takes 
  
    
      
        O
        (
        
          dm
        
        )
      
    
    {\displaystyle O({\text{dm}})}
  
 time, where 
  
    
      
        
          m
        
      
    
    {\displaystyle {\text{m}}}
  
 is the size of the string parameter 
  
    
      
        
          key
        
      
    
    {\displaystyle {\text{key}}}
  
, and 
  
    
      
        
          d
        
      
    
    {\displaystyle {\text{d}}}
  
 corresponds to the alphabet size.: 754  Binary search trees, on the other hand, take 
  
    
      
        O
        (
        m
        log
        ⁡
        n
        )
      
    
    {\displaystyle O(m\log n)}
  
 in the worst case, since the search depends on the height of the tree (
  
    
      
        log
        ⁡
        n
      
    
    {\displaystyle \log n}
  
) of the BST (in case of balanced trees), where 
  
    
      
        
          n
        
      
    
    {\displaystyle {\text{n}}}
  
 and 
  
    
      
        
          m
        
      
    
    {\displaystyle {\text{m}}}
  
 being number of keys and the length of the keys.: 358 
The trie occupies less space in comparison with a BST in the case of a large number of short strings, since nodes share common initial string subsequences and store the keys implicitly.: 358  The terminal node of the tree contains a non-null value, and it is a search hit if the associated value is found in the trie, and search miss if it is not.: 733

Insertion
Insertion into trie is guided by using the character sets as indexes to the children array until the last character of the string key is reached.: 733-734  Each node in the trie corresponds to one call of the radix sorting routine, as the trie structure reflects the execution of pattern of the top-down radix sort.: 135 

If a null link is encountered prior to reaching the last character of the string key, a new node is created (line 3).: 745  The value of the terminal node is assigned to the input value; therefore, if the former was non-null at the time of insertion, it is substituted with the new value.

Deletion
Deletion of a key–value pair from a trie involves finding the terminal node with the corresponding string key, marking the terminal indicator and value to false and null correspondingly.: 740 
The following is a recursive procedure for removing a string key from rooted trie (x).

The procedure begins by examining the key; null denotes the arrival of a terminal node or end of a string key. If the node is terminal it has no children, it is removed from the trie (line 14). However, an end of string key without the node being terminal indicates that the key does not exist, thus the procedure does not modify the trie. The recursion proceeds by incrementing key's index.

Replacing other data structures
Replacement for hash tables
A trie can be used to replace a hash table, over which it has the following advantages:: 358 

Searching for a node with an associated key of size 
  
    
      
        m
      
    
    {\displaystyle m}
  
 has the complexity of 
  
    
      
        O
        (
        m
        )
      
    
    {\displaystyle O(m)}
  
, whereas an imperfect hash function may have numerous colliding keys, and the worst-case lookup speed of such a table would be 
  
    
      
        O
        (
        N
        )
      
    
    {\displaystyle O(N)}
  
, where 
  
    
      
        N
      
    
    {\displaystyle N}
  
 denotes the total number of nodes within the table.
Tries do not need a hash function for the operation, unlike a hash table; there are also no collisions of different keys in a trie.
Buckets in a trie, which are analogous to hash table buckets that store key collisions, are necessary only if a single key is associated with more than one value.
String keys within the trie can be sorted using a predetermined alphabetical ordering.
However, tries are less efficient than a hash table when the data is directly accessed on a secondary storage device such as a hard disk drive that has higher random access time than the main memory. Tries are also disadvantageous when the key value cannot be easily represented as string, such as floating point numbers where multiple representations are possible (e.g. 1 is equivalent to 1.0, +1.0, 1.00, etc.),: 359  however it can be unambiguously represented as a binary number in IEEE 754, in comparison to two's complement format.

Implementation strategies
Tries can be represented in several ways, corresponding to different trade-offs between memory use and speed of the operations.: 341  Using a vector of pointers for representing a trie consumes enormous space; however, memory space can be reduced at the expense of running time if a singly linked list is used for each node vector, as most entries of the vector contains 
  
    
      
        
          nil
        
      
    
    {\displaystyle {\text{nil}}}
  
.: 495 
Techniques such as alphabet reduction may alleviate the high space complexity by reinterpreting the original string as a long string over a smaller alphabet i.e. a string of n bytes can alternatively be regarded as a string of 2n four-bit units and stored in a trie with sixteen pointers per node. However, lookups need to visit twice as many nodes in the worst-case, although space requirements go down by a factor of eight.: 347–352  Other techniques include storing a vector of 256 ASCII pointers as a bitmap of 256 bits representing ASCII alphabet, which reduces the size of individual nodes dramatically.

Bitwise tries
Bitwise tries are used to address the enormous space requirement for the trie nodes in a naive simple pointer vector implementations. Each character in the string key set is represented via individual bits, which are used to traverse the trie over a string key. The implementations for these types of trie use vectorized CPU instructions to find the first set bit in a fixed-length key input (e.g. GCC's __builtin_clz() intrinsic function). Accordingly, the set bit is used to index the first item, or child node, in the 32- or 64-entry based bitwise tree. Search then proceeds by testing each subsequent bit in the key.
This procedure is also cache-local and highly parallelizable due to register independency, and thus performant on out-of-order execution CPUs.

Compressed tries
Radix tree, also known as a compressed trie, is a space-optimized variant of a trie in which any node with only one child gets merged with its parent; elimination of branches of the nodes with a single child results in better metrics in both space and time.: 452  This works best when the trie remains static and set of keys stored are very sparse within their representation space.: 3–16 
One more approach is to "pack" the trie, in which a space-efficient implementation of a sparse packed trie applied to automatic hyphenation, in which the descendants of each node may be interleaved in memory.

Patricia trees
Patricia trees are a particular implementation of the compressed binary trie that uses the binary encoding of the string keys in its representation.: 140  Every node in a Patricia tree contains an index, known as a "skip number", that stores the node's branching index to avoid empty subtrees during traversal.: 140-141  A naive implementation of a trie consumes immense storage due to larger number of leaf-nodes caused by sparse distribution of keys; Patricia trees can be efficient for such cases.: 142 : 3 
A representation of a Patricia tree is shown to the right. Each index value adjacent to the nodes represents the "skip number"—the index of the bit with which branching is to be decided.: 3  The skip number 1 at node 0 corresponds to the position 1 in the binary encoded ASCII where the leftmost bit differed in the key set 
  
    
      
        X
      
    
    {\displaystyle X}
  
.: 3-4  The skip number is crucial for search, insertion, and deletion of nodes in the Patricia tree, and a bit masking operation is performed during every iteration.: 143

Applications
Trie data structures are commonly used in predictive text or autocomplete dictionaries, and approximate matching algorithms. Tries enable faster searches, occupy less space, especially when the set contains large number of short strings, thus used in spell checking, hyphenation applications and longest prefix match algorithms.: 358  However, if storing dictionary words is all that is required (i.e. there is no need to store metadata associated with each word), a minimal deterministic acyclic finite state automaton (DAFSA) or radix tree would use less storage space than a trie. This is because DAFSAs and radix trees can compress identical branches from the trie which correspond to the same suffixes (or parts) of different words being stored. String dictionaries are also utilized in natural language processing, such as finding lexicon of a text corpus.: 73

Sorting
Lexicographic sorting of a set of string keys can be implemented by building a trie for the given keys and traversing the tree in pre-order fashion; this is also a form of radix sort. Tries are also fundamental data structures for burstsort, which is notable for being the fastest string sorting algorithm as of 2007, accomplished by its efficient use of CPU cache.

Full-text search
A special kind of trie, called a suffix tree, can be used to index all suffixes in a text to carry out fast full-text searches.

Web search engines
A specialized kind of trie called a compressed trie, is used in web search engines for storing the indexes - a collection of all searchable words. Each terminal node is associated with a list of URLs—called occurrence list—to pages that match the keyword. The trie is stored in the main memory, whereas the occurrence is kept in an external storage, frequently in large clusters, or the in-memory index points to documents stored in an external location.

Bioinformatics
Tries are used in Bioinformatics, notably in sequence alignment software applications such as BLAST, which indexes all the different substring of length k (called k-mers) of a text by storing the positions of their occurrences in a compressed trie sequence databases.: 75

Internet routing
Compressed variants of tries, such as databases for managing Forwarding Information Base (FIB), are used in storing IP address prefixes within routers and bridges for prefix-based lookup to resolve mask-based operations in IP routing.: 75

See also
References
External links

NIST's Dictionary of Algorithms and Data Structures: Trie

## Related Articles

### Internal Links

- [B-tree](https://en.wikipedia.org/wiki/B-tree)
- [2–3 tree](https://en.wikipedia.org/wiki/2%E2%80%933_tree)
- [2–3–4 tree](https://en.wikipedia.org/wiki/2%E2%80%933%E2%80%934_tree)
- [AA tree](https://en.wikipedia.org/wiki/AA_tree)
- [ASCII](https://en.wikipedia.org/wiki/ASCII)
- [AVL tree](https://en.wikipedia.org/wiki/AVL_tree)
- [Abstract data type](https://en.wikipedia.org/wiki/Abstract_data_type)
- [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
- [Aho–Corasick algorithm](https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm)
- [Alphabet (formal languages)](https://en.wikipedia.org/wiki/Alphabet_(formal_languages))
- [Apostolico–Giancarlo algorithm](https://en.wikipedia.org/wiki/Apostolico%E2%80%93Giancarlo_algorithm)
- [Approximate string matching](https://en.wikipedia.org/wiki/Approximate_string_matching)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Array (data structure)](https://en.wikipedia.org/wiki/Array_(data_structure))
- [Association for Computing Machinery](https://en.wikipedia.org/wiki/Association_for_Computing_Machinery)
- [Association list](https://en.wikipedia.org/wiki/Association_list)
- [Associative array](https://en.wikipedia.org/wiki/Associative_array)
- [Autocomplete](https://en.wikipedia.org/wiki/Autocomplete)
- [Axel Thue](https://en.wikipedia.org/wiki/Axel_Thue)
- [B-tree](https://en.wikipedia.org/wiki/B-tree)
- [B+ tree](https://en.wikipedia.org/wiki/B%2B_tree)
- [B-tree](https://en.wikipedia.org/wiki/B-tree)
- [BK-tree](https://en.wikipedia.org/wiki/BK-tree)
- [BLAST (biotechnology)](https://en.wikipedia.org/wiki/BLAST_(biotechnology))
- [Binary space partitioning](https://en.wikipedia.org/wiki/Binary_space_partitioning)
- [Self-balancing binary search tree](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree)
- [Ball tree](https://en.wikipedia.org/wiki/Ball_tree)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Binary code](https://en.wikipedia.org/wiki/Binary_code)
- [Binary decision diagram](https://en.wikipedia.org/wiki/Binary_decision_diagram)
- [Binary heap](https://en.wikipedia.org/wiki/Binary_heap)
- [Binary number](https://en.wikipedia.org/wiki/Binary_number)
- [Binary search tree](https://en.wikipedia.org/wiki/Binary_search_tree)
- [Binary search tree](https://en.wikipedia.org/wiki/Binary_search_tree)
- [Binomial heap](https://en.wikipedia.org/wiki/Binomial_heap)
- [Bioinformatics](https://en.wikipedia.org/wiki/Bioinformatics)
- [Bit](https://en.wikipedia.org/wiki/Bit)
- [Bit array](https://en.wikipedia.org/wiki/Bit_array)
- [Mask (computing)](https://en.wikipedia.org/wiki/Mask_(computing))
- [Bitap algorithm](https://en.wikipedia.org/wiki/Bitap_algorithm)
- [Bitwise trie with bitmap](https://en.wikipedia.org/wiki/Bitwise_trie_with_bitmap)
- [Boston](https://en.wikipedia.org/wiki/Boston)
- [Boyer–Moore string-search algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm)
- [Boyer–Moore–Horspool algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore%E2%80%93Horspool_algorithm)
- [Brodal queue](https://en.wikipedia.org/wiki/Brodal_queue)
- [Burstsort](https://en.wikipedia.org/wiki/Burstsort)
- [Bx-tree](https://en.wikipedia.org/wiki/Bx-tree)
- [C-trie](https://en.wikipedia.org/wiki/C-trie)
- [Processor register](https://en.wikipedia.org/wiki/Processor_register)
- [Cache (computing)](https://en.wikipedia.org/wiki/Cache_(computing))
- [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press)
- [Cartesian tree](https://en.wikipedia.org/wiki/Cartesian_tree)
- [Chapman & Hall](https://en.wikipedia.org/wiki/Chapman_%26_Hall)
- [Character (computing)](https://en.wikipedia.org/wiki/Character_(computing))
- [Character encoding](https://en.wikipedia.org/wiki/Character_encoding)
- [Circular buffer](https://en.wikipedia.org/wiki/Circular_buffer)
- [Collection (abstract data type)](https://en.wikipedia.org/wiki/Collection_(abstract_data_type))
- [Commentz-Walter algorithm](https://en.wikipedia.org/wiki/Commentz-Walter_algorithm)
- [Communications of the ACM](https://en.wikipedia.org/wiki/Communications_of_the_ACM)
- [Comparison of regular expression engines](https://en.wikipedia.org/wiki/Comparison_of_regular_expression_engines)
- [Composite data type](https://en.wikipedia.org/wiki/Composite_data_type)
- [Compressed pattern matching](https://en.wikipedia.org/wiki/Compressed_pattern_matching)
- [Compressed suffix array](https://en.wikipedia.org/wiki/Compressed_suffix_array)
- [Computational Linguistics (journal)](https://en.wikipedia.org/wiki/Computational_Linguistics_(journal))
- [Computer cluster](https://en.wikipedia.org/wiki/Computer_cluster)
- [Computer data storage](https://en.wikipedia.org/wiki/Computer_data_storage)
- [Container (abstract data type)](https://en.wikipedia.org/wiki/Container_(abstract_data_type))
- [Cover tree](https://en.wikipedia.org/wiki/Cover_tree)
- [Ctrie](https://en.wikipedia.org/wiki/Ctrie)
- [D-ary heap](https://en.wikipedia.org/wiki/D-ary_heap)
- [Damerau–Levenshtein distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Dancing tree](https://en.wikipedia.org/wiki/Dancing_tree)
- [Data structure](https://en.wikipedia.org/wiki/Data_structure)
- [Depth-first search](https://en.wikipedia.org/wiki/Depth-first_search)
- [Deterministic acyclic finite state automaton](https://en.wikipedia.org/wiki/Deterministic_acyclic_finite_state_automaton)
- [Deterministic finite automaton](https://en.wikipedia.org/wiki/Deterministic_finite_automaton)
- [Directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)
- [Disjoint-set data structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Donald Knuth](https://en.wikipedia.org/wiki/Donald_Knuth)
- [Double-ended priority queue](https://en.wikipedia.org/wiki/Double-ended_priority_queue)
- [Double-ended queue](https://en.wikipedia.org/wiki/Double-ended_queue)
- [Dynamic array](https://en.wikipedia.org/wiki/Dynamic_array)
- [Edit distance](https://en.wikipedia.org/wiki/Edit_distance)
- [Edward Fredkin](https://en.wikipedia.org/wiki/Edward_Fredkin)
- [Elsevier](https://en.wikipedia.org/wiki/Elsevier)
- [Emory University](https://en.wikipedia.org/wiki/Emory_University)
- [Empty string](https://en.wikipedia.org/wiki/Empty_string)
- [Exponential tree](https://en.wikipedia.org/wiki/Exponential_tree)
- [FM-index](https://en.wikipedia.org/wiki/FM-index)
- [Fenwick tree](https://en.wikipedia.org/wiki/Fenwick_tree)
- [Fibonacci heap](https://en.wikipedia.org/wiki/Fibonacci_heap)
- [Find first set](https://en.wikipedia.org/wiki/Find_first_set)
- [Finger tree](https://en.wikipedia.org/wiki/Finger_tree)
- [Floating-point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic)
- [Forwarding information base](https://en.wikipedia.org/wiki/Forwarding_information_base)
- [Fractal tree index](https://en.wikipedia.org/wiki/Fractal_tree_index)
- [Fusion tree](https://en.wikipedia.org/wiki/Fusion_tree)
- [GNU Compiler Collection](https://en.wikipedia.org/wiki/GNU_Compiler_Collection)
- [Generalized suffix tree](https://en.wikipedia.org/wiki/Generalized_suffix_tree)
- [Gestalt pattern matching](https://en.wikipedia.org/wiki/Gestalt_pattern_matching)
- [Graph (abstract data type)](https://en.wikipedia.org/wiki/Graph_(abstract_data_type))
- [HAL (open archive)](https://en.wikipedia.org/wiki/HAL_(open_archive))
- [HAT-trie](https://en.wikipedia.org/wiki/HAT-trie)
- [HTree](https://en.wikipedia.org/wiki/HTree)
- [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance)
- [Hash array mapped trie](https://en.wikipedia.org/wiki/Hash_array_mapped_trie)
- [Hash calendar](https://en.wikipedia.org/wiki/Hash_calendar)
- [Hash collision](https://en.wikipedia.org/wiki/Hash_collision)
- [Hash table](https://en.wikipedia.org/wiki/Hash_table)
- [Hash tree (persistent data structure)](https://en.wikipedia.org/wiki/Hash_tree_(persistent_data_structure))
- [Hash trie](https://en.wikipedia.org/wiki/Hash_trie)
- [Hashed array tree](https://en.wikipedia.org/wiki/Hashed_array_tree)
- [Heap (data structure)](https://en.wikipedia.org/wiki/Heap_(data_structure))
- [Hilbert R-tree](https://en.wikipedia.org/wiki/Hilbert_R-tree)
- [Hirschberg's algorithm](https://en.wikipedia.org/wiki/Hirschberg%27s_algorithm)
- [Syllabification](https://en.wikipedia.org/wiki/Syllabification)
- [IDistance](https://en.wikipedia.org/wiki/IDistance)
- [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)
- [IP routing](https://en.wikipedia.org/wiki/IP_routing)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Implicit k-d tree](https://en.wikipedia.org/wiki/Implicit_k-d_tree)
- [Information Systems (journal)](https://en.wikipedia.org/wiki/Information_Systems_(journal))
- [Integer (computer science)](https://en.wikipedia.org/wiki/Integer_(computer_science))
- [Interval tree](https://en.wikipedia.org/wiki/Interval_tree)
- [Intrinsic function](https://en.wikipedia.org/wiki/Intrinsic_function)
- [Jaro–Winkler distance](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance)
- [M-ary tree](https://en.wikipedia.org/wiki/M-ary_tree)
- [K-d tree](https://en.wikipedia.org/wiki/K-d_tree)
- [K-mer](https://en.wikipedia.org/wiki/K-mer)
- [Name–value pair](https://en.wikipedia.org/wiki/Name%E2%80%93value_pair)
- [Knuth–Morris–Pratt algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)
- [LCP array](https://en.wikipedia.org/wiki/LCP_array)
- [Lee distance](https://en.wikipedia.org/wiki/Lee_distance)
- [Left-child right-sibling binary tree](https://en.wikipedia.org/wiki/Left-child_right-sibling_binary_tree)
- [Left-leaning red–black tree](https://en.wikipedia.org/wiki/Left-leaning_red%E2%80%93black_tree)
- [Leftist tree](https://en.wikipedia.org/wiki/Leftist_tree)
- [Levenshtein automaton](https://en.wikipedia.org/wiki/Levenshtein_automaton)
- [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
- [Lexicographic order](https://en.wikipedia.org/wiki/Lexicographic_order)
- [Lexicon](https://en.wikipedia.org/wiki/Lexicon)
- [Link/cut tree](https://en.wikipedia.org/wiki/Link/cut_tree)
- [Linked data structure](https://en.wikipedia.org/wiki/Linked_data_structure)
- [Linked list](https://en.wikipedia.org/wiki/Linked_list)
- [List (abstract data type)](https://en.wikipedia.org/wiki/List_(abstract_data_type))
- [List of data structures](https://en.wikipedia.org/wiki/List_of_data_structures)
- [Locality of reference](https://en.wikipedia.org/wiki/Locality_of_reference)
- [Log-structured merge-tree](https://en.wikipedia.org/wiki/Log-structured_merge-tree)
- [Longest common subsequence](https://en.wikipedia.org/wiki/Longest_common_subsequence)
- [Longest common substring](https://en.wikipedia.org/wiki/Longest_common_substring)
- [Longest prefix match](https://en.wikipedia.org/wiki/Longest_prefix_match)
- [Computational complexity](https://en.wikipedia.org/wiki/Computational_complexity)
- [Luleå algorithm](https://en.wikipedia.org/wiki/Lule%C3%A5_algorithm)
- [M-ary tree](https://en.wikipedia.org/wiki/M-ary_tree)
- [M-tree](https://en.wikipedia.org/wiki/M-tree)
- [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
- [Vantage-point tree](https://en.wikipedia.org/wiki/Vantage-point_tree)
- [Computer data storage](https://en.wikipedia.org/wiki/Computer_data_storage)
- [Memory address](https://en.wikipedia.org/wiki/Memory_address)
- [Merkle tree](https://en.wikipedia.org/wiki/Merkle_tree)
- [Metric tree](https://en.wikipedia.org/wiki/Metric_tree)
- [Multimap](https://en.wikipedia.org/wiki/Multimap)
- [National Institute of Standards and Technology](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)
- [Natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing)
- [Needleman–Wunsch algorithm](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm)
- [Network bridge](https://en.wikipedia.org/wiki/Network_bridge)
- [Nibble](https://en.wikipedia.org/wiki/Nibble)
- [Nondeterministic finite automaton](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton)
- [Octree](https://en.wikipedia.org/wiki/Octree)
- [Optimal binary search tree](https://en.wikipedia.org/wiki/Optimal_binary_search_tree)
- [Order statistic tree](https://en.wikipedia.org/wiki/Order_statistic_tree)
- [Tree (graph theory)](https://en.wikipedia.org/wiki/Tree_(graph_theory))
- [Out-of-order execution](https://en.wikipedia.org/wiki/Out-of-order_execution)
- [Oxford University Press](https://en.wikipedia.org/wiki/Oxford_University_Press)
- [PH-tree](https://en.wikipedia.org/wiki/PH-tree)
- [PQ tree](https://en.wikipedia.org/wiki/PQ_tree)
- [Pairing heap](https://en.wikipedia.org/wiki/Pairing_heap)
- [Palindrome tree](https://en.wikipedia.org/wiki/Palindrome_tree)
- [Parallel programming model](https://en.wikipedia.org/wiki/Parallel_programming_model)
- [Parsing](https://en.wikipedia.org/wiki/Parsing)
- [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching)
- [Permutation](https://en.wikipedia.org/wiki/Permutation)
- [Predictive text](https://en.wikipedia.org/wiki/Predictive_text)
- [Prefix](https://en.wikipedia.org/wiki/Prefix)
- [Substring](https://en.wikipedia.org/wiki/Substring)
- [Prefix hash tree](https://en.wikipedia.org/wiki/Prefix_hash_tree)
- [Princeton University](https://en.wikipedia.org/wiki/Princeton_University)
- [Priority R-tree](https://en.wikipedia.org/wiki/Priority_R-tree)
- [Priority queue](https://en.wikipedia.org/wiki/Priority_queue)
- [Quadtree](https://en.wikipedia.org/wiki/Quadtree)
- [Queue (abstract data type)](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))
- [R*-tree](https://en.wikipedia.org/wiki/R*-tree)
- [R+ tree](https://en.wikipedia.org/wiki/R%2B_tree)
- [R-tree](https://en.wikipedia.org/wiki/R-tree)
- [Rabin–Karp algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm)
- [Radix sort](https://en.wikipedia.org/wiki/Radix_sort)
- [Radix sort](https://en.wikipedia.org/wiki/Radix_sort)
- [Radix tree](https://en.wikipedia.org/wiki/Radix_tree)
- [Raita algorithm](https://en.wikipedia.org/wiki/Raita_algorithm)
- [Random access](https://en.wikipedia.org/wiki/Random_access)
- [Range tree](https://en.wikipedia.org/wiki/Range_tree)
- [Recursion (computer science)](https://en.wikipedia.org/wiki/Recursion_(computer_science))
- [Red–black tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)
- [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Regular grammar](https://en.wikipedia.org/wiki/Regular_grammar)
- [Retrieval Data Structure](https://en.wikipedia.org/wiki/Retrieval_Data_Structure)
- [Robert Sedgewick (computer scientist)](https://en.wikipedia.org/wiki/Robert_Sedgewick_(computer_scientist))
- [Rope (data structure)](https://en.wikipedia.org/wiki/Rope_(data_structure))
- [Routing](https://en.wikipedia.org/wiki/Routing)
- [Rutgers University](https://en.wikipedia.org/wiki/Rutgers_University)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [SIAM Journal on Computing](https://en.wikipedia.org/wiki/SIAM_Journal_on_Computing)
- [Single instruction, multiple data](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data)
- [SPQR tree](https://en.wikipedia.org/wiki/SPQR_tree)
- [Scapegoat tree](https://en.wikipedia.org/wiki/Scapegoat_tree)
- [Search tree](https://en.wikipedia.org/wiki/Search_tree)
- [Segment tree](https://en.wikipedia.org/wiki/Segment_tree)
- [Self-balancing binary search tree](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree)
- [Semi-Thue system](https://en.wikipedia.org/wiki/Semi-Thue_system)
- [Sentinel value](https://en.wikipedia.org/wiki/Sentinel_value)
- [Sequence alignment](https://en.wikipedia.org/wiki/Sequence_alignment)
- [Sequential pattern mining](https://en.wikipedia.org/wiki/Sequential_pattern_mining)
- [Set (abstract data type)](https://en.wikipedia.org/wiki/Set_(abstract_data_type))
- [Linked list](https://en.wikipedia.org/wiki/Linked_list)
- [Skew binomial heap](https://en.wikipedia.org/wiki/Skew_binomial_heap)
- [Skew heap](https://en.wikipedia.org/wiki/Skew_heap)
- [Skip list](https://en.wikipedia.org/wiki/Skip_list)
- [Smith–Waterman algorithm](https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm)
- [Society for Industrial and Applied Mathematics](https://en.wikipedia.org/wiki/Society_for_Industrial_and_Applied_Mathematics)
- [Space complexity](https://en.wikipedia.org/wiki/Space_complexity)
- [Sparse matrix](https://en.wikipedia.org/wiki/Sparse_matrix)
- [Spatial database](https://en.wikipedia.org/wiki/Spatial_database)
- [Spell checker](https://en.wikipedia.org/wiki/Spell_checker)
- [Splay tree](https://en.wikipedia.org/wiki/Splay_tree)
- [Springer Publishing](https://en.wikipedia.org/wiki/Springer_Publishing)
- [Stack (abstract data type)](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
- [String-searching algorithm](https://en.wikipedia.org/wiki/String-searching_algorithm)
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [String metric](https://en.wikipedia.org/wiki/String_metric)
- [String operations](https://en.wikipedia.org/wiki/String_operations)
- [Subnet](https://en.wikipedia.org/wiki/Subnet)
- [Substring index](https://en.wikipedia.org/wiki/Substring_index)
- [Suffix](https://en.wikipedia.org/wiki/Suffix)
- [Suffix array](https://en.wikipedia.org/wiki/Suffix_array)
- [Suffix automaton](https://en.wikipedia.org/wiki/Suffix_automaton)
- [Suffix tree](https://en.wikipedia.org/wiki/Suffix_tree)
- [Syracuse University](https://en.wikipedia.org/wiki/Syracuse_University)
- [T-tree](https://en.wikipedia.org/wiki/T-tree)
- [Ternary search tree](https://en.wikipedia.org/wiki/Ternary_search_tree)
- [Text corpus](https://en.wikipedia.org/wiki/Text_corpus)
- [The Art of Computer Programming](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming)
- [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction)
- [Time complexity](https://en.wikipedia.org/wiki/Time_complexity)
- [Top tree](https://en.wikipedia.org/wiki/Top_tree)
- [Tray](https://en.wikipedia.org/wiki/Tray)
- [Treap](https://en.wikipedia.org/wiki/Treap)
- [Tree (abstract data type)](https://en.wikipedia.org/wiki/Tree_(abstract_data_type))
- [Tree (abstract data type)](https://en.wikipedia.org/wiki/Tree_(abstract_data_type))
- [Tree (disambiguation)](https://en.wikipedia.org/wiki/Tree_(disambiguation))
- [Tree traversal](https://en.wikipedia.org/wiki/Tree_traversal)
- [Tri](https://en.wikipedia.org/wiki/Tri)
- [Trigram search](https://en.wikipedia.org/wiki/Trigram_search)
- [Try](https://en.wikipedia.org/wiki/Try)
- [Two's complement](https://en.wikipedia.org/wiki/Two%27s_complement)
- [Two-way string-matching algorithm](https://en.wikipedia.org/wiki/Two-way_string-matching_algorithm)
- [UB-tree](https://en.wikipedia.org/wiki/UB-tree)
- [United Kingdom](https://en.wikipedia.org/wiki/United_Kingdom)
- [URL](https://en.wikipedia.org/wiki/URL)
- [United States](https://en.wikipedia.org/wiki/United_States)
- [University of Florida](https://en.wikipedia.org/wiki/University_of_Florida)
- [University of Glasgow](https://en.wikipedia.org/wiki/University_of_Glasgow)
- [University of Helsinki](https://en.wikipedia.org/wiki/University_of_Helsinki)
- [Unrolled linked list](https://en.wikipedia.org/wiki/Unrolled_linked_list)
- [Van Emde Boas tree](https://en.wikipedia.org/wiki/Van_Emde_Boas_tree)
- [Vantage-point tree](https://en.wikipedia.org/wiki/Vantage-point_tree)
- [Wagner–Fischer algorithm](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm)
- [Weak heap](https://en.wikipedia.org/wiki/Weak_heap)
- [Web indexing](https://en.wikipedia.org/wiki/Web_indexing)
- [Search engine](https://en.wikipedia.org/wiki/Search_engine)
- [Weight-balanced tree](https://en.wikipedia.org/wiki/Weight-balanced_tree)
- [Wildcard mask](https://en.wikipedia.org/wiki/Wildcard_mask)
- [X-fast trie](https://en.wikipedia.org/wiki/X-fast_trie)
- [X-tree](https://en.wikipedia.org/wiki/X-tree)
- [XOR linked list](https://en.wikipedia.org/wiki/XOR_linked_list)
- [Y-fast trie](https://en.wikipedia.org/wiki/Y-fast_trie)
- [Zhu–Takaoka string matching algorithm](https://en.wikipedia.org/wiki/Zhu%E2%80%93Takaoka_string_matching_algorithm)
- [Wikipedia:Good articles](https://en.wikipedia.org/wiki/Wikipedia:Good_articles)
- [Template:CS trees](https://en.wikipedia.org/wiki/Template:CS_trees)
- [Template:Data structures](https://en.wikipedia.org/wiki/Template:Data_structures)
- [Template:Strings](https://en.wikipedia.org/wiki/Template:Strings)
- [Template talk:CS trees](https://en.wikipedia.org/wiki/Template_talk:CS_trees)
- [Template talk:Data structures](https://en.wikipedia.org/wiki/Template_talk:Data_structures)
- [Template talk:Strings](https://en.wikipedia.org/wiki/Template_talk:Strings)
- [Help:IPA/English](https://en.wikipedia.org/wiki/Help:IPA/English)
- [Category:String sorting algorithms](https://en.wikipedia.org/wiki/Category:String_sorting_algorithms)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:52:35.422962+00:00_