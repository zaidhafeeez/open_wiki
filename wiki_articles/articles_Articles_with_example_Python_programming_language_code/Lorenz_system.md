# Lorenz system

## Article Metadata

- **Last Updated:** 2024-12-15T04:33:58.599615+00:00
- **Original Article:** [Lorenz system](https://en.wikipedia.org/wiki/Lorenz_system)
- **Language:** en
- **Page ID:** 5642583

## Summary

The Lorenz system is a system of ordinary differential equations first studied by mathematician and meteorologist Edward Lorenz. It is notable for having chaotic solutions for certain parameter values and initial conditions. In particular, the Lorenz attractor is a set of chaotic solutions of the Lorenz system. The term "butterfly effect" in popular media may stem from the real-world implications of the Lorenz attractor, namely that tiny changes in initial conditions evolve to completely differe

## Categories

- Category:All articles that are too technical
- Category:All articles with unsourced statements
- Category:Articles containing video clips
- Category:Articles with example Julia code
- Category:Articles with example MATLAB/Octave code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from June 2017
- Category:Chaotic maps
- Category:Commons category link is on Wikidata
- Category:Short description is different from Wikidata
- Category:Webarchive template wayback links
- Category:Wikipedia articles that are too technical from December 2023

## Table of Contents

- Overview
- Analysis
- Connection to tent map
- A Generalized Lorenz System
- Simulations
- Applications
- Gallery
- See also
- Notes
- References
- Further reading
- External links

## Content

The Lorenz system is a system of ordinary differential equations first studied by mathematician and meteorologist Edward Lorenz. It is notable for having chaotic solutions for certain parameter values and initial conditions. In particular, the Lorenz attractor is a set of chaotic solutions of the Lorenz system. The term "butterfly effect" in popular media may stem from the real-world implications of the Lorenz attractor, namely that tiny changes in initial conditions evolve to completely different trajectories. This underscores that chaotic systems can be completely deterministic and yet still be inherently impractical or even impossible to predict over longer periods of time. For example, even the small flap of a butterfly's wings could set the earth's atmosphere on a vastly different trajectory, in which for example a hurricane occurs where it otherwise would have not (see Saddle points). The shape of the Lorenz attractor itself, when plotted in phase space, may also be seen to resemble a butterfly.

Overview
In 1963, Edward Lorenz, with the help of Ellen Fetter who was responsible for the numerical simulations and figures, and Margaret Hamilton who helped in the initial, numerical computations leading up to the findings of the Lorenz model,  developed a simplified mathematical model for atmospheric convection. The model is a system of three ordinary differential equations now known as the Lorenz equations:

  
    
      
        
          
            
              
                
                  
                    
                      
                        d
                      
                      x
                    
                    
                      
                        d
                      
                      t
                    
                  
                
              
              
                
                =
                σ
                (
                y
                −
                x
                )
                ,
              
            
            
              
                
                  
                    
                      
                        d
                      
                      y
                    
                    
                      
                        d
                      
                      t
                    
                  
                
              
              
                
                =
                x
                (
                ρ
                −
                z
                )
                −
                y
                ,
              
            
            
              
                
                  
                    
                      
                        d
                      
                      z
                    
                    
                      
                        d
                      
                      t
                    
                  
                
              
              
                
                =
                x
                y
                −
                β
                z
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\frac {\mathrm {d} x}{\mathrm {d} t}}&=\sigma (y-x),\\[6pt]{\frac {\mathrm {d} y}{\mathrm {d} t}}&=x(\rho -z)-y,\\[6pt]{\frac {\mathrm {d} z}{\mathrm {d} t}}&=xy-\beta z.\end{aligned}}}
  

The equations relate the properties of a two-dimensional fluid layer uniformly warmed from below and cooled from above. In particular, the equations describe the rate of change of three quantities with respect to time: x is proportional to the rate of convection, y to the horizontal temperature variation, and z to the vertical temperature variation. The constants σ, ρ, and β are system parameters proportional to the Prandtl number, Rayleigh number, and certain physical dimensions of the layer itself.
The Lorenz equations can arise in simplified models for lasers, dynamos, thermosyphons, brushless DC motors, electric circuits, chemical reactions and forward osmosis. Interestingly, the same Lorenz equations were also derived in 1963 by Sauermann and Haken  for a single-mode laser. In 1975, Haken realized  that their equations derived in 1963 were mathematically equivalent to the original Lorenz equations. Haken's paper  thus started a new field called laser chaos or optical chaos. The Lorenz equations are often called Lorenz-Haken equations in optical literature. Later on, it was also shown the complex version of Lorenz equations also had laser equivalent ones.     
The Lorenz equations are also the governing equations in Fourier space for the Malkus waterwheel. The Malkus waterwheel exhibits chaotic motion where instead of spinning in one direction at a constant speed, its rotation will speed up, slow down, stop, change directions, and oscillate back and forth between combinations of such behaviors in an unpredictable manner.
From a technical standpoint, the Lorenz system is nonlinear, aperiodic, three-dimensional and deterministic. The Lorenz equations have been the subject of hundreds of research articles, and at least one book-length study.

