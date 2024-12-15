# Linear congruential generator

## Article Metadata

- **Last Updated:** 2024-12-15T04:33:57.778667+00:00
- **Original Article:** [Linear congruential generator](https://en.wikipedia.org/wiki/Linear_congruential_generator)
- **Language:** en
- **Page ID:** 45527

## Summary

A linear congruential generator (LCG) is an algorithm that yields a sequence of pseudo-randomized numbers calculated with a discontinuous piecewise linear equation. The method represents one of the oldest and best-known pseudorandom number generator algorithms. The theory behind them is relatively easy to understand, and they are easily implemented and fast, especially on computer hardware which can provide modular arithmetic by storage-bit truncation.
The generator is defined by the recurrence 

## Categories

- Category:All articles needing additional references
- Category:All articles with unsourced statements
- Category:Articles needing additional references from July 2021
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from November 2017
- Category:Modular arithmetic
- Category:Pseudorandom number generators
- Category:Short description is different from Wikidata
- Category:Webarchive template wayback links

## Table of Contents

- History
- Period length
- Parameters in common use
- Advantages and disadvantages
- Sample code
- LCG derivatives
- Comparison with other PRNGs
- See also
- Notes
- References
- External links

## Content

A linear congruential generator (LCG) is an algorithm that yields a sequence of pseudo-randomized numbers calculated with a discontinuous piecewise linear equation. The method represents one of the oldest and best-known pseudorandom number generator algorithms. The theory behind them is relatively easy to understand, and they are easily implemented and fast, especially on computer hardware which can provide modular arithmetic by storage-bit truncation.
The generator is defined by the recurrence relation:

  
    
      
        
          X
          
            n
            +
            1
          
        
        =
        
          (
          
            a
            
              X
              
                n
              
            
            +
            c
          
          )
        
        
          mod
          
            m
          
        
      
    
    {\displaystyle X_{n+1}=\left(aX_{n}+c\right){\bmod {m}}}
  

where 
  
    
      
        X
      
    
    {\displaystyle X}
  
 is the sequence of pseudo-random values, and

  
    
      
        m
        ,
        
        0
        <
        m
      
    
    {\displaystyle m,\,0<m}
  
 — the "modulus"

  
    
      
        a
        ,
        
        0
        <
        a
        <
        m
      
    
    {\displaystyle a,\,0<a<m}
  
 — the "multiplier"

  
    
      
        c
        ,
        
        0
        ≤
        c
        <
        m
      
    
    {\displaystyle c,\,0\leq c<m}
  
 — the "increment"

  
    
      
        
          X
          
            0
          
        
        ,
        
        0
        ≤
        
          X
          
            0
          
        
        <
        m
      
    
    {\displaystyle X_{0},\,0\leq X_{0}<m}
  
 — the "seed" or "start value"
are integer constants that specify the generator. If c = 0, the generator is often called a multiplicative congruential generator (MCG), or Lehmer RNG. If c ≠ 0, the method is called a mixed congruential generator.: 4- 
When c ≠ 0, a mathematician would call the recurrence an affine transformation, not a linear one, but the misnomer is well-established in computer science.: 1

History
The Lehmer generator was published in 1951 and the Linear congruential generator was published in 1958 by W. E. Thomson and A. Rotenberg.

Period length
A benefit of LCGs is that an appropriate choice of parameters results in a period which is both known and long. Although not the only criterion, too short a period is a fatal flaw in a pseudorandom number generator.
While LCGs are capable of producing pseudorandom numbers which can pass formal tests for randomness, the quality of the output is extremely sensitive to the choice of the parameters m and a.  For example, a = 1 and c = 1 produces a simple modulo-m counter, which has a long period, but is obviously non-random.  Other values of c coprime to m produce a Weyl sequence, which is better distributed but still obviously non-random.
Historically, poor choices for a have led to ineffective implementations of LCGs. A particularly illustrative example of this is RANDU, which was widely used in the early 1970s and led to many results which are currently being questioned because of the use of this poor LCG.: 1198–9 
There are three common families of parameter choice:

m prime, c = 0
This is the original Lehmer RNG construction. The period is m−1 if the multiplier a is chosen to be a primitive element of the integers modulo m. The initial state must be chosen between 1 and m−1.
One disadvantage of a prime modulus is that the modular reduction requires a double-width product and an explicit reduction step. Often a prime just less than a power of 2 is used (the Mersenne primes 231−1 and 261−1 are popular), so that the reduction modulo m = 2e − d can be computed as (ax mod 2e) + d ⌊ax/2e⌋. This must be followed by a conditional subtraction of m if the result is too large, but the number of subtractions is limited to ad/m, which can be easily limited to one if d is small.
If a double-width product is unavailable, and the multiplier is chosen carefully, Schrage's method may be used. To do this, factor m = qa+r, i.e. q = ⌊m/a⌋ and r = m mod a. Then compute ax mod m = a(x mod q) − r⌊x/q⌋. Since x mod q < q ≤ m/a, the first term is strictly less than am/a = m. If a is chosen so that r ≤ q (and thus r/q ≤ 1), then the second term is also less than m: r⌊x/q⌋ ≤ rx/q = x(r/q) ≤ x < m. Thus, both products can be computed with a single-width product, and the difference between them lies in the range [1−m, m−1], so can be reduced to [0, m−1] with a single conditional add.
A second disadvantage is that it is awkward to convert the value 1 ≤ x < m to uniform random bits. If a prime just less than a power of 2 is used, sometimes the missing values are simply ignored.

m a power of 2, c = 0
Choosing m to be a power of two, most often m = 232 or m = 264, produces a particularly efficient LCG, because this allows the modulus operation to be computed by simply truncating the binary representation. In fact, the most significant bits are usually not computed at all. There are, however, disadvantages.
This form has maximal period m/4, achieved if a ≡ ±3 (mod 8) and the initial state X0 is odd.  Even in this best case, the low three bits of X alternate between two values and thus only contribute one bit to the state.  X is always odd (the lowest-order bit never changes), and only one of the next two bits ever changes.  If a ≡ +3, X alternates ±1↔±3, while if a ≡ −3, X alternates ±1↔∓3 (all modulo 8).
It can be shown that this form is equivalent to a generator with modulus m/4 and c ≠ 0.
A more serious issue with the use of a power-of-two modulus is that the low bits have a shorter period than the high bits.  Its simplicity of implementation comes from the fact that bits are never affected by higher-order bits, so the low b bits of such a generator form a modulo-2b LCG by themselves, repeating with a period of 2b−2. Only the most significant bit of X achieves the full period.

m a power of 2, c ≠ 0
When c ≠ 0, correctly chosen parameters allow a period equal to m, for all seed values. This will occur if and only if:: 17–19 

  
    
      
        m
      
    
    {\displaystyle m}
  
 and 
  
    
      
        c
      
    
    {\displaystyle c}
  
 are coprime,

  
    
      
        a
        −
        1
      
    
    {\displaystyle a-1}
  
 is divisible by all prime factors of 
  
    
      
        m
      
    
    {\displaystyle m}
  
,

  
    
      
        a
        −
        1
      
    
    {\displaystyle a-1}
  
 is divisible by 4 if 
  
    
      
        m
      
    
    {\displaystyle m}
  
 is divisible by 4.
These three requirements are referred to as the Hull–Dobell Theorem.
This form may be used with any m, but only works well for m with many repeated prime factors, such as a power of 2; using a computer's word size is the most common choice.  If m were a square-free integer, this would only allow a ≡ 1 (mod m), which makes a very poor PRNG; a selection of possible full-period multipliers is only available when m has repeated prime factors.
Although the Hull–Dobell theorem provides maximum period, it is not sufficient to guarantee a good generator.: 1199   For example, it is desirable for a − 1 to not be any more divisible by prime factors of m than necessary.  If m is a power of 2, then a − 1 should be divisible by 4 but not divisible by 8, i.e. a ≡ 5 (mod 8).: §3.2.1.3 
Indeed, most multipliers produce a sequence which fails one test for non-randomness or another, and finding a multiplier which is satisfactory to all applicable criteria: §3.3.3  is quite challenging.  The spectral test is one of the most important tests.
Note that a power-of-2 modulus shares the problem as described above for c = 0: the low k bits form a generator with modulus 2k and thus repeat with a period of 2k; only the most significant bit achieves the full period.  If a pseudorandom number less than r is desired, ⌊rX/m⌋ is a much higher-quality result than X mod r.  Unfortunately, most programming languages make the latter much easier to write (X % r), so it is very commonly used.
The generator is not sensitive to the choice of c, as long as it is relatively prime to the modulus (e.g. if m is a power of 2, then c must be odd), so the value c=1 is commonly chosen.
The sequence produced by other choices of c can be written as a simple function of the sequence when c=1.: 11   Specifically, if Y is the prototypical sequence defined by Y0 = 0 and Yn+1 = aYn + 1 mod m, then a general sequence Xn+1 = aXn + c mod m can be written as an affine function of Y:

  
    
      
        
          X
          
            n
          
        
        =
        (
        
          X
          
            0
          
        
        (
        a
        −
        1
        )
        +
        c
        )
        
          Y
          
            n
          
        
        +
        
          X
          
            0
          
        
        =
        (
        
          X
          
            1
          
        
        −
        
          X
          
            0
          
        
        )
        
          Y
          
            n
          
        
        +
        
          X
          
            0
          
        
        
          
          (
          mod
          
          m
          )
        
        .
      
    
    {\displaystyle X_{n}=(X_{0}(a-1)+c)Y_{n}+X_{0}=(X_{1}-X_{0})Y_{n}+X_{0}{\pmod {m}}.}
  

More generally, any two sequences X and Z with the same multiplier and modulus are related by

  
    
      
        
          
            
              
                X
                
                  n
                
              
              −
              
                X
                
                  0
                
              
            
            
              
                X
                
                  1
                
              
              −
              
                X
                
                  0
                
              
            
          
        
        =
        
          Y
          
            n
          
        
        =
        
          
            
              
                a
                
                  n
                
              
              −
              1
            
            
              a
              −
              1
            
          
        
        =
        
          
            
              
                Z
                
                  n
                
              
              −
              
                Z
                
                  0
                
              
            
            
              
                Z
                
                  1
                
              
              −
              
                Z
                
                  0
                
              
            
          
        
        
          
          (
          mod
          
          m
          )
        
        .
      
    
    {\displaystyle {X_{n}-X_{0} \over X_{1}-X_{0}}=Y_{n}={a^{n}-1 \over a-1}={Z_{n}-Z_{0} \over Z_{1}-Z_{0}}{\pmod {m}}.}
  

In the common case where m is a power of 2 and a ≡ 5 (mod 8) (a desirable property for other reasons), it is always possible to find an initial value X0 so that the denominator X1 − X0 ≡ ±1 (mod m), producing an even simpler relationship.  With this choice of X0, Xn = X0 ± Yn will remain true for all n.: 10-11  The sign is determined by c ≡ ±1 (mod 4), and the constant X0 is determined by 1 ∓ c ≡ (1 − a)X0 (mod m).
As a simple example, consider the generators Xn+1 = 157Xn + 3 mod 256 and Yn+1 = 157Yn + 1 mod 256; i.e. m = 256, a = 157, and c = 3.  Because 3 ≡ −1 (mod 4), we are searching for a solution to 1 + 3 ≡ (1 − 157)X0 (mod 256).  This is satisfied by X0 ≡ 41 (mod 64), so if we start with that, then Xn ≡ X0 − Yn (mod 256) for all n.
For example, using X0 = 233 = 3×64 + 41:

X = 233, 232, 75, 2, 61, 108, ...
Y = 0, 1, 158, 231, 172, 125, ...
X + Y mod 256 = 233, 233, 233, 233, 233, 233, ...

Parameters in common use
The following table lists the parameters of LCGs in common use, including built-in rand() functions in runtime libraries of various compilers.  This table is to show popularity, not examples to emulate; many of these parameters are poor.  Tables of good parameters are available.

As shown above, LCGs do not always use all of the bits in the values they produce.  In general, they return the most significant bits.  For example, the Java implementation operates with 48-bit values at each iteration but returns only their 32 most significant bits. This is because the higher-order bits have longer periods than the lower-order bits (see below). LCGs that use this truncation technique produce statistically better values than those that do not. This is especially noticeable in scripts that use the mod operation to reduce range; modifying the random number mod 2 will lead to alternating 0 and 1 without truncation.
Contrarily, some libraries use an implicit power-of-two modulus but never output or otherwise use the most significant bit, in order to limit the output to positive two's complement integers.  The output is as if the modulus were one bit less than the internal word size, and such generators are described as such in the table above.

Advantages and disadvantages
LCGs are fast and require minimal memory (one modulo-m number, often 32 or 64 bits) to retain state. This makes them valuable for simulating multiple independent streams.  LCGs are not intended, and must not be used, for cryptographic applications; use a cryptographically secure pseudorandom number generator for such applications.

Although LCGs have a few specific weaknesses, many of their flaws come from having too small a state. The fact that people have been lulled for so many years into using them with such small moduli can be seen as a testament to the strength of the technique. A LCG with large enough state can pass even stringent statistical tests; a modulo-264 LCG which returns the high 32 bits passes TestU01's SmallCrush suite, and a 96-bit LCG passes the most stringent BigCrush suite.
For a specific example, an ideal random number generator with 32 bits of output is expected (by the Birthday theorem) to begin duplicating earlier outputs after √m ≈ 216 results. Any PRNG whose output is its full, untruncated state will not produce duplicates until its full period elapses, an easily detectable statistical flaw.
For related reasons, any PRNG should have a period longer than the square of the number of outputs required. Given modern computer speeds, this means a period of 264 for all but the least demanding applications, and longer for demanding simulations.
One flaw specific to LCGs is that, if used to choose points in an n-dimensional space, the points will lie on, at most, n√n!⋅m hyperplanes (Marsaglia's theorem, developed by George Marsaglia). This is due to serial correlation between successive values of the sequence Xn. Carelessly chosen multipliers will usually have far fewer, widely spaced planes, which can lead to problems. The spectral test, which is a simple test of an LCG's quality, measures this spacing and allows a good multiplier to be chosen.
The plane spacing depends both on the modulus and the multiplier. A large enough modulus can reduce this distance below the resolution of double precision numbers. The choice of the multiplier becomes less important when the modulus is large. It is still necessary to calculate the spectral index and make sure that the multiplier is not a bad one, but purely probabilistically it becomes extremely unlikely to encounter a bad multiplier when the modulus is larger than about 264.
Another flaw specific to LCGs is the short period of the low-order bits when m is chosen to be a power of 2. This can be mitigated by using a modulus larger than the required output, and using the most significant bits of the state.
Nevertheless, for some applications LCGs may be a good option. For instance, in an embedded system, the amount of memory available is often severely limited. Similarly, in an environment such as a video game console taking a small number of high-order bits of an LCG may well suffice.  (The low-order bits of LCGs when m is a power of 2 should never be relied on for any degree of randomness whatsoever.)  The low order bits go through very short cycles.  In particular, any full-cycle LCG, when m is a power of 2, will produce alternately odd and even results.
LCGs should be evaluated very carefully for suitability in non-cryptographic applications where high-quality randomness is critical. For Monte Carlo simulations, an LCG must use a modulus greater and preferably much greater than the cube of the number of random samples which are required. This means, for example, that a (good) 32-bit LCG can be used to obtain about a thousand random numbers; a 64-bit LCG is good for about 221 random samples (a little over two million), etc. For this reason, in practice LCGs are not suitable for large-scale Monte Carlo simulations.

Sample code
Python code
The following is an implementation of an LCG in Python, in the form of a generator:

Haskell code
The following is an implementation of an LCG in Haskell utilizing a lazy evaluation strategy to generate an infinite stream of output values in a list:

Free Pascal
Free Pascal uses a Mersenne Twister as its default pseudo random number generator whereas Delphi uses a LCG. Here is a Delphi compatible example in Free Pascal based on the information in the table above. Given the same RandSeed value it generates the same sequence of random numbers as Delphi.

Like all pseudorandom number generators, a LCG needs to store state and alter it each time it generates a new number. Multiple threads may access this state simultaneously causing a race condition. Implementations should use different state each with unique initialization for different threads to avoid equal sequences of random numbers on simultaneously executing threads.

LCG derivatives
There are several generators which are linear congruential generators in a different form, and thus the techniques used to analyze LCGs can be applied to them.
One method of producing a longer period is to sum the outputs of several LCGs of different periods having a large least common multiple; the Wichmann–Hill generator is an example of this form. (We would prefer them to be completely coprime, but a prime modulus implies an even period, so there must be a common factor of 2, at least.) This can be shown to be equivalent to a single LCG with a modulus equal to the product of the component LCG moduli.
Marsaglia's add-with-carry and subtract-with-borrow PRNGs with a word size of b=2w and lags r and s (r > s) are equivalent to LCGs with a modulus of br ± bs ± 1.
Multiply-with-carry PRNGs with a multiplier of a are equivalent to LCGs with a large prime modulus of abr−1 and a power-of-2 multiplier b.
A permuted congruential generator begins with a power-of-2-modulus LCG and applies an output transformation to eliminate the short period problem in the low-order bits.

Comparison with other PRNGs
The other widely used primitive for obtaining long-period pseudorandom sequences is the linear-feedback shift register construction, which is based on arithmetic in GF(2)[x], the polynomial ring over GF(2).  Rather than integer addition and multiplication, the basic operations are exclusive-or and carry-less multiplication, which is usually implemented as a sequence of logical shifts.  These have the advantage that all of their bits are full-period; they do not suffer from the weakness in the low-order bits that plagues arithmetic modulo 2k.
Examples of this family include xorshift generators and the Mersenne twister.  The latter provides a very long period (219937−1) and variate uniformity, but it fails some statistical tests.  Lagged Fibonacci generators also fall into this category; although they use arithmetic addition, their period is ensured by an LFSR among the least-significant bits.
It is easy to detect the structure of a linear-feedback shift register with appropriate tests such as the linear complexity test implemented in the TestU01 suite; a Boolean circulant matrix initialized from consecutive bits of an LFSR will never have rank greater than the degree of the polynomial.  Adding a non-linear output mixing function (as in the xoshiro256** and permuted congruential generator constructions) can greatly improve the performance on statistical tests.
Another structure for a PRNG is a very simple recurrence function combined with a powerful output mixing function.  This includes counter mode block ciphers and non-cryptographic generators such as SplitMix64.
A structure similar to LCGs, but not equivalent, is the multiple-recursive generator: Xn = (a1Xn−1 + a2Xn−2 + ··· + akXn−k) mod m for k ≥ 2.  With a prime modulus, this can generate periods up to mk−1, so is a useful extension of the LCG structure to larger periods.
A powerful technique for generating high-quality pseudorandom numbers is to combine two or more PRNGs of different structure; the sum of an LFSR and an LCG (as in the KISS or xorwow constructions) can do very well at some cost in speed.

See also
List of random number generators – other PRNGs including some with better statistical qualitites
ACORN generator – not to be confused with ACG which term appears to have been used for variants of LCG and LFSR generators
Permuted congruential generator
Full cycle
Inversive congruential generator
Multiply-with-carry
Lehmer RNG (sometimes called the Park–Miller RNG)
Combined linear congruential generator

Notes
References
Press, WH; Teukolsky, SA; Vetterling, WT; Flannery, BP (2007), "Section 7.1.1. Some History", Numerical Recipes: The Art of Scientific Computing (3rd ed.), New York: Cambridge University Press, ISBN 978-0-521-88068-8, archived from the original on 2011-08-11, retrieved 2011-08-10
Gentle, James E., (2003). Random Number Generation and Monte Carlo Methods, 2nd edition, Springer, ISBN 0-387-00178-6.
Joan Boyar (1989). "Inferring sequences produced by pseudo-random number generators" (PDF). Journal of the ACM. 36 (1): 129–141. doi:10.1145/58562.59305. S2CID 3565772. (in this paper, efficient algorithms are given for inferring sequences produced by certain pseudo-random number generators).

External links
The simulation Linear Congruential Generator visualizes the correlations between the pseudo-random numbers when manipulating the parameters.
Security of Random Number Generation: An Annotated Bibliography
Linear Congruential Generators post to sci.math
The "Death of Art" computer art project at Goldstein Technologies LLC, uses an LCG to generate 33,554,432 images
P. L'Ecuyer and R. Simard, "TestU01: A C Library for Empirical Testing of Random Number Generators", May 2006, revised November 2006, ACM Transactions on Mathematical Software, 33, 4, Article 22, August 2007.
Article about another way of cracking LCG

## Related Articles

### Internal Links

- [ACORN (random number generator)](https://en.wikipedia.org/wiki/ACORN_(random_number_generator))
- [ANSI C](https://en.wikipedia.org/wiki/ANSI_C)
- [Affine transformation](https://en.wikipedia.org/wiki/Affine_transformation)
- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [As-if rule](https://en.wikipedia.org/wiki/As-if_rule)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Birthday problem](https://en.wikipedia.org/wiki/Birthday_problem)
- [Borland](https://en.wikipedia.org/wiki/Borland)
- [Delphi (software)](https://en.wikipedia.org/wiki/Delphi_(software))
- [C++11](https://en.wikipedia.org/wiki/C%2B%2B11)
- [C11 (C standard revision)](https://en.wikipedia.org/wiki/C11_(C_standard_revision))
- [C17 (C standard revision)](https://en.wikipedia.org/wiki/C17_(C_standard_revision))
- [ANSI C](https://en.wikipedia.org/wiki/ANSI_C)
- [C99](https://en.wikipedia.org/wiki/C99)
- [Carbon (API)](https://en.wikipedia.org/wiki/Carbon_(API))
- [Carry-less product](https://en.wikipedia.org/wiki/Carry-less_product)
- [Cc65](https://en.wikipedia.org/wiki/Cc65)
- [Circulant matrix](https://en.wikipedia.org/wiki/Circulant_matrix)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [CodeWarrior](https://en.wikipedia.org/wiki/CodeWarrior)
- [Combined linear congruential generator](https://en.wikipedia.org/wiki/Combined_linear_congruential_generator)
- [Communications of the ACM](https://en.wikipedia.org/wiki/Communications_of_the_ACM)
- [Compiler](https://en.wikipedia.org/wiki/Compiler)
- [Coprime integers](https://en.wikipedia.org/wiki/Coprime_integers)
- [Block cipher mode of operation](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation)
- [Cryptographically secure pseudorandom number generator](https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator)
- [Digital Mars](https://en.wikipedia.org/wiki/Digital_Mars)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Donald Knuth](https://en.wikipedia.org/wiki/Donald_Knuth)
- [List of Latin phrases (E)](https://en.wikipedia.org/wiki/List_of_Latin_phrases_(E))
- [Exclusive or](https://en.wikipedia.org/wiki/Exclusive_or)
- [Free Pascal](https://en.wikipedia.org/wiki/Free_Pascal)
- [Full cycle](https://en.wikipedia.org/wiki/Full_cycle)
- [GF(2)](https://en.wikipedia.org/wiki/GF(2))
- [GNU Compiler Collection](https://en.wikipedia.org/wiki/GNU_Compiler_Collection)
- [Generator (computer programming)](https://en.wikipedia.org/wiki/Generator_(computer_programming))
- [George Marsaglia](https://en.wikipedia.org/wiki/George_Marsaglia)
- [Glibc](https://en.wikipedia.org/wiki/Glibc)
- [Guy L. Steele Jr.](https://en.wikipedia.org/wiki/Guy_L._Steele_Jr.)
- [Harvey Mudd College](https://en.wikipedia.org/wiki/Harvey_Mudd_College)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Handle System](https://en.wikipedia.org/wiki/Handle_System)
- [Hyperplane](https://en.wikipedia.org/wiki/Hyperplane)
- [Hyperplane](https://en.wikipedia.org/wiki/Hyperplane)
- [VisualAge](https://en.wikipedia.org/wiki/VisualAge)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [If and only if](https://en.wikipedia.org/wiki/If_and_only_if)
- [Integer](https://en.wikipedia.org/wiki/Integer)
- [Internet Engineering Task Force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force)
- [Inversive congruential generator](https://en.wikipedia.org/wiki/Inversive_congruential_generator)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Joan Boyar](https://en.wikipedia.org/wiki/Joan_Boyar)
- [Journal of the ACM](https://en.wikipedia.org/wiki/Journal_of_the_ACM)
- [KISS (algorithm)](https://en.wikipedia.org/wiki/KISS_(algorithm))
- [Lagged Fibonacci generator](https://en.wikipedia.org/wiki/Lagged_Fibonacci_generator)
- [Lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation)
- [Least common multiple](https://en.wikipedia.org/wiki/Least_common_multiple)
- [Lehmer random number generator](https://en.wikipedia.org/wiki/Lehmer_random_number_generator)
- [Lehmer random number generator](https://en.wikipedia.org/wiki/Lehmer_random_number_generator)
- [Linear-feedback shift register](https://en.wikipedia.org/wiki/Linear-feedback_shift_register)
- [Linear map](https://en.wikipedia.org/wiki/Linear_map)
- [List of random number generators](https://en.wikipedia.org/wiki/List_of_random_number_generators)
- [Logical shift](https://en.wikipedia.org/wiki/Logical_shift)
- [Lehmer random number generator](https://en.wikipedia.org/wiki/Lehmer_random_number_generator)
- [MMIX](https://en.wikipedia.org/wiki/MMIX)
- [Marsaglia's theorem](https://en.wikipedia.org/wiki/Marsaglia%27s_theorem)
- [Mathematics of Computation](https://en.wikipedia.org/wiki/Mathematics_of_Computation)
- [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister)
- [Mersenne prime](https://en.wikipedia.org/wiki/Mersenne_prime)
- [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister)
- [Modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic)
- [Modulo](https://en.wikipedia.org/wiki/Modulo)
- [Multiply-with-carry pseudorandom number generator](https://en.wikipedia.org/wiki/Multiply-with-carry_pseudorandom_number_generator)
- [Musl](https://en.wikipedia.org/wiki/Musl)
- [Windows Native API](https://en.wikipedia.org/wiki/Windows_Native_API)
- [Neil Gershenfeld](https://en.wikipedia.org/wiki/Neil_Gershenfeld)
- [Newlib](https://en.wikipedia.org/wiki/Newlib)
- [Numerical Recipes](https://en.wikipedia.org/wiki/Numerical_Recipes)
- [OpenVMS](https://en.wikipedia.org/wiki/OpenVMS)
- [Operations Research Letters](https://en.wikipedia.org/wiki/Operations_Research_Letters)
- [PubMed Central](https://en.wikipedia.org/wiki/PubMed_Central)
- [PubMed](https://en.wikipedia.org/wiki/PubMed)
- [Proceedings of the National Academy of Sciences of the United States of America](https://en.wikipedia.org/wiki/Proceedings_of_the_National_Academy_of_Sciences_of_the_United_States_of_America)
- [POSIX](https://en.wikipedia.org/wiki/POSIX)
- [Permuted congruential generator](https://en.wikipedia.org/wiki/Permuted_congruential_generator)
- [Piecewise linear function](https://en.wikipedia.org/wiki/Piecewise_linear_function)
- [Polynomial ring](https://en.wikipedia.org/wiki/Polynomial_ring)
- [Power of two](https://en.wikipedia.org/wiki/Power_of_two)
- [Prime number](https://en.wikipedia.org/wiki/Prime_number)
- [Primitive element (finite field)](https://en.wikipedia.org/wiki/Primitive_element_(finite_field))
- [Pseudorandom number generator](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)
- [Pseudorandomness](https://en.wikipedia.org/wiki/Pseudorandomness)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [RANDU](https://en.wikipedia.org/wiki/RANDU)
- [Randomness](https://en.wikipedia.org/wiki/Randomness)
- [Rank (linear algebra)](https://en.wikipedia.org/wiki/Rank_(linear_algebra))
- [Recurrence relation](https://en.wikipedia.org/wiki/Recurrence_relation)
- [Request for Comments](https://en.wikipedia.org/wiki/Request_for_Comments)
- [Runtime library](https://en.wikipedia.org/wiki/Runtime_library)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Sebastiano Vigna](https://en.wikipedia.org/wiki/Sebastiano_Vigna)
- [Sequence](https://en.wikipedia.org/wiki/Sequence)
- [Spectral test](https://en.wikipedia.org/wiki/Spectral_test)
- [Square-free integer](https://en.wikipedia.org/wiki/Square-free_integer)
- [C standard library](https://en.wikipedia.org/wiki/C_standard_library)
- [Subtract with carry](https://en.wikipedia.org/wiki/Subtract_with_carry)
- [TestU01](https://en.wikipedia.org/wiki/TestU01)
- [Randomness test](https://en.wikipedia.org/wiki/Randomness_test)
- [The Art of Computer Programming](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming)
- [Turbo Pascal](https://en.wikipedia.org/wiki/Turbo_Pascal)
- [Two's complement](https://en.wikipedia.org/wiki/Two%27s_complement)
- [Video game console](https://en.wikipedia.org/wiki/Video_game_console)
- [Virtual Pascal](https://en.wikipedia.org/wiki/Virtual_Pascal)
- [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic)
- [Microsoft Visual C++](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B)
- [Watcom C/C++](https://en.wikipedia.org/wiki/Watcom_C/C%2B%2B)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Weyl sequence](https://en.wikipedia.org/wiki/Weyl_sequence)
- [Wichmann–Hill](https://en.wikipedia.org/wiki/Wichmann%E2%80%93Hill)
- [Windows Vista](https://en.wikipedia.org/wiki/Windows_Vista)
- [Word (computer architecture)](https://en.wikipedia.org/wiki/Word_(computer_architecture))
- [Xorshift](https://en.wikipedia.org/wiki/Xorshift)
- [ZX81](https://en.wikipedia.org/wiki/ZX81)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from July 2021](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_July_2021)
- [Category:Articles with unsourced statements from November 2017](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_November_2017)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:33:57.778667+00:00_