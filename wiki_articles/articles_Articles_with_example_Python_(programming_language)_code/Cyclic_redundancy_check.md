# Cyclic redundancy check

## Article Metadata

- **Last Updated:** 2024-12-14T19:36:15.530776+00:00
- **Original Article:** [Cyclic redundancy check](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)
- **Language:** en
- **Page ID:** 38838

## Summary

A cyclic redundancy check (CRC) is an error-detecting code commonly used in digital networks and storage devices to detect accidental changes to digital data.  Blocks of data entering these systems get a short check value attached, based on the remainder of a polynomial division of their contents. On retrieval, the calculation is repeated and, in the event the check values do not match, corrective action can be taken against data corruption. CRCs can be used for error correction (see bitfilters)

## Categories

- Category:All articles needing additional references
- Category:All articles with unsourced statements
- Category:Articles needing additional references from July 2016
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from January 2024
- Category:Binary arithmetic
- Category:Cyclic redundancy checks
- Category:Finite fields
- Category:Polynomials
- Category:Short description is different from Wikidata
- Category:Use dmy dates from October 2023
- Category:Webarchive template wayback links
- Category:Wikipedia articles with ASCII art

## Table of Contents

- Introduction
- Application
- Data integrity
- Computation
- Mathematics
- Specification
- Obfuscation
- Standards and common use
- Polynomial representations
- See also
- References
- Further reading
- External links

## Content

A cyclic redundancy check (CRC) is an error-detecting code commonly used in digital networks and storage devices to detect accidental changes to digital data.  Blocks of data entering these systems get a short check value attached, based on the remainder of a polynomial division of their contents. On retrieval, the calculation is repeated and, in the event the check values do not match, corrective action can be taken against data corruption. CRCs can be used for error correction (see bitfilters).
CRCs are so called because the check (data verification) value is a redundancy (it expands the message without adding information) and the algorithm is based on cyclic codes. CRCs are popular because they are simple to implement in binary hardware, easy to analyze mathematically, and particularly good at detecting common errors caused by noise in transmission channels.  Because the check value has a fixed length, the function that generates it is occasionally used as a hash function.

Introduction
CRCs are based on the theory of cyclic error-correcting codes. The use of systematic cyclic codes, which encode messages by adding a fixed-length check value, for the purpose of error detection in communication networks, was first proposed by W. Wesley Peterson in 1961.
Cyclic codes are not only simple to implement but have the benefit of being particularly well suited for the detection of burst errors: contiguous sequences of erroneous data symbols in messages. This is important because burst errors are common transmission errors in many communication channels, including magnetic and optical storage devices. Typically an n-bit CRC applied to a data block of arbitrary length will detect any single error burst not longer than n bits, and the fraction of all longer error bursts that it will detect is approximately (1 − 2−n).
Specification of a CRC code requires definition of a so-called generator polynomial. This polynomial becomes the divisor in a polynomial long division, which takes the message as the dividend and in which the quotient is discarded and the remainder becomes the result.  The important caveat is that the polynomial coefficients are calculated according to the arithmetic of a finite field, so the addition operation can always be performed bitwise-parallel (there is no carry between digits).
In practice, all commonly used CRCs employ the finite field of two elements, GF(2). The two elements are usually called 0 and 1, comfortably matching computer architecture.
A CRC is called an n-bit CRC when its check value is n bits long. For a given n, multiple CRCs are possible, each with a different polynomial. Such a polynomial has highest degree n, which means it has n + 1 terms. In other words, the polynomial has a length of n + 1; its encoding requires n + 1 bits. Note that most polynomial specifications either drop the MSb or LSb, since they are always 1. The CRC and associated polynomial typically have a name of the form CRC-n-XXX as in the table below.
The simplest error-detection system, the parity bit, is in fact a 1-bit CRC: it uses the generator polynomial x + 1 (two terms), and has the name CRC-1.

Application
A CRC-enabled device calculates a short, fixed-length binary sequence, known as the check value or CRC, for each block of data to be sent or stored and appends it to the data, forming a codeword.
When a codeword is received or read, the device either compares its check value with one freshly calculated from the data block, or equivalently, performs a CRC on the whole codeword and compares the resulting check value with an expected residue constant.
If the CRC values do not match, then the block contains a data error.
The device may take corrective action, such as rereading the block or requesting that it be sent again. Otherwise, the data is assumed to be error-free (though, with some small probability, it may contain undetected errors; this is inherent in the nature of error-checking).

