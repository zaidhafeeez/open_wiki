# Set-builder notation

## Article Metadata

- **Last Updated:** 2024-12-15T04:48:03.838968+00:00
- **Original Article:** [Set-builder notation](https://en.wikipedia.org/wiki/Set-builder_notation)
- **Language:** en
- **Page ID:** 220089

## Summary

In set theory and its applications to logic, mathematics, and computer science, set-builder notation is a mathematical notation for describing a set by stating the properties that its members must satisfy.
Defining sets by properties is also known as set comprehension, set abstraction or as defining a set's intension.

## Categories

- Category:All articles to be split
- Category:All articles to have a section moved
- Category:Articles to be split from December 2023
- Category:Articles to have a section moved from December 2023
- Category:Articles with example Haskell code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Mathematical notation
- Category:Set theory
- Category:Short description is different from Wikidata
- Category:Use dmy dates from December 2020

## Table of Contents

- Sets defined by a predicate
- More complex expressions on the left side of the notation
- Equivalent predicates yield equal sets
- Set existence axiom
- In programming languages
- See also

## Content

In set theory and its applications to logic, mathematics, and computer science, set-builder notation is a mathematical notation for describing a set by stating the properties that its members must satisfy.
Defining sets by properties is also known as set comprehension, set abstraction or as defining a set's intension.

Sets defined by a predicate
Set-builder notation can be used to describe a set that is defined by a predicate, that is, a logical formula that evaluates to true for an element of the set, and false otherwise. In this form, set-builder notation has three parts: a variable, a colon or vertical bar separator, and a predicate. Thus there is a variable on the left of the separator, and a rule on the right of it. These three parts are contained in curly brackets:

  
    
      
        {
        x
        ∣
        Φ
        (
        x
        )
        }
      
    
    {\displaystyle \{x\mid \Phi (x)\}}
  

or

  
    
      
        {
        x
        :
        Φ
        (
        x
        )
        }
        .
      
    
    {\displaystyle \{x:\Phi (x)\}.}
  

The vertical bar (or colon) is a separator that can be read as "such that",  "for which", or "with the property that".  The formula Φ(x) is said to be the rule or the predicate. All values of x for which the predicate holds (is true) belong to the set being defined. All values of x for which the predicate does not hold do not belong to the set.  Thus 
  
    
      
        {
        x
        ∣
        Φ
        (
        x
        )
        }
      
    
    {\displaystyle \{x\mid \Phi (x)\}}
  
 is the set of all values of x that satisfy the formula Φ. It may be the empty set, if no value of x satisfies the formula.

Specifying the domain
A domain E can appear on the left of the vertical bar: 

  
    
      
        {
        x
        ∈
        E
        ∣
        Φ
        (
        x
        )
        }
        ,
      
    
    {\displaystyle \{x\in E\mid \Phi (x)\},}
  

or by adjoining it to the predicate:

  
    
      
        {
        x
        ∣
        x
        ∈
        E
        
           and 
        
        Φ
        (
        x
        )
        }
        
        
          or
        
        
        {
        x
        ∣
        x
        ∈
        E
        ∧
        Φ
        (
        x
        )
        }
        .
      
    
    {\displaystyle \{x\mid x\in E{\text{ and }}\Phi (x)\}\quad {\text{or}}\quad \{x\mid x\in E\land \Phi (x)\}.}
  

The ∈ symbol here denotes set membership, while the 
  
    
      
        ∧
      
    
    {\displaystyle \land }
  
 symbol denotes the logical "and" operator, known as logical conjunction. This notation represents the set of all values of x that belong to some given set E for which the predicate is true (see "Set existence axiom" below). If 
  
    
      
        Φ
        (
        x
        )
      
    
    {\displaystyle \Phi (x)}
  
 is a conjunction 
  
    
      
        
          Φ
          
            1
          
        
        (
        x
        )
        ∧
        
          Φ
          
            2
          
        
        (
        x
        )
      
    
    {\displaystyle \Phi _{1}(x)\land \Phi _{2}(x)}
  
, then 
  
    
      
        {
        x
        ∈
        E
        ∣
        Φ
        (
        x
        )
        }
      
    
    {\displaystyle \{x\in E\mid \Phi (x)\}}
  
 is sometimes written 
  
    
      
        {
        x
        ∈
        E
        ∣
        
          Φ
          
            1
          
        
        (
        x
        )
        ,
        
          Φ
          
            2
          
        
        (
        x
        )
        }
      
    
    {\displaystyle \{x\in E\mid \Phi _{1}(x),\Phi _{2}(x)\}}
  
, using a comma instead of the symbol 
  
    
      
        ∧
      
    
    {\displaystyle \land }
  
.
In general, it is not a good idea to consider sets without defining a domain of discourse, as this would represent the subset of all possible things that may exist for which the predicate is true. This can easily lead to contradictions and paradoxes. For example, Russell's paradox shows that the expression 
  
    
      
        {
        x
         
        
          |
        
         
        x
        ∉
        x
        }
        ,
      
    
    {\displaystyle \{x~|~x\not \in x\},}
  
 although seemingly well formed as a set builder expression, cannot define a set without producing a contradiction.
In cases where the set E is clear from context, it may be not explicitly specified. It is common in the literature for an author to state the domain ahead of time, and then not specify it in the set-builder notation. For example, an author may say something such as, "Unless otherwise stated, variables are to be taken to be natural numbers," though in less formal contexts where the domain can be assumed, a written mention is often unnecessary.

Examples
The following examples illustrate particular sets defined by set-builder notation via predicates. In each case, the domain is specified on the left side of the vertical bar, while the rule is specified on the right side. 

  
    
      
        {
        x
        ∈
        
          R
        
        ∣
        x
        >
        0
        }
      
    
    {\displaystyle \{x\in \mathbb {R} \mid x>0\}}
  
 is the set of all strictly positive real numbers, which can be written in interval notation as 
  
    
      
        (
        0
        ,
        ∞
        )
      
    
    {\displaystyle (0,\infty )}
  
.

  
    
      
        {
        x
        ∈
        
          R
        
        ∣
        
          |
        
        x
        
          |
        
        =
        1
        }
      
    
    {\displaystyle \{x\in \mathbb {R} \mid |x|=1\}}
  
 is the set 
  
    
      
        {
        −
        1
        ,
        1
        }
      
    
    {\displaystyle \{-1,1\}}
  
. This set can also be defined as 
  
    
      
        {
        x
        ∈
        
          R
        
        ∣
        
          x
          
            2
          
        
        =
        1
        }
      
    
    {\displaystyle \{x\in \mathbb {R} \mid x^{2}=1\}}
  
; see equivalent predicates yield equal sets below.
For each integer m, we can define 
  
    
      
        
          G
          
            m
          
        
        =
        {
        x
        ∈
        
          Z
        
        ∣
        x
        ≥
        m
        }
        =
        {
        m
        ,
        m
        +
        1
        ,
        m
        +
        2
        ,
        …
        }
      
    
    {\displaystyle G_{m}=\{x\in \mathbb {Z} \mid x\geq m\}=\{m,m+1,m+2,\ldots \}}
  
. As an example, 
  
    
      
        
          G
          
            3
          
        
        =
        {
        x
        ∈
        
          Z
        
        ∣
        x
        ≥
        3
        }
        =
        {
        3
        ,
        4
        ,
        5
        ,
        …
        }
      
    
    {\displaystyle G_{3}=\{x\in \mathbb {Z} \mid x\geq 3\}=\{3,4,5,\ldots \}}
  
 and 
  
    
      
        
          G
          
            −
            2
          
        
        =
        {
        −
        2
        ,
        −
        1
        ,
        0
        ,
        …
        }
      
    
    {\displaystyle G_{-2}=\{-2,-1,0,\ldots \}}
  
.

  
    
      
        {
        (
        x
        ,
        y
        )
        ∈
        
          R
        
        ×
        
          R
        
        ∣
        0
        <
        y
        <
        f
        (
        x
        )
        }
      
    
    {\displaystyle \{(x,y)\in \mathbb {R} \times \mathbb {R} \mid 0<y<f(x)\}}
  
  is the set of pairs of real numbers such that y is greater than 0 and less than f(x), for a given function f.   Here the cartesian product 
  
    
      
        
          R
        
        ×
        
          R
        
      
    
    {\displaystyle \mathbb {R} \times \mathbb {R} }
  
 denotes the set of ordered pairs of real numbers.

  
    
      
        {
        n
        ∈
        
          N
        
        ∣
        (
        ∃
        k
        )
        [
        k
        ∈
        
          N
        
        ∧
        n
        =
        2
        k
        ]
        }
      
    
    {\displaystyle \{n\in \mathbb {N} \mid (\exists k)[k\in \mathbb {N} \land n=2k]\}}
  
 is the set of all even natural numbers. The 
  
    
      
        ∧
      
    
    {\displaystyle \land }
  
 sign stands for "and", which is known as logical conjunction. The ∃ sign stands for "there exists", which is known as existential quantification. So for example, 
  
    
      
        (
        ∃
        x
        )
        P
        (
        x
        )
      
    
    {\displaystyle (\exists x)P(x)}
  
 is read as  "there exists an x such that P(x)".

  
    
      
        {
        n
        ∣
        (
        ∃
        k
        ∈
        
          N
        
        )
        [
        n
        =
        2
        k
        ]
        }
      
    
    {\displaystyle \{n\mid (\exists k\in \mathbb {N} )[n=2k]\}}
  
 is a notational variant for the same set of even natural numbers. It is not necessary to specify that n is a natural number, as this is implied by the formula on the right.

  
    
      
        {
        a
        ∈
        
          R
        
        ∣
        (
        ∃
        p
        ∈
        
          Z
        
        )
        (
        ∃
        q
        ∈
        
          Z
        
        )
        [
        q
        ≠
        0
        ∧
        a
        q
        =
        p
        ]
        }
      
    
    {\displaystyle \{a\in \mathbb {R} \mid (\exists p\in \mathbb {Z} )(\exists q\in \mathbb {Z} )[q\not =0\land aq=p]\}}
  
 is the set of rational numbers; that is, real numbers that can be written as the ratio of two integers.

More complex expressions on the left side of the notation
An extension of set-builder notation replaces the single variable x with an expression. So instead of  
  
    
      
        {
        x
        ∣
        Φ
        (
        x
        )
        }
      
    
    {\displaystyle \{x\mid \Phi (x)\}}
  
, we may have 
  
    
      
        {
        f
        (
        x
        )
        ∣
        Φ
        (
        x
        )
        }
        ,
      
    
    {\displaystyle \{f(x)\mid \Phi (x)\},}
  
 which should be read

  
    
      
        {
        f
        (
        x
        )
        ∣
        Φ
        (
        x
        )
        }
        =
        {
        y
        ∣
        ∃
        x
        (
        y
        =
        f
        (
        x
        )
        ∧
        Φ
        (
        x
        )
        )
        }
      
    
    {\displaystyle \{f(x)\mid \Phi (x)\}=\{y\mid \exists x(y=f(x)\wedge \Phi (x))\}}
  
.
For example:

  
    
      
        {
        2
        n
        ∣
        n
        ∈
        
          N
        
        }
      
    
    {\displaystyle \{2n\mid n\in \mathbb {N} \}}
  
, where 
  
    
      
        
          N
        
      
    
    {\displaystyle \mathbb {N} }
  
 is the set of all natural numbers, is the set of all even natural numbers.

  
    
      
        {
        p
        
          /
        
        q
        ∣
        p
        ,
        q
        ∈
        
          Z
        
        ,
        q
        ≠
        0
        }
      
    
    {\displaystyle \{p/q\mid p,q\in \mathbb {Z} ,q\not =0\}}
  
, where 
  
    
      
        
          Z
        
      
    
    {\displaystyle \mathbb {Z} }
  
 is the set of all integers, is 
  
    
      
        
          Q
        
        ,
      
    
    {\displaystyle \mathbb {Q} ,}
  
 the set of all rational numbers.

  
    
      
        {
        2
        t
        +
        1
        ∣
        t
        ∈
        
          Z
        
        }
      
    
    {\displaystyle \{2t+1\mid t\in \mathbb {Z} \}}
  
 is the set of odd integers.

  
    
      
        {
        (
        t
        ,
        2
        t
        +
        1
        )
        ∣
        t
        ∈
        
          Z
        
        }
      
    
    {\displaystyle \{(t,2t+1)\mid t\in \mathbb {Z} \}}
  
  creates a set of pairs, where each pair puts an integer into correspondence with an odd integer.
When inverse functions can be explicitly stated, the expression on the left can be eliminated through simple substitution. Consider the example set 
  
    
      
        {
        2
        t
        +
        1
        ∣
        t
        ∈
        
          Z
        
        }
      
    
    {\displaystyle \{2t+1\mid t\in \mathbb {Z} \}}
  
. Make the substitution 
  
    
      
        u
        =
        2
        t
        +
        1
      
    
    {\displaystyle u=2t+1}
  
, which is to say 
  
    
      
        t
        =
        (
        u
        −
        1
        )
        
          /
        
        2
      
    
    {\displaystyle t=(u-1)/2}
  
, then replace t in the set builder notation to find 

  
    
      
        {
        2
        t
        +
        1
        ∣
        t
        ∈
        
          Z
        
        }
        =
        {
        u
        ∣
        (
        u
        −
        1
        )
        
          /
        
        2
        ∈
        
          Z
        
        }
        .
      
    
    {\displaystyle \{2t+1\mid t\in \mathbb {Z} \}=\{u\mid (u-1)/2\in \mathbb {Z} \}.}

Equivalent predicates yield equal sets
Two sets are equal if and only if they have the same elements. Sets defined by set builder notation are equal if and only if their set builder rules, including the domain specifiers, are equivalent. That is 

  
    
      
        {
        x
        ∈
        A
        ∣
        P
        (
        x
        )
        }
        =
        {
        x
        ∈
        B
        ∣
        Q
        (
        x
        )
        }
      
    
    {\displaystyle \{x\in A\mid P(x)\}=\{x\in B\mid Q(x)\}}
  

if and only if 

  
    
      
        (
        ∀
        t
        )
        [
        (
        t
        ∈
        A
        ∧
        P
        (
        t
        )
        )
        ⇔
        (
        t
        ∈
        B
        ∧
        Q
        (
        t
        )
        )
        ]
      
    
    {\displaystyle (\forall t)[(t\in A\land P(t))\Leftrightarrow (t\in B\land Q(t))]}
  
.
Therefore, in order to prove the equality of two sets defined by set builder notation, it suffices to prove the equivalence of their predicates, including the domain qualifiers.
For example,

  
    
      
        {
        x
        ∈
        
          R
        
        ∣
        
          x
          
            2
          
        
        =
        1
        }
        =
        {
        x
        ∈
        
          Q
        
        ∣
        
          |
        
        x
        
          |
        
        =
        1
        }
      
    
    {\displaystyle \{x\in \mathbb {R} \mid x^{2}=1\}=\{x\in \mathbb {Q} \mid |x|=1\}}
  

because the two rule predicates are logically equivalent:

  
    
      
        (
        x
        ∈
        
          R
        
        ∧
        
          x
          
            2
          
        
        =
        1
        )
        ⇔
        (
        x
        ∈
        
          Q
        
        ∧
        
          |
        
        x
        
          |
        
        =
        1
        )
        .
      
    
    {\displaystyle (x\in \mathbb {R} \land x^{2}=1)\Leftrightarrow (x\in \mathbb {Q} \land |x|=1).}
  

This equivalence holds because, for any real number x, we have 
  
    
      
        
          x
          
            2
          
        
        =
        1
      
    
    {\displaystyle x^{2}=1}
  
 if and only if x is a rational number with 
  
    
      
        
          |
        
        x
        
          |
        
        =
        1
      
    
    {\displaystyle |x|=1}
  
. In particular, both sets are equal to the set 
  
    
      
        {
        −
        1
        ,
        1
        }
      
    
    {\displaystyle \{-1,1\}}
  
.

Set existence axiom
In many formal set theories, such as Zermelo–Fraenkel set theory, set builder notation is not part of the formal syntax of the theory. Instead, there is a set existence axiom scheme, which states that if E is a set and Φ(x) is a formula in the language of set theory, then there is a set Y whose members are exactly the elements of E that satisfy Φ:

  
    
      
        (
        ∀
        E
        )
        (
        ∃
        Y
        )
        (
        ∀
        x
        )
        [
        x
        ∈
        Y
        ⇔
        x
        ∈
        E
        ∧
        Φ
        (
        x
        )
        ]
        .
      
    
    {\displaystyle (\forall E)(\exists Y)(\forall x)[x\in Y\Leftrightarrow x\in E\land \Phi (x)].}
  

The set Y obtained from this axiom is exactly the set described in set builder notation as 
  
    
      
        {
        x
        ∈
        E
        ∣
        Φ
        (
        x
        )
        }
      
    
    {\displaystyle \{x\in E\mid \Phi (x)\}}
  
.

In programming languages
A similar notation available in a number of programming languages (notably Python and Haskell) is the list comprehension, which combines map and filter operations over one or more lists.

In Python, the set-builder's braces are replaced with square brackets, parentheses, or curly braces, giving list, generator, and set objects, respectively. Python uses an English-based syntax. Haskell replaces the set-builder's braces with square brackets and uses symbols, including the standard set-builder vertical bar.
The same can be achieved in Scala using Sequence Comprehensions, where the "for" keyword returns a list of the yielded variables using the "yield" keyword.
Consider these set-builder notation examples in some programming languages:

The set builder notation and list comprehension notation are both instances of a more general notation known as monad comprehensions, which permits map/filter-like operations over any monad with a zero element.

See also
Glossary of set theory


== Notes ==

## Related Articles

### Internal Links

- [Abraham Fraenkel](https://en.wikipedia.org/wiki/Abraham_Fraenkel)
- [Almost](https://en.wikipedia.org/wiki/Almost)
- [List of alternative set theories](https://en.wikipedia.org/wiki/List_of_alternative_set_theories)
- [Amorphous set](https://en.wikipedia.org/wiki/Amorphous_set)
- [Axiom](https://en.wikipedia.org/wiki/Axiom)
- [Axiom of adjunction](https://en.wikipedia.org/wiki/Axiom_of_adjunction)
- [Axiom of choice](https://en.wikipedia.org/wiki/Axiom_of_choice)
- [Axiom schema of specification](https://en.wikipedia.org/wiki/Axiom_schema_of_specification)
- [Axiom of constructibility](https://en.wikipedia.org/wiki/Axiom_of_constructibility)
- [Axiom of countable choice](https://en.wikipedia.org/wiki/Axiom_of_countable_choice)
- [Axiom of dependent choice](https://en.wikipedia.org/wiki/Axiom_of_dependent_choice)
- [Axiom of determinacy](https://en.wikipedia.org/wiki/Axiom_of_determinacy)
- [Axiom of extensionality](https://en.wikipedia.org/wiki/Axiom_of_extensionality)
- [Axiom of global choice](https://en.wikipedia.org/wiki/Axiom_of_global_choice)
- [Axiom of infinity](https://en.wikipedia.org/wiki/Axiom_of_infinity)
- [Axiom of limitation of size](https://en.wikipedia.org/wiki/Axiom_of_limitation_of_size)
- [Axiom of pairing](https://en.wikipedia.org/wiki/Axiom_of_pairing)
- [Axiom of power set](https://en.wikipedia.org/wiki/Axiom_of_power_set)
- [Axiom of projective determinacy](https://en.wikipedia.org/wiki/Axiom_of_projective_determinacy)
- [Axiom of regularity](https://en.wikipedia.org/wiki/Axiom_of_regularity)
- [Axiom of union](https://en.wikipedia.org/wiki/Axiom_of_union)
- [Axiom schema](https://en.wikipedia.org/wiki/Axiom_schema)
- [Axiom schema of replacement](https://en.wikipedia.org/wiki/Axiom_schema_of_replacement)
- [Axiom schema of specification](https://en.wikipedia.org/wiki/Axiom_schema_of_specification)
- [Bertrand Russell](https://en.wikipedia.org/wiki/Bertrand_Russell)
- [Bijection](https://en.wikipedia.org/wiki/Bijection)
- [Burali-Forti paradox](https://en.wikipedia.org/wiki/Burali-Forti_paradox)
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Cantor's diagonal argument](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument)
- [Cantor's theorem](https://en.wikipedia.org/wiki/Cantor%27s_theorem)
- [Cardinal number](https://en.wikipedia.org/wiki/Cardinal_number)
- [Cardinality](https://en.wikipedia.org/wiki/Cardinality)
- [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product)
- [Class (set theory)](https://en.wikipedia.org/wiki/Class_(set_theory))
- [Colon (punctuation)](https://en.wikipedia.org/wiki/Colon_(punctuation))
- [Complement (set theory)](https://en.wikipedia.org/wiki/Complement_(set_theory))
- [Computable set](https://en.wikipedia.org/wiki/Computable_set)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Constructible universe](https://en.wikipedia.org/wiki/Constructible_universe)
- [Continuum hypothesis](https://en.wikipedia.org/wiki/Continuum_hypothesis)
- [Countable set](https://en.wikipedia.org/wiki/Countable_set)
- [De Morgan's laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws)
- [Dedekind-infinite set](https://en.wikipedia.org/wiki/Dedekind-infinite_set)
- [Disjoint union](https://en.wikipedia.org/wiki/Disjoint_union)
- [Domain of discourse](https://en.wikipedia.org/wiki/Domain_of_discourse)
- [Element (mathematics)](https://en.wikipedia.org/wiki/Element_(mathematics))
- [Empty set](https://en.wikipedia.org/wiki/Empty_set)
- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Ernst Zermelo](https://en.wikipedia.org/wiki/Ernst_Zermelo)
- [Parity (mathematics)](https://en.wikipedia.org/wiki/Parity_(mathematics))
- [Parity (mathematics)](https://en.wikipedia.org/wiki/Parity_(mathematics))
- [Existential quantification](https://en.wikipedia.org/wiki/Existential_quantification)
- [Expression (mathematics)](https://en.wikipedia.org/wiki/Expression_(mathematics))
- [Family of sets](https://en.wikipedia.org/wiki/Family_of_sets)
- [Filter (higher-order function)](https://en.wikipedia.org/wiki/Filter_(higher-order_function))
- [Filter (set theory)](https://en.wikipedia.org/wiki/Filter_(set_theory))
- [Finite set](https://en.wikipedia.org/wiki/Finite_set)
- [Forcing (mathematics)](https://en.wikipedia.org/wiki/Forcing_(mathematics))
- [Function (mathematics)](https://en.wikipedia.org/wiki/Function_(mathematics))
- [Fuzzy set](https://en.wikipedia.org/wiki/Fuzzy_set)
- [General set theory](https://en.wikipedia.org/wiki/General_set_theory)
- [Generator (computer programming)](https://en.wikipedia.org/wiki/Generator_(computer_programming))
- [Georg Cantor](https://en.wikipedia.org/wiki/Georg_Cantor)
- [Glossary of set theory](https://en.wikipedia.org/wiki/Glossary_of_set_theory)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Hereditarily finite set](https://en.wikipedia.org/wiki/Hereditarily_finite_set)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Infinite set](https://en.wikipedia.org/wiki/Infinite_set)
- [Integer](https://en.wikipedia.org/wiki/Integer)
- [Intension](https://en.wikipedia.org/wiki/Intension)
- [Intersection (set theory)](https://en.wikipedia.org/wiki/Intersection_(set_theory))
- [Interval (mathematics)](https://en.wikipedia.org/wiki/Interval_(mathematics))
- [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann)
- [Julia (programming language)](https://en.wikipedia.org/wiki/Julia_(programming_language))
- [Kripke–Platek set theory](https://en.wikipedia.org/wiki/Kripke%E2%80%93Platek_set_theory)
- [Kurt Gödel](https://en.wikipedia.org/wiki/Kurt_G%C3%B6del)
- [Large cardinal](https://en.wikipedia.org/wiki/Large_cardinal)
- [List (abstract data type)](https://en.wikipedia.org/wiki/List_(abstract_data_type))
- [List comprehension](https://en.wikipedia.org/wiki/List_comprehension)
- [List of set identities and relations](https://en.wikipedia.org/wiki/List_of_set_identities_and_relations)
- [Logic](https://en.wikipedia.org/wiki/Logic)
- [Logical conjunction](https://en.wikipedia.org/wiki/Logical_conjunction)
- [Map (higher-order function)](https://en.wikipedia.org/wiki/Map_(higher-order_function))
- [Martin's axiom](https://en.wikipedia.org/wiki/Martin%27s_axiom)
- [Mathematical notation](https://en.wikipedia.org/wiki/Mathematical_notation)
- [Mathematics](https://en.wikipedia.org/wiki/Mathematics)
- [Monad (functional programming)](https://en.wikipedia.org/wiki/Monad_(functional_programming))
- [Morse–Kelley set theory](https://en.wikipedia.org/wiki/Morse%E2%80%93Kelley_set_theory)
- [Naive set theory](https://en.wikipedia.org/wiki/Naive_set_theory)
- [Natural number](https://en.wikipedia.org/wiki/Natural_number)
- [New Foundations](https://en.wikipedia.org/wiki/New_Foundations)
- [Ordered pair](https://en.wikipedia.org/wiki/Ordered_pair)
- [Ordinal number](https://en.wikipedia.org/wiki/Ordinal_number)
- [Paradoxes of set theory](https://en.wikipedia.org/wiki/Paradoxes_of_set_theory)
- [Paul Bernays](https://en.wikipedia.org/wiki/Paul_Bernays)
- [Paul Cohen](https://en.wikipedia.org/wiki/Paul_Cohen)
- [Sign (mathematics)](https://en.wikipedia.org/wiki/Sign_(mathematics))
- [Power set](https://en.wikipedia.org/wiki/Power_set)
- [Predicate (mathematical logic)](https://en.wikipedia.org/wiki/Predicate_(mathematical_logic))
- [Principia Mathematica](https://en.wikipedia.org/wiki/Principia_Mathematica)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Prolog](https://en.wikipedia.org/wiki/Prolog)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Rational number](https://en.wikipedia.org/wiki/Rational_number)
- [Real number](https://en.wikipedia.org/wiki/Real_number)
- [Richard Dedekind](https://en.wikipedia.org/wiki/Richard_Dedekind)
- [Russell's paradox](https://en.wikipedia.org/wiki/Russell%27s_paradox)
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Set (mathematics)](https://en.wikipedia.org/wiki/Set_(mathematics))
- [Element (mathematics)](https://en.wikipedia.org/wiki/Element_(mathematics))
- [Set theory](https://en.wikipedia.org/wiki/Set_theory)
- [Singleton (mathematics)](https://en.wikipedia.org/wiki/Singleton_(mathematics))
- [Subset](https://en.wikipedia.org/wiki/Subset)
- [Suslin's problem](https://en.wikipedia.org/wiki/Suslin%27s_problem)
- [Symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference)
- [Tarski–Grothendieck set theory](https://en.wikipedia.org/wiki/Tarski%E2%80%93Grothendieck_set_theory)
- [Thomas Jech](https://en.wikipedia.org/wiki/Thomas_Jech)
- [Thoralf Skolem](https://en.wikipedia.org/wiki/Thoralf_Skolem)
- [Transfinite induction](https://en.wikipedia.org/wiki/Transfinite_induction)
- [Transitive set](https://en.wikipedia.org/wiki/Transitive_set)
- [Tuple](https://en.wikipedia.org/wiki/Tuple)
- [Ultrafilter on a set](https://en.wikipedia.org/wiki/Ultrafilter_on_a_set)
- [Uncountable set](https://en.wikipedia.org/wiki/Uncountable_set)
- [Union (set theory)](https://en.wikipedia.org/wiki/Union_(set_theory))
- [Universal set](https://en.wikipedia.org/wiki/Universal_set)
- [Venn diagram](https://en.wikipedia.org/wiki/Venn_diagram)
- [Vertical bar](https://en.wikipedia.org/wiki/Vertical_bar)
- [Von Neumann–Bernays–Gödel set theory](https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Bernays%E2%80%93G%C3%B6del_set_theory)
- [Willard Van Orman Quine](https://en.wikipedia.org/wiki/Willard_Van_Orman_Quine)
- [Wolfram Mathematica](https://en.wikipedia.org/wiki/Wolfram_Mathematica)
- [Zermelo set theory](https://en.wikipedia.org/wiki/Zermelo_set_theory)
- [Zermelo–Fraenkel set theory](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory)
- [Zero element](https://en.wikipedia.org/wiki/Zero_element)
- [Talk:Set-builder notation](https://en.wikipedia.org/wiki/Talk:Set-builder_notation)
- [Wikipedia:Section move](https://en.wikipedia.org/wiki/Wikipedia:Section_move)
- [Template:Set theory](https://en.wikipedia.org/wiki/Template:Set_theory)
- [Template talk:Set theory](https://en.wikipedia.org/wiki/Template_talk:Set_theory)
- [Category:Articles to be split from December 2023](https://en.wikipedia.org/wiki/Category:Articles_to_be_split_from_December_2023)
- [Category:Articles to have a section moved from December 2023](https://en.wikipedia.org/wiki/Category:Articles_to_have_a_section_moved_from_December_2023)
- [Category:Set theorists](https://en.wikipedia.org/wiki/Category:Set_theorists)
- [Category:Use dmy dates from December 2020](https://en.wikipedia.org/wiki/Category:Use_dmy_dates_from_December_2020)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:48:03.838968+00:00_