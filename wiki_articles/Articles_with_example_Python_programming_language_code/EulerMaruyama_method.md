---
title: Euler–Maruyama method
url: https://en.wikipedia.org/wiki/Euler%E2%80%93Maruyama_method
language: en
categories: ["Category:Articles with example MATLAB/Octave code", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Leonhard Euler", "Category:Numerical differential equations", "Category:Short description is different from Wikidata", "Category:Stochastic differential equations"]
references: 0
last_modified: 2024-12-19T13:59:04Z
---

# Euler–Maruyama method

## Summary

In Itô calculus, the Euler–Maruyama method (also simply called the Euler method) is a method for the approximate numerical solution of a stochastic differential equation (SDE). It is an extension of the Euler method for ordinary differential equations to stochastic differential equations named after Leonhard Euler and Gisiro Maruyama. The same generalization cannot be done for any arbitrary deterministic method.
Consider the stochastic differential equation (see Itô calculus)

  
    
      
   

## Full Content

In Itô calculus, the Euler–Maruyama method (also simply called the Euler method) is a method for the approximate numerical solution of a stochastic differential equation (SDE). It is an extension of the Euler method for ordinary differential equations to stochastic differential equations named after Leonhard Euler and Gisiro Maruyama. The same generalization cannot be done for any arbitrary deterministic method.
Consider the stochastic differential equation (see Itô calculus)

  
    
      
        
          d
        
        
          X
          
            t
          
        
        =
        a
        (
        
          X
          
            t
          
        
        ,
        t
        )
        
        
          d
        
        t
        +
        b
        (
        
          X
          
            t
          
        
        ,
        t
        )
        
        
          d
        
        
          W
          
            t
          
        
        ,
      
    
    {\displaystyle \mathrm {d} X_{t}=a(X_{t},t)\,\mathrm {d} t+b(X_{t},t)\,\mathrm {d} W_{t},}
  

with initial condition X0 = x0, where Wt denotes the Wiener process, and suppose that we wish to solve this SDE on some interval of time [0, T]. Then the Euler–Maruyama approximation to the true solution X is the Markov chain Y defined as follows:

Partition the interval [0, T] into N equal subintervals of width 
  
    
      
        Δ
        t
        >
        0
      
    
    {\displaystyle \Delta t>0}
  
:

  
    
      
        0
        =
        
          τ
          
            0
          
        
        <
        
          τ
          
            1
          
        
        <
        ⋯
        <
        
          τ
          
            N
          
        
        =
        T
        
           and 
        
        Δ
        t
        =
        T
        
          /
        
        N
        ;
      
    
    {\displaystyle 0=\tau _{0}<\tau _{1}<\cdots <\tau _{N}=T{\text{ and }}\Delta t=T/N;}
  

Set Y0 = x0
Recursively define Yn for 0 ≤ n ≤ N-1 by

  
    
      
        
        
          Y
          
            n
            +
            1
          
        
        =
        
          Y
          
            n
          
        
        +
        a
        (
        
          Y
          
            n
          
        
        ,
        
          τ
          
            n
          
        
        )
        
        Δ
        t
        +
        b
        (
        
          Y
          
            n
          
        
        ,
        
          τ
          
            n
          
        
        )
        
        Δ
        
          W
          
            n
          
        
        ,
      
    
    {\displaystyle \,Y_{n+1}=Y_{n}+a(Y_{n},\tau _{n})\,\Delta t+b(Y_{n},\tau _{n})\,\Delta W_{n},}
  

where

  
    
      
        Δ
        
          W
          
            n
          
        
        =
        
          W
          
            
              τ
              
                n
                +
                1
              
            
          
        
        −
        
          W
          
            
              τ
              
                n
              
            
          
        
        .
      
    
    {\displaystyle \Delta W_{n}=W_{\tau _{n+1}}-W_{\tau _{n}}.}
  

The random variables ΔWn are independent and identically distributed normal random variables with expected value zero and variance Δt.

Example
Numerical simulation
An area that has benefited significantly from SDEs is mathematical biology. As many biological processes are both stochastic and continuous in nature, numerical methods of solving SDEs are highly valuable in the field.
The graphic depicts a stochastic differential equation solved using the Euler-Maruyama method. The deterministic counterpart is shown in blue.

Computer implementation
The following Python code implements the Euler–Maruyama method and uses it to solve the Ornstein–Uhlenbeck process defined by

  
    
      
        d
        
          Y
          
            t
          
        
        =
        θ
        ⋅
        (
        μ
        −
        
          Y
          
            t
          
        
        )
        
        
          
            d
          
        
        t
        +
        σ
        
        
          
            d
          
        
        
          W
          
            t
          
        
      
    
    {\displaystyle dY_{t}=\theta \cdot (\mu -Y_{t})\,{\mathrm {d} }t+\sigma \,{\mathrm {d} }W_{t}}
  

  
    
      
        
          Y
          
            0
          
        
        =
        
          Y
          
            
              i
              n
              i
              t
            
          
        
        .
      
    
    {\displaystyle Y_{0}=Y_{\mathrm {init} }.}
  

The random numbers for 
  
    
      
        
          
            d
          
        
        
          W
          
            t
          
        
      
    
    {\displaystyle {\mathrm {d} }W_{t}}
  
 are generated using the NumPy mathematics package.

The following is simply the translation of the above code into the MATLAB (R2019b) programming language:

See also
Milstein method
Runge–Kutta method (SDE)
Leimkuhler–Matthews method


== References ==
