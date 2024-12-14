# Wang and Landau algorithm

## Article Metadata

- **Last Updated:** 2024-12-14T19:47:12.093344+00:00
- **Original Article:** [Wang and Landau algorithm](https://en.wikipedia.org/wiki/Wang_and_Landau_algorithm)
- **Language:** en
- **Page ID:** 17506694

## Summary

The Wang and Landau algorithm, proposed by  Fugao Wang and David P. Landau, is a Monte Carlo method designed to estimate the density of states of a system. The method performs a non-Markovian random walk to build the density of states by quickly visiting all the available energy spectrum. The Wang and Landau algorithm is an important method to obtain the density of states required to perform a multicanonical simulation.
The Wang–Landau algorithm can be applied to any system which is characterize

## Categories

- Category:Articles with example Python (programming language) code
- Category:Computational physics
- Category:Markov chain Monte Carlo
- Category:Statistical algorithms

## Table of Contents

- Overview
- Algorithm
- Test system
- Sample code
- Wang and Landau molecular dynamics: Statistical Temperature Molecular Dynamics (STMD)

## Content

The Wang and Landau algorithm, proposed by  Fugao Wang and David P. Landau, is a Monte Carlo method designed to estimate the density of states of a system. The method performs a non-Markovian random walk to build the density of states by quickly visiting all the available energy spectrum. The Wang and Landau algorithm is an important method to obtain the density of states required to perform a multicanonical simulation.
The Wang–Landau algorithm can be applied to any system which is characterized by a cost (or energy) function. For instance,
it has been applied to the solution of numerical integrals and the folding of proteins.
The Wang–Landau sampling is related to the metadynamics algorithm.

Overview
The Wang and Landau algorithm is used to obtain an estimate for the density of states of a system characterized by a cost function. It uses a non-Markovian stochastic process which asymptotically converges to a multicanonical ensemble. (I.e. to a Metropolis–Hastings algorithm with sampling distribution inverse to the density of states) The major consequence is that this sampling distribution leads to a simulation where the energy barriers are invisible. This means that the algorithm visits all the accessible states (favorable and less favorable) much faster than a Metropolis algorithm.

Algorithm
Consider a system defined on a phase space 
  
    
      
        Ω
      
    
    {\displaystyle \Omega }
  
, and a cost function, E, (e.g. the energy), bounded on a spectrum 
  
    
      
        E
        ∈
        Γ
        =
        [
        
          E
          
            min
          
        
        ,
        
          E
          
            max
          
        
        ]
      
    
    {\displaystyle E\in \Gamma =[E_{\min },E_{\max }]}
  
, which has an associated density of states 
  
    
      
        ρ
        (
        E
        )
      
    
    {\displaystyle \rho (E)}
  
, which is to be estimated. The estimator is 
  
    
      
        
          
            
              ρ
              ^
            
          
        
        (
        E
        )
        ≡
        exp
        ⁡
        (
        S
        (
        E
        )
        )
      
    
    {\displaystyle {\hat {\rho }}(E)\equiv \exp(S(E))}
  
. Because Wang and Landau algorithm works in discrete spectra, the spectrum 
  
    
      
        Γ
      
    
    {\displaystyle \Gamma }
  
 is divided in N discrete values with a difference between them of 
  
    
      
        Δ
      
    
    {\displaystyle \Delta }
  
, such that

  
    
      
        Δ
        =
        
          
            
              
                E
                
                  max
                
              
              −
              
                E
                
                  min
                
              
            
            N
          
        
      
    
    {\displaystyle \Delta ={\frac {E_{\max }-E_{\min }}{N}}}
  
.
Given this discrete spectrum, the algorithm is initialized by:

setting all entries of the microcanonical entropy to zero, 
  
    
      
        S
        (
        
          E
          
            i
          
        
        )
        =
        0
         
         
        i
        =
        1
        ,
        2
        ,
        .
        .
        .
        ,
        N
      
    
    {\displaystyle S(E_{i})=0\ \ i=1,2,...,N}
  

initializing 
  
    
      
        f
        =
        1
      
    
    {\displaystyle f=1}
  
 and
initializing the system randomly, by putting in a random configuration 
  
    
      
        
          r
        
        ∈
        Ω
      
    
    {\displaystyle {\boldsymbol {r}}\in \Omega }
  
.
The algorithm then performs a multicanonical ensemble simulation: a Metropolis–Hastings random walk in the phase space of the system with a probability distribution given by 
  
    
      
        P
        (
        
          r
        
        )
        =
        1
        
          /
        
        
          
            
              ρ
              ^
            
          
        
        (
        E
        (
        
          r
        
        )
        )
        =
        exp
        ⁡
        (
        −
        S
        (
        E
        (
        
          r
        
        )
        )
        )
      
    
    {\displaystyle P({\boldsymbol {r}})=1/{\hat {\rho }}(E({\boldsymbol {r}}))=\exp(-S(E({\boldsymbol {r}})))}
  
 and a probability of proposing a new state given by a probability distribution 
  
    
      
        g
        (
        
          r
        
        →
        
          
            r
          
          ′
        
        )
      
    
    {\displaystyle g({\boldsymbol {r}}\rightarrow {\boldsymbol {r}}')}
  
. A histogram 
  
    
      
        H
        (
        E
        )
      
    
    {\displaystyle H(E)}
  
 of visited energies is stored. Like in the Metropolis–Hastings algorithm, a proposal-acceptance step is performed, and consists in (see Metropolis–Hastings algorithm overview):

proposing a state 
  
    
      
        
          
            r
          
          ′
        
        ∈
        Ω
      
    
    {\displaystyle {\boldsymbol {r}}'\in \Omega }
  
 according to the arbitrary proposal distribution 
  
    
      
        g
        (
        
          r
        
        →
        
          
            r
          
          ′
        
        )
      
    
    {\displaystyle g({\boldsymbol {r}}\rightarrow {\boldsymbol {r}}')}
  

accept/refuse the proposed state according to

  
    
      
        A
        (
        
          r
        
        →
        
          
            r
          
          ′
        
        )
        =
        min
        
          (
          
            1
            ,
            
              e
              
                S
                −
                
                  S
                  ′
                
              
            
            
              
                
                  g
                  (
                  
                    
                      r
                    
                    ′
                  
                  →
                  
                    r
                  
                  )
                
                
                  g
                  (
                  
                    r
                  
                  →
                  
                    
                      r
                    
                    ′
                  
                  )
                
              
            
          
          )
        
      
    
    {\displaystyle A({\boldsymbol {r}}\rightarrow {\boldsymbol {r}}')=\min \left(1,e^{S-S'}{\frac {g({\boldsymbol {r}}'\rightarrow {\boldsymbol {r}})}{g({\boldsymbol {r}}\rightarrow {\boldsymbol {r}}')}}\right)}
  

where 
  
    
      
        S
        =
        S
        (
        E
        (
        
          r
        
        )
        )
      
    
    {\displaystyle S=S(E({\boldsymbol {r}}))}
  
 and 
  
    
      
        
          S
          ′
        
        =
        S
        (
        E
        (
        
          
            r
          
          ′
        
        )
        )
      
    
    {\displaystyle S'=S(E({\boldsymbol {r}}'))}
  
.
After each proposal-acceptance step, the system transits to some value 
  
    
      
        
          E
          
            i
          
        
      
    
    {\displaystyle E_{i}}
  
, 
  
    
      
        H
        (
        
          E
          
            i
          
        
        )
      
    
    {\displaystyle H(E_{i})}
  
 is incremented by one and the following update is performed:

  
    
      
        S
        (
        
          E
          
            i
          
        
        )
        ←
        S
        (
        
          E
          
            i
          
        
        )
        +
        f
      
    
    {\displaystyle S(E_{i})\leftarrow S(E_{i})+f}
  
.
This is the crucial step of the algorithm, and it is what makes the Wang and Landau algorithm non-Markovian: the stochastic process now depends on the history of the process. Hence the next time there is a proposal to a state with that particular energy 
  
    
      
        
          E
          
            i
          
        
      
    
    {\displaystyle E_{i}}
  
, that proposal is now more likely refused; in this sense, the algorithm forces the system to visit all of the spectrum equally. The consequence is that the histogram 
  
    
      
        H
        (
        E
        )
      
    
    {\displaystyle H(E)}
  
 is more and more flat. However, this flatness depends on how well-approximated the calculated entropy is to the exact entropy, which naturally depends on the value of f. To better and better approximate the exact entropy (and thus histogram's flatness), f is decreased after M proposal-acceptance steps:

  
    
      
        f
        ←
        f
        
          /
        
        2
      
    
    {\displaystyle f\leftarrow f/2}
  
.
It was later shown that updating the f by constantly dividing by two can lead to saturation errors. A small modification to the Wang and Landau method to avoid this problem is to use the f factor proportional to 
  
    
      
        1
        
          /
        
        t
      
    
    {\displaystyle 1/t}
  
, where 
  
    
      
        t
      
    
    {\displaystyle t}
  
 is proportional to the number of steps of the simulation.

Test system
We want to obtain the DOS for the harmonic oscillator potential.

  
    
      
        E
        (
        x
        )
        =
        
          x
          
            2
          
        
        ,
        
      
    
    {\displaystyle E(x)=x^{2},\,}
  

The analytical DOS is given by,

  
    
      
        ρ
        (
        E
        )
        =
        ∫
        δ
        (
        E
        (
        x
        )
        −
        E
        )
        
        d
        x
        =
        ∫
        δ
        (
        
          x
          
            2
          
        
        −
        E
        )
        
        d
        x
        ,
      
    
    {\displaystyle \rho (E)=\int \delta (E(x)-E)\,dx=\int \delta (x^{2}-E)\,dx,}
  

by performing the last integral we obtain

  
    
      
        ρ
        (
        E
        )
        ∝
        
          
            {
            
              
                
                  
                    E
                    
                      −
                      1
                      
                        /
                      
                      2
                    
                  
                  ,
                  
                    for 
                  
                  x
                  ∈
                  
                    
                      R
                    
                    
                      1
                    
                  
                
              
              
                
                  
                    const
                  
                  ,
                  
                    for 
                  
                  x
                  ∈
                  
                    
                      R
                    
                    
                      2
                    
                  
                
              
              
                
                  
                    E
                    
                      1
                      
                        /
                      
                      2
                    
                  
                  ,
                  
                    for 
                  
                  x
                  ∈
                  
                    
                      R
                    
                    
                      3
                    
                  
                
              
            
            
          
        
      
    
    {\displaystyle \rho (E)\propto {\begin{cases}E^{-1/2},{\text{for }}x\in \mathbb {R} ^{1}\\{\text{const}},{\text{for }}x\in \mathbb {R} ^{2}\\E^{1/2},{\text{for }}x\in \mathbb {R} ^{3}\\\end{cases}}}
  

In general, the DOS for a multidimensional harmonic oscillator will be given by some power of E, the exponent will be a function of the dimension of the system.
Hence, we can use a simple harmonic oscillator potential to test the accuracy of Wang–Landau algorithm because we know already the analytic form of the density of states. Therefore, we compare the estimated density of states 
  
    
      
        
          
            
              ρ
              ^
            
          
        
        (
        E
        )
      
    
    {\displaystyle {\hat {\rho }}(E)}
  
 obtained by the Wang–Landau algorithm with 
  
    
      
        ρ
        (
        E
        )
      
    
    {\displaystyle \rho (E)}
  
.

Sample code
The following is a sample code of the Wang–Landau algorithm in Python, where we assume that a symmetric proposal distribution g is used:

  
    
      
        g
        (
        
          
            x
          
          ′
        
        →
        
          x
        
        )
        =
        g
        (
        
          x
        
        →
        
          
            x
          
          ′
        
        )
      
    
    {\displaystyle g({\boldsymbol {x}}'\rightarrow {\boldsymbol {x}})=g({\boldsymbol {x}}\rightarrow {\boldsymbol {x}}')}
  

The code considers a "system" which is the underlying system being studied.

Wang and Landau molecular dynamics: Statistical Temperature Molecular Dynamics (STMD)
Molecular dynamics (MD) is usually preferable to Monte Carlo (MC), so it is desirable to have a MD algorithm incorporating the basic WL idea for flat energy sampling. That algorithm is Statistical Temperature Molecular Dynamics (STMD), developed  by Jaegil Kim et al at Boston University.
An essential first step was made with the Statistical Temperature Monte Carlo (STMC) algorithm.  WLMC requires an extensive increase in the number of energy bins with system size, caused by working directly with the density of states. STMC is centered on an intensive quantity, the statistical temperature, 
  
    
      
        T
        (
        E
        )
        =
        1
        
          /
        
        (
        d
        S
        (
        E
        )
        
          /
        
        d
        E
        )
      
    
    {\displaystyle T(E)=1/(dS(E)/dE)}
  
, where E is the potential energy. When combined with the relation, 
  
    
      
        Ω
        (
        E
        )
        =
        
          e
          
            S
            (
            E
            )
          
        
      
    
    {\displaystyle \Omega (E)=e^{S(E)}}
  
, where we set 
  
    
      
        
          k
          
            B
          
        
        =
        1
      
    
    {\displaystyle k_{B}=1}
  
, the WL rule for updating the density of states gives  the rule for updating the discretized statistical temperature,

  
    
      
        
          
            
              
                T
                ~
              
            
          
          
            j
            ±
            1
          
          
            ′
          
        
        =
        
          α
          
            j
            ±
            1
          
        
        
          
            
              
                T
                ~
              
            
          
          
            j
            ±
            1
          
        
        ,
      
    
    {\displaystyle {\tilde {T}}_{j\pm 1}^{\prime }=\alpha _{j\pm 1}{\tilde {T}}_{j\pm 1},}
  

where 
  
    
      
        
          α
          
            j
            ±
            1
          
        
        =
        1
        
          /
        
        (
        1
        ∓
        δ
        f
        
          
            
              
                T
                ~
              
            
          
          
            j
            ±
            1
          
        
        )
        ,
        δ
        f
        =
        (
        l
        n
        f
        
          /
        
        2
        Δ
        E
        )
        ,
        Δ
        E
      
    
    {\displaystyle \alpha _{j\pm 1}=1/(1\mp \delta f{\tilde {T}}_{j\pm 1}),\delta f=(lnf/2\Delta E),\Delta E}
  
 is the energy bin size, and 
  
    
      
        
          
            
              T
              ~
            
          
        
      
    
    {\displaystyle {\tilde {T}}}
  
 denotes the running estimate. We define f as in, a factor >1 that multiplies the estimate of the DOS for the i'th energy bin when the system visits an energy in that bin.
The details are given in Ref. With an initial guess for 
  
    
      
        T
        (
        E
        )
      
    
    {\displaystyle T(E)}
  
 and the range restricted to lie between 
  
    
      
        
          T
          
            L
          
        
      
    
    {\displaystyle T_{L}}
  
 and 
  
    
      
        
          T
          
            U
          
        
      
    
    {\displaystyle T_{U}}
  
, the simulation proceeds as in WLMC, with significant numerical differences. An interpolation of 
  
    
      
        
          
            
              T
              ~
            
          
        
        (
        E
        )
      
    
    {\displaystyle {\tilde {T}}(E)}
  
 gives a continuum expression of the estimated 
  
    
      
        S
        (
        E
        )
      
    
    {\displaystyle S(E)}
  
 upon integration of its inverse, allowing the use of larger energy bins than in WL. Different values of 
  
    
      
        S
        (
        E
        )
      
    
    {\displaystyle S(E)}
  
 are available within the same energy bin when evaluating the acceptance probability. When histogram fluctuations are less than 20% of the mean, 
  
    
      
        f
      
    
    {\displaystyle f}
  
  is reduced according to 
  
    
      
        f
        →
        
          
            f
          
        
      
    
    {\displaystyle f\rightarrow {\sqrt {f}}}
  
.
STMC was compared with WL for the Ising model and the Lennard-Jones liquid. Upon increasing energy bin size, STMC gets the same results over a considerable range, while the performance of WL deteriorates rapidly. STMD can use smaller initial values of 
  
    
      
        
          f
          
            d
          
        
        =
        f
        −
        1
      
    
    {\displaystyle f_{d}=f-1}
  
 for more rapid convergence. In sum, STMC needs fewer steps to obtain the same quality of results.
Now consider the main result, STMD. It is based on the observation that in a standard MD simulation at temperature 
  
    
      
        
          T
          
            0
          
        
      
    
    {\displaystyle T_{0}}
  
 with forces derived from the potential energy 
  
    
      
        E
        (
        [
        x
        ]
        )
      
    
    {\displaystyle E([x])}
  
, where 
  
    
      
        [
        x
        ]
      
    
    {\displaystyle [x]}
  
 denotes all the positions, the sampling weight for a configuration is 
  
    
      
        
          e
          
            −
            E
            (
            [
            x
            ]
            )
            
              /
            
            
              T
              
                0
              
            
          
        
      
    
    {\displaystyle e^{-E([x])/T_{0}}}
  
. Furthermore, if the forces are derived from a function 
  
    
      
        W
        (
        E
        )
      
    
    {\displaystyle W(E)}
  
, the sampling weight is 
  
    
      
        
          e
          
            −
            W
            (
            E
            (
            [
            x
            ]
            )
            )
            
              /
            
            
              T
              
                0
              
            
          
        
      
    
    {\displaystyle e^{-W(E([x]))/T_{0}}}
  
.
For flat energy sampling, let the effective potential be 
  
    
      
        
          T
          
            0
          
        
        S
        (
        E
        )
      
    
    {\displaystyle T_{0}S(E)}
  
 - entropic molecular dynamics. Then the weight is 
  
    
      
        
          e
          
            −
            S
            (
            E
            )
          
        
      
    
    {\displaystyle e^{-S(E)}}
  
. Since the density of states is 
  
    
      
        
          e
          
            +
            S
            (
            E
            )
          
        
      
    
    {\displaystyle e^{+S(E)}}
  
, their product gives flat energy sampling.
The forces are calculated as 

  
    
      
        F
        =
        (
        −
        d
        
          /
        
        d
        x
        )
        
          T
          
            0
          
        
        S
        (
        E
        )
        =
        
          T
          
            0
          
        
        (
        d
        S
        
          /
        
        d
        E
        )
        (
        −
        d
        
          /
        
        d
        x
        )
        E
        (
        [
        x
        ]
        )
        =
        (
        
          T
          
            0
          
        
        
          /
        
        T
        (
        E
        )
        )
        
          F
          
            0
          
        
      
    
    {\displaystyle F=(-d/dx)T_{0}S(E)=T_{0}(dS/dE)(-d/dx)E([x])=(T_{0}/T(E))F^{0}}
  

where 
  
    
      
        
          F
          
            0
          
        
      
    
    {\displaystyle F^{0}}
  
 denotes the usual force derived from the potential energy. Scaling the usual forces by the factor 
  
    
      
        (
        
          T
          
            0
          
        
        
          /
        
        T
        (
        E
        )
        )
      
    
    {\displaystyle (T_{0}/T(E))}
  
 produces flat energy sampling. 
STMD starts with an ordinary MD algorithm at constant 
  
    
      
        
          T
          
            0
          
        
      
    
    {\displaystyle T_{0}}
  
 and V. The forces are scaled as indicated, and the statistical temperature is updated every time step, using the same procedure as in STMC. As the simulation converges to flat energy sampling, the running estimate 
  
    
      
        
          
            
              T
              ~
            
          
        
        (
        E
        )
      
    
    {\displaystyle {\tilde {T}}(E)}
  
 converges to the true 
  
    
      
        T
        (
        E
        )
      
    
    {\displaystyle T(E)}
  
. Technical details including steps to speed convergence are described in  and.
In STMD 
  
    
      
        
          T
          
            0
          
        
      
    
    {\displaystyle T_{0}}
  
 is called the kinetic temperature as it controls the velocities as usual, but does not enter the configurational sampling, which is unusual. Thus STMD can probe low energies with fast particles. Any canonical average can be calculated with reweighting, but the statistical temperature, 
  
    
      
        T
        (
        E
        )
      
    
    {\displaystyle T(E)}
  
, is immediately available with no additional analysis. It is extremely valuable for studying phase transitions. In finite nanosystems 
  
    
      
        T
        (
        E
        )
      
    
    {\displaystyle T(E)}
  
 has a feature corresponding to every “subphase transition”. For a sufficiently strong transition, an equal-area construction on an S-loop in 
  
    
      
        1
        
          /
        
        T
        (
        E
        )
      
    
    {\displaystyle 1/T(E)}
  
 gives the transition temperature.
STMD has been refined by the BU group, and applied to several systems by them and others.  It was recognized by D. Stelter that despite our emphasis on working with intensive quantities, 
  
    
      
        l
        n
        (
        f
        )
      
    
    {\displaystyle ln(f)}
  
 is extensive. However 
  
    
      
        δ
        f
        =
        (
        l
        n
        (
        f
        )
        
          /
        
        2
        Δ
        E
        )
      
    
    {\displaystyle \delta f=(ln(f)/2\Delta E)}
  
 is intensive, and the procedure 
  
    
      
        f
        →
        
          
            f
          
        
      
    
    {\displaystyle f\rightarrow {\sqrt {f}}}
  
 based on histogram flatness is  replaced by cutting 
  
    
      
        δ
        f
      
    
    {\displaystyle \delta f}
  
 in half every fixed number of time steps. This simple change makes STMD entirely intensive and substantially improves performance for large systems. Furthermore, the final value of the intensive 
  
    
      
        δ
        f
      
    
    {\displaystyle \delta f}
  
 is a constant that determines the magnitude of error in the converged 
  
    
      
        T
        (
        E
        )
      
    
    {\displaystyle T(E)}
  
, and is independent of system size. STMD is implemented in LAMMPS as fix stmd.
STMD is particularly useful for phase transitions. Equilibrium information is impossible to obtain with a canonical simulation, as supercooling or superheating is necessary to cause the transition. However an STMD run obtains flat energy sampling with a natural progression of heating and cooling, without getting trapped in the low energy or high energy state. Most recently it has been applied to the fluid/gel transition  in lipid-wrapped nanoparticles.
Replica exchange STMD  has also been presented by the BU group.


== References ==

## Related Articles

### Internal Links

- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [David P. Landau](https://en.wikipedia.org/wiki/David_P._Landau)
- [Density of states](https://en.wikipedia.org/wiki/Density_of_states)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Estimator](https://en.wikipedia.org/wiki/Estimator)
- [Harmonic oscillator](https://en.wikipedia.org/wiki/Harmonic_oscillator)
- [Metadynamics](https://en.wikipedia.org/wiki/Metadynamics)
- [Metropolis–Hastings algorithm](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm)
- [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- [Multicanonical ensemble](https://en.wikipedia.org/wiki/Multicanonical_ensemble)
- [PubMed Central](https://en.wikipedia.org/wiki/PubMed_Central)
- [PubMed](https://en.wikipedia.org/wiki/PubMed)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Random walk](https://en.wikipedia.org/wiki/Random_walk)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Stochastic process](https://en.wikipedia.org/wiki/Stochastic_process)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:47:12.093344+00:00_