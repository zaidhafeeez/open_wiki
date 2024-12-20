---
title: TPK algorithm
url: https://en.wikipedia.org/wiki/TPK_algorithm
language: en
categories: ["Category:1977 in computing", "Category:Articles with example ALGOL 60 code", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Computer programming folklore", "Category:Donald Knuth", "Category:Short description matches Wikidata", "Category:Test items in computer languages"]
references: 0
last_modified: 2024-12-19T13:46:39Z
---

# TPK algorithm

## Summary

The TPK algorithm is a simple program introduced by Donald Knuth and Luis Trabb Pardo to illustrate the evolution of computer programming languages. In their 1977 work "The Early Development of Programming Languages", Trabb Pardo and Knuth introduced a small program that involved arrays, indexing, mathematical functions, subroutines, I/O, conditionals and iteration. They then wrote implementations of the algorithm in several early programming languages to show how such concepts were expressed.
T

## Full Content

The TPK algorithm is a simple program introduced by Donald Knuth and Luis Trabb Pardo to illustrate the evolution of computer programming languages. In their 1977 work "The Early Development of Programming Languages", Trabb Pardo and Knuth introduced a small program that involved arrays, indexing, mathematical functions, subroutines, I/O, conditionals and iteration. They then wrote implementations of the algorithm in several early programming languages to show how such concepts were expressed.
To explain the name "TPK", the authors referred to Grimm's law (which concerns the consonants 't', 'p', and 'k'), the sounds in the word "typical", and their own initials (Trabb Pardo and Knuth). In a talk based on the paper, Knuth said:

You can only appreciate how deep the subject is by seeing how good people struggled with it and how the ideas emerged one at a time. In order to study this—Luis I think was the main instigator of this idea—we take one program—one algorithm—and we write it in every language. And that way from one example we can quickly psych out the flavor of that particular language. We call this the TPK program, and well, the fact that it has the initials of Trabb Pardo and Knuth is just a funny coincidence.

The algorithm
Knuth describes it as follows:

We introduced a simple procedure called the “TPK algorithm,” and gave the flavor of each language by expressing TPK in each particular style. […] The TPK algorithm inputs eleven numbers 
  
    
      
        
          a
          
            0
          
        
        ,
        
          a
          
            1
          
        
        ,
        …
        ,
        
          a
          
            10
          
        
      
    
    {\displaystyle a_{0},a_{1},\ldots ,a_{10}}
  
; then it outputs a sequence of eleven pairs 
  
    
      
        (
        10
        ,
        
          b
          
            10
          
        
        )
        ,
        (
        9
        ,
        
          b
          
            9
          
        
        )
        ,
        …
        ,
        (
        0
        ,
        
          b
          
            0
          
        
        )
        ,
      
    
    {\displaystyle (10,b_{10}),(9,b_{9}),\ldots ,(0,b_{0}),}
  
 where

  
    
      
        
          b
          
            i
          
        
        =
        
          
            {
            
              
                
                  f
                  (
                  
                    a
                    
                      i
                    
                  
                  )
                  ,
                
                
                  
                    if 
                  
                  f
                  (
                  
                    a
                    
                      i
                    
                  
                  )
                  ≤
                  400
                  ;
                
              
              
                
                  999
                  ,
                
                
                  
                    if 
                  
                  f
                  (
                  
                    a
                    
                      i
                    
                  
                  )
                  >
                  400
                  ;
                
              
            
            
          
        
        
        f
        (
        x
        )
        =
        
          
            
              |
            
            x
            
              |
            
          
        
        +
        5
        
          x
          
            3
          
        
        .
      
    
    {\displaystyle b_{i}={\begin{cases}f(a_{i}),&{\text{if }}f(a_{i})\leq 400;\\999,&{\text{if }}f(a_{i})>400;\end{cases}}\quad f(x)={\sqrt {|x|}}+5x^{3}.}
  

This simple task is obviously not much of a challenge, in any decent computer language.
In pseudocode:

ask for 11 numbers to be read into a sequence S
reverse sequence S
for each item in sequence S
    call a function to do an operation
    if result overflows
        alert user
    else
        print result

The algorithm reads eleven numbers from an input device, stores them in an array, and then processes them in reverse order, applying a user-defined function to each value and reporting either the value of the function or a message to the effect that the value has exceeded some threshold.

Implementations
Implementations in the original paper
In the original paper, which covered "roughly the first decade" of the development of high-level programming languages (from 1945 up to 1957), they gave the following example implementation "in a dialect of ALGOL 60", noting that ALGOL 60 was a later development than the languages actually discussed in the paper:

As many of the early high-level languages could not handle the TPK algorithm exactly, they allow the following modifications:

If the language supports only integer variables, then assume that all inputs and outputs are integer-valued, and that sqrt(x) means the largest integer not exceeding 
  
    
      
        
          
            x
          
        
      
    
    {\displaystyle {\sqrt {x}}}
  
.
If the language does not support alphabetic output, then instead of the string 'TOO LARGE', output the number 999.
If the language does not allow any input and output, then assume that the 11 input values 
  
    
      
        
          a
          
            0
          
        
        ,
        
          a
          
            1
          
        
        ,
        …
        ,
        
          a
          
            10
          
        
      
    
    {\displaystyle a_{0},a_{1},\ldots ,a_{10}}
  
 have been supplied by an external process somehow, and the task is to compute the 22 output values 
  
    
      
        10
        ,
        f
        (
        10
        )
        ,
        9
        ,
        f
        (
        9
        )
        ,
        …
        ,
        0
        ,
        f
        (
        0
        )
      
    
    {\displaystyle 10,f(10),9,f(9),\ldots ,0,f(0)}
  
 (with 999 replacing too-large values of 
  
    
      
        f
        (
        i
        )
      
    
    {\displaystyle f(i)}
  
).
If the language does not allow programmers to define their own functions, then replace f(a[i]) with an expression equivalent to 
  
    
      
        
          
            
              |
            
            
              a
              
                i
              
            
            
              |
            
          
        
        +
        5
        
          x
          
            3
          
        
      
    
    {\displaystyle {\sqrt {|a_{i}|}}+5x^{3}}
  
.
With these modifications when necessary, the authors implement this algorithm in Konrad Zuse's Plankalkül, in Goldstine and von Neumann's flow diagrams, in Haskell Curry's proposed notation, in Short Code of John Mauchly and others, in the Intermediate Program Language of Arthur Burks, in the notation of Heinz Rutishauser, in the language and compiler by Corrado Böhm in 1951–52, in Autocode of Alick Glennie, in the A-2 system of Grace Hopper, in the Laning and Zierler system, in the earliest proposed Fortran (1954) of John Backus, in the Autocode for Mark 1 by Tony Brooker, in ПП-2 of Andrey Ershov, in BACAIC of Mandalay Grems and R. E. Porter, in Kompiler 2 of A. Kenton Elsworth and others, in ADES of E. K. Blum, the Internal Translator of Alan Perlis, in Fortran of John Backus, in ARITH-MATIC and MATH-MATIC from Grace Hopper's lab, in the system of Bauer and Samelson, and (in addenda in 2003 and 2009) PACT I and TRANSCODE. They then describe what kind of arithmetic was available, and provide a subjective rating of these languages on parameters of "implementation", "readability", "control structures", "data structures", "machine independence" and "impact", besides mentioning what each was the first to do.

Implementations in more recent languages
C implementation
This shows a C implementation equivalent to the above ALGOL 60.

Python implementation
This shows a Python implementation.

Rust implementation
This shows a Rust implementation.

References
External links
Implementations in many languages at Rosetta Code
Implementations in several languages
