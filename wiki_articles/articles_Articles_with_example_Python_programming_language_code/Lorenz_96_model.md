# Lorenz 96 model

## Article Metadata

- **Last Updated:** 2024-12-15T04:34:00.066701+00:00
- **Original Article:** [Lorenz 96 model](https://en.wikipedia.org/wiki/Lorenz_96_model)
- **Language:** en
- **Page ID:** 33035511

## Summary

The Lorenz 96 model is a dynamical system formulated by Edward Lorenz in 1996. It is defined as follows. For 
  
    
      
        i
        =
        1
        ,
        .
        .
        .
        ,
        N
      
    
    {\displaystyle i=1,...,N}
  
:

  
    
      
        
          
            
              d
              
                x
                
                  i
                
              
            
            
              d
              t
            


## Categories

- Category:Articles with example Julia code
- Category:Articles with example Python (programming language) code
- Category:Chaotic maps

## Table of Contents

- Python simulation
- Julia simulation

## Content

The Lorenz 96 model is a dynamical system formulated by Edward Lorenz in 1996. It is defined as follows. For 
  
    
      
        i
        =
        1
        ,
        .
        .
        .
        ,
        N
      
    
    {\displaystyle i=1,...,N}
  
:

  
    
      
        
          
            
              d
              
                x
                
                  i
                
              
            
            
              d
              t
            
          
        
        =
        (
        
          x
          
            i
            +
            1
          
        
        −
        
          x
          
            i
            −
            2
          
        
        )
        
          x
          
            i
            −
            1
          
        
        −
        
          x
          
            i
          
        
        +
        F
      
    
    {\displaystyle {\frac {dx_{i}}{dt}}=(x_{i+1}-x_{i-2})x_{i-1}-x_{i}+F}
  

where it is assumed that 
  
    
      
        
          x
          
            −
            1
          
        
        =
        
          x
          
            N
            −
            1
          
        
        ,
        
          x
          
            0
          
        
        =
        
          x
          
            N
          
        
      
    
    {\displaystyle x_{-1}=x_{N-1},x_{0}=x_{N}}
  
 and 
  
    
      
        
          x
          
            N
            +
            1
          
        
        =
        
          x
          
            1
          
        
      
    
    {\displaystyle x_{N+1}=x_{1}}
  
 and 
  
    
      
        N
        ≥
        4
      
    
    {\displaystyle N\geq 4}
  
. Here 
  
    
      
        
          x
          
            i
          
        
      
    
    {\displaystyle x_{i}}
  
 is the state of the system and 
  
    
      
        F
      
    
    {\displaystyle F}
  
 is a forcing constant. 
  
    
      
        F
        =
        8
      
    
    {\displaystyle F=8}
  
 is a common value known to cause chaotic behavior.
It is commonly used as a model problem in data assimilation.

Python simulation
Julia simulation


== References ==

## Related Articles

### Internal Links

- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Data assimilation](https://en.wikipedia.org/wiki/Data_assimilation)
- [Dynamical system](https://en.wikipedia.org/wiki/Dynamical_system)
- [Edward Norton Lorenz](https://en.wikipedia.org/wiki/Edward_Norton_Lorenz)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:34:00.066701+00:00_