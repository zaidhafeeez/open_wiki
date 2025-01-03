---
title: Burrows–Wheeler transform
url: https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Articles with example R code", "Category:Articles with example pseudocode", "Category:Articles with short description", "Category:Data compression", "Category:Data compression transforms", "Category:Lossless compression algorithms", "Category:Short description is different from Wikidata", "Category:Webarchive template wayback links"]
references: 0
last_modified: 2024-12-19T13:42:16Z
---

# Burrows–Wheeler transform

## Summary

The Burrows–Wheeler transform (BWT, also called block-sorting compression) rearranges a character string into runs of similar characters. This is useful for compression, since it tends to be easy to compress a string that has runs of repeated characters by techniques such as move-to-front transform and run-length encoding.  More importantly, the transformation is reversible, without needing to store any additional data except the position of the first original character. The BWT is thus a "free"

## Full Content

The Burrows–Wheeler transform (BWT, also called block-sorting compression) rearranges a character string into runs of similar characters. This is useful for compression, since it tends to be easy to compress a string that has runs of repeated characters by techniques such as move-to-front transform and run-length encoding.  More importantly, the transformation is reversible, without needing to store any additional data except the position of the first original character. The BWT is thus a "free" method of improving the efficiency of text compression algorithms, costing only some extra computation. The Burrows–Wheeler transform is an algorithm used to prepare data for use with data compression techniques such as bzip2. It was invented by Michael Burrows and David Wheeler in 1994 while Burrows was working at DEC Systems Research Center in Palo Alto, California. It is based on a previously unpublished transformation discovered by Wheeler in 1983. The  algorithm can be implemented efficiently using a suffix array thus reaching linear time complexity.

Description
When a character string is transformed by the BWT, the transformation permutes the order of the characters. If the original string had several substrings that occurred often, then the transformed string will have several places where a single character is repeated multiple times in a row.
For example:

The output is easier to compress because it has many repeated characters.
In this example the transformed string contains six runs of identical characters:
XX,
SS,
PP,
..,
II,
and
III, which together make 13 out of the 44 characters.

Example
The transform is done by sorting all the circular shifts of a text in lexicographic order and by extracting the last column and the index of the original string in the set of sorted permutations of S.
Given an input string S = ^BANANA$ (step 1 in the table below), rotate it N times (step 2), where N = 8 is the length of the S string considering also the red ^ character representing the start of the string and the red $ character representing the 'EOF' pointer; these rotations, or circular shifts, are then sorted lexicographically (step 3). The output of the encoding phase is the last column L = BNN^AA$A after step 3, and the index (0-based) I of the row containing the original string S, in this case I = 6.
It is not necessary to use both $ and ^, but at least one must be used, else we cannot invert the transform, since all circular permutations of a string have the same Burrows–Wheeler transform.

The following pseudocode gives a simple (though inefficient) way to calculate the BWT and its inverse.  It assumes that the input string s contains a special character 'EOF' which is the last character and occurs nowhere else in the text.

function BWT (string s)
    create a table, where the rows are all possible rotations of s
    sort rows alphabetically
    return (last column of the table)

function inverseBWT (string s)
    create empty table
    repeat length(s) times
        // first insert creates first column
        insert s as a column of table before first column of the table
        sort rows of the table alphabetically
    return (row that ends with the 'EOF' character)

Explanation
To understand why this creates more-easily-compressible data, consider transforming a long English text frequently containing the word "the". Sorting the rotations of this text will group rotations starting with "he " together, and the last character of that rotation (which is also the character before the "he ") will usually be "t", so the result of the transform would contain a number of "t" characters along with the perhaps less-common exceptions (such as if it contains "ache ") mixed in. So it can be seen that the success of this transform depends upon one value having a high probability of occurring before a sequence, so that in general it needs fairly long samples (a few kilobytes at least) of appropriate data (such as text).
The remarkable thing about the BWT is not that it generates a more easily encoded output—an ordinary sort would do that—but that it does this reversibly, allowing the original document to be re-generated from the last column data.
The inverse can be understood this way. Take the final table in the BWT algorithm, and erase all but the last column. Given only this information, you can easily reconstruct the first column. The last column tells you all the characters in the text, so just sort these characters alphabetically to get the first column. Then, the last and first columns (of each row) together give you all pairs of successive characters in the document, where pairs are taken cyclically so that the last and first character form a pair. Sorting the list of pairs gives the first and second columns. Continuing in this manner, you can reconstruct the entire list. Then, the row with the "end of file" character at the end is the original text. Reversing the example above is done like this:

