# Burrows–Wheeler transform

## Article Metadata

- **Last Updated:** 2024-12-14T19:34:14.715321+00:00
- **Original Article:** [Burrows–Wheeler transform](https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform)
- **Language:** en
- **Page ID:** 36777

## Summary

The Burrows–Wheeler transform (BWT, also called block-sorting compression) rearranges a character string into runs of similar characters. This is useful for compression, since it tends to be easy to compress a string that has runs of repeated characters by techniques such as move-to-front transform and run-length encoding.  More importantly, the transformation is reversible, without needing to store any additional data except the position of the first original character. The BWT is thus a "free"

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with example pseudocode
- Category:Articles with short description
- Category:Data compression
- Category:Data compression transforms
- Category:Lossless compression algorithms
- Category:Short description is different from Wikidata
- Category:Webarchive template wayback links

## Table of Contents

- Description
- Example
- Explanation
- Optimization
- Bijective variant
- Dynamic Burrows–Wheeler transform
- Sample implementation
- BWT applications
- References
- External links

## Content

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

## Related Articles

### Internal Links

- [842 (compression algorithm)](https://en.wikipedia.org/wiki/842_(compression_algorithm))
- [A-law algorithm](https://en.wikipedia.org/wiki/A-law_algorithm)
- [Adaptive Huffman coding](https://en.wikipedia.org/wiki/Adaptive_Huffman_coding)
- [Adaptive coding](https://en.wikipedia.org/wiki/Adaptive_coding)
- [Adaptive differential pulse-code modulation](https://en.wikipedia.org/wiki/Adaptive_differential_pulse-code_modulation)
- [Algebraic code-excited linear prediction](https://en.wikipedia.org/wiki/Algebraic_code-excited_linear_prediction)
- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Arithmetic coding](https://en.wikipedia.org/wiki/Arithmetic_coding)
- [Asymmetric numeral systems](https://en.wikipedia.org/wiki/Asymmetric_numeral_systems)
- [Audio codec](https://en.wikipedia.org/wiki/Audio_codec)
- [Average bitrate](https://en.wikipedia.org/wiki/Average_bitrate)
- [Base pair](https://en.wikipedia.org/wiki/Base_pair)
- [Best, worst and average case](https://en.wikipedia.org/wiki/Best,_worst_and_average_case)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Bijection](https://en.wikipedia.org/wiki/Bijection)
- [Bit rate](https://en.wikipedia.org/wiki/Bit_rate)
- [Bowtie (sequence analysis)](https://en.wikipedia.org/wiki/Bowtie_(sequence_analysis))
- [Brotli](https://en.wikipedia.org/wiki/Brotli)
- [Byte pair encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding)
- [Bzip2](https://en.wikipedia.org/wiki/Bzip2)
- [C0 and C1 control codes](https://en.wikipedia.org/wiki/C0_and_C1_control_codes)
- [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press)
- [Canonical Huffman code](https://en.wikipedia.org/wiki/Canonical_Huffman_code)
- [ChIP sequencing](https://en.wikipedia.org/wiki/ChIP_sequencing)
- [Chain code](https://en.wikipedia.org/wiki/Chain_code)
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [Monoid factorisation](https://en.wikipedia.org/wiki/Monoid_factorisation)
- [Chroma subsampling](https://en.wikipedia.org/wiki/Chroma_subsampling)
- [Circular shift](https://en.wikipedia.org/wiki/Circular_shift)
- [Code-excited linear prediction](https://en.wikipedia.org/wiki/Code-excited_linear_prediction)
- [Coding tree unit](https://en.wikipedia.org/wiki/Coding_tree_unit)
- [Lexicographic order](https://en.wikipedia.org/wiki/Lexicographic_order)
- [Color space](https://en.wikipedia.org/wiki/Color_space)
- [Companding](https://en.wikipedia.org/wiki/Companding)
- [Compressed data structure](https://en.wikipedia.org/wiki/Compressed_data_structure)
- [Compressed suffix array](https://en.wikipedia.org/wiki/Compressed_suffix_array)
- [Compression artifact](https://en.wikipedia.org/wiki/Compression_artifact)
- [Constant bitrate](https://en.wikipedia.org/wiki/Constant_bitrate)
- [Context mixing](https://en.wikipedia.org/wiki/Context_mixing)
- [Context tree weighting](https://en.wikipedia.org/wiki/Context_tree_weighting)
- [Convolution](https://en.wikipedia.org/wiki/Convolution)
- [DEC Systems Research Center](https://en.wikipedia.org/wiki/DEC_Systems_Research_Center)
- [DNA](https://en.wikipedia.org/wiki/DNA)
- [DNA sequencing](https://en.wikipedia.org/wiki/DNA_sequencing)
- [Data compression](https://en.wikipedia.org/wiki/Data_compression)
- [Data compression symmetry](https://en.wikipedia.org/wiki/Data_compression_symmetry)
- [Daubechies wavelet](https://en.wikipedia.org/wiki/Daubechies_wavelet)
- [David Wheeler (computer scientist)](https://en.wikipedia.org/wiki/David_Wheeler_(computer_scientist))
- [David Wheeler (computer scientist)](https://en.wikipedia.org/wiki/David_Wheeler_(computer_scientist))
- [Deblocking filter](https://en.wikipedia.org/wiki/Deblocking_filter)
- [Deflate](https://en.wikipedia.org/wiki/Deflate)
- [Delta encoding](https://en.wikipedia.org/wiki/Delta_encoding)
- [Delta modulation](https://en.wikipedia.org/wiki/Delta_modulation)
- [Dictionary coder](https://en.wikipedia.org/wiki/Dictionary_coder)
- [Differential pulse-code modulation](https://en.wikipedia.org/wiki/Differential_pulse-code_modulation)
- [Discrete cosine transform](https://en.wikipedia.org/wiki/Discrete_cosine_transform)
- [Discrete sine transform](https://en.wikipedia.org/wiki/Discrete_sine_transform)
- [Discrete wavelet transform](https://en.wikipedia.org/wiki/Discrete_wavelet_transform)
- [Display resolution](https://en.wikipedia.org/wiki/Display_resolution)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Dynamic Markov compression](https://en.wikipedia.org/wiki/Dynamic_Markov_compression)
- [Dynamic range](https://en.wikipedia.org/wiki/Dynamic_range)
- [Elias gamma coding](https://en.wikipedia.org/wiki/Elias_gamma_coding)
- [Embedded zerotrees of wavelet transforms](https://en.wikipedia.org/wiki/Embedded_zerotrees_of_wavelet_transforms)
- [End-of-file](https://en.wikipedia.org/wiki/End-of-file)
- [Entropy (information theory)](https://en.wikipedia.org/wiki/Entropy_(information_theory))
- [Entropy coding](https://en.wikipedia.org/wiki/Entropy_coding)
- [Exponential-Golomb coding](https://en.wikipedia.org/wiki/Exponential-Golomb_coding)
- [FM-index](https://en.wikipedia.org/wiki/FM-index)
- [Fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform)
- [Fibonacci coding](https://en.wikipedia.org/wiki/Fibonacci_coding)
- [Film frame](https://en.wikipedia.org/wiki/Film_frame)
- [Fourier transform](https://en.wikipedia.org/wiki/Fourier_transform)
- [Fractal compression](https://en.wikipedia.org/wiki/Fractal_compression)
- [Frame rate](https://en.wikipedia.org/wiki/Frame_rate)
- [Genome](https://en.wikipedia.org/wiki/Genome)
- [Golomb coding](https://en.wikipedia.org/wiki/Golomb_coding)
- [Grammar-based code](https://en.wikipedia.org/wiki/Grammar-based_code)
- [Hash function](https://en.wikipedia.org/wiki/Hash_function)
- [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding)
- [Hutter Prize](https://en.wikipedia.org/wiki/Hutter_Prize)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Image compression](https://en.wikipedia.org/wiki/Image_compression)
- [Image resolution](https://en.wikipedia.org/wiki/Image_resolution)
- [Incremental encoding](https://en.wikipedia.org/wiki/Incremental_encoding)
- [Information theory](https://en.wikipedia.org/wiki/Information_theory)
- [Interlaced video](https://en.wikipedia.org/wiki/Interlaced_video)
- [JPEG 2000](https://en.wikipedia.org/wiki/JPEG_2000)
- [Kosambi–Karhunen–Loève theorem](https://en.wikipedia.org/wiki/Kosambi%E2%80%93Karhunen%E2%80%93Lo%C3%A8ve_theorem)
- [Kolmogorov complexity](https://en.wikipedia.org/wiki/Kolmogorov_complexity)
- [LHA (file format)](https://en.wikipedia.org/wiki/LHA_(file_format))
- [LZ4 (compression algorithm)](https://en.wikipedia.org/wiki/LZ4_(compression_algorithm))
- [LZ77 and LZ78](https://en.wikipedia.org/wiki/LZ77_and_LZ78)
- [LZFSE](https://en.wikipedia.org/wiki/LZFSE)
- [Jeff Bonwick](https://en.wikipedia.org/wiki/Jeff_Bonwick)
- [LZRW](https://en.wikipedia.org/wiki/LZRW)
- [LZWL](https://en.wikipedia.org/wiki/LZWL)
- [LZX](https://en.wikipedia.org/wiki/LZX)
- [Lapped transform](https://en.wikipedia.org/wiki/Lapped_transform)
- [Latency (audio)](https://en.wikipedia.org/wiki/Latency_(audio))
- [Lempel–Ziv–Markov chain algorithm](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm)
- [Lempel–Ziv–Oberhumer](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Oberhumer)
- [Lempel–Ziv–Stac](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Stac)
- [Lempel–Ziv–Storer–Szymanski](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Storer%E2%80%93Szymanski)
- [Lempel–Ziv–Welch](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch)
- [Levenshtein coding](https://en.wikipedia.org/wiki/Levenshtein_coding)
- [Lexicographic order](https://en.wikipedia.org/wiki/Lexicographic_order)
- [Line spectral pairs](https://en.wikipedia.org/wiki/Line_spectral_pairs)
- [Linear predictive coding](https://en.wikipedia.org/wiki/Linear_predictive_coding)
- [Log area ratio](https://en.wikipedia.org/wiki/Log_area_ratio)
- [Lossless JPEG](https://en.wikipedia.org/wiki/Lossless_JPEG)
- [Lossless compression](https://en.wikipedia.org/wiki/Lossless_compression)
- [Lossy compression](https://en.wikipedia.org/wiki/Lossy_compression)
- [Lyndon word](https://en.wikipedia.org/wiki/Lyndon_word)
- [M. Lothaire](https://en.wikipedia.org/wiki/M._Lothaire)
- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
- [Macroblock](https://en.wikipedia.org/wiki/Macroblock)
- [MAQ](https://en.wikipedia.org/wiki/MAQ)
- [Mark Adler](https://en.wikipedia.org/wiki/Mark_Adler)
- [Michael Burrows](https://en.wikipedia.org/wiki/Michael_Burrows)
- [Modified Huffman coding](https://en.wikipedia.org/wiki/Modified_Huffman_coding)
- [Modified discrete cosine transform](https://en.wikipedia.org/wiki/Modified_discrete_cosine_transform)
- [Motion compensation](https://en.wikipedia.org/wiki/Motion_compensation)
- [Motion estimation](https://en.wikipedia.org/wiki/Motion_estimation)
- [Motion estimation](https://en.wikipedia.org/wiki/Motion_estimation)
- [Move-to-front transform](https://en.wikipedia.org/wiki/Move-to-front_transform)
- [Natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing)
- [Massive parallel sequencing](https://en.wikipedia.org/wiki/Massive_parallel_sequencing)
- [Null character](https://en.wikipedia.org/wiki/Null_character)
- [Nyquist–Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem)
- [Program optimization](https://en.wikipedia.org/wiki/Program_optimization)
- [PAQ](https://en.wikipedia.org/wiki/PAQ)
- [PubMed Central](https://en.wikipedia.org/wiki/PubMed_Central)
- [PubMed](https://en.wikipedia.org/wiki/PubMed)
- [Palo Alto, California](https://en.wikipedia.org/wiki/Palo_Alto,_California)
- [Peak signal-to-noise ratio](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio)
- [Permutation](https://en.wikipedia.org/wiki/Permutation)
- [Pixel](https://en.wikipedia.org/wiki/Pixel)
- [Prediction by partial matching](https://en.wikipedia.org/wiki/Prediction_by_partial_matching)
- [Prefix code](https://en.wikipedia.org/wiki/Prefix_code)
- [Pseudocode](https://en.wikipedia.org/wiki/Pseudocode)
- [Psychoacoustics](https://en.wikipedia.org/wiki/Psychoacoustics)
- [Pyramid (image processing)](https://en.wikipedia.org/wiki/Pyramid_(image_processing))
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quantization (image processing)](https://en.wikipedia.org/wiki/Quantization_(image_processing))
- [Quantization (signal processing)](https://en.wikipedia.org/wiki/Quantization_(signal_processing))
- [Range coding](https://en.wikipedia.org/wiki/Range_coding)
- [Rate–distortion theory](https://en.wikipedia.org/wiki/Rate%E2%80%93distortion_theory)
- [Re-Pair](https://en.wikipedia.org/wiki/Re-Pair)
- [Redundancy (information theory)](https://en.wikipedia.org/wiki/Redundancy_(information_theory))
- [Run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Sampling (signal processing)](https://en.wikipedia.org/wiki/Sampling_(signal_processing))
- [Sequence alignment](https://en.wikipedia.org/wiki/Sequence_alignment)
- [Sequitur algorithm](https://en.wikipedia.org/wiki/Sequitur_algorithm)
- [Set partitioning in hierarchical trees](https://en.wikipedia.org/wiki/Set_partitioning_in_hierarchical_trees)
- [Shannon coding](https://en.wikipedia.org/wiki/Shannon_coding)
- [Shannon–Fano coding](https://en.wikipedia.org/wiki/Shannon%E2%80%93Fano_coding)
- [Shannon–Fano–Elias coding](https://en.wikipedia.org/wiki/Shannon%E2%80%93Fano%E2%80%93Elias_coding)
- [Silence compression](https://en.wikipedia.org/wiki/Silence_compression)
- [Smallest grammar problem](https://en.wikipedia.org/wiki/Smallest_grammar_problem)
- [Snappy (compression)](https://en.wikipedia.org/wiki/Snappy_(compression))
- [Sorting](https://en.wikipedia.org/wiki/Sorting)
- [Sound quality](https://en.wikipedia.org/wiki/Sound_quality)
- [Space complexity](https://en.wikipedia.org/wiki/Space_complexity)
- [Speech coding](https://en.wikipedia.org/wiki/Speech_coding)
- [Standard test image](https://en.wikipedia.org/wiki/Standard_test_image)
- [State of the art](https://en.wikipedia.org/wiki/State_of_the_art)
- [Sub-band coding](https://en.wikipedia.org/wiki/Sub-band_coding)
- [Suffix](https://en.wikipedia.org/wiki/Suffix)
- [Suffix array](https://en.wikipedia.org/wiki/Suffix_array)
- [Texture compression](https://en.wikipedia.org/wiki/Texture_compression)
- [Time complexity](https://en.wikipedia.org/wiki/Time_complexity)
- [Timeline of information theory](https://en.wikipedia.org/wiki/Timeline_of_information_theory)
- [Transform coding](https://en.wikipedia.org/wiki/Transform_coding)
- [Tunstall coding](https://en.wikipedia.org/wiki/Tunstall_coding)
- [Unary coding](https://en.wikipedia.org/wiki/Unary_coding)
- [Universal code (data compression)](https://en.wikipedia.org/wiki/Universal_code_(data_compression))
- [Variable bitrate](https://en.wikipedia.org/wiki/Variable_bitrate)
- [Video](https://en.wikipedia.org/wiki/Video)
- [Video codec](https://en.wikipedia.org/wiki/Video_codec)
- [Video compression picture types](https://en.wikipedia.org/wiki/Video_compression_picture_types)
- [Video quality](https://en.wikipedia.org/wiki/Video_quality)
- [Warped linear predictive coding](https://en.wikipedia.org/wiki/Warped_linear_predictive_coding)
- [Wavelet transform](https://en.wikipedia.org/wiki/Wavelet_transform)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [ZbMATH Open](https://en.wikipedia.org/wiki/ZbMATH_Open)
- [Zstd](https://en.wikipedia.org/wiki/Zstd)
- [Μ-law algorithm](https://en.wikipedia.org/wiki/%CE%9C-law_algorithm)
- [Template:Compression methods](https://en.wikipedia.org/wiki/Template:Compression_methods)
- [Template talk:Compression methods](https://en.wikipedia.org/wiki/Template_talk:Compression_methods)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:34:14.715321+00:00_