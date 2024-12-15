# Zipping (computer science)

## Article Metadata

- **Last Updated:** 2024-12-15T04:55:33.120498+00:00
- **Original Article:** [Zipping (computer science)](https://en.wikipedia.org/wiki/Zipping_(computer_science))
- **Language:** en
- **Page ID:** 1463083

## Summary

In computer science, zipping is a function which maps a tuple of sequences into a sequence of tuples.  This name zip derives from the action of a zipper in that it interleaves two formerly disjoint sequences.  The inverse function is unzip.

## Categories

- Category:Articles with example Clojure code
- Category:Articles with example Haskell code
- Category:Articles with example Lisp (programming language) code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Data mapping
- Category:Short description is different from Wikidata

## Table of Contents

- Example
- Definition
- In programming languages
- Language comparison
- See also

## Content

In computer science, zipping is a function which maps a tuple of sequences into a sequence of tuples.  This name zip derives from the action of a zipper in that it interleaves two formerly disjoint sequences.  The inverse function is unzip.

Example
Given the three words cat, fish and be where |cat| is 3, |fish| is 4 and |be| is 2. Let 
  
    
      
        ℓ
      
    
    {\displaystyle \ell }
  
 denote the length of the longest word which is fish; 
  
    
      
        ℓ
        =
        4
      
    
    {\displaystyle \ell =4}
  
. The zip of cat, fish, be is then 4 tuples of elements:

  
    
      
        (
        c
        ,
        f
        ,
        b
        )
        (
        a
        ,
        i
        ,
        e
        )
        (
        t
        ,
        s
        ,
        #
        )
        (
        #
        ,
        h
        ,
        #
        )
      
    
    {\displaystyle (c,f,b)(a,i,e)(t,s,\#)(\#,h,\#)}
  

where # is a symbol not in the original alphabet. In Haskell this truncates to the shortest sequence 
  
    
      
        
          
            ℓ
            _
          
        
      
    
    {\displaystyle {\underline {\ell }}}
  
, where 
  
    
      
        
          
            ℓ
            _
          
        
        =
        2
      
    
    {\displaystyle {\underline {\ell }}=2}
  
:

Definition
Let Σ be an alphabet, # a symbol not in Σ.
Let x1x2... x|x|, y1y2... y|y|, z1z2... z|z|, ... be n words (i.e. finite sequences) of elements of Σ. Let 
  
    
      
        ℓ
      
    
    {\displaystyle \ell }
  
 denote the length of the longest word, i.e. the maximum of |x|, |y|, |z|, ... .
The zip of these words is a finite sequence of n-tuples of elements of (Σ ∪ {#}), i.e. an element of 
  
    
      
        (
        (
        Σ
        ∪
        {
        #
        }
        
          )
          
            n
          
        
        
          )
          
            ∗
          
        
      
    
    {\displaystyle ((\Sigma \cup \{\#\})^{n})^{*}}
  
:

  
    
      
        (
        
          x
          
            1
          
        
        ,
        
          y
          
            1
          
        
        ,
        …
        )
        (
        
          x
          
            2
          
        
        ,
        
          y
          
            2
          
        
        ,
        …
        )
        …
        (
        
          x
          
            ℓ
          
        
        ,
        
          y
          
            ℓ
          
        
        ,
        …
        )
      
    
    {\displaystyle (x_{1},y_{1},\ldots )(x_{2},y_{2},\ldots )\ldots (x_{\ell },y_{\ell },\ldots )}
  
,
where for any index i > |w|, the wi is #.
The zip of x, y, z, ... is denoted zip(x, y, z, ...) or x ⋆ y ⋆ z ⋆ ...
The inverse to zip is sometimes denoted unzip.
A variation of the zip operation is defined by:

  
    
      
        (
        
          x
          
            1
          
        
        ,
        
          y
          
            1
          
        
        ,
        …
        )
        (
        
          x
          
            2
          
        
        ,
        
          y
          
            2
          
        
        ,
        …
        )
        …
        (
        
          x
          
            
              ℓ
              _
            
          
        
        ,
        
          y
          
            
              ℓ
              _
            
          
        
        ,
        …
        )
      
    
    {\displaystyle (x_{1},y_{1},\ldots )(x_{2},y_{2},\ldots )\ldots (x_{\underline {\ell }},y_{\underline {\ell }},\ldots )}
  

where 
  
    
      
        
          
            ℓ
            _
          
        
      
    
    {\displaystyle {\underline {\ell }}}
  
 is the minimum length of the input words.  It avoids the use of an adjoined element 
  
    
      
        #
      
    
    {\displaystyle \#}
  
, but destroys information about elements of the input sequences beyond 
  
    
      
        
          
            ℓ
            _
          
        
      
    
    {\displaystyle {\underline {\ell }}}
  
.

In programming languages
Zip functions are often available in programming languages, often referred to as zip. In Lisp-dialects one can simply map the desired function over the desired lists, map is variadic in Lisp so it can take an arbitrary number of lists as argument. An example from Clojure:

In Common Lisp:

Languages such as Python provide a zip() function. zip() in conjunction with the * operator unzips a list:

Haskell has a method of zipping sequences but requires a specific function for each arity (zip for two sequences, zip3 for three etc.), similarly the functions unzip and unzip3 are available for unzipping:

Language comparison
List of languages by support of zip:

See also
Map (higher-order function)


== References ==

## Related Articles

### Internal Links

- [Alphabet (formal languages)](https://en.wikipedia.org/wiki/Alphabet_(formal_languages))
- [Arity](https://en.wikipedia.org/wiki/Arity)
- [Chapel (programming language)](https://en.wikipedia.org/wiki/Chapel_(programming_language))
- [Clojure](https://en.wikipedia.org/wiki/Clojure)
- [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Data mapping](https://en.wikipedia.org/wiki/Data_mapping)
- [F Sharp (programming language)](https://en.wikipedia.org/wiki/F_Sharp_(programming_language))
- [Data compression](https://en.wikipedia.org/wiki/Data_compression)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [Lisp (programming language)](https://en.wikipedia.org/wiki/Lisp_(programming_language))
- [Map (higher-order function)](https://en.wikipedia.org/wiki/Map_(higher-order_function))
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Sequence](https://en.wikipedia.org/wiki/Sequence)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Tuple](https://en.wikipedia.org/wiki/Tuple)
- [Uniform Function Call Syntax](https://en.wikipedia.org/wiki/Uniform_Function_Call_Syntax)
- [Variadic function](https://en.wikipedia.org/wiki/Variadic_function)
- [Formal language](https://en.wikipedia.org/wiki/Formal_language)
- [Zipper](https://en.wikipedia.org/wiki/Zipper)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:55:33.120498+00:00_