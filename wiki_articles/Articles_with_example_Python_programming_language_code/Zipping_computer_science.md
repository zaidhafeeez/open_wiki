---
title: Zipping (computer science)
url: https://en.wikipedia.org/wiki/Zipping_(computer_science)
language: en
categories: ["Category:Articles with example Clojure code", "Category:Articles with example Haskell code", "Category:Articles with example Lisp (programming language) code", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Data mapping", "Category:Short description is different from Wikidata"]
references: 0
last_modified: 2024-12-19T13:47:31Z
---

# Zipping (computer science)

## Summary

In computer science, zipping is a function which maps a tuple of sequences into a sequence of tuples.  This name zip derives from the action of a zipper in that it interleaves two formerly disjoint sequences.  The inverse function is unzip.

## Full Content

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