Data integrity
CRCs are specifically designed to protect against common types of errors on communication channels, where they can provide quick and reasonable assurance of the integrity of messages delivered. However, they are not suitable for protecting against intentional alteration of data.
Firstly, as there is no authentication, an attacker can edit a message and recompute the CRC without the substitution being detected. When stored alongside the data, CRCs and cryptographic hash functions by themselves do not protect against intentional modification of data. Any application that requires protection against such attacks must use cryptographic authentication mechanisms, such as message authentication codes or digital signatures (which are commonly based on cryptographic hash functions).
Secondly, unlike cryptographic hash functions, CRC is an easily reversible function, which makes it unsuitable for use in digital signatures.
Thirdly, CRC satisfies a relation similar to that of a linear function (or more accurately, an affine function):

  
    
      
        CRC
        ⁡
        (
        x
        ⊕
        y
        )
        =
        CRC
        ⁡
        (
        x
        )
        ⊕
        CRC
        ⁡
        (
        y
        )
        ⊕
        c
      
    
    {\displaystyle \operatorname {CRC} (x\oplus y)=\operatorname {CRC} (x)\oplus \operatorname {CRC} (y)\oplus c}
  

where 
  
    
      
        c
      
    
    {\displaystyle c}
  
 depends on the length of 
  
    
      
        x
      
    
    {\displaystyle x}
  
 and 
  
    
      
        y
      
    
    {\displaystyle y}
  
. This can be also stated as follows, where 
  
    
      
        x
      
    
    {\displaystyle x}
  
, 
  
    
      
        y
      
    
    {\displaystyle y}
  
 and 
  
    
      
        z
      
    
    {\displaystyle z}
  
 have the same length

  
    
      
        CRC
        ⁡
        (
        x
        ⊕
        y
        ⊕
        z
        )
        =
        CRC
        ⁡
        (
        x
        )
        ⊕
        CRC
        ⁡
        (
        y
        )
        ⊕
        CRC
        ⁡
        (
        z
        )
        ;
      
    
    {\displaystyle \operatorname {CRC} (x\oplus y\oplus z)=\operatorname {CRC} (x)\oplus \operatorname {CRC} (y)\oplus \operatorname {CRC} (z);}
  

as a result, even if the CRC is encrypted with a stream cipher that uses XOR as its combining operation (or mode of block cipher which effectively turns it into a stream cipher, such as OFB or CFB), both the message and the associated CRC can be manipulated without knowledge of the encryption key; this was one of the well-known design flaws of the Wired Equivalent Privacy (WEP) protocol.

Computation
To compute an n-bit binary CRC, line the bits representing the input in a row, and position the (n + 1)-bit pattern representing the CRC's divisor (called a "polynomial") underneath the left end of the row.
In this example, we shall encode 14 bits of message with a 3-bit CRC, with a polynomial x3 + x + 1. The polynomial is written in binary as the coefficients; a 3rd-degree polynomial has 4 coefficients (1x3 + 0x2 + 1x + 1). In this case, the coefficients are 1, 0, 1 and 1.  The result of the calculation is 3 bits long, which is why it is called a 3-bit CRC. However, you need 4 bits to explicitly state the polynomial.
Start with the message to be encoded:

11010011101100

This is first padded with zeros corresponding to the bit length n of the CRC. This is done so that the resulting code word is in systematic form. Here is the first calculation for computing a 3-bit CRC:

11010011101100 000 <--- input right padded by 3 bits
1011               <--- divisor (4 bits) = x³ + x + 1
------------------
01100011101100 000 <--- result

The algorithm acts on the bits directly above the divisor in each step.  The result for that iteration is the bitwise XOR of the polynomial divisor with the bits above it.  The bits not above the divisor are simply copied directly below for that step.  The divisor is then shifted right to align with the highest remaining 1 bit in the input, and the process is repeated until the divisor reaches the right-hand end of the input row. Here is the entire calculation:

11010011101100 000 <--- input right padded by 3 bits
1011               <--- divisor
01100011101100 000 <--- result (note the first four bits are the XOR with the divisor beneath, the rest of the bits are unchanged)
 1011              <--- divisor ...
00111011101100 000
  1011
00010111101100 000
   1011
