---
title: Trie
url: https://en.wikipedia.org/wiki/Trie
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Commons category link from Wikidata", "Category:Finite automata", "Category:Good articles", "Category:Short description is different from Wikidata", "Category:Trees (data structures)"]
references: 0
last_modified: 2024-12-19T13:42:13Z
---

# Trie

## Summary

In computer science, a trie (, ), also known as a digital tree or prefix tree, is a specialized search tree data structure used to store and retrieve strings from a dictionary or set. Unlike a binary search tree, nodes in a trie do not store their associated key. Instead, each node's position within the trie determines its associated key, with the connections between nodes defined by individual characters rather than the entire key.
Tries are particularly effective for tasks such as autocomplete

## Full Content

In computer science, a trie (, ), also known as a digital tree or prefix tree, is a specialized search tree data structure used to store and retrieve strings from a dictionary or set. Unlike a binary search tree, nodes in a trie do not store their associated key. Instead, each node's position within the trie determines its associated key, with the connections between nodes defined by individual characters rather than the entire key.
Tries are particularly effective for tasks such as autocomplete, spell checking, and IP routing, offering advantages over hash tables due to their prefix-based organization and lack of hash collisions. Every child node shares a common prefix with its parent node, and the root node represents the empty string. While basic trie implementations can be memory-intensive, various optimization techniques such as compression and bitwise representations have been developed to improve their efficiency. A notable optimization is the radix tree, which provides more efficient prefix-based storage.
While tries commonly store character strings, they can be adapted to work with any ordered sequence of elements, such as permutations of digits or shapes. A notable variant is the bitwise trie, which uses individual bits from fixed-length binary data (such as integers or memory addresses) as keys.

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
