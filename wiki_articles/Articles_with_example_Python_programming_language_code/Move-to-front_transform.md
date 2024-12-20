---
title: Move-to-front transform
url: https://en.wikipedia.org/wiki/Move-to-front_transform
language: en
categories: ["Category:All Wikipedia articles needing clarification", "Category:All articles needing additional references", "Category:All articles needing examples", "Category:Articles needing additional references from May 2011", "Category:Articles needing examples from February 2012", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:CS1 interwiki-linked names", "Category:Data compression", "Category:Data compression transforms", "Category:Lossless compression algorithms", "Category:Short description is different from Wikidata", "Category:Wikipedia articles needing clarification from February 2011", "Category:Wikipedia articles needing clarification from July 2015"]
references: 0
last_modified: 2024-12-20T21:32:05Z
---

# Move-to-front transform

## Summary

The move-to-front (MTF) transform is an encoding of data (typically a stream of bytes) designed to improve the performance of entropy encoding techniques of compression.  When efficiently implemented, it is fast enough that its benefits usually justify including it as an extra step in data compression algorithm.
This algorithm was first published by Boris Ryabko under the name of "book stack" in 1980. Subsequently, it was rediscovered by J.K. Bentley et al. in 1986, as attested in the explanator

## Full Content

The move-to-front (MTF) transform is an encoding of data (typically a stream of bytes) designed to improve the performance of entropy encoding techniques of compression.  When efficiently implemented, it is fast enough that its benefits usually justify including it as an extra step in data compression algorithm.
This algorithm was first published by Boris Ryabko under the name of "book stack" in 1980. Subsequently, it was rediscovered by J.K. Bentley et al. in 1986, as attested in the explanatory note.

The transform
The main idea is that each symbol in the data is replaced by its index in the stack of “recently used symbols”. For example, long sequences of identical symbols are replaced by as many zeroes, whereas when a symbol that has not been used in a long time appears, it is replaced with a large number. Thus at the end the data is transformed into a sequence of integers; if the data exhibits a lot of local correlations, then these integers tend to be small.
Let us give a precise description. Assume for simplicity that the symbols in the data are bytes.
Each byte value is encoded by its index in a list of bytes, which changes over the course of the algorithm.  The list is initially in order by byte value (0, 1, 2, 3, ..., 255).  Therefore, the first byte is always encoded by its own value.  However, after encoding a byte, that value is moved to the front of the list before continuing to the next byte.
An example will shed some light on how the transform works.  Imagine instead of bytes, we are encoding values in a–z.  We wish to transform the following sequence:

bananaaa

By convention, the list is initially (abcdefghijklmnopqrstuvwxyz).  The first letter in the sequence is b, which appears at index 1 (the list is indexed from 0 to 25).  We put a 1 to the output stream:

1

The b moves to the front of the list, producing (bacdefghijklmnopqrstuvwxyz).  The next letter is a, which now appears at index 1.  So we add a 1 to the output stream. We have:

1,1

and we move the letter a back to the top of the list.  Continuing this way, we find that the sequence is encoded by:

1,1,13,1,1,1,0,0

It is easy to see that the transform is reversible.  Simply maintain the same list and decode by replacing each index in the encoded stream with the letter at that index in the list. Note the difference between this and the encoding method: The index in the list is used directly instead of looking up each value for its index.
i.e. you start again with (abcdefghijklmnopqrstuvwxyz). You take the "1" of the encoded block and look it up in the list, which results in "b". Then move the "b" to front which results in (bacdef...). Then take the next "1", look it up in the list, this results in "a", move the "a" to front ... etc.

Implementation
Details of implementation are important for performance, particularly for decoding.  For encoding, no clear advantage is gained by using a linked list, so using an array to store the list is acceptable, with worst-case performance O(nk), where n is the length of the data to be encoded and k is the number of values (generally a constant for a given implementation).
The typical performance is better because frequently-used symbols are more likely to be at the front and will produce earlier hits. This is also the idea behind a Move-to-front self-organizing list.
However, for decoding, we can use specialized data structures to greatly improve performance.

Python
This is a possible implementation of the move-to-front algorithm in Python.

In this example we can see the MTF code taking advantage of the three repetitive i's in the input word. The common dictionary here, however, is less than ideal since it is initialized with more commonly used ASCII printable characters put after little-used control codes, against the MTF code's design intent of keeping what's commonly used in the front. If one rotates the dictionary to put the more-used characters in earlier places, a better encoding can be obtained:

Use in practical data compression algorithms
The MTF transform takes advantage of local correlation of frequencies to reduce the entropy of a message. Indeed, recently used letters stay towards the front of the list; if use of letters exhibits local correlations, this will result in a large number of small numbers such as "0"'s and "1"'s in the output.
However, not all data exhibits this type of local correlation, and for some messages, the MTF transform may actually increase the entropy.
An important use of the MTF transform is in Burrows–Wheeler transform based compression.  The Burrows–Wheeler transform is very good at producing a sequence that exhibits local frequency correlation from text and certain other special classes of data.  Compression benefits greatly from following up the Burrows–Wheeler transform with an MTF transform before the final entropy-encoding step.

Example
As an example, imagine we wish to compress Hamlet's soliloquy (To be, or not to be...).  We can calculate the size of this message to be 7033 bits.  Naively, we might try to apply the MTF transform directly.  The result is a message with 7807 bits (higher than the original).  The reason is that English text does not in general exhibit a high level of local frequency correlation.  However, if we first apply the Burrows–Wheeler transform, and then the MTF transform, we get a message with 6187 bits.  Note that the Burrows–Wheeler transform does not decrease the entropy of the message; it only reorders the bytes in a way that makes the MTF transform more effective.
One problem with the basic MTF transform is that it makes the same changes for any character, regardless of frequency, which can result in diminished compression as characters that occur rarely may push frequent characters to higher values.  Various alterations and alternatives have been developed for this reason.  One common change is to make it so that characters above a certain point can only be moved to a certain threshold.  Another is to make some algorithm that runs a count of each character's local frequency and uses these values to choose the characters' order at any point.  Many of these transforms still reserve zero for repeat characters, since these are often the most common in data after the Burrows Wheeler Transform.

Move-to-front linked-list
The term Move To Front (MTF) is also used in a slightly different context, as a type of a dynamic linked list. In an MTF list, each element is moved to the front when it is accessed. This ensures that, over time, the more frequently accessed elements are easier to access.

References
External links
"Move to front" by Arturo San Emeterio Campos
