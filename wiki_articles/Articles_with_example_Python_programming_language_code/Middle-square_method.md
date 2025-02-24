---
title: Middle-square method
url: https://en.wikipedia.org/wiki/Middle-square_method
language: en
categories: ["Category:Articles with example C code", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:John von Neumann", "Category:Pseudorandom number generators", "Category:Short description matches Wikidata"]
references: 0
last_modified: 2024-12-19T13:45:23Z
---

# Middle-square method

## Summary

In mathematics and computer science, the middle-square method is a method of generating pseudorandom numbers. In practice it is a highly flawed method for many practical purposes, since its period is usually very short and it has some severe weaknesses; repeated enough times, the middle-square method will either begin repeatedly generating the same number or cycle to a previous number in the sequence and loop indefinitely.

## Full Content

In mathematics and computer science, the middle-square method is a method of generating pseudorandom numbers. In practice it is a highly flawed method for many practical purposes, since its period is usually very short and it has some severe weaknesses; repeated enough times, the middle-square method will either begin repeatedly generating the same number or cycle to a previous number in the sequence and loop indefinitely.

History
In mathematics
The method was invented by John von Neumann, and was described by him at a conference in 1949.
In the 1949 talk, Von Neumann quipped that "Anyone who considers arithmetical methods of producing random digits is, of course, in a state of sin." What he meant, he elaborated, was that there were no true "random numbers", just means to produce them, and "a strict arithmetic procedure", like the middle-square method, "is not such a method". Nevertheless, he found these methods hundreds of times faster than reading "truly" random numbers off punch cards, which had practical importance for his ENIAC work. He found the "destruction" of middle-square sequences to be a factor in their favor, because it could be easily detected: "one always fears the appearance of undetected short cycles". Nicholas Metropolis reported sequences of 750,000 digits before "destruction" by means of using 38-bit numbers with the "middle-square" method.
The book The Broken Dice by Ivar Ekeland gives an extended account of how the method was invented by a Franciscan friar known only as Brother Edvin sometime between 1240 and 1250. Supposedly, the manuscript is now lost, but Jorge Luis Borges sent Ekeland a copy that he made at the Vatican Library.
Modifying the middle-square algorithm with a Weyl sequence improves period and randomness.

The method
To generate a sequence of n-digit pseudorandom numbers, an n-digit starting value is created and squared, producing a 2n-digit number. If the result has fewer than 2n digits, leading zeroes are added to compensate. The middle n digits of the result would be the next number in the sequence and returned as the result. This process is then repeated to generate more numbers. 
The value of n must be even in order for the method to work –  if the value of n is odd, then there will not necessarily be a uniquely defined "middle n-digits" to select from. Consider the following: If a 3-digit number is squared, it can yield a 6-digit number (e.g. 5402 = 291600). If there were to be middle 3 digits, that would leave 6 − 3 = 3 digits to be distributed to the left and right of the middle. It is impossible to evenly distribute these digits equally on both sides of the middle number, and therefore there are no "middle digits". It is acceptable to pad the seeds with zeros to the left in order to create an even valued n-digit number (e.g. 540 → 0540).
For a generator of n-digit numbers, the period can be no longer than 8n. If the middle n digits are all zeroes, the generator then outputs zeroes forever. If the first half of a number in the sequence is zeroes, the subsequent numbers will be decreasing to zero. While these runs of zero are easy to detect, they occur too frequently for this method to be of practical use. The middle-squared method can also get stuck on a number other than zero.  For n = 4, this occurs with the values 0100, 2500, 3792, and 7600. Other seed values form very short repeating cycles, e.g., 0540 → 2916 → 5030 → 3009. These phenomena are even more obvious when n = 2, as none of the 100 possible seeds generates more than 14 iterations without reverting to 0, 10, 50, 60, or a 24 ↔ 57 loop.

Example implementation
Here, the algorithm is rendered in Python 3.12.

See also
Linear congruential generator
Blum Blum Shub
 middle-square hash function 


== References ==
