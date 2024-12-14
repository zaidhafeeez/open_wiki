# Ruzzo–Tompa algorithm

## Article Metadata

- **Last Updated:** 2024-12-14T19:44:14.106821+00:00
- **Original Article:** [Ruzzo–Tompa algorithm](https://en.wikipedia.org/wiki/Ruzzo%E2%80%93Tompa_algorithm)
- **Language:** en
- **Page ID:** 57141126

## Summary

The Ruzzo–Tompa algorithm or the RT algorithm is a linear-time algorithm for finding all non-overlapping, contiguous, maximal scoring subsequences in a sequence of real numbers. The Ruzzo–Tompa algorithm was proposed by Walter L. Ruzzo and Martin Tompa. This algorithm is an improvement over previously known quadratic time algorithms. The maximum scoring subsequence from the set produced by the algorithm is also a solution to the maximum subarray problem.
The Ruzzo–Tompa algorithm has application

## Categories

- Category:Articles with example Python (programming language) code
- Category:Dynamic programming
- Category:Optimization algorithms and methods

## Table of Contents

- Applications
- Problem definition
- Other algorithms
- Algorithm
- See also
- References
- Further reading

## Content

The Ruzzo–Tompa algorithm or the RT algorithm is a linear-time algorithm for finding all non-overlapping, contiguous, maximal scoring subsequences in a sequence of real numbers. The Ruzzo–Tompa algorithm was proposed by Walter L. Ruzzo and Martin Tompa. This algorithm is an improvement over previously known quadratic time algorithms. The maximum scoring subsequence from the set produced by the algorithm is also a solution to the maximum subarray problem.
The Ruzzo–Tompa algorithm has applications in bioinformatics, web scraping, and information retrieval.

Applications
Bioinformatics
The Ruzzo–Tompa algorithm has been used in Bioinformatics tools to study biological data. The problem of finding disjoint maximal subsequences is of practical importance in the analysis of DNA. Maximal subsequences algorithms have been used in the identification of transmembrane segments and the evaluation of sequence homology.
The algorithm is used in sequence alignment which is used as a method of identifying similar DNA, RNA, or protein sequences. Accounting for the ordering of pairs of high-scoring subsequences in two sequences creates better sequence alignments. This is because the biological model suggests that separate high-scoring subsequence pairs arise from insertions or deletions within a matching region. Requiring consistent ordering of high-scoring subsequence pairs increases their statistical significance.

Web scraping
The Ruzzo–Tompa algorithm is used in Web scraping to extract information from web pages. Pasternack and Roth proposed a method for extracting important blocks of text from HTML documents. The web pages are first tokenized and the score for each token is found using local, token-level classifiers. A modified version of the Ruzzo–Tompa algorithm is then used to find the k highest-valued subsequences of tokens. These subsequences are then used as predictions of important blocks of text in the article.

Information retrieval
The Ruzzo–Tompa algorithm has been used in Information retrieval search algorithms. Liang et al. proposed a data fusion method to combine the search results of several microblog search algorithms. In their method, the Ruzzo–Tompa algorithm is used to detect bursts of information.

Problem definition
The problem of finding all maximal subsequences is defined as follows: Given a list of real numbered scores 
  
    
      
        
          x
          
            1
          
        
        ,
        
          x
          
            2
          
        
        ,
        …
        ,
        
          x
          
            n
          
        
      
    
    {\displaystyle x_{1},x_{2},\ldots ,x_{n}}
  
, find the list of contiguous subsequences that gives the greatest total score, where the score of each subsequence 
  
    
      
        
          S
          
            i
            ,
            j
          
        
        =
        
          ∑
          
            i
            ≤
            k
            ≤
            j
          
        
        
          x
          
            k
          
        
      
    
    {\displaystyle S_{i,j}=\sum _{i\leq k\leq j}x_{k}}
  
. The subsequences must be disjoint (non-overlapping) and have a positive score.

Other algorithms
There are several approaches to solving the all maximal scoring subsequences problem. A natural approach is to use existing, linear time algorithms to find the maximum subsequence (see maximum subarray problem) and then recursively find the maximal subsequences to the left and right of the maximum subsequence. The analysis of this algorithm is similar to that of Quicksort: The maximum subsequence could be small in comparison to the rest of sequence, leading to a running time of 
  
    
      
        O
        (
        
          n
          
            2
          
        
        )
      
    
    {\displaystyle O(n^{2})}
  
 in the worst case.

Algorithm
The standard implementation of the Ruzzo–Tompa algorithm runs in 
  
    
      
        O
        (
        n
        )
      
    
    {\displaystyle O(n)}
  
 time and uses O(n) space, where n is the length of the list of scores. The algorithm uses dynamic programming to progressively build the final solution by incrementally solving progressively larger subsets of the problem. The description of the algorithm provided by Ruzzo and Tompa is as follows:

Read the scores left to right and maintain the cumulative sum of the scores read. Maintain an ordered list 
  
    
      
        
          I
          
            1
          
        
        ,
        
          I
          
            2
          
        
        ,
        …
        ,
        
          I
          
            j
          
        
      
    
    {\displaystyle I_{1},I_{2},\ldots ,I_{j}}
  
 of disjoint subsequences. For each subsequence 
  
    
      
        
          I
          
            j
          
        
      
    
    {\displaystyle I_{j}}
  
, record the cumulative total 
  
    
      
        
          L
          
            j
          
        
      
    
    {\displaystyle L_{j}}
  
 of all scores up to but not including the leftmost score of 
  
    
      
        
          I
          
            j
          
        
      
    
    {\displaystyle I_{j}}
  
, and the total 
  
    
      
        
          R
          
            j
          
        
      
    
    {\displaystyle R_{j}}
  
 up to and including the rightmost score of 
  
    
      
        
          I
          
            j
          
        
      
    
    {\displaystyle I_{j}}
  
.
The lists are initially empty. Scores are read from left to right and are processed as follows. Nonpositive scores require no special processing, so the next score is read. A positive score is incorporated into a new sub-sequence 
  
    
      
        
          I
          
            k
          
        
      
    
    {\displaystyle I_{k}}
  
 of length one that is then integrated into the list by the following process:
The list 
  
    
      
        I
      
    
    {\displaystyle I}
  
 is searched from right to left for the maximum value of 
  
    
      
        j
      
    
    {\displaystyle j}
  
 satisfying 
  
    
      
        
          L
          
            j
          
        
        <
        
          L
          
            k
          
        
      
    
    {\displaystyle L_{j}<L_{k}}
  

If there is no such 
  
    
      
        j
      
    
    {\displaystyle j}
  
, then add 
  
    
      
        
          I
          
            k
          
        
      
    
    {\displaystyle I_{k}}
  
 to the end of the list.
If there is such a 
  
    
      
        j
      
    
    {\displaystyle j}
  
, and 
  
    
      
        
          R
          
            j
          
        
        ≥
        
          R
          
            k
          
        
      
    
    {\displaystyle R_{j}\geq R_{k}}
  
, then add 
  
    
      
        
          I
          
            k
          
        
      
    
    {\displaystyle I_{k}}
  
 to the end of the list.
Otherwise (i.e., there is such a j, but 
  
    
      
        
          R
          
            j
          
        
        <
        
          R
          
            k
          
        
      
    
    {\displaystyle R_{j}<R_{k}}
  
), extend the subsequence 
  
    
      
        
          I
          
            k
          
        
      
    
    {\displaystyle I_{k}}
  
 to the left to encompass everything up to and including the leftmost score in 
  
    
      
        
          I
          
            j
          
        
      
    
    {\displaystyle I_{j}}
  
. Delete subsequences 
  
    
      
        
          I
          
            j
          
        
        ,
        
          I
          
            j
          
        
        +
        1
        ,
        …
        ,
        
          I
          
            k
          
        
        −
        1
      
    
    {\displaystyle I_{j},I_{j}+1,\ldots ,I_{k}-1}
  
 from the list, and append 
  
    
      
        
          I
          
            k
          
        
      
    
    {\displaystyle I_{k}}
  
 to the end of the list. Reconsider the newly extended subsequence 
  
    
      
        
          I
          
            k
          
        
      
    
    {\displaystyle I_{k}}
  
 (now renumbered 
  
    
      
        
          I
          
            j
          
        
      
    
    {\displaystyle I_{j}}
  
) as in step 1.
Once the end of the input is reached, all subsequences remaining on the list 
  
    
      
        I
      
    
    {\displaystyle I}
  
 are maximal.
The following Python code implements the Ruzzo–Tompa algorithm:

See also
Maximum subarray problem
Quicksort

References
Further reading
Ali, Syed Arslan; Raza, Basit; Malik, Ahmad Kamran; Shahid, Ahmad Raza; Faheem, Muhammad; Alquhayz, Hani; Kumar, Yogan Jaya (2020). "An Optimally Configured and Improved Deep Belief Network (OCI-DBN) Approach for Heart Disease Prediction Based on Ruzzo–Tompa and Stacked Genetic Algorithm". IEEE Access. 8. Institute of Electrical and Electronics Engineers (IEEE): 65947–65958. doi:10.1109/access.2020.2985646. ISSN 2169-3536. S2CID 215817246.

## Related Articles

### Internal Links

- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Bioinformatics](https://en.wikipedia.org/wiki/Bioinformatics)
- [Bursting](https://en.wikipedia.org/wiki/Bursting)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [DNA](https://en.wikipedia.org/wiki/DNA)
- [Data fusion](https://en.wikipedia.org/wiki/Data_fusion)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Information retrieval](https://en.wikipedia.org/wiki/Information_retrieval)
- [Lexical analysis](https://en.wikipedia.org/wiki/Lexical_analysis)
- [Maximum subarray problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
- [PubMed Central](https://en.wikipedia.org/wiki/PubMed_Central)
- [PubMed](https://en.wikipedia.org/wiki/PubMed)
- [Protein](https://en.wikipedia.org/wiki/Protein)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quicksort](https://en.wikipedia.org/wiki/Quicksort)
- [RNA](https://en.wikipedia.org/wiki/RNA)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Sequence alignment](https://en.wikipedia.org/wiki/Sequence_alignment)
- [Sequence homology](https://en.wikipedia.org/wiki/Sequence_homology)
- [Time complexity](https://en.wikipedia.org/wiki/Time_complexity)
- [Web scraping](https://en.wikipedia.org/wiki/Web_scraping)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:44:14.106821+00:00_