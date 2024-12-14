# Lambda calculus

## Article Metadata

- **Last Updated:** 2024-12-14T19:39:21.640794+00:00
- **Original Article:** [Lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus)
- **Language:** en
- **Page ID:** 18203

## Summary

Lambda calculus (also written as λ-calculus) is a formal system in mathematical logic for expressing computation based on function abstraction and application using variable binding and substitution. Untyped lambda calculus, the topic of this article, is a universal machine, a model of computation that can be used to simulate any Turing machine (and vice versa). It was introduced by the mathematician Alonzo Church in the 1930s as part of his research into the foundations of mathematics. In 1936,

## Categories

- Category:1936 in computing
- Category:Articles with example Lisp (programming language) code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Commons category link from Wikidata
- Category:Computability theory
- Category:Formal methods
- Category:Lambda calculus
- Category:Models of computation
- Category:Programming language comparisons
- Category:Short description is different from Wikidata
- Category:Theoretical computer science
- Category:Webarchive template wayback links

## Table of Contents

- Explanation and applications
- History
- Informal description
- Formal definition
- Reduction
- Normal forms and confluence
- Encoding datatypes
- Additional programming techniques
- Typed lambda calculus
- Reduction strategies
- Computability
- Complexity
- Lambda calculus and programming languages
- Semantics
- Variations and extensions
- See also
- Further reading
- Notes
- References
- External links

## Content

Lambda calculus (also written as λ-calculus) is a formal system in mathematical logic for expressing computation based on function abstraction and application using variable binding and substitution. Untyped lambda calculus, the topic of this article, is a universal machine, a model of computation that can be used to simulate any Turing machine (and vice versa). It was introduced by the mathematician Alonzo Church in the 1930s as part of his research into the foundations of mathematics. In 1936, Church found a formulation which was logically consistent, and documented it in 1940.
Lambda calculus consists of constructing lambda terms and performing reduction operations on them. A term is defined as any valid lambda calculus expression. In the simplest form of lambda calculus, terms are built using only the following rules:

  
    
      
        x
      
    
    {\textstyle x}
  
: A variable is a character or string representing a parameter.

  
    
      
        (
        λ
        x
        .
        M
        )
      
    
    {\textstyle (\lambda x.M)}
  
: A lambda abstraction is a function definition, taking as input the bound variable 
  
    
      
        x
      
    
    {\displaystyle x}
  
 (between the λ and the punctum/dot .) and returning the body 
  
    
      
        M
      
    
    {\textstyle M}
  
.

  
    
      
        (
        M
         
        N
        )
      
    
    {\textstyle (M\ N)}
  
: An application, applying a function 
  
    
      
        M
      
    
    {\textstyle M}
  
 to an argument 
  
    
      
        N
      
    
    {\textstyle N}
  
. Both 
  
    
      
        M
      
    
    {\textstyle M}
  
 and 
  
    
      
        N
      
    
    {\textstyle N}
  
 are lambda terms.
The reduction operations include:

  
    
      
        (
        λ
        x
        .
        M
        [
        x
        ]
        )
        →
        (
        λ
        y
        .
        M
        [
        y
        ]
        )
      
    
    {\textstyle (\lambda x.M[x])\rightarrow (\lambda y.M[y])}
  
 : α-conversion, renaming the bound variables in the expression. Used to avoid name collisions.

  
    
      
        (
        (
        λ
        x
        .
        M
        )
         
        N
        )
        →
        (
        M
        [
        x
        :=
        N
        ]
        )
      
    
    {\textstyle ((\lambda x.M)\ N)\rightarrow (M[x:=N])}
  
 : β-reduction, replacing the bound variables with the argument expression in the body of the abstraction.
If De Bruijn indexing is used, then α-conversion is no longer required as there will be no name collisions. If repeated application of the reduction steps eventually terminates, then by the Church–Rosser theorem it will produce a β-normal form.
Variable names are not needed if using a universal lambda function, such as Iota and Jot, which can create any function behavior by calling it on itself in various combinations.

Explanation and applications
Lambda calculus is Turing complete, that is, it is a universal model of computation that can be used to simulate any Turing machine. Its namesake, the Greek letter lambda (λ), is used in lambda expressions and lambda terms to denote binding a variable in a function.
Lambda calculus may be untyped or typed. In typed lambda calculus, functions can be applied only if they are capable of accepting the given input's "type" of data. Typed lambda calculi are strictly weaker than the untyped lambda calculus, which is the primary subject of this article, in the sense that typed lambda calculi can express less than the untyped calculus can. On the other hand, typed lambda calculi allow more things to be proven. For example, in simply typed lambda calculus, it is a theorem that every evaluation strategy terminates for every simply typed lambda-term, whereas evaluation of untyped lambda-terms need not terminate (see below). One reason there are many different typed lambda calculi has been the desire to do more (of what the untyped calculus can do) without giving up on being able to prove strong theorems about the calculus.
Lambda calculus has applications in many different areas in mathematics, philosophy, linguistics, and computer science.
 Lambda calculus has played an important role in the development of the theory of programming languages. Functional programming languages implement lambda calculus. Lambda calculus is also a current research topic in category theory.

History
Lambda calculus was introduced by mathematician Alonzo Church in the 1930s as part of an investigation into the foundations of mathematics. The original system was shown to be logically inconsistent in 1935 when Stephen Kleene and J. B. Rosser developed the Kleene–Rosser paradox.
Subsequently, in 1936 Church isolated and published just the portion relevant to computation, what is now called the untyped lambda calculus. In 1940, he also introduced a computationally weaker, but logically consistent system, known as the simply typed lambda calculus.
Until the 1960s when its relation to programming languages was clarified, the lambda calculus was only a formalism. Thanks to Richard Montague and other linguists' applications in the semantics of natural language, the lambda calculus has begun to enjoy a respectable place in both linguistics and computer science.

Origin of the λ symbol
There is some uncertainty over the reason for Church's use of the Greek letter lambda (λ) as the notation for function-abstraction in the lambda calculus, perhaps in part due to conflicting explanations by Church himself. According to Cardone and Hindley (2006):

By the way, why did Church choose the notation “λ”? In [an unpublished 1964 letter to Harald Dickson] he stated clearly that it came from the notation “
  
    
      
        
          
            
              x
              ^
            
          
        
      
    
    {\displaystyle {\hat {x}}}
  
” used for class-abstraction by Whitehead and Russell, by first modifying “
  
    
      
        
          
            
              x
              ^
            
          
        
      
    
    {\displaystyle {\hat {x}}}
  
” to “
  
    
      
        ∧
        x
      
    
    {\displaystyle \land x}
  
” to distinguish function-abstraction from class-abstraction, and then changing “
  
    
      
        ∧
      
    
    {\displaystyle \land }
  
” to “λ” for ease of printing.
This origin was also reported in [Rosser, 1984, p.338]. On the other hand, in his later years Church told two enquirers that the choice was more accidental: a symbol was needed and λ just happened to be chosen.

Dana Scott has also addressed this question in various public lectures.
Scott recounts that he once posed a question about the origin of the lambda symbol to Church's former student and son-in-law John W. Addison Jr., who then wrote his father-in-law a postcard:

Dear Professor Church,
Russell had the iota operator, Hilbert had the epsilon operator. Why did you choose lambda for your operator?

According to Scott, Church's entire response consisted of returning the postcard with the following annotation: "eeny, meeny, miny, moe".

Informal description
Motivation
Computable functions are a fundamental concept within computer science and mathematics. The lambda calculus provides simple semantics for computation which are useful for formally studying properties of computation. The lambda calculus incorporates two simplifications that make its semantics simple.
The first simplification is that the lambda calculus treats functions "anonymously;" it does not give them explicit names. For example, the function

  
    
      
        
          s
          q
          u
          a
          r
          e
          _
          s
          u
          m
        
        ⁡
        (
        x
        ,
        y
        )
        =
        
          x
          
            2
          
        
        +
        
          y
          
            2
          
        
      
    
    {\displaystyle \operatorname {square\_sum} (x,y)=x^{2}+y^{2}}
  

can be rewritten in anonymous form as

  
    
      
        (
        x
        ,
        y
        )
        ↦
        
          x
          
            2
          
        
        +
        
          y
          
            2
          
        
      
    
    {\displaystyle (x,y)\mapsto x^{2}+y^{2}}
  