Analysis
One normally assumes that the parameters σ, ρ, and β are positive. Lorenz used the values σ = 10, β = ⁠8/3⁠ and ρ = 28. The system exhibits chaotic behavior for these (and nearby) values.
If ρ < 1 then there is only one equilibrium point, which is at the origin. This point corresponds to no convection. All orbits converge to the origin, which is a global attractor, when ρ < 1.
A pitchfork bifurcation occurs at ρ = 1, and for ρ > 1 two additional critical points appear at

  
    
      
        
          (
          
            
              
                β
                (
                ρ
                −
                1
                )
              
            
            ,
            
              
                β
                (
                ρ
                −
                1
                )
              
            
            ,
            ρ
            −
            1
          
          )
        
        
        
          and
        
        
        
          (
          
            −
            
              
                β
                (
                ρ
                −
                1
                )
              
            
            ,
            −
            
              
                β
                (
                ρ
                −
                1
                )
              
            
            ,
            ρ
            −
            1
          
          )
        
        .
      
    
    {\displaystyle \left({\sqrt {\beta (\rho -1)}},{\sqrt {\beta (\rho -1)}},\rho -1\right)\quad {\text{and}}\quad \left(-{\sqrt {\beta (\rho -1)}},-{\sqrt {\beta (\rho -1)}},\rho -1\right).}
  
 
These correspond to steady convection. This pair of equilibrium points is stable only if 

  
    
      
        ρ
        <
        σ
        
          
            
              σ
              +
              β
              +
              3
            
            
              σ
              −
              β
              −
              1
            
          
        
        ,
      
    
    {\displaystyle \rho <\sigma {\frac {\sigma +\beta +3}{\sigma -\beta -1}},}
  

which can hold only for positive ρ if σ > β + 1. At the critical value, both equilibrium points lose stability through a subcritical Hopf bifurcation.
When ρ = 28, σ = 10, and β = ⁠8/3⁠, the Lorenz system has chaotic solutions (but not all solutions are chaotic). Almost all initial points will tend to an invariant set – the Lorenz attractor – a strange attractor, a fractal, and a self-excited attractor with respect to all three equilibria. Its Hausdorff dimension is estimated from above by the Lyapunov dimension (Kaplan-Yorke dimension) as 2.06±0.01, and the correlation dimension is estimated to be 2.05±0.01. The exact Lyapunov dimension formula of the global attractor can be found analytically under classical restrictions on the parameters:

  
    
      
        3
        −
        
          
            
              2
              (
              σ
              +
              β
              +
              1
              )
            
            
              σ
              +
              1
              +
              
                
                  
                    
                      (
                      
                        σ
                        −
                        1
                      
                      )
                    
                    
                      2
                    
                  
                  +
                  4
                  σ
                  ρ
                
              
            
          
        
      
    
    {\displaystyle 3-{\frac {2(\sigma +\beta +1)}{\sigma +1+{\sqrt {\left(\sigma -1\right)^{2}+4\sigma \rho }}}}}
  

The Lorenz attractor is difficult to analyze, but the action of the differential equation on the attractor is described by a fairly simple geometric model. Proving that this is indeed the case is the fourteenth problem on the list of Smale's problems. This problem was the first one to be resolved, by Warwick Tucker in 2002.
For other values of ρ, the system displays knotted periodic orbits. For example, with ρ = 99.96 it becomes a T(3,2) torus knot.

Connection to tent map
In Figure 4 of his paper, Lorenz plotted the relative maximum value in the z direction achieved by the system against the previous relative maximum in the z direction. This procedure later became known as a Lorenz map (not to be confused with a Poincaré plot, which plots the intersections of a trajectory with a prescribed surface). The resulting plot has a shape very similar to the tent map. Lorenz also found that when the maximum z value is above a certain cut-off, the system will switch to the next lobe. Combining this with the chaos known to be exhibited by the tent map, he showed that the system switches between the two lobes chaotically.

A Generalized Lorenz System
Over the past several years, a series of papers regarding high-dimensional Lorenz models have yielded a generalized Lorenz model, which can be simplified into the classical Lorenz model  for three state variables or the following five-dimensional Lorenz model for five state variables:

  
    
      
        
          
            
              
                
                  
                    
                      
                        d
                      
                      x
                    
                    
                      
                        d
                      
                      t
                    
                  
                
              
              
                
                =
                σ
                (
                y
                −
                x
                )
                ,
              
            
            
              
                
                  
                    
                      
                        d
                      
                      y
                    
                    
                      
                        d
                      
                      t
                    
                  
                
              
              
                
                =
                x
                (
                ρ
                −
                z
                )
                −
                y
                ,
              
            
            
              
                
                  
                    
                      
                        d
                      
                      z
                    
                    
                      
                        d
                      
                      t
                    
                  
                
              
              
                
                =
                x
                y
                −
                x
                
                  y
                  
                    1
                  
                
                −
                β
                z
                ,
              
            
            
              
                
                  
                    
                      
                        d
                      
                      
                        y
                        
                          1
                        
                      
                    
                    
                      
                        d
                      
                      t
                    
                  
                
              
              
                
                =
                x
                z
                −
                2
                x
                
                  z
                  
                    1
                  
                
                −
                
                  d
                  
                    0
                  
                
                
                  y
                  
                    1
                  
                
                ,
              
            
            
              
                
                  
                    
                      
                        d
                      
                      
                        z
                        
                          1
                        
                      
                    
                    
                      
                        d
                      
                      t
                    
                  
                
              
              
                
                =
                2
                x
                
                  y
                  
                    1
                  
                
                −
                4
                β
                
                  z
                  
                    1
                  
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\frac {\mathrm {d} x}{\mathrm {d} t}}&=\sigma (y-x),\\[6pt]{\frac {\mathrm {d} y}{\mathrm {d} t}}&=x(\rho -z)-y,\\[6pt]{\frac {\mathrm {d} z}{\mathrm {d} t}}&=xy-xy_{1}-\beta z,\\[6pt]{\frac {\mathrm {d} y_{1}}{\mathrm {d} t}}&=xz-2xz_{1}-d_{0}y_{1},\\[6pt]{\frac {\mathrm {d} z_{1}}{\mathrm {d} t}}&=2xy_{1}-4\beta z_{1}.\end{aligned}}}
  

