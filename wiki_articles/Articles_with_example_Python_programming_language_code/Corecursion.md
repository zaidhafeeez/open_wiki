---
title: Corecursion
url: https://en.wikipedia.org/wiki/Corecursion
language: en
categories: ["Category:All articles that are too technical", "Category:All articles with style issues", "Category:All pages needing cleanup", "Category:Articles needing cleanup from July 2012", "Category:Articles with example Haskell code", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Category theory", "Category:Cleanup tagged articles with a reason field from July 2012", "Category:Functional programming", "Category:Recursion", "Category:Self-reference", "Category:Short description matches Wikidata", "Category:Theoretical computer science", "Category:Wikipedia articles that are too technical from November 2010", "Category:Wikipedia articles with style issues from February 2020", "Category:Wikipedia pages needing cleanup from July 2012"]
references: 0
last_modified: 2024-12-19T13:47:10Z
---

# Corecursion

## Summary

In computer science, corecursion is a type of operation that is dual to recursion. Whereas recursion works analytically, starting on data further from a base case and breaking it down into smaller data and repeating until one reaches a base case, corecursion works synthetically, starting from a base case and building it up, iteratively producing data further removed from a base case. Put simply, corecursive algorithms use the data that they themselves produce, bit by bit, as they become availabl

## Full Content

In computer science, corecursion is a type of operation that is dual to recursion. Whereas recursion works analytically, starting on data further from a base case and breaking it down into smaller data and repeating until one reaches a base case, corecursion works synthetically, starting from a base case and building it up, iteratively producing data further removed from a base case. Put simply, corecursive algorithms use the data that they themselves produce, bit by bit, as they become available, and needed, to produce further bits of data. A similar but distinct concept is generative recursion, which may lack a definite "direction" inherent in corecursion and recursion.
Where recursion allows programs to operate on arbitrarily complex data, so long as they can be reduced to simple data (base cases), corecursion allows programs to produce arbitrarily complex and potentially infinite data structures, such as streams, so long as it can be produced from simple data (base cases) in a sequence of finite steps. Where recursion may not terminate, never reaching a base state, corecursion starts from a base state, and thus produces subsequent steps deterministically, though it may proceed indefinitely (and thus not terminate under strict evaluation), or it may consume more than it produces and thus become non-productive. Many functions that are traditionally analyzed as recursive can alternatively, and arguably more naturally, be interpreted as corecursive functions that are terminated at a given stage, for example recurrence relations such as the factorial.
Corecursion can produce both finite and infinite data structures as results, and may employ self-referential data structures. Corecursion is often used in conjunction with lazy evaluation, to produce only a finite subset of a potentially infinite structure (rather than trying to produce an entire infinite structure at once). Corecursion is a particularly important concept in functional programming, where corecursion and codata allow total languages to work with infinite data structures.

Examples
Corecursion can be understood by contrast with recursion, which is more familiar. While corecursion is primarily of interest in functional programming, it can be illustrated using imperative programming, which is done below using the generator facility in Python. In these examples local variables are used, and assigned values imperatively (destructively), though these are not necessary in corecursion in pure functional programming. In pure functional programming, rather than assigning to local variables, these computed values form an invariable sequence, and prior values are accessed by self-reference (later values in the sequence reference earlier values in the sequence to be computed). The assignments simply express this in the imperative paradigm and explicitly specify where the computations happen, which serves to clarify the exposition.

Factorial
A classic example of recursion is computing the factorial, which is defined recursively by 0! := 1 and n! := n × (n - 1)!.
To recursively compute its result on a given input, a recursive function calls (a copy of) itself with a different ("smaller" in some way) input and uses the result of this call to construct its result. The recursive call does the same, unless the base case has been reached. Thus a call stack develops in the process. For example, to compute fac(3), this recursively calls in turn fac(2), fac(1), fac(0) ("winding up" the stack), at which point recursion terminates with fac(0) = 1, and then the stack unwinds in reverse order and the results are calculated on the way back along the call stack to the initial call frame fac(3) that uses the result of fac(2) = 2 to calculate the final result as 3 × 2 = 3 × fac(2) =: fac(3) and finally return fac(3) = 6. In this example a function returns a single value.
This stack unwinding can be explicated, defining the factorial corecursively, as an iterator, where one starts with the case of 
  
    
      
        1
        =:
        0
        !
      
    
    {\displaystyle 1=:0!}
  
, then from this starting value constructs factorial values for increasing numbers 1, 2, 3... as in the above recursive definition with "time arrow" reversed, as it were, by reading it backwards as 
  
    
      
        n
        !
        ×
        (
        n
        +
        1
        )
        =:
        (
        n
        +
        1
        )
        !
      
    
    {\displaystyle n!\times (n+1)=:(n+1)!}
  
. The corecursive algorithm thus defined produces a stream of all factorials. This may be concretely implemented as a generator. Symbolically, noting that computing next factorial value requires keeping track of both n and f (a previous factorial value), this can be represented as:

  
    
      
        n
        ,
        f
        =
        (
        0
        ,
        1
        )
        :
        (
        n
        +
        1
        ,
        f
        ×
        (
        n
        +
        1
        )
        )
      
    
    {\displaystyle n,f=(0,1):(n+1,f\times (n+1))}
  

or in Haskell, 

meaning, "starting from 
  
    
      
        n
        ,
        f
        =
        0
        ,
        1
      
    
    {\displaystyle n,f=0,1}
  
, on each step the next values are calculated as 
  
    
      
        n
        +
        1
        ,
        f
        ×
        (
        n
        +
        1
        )
      
    
    {\displaystyle n+1,f\times (n+1)}
  
". This is mathematically equivalent and almost identical to the recursive definition, but the 
  
    
      
        +
        1
      
    
    {\displaystyle +1}
  
 emphasizes that the factorial values are being built up, going forwards from the starting case, rather than being computed after first going backwards, down to the base case, with a 
  
    
      
        −
        1
      
    
    {\displaystyle -1}
  
 decrement. The direct output of the corecursive function does not simply contain the factorial 
  
    
      
        n
        !
      
    
    {\displaystyle n!}
  
 values, but also includes for each value the auxiliary data of its index n in the sequence, so that any one specific result can be selected among them all, as and when needed.
There is a connection with denotational semantics, where the denotations of recursive programs is built up corecursively in this way.
In Python, a recursive factorial function can be defined as:

This could then be called for example as factorial(5) to compute 5!.
A corresponding corecursive generator can be defined as:

This generates an infinite stream of factorials in order; a finite portion of it can be produced by:

This could then be called to produce the factorials up to 5! via:

If we're only interested in a certain factorial, just the last value can be taken, or we can fuse the production and the access into one function,

As can be readily seen here, this is practically equivalent (just by substituting return for the only yield there) to the accumulator argument technique for tail recursion, unwound into an explicit loop. Thus it can be said that the concept of corecursion is an explication of the embodiment of iterative computation processes by recursive definitions, where applicable.

Fibonacci sequence
In the same way, the Fibonacci sequence can be represented as:

  
    
      
        a
        ,
        b
        =
        (
        0
        ,
        1
        )
        :
        (
        b
        ,
        a
        +
        b
        )
      
    
    {\displaystyle a,b=(0,1):(b,a+b)}
  

Because the Fibonacci sequence is a recurrence relation of order 2, the corecursive relation must track two successive terms, with the 
  
    
      
        (
        b
        ,
        −
        )
      
    
    {\displaystyle (b,-)}
  
 corresponding to shift forward by one step, and the 
  
    
      
        (
        −
        ,
        a
        +
        b
        )
      
    
    {\displaystyle (-,a+b)}
  
 corresponding to computing the next term. This can then be implemented as follows (using parallel assignment):

In Haskell,

Tree traversal
Tree traversal via a depth-first approach is a classic example of recursion. Dually, breadth-first traversal can very naturally be implemented via corecursion.
Iteratively, one may traverse a tree by placing its root node in a data structure, then iterating with that data structure while it is non-empty, on each step removing the first node from it and placing the removed node's child nodes back into that data structure. If the data structure is a stack (LIFO), this yields depth-first traversal, and if the data structure is a queue (FIFO), this yields breadth-first traversal:

  
    
      
        
          
            trav
          
          
            nn
          
        
        (
        t
        )
        =
        
          
            aux
          
          
            nn
          
        
        (
        [
        t
        ]
        )
      
    
    {\displaystyle {\text{trav}}_{\text{nn}}(t)={\text{aux}}_{\text{nn}}([t])}
  

  
    
      
        
          
            aux
          
          
            df
          
        
        (
        [
        t
        ,
         
        .
        .
        .
        t
        s
        ]
        )
        =
        
          val
        
        (
        t
        )
        ;
         
        
          
            aux
          
          
            df
          
        
        (
        [
         
        .
        .
        .
        
          children
        
        (
        t
        )
        ,
         
        .
        .
        .
        t
        s
         
        ]
        )
      
    
    {\displaystyle {\text{aux}}_{\text{df}}([t,\ ...ts])={\text{val}}(t);\ {\text{aux}}_{\text{df}}([\ ...{\text{children}}(t),\ ...ts\ ])}
  

  
    
      
        
          
            aux
          
          
            bf
          
        
        (
        [
        t
        ,
         
        .
        .
        .
        t
        s
        ]
        )
        =
        
          val
        
        (
        t
        )
        ;
         
        
          
            aux
          
          
            bf
          
        
        (
        [
         
        .
        .
        .
        t
        s
        ,
         
        .
        .
        .
        
          children
        
        (
        t
        )
         
        ]
        )
      
    
    {\displaystyle {\text{aux}}_{\text{bf}}([t,\ ...ts])={\text{val}}(t);\ {\text{aux}}_{\text{bf}}([\ ...ts,\ ...{\text{children}}(t)\ ])}
  

Using recursion, a depth-first traversal of a tree is implemented simply as recursively traversing each of the root node's child nodes in turn. Thus the second child subtree is not processed until the first child subtree is finished. The root node's value is handled separately, whether before the first child is traversed (resulting in pre-order traversal), after the first is finished and before the second (in-order), or after the second child node is finished (post-order) — assuming the tree is binary, for simplicity of exposition. The call stack (of the recursive traversal function invocations) corresponds to the stack that would be iterated over with the explicit LIFO structure manipulation mentioned above. Symbolically,

  
    
      
        
          
            df
          
          
            in
          
        
        (
        t
        )
        =
        [
         
        .
        .
        .
        
          
            df
          
          
            in
          
        
        (
        
          left
        
        (
        t
        )
        )
        ,
         
        
          val
        
        (
        t
        )
        ,
         
        .
        .
        .
        
          
            df
          
          
            in
          
        
        (
        
          right
        
        (
        t
        )
        )
         
        ]
      
    
    {\displaystyle {\text{df}}_{\text{in}}(t)=[\ ...{\text{df}}_{\text{in}}({\text{left}}(t)),\ {\text{val}}(t),\ ...{\text{df}}_{\text{in}}({\text{right}}(t))\ ]}
  

  
    
      
        
          
            df
          
          
            pre
          
        
        (
        t
        )
        =
        [
         
        
          val
        
        (
        t
        )
        ,
         
        .
        .
        .
        
          
            df
          
          
            pre
          
        
        (
        
          left
        
        (
        t
        )
        )
        ,
         
        .
        .
        .
        
          
            df
          
          
            pre
          
        
        (
        
          right
        
        (
        t
        )
        )
         
        ]
      
    
    {\displaystyle {\text{df}}_{\text{pre}}(t)=[\ {\text{val}}(t),\ ...{\text{df}}_{\text{pre}}({\text{left}}(t)),\ ...{\text{df}}_{\text{pre}}({\text{right}}(t))\ ]}
  

  
    
      
        
          
            df
          
          
            post
          
        
        (
        t
        )
        =
        [
         
        .
        .
        .
        
          
            df
          
          
            post
          
        
        (
        
          left
        
        (
        t
        )
        )
        ,
         
        .
        .
        .
        
          
            df
          
          
            post
          
        
        (
        
          right
        
        (
        t
        )
        )
        ,
         
        
          val
        
        (
        t
        )
         
        ]
      
    
    {\displaystyle {\text{df}}_{\text{post}}(t)=[\ ...{\text{df}}_{\text{post}}({\text{left}}(t)),\ ...{\text{df}}_{\text{post}}({\text{right}}(t)),\ {\text{val}}(t)\ ]}
  

"Recursion" has two meanings here. First, the recursive invocations of the tree traversal functions 
  
    
      
        
          
            df
          
          
            x
            y
            z
          
        
      
    
    {\displaystyle {\text{df}}_{xyz}}
  
. More pertinently, we need to contend with how the resulting list of values is built here. Recursive, bottom-up output creation will result in the right-to-left tree traversal. To have it actually performed in the intended left-to-right order the sequencing would need to be enforced by some extraneous means, or it would be automatically achieved if the output were to be built in the top-down fashion, i.e. corecursively.
A breadth-first traversal creating its output in the top-down order, corecursively, can be also implemented by starting at the root node, outputting its value, then breadth-first traversing the subtrees – i.e., passing on the whole list of subtrees to the next step (not a single subtree, as in the recursive approach) – at the next step outputting the values of all of their root nodes, then passing on their child subtrees, etc. In this case the generator function, indeed the output sequence itself, acts as the queue. As in the factorial example above, where the auxiliary information of the index (which step one was at, n) was pushed forward, in addition to the actual output of n!, in this case the auxiliary information of the remaining subtrees is pushed forward, in addition to the actual output. Symbolically,

  
    
      
        v
        ,
        t
        s
        =
        (
        [
        ]
        ,
        [
        
          FullTree
        
        ]
        )
        :
        (
        
          RootValues
        
        (
        t
        s
        )
        ,
        
          ChildTrees
        
        (
        t
        s
        )
        )
      
    
    {\displaystyle v,ts=([],[{\text{FullTree}}]):({\text{RootValues}}(ts),{\text{ChildTrees}}(ts))}
  

meaning that at each step, one outputs the list of values in this level's nodes, then proceeds to the next level's nodes. Generating just the node values from this sequence simply requires discarding the auxiliary child tree data, then flattening the list of lists (values are initially grouped by level (depth); flattening (ungrouping) yields a flat linear list). This is extensionally equivalent to the 
  
    
      
        
          
            aux
          
          
            bf
          
        
      
    
    {\displaystyle {\text{aux}}_{\text{bf}}}
  
 specification above. In Haskell, 

Notably, given an infinite tree, the corecursive breadth-first traversal will traverse all nodes, just as for a finite tree, while the recursive depth-first traversal will go down one branch and not traverse all nodes, and indeed if traversing post-order, as in this example (or in-order), it will visit no nodes at all, because it never reaches a leaf. This shows the usefulness of corecursion rather than recursion for dealing with infinite data structures. One caveat still remains for trees with the infinite branching factor, which need a more attentive interlacing to explore the space better. See dovetailing.
In Python, this can be implemented as follows.
The usual post-order depth-first traversal can be defined as:

This can then be called by df(t) to print the values of the nodes of the tree in post-order depth-first order.
The breadth-first corecursive generator can be defined as:

This can then be called to print the values of the nodes of the tree in breadth-first order:

Definition
Initial data types can be defined as being the least fixpoint (up to isomorphism) of some type equation; the isomorphism is then given by an initial algebra. Dually, final (or terminal) data types can be defined as being the greatest fixpoint of a type equation; the isomorphism is then given by a final coalgebra.
If the domain of discourse is the category of sets and total functions, then final data types may contain infinite, non-wellfounded values, whereas initial types do not. On the other hand, if the domain of discourse is the category of complete partial orders and continuous functions, which corresponds roughly to the Haskell programming language, then final types coincide with initial types, and the corresponding final coalgebra and initial algebra form an isomorphism.
Corecursion is then a technique for recursively defining functions whose range (codomain) is a final data type, dual to the way that ordinary recursion recursively defines functions whose domain is an initial data type.
The discussion below provides several examples in Haskell that distinguish corecursion. Roughly speaking, if one were to port these definitions to the category of sets, they would still be corecursive. This informal usage is consistent with existing textbooks about Haskell. The examples used in this article predate the attempts to define corecursion and explain what it is.

Discussion
The rule for primitive corecursion on codata is the dual to that for primitive recursion on data. Instead of descending on the argument by pattern-matching on its constructors (that were called up before, somewhere, so we receive a ready-made datum and get at its constituent sub-parts, i.e. "fields"), we ascend on the result by filling-in its "destructors" (or "observers", that will be called afterwards, somewhere - so we're actually calling a constructor, creating another bit of the result to be observed later on). Thus corecursion creates (potentially infinite) codata, whereas ordinary recursion analyses (necessarily finite) data.  Ordinary recursion might not be applicable to the codata because it might not terminate.  Conversely, corecursion is not strictly necessary if the result type is data, because data must be finite.
In "Programming with streams in Coq: a case study: the Sieve of Eratosthenes" we find

where primes "are obtained by applying the primes operation to the stream (Enu 2)". Following the above notation, the sequence of primes (with a throwaway 0 prefixed to it) and numbers streams being progressively sieved, can be represented as 

  
    
      
        p
        ,
        s
        =
        (
        0
        ,
        [
        2..
        ]
        )
        :
        (
        h
        d
        (
        s
        )
        ,
        s
        i
        e
        v
        e
        (
        h
        d
        (
        s
        )
        ,
        t
        l
        (
        s
        )
        )
        )
      
    
    {\displaystyle p,s=(0,[2..]):(hd(s),sieve(hd(s),tl(s)))}
  

or in Haskell, 

The authors discuss how the definition of sieve is not guaranteed always to be productive, and could become stuck e.g. if called with [5,10..] as the initial stream.
Here is another example in Haskell. The following definition produces the list of Fibonacci numbers in linear time:

This infinite list depends on lazy evaluation;  elements are computed on an as-needed basis, and only finite prefixes are ever explicitly represented in memory. This feature allows algorithms on parts of codata to terminate; such techniques are an important part of Haskell programming.
This can be done in Python as well:

The definition of zipWith can be inlined, leading to this:

This example employs a self-referential data structure. Ordinary recursion makes use of self-referential functions,   but does not accommodate self-referential data. However,  this is not essential to the Fibonacci example. It can be rewritten as follows:

This employs only self-referential function to construct the result. If it were used with strict list constructor it would be an example of runaway recursion, but with non-strict list constructor this guarded recursion gradually produces an indefinitely defined list.
Corecursion need not produce an infinite object; a corecursive queue is a particularly good example of this phenomenon. The following definition produces a breadth-first traversal of a binary tree in the top-down manner, in linear time (already incorporating the flattening mentioned above):

This definition takes a tree and produces a list of its sub-trees (nodes and leaves). This list serves dual purpose as both the input queue and the result (gen len p produces its output len notches ahead of its input back-pointer, p, along the list).  It is finite if and only if the initial tree is finite.  The length of the queue must be explicitly tracked in order to ensure termination;  this can safely be elided if this definition is applied only to infinite trees.   
This Haskell code uses self-referential data structure, but does not essentially depend on lazy evaluation. It can be straightforwardly translated into e.g. Prolog which is not a lazy language. What is essential is the ability to build a list (used as the queue) in the top-down manner. For that, Prolog has tail recursion modulo cons (i.e. open ended lists). Which is also emulatable in Scheme, C, etc. using linked lists with mutable tail sentinel pointer:

Another particular example gives a solution to the problem of breadth-first labeling. The function label visits every node in a binary tree in the breadth first fashion,  replacing each label with an integer,  each subsequent integer bigger than the last by 1. This solution employs a self-referential data structure,  and the binary tree can be finite or infinite.

Or in Prolog, for comparison,

An apomorphism (such as an anamorphism, such as unfold) is a form of corecursion in the same way that a paramorphism (such as a catamorphism, such as fold) is a form of recursion.
The Coq proof assistant supports corecursion and coinduction using the CoFixpoint command.

History
Corecursion, referred to as circular programming, dates at least to (Bird 1984), who credits John Hughes and Philip Wadler; more general forms were developed in (Allison 1989). The original motivations included producing more efficient algorithms (allowing a single pass over data in some cases, instead of requiring multiple passes) and implementing classical data structures, such as doubly linked lists and queues, in functional languages.

See also
Bisimulation
Coinduction
Recursion
Anamorphism

Notes


== References ==