(which is read as "a tuple of x and y is mapped to 
  
    
      
        
          x
          
            2
          
        
        +
        
          y
          
            2
          
        
      
    
    {\textstyle x^{2}+y^{2}}
  
"). Similarly, the function

  
    
      
        id
        ⁡
        (
        x
        )
        =
        x
      
    
    {\displaystyle \operatorname {id} (x)=x}
  

can be rewritten in anonymous form as

  
    
      
        x
        ↦
        x
      
    
    {\displaystyle x\mapsto x}
  

where the input is simply mapped to itself.
The second simplification is that the lambda calculus only uses functions of a single input. An ordinary function that requires two inputs, for instance the 
  
    
      
        
          s
          q
          u
          a
          r
          e
          _
          s
          u
          m
        
      
    
    {\textstyle \operatorname {square\_sum} }
  
 function, can be reworked into an equivalent function that accepts a single input, and as output returns another function, that in turn accepts a single input. For example,

  
    
      
        (
        x
        ,
        y
        )
        ↦
        
          x
          
            2
          
        
        +
        
          y
          
            2
          
        
      
    
    {\displaystyle (x,y)\mapsto x^{2}+y^{2}}
  

can be reworked into

  
    
      
        x
        ↦
        (
        y
        ↦
        
          x
          
            2
          
        
        +
        
          y
          
            2
          
        
        )
      
    
    {\displaystyle x\mapsto (y\mapsto x^{2}+y^{2})}
  

This method, known as currying, transforms a function that takes multiple arguments into a chain of functions each with a single argument.
Function application of the 
  
    
      
        
          s
          q
          u
          a
          r
          e
          _
          s
          u
          m
        
      
    
    {\textstyle \operatorname {square\_sum} }
  
 function to the arguments (5, 2), yields at once

  
    
      
        (
        (
        x
        ,
        y
        )
        ↦
        
          x
          
            2
          
        
        +
        
          y
          
            2
          
        
        )
        (
        5
        ,
        2
        )
      
    
    {\textstyle ((x,y)\mapsto x^{2}+y^{2})(5,2)}
  

  
    
      
        =
        
          5
          
            2
          
        
        +
        
          2
          
            2
          
        
      
    
    {\textstyle =5^{2}+2^{2}}
  

  
    
      
        =
        29
      
    
    {\textstyle =29}
  
,
whereas evaluation of the curried version requires one more step

  
    
      
        
          
            (
          
        
        
          
            (
          
        
        x
        ↦
        (
        y
        ↦
        
          x
          
            2
          
        
        +
        
          y
          
            2
          
        
        )
        
          
            )
          
        
        (
        5
        )
        
          
            )
          
        
        (
        2
        )
      
    
    {\textstyle {\Bigl (}{\bigl (}x\mapsto (y\mapsto x^{2}+y^{2}){\bigr )}(5){\Bigr )}(2)}
  

  
    
      
        =
        (
        y
        ↦
        
          5
          
            2
          
        
        +
        
          y
          
            2
          
        
        )
        (
        2
        )
      
    
    {\textstyle =(y\mapsto 5^{2}+y^{2})(2)}
  
 // the definition of 
  
    
      
        x
      
    
    {\displaystyle x}
  
 has been used with 
  
    
      
        5
      
    
    {\displaystyle 5}
  
 in the inner expression. This is like β-reduction.

  
    
      
        =
        
          5
          
            2
          
        
        +
        
          2
          
            2
          
        
      
    
    {\textstyle =5^{2}+2^{2}}
  
 // the definition of 
  
    
      
        y
      
    
    {\displaystyle y}
  
 has been used with 
  
    
      
        2
      
    
    {\displaystyle 2}
  
. Again, similar to β-reduction.

  
    
      
        =
        29
      
    
    {\textstyle =29}
  

to arrive at the same result.

The lambda calculus
The lambda calculus consists of a language of lambda terms, that are defined by a certain formal syntax, and a set of transformation rules for manipulating the lambda terms. These transformation rules can be viewed as an equational theory or as an operational definition.
As described above, having no names, all functions in the lambda calculus are anonymous functions. They only accept one input variable, so currying is used to implement functions of several variables.

Lambda terms
The syntax of the lambda calculus defines some expressions as valid lambda calculus expressions and some as invalid, just as some strings of characters are valid computer programs and some are not. A valid lambda calculus expression is called a "lambda term".
The following three rules give an inductive definition that can be applied to build all syntactically valid lambda terms:

 variable x is itself a valid lambda term.
if t is a lambda term, and x is a variable, then 
  
    
      
        (
        λ
        x
        .
        t
        )
      
    
    {\displaystyle (\lambda x.t)}
  
  is a lambda term (called an abstraction);
if t and s are lambda terms, then 
  
    
      
        (
        t
      
    
    {\displaystyle (t}
  
  
  
    
      
        s
        )
      
    
    {\displaystyle s)}
  
 is a lambda term (called an application).
Nothing else is a lambda term. That is, a lambda term is valid if and only if it can be obtained by repeated application of these three rules. For convenience, some parentheses can be omitted when writing a lambda term. For example, the outermost parentheses are usually not written. See § Notation, below, for an explicit description of which parentheses are optional. It is also common to extend the syntax presented here with additional operations, which allows making sense of terms such as 
  
    
      
        λ
        x
        .
        
          x
          
            2
          
        
        .
      
    
    {\displaystyle \lambda x.x^{2}.}
  
 The focus of this article is the pure lambda calculus without extensions, but lambda terms extended with arithmetic operations are used for explanatory purposes.
 An abstraction 
  
    
      
        λ
        x
        .
        t
      
    
    {\displaystyle \lambda x.t}
  
 denotes an § anonymous function that takes a single input x and returns t. For example, 
  
    
      
        λ
        x
        .
        (
        
          x
          
            2
          
        
        +
        2
        )
      
    
    {\displaystyle \lambda x.(x^{2}+2)}
  
 is an abstraction representing the function 
  
    
      
        f
      
    
    {\displaystyle f}
  
 defined by 
  
    
      
        f
        (
        x
        )
        =
        
          x
          
            2
          
        
        +
        2
        ,
      
    
    {\displaystyle f(x)=x^{2}+2,}
  
 using the term 
  
    
      
        
          x
          
            2
          
        
        +
        2
      
    
    {\displaystyle x^{2}+2}
  
 for t. The name 
  
    
      
        f
      
    
    {\displaystyle f}
  
 is superfluous when using abstraction. The syntax 
  
    
      
        (
        λ
        x
        .
        t
        )
      
    
    {\displaystyle (\lambda x.t)}
  
 binds the variable x in the term t. The definition of a function with an abstraction merely "sets up" the function but does not invoke it.
 An application 
  
    
      
        t
      
    
    {\displaystyle t}
  
  
  
    
      
        s
      
    
    {\displaystyle s}
  
 represents the application of a function t to an input s, that is, it represents the act of calling function t on input s to produce 
  
    
      
        t
        (
        s
        )
      
    
    {\displaystyle t(s)}
  
.
A lambda term may refer to a variable that has not been bound, such as the term 
  
    
      
        λ
        x
        .
        (
        x
        +
        y
        )
      
    
    {\displaystyle \lambda x.(x+y)}
  
 (which represents the function definition 
  
    
      
        f
        (
        x
        )
        =
        x
        +
        y
      
    
    {\displaystyle f(x)=x+y}
  
). In this term, the variable y has not been defined and is considered an unknown. The abstraction 
  
    
      
        λ
        x
        .
        (
        x
        +
        y
        )
      
    
    {\displaystyle \lambda x.(x+y)}
  
 is a syntactically valid term and represents a function that adds its input to the yet-unknown y.
Parentheses may be used and might be needed to disambiguate terms. For example, 

  
    
      
        λ
        x
        .
        (
        (
        λ
        x
        .
        x
        )
        x
        )
      
    
    {\displaystyle \lambda x.((\lambda x.x)x)}
  
 is of form 
  
    
      
        λ
        x
        .
        B
      
    
    {\displaystyle \lambda x.B}
  
 and is therefore an abstraction, while

  
    
      
        (
        λ
        x
        .
        (
        λ
        x
        .
        x
        )
        )
      
    
    {\displaystyle (\lambda x.(\lambda x.x))}
  
 
  
    
      
        x
      
    
    {\displaystyle x}
  
 is of form 
  
    
      
        M
      
    
    {\displaystyle M}
  
  
  
    
      
        N
      
    
    {\displaystyle N}
  
 and is therefore an application.
The examples 1 and 2 denote different terms, differing only in where the parentheses are placed. They have different meanings: example 1 is a function definition, while example 2 is a function application. The lambda variable x is a placeholder in both examples.
Here, example 1 defines a function 
  
    
      
        λ
        x
        .
        B
      
    
    {\displaystyle \lambda x.B}
  
, where 
  
    
      
        B
      
    
    {\displaystyle B}
  
 is 
  
    
      
        (
        λ
        x
        .
        x
        )
        x
      
    
    {\displaystyle (\lambda x.x)x}
  
, an anonymous function 
  
    
      
        (
        λ
        x
        .
        x
        )
      
    
    {\displaystyle (\lambda x.x)}
  
, with input 
  
    
      
        x
      
    
    {\displaystyle x}
  
; while example 2, 
  
    
      
        M
      
    
    {\displaystyle M}
  
 
  
    
      
        N
      
    
    {\displaystyle N}
  
, is M applied to N, where 
  
    
      
        M
      
    
    {\displaystyle M}
  
 is the lambda term 
  
    
      
        (
        λ
        x
        .
        (
        λ
        x
        .
        x
        )
        )
      
    
    {\displaystyle (\lambda x.(\lambda x.x))}
  
 being applied to the input 
  
    
      
        N
      
    
    {\displaystyle N}
  
 which is 
  
    
      
        x
      
    
    {\displaystyle x}
  
. Both examples 1 and 2 would evaluate to the identity function 
  
    
      
        λ
        x
        .
        x
      
    
    {\displaystyle \lambda x.x}
  
.

Functions that operate on functions
In lambda calculus, functions are taken to be 'first class values', so functions may be used as the inputs, or be returned as outputs from other functions.
For example, the lambda term 
  
    
      
        λ
        x
        .
        x
      
    
    {\displaystyle \lambda x.x}
  
 represents the identity function, 
  
    
      
        x
        ↦
        x
      
    
    {\displaystyle x\mapsto x}
  
. Further, 
  
    
      
        λ
        x
        .
        y
      
    
    {\displaystyle \lambda x.y}
  
 represents the constant function 
  
    
      
        x
        ↦
        y
      
    
    {\displaystyle x\mapsto y}
  
, the function that always returns 
  
    
      
        y
      
    
    {\displaystyle y}
  
, no matter the input. As an example of a function operating on functions, the function composition can be defined as 
  
    
      
        λ
        f
        .
        λ
        g
        .
        λ
        x
        .
        (
        f
        (
        g
        x
        )
        )
      
    
    {\displaystyle \lambda f.\lambda g.\lambda x.(f(gx))}
  
.
There are several notions of "equivalence" and "reduction" that allow lambda terms to be "reduced" to "equivalent" lambda terms.

Alpha equivalence
A basic form of equivalence, definable on lambda terms, is alpha equivalence. It captures the intuition that the particular choice of a bound variable, in an abstraction, does not (usually) matter.
For instance, 
  
    
      
        λ
        x
        .
        x
      
    
    {\displaystyle \lambda x.x}
  
 and 
  
    
      
        λ
        y
        .
        y
      
    
    {\displaystyle \lambda y.y}
  
 are alpha-equivalent lambda terms, and they both represent the same function (the identity function).
The terms 
  
    
      
        x
      
    
    {\displaystyle x}
  
 and 
  
    
      
        y
      
    
    {\displaystyle y}
  
 are not alpha-equivalent, because they are not bound in an abstraction.
In many presentations, it is usual to identify alpha-equivalent lambda terms.
The following definitions are necessary in order to be able to define β-reduction:

Free variables
The free variables
 of a term are those variables not bound by an abstraction. The set of free variables of an expression is defined inductively:

The free variables of 
  
    
      
        x
      
    
    {\displaystyle x}
  
 are just 
  
    
      
        x
      
    
    {\displaystyle x}
  

The set of free variables of 
  
    
      
        λ
        x
        .
        t
      
    
    {\displaystyle \lambda x.t}
  
 is the set of free variables of 
  
    
      
        t
      
    
    {\displaystyle t}
  
, but with 
  
    
      
        x
      
    
    {\displaystyle x}
  
 removed
The set of free variables of 
  
    
      
        t
      
    
    {\displaystyle t}
  
  
  
    
      
        s
      
    
    {\displaystyle s}
  
 is the union of the set of free variables of 
  
    
      
        t
      
    
    {\displaystyle t}
  
 and the set of free variables of 
  
    
      
        s
      
    
    {\displaystyle s}
  
.
For example, the lambda term representing the identity 
  
    
      
        λ
        x
        .
        x
      
    
    {\displaystyle \lambda x.x}
  
 has no free variables, but the function 
  
    
      
        λ
        x
        .
        y
      
    
    {\displaystyle \lambda x.y}
  
 
  
    
      
        x
      
    
    {\displaystyle x}
  
 has a single free variable, 
  
    
      
        y
      
    
    {\displaystyle y}
  
.

Capture-avoiding substitutions
Suppose 
  
    
      
        t
      
    
    {\displaystyle t}
  
, 
  
    
      
        s
      
    
    {\displaystyle s}
  
 and 
  
    
      
        r
      
    
    {\displaystyle r}
  
 are lambda terms, and 
  
    
      
        x
      
    
    {\displaystyle x}
  
 and 
  
    
      
        y
      
    
    {\displaystyle y}
  
 are variables.
The notation 
  
    
      
        t
        [
        x
        :=
        r
        ]
      
    
    {\displaystyle t[x:=r]}
  
 indicates substitution of 
  
    
      
        r
      
    
    {\displaystyle r}
  
 for 
  
    
      
        x
      
    
    {\displaystyle x}
  
 in 
  
    
      
        t
      
    
    {\displaystyle t}
  
 in a capture-avoiding manner. This is defined so that:

  
    
      
        x
        [
        x
        :=
        r
        ]
        =
        r
      
    
    {\displaystyle x[x:=r]=r}
  
 ; with 
  
    
      
        r
      
    
    {\displaystyle r}
  
 substituted for 
  
    
      
        x
      
    
    {\displaystyle x}
  
, 
  
    
      
        x
      
    
    {\displaystyle x}
  
 becomes 
  
    
      
        r
      
    
    {\displaystyle r}
  

  
    
      
        y
        [
        x
        :=
        r
        ]
        =
        y
      
    
    {\displaystyle y[x:=r]=y}
  
 if 
  
    
      
        x
        ≠
        y
      
    
    {\displaystyle x\neq y}
  
 ; with 
  
    
      
        r
      
    
    {\displaystyle r}
  
 substituted for 
  
    
      
        x
      
    
    {\displaystyle x}
  
, 
  
    
      
        y
      
    
    {\displaystyle y}
  
 (which is not 
  
    
      
        x
      
    
    {\displaystyle x}
  
) remains 
  
    
      
        y
      
    
    {\displaystyle y}
  

  
    
      
        (
        t
      
    
    {\displaystyle (t}
  
 
  
    
      
        s
        )
        [
        x
        :=
        r
        ]
        =
        (
        t
        [
        x
        :=
        r
        ]
        )
        (
        s
        [
        x
        :=
        r
        ]
        )
      
    
    {\displaystyle s)[x:=r]=(t[x:=r])(s[x:=r])}
  
 ; substitution distributes to both sides of an application

  
    
      
        (
        λ
        x
        .
        t
        )
        [
        x
        :=
        r
        ]
        =
        λ
        x
        .
        t
      
    
    {\displaystyle (\lambda x.t)[x:=r]=\lambda x.t}
  
 ; a variable bound by an abstraction is not subject to substitution; substituting such variable leaves the abstraction unchanged

  
    
      
        (
        λ
        y
        .
        t
        )
        [
        x
        :=
        r
        ]
        =
        λ
        y
        .
        (
        t
        [
        x
        :=
        r
        ]
        )
      
    
    {\displaystyle (\lambda y.t)[x:=r]=\lambda y.(t[x:=r])}
  
 if 
  
    
      
        x
        ≠
        y
      
    
    {\displaystyle x\neq y}
  
 and 
  
    
      
        y
      
    
    {\displaystyle y}
  
 does not appear among the free variables of 
  
    
      
        r
      
    
    {\displaystyle r}
  
 (
  
    
      
        y
      
    
    {\displaystyle y}
  
 is said to be "fresh" for 
  
    
      
        r
      
    
    {\displaystyle r}
  
) ; substituting a variable which is not bound by an abstraction proceeds in the abstraction's body, provided that the abstracted variable 
  
    
      
        y
      
    
    {\displaystyle y}
  
 is "fresh" for the substitution term 
  
    
      
        r
      
    
    {\displaystyle r}
  
.
For example, 
  
    
      
        (
        λ
        x
        .
        x
        )
        [
        y
        :=
        y
        ]
        =
        λ
        x
        .
        (
        x
        [
        y
        :=
        y
        ]
        )
        =
        λ
        x
        .
        x
      
    
    {\displaystyle (\lambda x.x)[y:=y]=\lambda x.(x[y:=y])=\lambda x.x}
  
, and 
  
    
      
        (
        (
        λ
        x
        .
        y
        )
        x
        )
        [
        x
        :=
        y
        ]
        =
        (
        (
        λ
        x
        .
        y
        )
        [
        x
        :=
        y
        ]
        )
        (
        x
        [
        x
        :=
        y
        ]
        )
        =
        (
        λ
        x
        .
        y
        )
        y
      
    
    {\displaystyle ((\lambda x.y)x)[x:=y]=((\lambda x.y)[x:=y])(x[x:=y])=(\lambda x.y)y}
  
.
The freshness condition (requiring that 
  
    
      
        y
      
    
    {\displaystyle y}
  
 is not in the free variables of 
  
    
      
        r
      
    
    {\displaystyle r}
  
) is crucial in order to ensure that substitution does not change the meaning of functions.
For example, a substitution that ignores the freshness condition could lead to errors: 
  
    
      
        (
        λ
        x
        .
        y
        )
        [
        y
        :=
        x
        ]
        =
        λ
        x
        .
        (
        y
        [
        y
        :=
        x
        ]
        )
        =
        λ
        x
        .
        x
      
    
    {\displaystyle (\lambda x.y)[y:=x]=\lambda x.(y[y:=x])=\lambda x.x}
  
. This erroneous substitution would turn the constant function 
  
    
      
        λ
        x
        .
        y
      
    
    {\displaystyle \lambda x.y}
  
 into the identity 
  
    
      
        λ
        x
        .
        x
      
    
    {\displaystyle \lambda x.x}
  
.
In general, failure to meet the freshness condition can be remedied by alpha-renaming first, with a suitable fresh variable.
For example, switching back to our correct notion of substitution, in 
  
    
      
        (
        λ
        x
        .
        y
        )
        [
        y
        :=
        x
        ]
      
    
    {\displaystyle (\lambda x.y)[y:=x]}
  
 the abstraction can be renamed with a fresh variable 
  
    
      
        z
      
    
    {\displaystyle z}
  
, to obtain 
  
    
      
        (
        λ
        z
        .
        y
        )
        [
        y
        :=
        x
        ]
        =
        λ
        z
        .
        (
        y
        [
        y
        :=
        x
        ]
        )
        =
        λ
        z
        .
        x
      
    
    {\displaystyle (\lambda z.y)[y:=x]=\lambda z.(y[y:=x])=\lambda z.x}
  
, and the meaning of the function is preserved by substitution.

β-reduction
The β-reduction rule states that an application of the form 
  
    
      
        (
        λ
        x
        .
        t
        )
        s
      
    
    {\displaystyle (\lambda x.t)s}
  
 reduces to the term 
  
    
      
        t
        [
        x
        :=
        s
        ]
      
    
    {\displaystyle t[x:=s]}
  
. The notation 
  
    
      
        (
        λ
        x
        .
        t
        )
        s
        →
        t
        [
        x
        :=
        s
        ]
      
    
    {\displaystyle (\lambda x.t)s\to t[x:=s]}
  
 is used to indicate that 
  
    
      
        (
        λ
        x
        .
        t
        )
        s
      
    
    {\displaystyle (\lambda x.t)s}
  
 β-reduces to 
  
    
      
        t
        [
        x
        :=
        s
        ]
      
    
    {\displaystyle t[x:=s]}
  
.
For example, for every 
  
    
      
        s
      
    
    {\displaystyle s}
  
, 
  
    
      
        (
        λ
        x
        .
        x
        )
        s
        →
        x
        [
        x
        :=
        s
        ]
        =
        s
      
    
    {\displaystyle (\lambda x.x)s\to x[x:=s]=s}
  
. This demonstrates that 
  
    
      
        λ
        x
        .
        x
      
    
    {\displaystyle \lambda x.x}
  
 really is the identity.
Similarly, 
  
    
      
        (
        λ
        x
        .
        y
        )
        s
        →
        y
        [
        x
        :=
        s
        ]
        =
        y
      
    
    {\displaystyle (\lambda x.y)s\to y[x:=s]=y}
  
, which demonstrates that 
  
    
      
        λ
        x
        .
        y
      
    
    {\displaystyle \lambda x.y}
  
 is a constant function.
The lambda calculus may be seen as an idealized version of a functional programming language, like Haskell or Standard ML. Under this view, β-reduction corresponds to a computational step. This step can be repeated by additional β-reductions until there are no more applications left to reduce. In the untyped lambda calculus, as presented here, this reduction process may not terminate. For instance, consider the term 
  
    
      
        Ω
        =
        (
        λ
        x
        .
        x
        x
        )
        (
        λ
        x
        .
        x
        x
        )
      
    
    {\displaystyle \Omega =(\lambda x.xx)(\lambda x.xx)}
  
.
Here 
  
    
      
        (
        λ
        x
        .
        x
        x
        )
        (
        λ
        x
        .
        x
        x
        )
        →
        (
        x
        x
        )
        [
        x
        :=
        λ
        x
        .
        x
        x
        ]
        =
        (
        x
        [
        x
        :=
        λ
        x
        .
        x
        x
        ]
        )
        (
        x
        [
        x
        :=
        λ
        x
        .
        x
        x
        ]
        )
        =
        (
        λ
        x
        .
        x
        x
        )
        (
        λ
        x
        .
        x
        x
        )
      
    
    {\displaystyle (\lambda x.xx)(\lambda x.xx)\to (xx)[x:=\lambda x.xx]=(x[x:=\lambda x.xx])(x[x:=\lambda x.xx])=(\lambda x.xx)(\lambda x.xx)}
  
.
That is, the term reduces to itself in a single β-reduction, and therefore the reduction process will never terminate.
Another aspect of the untyped lambda calculus is that it does not distinguish between different kinds of data. For instance, it may be desirable to write a function that only operates on numbers. However, in the untyped lambda calculus, there is no way to prevent a function from being applied to truth values, strings, or other non-number objects.

Formal definition
Definition
Lambda expressions are composed of:

variables v1, v2, ...;
the abstraction symbols λ (lambda) and . (dot);
parentheses ().
The set of lambda expressions, Λ, can be defined inductively:

If x is a variable, then x ∈ Λ.
If x is a variable and M ∈ Λ, then (λx.M) ∈ Λ.
If M, N ∈ Λ, then (M N) ∈ Λ.
Instances of rule 2 are known as abstractions and instances of rule 3 are known as applications. See § reducible expression
This set of rules may be written in Backus–Naur form as:

Notation
To keep the notation of lambda expressions uncluttered, the following conventions are usually applied:

Outermost parentheses are dropped: M N instead of (M N).
Applications are assumed to be left associative: M N P may be written instead of ((M N) P).
When all variables are single-letter, the space in applications may be omitted: MNP instead of M N P.
The body of an abstraction extends as far right as possible: λx.M N means λx.(M N) and not (λx.M) N.
A sequence of abstractions is contracted: λx.λy.λz.N is abbreviated as λxyz.N.

Free and bound variables
The abstraction operator, λ, is said to bind its variable wherever it occurs in the body of the abstraction. Variables that fall within the scope of an abstraction are said to be bound. In an expression λx.M, the part λx is often called binder, as a hint that the variable x is getting bound by prepending λx to M. All other variables are called free. For example, in the expression λy.x x y, y is a bound variable and x is a free variable. Also a variable is bound by its nearest abstraction. In the following example the single occurrence of x in the expression is bound by the second lambda: λx.y (λx.z x).
The set of free variables of a lambda expression, M, is denoted as FV(M) and is defined by recursion on the structure of the terms, as follows:

FV(x) = {x}, where x is a variable.
 FV(λx.M) = FV(M) \ {x}.
 FV(M N) = FV(M) ∪ FV(N).
An expression that contains no free variables is said to be closed. Closed lambda expressions are also known as combinators and are equivalent to terms in combinatory logic.

Reduction
The meaning of lambda expressions is defined by how expressions can be reduced.
There are three kinds of reduction:

α-conversion: changing bound variables;
β-reduction: applying functions to their arguments;
η-reduction: which captures a notion of extensionality.
We also speak of the resulting equivalences: two expressions are α-equivalent, if they can be α-converted into the same expression. β-equivalence and η-equivalence are defined similarly.
The term redex, short for reducible expression, refers to subterms that can be reduced by one of the reduction rules. For example, (λx.M) N is a β-redex in expressing the substitution of N for x in M. The expression to which a redex reduces is called its reduct; the reduct of (λx.M) N is M[x := N].
If x is not free in M, λx.M x is also an η-redex, with a reduct of M.

α-conversion
α-conversion (alpha-conversion), sometimes known as α-renaming, allows bound variable names to be changed. For example, α-conversion of λx.x might yield λy.y. Terms that differ only by α-conversion are called α-equivalent. Frequently, in uses of lambda calculus, α-equivalent terms are considered to be equivalent.
The precise rules for α-conversion are not completely trivial. First, when α-converting an abstraction, the only variable occurrences that are renamed are those that are bound to the same abstraction. For example, an α-conversion of λx.λx.x could result in λy.λx.x, but it could not result in λy.λx.y. The latter has a different meaning from the original. This is analogous to the programming notion of variable shadowing.
Second, α-conversion is not possible if it would result in a variable getting captured by a different abstraction. For example, if we replace x with y in λx.λy.x, we get λy.λy.y, which is not at all the same.
In programming languages with static scope, α-conversion can be used to make name resolution simpler by ensuring that no variable name masks a name in a containing scope (see α-renaming to make name resolution trivial).
In the De Bruijn index notation, any two α-equivalent terms are syntactically identical.

Substitution
Substitution, written M[x := N], is the process of replacing all free occurrences of the variable x in the expression M with expression N. Substitution on terms of the lambda calculus is defined by recursion on the structure of terms, as follows (note: x and y are only variables while M and N are any lambda expression):

x[x := N] = N
y[x := N] = y, if x ≠ y
(M1 M2)[x := N] = M1[x := N] M2[x := N]
(λx.M)[x := N] = λx.M
(λy.M)[x := N] = λy.(M[x := N]), if x ≠ y and y ∉ FV(N)  See above for the FV
To substitute into an abstraction, it is sometimes necessary to α-convert the expression. For example, it is not correct for (λx.y)[y := x] to result in λx.x, because the substituted x was supposed to be free but ended up being bound. The correct substitution in this case is λz.x, up to α-equivalence. Substitution is defined uniquely up to α-equivalence. See Capture-avoiding substitutions above

β-reduction
β-reduction (beta reduction) captures the idea of function application. β-reduction is defined in terms of substitution: the β-reduction of (λx.M) N is M[x := N].
For example, assuming some encoding of 2, 7, ×, we have the following β-reduction: (λn.n × 2) 7 → 7 × 2.
β-reduction can be seen to be the same as the concept of local reducibility in natural deduction, via the Curry–Howard isomorphism.

η-reduction
η-reduction (eta reduction) expresses the idea of extensionality, which in this context is that two functions are the same if and only if they give the same result for all arguments. η-reduction converts between λx.f x and f whenever x does not appear free in f.
η-reduction can be seen to be the same as the concept of local completeness in natural deduction, via the Curry–Howard isomorphism.

Normal forms and confluence
For the untyped lambda calculus, β-reduction as a rewriting rule is neither strongly normalising nor weakly normalising.
However, it can be shown that β-reduction is confluent when working up to α-conversion (i.e. we consider two normal forms to be equal if it is possible to α-convert one into the other).
Therefore, both strongly normalising terms and weakly normalising terms have a unique normal form. For strongly normalising terms, any reduction strategy is guaranteed to yield the normal form, whereas for weakly normalising terms, some reduction strategies may fail to find it.

Encoding datatypes
The basic lambda calculus may be used to model arithmetic, Booleans, data structures, and recursion, as illustrated in the following sub-sections i, ii, iii, and § iv.

Arithmetic in lambda calculus
There are several possible ways to define the natural numbers in lambda calculus, but by far the most common are the Church numerals, which can be defined as follows:

0 := λf.λx.x
1 := λf.λx.f x
2 := λf.λx.f (f x)
3 := λf.λx.f (f (f x))
and so on. Or using the alternative syntax presented above in Notation:

0 := λfx.x
1 := λfx.f x
2 := λfx.f (f x)
3 := λfx.f (f (f x))
A Church numeral is a higher-order function—it takes a single-argument function f, and returns another single-argument function. The Church numeral n is a function that takes a function f as argument and returns the n-th composition of f, i.e. the function f composed with itself n times. This is denoted f(n) and is in fact the n-th power of f (considered as an operator); f(0) is defined to be the identity function. Such repeated compositions (of a single function f) obey the laws of exponents, which is why these numerals can be used for arithmetic. (In Church's original lambda calculus, the formal parameter of a lambda expression was required to occur at least once in the function body, which made the above definition of 0 impossible.)
One way of thinking about the Church numeral n, which is often useful when analysing programs, is as an instruction 'repeat n times'. For example, using the PAIR and NIL functions defined below, one can define a function that constructs a (linked) list of n elements all equal to x by repeating 'prepend another x element' n times, starting from an empty list. The lambda term is

λn.λx.n (PAIR x) NIL
By varying what is being repeated, and varying what argument that function being repeated is applied to, a great many different effects can be achieved.
We can define a successor function, which takes a Church numeral n and returns n + 1 by adding another application of f, where '(mf)x' means the function 'f' is applied 'm' times on 'x':

SUCC := λn.λf.λx.f (n f x)
Because the m-th composition of f composed with the n-th composition of f gives the m+n-th composition of f, addition can be defined as follows:

PLUS := λm.λn.λf.λx.m f (n f x)
PLUS can be thought of as a function taking two natural numbers as arguments and returning a natural number; it can be verified that

PLUS 2 3
and

5
are β-equivalent lambda expressions. Since adding m to a number n can be accomplished by adding 1 m times, an alternative definition is:

PLUS := λm.λn.m SUCC n 
Similarly, multiplication can be defined as

MULT := λm.λn.λf.m (n f)
Alternatively

MULT := λm.λn.m (PLUS n) 0
since multiplying m and n is the same as repeating the add n function m times and then applying it to zero.
Exponentiation has a rather simple rendering in Church numerals, namely

POW := λb.λe.e b
The predecessor function defined by PRED n = n − 1 for a positive integer n and PRED 0 = 0 is considerably more difficult. The formula

PRED := λn.λf.λx.n (λg.λh.h (g f)) (λu.x) (λu.u)
can be validated by showing inductively that if T denotes (λg.λh.h (g f)), then T(n)(λu.x) = (λh.h(f(n−1)(x))) for n > 0. Two other definitions of PRED are given below, one using conditionals and the other using pairs. With the predecessor function, subtraction is straightforward. Defining

SUB := λm.λn.n PRED m,
SUB m n yields m − n when m > n and 0 otherwise.

Logic and predicates
By convention, the following two definitions (known as Church Booleans) are used for the Boolean values TRUE and FALSE:

TRUE := λx.λy.x
FALSE := λx.λy.y
Then, with these two lambda terms, we can define some logic operators (these are just possible formulations; other expressions could be equally correct):

AND := λp.λq.p q p
OR := λp.λq.p p q
NOT := λp.p FALSE TRUE
IFTHENELSE := λp.λa.λb.p a b
We are now able to compute some logic functions, for example:

AND TRUE FALSE
≡ (λp.λq.p q p) TRUE FALSE →β TRUE FALSE TRUE
≡ (λx.λy.x) FALSE TRUE →β FALSE
and we see that AND TRUE FALSE is equivalent to FALSE.
A predicate is a function that returns a Boolean value. The most fundamental predicate is ISZERO, which returns TRUE if its argument is the Church numeral 0, but FALSE if its argument were any other Church numeral:

ISZERO := λn.n (λx.FALSE) TRUE
The following predicate tests whether the first argument is less-than-or-equal-to the second:

LEQ := λm.λn.ISZERO (SUB m n),
and since m = n, if LEQ m n and LEQ n m, it is straightforward to build a predicate for numerical equality.
The availability of predicates and the above definition of TRUE and FALSE make it convenient to write "if-then-else" expressions in lambda calculus. For example, the predecessor function can be defined as:

PRED := λn.n (λg.λk.ISZERO (g 1) k (PLUS (g k) 1)) (λv.0) 0
which can be verified by showing inductively that n (λg.λk.ISZERO (g 1) k (PLUS (g k) 1)) (λv.0) is the add n − 1 function for n > 0.

Pairs
A pair (2-tuple) can be defined in terms of TRUE and FALSE, by using the Church encoding for pairs. For example, PAIR encapsulates the pair (x,y), FIRST returns the first element of the pair, and SECOND returns the second.

PAIR := λx.λy.λf.f x y
FIRST := λp.p TRUE
SECOND := λp.p FALSE
NIL := λx.TRUE
NULL := λp.p (λx.λy.FALSE)
A linked list can be defined as either NIL for the empty list, or the PAIR of an element and a smaller list. The predicate NULL tests for the value NIL. (Alternatively, with NIL := FALSE, the construct l (λh.λt.λz.deal_with_head_h_and_tail_t) (deal_with_nil) obviates the need for an explicit NULL test).
As an example of the use of pairs, the shift-and-increment function that maps (m, n) to (n, n + 1) can be defined as

Φ := λx.PAIR (SECOND x) (SUCC (SECOND x))
which allows us to give perhaps the most transparent version of the predecessor function:

PRED := λn.FIRST (n Φ (PAIR 0 0)).

Additional programming techniques
There is a considerable body of programming idioms for lambda calculus. Many of these were originally developed in the context of using lambda calculus as a foundation for programming language semantics, effectively using lambda calculus as a low-level programming language. Because several programming languages include the lambda calculus (or something very similar) as a fragment, these techniques also see use in practical programming, but may then be perceived as obscure or foreign.

Named constants
In lambda calculus, a library would take the form of a collection of previously defined functions, which as lambda-terms are merely particular constants. The pure lambda calculus does not have a concept of named constants since all atomic lambda-terms are variables, but one can emulate having named constants by setting aside a variable as the name of the constant, using abstraction to bind that variable in the main body, and apply that abstraction to the intended definition. Thus to use f to mean N (some explicit lambda-term) in M (another lambda-term, the "main program"), one can say

(λf.M) N
Authors often introduce syntactic sugar, such as let, to permit writing the above in the more intuitive order

let f =NinM
By chaining such definitions, one can write a lambda calculus "program" as zero or more function definitions, followed by one lambda-term using those functions that constitutes the main body of the program.
A notable restriction of this let is that the name f be not defined in N, for N to be outside the scope of the abstraction binding f; this means a recursive function definition cannot be used as the N with let. The letrec construction would allow writing recursive function definitions.

Recursion and fixed points
Recursion is the definition of a function invoking itself. A definition containing itself inside itself, by value, leads to the whole value being of infinite size. Other notations which support recursion natively overcome this by referring to the function definition by name. Lambda calculus cannot express this: all functions are anonymous in lambda calculus, so we can't refer by name to a value which is yet to be defined, inside the lambda term defining that same value. However, a lambda expression can receive itself as its own argument, for example in  (λx.x x) E. Here E should be an abstraction, applying its parameter to a value to express recursion.
Consider the factorial function F(n) recursively defined by

F(n) = 1, if n = 0; else n × F(n − 1).
In the lambda expression which is to represent this function, a parameter (typically the first one) will be assumed to receive the lambda expression itself as its value, so that calling it – applying it to an argument – will amount to recursion. Thus to achieve recursion, the intended-as-self-referencing argument (called r here) must always be passed to itself within the function body, at a call point:

G := λr. λn.(1, if n = 0; else n × (r r (n−1)))
with  r r x = F x = G r x  to hold, so  r = G  and
F := G G = (λx.x x) G
The self-application achieves replication here, passing the function's lambda expression on to the next invocation as an argument value, making it available to be referenced and called there.
This solves it but requires re-writing each recursive call as self-application. We would like to have a generic solution, without a need for any re-writes:

G := λr. λn.(1, if n = 0; else n × (r (n−1)))
with  r x = F x = G r x  to hold, so  r = G r =: FIX G  and
F := FIX G  where  FIX g := (r where r = g r) = g (FIX g)
so that  FIX G = G (FIX G) = (λn.(1, if n = 0; else n × ((FIX G) (n−1))))
Given a lambda term with first argument representing recursive call (e.g. G here), the fixed-point combinator FIX will return a self-replicating lambda expression representing the recursive function (here, F). The function does not need to be explicitly passed to itself at any point, for the self-replication is arranged in advance, when it is created, to be done each time it is called. Thus the original lambda expression (FIX G) is re-created inside itself, at call-point, achieving self-reference.
In fact, there are many possible definitions for this FIX operator, the simplest of them being:

 Y := λg.(λx.g (x x)) (λx.g (x x))
In the lambda calculus, Y g  is a fixed-point of g, as it expands to:

Y g
(λh.(λx.h (x x)) (λx.h (x x))) g
(λx.g (x x)) (λx.g (x x))
g ((λx.g (x x)) (λx.g (x x)))
g (Y g)
Now, to perform our recursive call to the factorial function, we would simply call (Y G) n,  where n is the number we are calculating the factorial of. Given n = 4, for example, this gives:

(Y G) 4
G (Y G) 4
(λr.λn.(1, if n = 0; else n × (r (n−1)))) (Y G) 4
(λn.(1, if n = 0; else n × ((Y G) (n−1)))) 4
1, if 4 = 0; else 4 × ((Y G) (4−1))
4 × (G (Y G) (4−1))
4 × ((λn.(1, if n = 0; else n × ((Y G) (n−1)))) (4−1))
4 × (1, if 3 = 0; else 3 × ((Y G) (3−1)))
4 × (3 × (G (Y G) (3−1)))
4 × (3 × ((λn.(1, if n = 0; else n × ((Y G) (n−1)))) (3−1)))
4 × (3 × (1, if 2 = 0; else 2 × ((Y G) (2−1))))
4 × (3 × (2 × (G (Y G) (2−1))))
4 × (3 × (2 × ((λn.(1, if n = 0; else n × ((Y G) (n−1)))) (2−1))))
4 × (3 × (2 × (1, if 1 = 0; else 1 × ((Y G) (1−1)))))
4 × (3 × (2 × (1 × (G (Y G) (1−1)))))
4 × (3 × (2 × (1 × ((λn.(1, if n = 0; else n × ((Y G) (n−1)))) (1−1)))))
4 × (3 × (2 × (1 × (1, if 0 = 0; else 0 × ((Y G) (0−1))))))
4 × (3 × (2 × (1 × (1))))
24
Every recursively defined function can be seen as a fixed point of some suitably defined function closing over the recursive call with an extra argument, and therefore, using Y, every recursively defined function can be expressed as a lambda expression. In particular, we can now cleanly define the subtraction, multiplication and comparison predicate of natural numbers recursively.

Standard terms
Certain terms have commonly accepted names:

 I := λx.x
 S := λx.λy.λz.x z (y z)
 K := λx.λy.x
 B := λx.λy.λz.x (y z)
 C := λx.λy.λz.x z y
 W := λx.λy.x y y
 ω or Δ or U := λx.x x
 Ω := ω ω
I is the identity function. SK and BCKW form complete combinator calculus systems that can express any lambda term - see 
the next section. Ω is UU, the smallest term that has no normal form. YI is another such term.
Y is standard and defined above, and can also be defined as Y=BU(CBU), so that Yg=g(Yg). TRUE and FALSE defined above are commonly abbreviated as T and F.

Abstraction elimination
If N is a lambda-term without abstraction, but possibly containing named constants (combinators), then there exists a lambda-term T(x,N) which is equivalent to λx.N but lacks abstraction (except as part of the named constants, if these are considered non-atomic). This can also be viewed as anonymising variables, as T(x,N) removes all occurrences of x from N, while still allowing argument values to be substituted into the positions where N contains an x. The conversion function T can be defined by:

T(x, x) := I
T(x, N) := K N if x is not free in N.
T(x, M N) := S T(x, M) T(x, N)
In either case, a term of the form T(x,N) P can reduce by having the initial combinator I, K, or S grab the argument P, just like β-reduction of (λx.N) P would do. I returns that argument. K throws the argument away, just like (λx.N) would do if x has no free occurrence in N. S passes the argument on to both subterms of the application, and then applies the result of the first to the result of the second.
The combinators B and C are similar to S, but pass the argument on to only one subterm of an application (B to the "argument" subterm and C to the "function" subterm), thus saving a subsequent K if there is no occurrence of x in one subterm. In comparison to B and C, the S combinator actually conflates two functionalities: rearranging arguments, and duplicating an argument so that it may be used in two places. The W combinator does only the latter, yielding the B, C, K, W system as an alternative to SKI combinator calculus.

Typed lambda calculus
A typed lambda calculus is a typed formalism that uses the lambda-symbol (
  
    
      
        λ
      
    
    {\displaystyle \lambda }
  
) to denote anonymous function abstraction. In this context, types are usually objects of a syntactic nature that are assigned to lambda terms; the exact nature of a type depends on the calculus considered (see Kinds of typed lambda calculi). From a certain point of view, typed lambda calculi can be seen as refinements of the untyped lambda calculus but from another point of view, they can also be considered the more fundamental theory and untyped lambda calculus a special case with only one type.
Typed lambda calculi are foundational programming languages and are the base of typed functional programming languages such as ML and Haskell and, more indirectly, typed imperative programming languages. Typed lambda calculi play an important role in the design of type systems for programming languages; here typability usually captures desirable properties of the program, e.g., the program will not cause a memory access violation.
Typed lambda calculi are closely related to mathematical logic and proof theory via the Curry–Howard isomorphism and they can be considered as the internal language of classes of categories, e.g., the simply typed lambda calculus is the language of a Cartesian closed category (CCC).

Reduction strategies
Whether a term is normalising or not, and how much work needs to be done in normalising it if it is, depends to a large extent on the reduction strategy used. Common lambda calculus reduction strategies include:

Normal order
The leftmost outermost redex is reduced first. That is, whenever possible, arguments are substituted into the body of an abstraction before the arguments are reduced. If a term has a beta-normal form, normal order reduction will always reach that normal form.
Applicative order
The leftmost innermost redex is reduced first. As a consequence, a function's arguments are always reduced before they are substituted into the function. Unlike normal order reduction, applicative order reduction may fail to find the beta-normal form of an expression, even if such a normal form exists. For example, the term 
  
    
      
        (
        
        λ
        x
        .
        y
        
        
        (
        λ
        z
        .
        (
        z
        z
        )
        
        λ
        z
        .
        (
        z
        z
        )
        )
        
        )
      
    
    {\displaystyle (\;\lambda x.y\;\;(\lambda z.(zz)\;\lambda z.(zz))\;)}
  
 is reduced to itself by applicative order, while normal order reduces it to its beta-normal form 
  
    
      
        y
      
    
    {\displaystyle y}
  
.
Full β-reductions
Any redex can be reduced at any time. This means essentially the lack of any particular reduction strategy—with regard to reducibility, "all bets are off".
Weak reduction strategies do not reduce under lambda abstractions:

Call by value
Like applicative order, but no reductions are performed inside abstractions. This is similar to the evaluation order of strict languages like C: the arguments to a function are evaluated before calling the function, and function bodies are not even partially evaluated until the arguments are substituted in.
Call by name
Like normal order, but no reductions are performed inside abstractions. For example, λx.(λy.y)x is in normal form according to this strategy, although it contains the redex (λy.y)x.
Strategies with sharing reduce computations that are "the same" in parallel:

Optimal reduction
As normal order, but computations that have the same label are reduced simultaneously.
Call by need
As call by name (hence weak), but function applications that would duplicate terms instead name the argument. The argument may be evaluated "when needed," at which point the name binding is updated with the reduced value. This can save time compared to normal order evaluation.

Computability
There is no algorithm that takes as input any two lambda expressions and outputs TRUE or FALSE depending on whether one expression reduces to the other. More precisely, no computable function can decide the question. This was historically the first problem for which undecidability could be proven. As usual for such a proof, computable means computable by any model of computation that is Turing complete. In fact computability can itself be defined via the lambda calculus: a function F: N → N of natural numbers is a computable function if and only if there exists a lambda expression f such that for every pair of x, y in N, F(x)=y if and only if f x =β y,  where x and y are the Church numerals corresponding to x and y, respectively and =β meaning equivalence with β-reduction. See the Church–Turing thesis for other approaches to defining computability and their equivalence.
Church's proof of uncomputability first reduces the problem to determining whether a given lambda expression has a normal form. Then he assumes that this predicate is computable, and can hence be expressed in lambda calculus. Building on earlier work by Kleene and constructing a Gödel numbering for lambda expressions, he constructs a lambda expression e that closely follows the proof of Gödel's first incompleteness theorem. If e is applied to its own Gödel number, a contradiction results.

Complexity
The notion of computational complexity for the lambda calculus is a bit tricky, because the cost of a β-reduction may vary depending on how it is implemented. 
To be precise, one must somehow find the location of all of the occurrences of the bound variable V in the expression E, implying a time cost, or one must keep track of the locations of free variables in some way, implying a space cost. A naïve search for the locations of V in E is O(n) in the length n of E. Director strings were an early approach that traded this time cost for a quadratic space usage. More generally this has led to the study of systems that use explicit substitution.
In 2014, it was shown that the number of β-reduction steps taken by normal order reduction to reduce a term is a reasonable time cost model, that is, the reduction can be simulated on a Turing machine in time polynomially proportional to the number of steps. This was a long-standing open problem, due to size explosion, the existence of lambda terms which grow exponentially in size for each β-reduction. The result gets around this by working with a compact shared representation. The result makes clear that the amount of space needed to evaluate a lambda term is not proportional to the size of the term during reduction. It is not currently known what a good measure of space complexity would be.
An unreasonable model does not necessarily mean inefficient. Optimal reduction reduces all computations with the same label in one step, avoiding duplicated work, but the number of parallel β-reduction steps to reduce a given term to normal form is approximately linear in the size of the term. This is far too small to be a reasonable cost measure, as any Turing machine may be encoded in the lambda calculus in size linearly proportional to the size of the Turing machine. The true cost of reducing lambda terms is not due to β-reduction per se but rather the handling of the duplication of redexes during β-reduction. It is not known if optimal reduction implementations are reasonable when measured with respect to a reasonable cost model such as the number of leftmost-outermost steps to normal form, but it has been shown for fragments of the lambda calculus that the optimal reduction algorithm is efficient and has at most a quadratic overhead compared to leftmost-outermost. In addition the BOHM prototype implementation of optimal reduction outperformed both Caml Light and Haskell on pure lambda terms.

Lambda calculus and programming languages
As pointed out by Peter Landin's 1965 paper "A Correspondence between ALGOL 60 and Church's Lambda-notation", sequential procedural programming languages can be understood in terms of the lambda calculus, which provides the basic mechanisms for procedural abstraction and procedure (subprogram) application.

Anonymous functions
For example, in Python the "square" function can be expressed as a lambda expression as follows:

The above example is an expression that evaluates to a first-class function. The symbol lambda creates an anonymous function, given a list of parameter names, x – just a single argument in this case, and an expression that is evaluated as the body of the function, x**2. Anonymous functions are sometimes called lambda expressions.
For example, Pascal and many other imperative languages have long supported passing subprograms as arguments to other subprograms through the mechanism of function pointers. However, function pointers are an insufficient condition for functions to be first class datatypes, because a function is a first class datatype if and only if new instances of the function can be created at runtime. Such runtime creation of functions is supported in Smalltalk, JavaScript, Wolfram Language, and more recently in Scala, Eiffel (as agents), C# (as delegates) and C++11, among others.

Parallelism and concurrency
The Church–Rosser property of the lambda calculus means that evaluation (β-reduction) can be carried out in any order, even in parallel. This means that various nondeterministic evaluation strategies are relevant. However, the lambda calculus does not offer any explicit constructs for parallelism. One can add constructs such as futures to the lambda calculus. Other process calculi have been developed for describing communication and concurrency.

Semantics
The fact that lambda calculus terms act as functions on other lambda calculus terms, and even on themselves, led to questions about the semantics of the lambda calculus. Could a sensible meaning be assigned to lambda calculus terms? The natural semantics was to find a set D isomorphic to the function space D → D, of functions on itself. However, no nontrivial such D can exist, by cardinality constraints because the set of all functions from D to D has greater cardinality than D, unless D is a singleton set.
In the 1970s, Dana Scott showed that if only continuous functions were considered, a set or domain D with the required property could be found, thus providing a model for the lambda calculus.
This work also formed the basis for the denotational semantics of programming languages.

Variations and extensions
These extensions are in the lambda cube:

Typed lambda calculus – Lambda calculus with typed variables (and functions)
System F – A typed lambda calculus with type-variables
Calculus of constructions – A typed lambda calculus with types as first-class values
These formal systems are extensions of lambda calculus that are not in the lambda cube:

Binary lambda calculus – A version of lambda calculus with binary input/output (I/O), a binary encoding of terms, and a designated universal machine.
Lambda-mu calculus – An extension of the lambda calculus for treating classical logic
These formal systems are variations of lambda calculus:

Kappa calculus – A first-order analogue of lambda calculus
These formal systems are related to lambda calculus:

Combinatory logic – A notation for mathematical logic without variables
SKI combinator calculus – A computational system based on the S, K and I combinators, equivalent to lambda calculus, but reducible without variable substitutions

See also
Further reading
Abelson, Harold & Gerald Jay Sussman. Structure and Interpretation of Computer Programs. The MIT Press. ISBN 0-262-51087-1.
Barendregt, Hendrik Pieter Introduction to Lambda Calculus.
Barendregt, Hendrik Pieter, The Impact of the Lambda Calculus in Logic and Computer Science. The Bulletin of Symbolic Logic, Volume 3, Number 2, June 1997.
Barendregt, Hendrik Pieter, The Type Free Lambda Calculus pp1091–1132 of Handbook of Mathematical Logic, North-Holland (1977) ISBN 0-7204-2285-X
Cardone, Felice and Hindley, J. Roger, 2006. History of Lambda-calculus and Combinatory Logic Archived 2021-05-06 at the Wayback Machine. In Gabbay and Woods (eds.), Handbook of the History of Logic, vol. 5. Elsevier.
Church, Alonzo, An unsolvable problem of elementary number theory, American Journal of Mathematics, 58 (1936), pp. 345–363. This paper contains the proof that the equivalence of lambda expressions is in general not decidable.
Church, Alonzo (1941). The Calculi of Lambda-Conversion. Princeton: Princeton University Press. Retrieved 2020-04-14. (ISBN 978-0-691-08394-0)
Frink Jr., Orrin (1944). "Review: The Calculi of Lambda-Conversion by Alonzo Church" (PDF). Bulletin of the American Mathematics Society. 50 (3): 169–172. doi:10.1090/s0002-9904-1944-08090-7.
Kleene, Stephen, A theory of positive integers in formal logic, American Journal of Mathematics, 57 (1935), pp. 153–173 and 219–244. Contains the lambda calculus definitions of several familiar functions.
Landin, Peter, A Correspondence Between ALGOL 60 and Church's Lambda-Notation, Communications of the ACM, vol. 8, no. 2 (1965), pages 89–101. Available from the ACM site. A classic paper highlighting the importance of lambda calculus as a basis for programming languages.
Larson, Jim, An Introduction to Lambda Calculus and Scheme. A gentle introduction for programmers.
Michaelson, Greg (10 April 2013). An Introduction to Functional Programming Through Lambda Calculus. Courier Corporation. ISBN 978-0-486-28029-5.
Schalk, A. and Simmons, H. (2005) An introduction to λ-calculi and arithmetic with a decent selection of exercises. Notes for a course in the Mathematical Logic MSc at Manchester University.
de Queiroz, Ruy J.G.B. (2008). "On Reduction Rules, Meaning-as-Use and Proof-Theoretic Semantics". Studia Logica. 90 (2): 211–247. doi:10.1007/s11225-008-9150-5. S2CID 11321602. A paper giving a formal underpinning to the idea of 'meaning-is-use' which, even if based on proofs, it is different from proof-theoretic semantics as in the Dummett–Prawitz tradition since it takes reduction as the rules giving meaning.
Hankin, Chris, An Introduction to Lambda Calculi for Computer Scientists, ISBN 0954300653
Monographs/textbooks for graduate students

Sørensen, Morten Heine and Urzyczyn, Paweł (2006), Lectures on the Curry–Howard isomorphism, Elsevier, ISBN 0-444-52077-5 is a recent monograph that covers the main topics of lambda calculus from the type-free variety, to most typed lambda calculi, including more recent developments like pure type systems and the lambda cube. It does not cover subtyping extensions.
Pierce, Benjamin (2002), Types and Programming Languages, MIT Press, ISBN 0-262-16209-1 covers lambda calculi from a practical type system perspective; some topics like dependent types are only mentioned, but subtyping is an important topic.
Documents
A Short Introduction to the Lambda Calculus-(PDF) by Achim Jung
A timeline of lambda calculus-(PDF) by Dana Scott
A Tutorial Introduction to the Lambda Calculus-(PDF) by Raúl Rojas
Lecture Notes on the Lambda Calculus-(PDF) by Peter Selinger
Graphic lambda calculus by Marius Buliga
Lambda Calculus as a Workflow Model by Peter Kelly, Paul Coddington, and Andrew Wendelborn; mentions graph reduction as a common means of evaluating lambda expressions and discusses the applicability of lambda calculus for distributed computing (due to the Church–Rosser property, which enables parallel graph reduction for lambda expressions).

Notes
References
Some parts of this article are based on material from FOLDOC, used with permission.

External links

Graham Hutton, Lambda Calculus, a short (12 minutes) Computerphile video on the Lambda Calculus
Helmut Brandl, Step by Step Introduction to Lambda Calculus
"Lambda-calculus", Encyclopedia of Mathematics, EMS Press, 2001 [1994]
David C. Keenan, To Dissect a Mockingbird: A Graphical Notation for the Lambda Calculus with Animated Reduction
L. Allison, Some executable λ-calculus examples
Georg P. Loczewski, The Lambda Calculus and A++
Bret Victor, Alligator Eggs: A Puzzle Game Based on Lambda Calculus
Lambda Calculus Archived 2012-10-14 at the Wayback Machine on Safalra's Website Archived 2021-05-02 at the Wayback Machine
LCI Lambda Interpreter a simple yet powerful pure calculus interpreter
Lambda Calculus links on Lambda-the-Ultimate
Mike Thyer, Lambda Animator, a graphical Java applet demonstrating alternative reduction strategies.
Implementing the Lambda calculus using C++ Templates
Shane Steinert-Threlkeld, "Lambda Calculi", Internet Encyclopedia of Philosophy
Anton Salikhmetov, Macro Lambda Calculus

## Related Articles

### Internal Links

- [A. C. Croom](https://en.wikipedia.org/wiki/A._C._Croom)
- [ALGOL 60](https://en.wikipedia.org/wiki/ALGOL_60)
- [ASCII](https://en.wikipedia.org/wiki/ASCII)
- [Abstract logic](https://en.wikipedia.org/wiki/Abstract_logic)
- [Abstraction (computer science)](https://en.wikipedia.org/wiki/Abstraction_(computer_science))
- [Ackermann set theory](https://en.wikipedia.org/wiki/Ackermann_set_theory)
- [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing)
- [Aleph number](https://en.wikipedia.org/wiki/Aleph_number)
- [Alfred Foster (mathematician)](https://en.wikipedia.org/wiki/Alfred_Foster_(mathematician))
- [Algebraic function](https://en.wikipedia.org/wiki/Algebraic_function)
- [Algebraic logic](https://en.wikipedia.org/wiki/Algebraic_logic)
- [Alice ter Meulen](https://en.wikipedia.org/wiki/Alice_ter_Meulen)
- [Alonzo Church](https://en.wikipedia.org/wiki/Alonzo_Church)
- [Alonzo Church (college president)](https://en.wikipedia.org/wiki/Alonzo_Church_(college_president))
- [Alpha](https://en.wikipedia.org/wiki/Alpha)
- [Alphabet (formal languages)](https://en.wikipedia.org/wiki/Alphabet_(formal_languages))
- [Alternative semantics](https://en.wikipedia.org/wiki/Alternative_semantics)
- [Ambiguity](https://en.wikipedia.org/wiki/Ambiguity)
- [American Journal of Mathematics](https://en.wikipedia.org/wiki/American_Journal_of_Mathematics)
- [Analytic function](https://en.wikipedia.org/wiki/Analytic_function)
- [Anaphora (linguistics)](https://en.wikipedia.org/wiki/Anaphora_(linguistics))
- [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- [Antecedent-contained deletion](https://en.wikipedia.org/wiki/Antecedent-contained_deletion)
- [Applicative computing systems](https://en.wikipedia.org/wiki/Applicative_computing_systems)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Argument](https://en.wikipedia.org/wiki/Argument)
- [Arithmetic](https://en.wikipedia.org/wiki/Arithmetic)
- [Arity](https://en.wikipedia.org/wiki/Arity)
- [Atomic formula](https://en.wikipedia.org/wiki/Atomic_formula)
- [Atomic sentence](https://en.wikipedia.org/wiki/Atomic_sentence)
- [Automata theory](https://en.wikipedia.org/wiki/Automata_theory)
- [Automated theorem proving](https://en.wikipedia.org/wiki/Automated_theorem_proving)
- [Autonomy of syntax](https://en.wikipedia.org/wiki/Autonomy_of_syntax)
- [Axiom](https://en.wikipedia.org/wiki/Axiom)
- [Axiom of choice](https://en.wikipedia.org/wiki/Axiom_of_choice)
- [Axiom schema](https://en.wikipedia.org/wiki/Axiom_schema)
- [Axiomatic system](https://en.wikipedia.org/wiki/Axiomatic_system)
- [Boolean algebra (structure)](https://en.wikipedia.org/wiki/Boolean_algebra_(structure))
- [B, C, K, W system](https://en.wikipedia.org/wiki/B,_C,_K,_W_system)
- [Backus–Naur form](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form)
- [Banach–Tarski paradox](https://en.wikipedia.org/wiki/Banach%E2%80%93Tarski_paradox)
- [Benjamin C. Pierce](https://en.wikipedia.org/wiki/Benjamin_C._Pierce)
- [Beta](https://en.wikipedia.org/wiki/Beta)
- [Beta normal form](https://en.wikipedia.org/wiki/Beta_normal_form)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Bijection](https://en.wikipedia.org/wiki/Bijection)
- [Binary combinatory logic](https://en.wikipedia.org/wiki/Binary_combinatory_logic)
- [Binary operation](https://en.wikipedia.org/wiki/Binary_operation)
- [Binary relation](https://en.wikipedia.org/wiki/Binary_relation)
- [Binding (linguistics)](https://en.wikipedia.org/wiki/Binding_(linguistics))
- [Boolean-valued function](https://en.wikipedia.org/wiki/Boolean-valued_function)
- [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra)
- [Boolean algebras canonically defined](https://en.wikipedia.org/wiki/Boolean_algebras_canonically_defined)
- [Boolean function](https://en.wikipedia.org/wiki/Boolean_function)
- [C++11](https://en.wikipedia.org/wiki/C%2B%2B11)
- [Template (C++)](https://en.wikipedia.org/wiki/Template_(C%2B%2B))
- [C. Anthony Anderson](https://en.wikipedia.org/wiki/C._Anthony_Anderson)
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Calculus of constructions](https://en.wikipedia.org/wiki/Calculus_of_constructions)
- [Caml](https://en.wikipedia.org/wiki/Caml)
- [Cantor's diagonal argument](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument)
- [Cantor's paradox](https://en.wikipedia.org/wiki/Cantor%27s_paradox)
- [Cantor's theorem](https://en.wikipedia.org/wiki/Cantor%27s_theorem)
- [Cardinality](https://en.wikipedia.org/wiki/Cardinality)
- [Cartesian closed category](https://en.wikipedia.org/wiki/Cartesian_closed_category)
- [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product)
- [Cataphora](https://en.wikipedia.org/wiki/Cataphora)
- [Categorial grammar](https://en.wikipedia.org/wiki/Categorial_grammar)
- [Categorical abstract machine](https://en.wikipedia.org/wiki/Categorical_abstract_machine)
- [Categorical theory](https://en.wikipedia.org/wiki/Categorical_theory)
- [Category (mathematics)](https://en.wikipedia.org/wiki/Category_(mathematics))
- [Category of sets](https://en.wikipedia.org/wiki/Category_of_sets)
- [Category theory](https://en.wikipedia.org/wiki/Category_theory)
- [Church encoding](https://en.wikipedia.org/wiki/Church_encoding)
- [Church encoding](https://en.wikipedia.org/wiki/Church_encoding)
- [Church–Rosser theorem](https://en.wikipedia.org/wiki/Church%E2%80%93Rosser_theorem)
- [Church–Turing thesis](https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Class (set theory)](https://en.wikipedia.org/wiki/Class_(set_theory))
- [Classical logic](https://en.wikipedia.org/wiki/Classical_logic)
- [Clojure](https://en.wikipedia.org/wiki/Clojure)
- [Codomain](https://en.wikipedia.org/wiki/Codomain)
- [Coercion (linguistics)](https://en.wikipedia.org/wiki/Coercion_(linguistics))
- [Cognitive semantics](https://en.wikipedia.org/wiki/Cognitive_semantics)
- [Combinatory logic](https://en.wikipedia.org/wiki/Combinatory_logic)
- [Combinatory categorial grammar](https://en.wikipedia.org/wiki/Combinatory_categorial_grammar)
- [Combinatory logic](https://en.wikipedia.org/wiki/Combinatory_logic)
- [Communications of the ACM](https://en.wikipedia.org/wiki/Communications_of_the_ACM)
- [Compactness theorem](https://en.wikipedia.org/wiki/Compactness_theorem)
- [Complement (set theory)](https://en.wikipedia.org/wiki/Complement_(set_theory))
- [Complete theory](https://en.wikipedia.org/wiki/Complete_theory)
- [Complex analysis](https://en.wikipedia.org/wiki/Complex_analysis)
- [Computability](https://en.wikipedia.org/wiki/Computability)
- [Computability theory](https://en.wikipedia.org/wiki/Computability_theory)
- [Computable function](https://en.wikipedia.org/wiki/Computable_function)
- [Computable set](https://en.wikipedia.org/wiki/Computable_set)
- [Computably enumerable set](https://en.wikipedia.org/wiki/Computably_enumerable_set)
- [Computational complexity theory](https://en.wikipedia.org/wiki/Computational_complexity_theory)
- [Computational semantics](https://en.wikipedia.org/wiki/Computational_semantics)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Concrete category](https://en.wikipedia.org/wiki/Concrete_category)
- [Conditional sentence](https://en.wikipedia.org/wiki/Conditional_sentence)
- [Confluence (abstract rewriting)](https://en.wikipedia.org/wiki/Confluence_(abstract_rewriting))
- [Conservative extension](https://en.wikipedia.org/wiki/Conservative_extension)
- [Conservativity](https://en.wikipedia.org/wiki/Conservativity)
- [Consistency](https://en.wikipedia.org/wiki/Consistency)
- [Constant function](https://en.wikipedia.org/wiki/Constant_function)
- [Constructible universe](https://en.wikipedia.org/wiki/Constructible_universe)
- [Construction of the real numbers](https://en.wikipedia.org/wiki/Construction_of_the_real_numbers)
- [Constructive set theory](https://en.wikipedia.org/wiki/Constructive_set_theory)
- [Common ground (linguistics)](https://en.wikipedia.org/wiki/Common_ground_(linguistics))
- [Continuation](https://en.wikipedia.org/wiki/Continuation)
- [Continuous function](https://en.wikipedia.org/wiki/Continuous_function)
- [Continuum hypothesis](https://en.wikipedia.org/wiki/Continuum_hypothesis)
- [Conversational scoreboard](https://en.wikipedia.org/wiki/Conversational_scoreboard)
- [Countable set](https://en.wikipedia.org/wiki/Countable_set)
- [Counterfactual conditional](https://en.wikipedia.org/wiki/Counterfactual_conditional)
- [Crossover effects](https://en.wikipedia.org/wiki/Crossover_effects)
- [Cumulativity (linguistics)](https://en.wikipedia.org/wiki/Cumulativity_(linguistics))
- [Currying](https://en.wikipedia.org/wiki/Currying)
- [Curry–Howard correspondence](https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence)
- [Dana Scott](https://en.wikipedia.org/wiki/Dana_Scott)
- [De Bruijn index](https://en.wikipedia.org/wiki/De_Bruijn_index)
- [De Bruijn notation](https://en.wikipedia.org/wiki/De_Bruijn_notation)
- [De dicto and de re](https://en.wikipedia.org/wiki/De_dicto_and_de_re)
- [De se](https://en.wikipedia.org/wiki/De_se)
- [Decidability (logic)](https://en.wikipedia.org/wiki/Decidability_(logic))
- [Decision problem](https://en.wikipedia.org/wiki/Decision_problem)
- [Formal system](https://en.wikipedia.org/wiki/Formal_system)
- [Definiteness](https://en.wikipedia.org/wiki/Definiteness)
- [Denotation](https://en.wikipedia.org/wiki/Denotation)
- [Denotational semantics](https://en.wikipedia.org/wiki/Denotational_semantics)
- [Deontic modality](https://en.wikipedia.org/wiki/Deontic_modality)
- [Diagram (mathematical logic)](https://en.wikipedia.org/wiki/Diagram_(mathematical_logic))
- [Director string](https://en.wikipedia.org/wiki/Director_string)
- [Discourse relation](https://en.wikipedia.org/wiki/Discourse_relation)
- [Discourse representation theory](https://en.wikipedia.org/wiki/Discourse_representation_theory)
- [Logical disjunction](https://en.wikipedia.org/wiki/Logical_disjunction)
- [Distributed computing](https://en.wikipedia.org/wiki/Distributed_computing)
- [Distributional semantics](https://en.wikipedia.org/wiki/Distributional_semantics)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Domain of a function](https://en.wikipedia.org/wiki/Domain_of_a_function)
- [Domain theory](https://en.wikipedia.org/wiki/Domain_theory)
- [Donkey sentence](https://en.wikipedia.org/wiki/Donkey_sentence)
- [Downward entailing](https://en.wikipedia.org/wiki/Downward_entailing)
- [Dynamic semantics](https://en.wikipedia.org/wiki/Dynamic_semantics)
- [Eeny, meeny, miny, moe](https://en.wikipedia.org/wiki/Eeny,_meeny,_miny,_moe)
- [Eiffel (programming language)](https://en.wikipedia.org/wiki/Eiffel_(programming_language))
- [Element (mathematics)](https://en.wikipedia.org/wiki/Element_(mathematics))
- [Elementary diagram](https://en.wikipedia.org/wiki/Elementary_diagram)
- [Elementary equivalence](https://en.wikipedia.org/wiki/Elementary_equivalence)
- [Elementary function arithmetic](https://en.wikipedia.org/wiki/Elementary_function_arithmetic)
- [Empty set](https://en.wikipedia.org/wiki/Empty_set)
- [Encyclopedia of Mathematics](https://en.wikipedia.org/wiki/Encyclopedia_of_Mathematics)
- [Logical consequence](https://en.wikipedia.org/wiki/Logical_consequence)
- [Enumeration](https://en.wikipedia.org/wiki/Enumeration)
- [Epistemic modality](https://en.wikipedia.org/wiki/Epistemic_modality)
- [Epsilon calculus](https://en.wikipedia.org/wiki/Epsilon_calculus)
- [Universal algebra](https://en.wikipedia.org/wiki/Universal_algebra)
- [Equiconsistency](https://en.wikipedia.org/wiki/Equiconsistency)
- [Equivalence relation](https://en.wikipedia.org/wiki/Equivalence_relation)
- [Esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language)
- [Eta](https://en.wikipedia.org/wiki/Eta)
- [Euclid's Elements](https://en.wikipedia.org/wiki/Euclid%27s_Elements)
- [Euclidean geometry](https://en.wikipedia.org/wiki/Euclidean_geometry)
- [European Mathematical Society](https://en.wikipedia.org/wiki/European_Mathematical_Society)
- [Evaluation strategy](https://en.wikipedia.org/wiki/Evaluation_strategy)
- [Evidentiality](https://en.wikipedia.org/wiki/Evidentiality)
- [Execution (computing)](https://en.wikipedia.org/wiki/Execution_(computing))
- [Exhaustivity](https://en.wikipedia.org/wiki/Exhaustivity)
- [Existential closure](https://en.wikipedia.org/wiki/Existential_closure)
- [Existential quantification](https://en.wikipedia.org/wiki/Existential_quantification)
- [Explicit substitution](https://en.wikipedia.org/wiki/Explicit_substitution)
- [Expression (mathematics)](https://en.wikipedia.org/wiki/Expression_(mathematics))
- [Extension (semantics)](https://en.wikipedia.org/wiki/Extension_(semantics))
- [Extension by definitions](https://en.wikipedia.org/wiki/Extension_by_definitions)
- [Extension by new constant and function names](https://en.wikipedia.org/wiki/Extension_by_new_constant_and_function_names)
- [Extensionality](https://en.wikipedia.org/wiki/Extensionality)
- [Factorial](https://en.wikipedia.org/wiki/Factorial)
- [Faultless disagreement](https://en.wikipedia.org/wiki/Faultless_disagreement)
- [Finitary relation](https://en.wikipedia.org/wiki/Finitary_relation)
- [Finite-valued logic](https://en.wikipedia.org/wiki/Finite-valued_logic)
- [Finite model theory](https://en.wikipedia.org/wiki/Finite_model_theory)
- [Finite set](https://en.wikipedia.org/wiki/Finite_set)
- [First-class function](https://en.wikipedia.org/wiki/First-class_function)
- [First-class citizen](https://en.wikipedia.org/wiki/First-class_citizen)
- [First-order logic](https://en.wikipedia.org/wiki/First-order_logic)
- [Fixed-point combinator](https://en.wikipedia.org/wiki/Fixed-point_combinator)
- [Fixed-point logic](https://en.wikipedia.org/wiki/Fixed-point_logic)
- [Focus (linguistics)](https://en.wikipedia.org/wiki/Focus_(linguistics))
- [Forcing (mathematics)](https://en.wikipedia.org/wiki/Forcing_(mathematics))
- [Formal grammar](https://en.wikipedia.org/wiki/Formal_grammar)
- [Formal language](https://en.wikipedia.org/wiki/Formal_language)
- [Formal proof](https://en.wikipedia.org/wiki/Formal_proof)
- [Semantics of logic](https://en.wikipedia.org/wiki/Semantics_of_logic)
- [Formal semantics (natural language)](https://en.wikipedia.org/wiki/Formal_semantics_(natural_language))
- [Formal system](https://en.wikipedia.org/wiki/Formal_system)
- [Formalism (philosophy of mathematics)](https://en.wikipedia.org/wiki/Formalism_(philosophy_of_mathematics))
- [Formation rule](https://en.wikipedia.org/wiki/Formation_rule)
- [Foundations of geometry](https://en.wikipedia.org/wiki/Foundations_of_geometry)
- [Foundations of mathematics](https://en.wikipedia.org/wiki/Foundations_of_mathematics)
- [Free On-line Dictionary of Computing](https://en.wikipedia.org/wiki/Free_On-line_Dictionary_of_Computing)
- [Free choice inference](https://en.wikipedia.org/wiki/Free_choice_inference)
- [Free logic](https://en.wikipedia.org/wiki/Free_logic)
- [Free variables and bound variables](https://en.wikipedia.org/wiki/Free_variables_and_bound_variables)
- [Frege–Church ontology](https://en.wikipedia.org/wiki/Frege%E2%80%93Church_ontology)
- [Fresh variable](https://en.wikipedia.org/wiki/Fresh_variable)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Function (mathematics)](https://en.wikipedia.org/wiki/Function_(mathematics))
- [Function application](https://en.wikipedia.org/wiki/Function_application)
- [Function composition](https://en.wikipedia.org/wiki/Function_composition)
- [Complex analysis](https://en.wikipedia.org/wiki/Complex_analysis)
- [Function of a real variable](https://en.wikipedia.org/wiki/Function_of_a_real_variable)
- [Function of several complex variables](https://en.wikipedia.org/wiki/Function_of_several_complex_variables)
- [Function of several real variables](https://en.wikipedia.org/wiki/Function_of_several_real_variables)
- [Function pointer](https://en.wikipedia.org/wiki/Function_pointer)
- [Function space](https://en.wikipedia.org/wiki/Function_space)
- [Functional predicate](https://en.wikipedia.org/wiki/Functional_predicate)
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- [Functor](https://en.wikipedia.org/wiki/Functor)
- [Futures and promises](https://en.wikipedia.org/wiki/Futures_and_promises)
- [Fuzzy set](https://en.wikipedia.org/wiki/Fuzzy_set)
- [Gary R. Mar](https://en.wikipedia.org/wiki/Gary_R._Mar)
- [General set theory](https://en.wikipedia.org/wiki/General_set_theory)
- [Generalized quantifier](https://en.wikipedia.org/wiki/Generalized_quantifier)
- [Generative grammar](https://en.wikipedia.org/wiki/Generative_grammar)
- [George Alfred Barnard](https://en.wikipedia.org/wiki/George_Alfred_Barnard)
- [Givenness](https://en.wikipedia.org/wiki/Givenness)
- [Glue semantics](https://en.wikipedia.org/wiki/Glue_semantics)
- [Graph reduction](https://en.wikipedia.org/wiki/Graph_reduction)
- [Grothendieck universe](https://en.wikipedia.org/wiki/Grothendieck_universe)
- [Ground expression](https://en.wikipedia.org/wiki/Ground_expression)
- [Ground expression](https://en.wikipedia.org/wiki/Ground_expression)
- [Gödel's completeness theorem](https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem)
- [Gödel's incompleteness theorems](https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems)
- [Gödel numbering](https://en.wikipedia.org/wiki/G%C3%B6del_numbering)
- [Hacker culture](https://en.wikipedia.org/wiki/Hacker_culture)
- [Halting problem](https://en.wikipedia.org/wiki/Halting_problem)
- [Harrop formula](https://en.wikipedia.org/wiki/Harrop_formula)
- [Hartley Rogers Jr.](https://en.wikipedia.org/wiki/Hartley_Rogers_Jr.)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Handle System](https://en.wikipedia.org/wiki/Handle_System)
- [Henk Barendregt](https://en.wikipedia.org/wiki/Henk_Barendregt)
- [Hereditary set](https://en.wikipedia.org/wiki/Hereditary_set)
- [Heriot-Watt University](https://en.wikipedia.org/wiki/Heriot-Watt_University)
- [Higher-order function](https://en.wikipedia.org/wiki/Higher-order_function)
- [Higher-order logic](https://en.wikipedia.org/wiki/Higher-order_logic)
- [Hilbert's axioms](https://en.wikipedia.org/wiki/Hilbert%27s_axioms)
- [Hilbert system](https://en.wikipedia.org/wiki/Hilbert_system)
- [History of logic](https://en.wikipedia.org/wiki/History_of_logic)
- [Mathematical logic](https://en.wikipedia.org/wiki/Mathematical_logic)
- [History of the function concept](https://en.wikipedia.org/wiki/History_of_the_function_concept)
- [Homogeneity (semantics)](https://en.wikipedia.org/wiki/Homogeneity_(semantics))
- [Hurford disjunction](https://en.wikipedia.org/wiki/Hurford_disjunction)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Identity function](https://en.wikipedia.org/wiki/Identity_function)
- [If and only if](https://en.wikipedia.org/wiki/If_and_only_if)
- [Image (mathematics)](https://en.wikipedia.org/wiki/Image_(mathematics))
- [Imperative programming](https://en.wikipedia.org/wiki/Imperative_programming)
- [Implicit function](https://en.wikipedia.org/wiki/Implicit_function)
- [Inaccessible cardinal](https://en.wikipedia.org/wiki/Inaccessible_cardinal)
- [Inalienable possession](https://en.wikipedia.org/wiki/Inalienable_possession)
- [Independence (mathematical logic)](https://en.wikipedia.org/wiki/Independence_(mathematical_logic))
- [Indexicality](https://en.wikipedia.org/wiki/Indexicality)
- [Recursive definition](https://en.wikipedia.org/wiki/Recursive_definition)
- [Inference](https://en.wikipedia.org/wiki/Inference)
- [Inferential role semantics](https://en.wikipedia.org/wiki/Inferential_role_semantics)
- [Infinite-valued logic](https://en.wikipedia.org/wiki/Infinite-valued_logic)
- [Infinite set](https://en.wikipedia.org/wiki/Infinite_set)
- [Information theory](https://en.wikipedia.org/wiki/Information_theory)
- [Inhabited set](https://en.wikipedia.org/wiki/Inhabited_set)
- [Injective function](https://en.wikipedia.org/wiki/Injective_function)
- [Input/output](https://en.wikipedia.org/wiki/Input/output)
- [Inquisitive semantics](https://en.wikipedia.org/wiki/Inquisitive_semantics)
- [Integer-valued function](https://en.wikipedia.org/wiki/Integer-valued_function)
- [Intension](https://en.wikipedia.org/wiki/Intension)
- [Intensional logic](https://en.wikipedia.org/wiki/Intensional_logic)
- [Interaction nets](https://en.wikipedia.org/wiki/Interaction_nets)
- [Categorical logic](https://en.wikipedia.org/wiki/Categorical_logic)
- [Internet Encyclopedia of Philosophy](https://en.wikipedia.org/wiki/Internet_Encyclopedia_of_Philosophy)
- [Interpretation (logic)](https://en.wikipedia.org/wiki/Interpretation_(logic))
- [Interpretation (model theory)](https://en.wikipedia.org/wiki/Interpretation_(model_theory))
- [Structure (mathematical logic)](https://en.wikipedia.org/wiki/Structure_(mathematical_logic))
- [Intersection (set theory)](https://en.wikipedia.org/wiki/Intersection_(set_theory))
- [Intersective modifier](https://en.wikipedia.org/wiki/Intersective_modifier)
- [Inverse function](https://en.wikipedia.org/wiki/Inverse_function)
- [Iota and Jot](https://en.wikipedia.org/wiki/Iota_and_Jot)
- [Definite description](https://en.wikipedia.org/wiki/Definite_description)
- [Isomorphism](https://en.wikipedia.org/wiki/Isomorphism)
- [J. Barkley Rosser](https://en.wikipedia.org/wiki/J._Barkley_Rosser)
- [J. Barkley Rosser](https://en.wikipedia.org/wiki/J._Barkley_Rosser)
- [JSTOR](https://en.wikipedia.org/wiki/JSTOR)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [John C. Mitchell](https://en.wikipedia.org/wiki/John_C._Mitchell)
- [John G. Kemeny](https://en.wikipedia.org/wiki/John_G._Kemeny)
- [Kappa calculus](https://en.wikipedia.org/wiki/Kappa_calculus)
- [Kleene–Rosser paradox](https://en.wikipedia.org/wiki/Kleene%E2%80%93Rosser_paradox)
- [Knights of the Lambda Calculus](https://en.wikipedia.org/wiki/Knights_of_the_Lambda_Calculus)
- [Kolmogorov complexity](https://en.wikipedia.org/wiki/Kolmogorov_complexity)
- [Semantic theory of truth](https://en.wikipedia.org/wiki/Semantic_theory_of_truth)
- [Kripke–Platek set theory](https://en.wikipedia.org/wiki/Kripke%E2%80%93Platek_set_theory)
- [Krivine machine](https://en.wikipedia.org/wiki/Krivine_machine)
- [Lambda](https://en.wikipedia.org/wiki/Lambda)
- [Lambda-mu calculus](https://en.wikipedia.org/wiki/Lambda-mu_calculus)
- [Lambda calculus definition](https://en.wikipedia.org/wiki/Lambda_calculus_definition)
- [Lambda cube](https://en.wikipedia.org/wiki/Lambda_cube)
- [Large cardinal](https://en.wikipedia.org/wiki/Large_cardinal)
- [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)
- [Lemma (mathematics)](https://en.wikipedia.org/wiki/Lemma_(mathematics))
- [Leon Henkin](https://en.wikipedia.org/wiki/Leon_Henkin)
- [Let expression](https://en.wikipedia.org/wiki/Let_expression)
- [Lexical semantics](https://en.wikipedia.org/wiki/Lexical_semantics)
- [Library (computing)](https://en.wikipedia.org/wiki/Library_(computing))
- [Lindström's theorem](https://en.wikipedia.org/wiki/Lindstr%C3%B6m%27s_theorem)
- [Linear map](https://en.wikipedia.org/wiki/Linear_map)
- [Modality (semantics)](https://en.wikipedia.org/wiki/Modality_(semantics))
- [Linguistics](https://en.wikipedia.org/wiki/Linguistics)
- [Linguistics wars](https://en.wikipedia.org/wiki/Linguistics_wars)
- [List of axiomatic systems in logic](https://en.wikipedia.org/wiki/List_of_axiomatic_systems_in_logic)
- [List of axioms](https://en.wikipedia.org/wiki/List_of_axioms)
- [List of first-order theories](https://en.wikipedia.org/wiki/List_of_first-order_theories)
- [List of formal systems](https://en.wikipedia.org/wiki/List_of_formal_systems)
- [List of mathematical functions](https://en.wikipedia.org/wiki/List_of_mathematical_functions)
- [List of mathematical theories](https://en.wikipedia.org/wiki/List_of_mathematical_theories)
- [List of set identities and relations](https://en.wikipedia.org/wiki/List_of_set_identities_and_relations)
- [List of statements independent of ZFC](https://en.wikipedia.org/wiki/List_of_statements_independent_of_ZFC)
- [Logic](https://en.wikipedia.org/wiki/Logic)
- [Logic translation](https://en.wikipedia.org/wiki/Logic_translation)
- [Logical biconditional](https://en.wikipedia.org/wiki/Logical_biconditional)
- [Logical conjunction](https://en.wikipedia.org/wiki/Logical_conjunction)
- [Logical connective](https://en.wikipedia.org/wiki/Logical_connective)
- [Logical consequence](https://en.wikipedia.org/wiki/Logical_consequence)
- [Logical constant](https://en.wikipedia.org/wiki/Logical_constant)
- [Logical disjunction](https://en.wikipedia.org/wiki/Logical_disjunction)
- [Logical equality](https://en.wikipedia.org/wiki/Logical_equality)
- [Logical equivalence](https://en.wikipedia.org/wiki/Logical_equivalence)
- [Logical form (linguistics)](https://en.wikipedia.org/wiki/Logical_form_(linguistics))
- [Logical truth](https://en.wikipedia.org/wiki/Logical_truth)
- [Logicism](https://en.wikipedia.org/wiki/Logicism)
- [Logophoricity](https://en.wikipedia.org/wiki/Logophoricity)
- [Low-level programming language](https://en.wikipedia.org/wiki/Low-level_programming_language)
- [Löwenheim–Skolem theorem](https://en.wikipedia.org/wiki/L%C3%B6wenheim%E2%80%93Skolem_theorem)
- [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
- [Many-valued logic](https://en.wikipedia.org/wiki/Many-valued_logic)
- [Map (mathematics)](https://en.wikipedia.org/wiki/Map_(mathematics))
- [Maps to](https://en.wikipedia.org/wiki/Maps_to)
- [Martin Davis (mathematician)](https://en.wikipedia.org/wiki/Martin_Davis_(mathematician))
- [Material conditional](https://en.wikipedia.org/wiki/Material_conditional)
- [Mathematical logic](https://en.wikipedia.org/wiki/Mathematical_logic)
- [Mathematical object](https://en.wikipedia.org/wiki/Mathematical_object)
- [Mathematical proof](https://en.wikipedia.org/wiki/Mathematical_proof)
- [Mathematics](https://en.wikipedia.org/wiki/Mathematics)
- [Maurice L'Abbé](https://en.wikipedia.org/wiki/Maurice_L%27Abb%C3%A9)
- [Meaning postulate](https://en.wikipedia.org/wiki/Meaning_postulate)
- [Measurable function](https://en.wikipedia.org/wiki/Measurable_function)
- [Mereology](https://en.wikipedia.org/wiki/Mereology)
- [Metalanguage](https://en.wikipedia.org/wiki/Metalanguage)
- [Michael O. Rabin](https://en.wikipedia.org/wiki/Michael_O._Rabin)
- [Minimal axioms for Boolean algebra](https://en.wikipedia.org/wiki/Minimal_axioms_for_Boolean_algebra)
- [Minimalism (computing)](https://en.wikipedia.org/wiki/Minimalism_(computing))
- [Mirativity](https://en.wikipedia.org/wiki/Mirativity)
- [Modal subordination](https://en.wikipedia.org/wiki/Modal_subordination)
- [Model complete theory](https://en.wikipedia.org/wiki/Model_complete_theory)
- [Model of computation](https://en.wikipedia.org/wiki/Model_of_computation)
- [Model theory](https://en.wikipedia.org/wiki/Model_theory)
- [Mogensen–Scott encoding](https://en.wikipedia.org/wiki/Mogensen%E2%80%93Scott_encoding)
- [Monad (functional programming)](https://en.wikipedia.org/wiki/Monad_(functional_programming))
- [Monadic predicate calculus](https://en.wikipedia.org/wiki/Monadic_predicate_calculus)
- [Monadic second-order logic](https://en.wikipedia.org/wiki/Monadic_second-order_logic)
- [Montague grammar](https://en.wikipedia.org/wiki/Montague_grammar)
- [Morphism](https://en.wikipedia.org/wiki/Morphism)
- [Morse–Kelley set theory](https://en.wikipedia.org/wiki/Morse%E2%80%93Kelley_set_theory)
- [Multivalued function](https://en.wikipedia.org/wiki/Multivalued_function)
- [NLab](https://en.wikipedia.org/wiki/NLab)
- [NP (complexity)](https://en.wikipedia.org/wiki/NP_(complexity))
- [Naive set theory](https://en.wikipedia.org/wiki/Naive_set_theory)
- [Name binding](https://en.wikipedia.org/wiki/Name_binding)
- [Name collision](https://en.wikipedia.org/wiki/Name_collision)
- [Name resolution (programming languages)](https://en.wikipedia.org/wiki/Name_resolution_(programming_languages))
- [Natural deduction](https://en.wikipedia.org/wiki/Natural_deduction)
- [Natural number](https://en.wikipedia.org/wiki/Natural_number)
- [Negation](https://en.wikipedia.org/wiki/Negation)
- [New Foundations](https://en.wikipedia.org/wiki/New_Foundations)
- [Nicholas Rescher](https://en.wikipedia.org/wiki/Nicholas_Rescher)
- [Non-Euclidean geometry](https://en.wikipedia.org/wiki/Non-Euclidean_geometry)
- [Non-logical symbol](https://en.wikipedia.org/wiki/Non-logical_symbol)
- [Non-standard model](https://en.wikipedia.org/wiki/Non-standard_model)
- [Non-standard model of arithmetic](https://en.wikipedia.org/wiki/Non-standard_model_of_arithmetic)
- [Nondeterministic algorithm](https://en.wikipedia.org/wiki/Nondeterministic_algorithm)
- [Normal form (abstract rewriting)](https://en.wikipedia.org/wiki/Normal_form_(abstract_rewriting))
- [Norman Shapiro](https://en.wikipedia.org/wiki/Norman_Shapiro)
- [Elsevier](https://en.wikipedia.org/wiki/Elsevier)
- [Object (computer science)](https://en.wikipedia.org/wiki/Object_(computer_science))
- [Opaque context](https://en.wikipedia.org/wiki/Opaque_context)
- [Open formula](https://en.wikipedia.org/wiki/Open_formula)
- [Operation (mathematics)](https://en.wikipedia.org/wiki/Operation_(mathematics))
- [Operational definition](https://en.wikipedia.org/wiki/Operational_definition)
- [Ordered pair](https://en.wikipedia.org/wiki/Ordered_pair)
- [Ordinal analysis](https://en.wikipedia.org/wiki/Ordinal_analysis)
- [Ordinal number](https://en.wikipedia.org/wiki/Ordinal_number)
- [Orrin Frink](https://en.wikipedia.org/wiki/Orrin_Frink)
- [P (complexity)](https://en.wikipedia.org/wiki/P_(complexity))
- [P versus NP problem](https://en.wikipedia.org/wiki/P_versus_NP_problem)
- [Paradoxes of set theory](https://en.wikipedia.org/wiki/Paradoxes_of_set_theory)
- [Parallel computing](https://en.wikipedia.org/wiki/Parallel_computing)
- [Parameter (computer programming)](https://en.wikipedia.org/wiki/Parameter_(computer_programming))
- [Partial function](https://en.wikipedia.org/wiki/Partial_function)
- [Partially ordered set](https://en.wikipedia.org/wiki/Partially_ordered_set)
- [Partition of a set](https://en.wikipedia.org/wiki/Partition_of_a_set)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Peano axioms](https://en.wikipedia.org/wiki/Peano_axioms)
- [Performative utterance](https://en.wikipedia.org/wiki/Performative_utterance)
- [Peter B. Andrews](https://en.wikipedia.org/wiki/Peter_B._Andrews)
- [Peter Landin](https://en.wikipedia.org/wiki/Peter_Landin)
- [Philosophy](https://en.wikipedia.org/wiki/Philosophy)
- [Philosophy of language](https://en.wikipedia.org/wiki/Philosophy_of_language)
- [Philosophy of mathematics](https://en.wikipedia.org/wiki/Philosophy_of_mathematics)
- [Plural quantification](https://en.wikipedia.org/wiki/Plural_quantification)
- [Polarity item](https://en.wikipedia.org/wiki/Polarity_item)
- [Polynomial](https://en.wikipedia.org/wiki/Polynomial)
- [PDF](https://en.wikipedia.org/wiki/PDF)
- [Possible world](https://en.wikipedia.org/wiki/Possible_world)
- [Power set](https://en.wikipedia.org/wiki/Power_set)
- [Pragmatics](https://en.wikipedia.org/wiki/Pragmatics)
- [Predicate (mathematical logic)](https://en.wikipedia.org/wiki/Predicate_(mathematical_logic))
- [First-order logic](https://en.wikipedia.org/wiki/First-order_logic)
- [Predicate variable](https://en.wikipedia.org/wiki/Predicate_variable)
- [Presupposition](https://en.wikipedia.org/wiki/Presupposition)
- [Primitive recursive arithmetic](https://en.wikipedia.org/wiki/Primitive_recursive_arithmetic)
- [Primitive recursive function](https://en.wikipedia.org/wiki/Primitive_recursive_function)
- [Princeton University](https://en.wikipedia.org/wiki/Princeton_University)
- [Principia Mathematica](https://en.wikipedia.org/wiki/Principia_Mathematica)
- [Principle of compositionality](https://en.wikipedia.org/wiki/Principle_of_compositionality)
- [Privative adjective](https://en.wikipedia.org/wiki/Privative_adjective)
- [Procedural programming](https://en.wikipedia.org/wiki/Procedural_programming)
- [Process calculus](https://en.wikipedia.org/wiki/Process_calculus)
- [Programming idiom](https://en.wikipedia.org/wiki/Programming_idiom)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Programming language theory](https://en.wikipedia.org/wiki/Programming_language_theory)
- [Proof of impossibility](https://en.wikipedia.org/wiki/Proof_of_impossibility)
- [Proof theory](https://en.wikipedia.org/wiki/Proof_theory)
- [Proposition](https://en.wikipedia.org/wiki/Proposition)
- [Propositional attitude](https://en.wikipedia.org/wiki/Propositional_attitude)
- [Propositional calculus](https://en.wikipedia.org/wiki/Propositional_calculus)
- [Propositional formula](https://en.wikipedia.org/wiki/Propositional_formula)
- [Propositional variable](https://en.wikipedia.org/wiki/Propositional_variable)
- [Pure type system](https://en.wikipedia.org/wiki/Pure_type_system)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quantificational variability effect](https://en.wikipedia.org/wiki/Quantificational_variability_effect)
- [Quantifier (logic)](https://en.wikipedia.org/wiki/Quantifier_(logic))
- [Operator (linguistics)](https://en.wikipedia.org/wiki/Operator_(linguistics))
- [Quantifier rank](https://en.wikipedia.org/wiki/Quantifier_rank)
- [Quantization (linguistics)](https://en.wikipedia.org/wiki/Quantization_(linguistics))
- [Question under discussion](https://en.wikipedia.org/wiki/Question_under_discussion)
- [Rational function](https://en.wikipedia.org/wiki/Rational_function)
- [Raymond Smullyan](https://en.wikipedia.org/wiki/Raymond_Smullyan)
- [Real-valued function](https://en.wikipedia.org/wiki/Real-valued_function)
- [Recursion](https://en.wikipedia.org/wiki/Recursion)
- [Recursive definition](https://en.wikipedia.org/wiki/Recursive_definition)
- [Computable set](https://en.wikipedia.org/wiki/Computable_set)
- [Reduction strategy](https://en.wikipedia.org/wiki/Reduction_strategy)
- [Reduction strategy](https://en.wikipedia.org/wiki/Reduction_strategy)
- [Reference](https://en.wikipedia.org/wiki/Reference)
- [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Relation (mathematics)](https://en.wikipedia.org/wiki/Relation_(mathematics))
- [Responsive predicate](https://en.wikipedia.org/wiki/Responsive_predicate)
- [Restriction (mathematics)](https://en.wikipedia.org/wiki/Restriction_(mathematics))
- [Reverse mathematics](https://en.wikipedia.org/wiki/Reverse_mathematics)
- [Rewriting](https://en.wikipedia.org/wiki/Rewriting)
- [Rewriting](https://en.wikipedia.org/wiki/Rewriting)
- [Richard Montague](https://en.wikipedia.org/wiki/Richard_Montague)
- [Rising declarative](https://en.wikipedia.org/wiki/Rising_declarative)
- [Robinson arithmetic](https://en.wikipedia.org/wiki/Robinson_arithmetic)
- [Rule of inference](https://en.wikipedia.org/wiki/Rule_of_inference)
- [Russell's paradox](https://en.wikipedia.org/wiki/Russell%27s_paradox)
- [Ruy de Queiroz](https://en.wikipedia.org/wiki/Ruy_de_Queiroz)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [SECD machine](https://en.wikipedia.org/wiki/SECD_machine)
- [SKI combinator calculus](https://en.wikipedia.org/wiki/SKI_combinator_calculus)
- [Satisfiability](https://en.wikipedia.org/wiki/Satisfiability)
- [Saturated model](https://en.wikipedia.org/wiki/Saturated_model)
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scalar implicature](https://en.wikipedia.org/wiki/Scalar_implicature)
- [Scheme (programming language)](https://en.wikipedia.org/wiki/Scheme_(programming_language))
- [Schröder–Bernstein theorem](https://en.wikipedia.org/wiki/Schr%C3%B6der%E2%80%93Bernstein_theorem)
- [Scope (formal semantics)](https://en.wikipedia.org/wiki/Scope_(formal_semantics))
- [Scope (computer science)](https://en.wikipedia.org/wiki/Scope_(computer_science))
- [Scott continuity](https://en.wikipedia.org/wiki/Scott_continuity)
- [Scott–Curry theorem](https://en.wikipedia.org/wiki/Scott%E2%80%93Curry_theorem)
- [Second-order arithmetic](https://en.wikipedia.org/wiki/Second-order_arithmetic)
- [Second-order logic](https://en.wikipedia.org/wiki/Second-order_logic)
- [Discourse relation](https://en.wikipedia.org/wiki/Discourse_relation)
- [Self-reference](https://en.wikipedia.org/wiki/Self-reference)
- [Self-verifying theories](https://en.wikipedia.org/wiki/Self-verifying_theories)
- [Semantic parsing](https://en.wikipedia.org/wiki/Semantic_parsing)
- [Semantic theory of truth](https://en.wikipedia.org/wiki/Semantic_theory_of_truth)
- [Semantics](https://en.wikipedia.org/wiki/Semantics)
- [Semantics (computer science)](https://en.wikipedia.org/wiki/Semantics_(computer_science))
- [Semantics of logic](https://en.wikipedia.org/wiki/Semantics_of_logic)
- [Sentence (mathematical logic)](https://en.wikipedia.org/wiki/Sentence_(mathematical_logic))
- [Sequence](https://en.wikipedia.org/wiki/Sequence)
- [Sequent calculus](https://en.wikipedia.org/wiki/Sequent_calculus)
- [Set-valued function](https://en.wikipedia.org/wiki/Set-valued_function)
- [Set (mathematics)](https://en.wikipedia.org/wiki/Set_(mathematics))
- [Set theory](https://en.wikipedia.org/wiki/Set_theory)
- [Signature (logic)](https://en.wikipedia.org/wiki/Signature_(logic))
- [Simon B. Kochen](https://en.wikipedia.org/wiki/Simon_B._Kochen)
- [Simply typed lambda calculus](https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus)
- [Singleton (mathematics)](https://en.wikipedia.org/wiki/Singleton_(mathematics))
- [Singleton (mathematics)](https://en.wikipedia.org/wiki/Singleton_(mathematics))
- [Situation semantics](https://en.wikipedia.org/wiki/Situation_semantics)
- [Skolem arithmetic](https://en.wikipedia.org/wiki/Skolem_arithmetic)
- [Sloppy identity](https://en.wikipedia.org/wiki/Sloppy_identity)
- [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)
- [Smoothness](https://en.wikipedia.org/wiki/Smoothness)
- [Soundness](https://en.wikipedia.org/wiki/Soundness)
- [Spectrum of a sentence](https://en.wikipedia.org/wiki/Spectrum_of_a_sentence)
- [Spectrum of a theory](https://en.wikipedia.org/wiki/Spectrum_of_a_theory)
- [Speech act](https://en.wikipedia.org/wiki/Speech_act)
- [Square of opposition](https://en.wikipedia.org/wiki/Square_of_opposition)
- [Squiggle operator](https://en.wikipedia.org/wiki/Squiggle_operator)
- [Standard ML](https://en.wikipedia.org/wiki/Standard_ML)
- [Stephen Cole Kleene](https://en.wikipedia.org/wiki/Stephen_Cole_Kleene)
- [Stephen Cole Kleene](https://en.wikipedia.org/wiki/Stephen_Cole_Kleene)
- [Strawson entailment](https://en.wikipedia.org/wiki/Strawson_entailment)
- [Strength (mathematical logic)](https://en.wikipedia.org/wiki/Strength_(mathematical_logic))
- [Strict conditional](https://en.wikipedia.org/wiki/Strict_conditional)
- [String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
- [Normal form (abstract rewriting)](https://en.wikipedia.org/wiki/Normal_form_(abstract_rewriting))
- [Structure (mathematical logic)](https://en.wikipedia.org/wiki/Structure_(mathematical_logic))
- [Structure and Interpretation of Computer Programs](https://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs)
- [Studia Logica](https://en.wikipedia.org/wiki/Studia_Logica)
- [Subsective modifier](https://en.wikipedia.org/wiki/Subsective_modifier)
- [Substitution (logic)](https://en.wikipedia.org/wiki/Substitution_(logic))
- [Substitution (logic)](https://en.wikipedia.org/wiki/Substitution_(logic))
- [Substructure (mathematics)](https://en.wikipedia.org/wiki/Substructure_(mathematics))
- [Subtrigging](https://en.wikipedia.org/wiki/Subtrigging)
- [Subtyping](https://en.wikipedia.org/wiki/Subtyping)
- [Supertask](https://en.wikipedia.org/wiki/Supertask)
- [Supervaluationism](https://en.wikipedia.org/wiki/Supervaluationism)
- [Surjective function](https://en.wikipedia.org/wiki/Surjective_function)
- [Syllogism](https://en.wikipedia.org/wiki/Syllogism)
- [Symbol (formal)](https://en.wikipedia.org/wiki/Symbol_(formal))
- [Syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar)
- [Syntax (logic)](https://en.wikipedia.org/wiki/Syntax_(logic))
- [Syntax–semantics interface](https://en.wikipedia.org/wiki/Syntax%E2%80%93semantics_interface)
- [System F](https://en.wikipedia.org/wiki/System_F)
- [T-schema](https://en.wikipedia.org/wiki/T-schema)
- [Tarski's axiomatization of the reals](https://en.wikipedia.org/wiki/Tarski%27s_axiomatization_of_the_reals)
- [Tarski's axioms](https://en.wikipedia.org/wiki/Tarski%27s_axioms)
- [Semantic theory of truth](https://en.wikipedia.org/wiki/Semantic_theory_of_truth)
- [Tarski's undefinability theorem](https://en.wikipedia.org/wiki/Tarski%27s_undefinability_theorem)
- [Tarski–Grothendieck set theory](https://en.wikipedia.org/wiki/Tarski%E2%80%93Grothendieck_set_theory)
- [Tautology (logic)](https://en.wikipedia.org/wiki/Tautology_(logic))
- [Telicity](https://en.wikipedia.org/wiki/Telicity)
- [Temperature paradox](https://en.wikipedia.org/wiki/Temperature_paradox)
- [Tense–aspect–mood](https://en.wikipedia.org/wiki/Tense%E2%80%93aspect%E2%80%93mood)
- [Term (logic)](https://en.wikipedia.org/wiki/Term_(logic))
- [Term logic](https://en.wikipedia.org/wiki/Term_logic)
- [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
- [Theorem](https://en.wikipedia.org/wiki/Theorem)
- [Truth](https://en.wikipedia.org/wiki/Truth)
- [Theory (mathematical logic)](https://en.wikipedia.org/wiki/Theory_(mathematical_logic))
- [Thierry Coquand](https://en.wikipedia.org/wiki/Thierry_Coquand)
- [Three-valued logic](https://en.wikipedia.org/wiki/Three-valued_logic)
- [Timeline of mathematical logic](https://en.wikipedia.org/wiki/Timeline_of_mathematical_logic)
- [To Mock a Mockingbird](https://en.wikipedia.org/wiki/To_Mock_a_Mockingbird)
- [Transfer principle](https://en.wikipedia.org/wiki/Transfer_principle)
- [Transitive set](https://en.wikipedia.org/wiki/Transitive_set)
- [True arithmetic](https://en.wikipedia.org/wiki/True_arithmetic)
- [Truth-conditional semantics](https://en.wikipedia.org/wiki/Truth-conditional_semantics)
- [Truth predicate](https://en.wikipedia.org/wiki/Truth_predicate)
- [Truth table](https://en.wikipedia.org/wiki/Truth_table)
- [Truth value](https://en.wikipedia.org/wiki/Truth_value)
- [Tuple](https://en.wikipedia.org/wiki/Tuple)
- [Turing completeness](https://en.wikipedia.org/wiki/Turing_completeness)
- [Turing completeness](https://en.wikipedia.org/wiki/Turing_completeness)
- [Turing machine](https://en.wikipedia.org/wiki/Turing_machine)
- [Type (model theory)](https://en.wikipedia.org/wiki/Type_(model_theory))
- [Type shifter](https://en.wikipedia.org/wiki/Type_shifter)
- [Type system](https://en.wikipedia.org/wiki/Type_system)
- [Type theory](https://en.wikipedia.org/wiki/Type_theory)
- [Type theory with records](https://en.wikipedia.org/wiki/Type_theory_with_records)
- [Typed lambda calculus](https://en.wikipedia.org/wiki/Typed_lambda_calculus)
- [Typed lambda calculus](https://en.wikipedia.org/wiki/Typed_lambda_calculus)
- [Ultrafilter on a set](https://en.wikipedia.org/wiki/Ultrafilter_on_a_set)
- [Ultraproduct](https://en.wikipedia.org/wiki/Ultraproduct)
- [Uncountable set](https://en.wikipedia.org/wiki/Uncountable_set)
- [Undecidable problem](https://en.wikipedia.org/wiki/Undecidable_problem)
- [Uninterpreted function](https://en.wikipedia.org/wiki/Uninterpreted_function)
- [Union (set theory)](https://en.wikipedia.org/wiki/Union_(set_theory))
- [Uniqueness quantification](https://en.wikipedia.org/wiki/Uniqueness_quantification)
- [Universal Turing machine](https://en.wikipedia.org/wiki/Universal_Turing_machine)
- [Universal grinder](https://en.wikipedia.org/wiki/Universal_grinder)
- [Universal Turing machine](https://en.wikipedia.org/wiki/Universal_Turing_machine)
- [Universal quantification](https://en.wikipedia.org/wiki/Universal_quantification)
- [Universal set](https://en.wikipedia.org/wiki/Universal_set)
- [Universe (mathematics)](https://en.wikipedia.org/wiki/Universe_(mathematics))
- [University of California, Los Angeles](https://en.wikipedia.org/wiki/University_of_California,_Los_Angeles)
- [Unlambda](https://en.wikipedia.org/wiki/Unlambda)
- [Up to](https://en.wikipedia.org/wiki/Up_to)
- [Urelement](https://en.wikipedia.org/wiki/Urelement)
- [Vagueness](https://en.wikipedia.org/wiki/Vagueness)
- [Validity (logic)](https://en.wikipedia.org/wiki/Validity_(logic))
- [Variable (mathematics)](https://en.wikipedia.org/wiki/Variable_(mathematics))
- [Variable shadowing](https://en.wikipedia.org/wiki/Variable_shadowing)
- [Venn diagram](https://en.wikipedia.org/wiki/Venn_diagram)
- [Veridicality](https://en.wikipedia.org/wiki/Veridicality)
- [Virtual machine](https://en.wikipedia.org/wiki/Virtual_machine)
- [Von Neumann universe](https://en.wikipedia.org/wiki/Von_Neumann_universe)
- [Von Neumann–Bernays–Gödel set theory](https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Bernays%E2%80%93G%C3%B6del_set_theory)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Normal form (abstract rewriting)](https://en.wikipedia.org/wiki/Normal_form_(abstract_rewriting))
- [Well-formed formula](https://en.wikipedia.org/wiki/Well-formed_formula)
- [William Bigelow Easton](https://en.wikipedia.org/wiki/William_Bigelow_Easton)
- [William Boone (mathematician)](https://en.wikipedia.org/wiki/William_Boone_(mathematician))
- [Wolfram Language](https://en.wikipedia.org/wiki/Wolfram_Language)
- [Zermelo–Fraenkel set theory](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory)
- [Wikipedia:Foldoc license](https://en.wikipedia.org/wiki/Wikipedia:Foldoc_license)
- [Template:Alonzo Church](https://en.wikipedia.org/wiki/Template:Alonzo_Church)
- [Template:Formal semantics](https://en.wikipedia.org/wiki/Template:Formal_semantics)
- [Template:Functions navbox](https://en.wikipedia.org/wiki/Template:Functions_navbox)
- [Template:Mathematical logic](https://en.wikipedia.org/wiki/Template:Mathematical_logic)
- [Template talk:Alonzo Church](https://en.wikipedia.org/wiki/Template_talk:Alonzo_Church)
- [Template talk:Formal semantics](https://en.wikipedia.org/wiki/Template_talk:Formal_semantics)
- [Template talk:Mathematical logic](https://en.wikipedia.org/wiki/Template_talk:Mathematical_logic)
- [Help:Authority control](https://en.wikipedia.org/wiki/Help:Authority_control)
- [Category:Functions](https://en.wikipedia.org/wiki/Category:Functions)
- [Category:Theorems in the foundations of mathematics](https://en.wikipedia.org/wiki/Category:Theorems_in_the_foundations_of_mathematics)
- [Portal:Mathematics](https://en.wikipedia.org/wiki/Portal:Mathematics)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:39:21.640794+00:00_