Optimization
A number of optimizations can make these algorithms run more efficiently without changing the output. There is no need to represent the table in either the encoder or decoder. In the encoder, each row of the table can be represented by a single pointer into the strings, and the sort performed using the indices. In the decoder, there is also no need to store the table, and in fact no sort is needed at all. In time proportional to the alphabet size and string length, the decoded string may be generated one character at a time from right to left. A "character" in the algorithm can be a byte, or a bit, or any other convenient size.
One may also make the observation that mathematically, the encoded string can be computed as a simple modification of the suffix array, and suffix arrays can be computed with linear time and memory. The BWT can be defined with regards to the suffix array SA of text T as (1-based indexing):

  
    
      
        B
        W
        T
        [
        i
        ]
        =
        
          
            {
            
              
                
                  T
                  [
                  S
                  A
                  [
                  i
                  ]
                  −
                  1
                  ]
                  ,
                
                
                  
                    if 
                  
                  S
                  A
                  [
                  i
                  ]
                  >
                  0
                
              
              
                
                  $
                  ,
                
                
                  
                    otherwise
                  
                
              
            
            
          
        
      
    
    {\displaystyle BWT[i]={\begin{cases}T[SA[i]-1],&{\text{if }}SA[i]>0\\\$,&{\text{otherwise}}\end{cases}}}
  

There is no need to have an actual 'EOF' character. Instead, a pointer can be used that remembers where in a string the 'EOF' would be if it existed. In this approach, the output of the BWT must include both the transformed string, and the final value of the pointer. The inverse transform then shrinks it back down to the original size: it is given a string and a pointer, and returns just a string.
A complete description of the algorithms can be found in Burrows and Wheeler's paper, or in a number of online sources. The algorithms vary somewhat by whether EOF is used, and in which direction the sorting was done. In fact, the original formulation did not use an EOF marker.

Bijective variant
Since any rotation of the input string will lead to the same transformed string, the BWT cannot be inverted without adding an EOF marker to the end of the input or doing something equivalent, making it possible to distinguish the input string from all its rotations.  Increasing the size of the alphabet (by appending the EOF character) makes later compression steps awkward.
There is a bijective version of the transform, by which the transformed string uniquely identifies the original, and the two have the same length and contain exactly the same characters, just in a different order.
The bijective transform is computed by factoring the input into a non-increasing sequence of Lyndon words; such a factorization exists and is unique by the Chen–Fox–Lyndon theorem, and may be found in linear time and constant space. The algorithm sorts the rotations of all the words; as in the Burrows–Wheeler transform, this produces a sorted sequence of n strings. The transformed string is then obtained by picking the final character of each string in this sorted list.  The one important caveat here is that strings of different lengths are not ordered in the usual way; the two strings are repeated forever, and the infinite repeats are sorted.  For example, "ORO" precedes "OR" because "OROORO..." precedes "OROROR...".
For example, the text "^BANANA$" is transformed into "ANNBAA^$" through these steps (the red $ character indicates the EOF pointer) in the original string. The EOF character is unneeded in the bijective transform, so it is dropped during the transform and re-added to its proper place in the file.
The string is broken into Lyndon words so the words in the sequence are decreasing using the comparison method above. (Note that we're sorting '^' as succeeding other characters.)  "^BANANA" becomes (^) (B) (AN) (AN) (A).

Up until the last step, the process is identical to the inverse Burrows–Wheeler process, but here it will not necessarily give rotations of a single sequence; it instead gives rotations of Lyndon words (which will start to repeat as the process is continued).  Here, we can see (repetitions of) four distinct Lyndon words: (A), (AN) (twice), (B), and (^).  (NANA... doesn't represent a distinct word, as it is a cycle of ANAN....)
At this point, these words are sorted into reverse order: (^), (B), (AN), (AN), (A).  These are then concatenated to get

^BANANA
The Burrows–Wheeler transform can indeed be viewed as a special case of this bijective transform; instead of the traditional introduction of a new letter from outside our alphabet to denote the end of the string, we can introduce a new letter that compares as preceding all existing letters that is put at the beginning of the string.  The whole string is now a Lyndon word, and running it through the bijective process will therefore result in a transformed result that, when inverted, gives back the Lyndon word, with no need for reassembling at the end.
Relatedly, the transformed text will only differ from the result of BWT by one character per Lyndon word; for example, if the input is decomposed into six Lyndon words, the output will only differ in six characters.
For example, applying the bijective transform gives:

The bijective transform includes eight runs of identical
characters. These runs are, in order: XX,
II,
XX,
PP,
..,
EE,
..,
and
IIII.
In total, 18 characters are used in these runs.

Dynamic Burrows–Wheeler transform
When a text is edited, its Burrows–Wheeler transform will change. Salson et al. propose an algorithm that deduces the Burrows–Wheeler transform of an edited text from that of the original text, doing a limited number of local reorderings in the original Burrows–Wheeler transform, which can be faster than constructing the Burrows–Wheeler transform of the edited text directly.

Sample implementation
This Python implementation sacrifices speed for simplicity: the program is short, but takes more than the linear time that would be desired in a practical implementation. It essentially does what the pseudocode section does.
Using the STX/ETX control codes to mark the start and end of the text, and using s[i:] + s[:i] to construct the ith rotation of s, the forward transform takes the last character of each of the sorted rows:

The inverse transform repeatedly inserts r as the left column of the table and sorts the table.  After the whole table is built, it returns the row that ends with ETX, minus the STX and ETX.

Following implementation notes from Manzini, it is equivalent to use a simple null character suffix instead. The sorting should be done in colexicographic order (string read right-to-left), i.e. sorted(..., key=lambda s: s[::-1]) in Python. (The above control codes actually fail to satisfy EOF being the last character; the two codes are actually the first. The rotation holds nevertheless.)

BWT applications
As a lossless compression algorithm the Burrows–Wheeler transform offers the important quality that its encoding is reversible and hence the original data may be recovered from the resulting compression. The lossless quality of Burrows algorithm has provided for different algorithms with different purposes in mind. To name a few, Burrows–Wheeler transform is used in algorithms for sequence alignment, image compression, data compression, etc. The following is a compilation of some uses given to the Burrows–Wheeler Transform.

BWT for sequence alignment
The advent of next-generation sequencing (NGS) techniques at the end of the 2000s decade has led to another application of the Burrows–Wheeler transformation. In NGS, DNA is fragmented into small pieces, of which the first few bases are sequenced, yielding several millions of "reads", each 30 to 500 base pairs ("DNA characters") long. In many experiments, e.g., in ChIP-Seq, the task is now to align these reads to a reference genome, i.e., to the known, nearly complete sequence of the organism in question (which may be up to several billion base pairs long). A number of alignment programs, specialized for this task, were published, which initially relied on hashing (e.g., Eland, SOAP, or Maq). In an effort to reduce the memory requirement for sequence alignment, several alignment programs were developed (Bowtie, BWA, and SOAP2) that use the Burrows–Wheeler transform.

BWT for image compression
The Burrows–Wheeler transformation has proved to be fundamental for image compression applications. For example, Showed a compression pipeline based on the application of the Burrows–Wheeler transformation followed by inversion, run-length, and arithmetic encoders. The pipeline developed in this case is known as Burrows–Wheeler transform with an inversion encoder (BWIC). The results shown by BWIC are shown to outperform the compression performance of well-known and widely used algorithms like Lossless JPEG and JPEG 2000. BWIC is shown to outperform those in terms of final compression size of radiography medical images on the order of 5.1% and 4.1% respectively. The improvements are achieved by combining BWIC and a pre-BWIC scan of the image in a vertical snake order fashion. More recently, additional works like that of  have shown the implementation of the Burrows–Wheeler Transform in conjunction with the known move-to-front transform (MTF) achieve near lossless compression of images.

BWT for compression of genomic databases
Cox et al. presented a genomic compression scheme that uses BWT as the algorithm applied during the first stage of compression of several genomic datasets including the human genomic information. Their work proposed that BWT compression could be enhanced by including a second stage compression mechanism called same-as-previous encoding ("SAP"), which makes use of the fact that suffixes of two or more prefix letters could be equal. With the compression mechanism BWT-SAP, Cox et al. showed that in the genomic database ERA015743, 135.5 GB in size, the compression scheme BWT-SAP compresses the ERA015743 dataset by around 94%, to 8.2 GB.

BWT for sequence prediction
BWT has also been proved to be useful on sequence prediction which is a common area of study in machine learning and natural-language processing. In particular, Ktistakis et al. proposed a sequence prediction scheme called SuBSeq that exploits the lossless compression of data of the Burrows–Wheeler transform. SuBSeq exploits BWT by extracting the FM-index and then performing a series of operations called backwardSearch, forwardSearch, neighbourExpansion, and getConsequents in order to search for predictions given a suffix. The predictions are then classified based on a weight and put into an array from which the element with the highest weight is given as the prediction from the SuBSeq algorithm. SuBSeq has been shown to outperform state of the art algorithms for sequence prediction both in terms of training time and accuracy.

References
External links
Article by Mark Nelson on the BWT Archived 2017-03-25 at the Wayback Machine
A Bijective String-Sorting Transform, by Gil and Scott Archived 2011-10-08 at the Wayback Machine
Yuta's openbwt-v1.5.zip contains source code for various BWT routines including BWTS for bijective version
On Bijective Variants of the Burrows–Wheeler Transform, by Kufleitner
Blog post and project page for an open-source compression program and library based on the Burrows–Wheeler algorithm
MIT open courseware lecture on BWT (Foundations of Computational and Systems Biology)
League Table Sort (LTS) or The Weighting algorithm to BWT by Abderrahim Hechachena