A choice of the parameter 
  
    
      
        
          d
          
            0
          
        
        =
        
          
            
              19
              3
            
          
        
      
    
    {\textstyle d_{0}={\dfrac {19}{3}}}
  
 has been applied to be consistent with the choice of the other parameters. See details in.

Simulations
Julia simulation
Maple simulation
Maxima simulation
MATLAB simulation
Mathematica simulation
Standard way:

Less verbose:

Python simulation
R simulation
Applications
Model for atmospheric convection
As shown in Lorenz's original paper, the Lorenz system is a reduced version of a larger system studied earlier by Barry Saltzman. The Lorenz equations are derived from the Oberbeck–Boussinesq approximation to the equations describing fluid circulation in a shallow layer of fluid, heated uniformly from below and cooled uniformly from above. This fluid circulation is known as Rayleigh–Bénard convection. The fluid is assumed to circulate in two dimensions (vertical and horizontal) with periodic rectangular boundary conditions.
The partial differential equations modeling the system's stream function and temperature are subjected to a spectral Galerkin approximation: the hydrodynamic fields are expanded in Fourier series, which are then severely truncated to a single term for the stream function and two terms for the temperature. This reduces the model equations to a set of three coupled, nonlinear ordinary differential equations. A detailed derivation may be found, for example, in nonlinear dynamics texts from Hilborn (2000), Appendix C;  Bergé, Pomeau & Vidal (1984), Appendix D; or Shen (2016), Supplementary Materials.

Model for the nature of chaos and order in the atmosphere
The scientific community accepts that the chaotic features found in low-dimensional Lorenz models could represent features of the Earth's atmosphere (), yielding the statement of “weather is chaotic.” By comparison, based on the concept of attractor coexistence within the generalized Lorenz model and the original Lorenz model (), Shen and his co-authors  proposed a revised view that “weather possesses both chaos and order with distinct predictability”. The revised view,  which is a build-up of the conventional view, is used to suggest that “the chaotic and regular features found in theoretical Lorenz models could better represent features of the Earth's atmosphere”.

Resolution of Smale's 14th problem
Smale's 14th problem says, 'Do the properties of the Lorenz attractor exhibit that of a strange attractor?'. The problem was answered affirmatively by Warwick Tucker in 2002. To prove this result, Tucker used rigorous numerics methods like interval arithmetic and normal forms. First, Tucker defined a cross section 
  
    
      
        Σ
        ⊂
        {
        
          x
          
            3
          
        
        =
        r
        −
        1
        }
      
    
    {\displaystyle \Sigma \subset \{x_{3}=r-1\}}
  
 that is cut transversely by the flow trajectories. From this, one can define the first-return map 
  
    
      
        P
      
    
    {\displaystyle P}
  
, which assigns to each 
  
    
      
        x
        ∈
        Σ
      
    
    {\displaystyle x\in \Sigma }
  
 the point 
  
    
      
        P
        (
        x
        )
      
    
    {\displaystyle P(x)}
  
 where the trajectory of 
  
    
      
        x
      
    
    {\displaystyle x}
  
 first intersects 
  
    
      
        Σ
      
    
    {\displaystyle \Sigma }
  
.
Then the proof is split in three main points that are proved and imply the existence of a strange attractor. The three points are:

There exists a region 
  
    
      
        N
        ⊂
        Σ
      
    
    {\displaystyle N\subset \Sigma }
  
 invariant under the first-return map, meaning 
  
    
      
        P
        (
        N
        )
        ⊂
        N
      
    
    {\displaystyle P(N)\subset N}
  
.
The return map admits a forward invariant cone field.
Vectors inside this invariant cone field are uniformly expanded by the derivative 
  
    
      
        D
        P
      
    
    {\displaystyle DP}
  
 of the return map.
To prove the first point, we notice that the cross section 
  
    
      
        Σ
      
    
    {\displaystyle \Sigma }
  
 is cut by two arcs formed by 
  
    
      
        P
        (
        Σ
        )
      
    
    {\displaystyle P(\Sigma )}
  
. Tucker covers the location of these two arcs by small rectangles 
  
    
      
        
          R
          
            i
          
        
      
    
    {\displaystyle R_{i}}
  
, the union of these rectangles gives 
  
    
      
        N
      
    
    {\displaystyle N}
  
. Now, the goal is to prove that for all points in 
  
    
      
        N
      
    
    {\displaystyle N}
  
, the flow will bring back the points in 
  
    
      
        Σ
      
    
    {\displaystyle \Sigma }
  
, in 
  
    
      
        N
      
    
    {\displaystyle N}
  
