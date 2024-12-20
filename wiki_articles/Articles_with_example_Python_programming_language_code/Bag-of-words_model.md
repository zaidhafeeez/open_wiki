---
title: Bag-of-words model
url: https://en.wikipedia.org/wiki/Bag-of-words_model
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Machine learning", "Category:Natural language processing", "Category:Short description is different from Wikidata", "Category:Wikipedia articles needing clarification from December 2023"]
references: 0
last_modified: 2024-12-19T14:07:09Z
---

# Bag-of-words model

## Summary

The bag-of-words model (BoW) is a model of text which uses a representation of text that is based on an unordered collection (a "bag") of words. It is used in natural language processing and information retrieval (IR). It disregards word order (and thus most of syntax or grammar) but captures multiplicity.
The bag-of-words model is commonly used in methods of document classification where, for example, the (frequency of) occurrence of each word is used as a feature for training a classifier. It 

## Full Content

The bag-of-words model (BoW) is a model of text which uses a representation of text that is based on an unordered collection (a "bag") of words. It is used in natural language processing and information retrieval (IR). It disregards word order (and thus most of syntax or grammar) but captures multiplicity.
The bag-of-words model is commonly used in methods of document classification where, for example, the (frequency of) occurrence of each word is used as a feature for training a classifier. It has also been used for computer vision.
An early reference to "bag of words" in a linguistic context can be found in Zellig Harris's 1954 article on Distributional Structure.

Definition
The following models a text document using bag-of-words. Here are two simple text documents:

Based on these two text documents, a list is constructed as follows for each document:

Representing each bag-of-words as a JSON object, and attributing to the respective JavaScript variable:

Each key is the word, and each value is the number of occurrences of that word in the given text document.
The order of elements is free, so, for example {"too":1,"Mary":1,"movies":2,"John":1,"watch":1,"likes":2,"to":1} is also equivalent to BoW1. It is also what we expect from a strict JSON object representation.
Note: if another document is like a union of these two,

its JavaScript representation will be:

So, as we see in the bag algebra, the "union" of two documents in the bags-of-words representation is, formally, the disjoint union, summing the multiplicities of each element.
  
    
      
        B
        o
        W
        3
        =
        B
        o
        W
        1
        ⨄
        B
        o
        W
        2
      
    
    {\displaystyle BoW3=BoW1\biguplus BoW2}

Word order
The BoW representation of a text removes all word ordering. For example, the BoW representation of "man bites dog" and "dog bites man" are the same, so any algorithm that operates with a BoW representation of text must treat them in the same way. Despite this lack of syntax or grammar, BoW representation is fast and may be sufficient for simple tasks that do not require word order. For instance, for document classification, if the words "stocks" "trade" "investors" appears multiple times, then the text is likely a financial report, even though it would be insufficient to distinguish between Yesterday, investors were rallying, but today, they are retreating.andYesterday, investors were retreating, but today, they are rallying.and so the BoW representation would be insufficient to determine the detailed meaning of the document.

Implementations
Implementations of the bag-of-words model might involve using frequencies of words in a document to represent its contents. The frequencies can be "normalized" by the inverse of document frequency, or tf–idf. Additionally, for the specific purpose of classification, supervised alternatives have been developed to account for the class label of a document. Lastly, binary (presence/absence or 1/0) weighting is used in place of frequencies for some problems (e.g., this option is implemented in the WEKA machine learning software system).

Python implementation
Hashing trick
A common alternative to using dictionaries is the hashing trick, where words are mapped directly to indices with a hashing function. Thus, no memory is required to store a dictionary. Hash collisions are typically dealt via freed-up memory to increase the number of hash buckets. In practice, hashing simplifies the implementation of bag-of-words models and improves scalability.

See also
Additive smoothing
Feature extraction
Machine learning
MinHash
Vector space model
w-shingling

Notes
References
McTear, Michael (et al) (2016). The Conversational Interface. Springer International Publishing.
