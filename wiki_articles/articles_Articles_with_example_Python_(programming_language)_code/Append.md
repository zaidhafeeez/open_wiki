# Append

_Last updated: 2024-12-14T15:39:12.783288_

**Original Article:** [Append](https://en.wikipedia.org/wiki/Append)

**Summary:** In computer programming, append is the operation for concatenating linked lists or arrays in some high-level programming languages.

## Categories
- Category:Articles with example Haskell code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example code
- Category:Articles with short description
- Category:CS1 errors: missing periodical
- Category:DOS on IBM PC compatibles
- Category:Functional programming
- Category:Lisp (programming language)
- Category:Programming constructs
- Category:Short description matches Wikidata

## Content

In computer programming, append is the operation for concatenating linked lists or arrays in some high-level programming languages.

Lisp
Append originates in the programming language Lisp. The append procedure takes zero or more (linked) lists as arguments, and returns the concatenation of these lists.

Since the append procedure must completely copy all of its arguments except the last, both its time and space complexity are O(n) for a list of 
  
    
      
        n
      
    
    {\displaystyle n}
  
 elements.  It may thus be a source of inefficiency if used injudiciously in code.
The nconc procedure (called append! in Scheme) performs the same function as append, but destructively: it alters the cdr of each argument (save the last), pointing it to the next list.

Implementation
Append can easily be defined recursively in terms of cons. The following is a simple implementation in Scheme, for two arguments only:

Append can also be implemented using fold-right:

Other languages
Following Lisp, other high-level programming languages which feature linked lists as primitive data structures have adopted an append. To append lists, as an operator, Haskell uses ++, OCaml uses @.
Other languages use the + or ++ symbols to nondestructively concatenate a string, list, or array.

Prolog
The logic programming language Prolog features a built-in append predicate, which can be implemented as follows:

This predicate can be used for appending, but also for picking lists apart. Calling

yields the solutions:

L = [], R = [1, 2, 3] ;
L = [1], R = [2, 3] ;
L = [1, 2], R = [3] ;
L = [1, 2, 3], R = []

Miranda
In Miranda, this right-fold, from Hughes (1989:5-6), has the same semantics (by example) as the Scheme implementation above, for two arguments.

append a b = reduce cons b a

Where reduce is Miranda's name for fold, and cons constructs a list from two values or lists.
For example,

append [1,2] [3,4] = reduce cons [3,4] [1,2]
    = (reduce cons [3,4]) (cons 1 (cons 2 nil))
    = cons 1 (cons 2 [3,4]))
        (replacing cons by cons and nil by [3,4])
    = [1,2,3,4]

Haskell
In Haskell, this right-fold has the same effect as the Scheme implementation above:

This is essentially a reimplementation of Haskell's ++ operator.

Perl
In Perl, the push function is equivalent to the append method, and can be used in the following way.

The end result is a list containing [1, 2, 3]
The unshift function appends to the front of a list, rather than the end

The end result is a list containing [2, 3, 1]
When opening a file, use the ">>" mode to append rather than over write.

Note that when opening and closing file handles, one should always check the return value.

Python
In Python, use the list method extend or the infix operators + and += to append lists.

Do not confuse with the list method append, which adds a single element to a list:

Bash
In Bash the append redirect is the usage of ">>" for adding a stream to something, like in the following series of shell commands:

The stream "Goodbye world!" is added to the text file written in the first command. The ";" implies the execution of the given commands in order, not simultaneously. So, the final content of the text file is:

References
Hughes, John (1989). "Why functional programming matters" (PDF). Computer Journal. 32 (2): 98–107. doi:10.1093/comjnl/32.2.98. Archived from the original (PDF) on 2007-04-13.
Steele, Guy L. Jr. (1990). "Common Lisp: The Language" (2nd ed.): 418. {{cite journal}}: Cite journal requires |journal= (help) Description of append.