00000001101100 000 <--- note that the divisor moves over to align with the next 1 in the dividend (since quotient for that step was zero)
       1011             (in other words, it doesn't necessarily move one bit per iteration)
00000000110100 000
        1011
00000000011000 000
         1011
00000000001110 000
          1011
00000000000101 000
           101 1
-----------------
00000000000000 100 <--- remainder (3 bits).  Division algorithm stops here as dividend is equal to zero.

Since the leftmost divisor bit zeroed every input bit it touched, when this process ends the only bits in the input row that can be nonzero are the n bits at the right-hand end of the row. These n bits are the remainder of the division step, and will also be the value of the CRC function (unless the chosen CRC specification calls for some postprocessing).
The validity of a received message can easily be verified by performing the above calculation again, this time with the check value added instead of zeroes. The remainder should equal zero if there are no detectable errors.

11010011101100 100 <--- input with check value
1011               <--- divisor
01100011101100 100 <--- result
 1011              <--- divisor ...
00111011101100 100

......

00000000001110 100
          1011
00000000000101 100
           101 1
------------------
00000000000000 000 <--- remainder

The following Python code outlines a function which will return the initial CRC remainder for a chosen input and polynomial, with either 1 or 0 as the initial padding. Note that this code works with string inputs rather than raw numbers:

Mathematics
Mathematical analysis of this division-like process reveals how to select a divisor that guarantees good error-detection properties. In this analysis, the digits of the bit strings are taken as the coefficients of a polynomial in some variable x—coefficients that are elements of the finite field GF(2) (the integers modulo 2, i.e. either a zero or a one), instead of more familiar numbers. The set of binary polynomials is a mathematical ring.

Designing polynomials
The selection of the generator polynomial is the most important part of implementing the CRC algorithm. The polynomial must be chosen to maximize the error-detecting capabilities while minimizing overall collision probabilities.
The most important attribute of the polynomial is its length (largest degree(exponent) +1 of any one term in the polynomial), because of its direct influence on the length of the computed check value.
The most commonly used polynomial lengths are 9 bits (CRC-8), 17 bits (CRC-16), 33 bits (CRC-32), and 65 bits (CRC-64).
A CRC is called an n-bit CRC when its check value is n-bits. For a given n, multiple CRCs are possible, each with a different polynomial. Such a polynomial has highest degree n, and hence n + 1 terms (the polynomial has a length of n + 1). The remainder has length n. The CRC has a name of the form CRC-n-XXX.
The design of the CRC polynomial depends on the maximum total length of the block to be protected (data + CRC bits), the desired error protection features, and the type of resources for implementing the CRC, as well as the desired performance. A common misconception is that the "best" CRC polynomials are derived from either irreducible polynomials or irreducible polynomials times the factor 1 + x, which adds to the code the ability to detect all errors affecting an odd number of bits. In reality, all the factors described above should enter into the selection of the polynomial and may lead to a reducible polynomial. However, choosing a reducible polynomial will result in a certain proportion of missed errors, due to the quotient ring having zero divisors.
The advantage of choosing a primitive polynomial as the generator for a CRC code is that the resulting code has maximal total block length in the sense that all 1-bit errors within that block length have different remainders (also called syndromes) and therefore, since the remainder is a linear function of the block, the code can detect all 2-bit errors within that block length. If 
  
    
      
        r
      
    
    {\displaystyle r}
  
 is the degree of the primitive generator polynomial, then the maximal total block length is 
  
    
      
        
          2
          
            r
          
        
        −
        1
      
    
    {\displaystyle 2^{r}-1}
  
, and the associated code is able to detect any single-bit or double-bit errors. We can improve this situation. If we use the generator polynomial 
  
    
      
        g
        (
        x
        )
        =
        p
        (
        x
        )
        (
        1
        +
        x
        )
      
    
    {\displaystyle g(x)=p(x)(1+x)}
  
, where 
  
    
      
        p
      
    
    {\displaystyle p}
  
 is a primitive polynomial of degree 
  
    
      
        r
        −
        1
      
    
    {\displaystyle r-1}
  
, then the maximal total block length is 
  
    
      
        
          2
          
            r
            −
            1
          
        
        −
        1
      
    
    {\displaystyle 2^{r-1}-1}
  
, and the code is able to detect single, double, triple and any odd number of errors.
A polynomial 
  
    
      
        g
        (
        x
        )
      
    
    {\displaystyle g(x)}
  
 that admits other factorizations may be chosen then so as to balance the maximal total blocklength with a desired error detection power. The BCH codes are a powerful class of such polynomials. They subsume the two examples above. Regardless of the reducibility properties of a generator polynomial of degree r, if it includes the "+1" term, the code will be able to detect error patterns that are confined to a window of r contiguous bits. These patterns are called "error bursts".

Specification
The concept of the CRC as an error-detecting code gets complicated when an implementer or standards committee uses it to design a practical system. Here are some of the complications:

Sometimes an implementation prefixes a fixed bit pattern to the bitstream to be checked. This is useful when clocking errors might insert 0-bits in front of a message, an alteration that would otherwise leave the check value unchanged.
Usually, but not always, an implementation appends n 0-bits (n being the size of the CRC) to the bitstream to be checked before the polynomial division occurs. Such appending is explicitly demonstrated in the Computation of CRC article. This has the convenience that the remainder of the original bitstream with the check value appended is exactly zero, so the CRC can be checked simply by performing the polynomial division on the received bitstream and comparing the remainder with zero. Due to the associative and commutative properties of the exclusive-or operation, practical table driven implementations can obtain a result numerically equivalent to zero-appending without explicitly appending any zeroes, by using an equivalent, faster algorithm that combines the message bitstream with the stream being shifted out of the CRC register.
Sometimes an implementation exclusive-ORs a fixed bit pattern into the remainder of the polynomial division.
Bit order: Some schemes view the low-order bit of each byte as "first", which then during polynomial division means "leftmost", which is contrary to our customary understanding of "low-order". This convention makes sense when serial-port transmissions are CRC-checked in hardware, because some widespread serial-port transmission conventions transmit bytes least-significant bit first.
Byte order: With multi-byte CRCs, there can be confusion over whether the byte transmitted first (or stored in the lowest-addressed byte of memory) is the least-significant byte (LSB) or the most-significant byte (MSB). For example, some 16-bit CRC schemes swap the bytes of the check value.
Omission of the high-order bit of the divisor polynomial: Since the high-order bit is always 1, and since an n-bit CRC must be defined by an (n + 1)-bit divisor which overflows an n-bit register, some writers assume that it is unnecessary to mention the divisor's high-order bit.
Omission of the low-order bit of the divisor polynomial: Since the low-order bit is always 1, authors such as Philip Koopman represent polynomials with their high-order bit intact, but without the low-order bit (the 
  
    
      
        
          x
          
            0
          
        
      
    
    {\displaystyle x^{0}}
  
 or 1 term).  This convention encodes the polynomial complete with its degree in one integer.
These complications mean that there are three common ways to express a polynomial as an integer: the first two, which are mirror images in binary, are the constants found in code; the third is the number found in Koopman's papers.  In each case, one term is omitted. So the polynomial 
  
    
      
        
          x
          
            4
          
        
        +
        x
        +
        1
      
    
    {\displaystyle x^{4}+x+1}
  
 may be transcribed as:

0x3 = 0b0011, representing 
  
    
      
        
          x
          
            4
          
        
        +
        (
        0
        
          x
          
            3
          
        
        +
        0
        
          x
          
            2
          
        
        +
        1
        
          x
          
            1
          
        
        +
        1
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle x^{4}+(0x^{3}+0x^{2}+1x^{1}+1x^{0})}
  
 (MSB-first code)
0xC = 0b1100, representing 
  
    
      
        (
        1
        
          x
          
            0
          
        
        +
        1
        
          x
          
            1
          
        
        +
        0
        
          x
          
            2
          
        
        +
        0
        
          x
          
            3
          
        
        )
        +
        
          x
          
            4
          
        
      
    
    {\displaystyle (1x^{0}+1x^{1}+0x^{2}+0x^{3})+x^{4}}
  
 (LSB-first code)
0x9 = 0b1001, representing 
  
    
      
        (
        1
        
          x
          
            4
          
        
        +
        0
        
          x
          
            3
          
        
        +
        0
        
          x
          
            2
          
        
        +
        1
        
          x
          
            1
          
        
        )
        +
        
          x
          
            0
          
        
      
    
    {\displaystyle (1x^{4}+0x^{3}+0x^{2}+1x^{1})+x^{0}}
  
 (Koopman notation)
In the table below they are shown as:

Obfuscation
CRCs in proprietary protocols might be obfuscated by using a non-trivial initial value and a final XOR, but these techniques do not add cryptographic strength to the algorithm and can be reverse engineered using straightforward methods.

Standards and common use
Numerous varieties of cyclic redundancy checks have been incorporated into technical standards.  By no means does one algorithm, or one of each degree, suit every purpose; Koopman and Chakravarty recommend selecting a polynomial according to the application requirements and the expected distribution of message lengths. The number of distinct CRCs in use has confused developers, a situation which authors have sought to address. There are three polynomials reported for CRC-12, twenty-two conflicting definitions of CRC-16, and seven of CRC-32.
The polynomials commonly applied are not the most efficient ones possible. Since 1993, Koopman, Castagnoli and others have surveyed the space of polynomials between 3 and 64 bits in size, finding examples that have much better performance (in terms of Hamming distance for a given message size) than the polynomials of earlier protocols, and publishing the best of these with the aim of improving the error detection capacity of future standards. In particular, iSCSI and SCTP have adopted one of the findings of this research, the CRC-32C (Castagnoli) polynomial.
The design of the 32-bit polynomial most commonly used by standards bodies, CRC-32-IEEE, was the result of a joint effort for the Rome Laboratory and the Air Force Electronic Systems Division by Joseph Hammond, James Brown and Shyan-Shiang Liu of the Georgia Institute of Technology and Kenneth Brayer of the Mitre Corporation. The earliest known appearances of the 32-bit polynomial were in their 1975 publications: Technical Report 2956 by Brayer for Mitre, published in January and released for public dissemination through DTIC in August, and Hammond, Brown and Liu's report for the Rome Laboratory, published in May. Both reports contained contributions from the other team. During December 1975, Brayer and Hammond presented their work in a paper at the IEEE National Telecommunications Conference: the IEEE CRC-32 polynomial is the generating polynomial of a Hamming code and was selected for its error detection performance.  Even so, the Castagnoli CRC-32C polynomial used in iSCSI or SCTP matches its performance on messages from 58 bits to 131 kbits, and outperforms it in several size ranges including the two most common sizes of Internet packet. The ITU-T G.hn standard also uses CRC-32C to detect errors in the payload (although it uses CRC-16-CCITT for PHY headers).
CRC-32C computation is implemented in hardware as an operation (CRC32) of SSE4.2 instruction set, first introduced in Intel processors' Nehalem microarchitecture. ARM AArch64 architecture also provides hardware acceleration for both CRC-32 and CRC-32C operations.

Polynomial representations
The table below lists only the polynomials of the various algorithms in use. Variations of a particular protocol can impose pre-inversion, post-inversion and reversed bit ordering as described above. For example, the CRC32 used in Gzip and Bzip2 use the same polynomial, but Gzip employs reversed bit ordering, while Bzip2 does not.
Note that even parity polynomials in GF(2) with degree greater than 1 are never primitive. Even parity polynomial marked as primitive in this table represent a primitive polynomial multiplied by 
  
    
      
        
          (
          
            x
            +
            1
          
          )
        
      
    
    {\displaystyle \left(x+1\right)}
  
. The most significant bit of a polynomial is always 1, and is not shown in the hex representations.

Implementations
Implementation of CRC32 in GNU Radio up to 3.6.1 (ca. 2012)
C class code for CRC checksum calculation with many different CRCs to choose from

CRC catalogues
Catalogue of parametrised CRC algorithms
CRC Polynomial Zoo

See also
Checksum
Computation of cyclic redundancy checks
Information security
List of checksum algorithms
List of hash functions
LRC
Mathematics of cyclic redundancy checks
Simple file verification

References
Further reading
External links

ISO/IEC 13239:2002: Information technology -- Telecommunications and information exchange between systems -- High-level data link control (HDLC) procedures
CRC32-Castagnoli Linux Library

## Related Articles

### Internal Links

- [1-Wire](https://en.wikipedia.org/wiki/1-Wire)
- [AArch64](https://en.wikipedia.org/wiki/AArch64)
- [Advanced Data Communication Control Procedures](https://en.wikipedia.org/wiki/Advanced_Data_Communication_Control_Procedures)
- [AES3](https://en.wikipedia.org/wiki/AES3)
- [AIXM](https://en.wikipedia.org/wiki/AIXM)
- [American National Standards Institute](https://en.wikipedia.org/wiki/American_National_Standards_Institute)
- [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code)
- [ARINC](https://en.wikipedia.org/wiki/ARINC)
- [ARM architecture family](https://en.wikipedia.org/wiki/ARM_architecture_family)
- [Amazon Standard Identification Number](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)
- [AUTOSAR](https://en.wikipedia.org/wiki/AUTOSAR)
- [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
- [Adler-32](https://en.wikipedia.org/wiki/Adler-32)
- [Advanced Intelligent Tape](https://en.wikipedia.org/wiki/Advanced_Intelligent_Tape)
- [Affine transformation](https://en.wikipedia.org/wiki/Affine_transformation)
- [ACARS](https://en.wikipedia.org/wiki/ACARS)
- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [Application Programming Interface for Windows](https://en.wikipedia.org/wiki/Application_Programming_Interface_for_Windows)
- [Integer overflow](https://en.wikipedia.org/wiki/Integer_overflow)
- [Asynchronous Transfer Mode](https://en.wikipedia.org/wiki/Asynchronous_Transfer_Mode)
- [BCH code](https://en.wikipedia.org/wiki/BCH_code)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Binary Synchronous Communications](https://en.wikipedia.org/wiki/Binary_Synchronous_Communications)
- [Block cipher](https://en.wikipedia.org/wiki/Block_cipher)
- [Block cipher mode of operation](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation)
- [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth)
- [Btrfs](https://en.wikipedia.org/wiki/Btrfs)
- [Burst error](https://en.wikipedia.org/wiki/Burst_error)
- [Bus (computing)](https://en.wikipedia.org/wiki/Bus_(computing))
- [Endianness](https://en.wikipedia.org/wiki/Endianness)
- [Bzip2](https://en.wikipedia.org/wiki/Bzip2)
- [C++/CLI](https://en.wikipedia.org/wiki/C%2B%2B/CLI)
- [ITU-T](https://en.wikipedia.org/wiki/ITU-T)
- [CD-ROM](https://en.wikipedia.org/wiki/CD-ROM)
- [Code-division multiple access](https://en.wikipedia.org/wiki/Code-division_multiple_access)
- [CDMA2000](https://en.wikipedia.org/wiki/CDMA2000)
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Ceph (software)](https://en.wikipedia.org/wiki/Ceph_(software))
- [Checksum](https://en.wikipedia.org/wiki/Checksum)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Cksum](https://en.wikipedia.org/wiki/Cksum)
- [Coefficient](https://en.wikipedia.org/wiki/Coefficient)
- [Common Language Infrastructure](https://en.wikipedia.org/wiki/Common_Language_Infrastructure)
- [Communication channel](https://en.wikipedia.org/wiki/Communication_channel)
- [Computation of cyclic redundancy checks](https://en.wikipedia.org/wiki/Computation_of_cyclic_redundancy_checks)
- [Computer hardware](https://en.wikipedia.org/wiki/Computer_hardware)
- [CAN bus](https://en.wikipedia.org/wiki/CAN_bus)
- [Cryptographic hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
- [Cyclic code](https://en.wikipedia.org/wiki/Cyclic_code)
- [DNP3](https://en.wikipedia.org/wiki/DNP3)
- [Defense Technical Information Center](https://en.wikipedia.org/wiki/Defense_Technical_Information_Center)
- [DVB-S2](https://en.wikipedia.org/wiki/DVB-S2)
- [Dallas Semiconductor](https://en.wikipedia.org/wiki/Dallas_Semiconductor)
- [Dart (programming language)](https://en.wikipedia.org/wiki/Dart_(programming_language))
- [Data Integrity Field](https://en.wikipedia.org/wiki/Data_Integrity_Field)
- [Data Radio Channel](https://en.wikipedia.org/wiki/Data_Radio_Channel)
- [Data integrity](https://en.wikipedia.org/wiki/Data_integrity)
- [DigRF](https://en.wikipedia.org/wiki/DigRF)
- [Digital Data Storage](https://en.wikipedia.org/wiki/Digital_Data_Storage)
- [DECT](https://en.wikipedia.org/wiki/DECT)
- [Digital Linear Tape](https://en.wikipedia.org/wiki/Digital_Linear_Tape)
- [Digital signature](https://en.wikipedia.org/wiki/Digital_signature)
- [Division (mathematics)](https://en.wikipedia.org/wiki/Division_(mathematics))
- [Divisor](https://en.wikipedia.org/wiki/Divisor)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Dr. Dobb's Journal](https://en.wikipedia.org/wiki/Dr._Dobb%27s_Journal)
- [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript)
- [ECMAScript for XML](https://en.wikipedia.org/wiki/ECMAScript_for_XML)
- [Electronic Product Code](https://en.wikipedia.org/wiki/Electronic_Product_Code)
- [Ecma International](https://en.wikipedia.org/wiki/Ecma_International)
- [Eiffel (programming language)](https://en.wikipedia.org/wiki/Eiffel_(programming_language))
- [Entropy (information theory)](https://en.wikipedia.org/wiki/Entropy_(information_theory))
- [Error correction code](https://en.wikipedia.org/wiki/Error_correction_code)
- [Error correction code](https://en.wikipedia.org/wiki/Error_correction_code)
- [Error detection and correction](https://en.wikipedia.org/wiki/Error_detection_and_correction)
- [Ethernet](https://en.wikipedia.org/wiki/Ethernet)
- [Eurocontrol](https://en.wikipedia.org/wiki/Eurocontrol)
- [Exclusive or](https://en.wikipedia.org/wiki/Exclusive_or)
- [Ext4](https://en.wikipedia.org/wiki/Ext4)
- [File Allocation Table](https://en.wikipedia.org/wiki/File_Allocation_Table)
- [File Allocation Table](https://en.wikipedia.org/wiki/File_Allocation_Table)
- [File Allocation Table](https://en.wikipedia.org/wiki/File_Allocation_Table)
- [Federal Information Processing Standards](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards)
- [File Allocation Table](https://en.wikipedia.org/wiki/File_Allocation_Table)
- [Finite field](https://en.wikipedia.org/wiki/Finite_field)
- [Fletcher's checksum](https://en.wikipedia.org/wiki/Fletcher%27s_checksum)
- [FlexRay](https://en.wikipedia.org/wiki/FlexRay)
- [Floppy disk](https://en.wikipedia.org/wiki/Floppy_disk)
- [Full BASIC](https://en.wikipedia.org/wiki/Full_BASIC)
- [Function (mathematics)](https://en.wikipedia.org/wiki/Function_(mathematics))
- [G.hn](https://en.wikipedia.org/wiki/G.hn)
- [GF(2)](https://en.wikipedia.org/wiki/GF(2))
- [GSM](https://en.wikipedia.org/wiki/GSM)
- [Polynomial code](https://en.wikipedia.org/wiki/Polynomial_code)
- [Georgia Tech](https://en.wikipedia.org/wiki/Georgia_Tech)
- [Gzip](https://en.wikipedia.org/wiki/Gzip)
- [High-Level Data Link Control](https://en.wikipedia.org/wiki/High-Level_Data_Link_Control)
- [Hacker's Delight](https://en.wikipedia.org/wiki/Hacker%27s_Delight)
- [Hamming code](https://en.wikipedia.org/wiki/Hamming_code)
- [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance)
- [Hash function](https://en.wikipedia.org/wiki/Hash_function)
- [CRC-based framing](https://en.wikipedia.org/wiki/CRC-based_framing)
- [High-Level Data Link Control](https://en.wikipedia.org/wiki/High-Level_Data_Link_Control)
- [Holographic Versatile Disc](https://en.wikipedia.org/wiki/Holographic_Versatile_Disc)
- [IBM](https://en.wikipedia.org/wiki/IBM)
- [IEC 60870-5](https://en.wikipedia.org/wiki/IEC_60870-5)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISCSI](https://en.wikipedia.org/wiki/ISCSI)
- [ISDN](https://en.wikipedia.org/wiki/ISDN)
- [International Organization for Standardization](https://en.wikipedia.org/wiki/International_Organization_for_Standardization)
- [ISO/IEC 2022](https://en.wikipedia.org/wiki/ISO/IEC_2022)
- [ISO 9660](https://en.wikipedia.org/wiki/ISO_9660)
- [ITU-T](https://en.wikipedia.org/wiki/ITU-T)
- [List of ITU-T V-series recommendations](https://en.wikipedia.org/wiki/List_of_ITU-T_V-series_recommendations)
- [List of ITU-T V-series recommendations](https://en.wikipedia.org/wiki/List_of_ITU-T_V-series_recommendations)
- [Information security](https://en.wikipedia.org/wiki/Information_security)
- [Intel](https://en.wikipedia.org/wiki/Intel)
- [International Committee for Information Technology Standards](https://en.wikipedia.org/wiki/International_Committee_for_Information_Technology_Standards)
- [Irreducible polynomial](https://en.wikipedia.org/wiki/Irreducible_polynomial)
- [JSON](https://en.wikipedia.org/wiki/JSON)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Bit numbering](https://en.wikipedia.org/wiki/Bit_numbering)
- [Linear Tape-Open](https://en.wikipedia.org/wiki/Linear_Tape-Open)
- [Linear function](https://en.wikipedia.org/wiki/Linear_function)
- [List of Ecma standards](https://en.wikipedia.org/wiki/List_of_Ecma_standards)
- [List of hash functions](https://en.wikipedia.org/wiki/List_of_hash_functions)
- [List of hash functions](https://en.wikipedia.org/wiki/List_of_hash_functions)
- [Longitudinal redundancy check](https://en.wikipedia.org/wiki/Longitudinal_redundancy_check)
- [MPEG-2](https://en.wikipedia.org/wiki/MPEG-2)
- [MPT-1327](https://en.wikipedia.org/wiki/MPT-1327)
- [Mathematics of cyclic redundancy checks](https://en.wikipedia.org/wiki/Mathematics_of_cyclic_redundancy_checks)
- [Maxim Integrated](https://en.wikipedia.org/wiki/Maxim_Integrated)
- [Message authentication code](https://en.wikipedia.org/wiki/Message_authentication_code)
- [Meter-Bus](https://en.wikipedia.org/wiki/Meter-Bus)
- [Minimal BASIC](https://en.wikipedia.org/wiki/Minimal_BASIC)
- [Mitre Corporation](https://en.wikipedia.org/wiki/Mitre_Corporation)
- [Modbus](https://en.wikipedia.org/wiki/Modbus)
- [Bit numbering](https://en.wikipedia.org/wiki/Bit_numbering)
- [MultiMediaCard](https://en.wikipedia.org/wiki/MultiMediaCard)
- [National Technical Information Service](https://en.wikipedia.org/wiki/National_Technical_Information_Service)
- [Near-field communication](https://en.wikipedia.org/wiki/Near-field_communication)
- [Nehalem (microarchitecture)](https://en.wikipedia.org/wiki/Nehalem_(microarchitecture))
- [Noise (electronics)](https://en.wikipedia.org/wiki/Noise_(electronics))
- [OCLC](https://en.wikipedia.org/wiki/OCLC)
- [OS-9](https://en.wikipedia.org/wiki/OS-9)
- [Obfuscation](https://en.wikipedia.org/wiki/Obfuscation)
- [Ofcom](https://en.wikipedia.org/wiki/Ofcom)
- [Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML)
- [On-board diagnostics](https://en.wikipedia.org/wiki/On-board_diagnostics)
- [OpenSafety](https://en.wikipedia.org/wiki/OpenSafety)
- [Open XML Paper Specification](https://en.wikipedia.org/wiki/Open_XML_Paper_Specification)
- [PACTOR](https://en.wikipedia.org/wiki/PACTOR)
- [PKZIP](https://en.wikipedia.org/wiki/PKZIP)
- [POSIX](https://en.wikipedia.org/wiki/POSIX)
- [Parity bit](https://en.wikipedia.org/wiki/Parity_bit)
- [Parity bit](https://en.wikipedia.org/wiki/Parity_bit)
- [Physical layer](https://en.wikipedia.org/wiki/Physical_layer)
- [Polynomial](https://en.wikipedia.org/wiki/Polynomial)
- [Polynomial long division](https://en.wikipedia.org/wiki/Polynomial_long_division)
- [PNG](https://en.wikipedia.org/wiki/PNG)
- [Pretty Good Privacy](https://en.wikipedia.org/wiki/Pretty_Good_Privacy)
- [Primitive polynomial (field theory)](https://en.wikipedia.org/wiki/Primitive_polynomial_(field_theory))
- [Processor register](https://en.wikipedia.org/wiki/Processor_register)
- [Profibus](https://en.wikipedia.org/wiki/Profibus)
- [Proprietary protocol](https://en.wikipedia.org/wiki/Proprietary_protocol)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quotient](https://en.wikipedia.org/wiki/Quotient)
- [Radio Technical Commission for Maritime Services](https://en.wikipedia.org/wiki/Radio_Technical_Commission_for_Maritime_Services)
- [Radio-frequency identification](https://en.wikipedia.org/wiki/Radio-frequency_identification)
- [Radio teleswitch](https://en.wikipedia.org/wiki/Radio_teleswitch)
- [Base64](https://en.wikipedia.org/wiki/Base64)
- [Remainder](https://en.wikipedia.org/wiki/Remainder)
- [Reverse engineering](https://en.wikipedia.org/wiki/Reverse_engineering)
- [Ring (mathematics)](https://en.wikipedia.org/wiki/Ring_(mathematics))
- [Rome Laboratory](https://en.wikipedia.org/wiki/Rome_Laboratory)
- [Ross Williams](https://en.wikipedia.org/wiki/Ross_Williams)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [On-board diagnostics](https://en.wikipedia.org/wiki/On-board_diagnostics)
- [SATA](https://en.wikipedia.org/wiki/SATA)
- [SCSI](https://en.wikipedia.org/wiki/SCSI)
- [Stream Control Transmission Protocol](https://en.wikipedia.org/wiki/Stream_Control_Transmission_Protocol)
- [SSE4](https://en.wikipedia.org/wiki/SSE4)
- [SD card](https://en.wikipedia.org/wiki/SD_card)
- [Serial port](https://en.wikipedia.org/wiki/Serial_port)
- [Simple file verification](https://en.wikipedia.org/wiki/Simple_file_verification)
- [Springer Nature](https://en.wikipedia.org/wiki/Springer_Nature)
- [Stream cipher](https://en.wikipedia.org/wiki/Stream_cipher)
- [UniProt](https://en.wikipedia.org/wiki/UniProt)
- [Decoding methods](https://en.wikipedia.org/wiki/Decoding_methods)
- [System Management Bus](https://en.wikipedia.org/wiki/System_Management_Bus)
- [Systematic code](https://en.wikipedia.org/wiki/Systematic_code)
- [Technical standard](https://en.wikipedia.org/wiki/Technical_standard)
- [Telecommunications network](https://en.wikipedia.org/wiki/Telecommunications_network)
- [UniProt](https://en.wikipedia.org/wiki/UniProt)
- [Train communication network](https://en.wikipedia.org/wiki/Train_communication_network)
- [Ultra-wideband](https://en.wikipedia.org/wiki/Ultra-wideband)
- [Ultra Density Optical](https://en.wikipedia.org/wiki/Ultra_Density_Optical)
- [Universal 3D](https://en.wikipedia.org/wiki/Universal_3D)
- [Universal Disk Format](https://en.wikipedia.org/wiki/Universal_Disk_Format)
- [Universal Media Disc](https://en.wikipedia.org/wiki/Universal_Media_Disc)
- [USB](https://en.wikipedia.org/wiki/USB)
- [VXA](https://en.wikipedia.org/wiki/VXA)
- [W. Wesley Peterson](https://en.wikipedia.org/wiki/W._Wesley_Peterson)
- [UMTS](https://en.wikipedia.org/wiki/UMTS)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Wired Equivalent Privacy](https://en.wikipedia.org/wiki/Wired_Equivalent_Privacy)
- [X.25](https://en.wikipedia.org/wiki/X.25)
- [XMODEM](https://en.wikipedia.org/wiki/XMODEM)
- [XZ Utils](https://en.wikipedia.org/wiki/XZ_Utils)
- [ZMODEM](https://en.wikipedia.org/wiki/ZMODEM)
- [Zero divisor](https://en.wikipedia.org/wiki/Zero_divisor)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Ecma International Standards](https://en.wikipedia.org/wiki/Template:Ecma_International_Standards)
- [Template talk:Ecma International Standards](https://en.wikipedia.org/wiki/Template_talk:Ecma_International_Standards)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from July 2016](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_July_2016)
- [Category:Articles with unsourced statements from January 2024](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_January_2024)
- [Category:Use dmy dates from October 2023](https://en.wikipedia.org/wiki/Category:Use_dmy_dates_from_October_2023)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:36:15.530776+00:00_