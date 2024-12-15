# De Bruijn sequence

## Article Metadata

- **Last Updated:** 2024-12-15T03:59:03.079452+00:00
- **Original Article:** [De Bruijn sequence](https://en.wikipedia.org/wiki/De_Bruijn_sequence)
- **Language:** en
- **Page ID:** 1565267

## Summary

In combinatorial mathematics, a de Bruijn sequence of order n on a size-k alphabet A is a cyclic sequence in which every possible length-n string on A occurs exactly once as a substring (i.e., as a contiguous subsequence). Such a sequence is denoted by B(k, n) and has length kn, which is also the number of distinct strings of length n on A. Each of these distinct strings, when taken as a substring of B(k, n), must start at a different position, because substrings starting at the same position ar

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Binary sequences
- Category:CS1 maint: postscript
- Category:Enumerative combinatorics
- Category:Short description is different from Wikidata

## Table of Contents

- History
- Examples
- Construction
- Uses
- f-fold de Bruijn sequences
- de Bruijn torus
- de Bruijn decoding
- See also
- Notes
- References
- External links

## Content

In combinatorial mathematics, a de Bruijn sequence of order n on a size-k alphabet A is a cyclic sequence in which every possible length-n string on A occurs exactly once as a substring (i.e., as a contiguous subsequence). Such a sequence is denoted by B(k, n) and has length kn, which is also the number of distinct strings of length n on A. Each of these distinct strings, when taken as a substring of B(k, n), must start at a different position, because substrings starting at the same position are not distinct. Therefore, B(k, n) must have at least kn symbols. And since B(k, n) has exactly kn symbols, de Bruijn sequences are optimally short with respect to the property of containing every string of length n at least once.
The number of distinct de Bruijn sequences B(k, n) is

  
    
      
        
          
            
              
                
                  (
                  
                    k
                    !
                  
                  )
                
                
                  
                    k
                    
                      n
                      −
                      1
                    
                  
                
              
              
                k
                
                  n
                
              
            
          
        
        .
      
    
    {\displaystyle {\dfrac {\left(k!\right)^{k^{n-1}}}{k^{n}}}.}
  

The sequences are named after the Dutch mathematician Nicolaas Govert de Bruijn, who wrote about them in 1946. As he later wrote, the existence of de Bruijn sequences for each order together with the above properties were first proved, for the case of alphabets with two elements, by Camille Flye Sainte-Marie (1894). The generalization to larger alphabets is due to Tatyana van Aardenne-Ehrenfest and de Bruijn (1951). Automata for recognizing these sequences are denoted as de Bruijn automata.
In most applications, A = {0,1}.

History
The earliest known example of a de Bruijn sequence comes from Sanskrit prosody where, since the work of Pingala, each possible three-syllable pattern of long and short syllables is given a name, such as 'y' for short–long–long and 'm' for long–long–long. To remember these names, the mnemonic yamātārājabhānasalagām is used, in which each three-syllable pattern occurs starting at its name: 'yamātā' has a short–long–long pattern, 'mātārā' has a long–long–long pattern, and so on, until 'salagām' which has a short–short–long pattern. This mnemonic, equivalent to a de Bruijn sequence on binary 3-tuples, is of unknown antiquity, but is at least as old as Charles Philip Brown's 1869 book on Sanskrit prosody that mentions it and considers it "an ancient line, written by Pāṇini".
In 1894, A. de Rivière raised the question in an issue of the French problem journal L'Intermédiaire des Mathématiciens, of the existence of a circular arrangement of zeroes and ones of size 
  
    
      
        
          2
          
            n
          
        
      
    
    {\displaystyle 2^{n}}
  
 that contains all 
  
    
      
        
          2
          
            n
          
        
      
    
    {\displaystyle 2^{n}}
  
 binary sequences of length 
  
    
      
        n
      
    
    {\displaystyle n}
  
. The problem was solved (in the affirmative), along with the count of 
  
    
      
        
          2
          
            
              2
              
                n
                −
                1
              
            
            −
            n
          
        
      
    
    {\displaystyle 2^{2^{n-1}-n}}
  
 distinct solutions, by Camille Flye Sainte-Marie in the same year. This was largely forgotten, and Martin (1934) proved the existence of such cycles for general alphabet size in place of 2, with an algorithm for constructing them. Finally, when in 1944 Kees Posthumus conjectured the count 
  
    
      
        
          2
          
            
              2
              
                n
                −
                1
              
            
            −
            n
          
        
      
    
    {\displaystyle 2^{2^{n-1}-n}}
  
 for binary sequences, de Bruijn proved the conjecture in 1946, through which the problem became well-known.
Karl Popper independently describes these objects in his The Logic of Scientific Discovery (1934), calling them "shortest random-like sequences".

Examples
Taking A = {0, 1}, there are two distinct B(2, 3): 00010111 and 11101000, one being the reverse or negation of the other.
Two of the 16 possible B(2, 4) in the same alphabet are 0000100110101111 and 0000111101100101.
Two of the 2048 possible B(2, 5) in the same alphabet are 00000100011001010011101011011111 and 00000101001000111110111001101011.

Construction
The de Bruijn sequences can be constructed by taking a Hamiltonian path of an n-dimensional de Bruijn graph over k symbols (or equivalently, an Eulerian cycle of an (n − 1)-dimensional de Bruijn graph).
An alternative construction involves concatenating together, in lexicographic order, all the Lyndon words whose length divides n.
An inverse Burrows–Wheeler transform can be used to generate the required Lyndon words in lexicographic order.
de Bruijn sequences can also be constructed using shift registers or via finite fields.

Example using de Bruijn graph
Goal: to construct a B(2, 4) de Bruijn sequence of length 24 = 16 using Eulerian (n − 1 = 4 − 1 = 3) 3-D de Bruijn graph cycle.
Each edge in this 3-dimensional de Bruijn graph corresponds to a sequence of four digits: the three digits that label the vertex that the edge is leaving followed by the one that labels the edge. If one traverses the edge labeled 1 from 000, one arrives at 001, thereby indicating the presence of the subsequence 0001 in the de Bruijn sequence.  To traverse each edge exactly once is to use each of the 16 four-digit sequences exactly once.
For example, suppose we follow the following Eulerian path through these vertices:

000, 000, 001, 011, 111, 111, 110, 101, 011,
110, 100, 001, 010, 101, 010, 100, 000.
These are the output sequences of length k:

0 0 0 0
_ 0 0 0 1
_ _ 0 0 1 1
This corresponds to the following de Bruijn sequence:

0 0 0 0 1 1 1 1 0 1 1 0 0 1 0 1
The eight vertices appear in the sequence in the following way:

      {0  0  0  0} 1  1  1  1  0  1  1  0  0  1  0  1
       0 {0  0  0  1} 1  1  1  0  1  1  0  0  1  0  1
       0  0 {0  0  1  1} 1  1  0  1  1  0  0  1  0  1
       0  0  0 {0  1  1  1} 1  0  1  1  0  0  1  0  1
       0  0  0  0 {1  1  1  1} 0  1  1  0  0  1  0  1
       0  0  0  0  1 {1  1  1  0} 1  1  0  0  1  0  1
       0  0  0  0  1  1 {1  1  0  1} 1  0  0  1  0  1
       0  0  0  0  1  1  1 {1  0  1  1} 0  0  1  0  1
       0  0  0  0  1  1  1  1 {0  1  1  0} 0  1  0  1
       0  0  0  0  1  1  1  1  0 {1  1  0  0} 1  0  1
       0  0  0  0  1  1  1  1  0  1 {1  0  0  1} 0  1
       0  0  0  0  1  1  1  1  0  1  1 {0  0  1  0} 1
       0  0  0  0  1  1  1  1  0  1  1  0 {0  1  0  1}
       0} 0  0  0  1  1  1  1  0  1  1  0  0 {1  0  1 ...
   ... 0  0} 0  0  1  1  1  1  0  1  1  0  0  1 {0  1 ...
   ... 0  0  0} 0  1  1  1  1  0  1  1  0  0  1  0 {1 ...

...and then we return to the starting point.  Each of the eight 3-digit sequences (corresponding to the eight vertices) appears exactly twice, and each of the sixteen 4-digit sequences (corresponding to the 16 edges) appears exactly once.

Example using inverse Burrows—Wheeler transform
Mathematically, an inverse Burrows—Wheeler transform on a word w generates a multi-set of equivalence classes consisting of strings and their rotations. These equivalence classes of strings each contain a Lyndon word as a unique minimum element, so the inverse Burrows—Wheeler transform can be considered to generate a set of Lyndon words. It can be shown that if we perform the inverse Burrows—Wheeler transform on a word w consisting of the size-k alphabet repeated kn−1 times (so that it will produce a word the same length as the desired de Bruijn sequence), then the result will be the set of all Lyndon words whose length divides n. It follows that arranging these Lyndon words in lexicographic order will yield a de Bruijn sequence B(k,n), and that this will be the first de Bruijn sequence in lexicographic order. The following method can be used to perform the inverse Burrows—Wheeler transform, using its standard permutation:

Sort the characters in the string w, yielding a new string w′
Position the string w′ above the string w, and map each letter's position in w′ to its position in w while preserving order. This process defines the Standard Permutation.
Write this permutation in cycle notation with the smallest position in each cycle first, and the cycles sorted in increasing order.
For each cycle, replace each number with the corresponding letter from string w′ in that position.
Each cycle has now become a Lyndon word, and they are arranged in lexicographic order, so dropping the parentheses yields the first de Bruijn sequence.
For example, to construct the smallest B(2,4) de Bruijn sequence of length 24 = 16, repeat the alphabet (ab) 8 times yielding w=abababababababab. Sort the characters in w, yielding w′=aaaaaaaabbbbbbbb. Position w′ above w as shown, and map each element in w′ to the corresponding element in w by drawing a line. Number the columns as shown so we can read the cycles of the permutation:

Starting from the left, the Standard Permutation notation cycles are: (1) (2 3 5 9) (4 7 13 10) (6 11) (8 15 14 12) (16). (Standard Permutation)
Then, replacing each number by the corresponding letter in w′ from that column yields: (a)(aaab)(aabb)(ab)(abbb)(b).
These are all of the Lyndon words whose length divides 4, in lexicographic order, so dropping the parentheses gives B(2,4) = aaaabaabbababbbb.

Algorithm
The following Python code calculates a de Bruijn sequence, given k and n, based on an algorithm from Frank Ruskey's Combinatorial Generation.

which prints

00010111
aabacadbbcbdccdd

Note that these sequences are understood to "wrap around" in a cycle. For example, the first sequence contains 110 and 100 in this fashion.

Uses
de Bruijn cycles are of general use in neuroscience and psychology experiments that examine the effect of stimulus order upon neural systems, and can be specially crafted for use with functional magnetic resonance imaging.

Angle detection
The symbols of a de Bruijn sequence written around a circular object (such as a wheel of a robot) can be used to identify its angle by examining the n consecutive symbols facing a fixed point. This angle-encoding problem is known as the "rotating drum problem". Gray codes can be used as similar rotary positional encoding mechanisms, a method commonly found in rotary encoders.

Finding least- or most-significant set bit in a word
A de Bruijn sequence can be used to quickly find the index of the least significant set bit ("right-most 1") or the most significant set bit ("left-most 1") in a word using bitwise operations and multiplication. The following example uses a de Bruijn sequence to determine the index of the least significant set bit (equivalent to counting the number of trailing '0' bits) in a 32 bit unsigned integer:

The lowestBitIndex() function returns the index of the least-significant set bit in v, or zero if v has no set bits. The constant 0x077CB531U in the expression is the B (2, 5) sequence 0000 0111 0111 1100 1011 0101 0011 0001 (spaces added for clarity). The operation (v & -v) zeros all bits except the least-significant bit set, resulting in a new value which is a power of 2. This power of 2 is multiplied (arithmetic modulo 232) by the de Bruijn sequence, thus producing a 32-bit product in which the bit sequence of the 5 MSBs is unique for each power of 2. The 5 MSBs are shifted into the LSB positions to produce a hash code in the range [0, 31], which is then used as an index into hash table BitPositionLookup. The selected hash table value is the bit index of the least significant set bit in v.
The following example determines the index of the most significant bit set in a 32 bit unsigned integer:

In the above example an alternative de Bruijn sequence (0x06EB14F9U) is used, with corresponding reordering of array values. The choice of this particular de Bruijn sequence is arbitrary, but the hash table values must be ordered to match the chosen de Bruijn sequence. The keepHighestBit() function zeros all bits except the most-significant set bit, resulting in a value which is a power of 2, which is then processed as in the previous example.

Brute-force attacks on locks
A de Bruijn sequence can be used to shorten a brute-force attack on a PIN-like code lock that does not have an "enter" key and accepts the last n digits entered. For example, a digital door lock with a 4-digit code (each digit having 10 possibilities, from 0 to 9) would have B (10, 4) solutions, with length 10000. Therefore, only at most 10000 + 3 = 10003 (as the solutions are cyclic) presses are needed to open the lock, whereas trying all codes separately would require 4 × 10000 = 40000 presses.

f-fold de Bruijn sequences
An f-fold n-ary de Bruijn sequence is an extension of the notion n-ary de Bruijn sequence, such that the sequence of the length 
  
    
      
        f
        
          k
          
            n
          
        
      
    
    {\displaystyle fk^{n}}
  
 contains every possible subsequence of the length n exactly f times. For example, for 
  
    
      
        n
        =
        2
      
    
    {\displaystyle n=2}
  
 the cyclic sequences 11100010 and 11101000  are two-fold binary de Bruijn sequences. The number of two-fold de Bruijn sequences, 
  
    
      
        
          N
          
            n
          
        
      
    
    {\displaystyle N_{n}}
  
 for 
  
    
      
        n
        =
        1
      
    
    {\displaystyle n=1}
  
 is 
  
    
      
        
          N
          
            1
          
        
        =
        2
      
    
    {\displaystyle N_{1}=2}
  
, the other known numbers are 
  
    
      
        
          N
          
            2
          
        
        =
        5
      
    
    {\displaystyle N_{2}=5}
  
, 
  
    
      
        
          N
          
            3
          
        
        =
        72
      
    
    {\displaystyle N_{3}=72}
  
, and 
  
    
      
        
          N
          
            4
          
        
        =
        43768
      
    
    {\displaystyle N_{4}=43768}
  
.

de Bruijn torus
A de Bruijn torus is a toroidal array with the property that every k-ary m-by-n matrix occurs exactly once.
Such a pattern can be used for two-dimensional positional encoding in a fashion analogous to that described above for rotary encoding.  Position can be determined by examining the m-by-n matrix directly adjacent to the sensor, and calculating its position on the de Bruijn torus.

de Bruijn decoding
Computing the position of a particular unique tuple or matrix in a de Bruijn sequence or torus is known as the de Bruijn decoding problem. Efficient ⁠
  
    
      
        
          O
          (
          n
          log
          ⁡
          n
          )
        
      
    
    {\displaystyle \color {Blue}O(n\log n)}
  
⁠ decoding algorithms exist for special, recursively constructed sequences and extend to the two-dimensional case. de Bruijn decoding is of interest, e.g., in cases where large sequences or tori are used for positional encoding.

See also
Normal number
Linear-feedback shift register
n-sequence
BEST theorem
Superpermutation

Notes
References
van Aardenne-Ehrenfest, Tanja; de Bruijn, Nicolaas Govert (1951). "Circuits and trees in oriented linear graphs" (PDF). Simon Stevin. 28: 203–217. MR 0047311.
Aguirre, G. K.; Mattar, M. G.; Magis-Weinberg, L. (2011). "de Bruijn cycles for neural decoding". NeuroImage. 56 (3): 1293–1300. doi:10.1016/j.neuroimage.2011.02.005. PMC 3104402. PMID 21315160. Archived from the original on 2016-01-26. Retrieved 2015-06-04.
Anderson, Sean Eron (1997–2009). "Bit Twiddling Hacks". Stanford University. Retrieved 2009-02-12.
Berstel, Jean; Perrin, Dominique (2007). "The origins of combinatorics on words" (PDF). European Journal of Combinatorics. 28 (3): 996–1022. doi:10.1016/j.ejc.2005.07.019. MR 2300777.
Brown, C. P. (1869). Sanskrit Prosody and Numerical Symbols Explained. p. 28.
de Bruijn, Nicolaas Govert (1946). "A combinatorial problem" (PDF). Proc. Koninklijke Nederlandse Akademie V. Wetenschappen. 49: 758–764. MR 0018142, Indagationes Mathematicae 8: 461–467{{cite journal}}:  CS1 maint: postscript (link)
de Bruijn, Nicolaas Govert (1975). Acknowledgement of Priority to C. Flye Sainte-Marie on the counting of circular arrangements of 2n zeros and ones that show each n-letter word exactly once (PDF). T.H.-Report 75-WSK-06. Technological University Eindhoven.
Busch, Philip (2009). "Computing Trailing Zeros HOWTO". Archived from the original on 2015-01-29. Retrieved 2015-01-29.
Flye Sainte-Marie, Camille (1894). "Solution to question nr. 48". L'Intermédiaire des Mathématiciens. 1: 107–110.
Goresky, Mark; Klapper, Andrew (2012). "8.2.5 Shift register generation of de Bruijn sequences". Algebraic Shift Register Sequences. Cambridge University Press. pp. 174–175. ISBN 978-1-10701499-2.
Hall, Rachel W. (2008). "Math for poets and drummers" (PDF). Math Horizons. 15 (3): 10–11. doi:10.1080/10724117.2008.11974752. S2CID 3637061. Archived from the original (PDF) on 2012-02-12. Retrieved 2008-10-22.
Higgins, Peter (November 2012). "Burrows-Wheeler transforms and de Bruijn words" (PDF). Retrieved 2017-02-11.
Hurlbert, Glenn; Isaak, Garth (1993). "On the de Bruijn torus problem". Journal of Combinatorial Theory. Series A. 64 (1): 50–62. doi:10.1016/0097-3165(93)90087-O. MR 1239511.
Kak, Subhash (2000). "Yamātārājabhānasalagāṃ an interesting combinatoric sūtra" (PDF). Indian Journal of History of Science. 35 (2): 123–127. Archived from the original (PDF) on 2014-10-29.
Klein, Andreas (2013). Stream Ciphers. Springer. p. 59. ISBN 978-1-44715079-4.
Knuth, Donald Ervin (2006). The Art of Computer Programming, Fascicle 4: Generating All Trees – History of Combinatorial Generation. Addison–Wesley. p. 50. ISBN 978-0-321-33570-8.
Fredricksen, Harold; Maiorana, James (1978). "Necklaces of beads in k colors and k-ary de Bruijn sequences". Discrete Mathematics. 23 (3): 207–210. doi:10.1016/0012-365X(78)90002-X. MR 0523071.
Martin, Monroe H. (1934). "A problem in arrangements" (PDF). Bulletin of the American Mathematical Society. 40 (12): 859–864. doi:10.1090/S0002-9904-1934-05988-3. MR 1562989.
Osipov, Vladimir (2016). "Wavelet Analysis on Symbolic Sequences and Two-Fold de Bruijn Sequences". Journal of Statistical Physics. 164 (1): 142–165. arXiv:1601.02097. Bibcode:2016JSP...164..142O. doi:10.1007/s10955-016-1537-5. ISSN 1572-9613. S2CID 16535836.
Popper, Karl (2002) [1934]. The logic of scientific discovery. Routledge. p. 294. ISBN 978-0-415-27843-0.
Ralston, Anthony (1982). "de Bruijn sequences—a model example of the interaction of discrete mathematics and computer science". Mathematics Magazine. 55 (3): 131–143. doi:10.2307/2690079. JSTOR 2690079. MR 0653429.
Stein, Sherman K. (1963). "Yamátárájabhánasalagám". The Man-made Universe: An Introduction to the Spirit of Mathematics. pp. 110–118. Reprinted in Wardhaugh, Benjamin, ed. (2012), A Wealth of Numbers: An Anthology of 500 Years of Popular Mathematics Writing, Princeton University Press, pp. 139–144.
Tuliani, Jonathan (2001). "de Bruijn sequences with efficient decoding algorithms". Discrete Mathematics. 226 (1–3): 313–336. doi:10.1016/S0012-365X(00)00117-5. MR 1802599.
van Lint, J. H.; Wilson, Richard Michael (2001). A Course in Combinatorics. Cambridge University Press. p. 71. ISBN 978-0-52100601-9.

External links
Weisstein, Eric W. "de Bruijn Sequence". MathWorld.
OEIS sequence A166315 (Lexicographically smallest binary de Bruijn sequences)
De Bruijn sequence
CGI generator
Applet generator
Javascript generator and decoder. Implementation of J. Tuliani's algorithm.
Door code lock
Minimal arrays containing all sub-array combinations of symbols: de Bruijn sequences and tori
http://debruijnsequence.org has many kinds of de Bruijn sequences.

## Related Articles

### Internal Links

- [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
- [Alphabet (formal languages)](https://en.wikipedia.org/wiki/Alphabet_(formal_languages))
- [Analysis of algorithms](https://en.wikipedia.org/wiki/Analysis_of_algorithms)
- [Angle](https://en.wikipedia.org/wiki/Angle)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Automata theory](https://en.wikipedia.org/wiki/Automata_theory)
- [BEST theorem](https://en.wikipedia.org/wiki/BEST_theorem)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Bitwise operation](https://en.wikipedia.org/wiki/Bitwise_operation)
- [Bulletin of the American Mathematical Society](https://en.wikipedia.org/wiki/Bulletin_of_the_American_Mathematical_Society)
- [Burrows–Wheeler transform](https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform)
- [Charles Philip Brown](https://en.wikipedia.org/wiki/Charles_Philip_Brown)
- [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press)
- [Charles Philip Brown](https://en.wikipedia.org/wiki/Charles_Philip_Brown)
- [Combinatorics](https://en.wikipedia.org/wiki/Combinatorics)
- [Conjecture](https://en.wikipedia.org/wiki/Conjecture)
- [Cyclic order](https://en.wikipedia.org/wiki/Cyclic_order)
- [De Bruijn graph](https://en.wikipedia.org/wiki/De_Bruijn_graph)
- [De Bruijn torus](https://en.wikipedia.org/wiki/De_Bruijn_torus)
- [Electronic lock](https://en.wikipedia.org/wiki/Electronic_lock)
- [Discrete Mathematics (journal)](https://en.wikipedia.org/wiki/Discrete_Mathematics_(journal))
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Dominique Perrin](https://en.wikipedia.org/wiki/Dominique_Perrin)
- [Donald Knuth](https://en.wikipedia.org/wiki/Donald_Knuth)
- [Equivalence class](https://en.wikipedia.org/wiki/Equivalence_class)
- [Eric W. Weisstein](https://en.wikipedia.org/wiki/Eric_W._Weisstein)
- [Eulerian path](https://en.wikipedia.org/wiki/Eulerian_path)
- [European Journal of Combinatorics](https://en.wikipedia.org/wiki/European_Journal_of_Combinatorics)
- [Finite field](https://en.wikipedia.org/wiki/Finite_field)
- [Frank Ruskey](https://en.wikipedia.org/wiki/Frank_Ruskey)
- [Functional magnetic resonance imaging](https://en.wikipedia.org/wiki/Functional_magnetic_resonance_imaging)
- [Gray code](https://en.wikipedia.org/wiki/Gray_code)
- [Hamiltonian path](https://en.wikipedia.org/wiki/Hamiltonian_path)
- [Hash table](https://en.wikipedia.org/wiki/Hash_table)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Indagationes Mathematicae](https://en.wikipedia.org/wiki/Indagationes_Mathematicae)
- [Integer sequence](https://en.wikipedia.org/wiki/Integer_sequence)
- [J. H. van Lint](https://en.wikipedia.org/wiki/J._H._van_Lint)
- [JSTOR](https://en.wikipedia.org/wiki/JSTOR)
- [Jean Berstel](https://en.wikipedia.org/wiki/Jean_Berstel)
- [Journal of Combinatorial Theory](https://en.wikipedia.org/wiki/Journal_of_Combinatorial_Theory)
- [Journal of Statistical Physics](https://en.wikipedia.org/wiki/Journal_of_Statistical_Physics)
- [Karl Popper](https://en.wikipedia.org/wiki/Karl_Popper)
- [Kees Posthumus](https://en.wikipedia.org/wiki/Kees_Posthumus)
- [L'Intermédiaire des mathématiciens](https://en.wikipedia.org/wiki/L%27Interm%C3%A9diaire_des_math%C3%A9maticiens)
- [Linear-feedback shift register](https://en.wikipedia.org/wiki/Linear-feedback_shift_register)
- [Lyndon word](https://en.wikipedia.org/wiki/Lyndon_word)
- [Mathematical Reviews](https://en.wikipedia.org/wiki/Mathematical_Reviews)
- [Mark Goresky](https://en.wikipedia.org/wiki/Mark_Goresky)
- [MathWorld](https://en.wikipedia.org/wiki/MathWorld)
- [Mathematical proof](https://en.wikipedia.org/wiki/Mathematical_proof)
- [Mathematics](https://en.wikipedia.org/wiki/Mathematics)
- [Mathematics Magazine](https://en.wikipedia.org/wiki/Mathematics_Magazine)
- [Moser–de Bruijn sequence](https://en.wikipedia.org/wiki/Moser%E2%80%93de_Bruijn_sequence)
- [Maximum length sequence](https://en.wikipedia.org/wiki/Maximum_length_sequence)
- [Nicolaas Govert de Bruijn](https://en.wikipedia.org/wiki/Nicolaas_Govert_de_Bruijn)
- [Normal number](https://en.wikipedia.org/wiki/Normal_number)
- [Number theory](https://en.wikipedia.org/wiki/Number_theory)
- [PubMed Central](https://en.wikipedia.org/wiki/PubMed_Central)
- [PubMed](https://en.wikipedia.org/wiki/PubMed)
- [Permutation](https://en.wikipedia.org/wiki/Permutation)
- [Personal identification number](https://en.wikipedia.org/wiki/Personal_identification_number)
- [Pingala](https://en.wikipedia.org/wiki/Pingala)
- [Princeton University Press](https://en.wikipedia.org/wiki/Princeton_University_Press)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Pāṇini](https://en.wikipedia.org/wiki/P%C4%81%E1%B9%87ini)
- [R. M. Wilson](https://en.wikipedia.org/wiki/R._M._Wilson)
- [Robot](https://en.wikipedia.org/wiki/Robot)
- [Rotary encoder](https://en.wikipedia.org/wiki/Rotary_encoder)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [STL (file format)](https://en.wikipedia.org/wiki/STL_(file_format))
- [Sanskrit prosody](https://en.wikipedia.org/wiki/Sanskrit_prosody)
- [Sherman K. Stein](https://en.wikipedia.org/wiki/Sherman_K._Stein)
- [Shift register](https://en.wikipedia.org/wiki/Shift_register)
- [Simon Stevin (journal)](https://en.wikipedia.org/wiki/Simon_Stevin_(journal))
- [Stanford University](https://en.wikipedia.org/wiki/Stanford_University)
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [Subhash Kak](https://en.wikipedia.org/wiki/Subhash_Kak)
- [Subsequence](https://en.wikipedia.org/wiki/Subsequence)
- [Substring](https://en.wikipedia.org/wiki/Substring)
- [Superpermutation](https://en.wikipedia.org/wiki/Superpermutation)
- [Tatyana Ehrenfest](https://en.wikipedia.org/wiki/Tatyana_Ehrenfest)
- [The Logic of Scientific Discovery](https://en.wikipedia.org/wiki/The_Logic_of_Scientific_Discovery)
- [Up to](https://en.wikipedia.org/wiki/Up_to)
- [Word (computer architecture)](https://en.wikipedia.org/wiki/Word_(computer_architecture))
- [Template:Cite journal](https://en.wikipedia.org/wiki/Template:Cite_journal)
- [Category:CS1 maint: postscript](https://en.wikipedia.org/wiki/Category:CS1_maint:_postscript)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:59:03.079452+00:00_