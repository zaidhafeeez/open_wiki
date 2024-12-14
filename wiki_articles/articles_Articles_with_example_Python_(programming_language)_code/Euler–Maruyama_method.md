# Euler–Maruyama method

## Article Metadata

- **Last Updated:** 2024-12-14T19:36:45.603505+00:00
- **Original Article:** [Euler–Maruyama method](https://en.wikipedia.org/wiki/Euler%E2%80%93Maruyama_method)
- **Language:** en
- **Page ID:** 7139118

## Summary

In Itô calculus, the Euler–Maruyama method (also simply called the Euler method) is a method for the approximate numerical solution of a stochastic differential equation (SDE). It is an extension of the Euler method for ordinary differential equations to stochastic differential equations named after Leonhard Euler and Gisiro Maruyama. The same generalization cannot be done for any arbitrary deterministic method.
Consider the stochastic differential equation (see Itô calculus)

  
    
      
   

## Categories

- Category:Articles with example MATLAB/Octave code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Leonhard Euler
- Category:Numerical differential equations
- Category:Short description is different from Wikidata
- Category:Stochastic differential equations

## Table of Contents

- Example
- See also

## Content

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

## Related Articles

### Internal Links

- [Euler's continued fraction formula](https://en.wikipedia.org/wiki/Euler%27s_continued_fraction_formula)
- [Euler's critical load](https://en.wikipedia.org/wiki/Euler%27s_critical_load)
- [Euler's formula](https://en.wikipedia.org/wiki/Euler%27s_formula)
- [Euler's four-square identity](https://en.wikipedia.org/wiki/Euler%27s_four-square_identity)
- [Euler's identity](https://en.wikipedia.org/wiki/Euler%27s_identity)
- [Euler's pump and turbine equation](https://en.wikipedia.org/wiki/Euler%27s_pump_and_turbine_equation)
- [Euler's rotation theorem](https://en.wikipedia.org/wiki/Euler%27s_rotation_theorem)
- [Euler's sum of powers conjecture](https://en.wikipedia.org/wiki/Euler%27s_sum_of_powers_conjecture)
- [Euler's theorem](https://en.wikipedia.org/wiki/Euler%27s_theorem)
- [Euler equations (fluid dynamics)](https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics))
- [Euler function](https://en.wikipedia.org/wiki/Euler_function)
- [Euler method](https://en.wikipedia.org/wiki/Euler_method)
- [Euler number (physics)](https://en.wikipedia.org/wiki/Euler_number_(physics))
- [Euler numbers](https://en.wikipedia.org/wiki/Euler_numbers)
- [Euler–Bernoulli beam theory](https://en.wikipedia.org/wiki/Euler%E2%80%93Bernoulli_beam_theory)
- [Euler–Lagrange equation](https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation)
- [Euler–Lotka equation](https://en.wikipedia.org/wiki/Euler%E2%80%93Lotka_equation)
- [Euler–Maclaurin formula](https://en.wikipedia.org/wiki/Euler%E2%80%93Maclaurin_formula)
- [Euler's constant](https://en.wikipedia.org/wiki/Euler%27s_constant)
- [Euler–Poisson–Darboux equation](https://en.wikipedia.org/wiki/Euler%E2%80%93Poisson%E2%80%93Darboux_equation)
- [Euler–Rodrigues formula](https://en.wikipedia.org/wiki/Euler%E2%80%93Rodrigues_formula)
- [Euler–Tricomi equation](https://en.wikipedia.org/wiki/Euler%E2%80%93Tricomi_equation)
- [Expected value](https://en.wikipedia.org/wiki/Expected_value)
- [Gene expression](https://en.wikipedia.org/wiki/Gene_expression)
- [Gisiro Maruyama](https://en.wikipedia.org/wiki/Gisiro_Maruyama)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Independent and identically distributed random variables](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables)
- [Initial condition](https://en.wikipedia.org/wiki/Initial_condition)
- [Itô calculus](https://en.wikipedia.org/wiki/It%C3%B4_calculus)
- [Leimkuhler–Matthews method](https://en.wikipedia.org/wiki/Leimkuhler%E2%80%93Matthews_method)
- [Leonhard Euler](https://en.wikipedia.org/wiki/Leonhard_Euler)
- [List of topics named after Leonhard Euler](https://en.wikipedia.org/wiki/List_of_topics_named_after_Leonhard_Euler)
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [Markov chain](https://en.wikipedia.org/wiki/Markov_chain)
- [Mathematical and theoretical biology](https://en.wikipedia.org/wiki/Mathematical_and_theoretical_biology)
- [Milstein method](https://en.wikipedia.org/wiki/Milstein_method)
- [Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)
- [NumPy](https://en.wikipedia.org/wiki/NumPy)
- [Numerical analysis](https://en.wikipedia.org/wiki/Numerical_analysis)
- [Ordinary differential equation](https://en.wikipedia.org/wiki/Ordinary_differential_equation)
- [Ornstein–Uhlenbeck process](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Random variable](https://en.wikipedia.org/wiki/Random_variable)
- [Runge–Kutta method (SDE)](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_method_(SDE))
- [Stochastic differential equation](https://en.wikipedia.org/wiki/Stochastic_differential_equation)
- [Variance](https://en.wikipedia.org/wiki/Variance)
- [Wiener process](https://en.wikipedia.org/wiki/Wiener_process)
- [Template:Leonhard Euler](https://en.wikipedia.org/wiki/Template:Leonhard_Euler)
- [Template talk:Leonhard Euler](https://en.wikipedia.org/wiki/Template_talk:Leonhard_Euler)
- [Category:Leonhard Euler](https://en.wikipedia.org/wiki/Category:Leonhard_Euler)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:36:45.603505+00:00_