# Mask generation function

## Article Metadata

- **Last Updated:** 2024-12-14T19:40:37.229756+00:00
- **Original Article:** [Mask generation function](https://en.wikipedia.org/wiki/Mask_generation_function)
- **Language:** en
- **Page ID:** 53230626

## Summary

A mask generation function (MGF) is a cryptographic primitive similar to a cryptographic hash function except that while a hash function's output has a fixed size, a MGF supports output of a variable length. In this respect, a MGF can be viewed as a extendable-output function (XOF): it can accept input of any length and process it to produce output of any length. Mask generation functions are completely deterministic: for any given input and any desired output length the output is always the sam

## Categories

- Category:All Wikipedia articles written in American English
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:CS1 errors: missing periodical
- Category:Cryptographic hash functions
- Category:Cryptographic primitives
- Category:Short description matches Wikidata
- Category:Theory of cryptography
- Category:Use American English from April 2019

## Table of Contents

- Definition
- Applications
- Examples

## Content

A mask generation function (MGF) is a cryptographic primitive similar to a cryptographic hash function except that while a hash function's output has a fixed size, a MGF supports output of a variable length. In this respect, a MGF can be viewed as a extendable-output function (XOF): it can accept input of any length and process it to produce output of any length. Mask generation functions are completely deterministic: for any given input and any desired output length the output is always the same.

Definition
A mask generation function takes an octet string of variable length and a desired output length as input, and outputs an octet string of the desired length. There may be restrictions on the length of the input and output octet strings, but such bounds are generally very large. Mask generation functions are deterministic; the octet string output is completely determined by the input octet string. The output of a mask generation function should be pseudorandom, that is, if the seed to the function is unknown, it should be infeasible to distinguish the output from a truly random string.

Applications
Mask generation functions, as generalizations of hash functions, are useful wherever hash functions are. However, use of a MGF is desirable in cases where a fixed-size hash would be inadequate.  Examples include generating padding, producing one-time pads or keystreams in symmetric-key encryption, and yielding outputs for pseudorandom number generators.

Padding schemes
Mask generation functions were first proposed as part of the specification for padding in the RSA-OAEP algorithm. The OAEP algorithm required a cryptographic hash function that could generate an output equal in size to a "data block" whose length was proportional to arbitrarily sized input message.

Random number generators
NIST Special Publication 800-90A defines a class of cryptographically secure random number generators, one of which is the "Hash DRBG", which uses a hash function with a counter to produce a requested sequence of random bits equal in size to the requested number of random bits.

Examples
Perhaps the most common and straightforward mechanism to build a MGF is to iteratively apply a hash function together with an incrementing counter value. The counter may be incremented indefinitely to yield new output blocks until a sufficient amount of output is collected. This is the approach used in MGF1.

MGF1
MGF1 is a mask generation function defined in the Public Key Cryptography Standard #1 published by RSA Laboratories:

Options
H
            a
            s
            h
          
        
      
    
    {\displaystyle {\mathsf {Hash}}}
  

hash function (
  
    
      
        
          
            h
            L
            e
            n
          
        
      
    
    {\displaystyle {\mathsf {hLen}}}
  
 denotes the length in octets of the hash function output)

Input
Z
      
    
    {\displaystyle Z}
  

seed from which mask is generated, an octet string

  
    
      
        l
      
    
    {\displaystyle l}
  

intended length in octets of the mask, at most 
  
    
      
        
          2
          
            32
          
        
        (
        
          
            h
            L
            e
            n
          
        
        )
      
    
    {\displaystyle 2^{32}({\mathsf {hLen}})}

Output
m
            a
            s
            k
          
        
      
    
    {\displaystyle {\mathsf {mask}}}
  

mask, an octet string of length 
  
    
      
        l
      
    
    {\displaystyle l}
  
; or "mask too long"

Steps
Example code
Below is Python code implementing MGF1:

Example outputs of MGF1:


== References ==

## Related Articles

### Internal Links

- [Cryptographic hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Extendable-output function](https://en.wikipedia.org/wiki/Extendable-output_function)
- [Keystream](https://en.wikipedia.org/wiki/Keystream)
- [One-time pad](https://en.wikipedia.org/wiki/One-time_pad)
- [Optimal asymmetric encryption padding](https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding)
- [Padding (cryptography)](https://en.wikipedia.org/wiki/Padding_(cryptography))
- [Pseudorandom number generator](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)
- [Symmetric-key algorithm](https://en.wikipedia.org/wiki/Symmetric-key_algorithm)
- [Template:Cite journal](https://en.wikipedia.org/wiki/Template:Cite_journal)
- [Help:CS1 errors](https://en.wikipedia.org/wiki/Help:CS1_errors)
- [Category:Use American English from April 2019](https://en.wikipedia.org/wiki/Category:Use_American_English_from_April_2019)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:40:37.229756+00:00_