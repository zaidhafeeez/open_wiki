# Full cycle

## Metadata
- **Last Updated:** 2024-12-03 06:57:57 UTC
- **Original Article:** [Full cycle](https://en.wikipedia.org/wiki/Full_cycle)
- **Language:** en
- **Page ID:** 2145989

## Summary
In a pseudorandom number generator (PRNG), a full cycle or full period is the behavior of a PRNG over its set of valid states. In particular, a PRNG is said to have a full cycle if, for any valid seed state, the PRNG traverses every valid state before returning to the seed state, i.e., the period is equal to the cardinality of the state space.
The restrictions on the parameters of a PRNG for it to possess a full cycle are known only for certain types of PRNGs, such as linear congruential generators and linear-feedback shift registers. There is no general method to determine whether a PRNG algorithm is full-cycle short of exhausting the state space, which may be exponentially large compared to the size of the algorithm's internal state.

## Categories
This article belongs to the following categories:

- Category:All articles lacking sources
- Category:Articles lacking sources from June 2019
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Pseudorandom number generators
- Category:Short description matches Wikidata

## Table of Contents

- Example 1 (in C/C++)
- Example 1 (in Python)
- See also

## Content

In a pseudorandom number generator (PRNG), a full cycle or full period is the behavior of a PRNG over its set of valid states. In particular, a PRNG is said to have a full cycle if, for any valid seed state, the PRNG traverses every valid state before returning to the seed state, i.e., the period is equal to the cardinality of the state space.
The restrictions on the parameters of a PRNG for it to possess a full cycle are known only for certain types of PRNGs, such as linear congruential generators and linear-feedback shift registers. There is no general method to determine whether a PRNG algorithm is full-cycle short of exhausting the state space, which may be exponentially large compared to the size of the algorithm's internal state.

Example 1 (in C/C++)
Given a random number seed that is greater or equal to zero, a total sample size greater than 1, and an increment coprime to the total sample size, a full cycle can be generated with the following logic. Each nonnegative number smaller than the sample size occurs exactly once.

Example 1 (in Python)
See also
Linear congruential generator
Xorshift

## Archive Info
- **Archived on:** 2024-12-15 15:18:41 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 1116 bytes
- **Word Count:** 193 words