. To do that, we take a plan 
  
    
      
        
          Σ
          ′
        
      
    
    {\displaystyle \Sigma '}
  
 below 
  
    
      
        Σ
      
    
    {\displaystyle \Sigma }
  
 at a distance 
  
    
      
        h
      
    
    {\displaystyle h}
  
 small, then by taking the center 
  
    
      
        
          c
          
            i
          
        
      
    
    {\displaystyle c_{i}}
  
 of 
  
    
      
        
          R
          
            i
          
        
      
    
    {\displaystyle R_{i}}
  
 and using Euler integration method, one can estimate where the flow will bring 
  
    
      
        
          c
          
            i
          
        
      
    
    {\displaystyle c_{i}}
  
 in 
  
    
      
        
          Σ
          ′
        
      
    
    {\displaystyle \Sigma '}
  
 which gives us a new point 
  
    
      
        
          c
          
            i
          
          ′
        
      
    
    {\displaystyle c_{i}'}
  
. Then, one can estimate where the points in 
  
    
      
        Σ
      
    
    {\displaystyle \Sigma }
  
 will be mapped in 
  
    
      
        
          Σ
          ′
        
      
    
    {\displaystyle \Sigma '}
  
 using Taylor expansion, this gives us a new rectangle 
  
    
      
        
          R
          
            i
          
          ′
        
      
    
    {\displaystyle R_{i}'}
  
 centered on 
  
    
      
        
          c
          
            i
          
        
      
    
    {\displaystyle c_{i}}
  
. Thus we know that all points in 
  
    
      
        
          R
          
            i
          
        
      
    
    {\displaystyle R_{i}}
  
 will be mapped in 
  
    
      
        
          R
          
            i
          
          ′
        
      
    
    {\displaystyle R_{i}'}
  
. The goal is to do this method recursively until the flow comes back to 
  
    
      
        Σ
      
    
    {\displaystyle \Sigma }
  
 and we obtain a rectangle 
  
    
      
        R
        
          f
          
            i
          
        
      
    
    {\displaystyle Rf_{i}}
  
 in 
  
    
      
        Σ
      
    
    {\displaystyle \Sigma }
  
 such that we know that 
  
    
      
        P
        (
        
          R
          
            i
          
        
        )
        ⊂
        R
        
          f
          
            i
          
        
      
    
    {\displaystyle P(R_{i})\subset Rf_{i}}
  
. The problem is that our estimation may become imprecise after several iterations, thus what Tucker does is to split 
  
    
      
        
          R
          
            i
          
          ′
        
      
    
    {\displaystyle R_{i}'}
  
 into smaller rectangles 
  
    
      
        
          R
          
            i
            ,
            j
          
        
      
    
    {\displaystyle R_{i,j}}
  
 and then apply the process recursively.
Another problem is that as we are applying this algorithm, the flow becomes more 'horizontal', leading to a dramatic increase in imprecision. To prevent this, the algorithm changes the orientation of the cross sections, becoming either horizontal or vertical.

Gallery
See also
Eden's conjecture on the Lyapunov dimension
Lorenz 96 model
List of chaotic maps
Takens' theorem

Notes
References
Bergé, Pierre; Pomeau, Yves; Vidal, Christian (1984). Order within Chaos: Towards a Deterministic Approach to Turbulence. New York: John Wiley & Sons. ISBN 978-0-471-84967-4.
Cuomo, Kevin M.; Oppenheim, Alan V. (1993). "Circuit implementation of synchronized chaos with applications to communications". Physical Review Letters. 71 (1): 65–68. Bibcode:1993PhRvL..71...65C. doi:10.1103/PhysRevLett.71.65. ISSN 0031-9007. PMID 10054374.
Gorman, M.; Widmann, P.J.; Robbins, K.A. (1986). "Nonlinear dynamics of a convection loop: A quantitative comparison of experiment with theory". Physica D. 19 (2): 255–267. Bibcode:1986PhyD...19..255G. doi:10.1016/0167-2789(86)90022-9.
Grassberger, P.; Procaccia, I. (1983). "Measuring the strangeness of strange attractors". Physica D. 9 (1–2): 189–208. Bibcode:1983PhyD....9..189G. doi:10.1016/0167-2789(83)90298-1.
Haken, H. (1975). "Analogy between higher instabilities in fluids and lasers". Physics Letters A. 53 (1): 77–78. Bibcode:1975PhLA...53...77H. doi:10.1016/0375-9601(75)90353-9.
Sauermann, H.; Haken, H. (1963). "Nonlinear Interaction of Laser Modes". Z. Phys. 173: 261–275.
Ning, C.Z.; Haken, H. (1990). "Detuned lasers and the complex Lorenz equations: Subcritical and supercritical Hopf bifurcations". Phys.Rev. A. 41: 3826–3837.
Hemati, N. (1994). "Strange attractors in brushless DC motors". IEEE Transactions on Circuits and Systems I: Fundamental Theory and Applications. 41 (1): 40–45. doi:10.1109/81.260218. ISSN 1057-7122.
Hilborn, Robert C. (2000). Chaos and Nonlinear Dynamics: An Introduction for Scientists and Engineers (second ed.). Oxford University Press. ISBN 978-0-19-850723-9.
Hirsch, Morris W.; Smale, Stephen; Devaney, Robert (2003). Differential Equations, Dynamical Systems, & An Introduction to Chaos (Second ed.). Boston, MA: Academic Press. ISBN 978-0-12-349703-1.
Knobloch, Edgar (1981). "Chaos in the segmented disc dynamo". Physics Letters A. 82 (9): 439–440. Bibcode:1981PhLA...82..439K. doi:10.1016/0375-9601(81)90274-7.
Kolář, Miroslav; Gumbs, Godfrey (1992). "Theory for the experimental observation of chaos in a rotating waterwheel". Physical Review A. 45 (2): 626–637. Bibcode:1992PhRvA..45..626K. doi:10.1103/PhysRevA.45.626. PMID 9907027.
Leonov, G.A.; Kuznetsov, N.V.; Korzhemanova, N.A.; Kusakin, D.V. (2016). "Lyapunov dimension formula for the global attractor of the Lorenz system". Communications in Nonlinear Science and Numerical Simulation. 41: 84–103. arXiv:1508.07498. Bibcode:2016CNSNS..41...84L. doi:10.1016/j.cnsns.2016.04.032. S2CID 119614076.
Lorenz, Edward Norton (1963). "Deterministic nonperiodic flow". Journal of the Atmospheric Sciences. 20 (2): 130–141. Bibcode:1963JAtS...20..130L. doi:10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2.
Mishra, Aashwin; Sanghi, Sanjeev (2006). "A study of the asymmetric Malkus waterwheel: The biased Lorenz equations". Chaos: An Interdisciplinary Journal of Nonlinear Science. 16 (1): 013114. Bibcode:2006Chaos..16a3114M. doi:10.1063/1.2154792. PMID 16599745.
Pchelintsev, A.N. (2014). "Numerical and Physical Modeling of the Dynamics of the Lorenz System". Numerical Analysis and Applications. 7 (2): 159–167. doi:10.1134/S1995423914020098. S2CID 123023929.
Poland, Douglas (1993). "Cooperative catalysis and chemical chaos: a chemical model for the Lorenz equations". Physica D. 65 (1): 86–99. Bibcode:1993PhyD...65...86P. doi:10.1016/0167-2789(93)90006-M.
Saltzman, Barry (1962). "Finite Amplitude Free Convection as an Initial Value Problem—I". Journal of the Atmospheric Sciences. 19 (4): 329–341. Bibcode:1962JAtS...19..329S. doi:10.1175/1520-0469(1962)019<0329:FAFCAA>2.0.CO;2.
Shen, B.-W. (2015-12-21). "Nonlinear feedback in a six-dimensional Lorenz model: impact of an additional heating term". Nonlinear Processes in Geophysics. 22 (6): 749–764. doi:10.5194/npg-22-749-2015. ISSN 1607-7946.
Sparrow, Colin (1982). The Lorenz Equations: Bifurcations, Chaos, and Strange Attractors. Springer.
Tucker, Warwick (2002). "A Rigorous ODE Solver and Smale's 14th Problem" (PDF). Foundations of Computational Mathematics. 2 (1): 53–117. CiteSeerX 10.1.1.545.3996. doi:10.1007/s002080010018. S2CID 353254.
Tzenov, Stephan (2014). "Strange Attractors Characterizing the Osmotic Instability". arXiv:1406.0979v1 [physics.flu-dyn].
Viana, Marcelo (2000). "What's new on Lorenz strange attractors?". The Mathematical Intelligencer. 22 (3): 6–19. doi:10.1007/BF03025276. S2CID 121427433.
Lorenz, Edward N. (1960). "The statistical prediction of solutions of dynamic equations" (PDF). Symposium on Numerical Weather Prediction in Tokyo. Archived from the original (PDF) on 2019-05-23. Retrieved 2020-09-16.

Further reading
G.A. Leonov & N.V. Kuznetsov (2015). "On differences and similarities in the analysis of Lorenz, Chen, and Lu systems". Applied Mathematics and Computation. 256: 334–343. arXiv:1409.8649. doi:10.1016/j.amc.2014.12.132.
Pchelintsev, A.N. (2022). "On a high-precision method for studying attractors of dynamical systems and systems of explosive type". Mathematics. 10 (8): 1207. arXiv:2206.08195. doi:10.3390/math10081207.

External links

"Lorenz attractor", Encyclopedia of Mathematics, EMS Press, 2001 [1994]
Weisstein, Eric W. "Lorenz attractor". MathWorld.
Lorenz attractor by Rob Morris, Wolfram Demonstrations Project.
Lorenz equation Archived 2009-06-07 at the Wayback Machine on planetmath.org
Synchronized Chaos and Private Communications, with Kevin Cuomo. The implementation of Lorenz attractor in an electronic circuit.
Lorenz attractor interactive animation (you need the Adobe Shockwave plugin)
3D Attractors: Mac program to visualize and explore the Lorenz attractor in 3 dimensions
Lorenz Attractor implemented in analog electronic
Lorenz Attractor interactive animation (implemented in Ada with GTK+. Sources & executable)
Interactive web based Lorenz Attractor made with Iodide

## Related Articles

### Internal Links

- [Academic Press](https://en.wikipedia.org/wiki/Academic_Press)
- [Alan V. Oppenheim](https://en.wikipedia.org/wiki/Alan_V._Oppenheim)
- [Aleksandr Lyapunov](https://en.wikipedia.org/wiki/Aleksandr_Lyapunov)
- [Amie Wilkinson](https://en.wikipedia.org/wiki/Amie_Wilkinson)
- [Anosov diffeomorphism](https://en.wikipedia.org/wiki/Anosov_diffeomorphism)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Arnold's cat map](https://en.wikipedia.org/wiki/Arnold%27s_cat_map)
- [Arnold tongue](https://en.wikipedia.org/wiki/Arnold_tongue)
- [Atmospheric convection](https://en.wikipedia.org/wiki/Atmospheric_convection)
- [Attractor](https://en.wikipedia.org/wiki/Attractor)
- [Audrey Terras](https://en.wikipedia.org/wiki/Audrey_Terras)
- [Axiom A](https://en.wikipedia.org/wiki/Axiom_A)
- [Baker's map](https://en.wikipedia.org/wiki/Baker%27s_map)
- [Benoit Mandelbrot](https://en.wikipedia.org/wiki/Benoit_Mandelbrot)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Bifurcation diagram](https://en.wikipedia.org/wiki/Bifurcation_diagram)
- [Bifurcation theory](https://en.wikipedia.org/wiki/Bifurcation_theory)
- [Boussinesq approximation (buoyancy)](https://en.wikipedia.org/wiki/Boussinesq_approximation_(buoyancy))
- [Minkowski–Bouligand dimension](https://en.wikipedia.org/wiki/Minkowski%E2%80%93Bouligand_dimension)
- [Brosl Hasslacher](https://en.wikipedia.org/wiki/Brosl_Hasslacher)
- [Bryna Kra](https://en.wikipedia.org/wiki/Bryna_Kra)
- [Butterfly](https://en.wikipedia.org/wiki/Butterfly)
- [Butterfly effect](https://en.wikipedia.org/wiki/Butterfly_effect)
- [Caroline Series](https://en.wikipedia.org/wiki/Caroline_Series)
- [Celso Grebogi](https://en.wikipedia.org/wiki/Celso_Grebogi)
- [Chaos theory](https://en.wikipedia.org/wiki/Chaos_theory)
- [Chemical reaction](https://en.wikipedia.org/wiki/Chemical_reaction)
- [Chen Guanrong](https://en.wikipedia.org/wiki/Chen_Guanrong)
- [Chua's circuit](https://en.wikipedia.org/wiki/Chua%27s_circuit)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Complex quadratic polynomial](https://en.wikipedia.org/wiki/Complex_quadratic_polynomial)
- [Complexity](https://en.wikipedia.org/wiki/Complexity)
- [Conservative system](https://en.wikipedia.org/wiki/Conservative_system)
- [Control of chaos](https://en.wikipedia.org/wiki/Control_of_chaos)
- [Correlation dimension](https://en.wikipedia.org/wiki/Correlation_dimension)
- [Coupled map lattice](https://en.wikipedia.org/wiki/Coupled_map_lattice)
- [DC motor](https://en.wikipedia.org/wiki/DC_motor)
- [David Ruelle](https://en.wikipedia.org/wiki/David_Ruelle)
- [Determinism](https://en.wikipedia.org/wiki/Determinism)
- [Deterministic system](https://en.wikipedia.org/wiki/Deterministic_system)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Double pendulum](https://en.wikipedia.org/wiki/Double_pendulum)
- [Multiscroll attractor](https://en.wikipedia.org/wiki/Multiscroll_attractor)
- [Duffing equation](https://en.wikipedia.org/wiki/Duffing_equation)
- [Duffing map](https://en.wikipedia.org/wiki/Duffing_map)
- [Dyadic transformation](https://en.wikipedia.org/wiki/Dyadic_transformation)
- [Dynamical billiards](https://en.wikipedia.org/wiki/Dynamical_billiards)
- [Dynamical system](https://en.wikipedia.org/wiki/Dynamical_system)
- [Eden's conjecture](https://en.wikipedia.org/wiki/Eden%27s_conjecture)
- [Edge of chaos](https://en.wikipedia.org/wiki/Edge_of_chaos)
- [Edward Norton Lorenz](https://en.wikipedia.org/wiki/Edward_Norton_Lorenz)
- [Edward Norton Lorenz](https://en.wikipedia.org/wiki/Edward_Norton_Lorenz)
- [Edward Ott](https://en.wikipedia.org/wiki/Edward_Ott)
- [Elastic pendulum](https://en.wikipedia.org/wiki/Elastic_pendulum)
- [Electrical network](https://en.wikipedia.org/wiki/Electrical_network)
- [Electric generator](https://en.wikipedia.org/wiki/Electric_generator)
- [Ellen Fetter](https://en.wikipedia.org/wiki/Ellen_Fetter)
- [Encyclopedia of Mathematics](https://en.wikipedia.org/wiki/Encyclopedia_of_Mathematics)
- [Ergodic theory](https://en.wikipedia.org/wiki/Ergodic_theory)
- [Ergodicity](https://en.wikipedia.org/wiki/Ergodicity)
- [Eric W. Weisstein](https://en.wikipedia.org/wiki/Eric_W._Weisstein)
- [European Mathematical Society](https://en.wikipedia.org/wiki/European_Mathematical_Society)
- [Exponential map (discrete dynamical systems)](https://en.wikipedia.org/wiki/Exponential_map_(discrete_dynamical_systems))
- [False nearest neighbor algorithm](https://en.wikipedia.org/wiki/False_nearest_neighbor_algorithm)
- [Fermi–Pasta–Ulam–Tsingou problem](https://en.wikipedia.org/wiki/Fermi%E2%80%93Pasta%E2%80%93Ulam%E2%80%93Tsingou_problem)
- [Floris Takens](https://en.wikipedia.org/wiki/Floris_Takens)
- [Forward osmosis](https://en.wikipedia.org/wiki/Forward_osmosis)
- [Fractal](https://en.wikipedia.org/wiki/Fractal)
- [Galerkin method](https://en.wikipedia.org/wiki/Galerkin_method)
- [Gauss iterated map](https://en.wikipedia.org/wiki/Gauss_iterated_map)
- [Gingerbreadman map](https://en.wikipedia.org/wiki/Gingerbreadman_map)
- [Hausdorff dimension](https://en.wikipedia.org/wiki/Hausdorff_dimension)
- [Hee Oh](https://en.wikipedia.org/wiki/Hee_Oh)
- [Henri Poincaré](https://en.wikipedia.org/wiki/Henri_Poincar%C3%A9)
- [Hidden attractor](https://en.wikipedia.org/wiki/Hidden_attractor)
- [Hopf bifurcation](https://en.wikipedia.org/wiki/Hopf_bifurcation)
- [Horseshoe map](https://en.wikipedia.org/wiki/Horseshoe_map)
- [Tropical cyclone](https://en.wikipedia.org/wiki/Tropical_cyclone)
- [Hénon map](https://en.wikipedia.org/wiki/H%C3%A9non_map)
- [Hénon–Heiles system](https://en.wikipedia.org/wiki/H%C3%A9non%E2%80%93Heiles_system)
- [Institute of Electrical and Electronics Engineers](https://en.wikipedia.org/wiki/Institute_of_Electrical_and_Electronics_Engineers)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Ikeda map](https://en.wikipedia.org/wiki/Ikeda_map)
- [Initial condition](https://en.wikipedia.org/wiki/Initial_condition)
- [Interval arithmetic](https://en.wikipedia.org/wiki/Interval_arithmetic)
- [Interval exchange transformation](https://en.wikipedia.org/wiki/Interval_exchange_transformation)
- [Invariant measure](https://en.wikipedia.org/wiki/Invariant_measure)
- [Irrational rotation](https://en.wikipedia.org/wiki/Irrational_rotation)
- [Itamar Procaccia](https://en.wikipedia.org/wiki/Itamar_Procaccia)
- [James A. Yorke](https://en.wikipedia.org/wiki/James_A._Yorke)
- [Wiley (publisher)](https://en.wikipedia.org/wiki/Wiley_(publisher))
- [Kaplan–Yorke map](https://en.wikipedia.org/wiki/Kaplan%E2%80%93Yorke_map)
- [Kicked rotator](https://en.wikipedia.org/wiki/Kicked_rotator)
- [Krylov–Bogolyubov theorem](https://en.wikipedia.org/wiki/Krylov%E2%80%93Bogolyubov_theorem)
- [Lai-Sang Young](https://en.wikipedia.org/wiki/Lai-Sang_Young)
- [Langton's ant](https://en.wikipedia.org/wiki/Langton%27s_ant)
- [Laser](https://en.wikipedia.org/wiki/Laser)
- [Leon O. Chua](https://en.wikipedia.org/wiki/Leon_O._Chua)
- [Limit set](https://en.wikipedia.org/wiki/Limit_set)
- [Liouville's theorem (Hamiltonian)](https://en.wikipedia.org/wiki/Liouville%27s_theorem_(Hamiltonian))
- [List of chaotic maps](https://en.wikipedia.org/wiki/List_of_chaotic_maps)
- [Logistic map](https://en.wikipedia.org/wiki/Logistic_map)
- [Cauchy distribution](https://en.wikipedia.org/wiki/Cauchy_distribution)
- [Lorenz 96 model](https://en.wikipedia.org/wiki/Lorenz_96_model)
- [Lorenz curve](https://en.wikipedia.org/wiki/Lorenz_curve)
- [Lotka–Volterra equations](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations)
- [Lyapunov dimension](https://en.wikipedia.org/wiki/Lyapunov_dimension)
- [Lyapunov exponent](https://en.wikipedia.org/wiki/Lyapunov_exponent)
- [Lyapunov stability](https://en.wikipedia.org/wiki/Lyapunov_stability)
- [Mackey–Glass equations](https://en.wikipedia.org/wiki/Mackey%E2%80%93Glass_equations)
- [Malkus waterwheel](https://en.wikipedia.org/wiki/Malkus_waterwheel)
- [Marcelo Viana](https://en.wikipedia.org/wiki/Marcelo_Viana)
- [Margaret Hamilton (software engineer)](https://en.wikipedia.org/wiki/Margaret_Hamilton_(software_engineer))
- [Martin Gutzwiller](https://en.wikipedia.org/wiki/Martin_Gutzwiller)
- [Mary Cartwright](https://en.wikipedia.org/wiki/Mary_Cartwright)
- [Mary Rees](https://en.wikipedia.org/wiki/Mary_Rees)
- [Mary Tsingou](https://en.wikipedia.org/wiki/Mary_Tsingou)
- [MathWorld](https://en.wikipedia.org/wiki/MathWorld)
- [Wolfram Mathematica](https://en.wikipedia.org/wiki/Wolfram_Mathematica)
- [Measure-preserving dynamical system](https://en.wikipedia.org/wiki/Measure-preserving_dynamical_system)
- [Michael Berry (physicist)](https://en.wikipedia.org/wiki/Michael_Berry_(physicist))
- [Michel Hénon](https://en.wikipedia.org/wiki/Michel_H%C3%A9non)
- [Mitchell Feigenbaum](https://en.wikipedia.org/wiki/Mitchell_Feigenbaum)
- [Mixing (mathematics)](https://en.wikipedia.org/wiki/Mixing_(mathematics))
- [Morris Hirsch](https://en.wikipedia.org/wiki/Morris_Hirsch)
- [Multiscroll attractor](https://en.wikipedia.org/wiki/Multiscroll_attractor)
- [Nina Snaith](https://en.wikipedia.org/wiki/Nina_Snaith)
- [Nonlinear system](https://en.wikipedia.org/wiki/Nonlinear_system)
- [Normal form (dynamical systems)](https://en.wikipedia.org/wiki/Normal_form_(dynamical_systems))
- [Oleksandr Sharkovsky](https://en.wikipedia.org/wiki/Oleksandr_Sharkovsky)
- [Orbit (dynamics)](https://en.wikipedia.org/wiki/Orbit_(dynamics))
- [Ordinary differential equation](https://en.wikipedia.org/wiki/Ordinary_differential_equation)
- [Otto Rössler](https://en.wikipedia.org/wiki/Otto_R%C3%B6ssler)
- [Outer billiards](https://en.wikipedia.org/wiki/Outer_billiards)
- [Oxford University Press](https://en.wikipedia.org/wiki/Oxford_University_Press)
- [PubMed](https://en.wikipedia.org/wiki/PubMed)
- [Periodic point](https://en.wikipedia.org/wiki/Periodic_point)
- [Peter Grassberger](https://en.wikipedia.org/wiki/Peter_Grassberger)
- [Phase space](https://en.wikipedia.org/wiki/Phase_space)
- [Physical Review Letters](https://en.wikipedia.org/wiki/Physical_Review_Letters)
- [Physics Letters](https://en.wikipedia.org/wiki/Physics_Letters)
- [Pitchfork bifurcation](https://en.wikipedia.org/wiki/Pitchfork_bifurcation)
- [Poincaré plot](https://en.wikipedia.org/wiki/Poincar%C3%A9_plot)
- [Poincaré recurrence theorem](https://en.wikipedia.org/wiki/Poincar%C3%A9_recurrence_theorem)
- [Poincaré map](https://en.wikipedia.org/wiki/Poincar%C3%A9_map)
- [Poincaré–Bendixson theorem](https://en.wikipedia.org/wiki/Poincar%C3%A9%E2%80%93Bendixson_theorem)
- [Mass media](https://en.wikipedia.org/wiki/Mass_media)
- [Population dynamics](https://en.wikipedia.org/wiki/Population_dynamics)
- [Prandtl number](https://en.wikipedia.org/wiki/Prandtl_number)
- [Predictability](https://en.wikipedia.org/wiki/Predictability)
- [Quantum chaos](https://en.wikipedia.org/wiki/Quantum_chaos)
- [Rabinovich–Fabrikant equations](https://en.wikipedia.org/wiki/Rabinovich%E2%80%93Fabrikant_equations)
- [Rayleigh number](https://en.wikipedia.org/wiki/Rayleigh_number)
- [Rayleigh–Bénard convection](https://en.wikipedia.org/wiki/Rayleigh%E2%80%93B%C3%A9nard_convection)
- [Recurrence plot](https://en.wikipedia.org/wiki/Recurrence_plot)
- [Robert L. Devaney](https://en.wikipedia.org/wiki/Robert_L._Devaney)
- [Rufus Bowen](https://en.wikipedia.org/wiki/Rufus_Bowen)
- [Rössler attractor](https://en.wikipedia.org/wiki/R%C3%B6ssler_attractor)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Sinai–Ruelle–Bowen measure](https://en.wikipedia.org/wiki/Sinai%E2%80%93Ruelle%E2%80%93Bowen_measure)
- [SVG](https://en.wikipedia.org/wiki/SVG)
- [Saddle point](https://en.wikipedia.org/wiki/Saddle_point)
- [Santa Fe Institute](https://en.wikipedia.org/wiki/Santa_Fe_Institute)
- [Smale's problems](https://en.wikipedia.org/wiki/Smale%27s_problems)
- [Stability theory](https://en.wikipedia.org/wiki/Stability_theory)
- [Stable manifold](https://en.wikipedia.org/wiki/Stable_manifold)
- [Stable manifold theorem](https://en.wikipedia.org/wiki/Stable_manifold_theorem)
- [Standard map](https://en.wikipedia.org/wiki/Standard_map)
- [Stephen Smale](https://en.wikipedia.org/wiki/Stephen_Smale)
- [Stream function](https://en.wikipedia.org/wiki/Stream_function)
- [Svetlana Jitomirskaya](https://en.wikipedia.org/wiki/Svetlana_Jitomirskaya)
- [Swinging Atwood's machine](https://en.wikipedia.org/wiki/Swinging_Atwood%27s_machine)
- [Synchronization of chaos](https://en.wikipedia.org/wiki/Synchronization_of_chaos)
- [Takens's theorem](https://en.wikipedia.org/wiki/Takens%27s_theorem)
- [Takens's theorem](https://en.wikipedia.org/wiki/Takens%27s_theorem)
- [Tent map](https://en.wikipedia.org/wiki/Tent_map)
- [Thermosiphon](https://en.wikipedia.org/wiki/Thermosiphon)
- [Three-body problem](https://en.wikipedia.org/wiki/Three-body_problem)
- [Three-dimensional space](https://en.wikipedia.org/wiki/Three-dimensional_space)
- [Tilt-A-Whirl](https://en.wikipedia.org/wiki/Tilt-A-Whirl)
- [Tinkerbell map](https://en.wikipedia.org/wiki/Tinkerbell_map)
- [Topological conjugacy](https://en.wikipedia.org/wiki/Topological_conjugacy)
- [Torus knot](https://en.wikipedia.org/wiki/Torus_knot)
- [Trajectory](https://en.wikipedia.org/wiki/Trajectory)
- [Van der Pol oscillator](https://en.wikipedia.org/wiki/Van_der_Pol_oscillator)
- [Warwick Tucker](https://en.wikipedia.org/wiki/Warwick_Tucker)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Weather forecasting](https://en.wikipedia.org/wiki/Weather_forecasting)
- [Wolfram Demonstrations Project](https://en.wikipedia.org/wiki/Wolfram_Demonstrations_Project)
- [Maxima (software)](https://en.wikipedia.org/wiki/Maxima_(software))
- [Yakov Sinai](https://en.wikipedia.org/wiki/Yakov_Sinai)
- [Zeitschrift für Physik](https://en.wikipedia.org/wiki/Zeitschrift_f%C3%BCr_Physik)
- [Zaslavskii map](https://en.wikipedia.org/wiki/Zaslavskii_map)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Make technical articles understandable](https://en.wikipedia.org/wiki/Wikipedia:Make_technical_articles_understandable)
- [Template:Chaos theory](https://en.wikipedia.org/wiki/Template:Chaos_theory)
- [Template talk:Chaos theory](https://en.wikipedia.org/wiki/Template_talk:Chaos_theory)
- [Help:Authority control](https://en.wikipedia.org/wiki/Help:Authority_control)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles with unsourced statements from June 2017](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_June_2017)
- [Category:Wikipedia articles that are too technical from December 2023](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_that_are_too_technical_from_December_2023)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:33:58.599615+00:00_