# Geometric Brownian motion

## Article Metadata

- **Last Updated:** 2024-12-14T19:37:39.989185+00:00
- **Original Article:** [Geometric Brownian motion](https://en.wikipedia.org/wiki/Geometric_Brownian_motion)
- **Language:** en
- **Page ID:** 203523

## Summary

A geometric Brownian motion (GBM) (also known as exponential Brownian motion) is a continuous-time stochastic process in which the logarithm of the randomly varying quantity follows a Brownian motion (also called a Wiener process) with drift. It is an important example of stochastic processes satisfying a stochastic differential equation (SDE); in particular, it is used in mathematical finance to model stock prices in the Black–Scholes model.

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Non-Newtonian calculus
- Category:Short description is different from Wikidata
- Category:Wiener process

## Table of Contents

- Technical definition: the SDE
- Solving the SDE
- Arithmetic Brownian Motion
- Properties of GBM
- Simulating sample paths
- Multivariate version
- Use in finance
- Extensions
- See also
- References
- External links

## Content

A geometric Brownian motion (GBM) (also known as exponential Brownian motion) is a continuous-time stochastic process in which the logarithm of the randomly varying quantity follows a Brownian motion (also called a Wiener process) with drift. It is an important example of stochastic processes satisfying a stochastic differential equation (SDE); in particular, it is used in mathematical finance to model stock prices in the Black–Scholes model.

Technical definition: the SDE
A stochastic process St is said to follow a GBM if it satisfies the following stochastic differential equation (SDE):

  
    
      
        d
        
          S
          
            t
          
        
        =
        μ
        
          S
          
            t
          
        
        
        d
        t
        +
        σ
        
          S
          
            t
          
        
        
        d
        
          W
          
            t
          
        
      
    
    {\displaystyle dS_{t}=\mu S_{t}\,dt+\sigma S_{t}\,dW_{t}}
  

where 
  
    
      
        
          W
          
            t
          
        
      
    
    {\displaystyle W_{t}}
  
 is a Wiener process or Brownian motion, and 
  
    
      
        μ
      
    
    {\displaystyle \mu }
  
 ('the percentage drift') and 
  
    
      
        σ
      
    
    {\displaystyle \sigma }
  
 ('the percentage volatility') are constants.
The former parameter is used to model deterministic trends, while the latter parameter models unpredictable events occurring during the motion.

Solving the SDE
For an arbitrary initial value S0 the above SDE has the analytic solution (under Itô's interpretation):

  
    
      
        
          S
          
            t
          
        
        =
        
          S
          
            0
          
        
        exp
        ⁡
        
          (
          
            
              (
              
                μ
                −
                
                  
                    
                      σ
                      
                        2
                      
                    
                    2
                  
                
              
              )
            
            t
            +
            σ
            
              W
              
                t
              
            
          
          )
        
        .
      
    
    {\displaystyle S_{t}=S_{0}\exp \left(\left(\mu -{\frac {\sigma ^{2}}{2}}\right)t+\sigma W_{t}\right).}
  

The derivation requires the use of Itô calculus. Applying Itô's formula leads to

  
    
      
        d
        (
        ln
        ⁡
        
          S
          
            t
          
        
        )
        =
        (
        ln
        ⁡
        
          S
          
            t
          
        
        
          )
          ′
        
        d
        
          S
          
            t
          
        
        +
        
          
            1
            2
          
        
        (
        ln
        ⁡
        
          S
          
            t
          
        
        
          )
          ″
        
        
        d
        
          S
          
            t
          
        
        
        d
        
          S
          
            t
          
        
        =
        
          
            
              d
              
                S
                
                  t
                
              
            
            
              S
              
                t
              
            
          
        
        −
        
          
            1
            2
          
        
        
        
          
            1
            
              S
              
                t
              
              
                2
              
            
          
        
        
        d
        
          S
          
            t
          
        
        
        d
        
          S
          
            t
          
        
      
    
    {\displaystyle d(\ln S_{t})=(\ln S_{t})'dS_{t}+{\frac {1}{2}}(\ln S_{t})''\,dS_{t}\,dS_{t}={\frac {dS_{t}}{S_{t}}}-{\frac {1}{2}}\,{\frac {1}{S_{t}^{2}}}\,dS_{t}\,dS_{t}}
  

where 
  
    
      
        d
        
          S
          
            t
          
        
        
        d
        
          S
          
            t
          
        
      
    
    {\displaystyle dS_{t}\,dS_{t}}
  
 is the quadratic variation of the SDE. 

  
    
      
        d
        
          S
          
            t
          
        
        
        d
        
          S
          
            t
          
        
        
        =
        
        
          σ
          
            2
          
        
        
        
          S
          
            t
          
          
            2
          
        
        
        d
        
          W
          
            t
          
          
            2
          
        
        +
        2
        σ
        
          S
          
            t
          
          
            2
          
        
        μ
        
        d
        
          W
          
            t
          
        
        
        d
        t
        +
        
          μ
          
            2
          
        
        
          S
          
            t
          
          
            2
          
        
        
        d
        
          t
          
            2
          
        
      
    
    {\displaystyle dS_{t}\,dS_{t}\,=\,\sigma ^{2}\,S_{t}^{2}\,dW_{t}^{2}+2\sigma S_{t}^{2}\mu \,dW_{t}\,dt+\mu ^{2}S_{t}^{2}\,dt^{2}}
  

When 
  
    
      
        d
        t
        →
        0
      
    
    {\displaystyle dt\to 0}
  
, 
  
    
      
        d
        t
      
    
    {\displaystyle dt}
  
 converges to 0 faster than 
  
    
      
        d
        
          W
          
            t
          
        
      
    
    {\displaystyle dW_{t}}
  
, 
since 
  
    
      
        d
        
          W
          
            t
          
          
            2
          
        
        =
        O
        (
        d
        t
        )
      
    
    {\displaystyle dW_{t}^{2}=O(dt)}
  
. So the above infinitesimal can be simplified by 

  
    
      
        d
        
          S
          
            t
          
        
        
        d
        
          S
          
            t
          
        
        
        =
        
        
          σ
          
            2
          
        
        
        
          S
          
            t
          
          
            2
          
        
        
        d
        t
      
    
    {\displaystyle dS_{t}\,dS_{t}\,=\,\sigma ^{2}\,S_{t}^{2}\,dt}
  

Plugging the value of 
  
    
      
        d
        
          S
          
            t
          
        
      
    
    {\displaystyle dS_{t}}
  
 in the above equation and simplifying we obtain

  
    
      
        ln
        ⁡
        
          
            
              S
              
                t
              
            
            
              S
              
                0
              
            
          
        
        =
        
          (
          
            μ
            −
            
              
                
                  σ
                  
                    2
                  
                
                2
              
            
            
          
          )
        
        t
        +
        σ
        
          W
          
            t
          
        
        
        .
      
    
    {\displaystyle \ln {\frac {S_{t}}{S_{0}}}=\left(\mu -{\frac {\sigma ^{2}}{2}}\,\right)t+\sigma W_{t}\,.}
  

Taking the exponential and multiplying both sides by 
  
    
      
        
          S
          
            0
          
        
      
    
    {\displaystyle S_{0}}
  
 gives the solution claimed above.

Arithmetic Brownian Motion
The process for 
  
    
      
        
          X
          
            t
          
        
        =
        ln
        ⁡
        
          
            
              S
              
                t
              
            
            
              S
              
                0
              
            
          
        
      
    
    {\displaystyle X_{t}=\ln {\frac {S_{t}}{S_{0}}}}
  
, satisfying the SDE  

  
    
      
        d
        
          X
          
            t
          
        
        =
        
          (
          
            μ
            −
            
              
                
                  σ
                  
                    2
                  
                
                2
              
            
            
          
          )
        
        d
        t
        +
        σ
        d
        
          W
          
            t
          
        
        
        ,
      
    
    {\displaystyle dX_{t}=\left(\mu -{\frac {\sigma ^{2}}{2}}\,\right)dt+\sigma dW_{t}\,,}
  

or more generally the process solving the SDE

  
    
      
        d
        
          X
          
            t
          
        
        =
        m
        
        d
        t
        +
        v
        
        d
        
          W
          
            t
          
        
        
        ,
      
    
    {\displaystyle dX_{t}=m\,dt+v\,dW_{t}\,,}
  

where 
  
    
      
        m
      
    
    {\displaystyle m}
  
 and 
  
    
      
        v
        >
        0
      
    
    {\displaystyle v>0}
  
 are real constants and for an initial condition 
  
    
      
        
          X
          
            0
          
        
      
    
    {\displaystyle X_{0}}
  
, is called an Arithmetic Brownian Motion (ABM). This was the model postulated by Louis Bachelier in 1900 for stock prices, in the first published attempt to model Brownian motion, known today as Bachelier model. As was shown above, the ABM SDE can be obtained through the logarithm of a GBM via Itô's formula. Similarly, a GBM can be obtained by exponentiation of an ABM through Itô's formula.

Properties of GBM
The above solution 
  
    
      
        
          S
          
            t
          
        
      
    
    {\displaystyle S_{t}}
  
 (for any value of t) is a log-normally distributed random variable with expected value and variance given by

  
    
      
        E
        ⁡
        (
        
          S
          
            t
          
        
        )
        =
        
          S
          
            0
          
        
        
          e
          
            μ
            t
          
        
        ,
      
    
    {\displaystyle \operatorname {E} (S_{t})=S_{0}e^{\mu t},}
  

  
    
      
        Var
        ⁡
        (
        
          S
          
            t
          
        
        )
        =
        
          S
          
            0
          
          
            2
          
        
        
          e
          
            2
            μ
            t
          
        
        
          (
          
            
              e
              
                
                  σ
                  
                    2
                  
                
                t
              
            
            −
            1
          
          )
        
        .
      
    
    {\displaystyle \operatorname {Var} (S_{t})=S_{0}^{2}e^{2\mu t}\left(e^{\sigma ^{2}t}-1\right).}
  

They can be derived using the fact that 
  
    
      
        
          Z
          
            t
          
        
        =
        exp
        ⁡
        
          (
          
            σ
            
              W
              
                t
              
            
            −
            
              
                1
                2
              
            
            
              σ
              
                2
              
            
            t
          
          )
        
      
    
    {\displaystyle Z_{t}=\exp \left(\sigma W_{t}-{\frac {1}{2}}\sigma ^{2}t\right)}
  
 is a martingale, and that

  
    
      
        E
        ⁡
        
          [
          
            exp
            ⁡
            
              (
              
                2
                σ
                
                  W
                  
                    t
                  
                
                −
                
                  σ
                  
                    2
                  
                
                t
              
              )
            
            ∣
            
              
                
                  F
                
              
              
                s
              
            
          
          ]
        
        =
        
          e
          
            
              σ
              
                2
              
            
            (
            t
            −
            s
            )
          
        
        exp
        ⁡
        
          (
          
            2
            σ
            
              W
              
                s
              
            
            −
            
              σ
              
                2
              
            
            s
          
          )
        
        ,
        
        ∀
        0
        ≤
        s
        <
        t
        .
      
    
    {\displaystyle \operatorname {E} \left[\exp \left(2\sigma W_{t}-\sigma ^{2}t\right)\mid {\mathcal {F}}_{s}\right]=e^{\sigma ^{2}(t-s)}\exp \left(2\sigma W_{s}-\sigma ^{2}s\right),\quad \forall 0\leq s<t.}
  

The probability density function of 
  
    
      
        
          S
          
            t
          
        
      
    
    {\displaystyle S_{t}}
  
 is:

  
    
      
        
          f
          
            
              S
              
                t
              
            
          
        
        (
        s
        ;
        μ
        ,
        σ
        ,
        t
        )
        =
        
          
            1
            
              2
              π
            
          
        
        
        
          
            1
            
              s
              σ
              
                
                  t
                
              
            
          
        
        
        exp
        ⁡
        
          (
          
            −
            
              
                
                  
                    (
                    
                      ln
                      ⁡
                      s
                      −
                      ln
                      ⁡
                      
                        S
                        
                          0
                        
                      
                      −
                      
                        (
                        
                          μ
                          −
                          
                            
                              1
                              2
                            
                          
                          
                            σ
                            
                              2
                            
                          
                        
                        )
                      
                      t
                    
                    )
                  
                  
                    2
                  
                
                
                  2
                  
                    σ
                    
                      2
                    
                  
                  t
                
              
            
          
          )
        
        .
      
    
    {\displaystyle f_{S_{t}}(s;\mu ,\sigma ,t)={\frac {1}{\sqrt {2\pi }}}\,{\frac {1}{s\sigma {\sqrt {t}}}}\,\exp \left(-{\frac {\left(\ln s-\ln S_{0}-\left(\mu -{\frac {1}{2}}\sigma ^{2}\right)t\right)^{2}}{2\sigma ^{2}t}}\right).}
  

When deriving further properties of GBM, use can be made of the SDE of which GBM is the solution, or the explicit solution given above can be used. For example, consider the stochastic process log(St). This is an interesting process, because in the  Black–Scholes model it is related to the log return of the stock price. Using Itô's lemma with f(S) = log(S) gives

  
    
      
        
          
            
              
                d
                log
                ⁡
                (
                S
                )
              
              
                
                =
                
                  f
                  ′
                
                (
                S
                )
                
                d
                S
                +
                
                  
                    1
                    2
                  
                
                
                  f
                  ″
                
                (
                S
                )
                
                  S
                  
                    2
                  
                
                
                  σ
                  
                    2
                  
                
                
                d
                t
              
            
            
              
              
                
                =
                
                  
                    1
                    S
                  
                
                
                  (
                  
                    σ
                    S
                    
                    d
                    
                      W
                      
                        t
                      
                    
                    +
                    μ
                    S
                    
                    d
                    t
                  
                  )
                
                −
                
                  
                    1
                    2
                  
                
                
                  σ
                  
                    2
                  
                
                
                d
                t
              
            
            
              
              
                
                =
                σ
                
                d
                
                  W
                  
                    t
                  
                
                +
                (
                μ
                −
                
                  σ
                  
                    2
                  
                
                
                  /
                
                2
                )
                
                d
                t
                .
              
            
          
        
      
    
    {\displaystyle {\begin{alignedat}{2}d\log(S)&=f'(S)\,dS+{\frac {1}{2}}f''(S)S^{2}\sigma ^{2}\,dt\\[6pt]&={\frac {1}{S}}\left(\sigma S\,dW_{t}+\mu S\,dt\right)-{\frac {1}{2}}\sigma ^{2}\,dt\\[6pt]&=\sigma \,dW_{t}+(\mu -\sigma ^{2}/2)\,dt.\end{alignedat}}}
  

It follows that 
  
    
      
        E
        ⁡
        log
        ⁡
        (
        
          S
          
            t
          
        
        )
        =
        log
        ⁡
        (
        
          S
          
            0
          
        
        )
        +
        (
        μ
        −
        
          σ
          
            2
          
        
        
          /
        
        2
        )
        t
      
    
    {\displaystyle \operatorname {E} \log(S_{t})=\log(S_{0})+(\mu -\sigma ^{2}/2)t}
  
.
This result can also be derived by applying the logarithm to the explicit solution of GBM:

  
    
      
        
          
            
              
                log
                ⁡
                (
                
                  S
                  
                    t
                  
                
                )
              
              
                
                =
                log
                ⁡
                
                  (
                  
                    
                      S
                      
                        0
                      
                    
                    exp
                    ⁡
                    
                      (
                      
                        
                          (
                          
                            μ
                            −
                            
                              
                                
                                  σ
                                  
                                    2
                                  
                                
                                2
                              
                            
                          
                          )
                        
                        t
                        +
                        σ
                        
                          W
                          
                            t
                          
                        
                      
                      )
                    
                  
                  )
                
              
            
            
              
              
                
                =
                log
                ⁡
                (
                
                  S
                  
                    0
                  
                
                )
                +
                
                  (
                  
                    μ
                    −
                    
                      
                        
                          σ
                          
                            2
                          
                        
                        2
                      
                    
                  
                  )
                
                t
                +
                σ
                
                  W
                  
                    t
                  
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{alignedat}{2}\log(S_{t})&=\log \left(S_{0}\exp \left(\left(\mu -{\frac {\sigma ^{2}}{2}}\right)t+\sigma W_{t}\right)\right)\\[6pt]&=\log(S_{0})+\left(\mu -{\frac {\sigma ^{2}}{2}}\right)t+\sigma W_{t}.\end{alignedat}}}
  

Taking the expectation yields the same result as above:  
  
    
      
        E
        ⁡
        log
        ⁡
        (
        
          S
          
            t
          
        
        )
        =
        log
        ⁡
        (
        
          S
          
            0
          
        
        )
        +
        (
        μ
        −
        
          σ
          
            2
          
        
        
          /
        
        2
        )
        t
      
    
    {\displaystyle \operatorname {E} \log(S_{t})=\log(S_{0})+(\mu -\sigma ^{2}/2)t}
  
.

Simulating sample paths
Multivariate version
GBM can be extended to the case where there are multiple correlated price paths.
Each price path follows the underlying process

  
    
      
        d
        
          S
          
            t
          
          
            i
          
        
        =
        
          μ
          
            i
          
        
        
          S
          
            t
          
          
            i
          
        
        
        d
        t
        +
        
          σ
          
            i
          
        
        
          S
          
            t
          
          
            i
          
        
        
        d
        
          W
          
            t
          
          
            i
          
        
        ,
      
    
    {\displaystyle dS_{t}^{i}=\mu _{i}S_{t}^{i}\,dt+\sigma _{i}S_{t}^{i}\,dW_{t}^{i},}
  

where the Wiener processes are correlated such that 
  
    
      
        E
        ⁡
        (
        d
        
          W
          
            t
          
          
            i
          
        
        
        d
        
          W
          
            t
          
          
            j
          
        
        )
        =
        
          ρ
          
            i
            ,
            j
          
        
        
        d
        t
      
    
    {\displaystyle \operatorname {E} (dW_{t}^{i}\,dW_{t}^{j})=\rho _{i,j}\,dt}
  
 where 
  
    
      
        
          ρ
          
            i
            ,
            i
          
        
        =
        1
      
    
    {\displaystyle \rho _{i,i}=1}
  
.
For the multivariate case, this implies that

  
    
      
        Cov
        ⁡
        (
        
          S
          
            t
          
          
            i
          
        
        ,
        
          S
          
            t
          
          
            j
          
        
        )
        =
        
          S
          
            0
          
          
            i
          
        
        
          S
          
            0
          
          
            j
          
        
        
          e
          
            (
            
              μ
              
                i
              
            
            +
            
              μ
              
                j
              
            
            )
            t
          
        
        
          (
          
            
              e
              
                
                  ρ
                  
                    i
                    ,
                    j
                  
                
                
                  σ
                  
                    i
                  
                
                
                  σ
                  
                    j
                  
                
                t
              
            
            −
            1
          
          )
        
        .
      
    
    {\displaystyle \operatorname {Cov} (S_{t}^{i},S_{t}^{j})=S_{0}^{i}S_{0}^{j}e^{(\mu _{i}+\mu _{j})t}\left(e^{\rho _{i,j}\sigma _{i}\sigma _{j}t}-1\right).}
  

A multivariate formulation that maintains the driving Brownian motions 
  
    
      
        
          W
          
            t
          
          
            i
          
        
      
    
    {\displaystyle W_{t}^{i}}
  
 independent is 

  
    
      
        d
        
          S
          
            t
          
          
            i
          
        
        =
        
          μ
          
            i
          
        
        
          S
          
            t
          
          
            i
          
        
        
        d
        t
        +
        
          ∑
          
            j
            =
            1
          
          
            d
          
        
        
          σ
          
            i
            ,
            j
          
        
        
          S
          
            t
          
          
            i
          
        
        
        d
        
          W
          
            t
          
          
            j
          
        
        ,
      
    
    {\displaystyle dS_{t}^{i}=\mu _{i}S_{t}^{i}\,dt+\sum _{j=1}^{d}\sigma _{i,j}S_{t}^{i}\,dW_{t}^{j},}
  

where the correlation between 
  
    
      
        
          S
          
            t
          
          
            i
          
        
      
    
    {\displaystyle S_{t}^{i}}
  
 and 
  
    
      
        
          S
          
            t
          
          
            j
          
        
      
    
    {\displaystyle S_{t}^{j}}
  
 is now expressed through the 
  
    
      
        
          σ
          
            i
            ,
            j
          
        
        =
        
          ρ
          
            i
            ,
            j
          
        
        
        
          σ
          
            i
          
        
        
        
          σ
          
            j
          
        
      
    
    {\displaystyle \sigma _{i,j}=\rho _{i,j}\,\sigma _{i}\,\sigma _{j}}
  
 terms.

Use in finance
Geometric Brownian motion is used to model stock prices in the Black–Scholes model and is the most widely used model of stock price behavior.
Some of the arguments for using GBM to model stock prices are:

The expected returns of GBM are independent of the value of the process (stock price), which agrees with what we would expect in reality.
A GBM process only assumes positive values, just like real stock prices.
A GBM process shows the same kind of 'roughness' in its paths as we see in real stock prices.
Calculations with GBM processes are relatively easy.
However, GBM is not a completely realistic model, in particular it falls short of reality in the following points:

In real stock prices, volatility changes over time (possibly stochastically), but in GBM, volatility is assumed constant.
In real life, stock prices often show jumps caused by unpredictable events or news, but in GBM, the path is continuous (no discontinuity).
Apart from modeling stock prices, Geometric Brownian motion has also found applications in the monitoring of trading strategies.

Extensions
In an attempt to make GBM more realistic as a model for stock prices, also in relation to the volatility smile problem, one can drop the assumption that the volatility (
  
    
      
        σ
      
    
    {\displaystyle \sigma }
  
) is constant. If we assume that the volatility is a deterministic function of the stock price and time, this is called a local volatility model. A straightforward extension of the Black Scholes GBM is a local volatility SDE whose distribution is a mixture of distributions of GBM, the lognormal mixture dynamics, resulting in a convex combination of Black Scholes prices for options. If instead we assume that the volatility has a randomness of its own—often described by a different equation driven by a different Brownian Motion—the model is called a stochastic volatility model, see for example the Heston model.

See also
Brownian surface

References
External links
Geometric Brownian motion models for stock movement except in rare events.
Excel Simulation of a Geometric Brownian Motion to simulate Stock Prices 
"Interactive Web Application: Stochastic Processes used in Quantitative Finance". Archived from the original on 2015-09-20. Retrieved 2015-07-03.
Non-Newtonian calculus website
Trading Strategy Monitoring: Modeling the PnL as a Geometric Brownian Motion

## Related Articles

### Internal Links

- [Abstract Wiener space](https://en.wikipedia.org/wiki/Abstract_Wiener_space)
- [Actuarial science](https://en.wikipedia.org/wiki/Actuarial_science)
- [Additive process](https://en.wikipedia.org/wiki/Additive_process)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Asset pricing](https://en.wikipedia.org/wiki/Asset_pricing)
- [Autoregressive conditional heteroskedasticity](https://en.wikipedia.org/wiki/Autoregressive_conditional_heteroskedasticity)
- [Autoregressive integrated moving average](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average)
- [Autoregressive model](https://en.wikipedia.org/wiki/Autoregressive_model)
- [Autoregressive moving-average model](https://en.wikipedia.org/wiki/Autoregressive_moving-average_model)
- [Bachelier model](https://en.wikipedia.org/wiki/Bachelier_model)
- [Bernoulli process](https://en.wikipedia.org/wiki/Bernoulli_process)
- [Bessel process](https://en.wikipedia.org/wiki/Bessel_process)
- [Biased random walk on a graph](https://en.wikipedia.org/wiki/Biased_random_walk_on_a_graph)
- [Binomial options pricing model](https://en.wikipedia.org/wiki/Binomial_options_pricing_model)
- [Birth process](https://en.wikipedia.org/wiki/Birth_process)
- [Birth–death process](https://en.wikipedia.org/wiki/Birth%E2%80%93death_process)
- [Black–Derman–Toy model](https://en.wikipedia.org/wiki/Black%E2%80%93Derman%E2%80%93Toy_model)
- [Black–Karasinski model](https://en.wikipedia.org/wiki/Black%E2%80%93Karasinski_model)
- [Black–Scholes model](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)
- [Blumenthal's zero–one law](https://en.wikipedia.org/wiki/Blumenthal%27s_zero%E2%80%93one_law)
- [Boolean network](https://en.wikipedia.org/wiki/Boolean_network)
- [Borel–Cantelli lemma](https://en.wikipedia.org/wiki/Borel%E2%80%93Cantelli_lemma)
- [Branching process](https://en.wikipedia.org/wiki/Branching_process)
- [Brownian bridge](https://en.wikipedia.org/wiki/Brownian_bridge)
- [Brownian excursion](https://en.wikipedia.org/wiki/Brownian_excursion)
- [Brownian meander](https://en.wikipedia.org/wiki/Brownian_meander)
- [Brownian motion](https://en.wikipedia.org/wiki/Brownian_motion)
- [Brownian surface](https://en.wikipedia.org/wiki/Brownian_surface)
- [Bulk queue](https://en.wikipedia.org/wiki/Bulk_queue)
- [Quadratic variation](https://en.wikipedia.org/wiki/Quadratic_variation)
- [Bühlmann model](https://en.wikipedia.org/wiki/B%C3%BChlmann_model)
- [Cameron–Martin theorem](https://en.wikipedia.org/wiki/Cameron%E2%80%93Martin_theorem)
- [Cauchy process](https://en.wikipedia.org/wiki/Cauchy_process)
- [Central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)
- [Chan–Karolyi–Longstaff–Sanders process](https://en.wikipedia.org/wiki/Chan%E2%80%93Karolyi%E2%80%93Longstaff%E2%80%93Sanders_process)
- [Chen model](https://en.wikipedia.org/wiki/Chen_model)
- [Chinese restaurant process](https://en.wikipedia.org/wiki/Chinese_restaurant_process)
- [Classical Wiener space](https://en.wikipedia.org/wiki/Classical_Wiener_space)
- [Compound Poisson process](https://en.wikipedia.org/wiki/Compound_Poisson_process)
- [Constant elasticity of variance model](https://en.wikipedia.org/wiki/Constant_elasticity_of_variance_model)
- [Contact process (mathematics)](https://en.wikipedia.org/wiki/Contact_process_(mathematics))
- [Continuous-time random walk](https://en.wikipedia.org/wiki/Continuous-time_random_walk)
- [Continuous-time stochastic process](https://en.wikipedia.org/wiki/Continuous-time_stochastic_process)
- [Continuous stochastic process](https://en.wikipedia.org/wiki/Continuous_stochastic_process)
- [Convergence of random variables](https://en.wikipedia.org/wiki/Convergence_of_random_variables)
- [Cox process](https://en.wikipedia.org/wiki/Cox_process)
- [Cox–Ingersoll–Ross model](https://en.wikipedia.org/wiki/Cox%E2%80%93Ingersoll%E2%80%93Ross_model)
- [Ruin theory](https://en.wikipedia.org/wiki/Ruin_theory)
- [Càdlàg](https://en.wikipedia.org/wiki/C%C3%A0dl%C3%A0g)
- [Damiano Brigo](https://en.wikipedia.org/wiki/Damiano_Brigo)
- [Deterministic system](https://en.wikipedia.org/wiki/Deterministic_system)
- [Diffusion process](https://en.wikipedia.org/wiki/Diffusion_process)
- [Dirac delta function](https://en.wikipedia.org/wiki/Dirac_delta_function)
- [Dirichlet process](https://en.wikipedia.org/wiki/Dirichlet_process)
- [Stochastic process](https://en.wikipedia.org/wiki/Stochastic_process)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Doléans-Dade exponential](https://en.wikipedia.org/wiki/Dol%C3%A9ans-Dade_exponential)
- [Donsker's theorem](https://en.wikipedia.org/wiki/Donsker%27s_theorem)
- [Doob's martingale convergence theorems](https://en.wikipedia.org/wiki/Doob%27s_martingale_convergence_theorems)
- [Doob's martingale inequality](https://en.wikipedia.org/wiki/Doob%27s_martingale_inequality)
- [Optional stopping theorem](https://en.wikipedia.org/wiki/Optional_stopping_theorem)
- [Doob's martingale convergence theorems](https://en.wikipedia.org/wiki/Doob%27s_martingale_convergence_theorems)
- [Doob decomposition theorem](https://en.wikipedia.org/wiki/Doob_decomposition_theorem)
- [Doob–Meyer decomposition theorem](https://en.wikipedia.org/wiki/Doob%E2%80%93Meyer_decomposition_theorem)
- [Dynkin's formula](https://en.wikipedia.org/wiki/Dynkin%27s_formula)
- [Dyson Brownian motion](https://en.wikipedia.org/wiki/Dyson_Brownian_motion)
- [Econometrics](https://en.wikipedia.org/wiki/Econometrics)
- [Empirical process](https://en.wikipedia.org/wiki/Empirical_process)
- [Engelbert–Schmidt zero–one law](https://en.wikipedia.org/wiki/Engelbert%E2%80%93Schmidt_zero%E2%80%93one_law)
- [Ergodic theory](https://en.wikipedia.org/wiki/Ergodic_theory)
- [Ergodic theory](https://en.wikipedia.org/wiki/Ergodic_theory)
- [Ergodicity](https://en.wikipedia.org/wiki/Ergodicity)
- [Exchangeable random variables](https://en.wikipedia.org/wiki/Exchangeable_random_variables)
- [Expected value](https://en.wikipedia.org/wiki/Expected_value)
- [Extreme value theory](https://en.wikipedia.org/wiki/Extreme_value_theory)
- [Fabio Mercurio](https://en.wikipedia.org/wiki/Fabio_Mercurio)
- [Feller-continuous process](https://en.wikipedia.org/wiki/Feller-continuous_process)
- [Feller process](https://en.wikipedia.org/wiki/Feller_process)
- [Feynman–Kac formula](https://en.wikipedia.org/wiki/Feynman%E2%80%93Kac_formula)
- [Filtration (probability theory)](https://en.wikipedia.org/wiki/Filtration_(probability_theory))
- [Fisher–Tippett–Gnedenko theorem](https://en.wikipedia.org/wiki/Fisher%E2%80%93Tippett%E2%80%93Gnedenko_theorem)
- [Fleming–Viot process](https://en.wikipedia.org/wiki/Fleming%E2%80%93Viot_process)
- [Fluid queue](https://en.wikipedia.org/wiki/Fluid_queue)
- [Fokker–Planck equation](https://en.wikipedia.org/wiki/Fokker%E2%80%93Planck_equation)
- [Fractional Brownian motion](https://en.wikipedia.org/wiki/Fractional_Brownian_motion)
- [G-network](https://en.wikipedia.org/wiki/G-network)
- [Galton–Watson process](https://en.wikipedia.org/wiki/Galton%E2%80%93Watson_process)
- [Gamma process](https://en.wikipedia.org/wiki/Gamma_process)
- [Foreign exchange option](https://en.wikipedia.org/wiki/Foreign_exchange_option)
- [Gaussian process](https://en.wikipedia.org/wiki/Gaussian_process)
- [Gaussian random field](https://en.wikipedia.org/wiki/Gaussian_random_field)
- [Gauss–Markov process](https://en.wikipedia.org/wiki/Gauss%E2%80%93Markov_process)
- [Geometric process](https://en.wikipedia.org/wiki/Geometric_process)
- [Gibbs measure](https://en.wikipedia.org/wiki/Gibbs_measure)
- [Girsanov theorem](https://en.wikipedia.org/wiki/Girsanov_theorem)
- [Hawkes process](https://en.wikipedia.org/wiki/Hawkes_process)
- [Heat equation](https://en.wikipedia.org/wiki/Heat_equation)
- [Heat kernel](https://en.wikipedia.org/wiki/Heat_kernel)
- [Heath–Jarrow–Morton framework](https://en.wikipedia.org/wiki/Heath%E2%80%93Jarrow%E2%80%93Morton_framework)
- [Heston model](https://en.wikipedia.org/wiki/Heston_model)
- [Hewitt–Savage zero–one law](https://en.wikipedia.org/wiki/Hewitt%E2%80%93Savage_zero%E2%80%93one_law)
- [Hidden Markov model](https://en.wikipedia.org/wiki/Hidden_Markov_model)
- [Hopfield network](https://en.wikipedia.org/wiki/Hopfield_network)
- [Ho–Lee model](https://en.wikipedia.org/wiki/Ho%E2%80%93Lee_model)
- [Hull–White model](https://en.wikipedia.org/wiki/Hull%E2%80%93White_model)
- [Hunt process](https://en.wikipedia.org/wiki/Hunt_process)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Independent and identically distributed random variables](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables)
- [Infinitesimal generator (stochastic processes)](https://en.wikipedia.org/wiki/Infinitesimal_generator_(stochastic_processes))
- [Interacting particle system](https://en.wikipedia.org/wiki/Interacting_particle_system)
- [Ising model](https://en.wikipedia.org/wiki/Ising_model)
- [Itô's lemma](https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma)
- [Itô's lemma](https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma)
- [Itô calculus](https://en.wikipedia.org/wiki/It%C3%B4_calculus)
- [Itô diffusion](https://en.wikipedia.org/wiki/It%C3%B4_diffusion)
- [Itô calculus](https://en.wikipedia.org/wiki/It%C3%B4_calculus)
- [Itô calculus](https://en.wikipedia.org/wiki/It%C3%B4_calculus)
- [JSTOR](https://en.wikipedia.org/wiki/JSTOR)
- [Jump diffusion](https://en.wikipedia.org/wiki/Jump_diffusion)
- [Jump process](https://en.wikipedia.org/wiki/Jump_process)
- [Kosambi–Karhunen–Loève theorem](https://en.wikipedia.org/wiki/Kosambi%E2%80%93Karhunen%E2%80%93Lo%C3%A8ve_theorem)
- [Kolmogorov's zero–one law](https://en.wikipedia.org/wiki/Kolmogorov%27s_zero%E2%80%93one_law)
- [Kolmogorov continuity theorem](https://en.wikipedia.org/wiki/Kolmogorov_continuity_theorem)
- [Kolmogorov extension theorem](https://en.wikipedia.org/wiki/Kolmogorov_extension_theorem)
- [Korn–Kreer–Lenssen model](https://en.wikipedia.org/wiki/Korn%E2%80%93Kreer%E2%80%93Lenssen_model)
- [Kunita–Watanabe inequality](https://en.wikipedia.org/wiki/Kunita%E2%80%93Watanabe_inequality)
- [LIBOR market model](https://en.wikipedia.org/wiki/LIBOR_market_model)
- [Rate function](https://en.wikipedia.org/wiki/Rate_function)
- [Large deviations theory](https://en.wikipedia.org/wiki/Large_deviations_theory)
- [Law of large numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers)
- [Law of the iterated logarithm](https://en.wikipedia.org/wiki/Law_of_the_iterated_logarithm)
- [List of inequalities](https://en.wikipedia.org/wiki/List_of_inequalities)
- [List of stochastic processes topics](https://en.wikipedia.org/wiki/List_of_stochastic_processes_topics)
- [Local martingale](https://en.wikipedia.org/wiki/Local_martingale)
- [Local time (mathematics)](https://en.wikipedia.org/wiki/Local_time_(mathematics))
- [Local volatility](https://en.wikipedia.org/wiki/Local_volatility)
- [Log-normal distribution](https://en.wikipedia.org/wiki/Log-normal_distribution)
- [Rate of return](https://en.wikipedia.org/wiki/Rate_of_return)
- [Logarithm](https://en.wikipedia.org/wiki/Logarithm)
- [Loop-erased random walk](https://en.wikipedia.org/wiki/Loop-erased_random_walk)
- [Louis Bachelier](https://en.wikipedia.org/wiki/Louis_Bachelier)
- [Doob's martingale convergence theorems](https://en.wikipedia.org/wiki/Doob%27s_martingale_convergence_theorems)
- [Lévy process](https://en.wikipedia.org/wiki/L%C3%A9vy_process)
- [Lévy–Prokhorov metric](https://en.wikipedia.org/wiki/L%C3%A9vy%E2%80%93Prokhorov_metric)
- [M/G/1 queue](https://en.wikipedia.org/wiki/M/G/1_queue)
- [M/M/1 queue](https://en.wikipedia.org/wiki/M/M/1_queue)
- [M/M/c queue](https://en.wikipedia.org/wiki/M/M/c_queue)
- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
- [Malliavin calculus](https://en.wikipedia.org/wiki/Malliavin_calculus)
- [Marcinkiewicz–Zygmund inequality](https://en.wikipedia.org/wiki/Marcinkiewicz%E2%80%93Zygmund_inequality)
- [Markov additive process](https://en.wikipedia.org/wiki/Markov_additive_process)
- [Markov chain](https://en.wikipedia.org/wiki/Markov_chain)
- [Markov chain](https://en.wikipedia.org/wiki/Markov_chain)
- [Markov property](https://en.wikipedia.org/wiki/Markov_property)
- [Markov random field](https://en.wikipedia.org/wiki/Markov_random_field)
- [Martingale (probability theory)](https://en.wikipedia.org/wiki/Martingale_(probability_theory))
- [Martingale difference sequence](https://en.wikipedia.org/wiki/Martingale_difference_sequence)
- [Martingale representation theorem](https://en.wikipedia.org/wiki/Martingale_representation_theorem)
- [Mathematical finance](https://en.wikipedia.org/wiki/Mathematical_finance)
- [Mathematical statistics](https://en.wikipedia.org/wiki/Mathematical_statistics)
- [Maximal entropy random walk](https://en.wikipedia.org/wiki/Maximal_entropy_random_walk)
- [Maximal ergodic theorem](https://en.wikipedia.org/wiki/Maximal_ergodic_theorem)
- [McKean–Vlasov process](https://en.wikipedia.org/wiki/McKean%E2%80%93Vlasov_process)
- [Mixing (mathematics)](https://en.wikipedia.org/wiki/Mixing_(mathematics))
- [Moran process](https://en.wikipedia.org/wiki/Moran_process)
- [Moving-average model](https://en.wikipedia.org/wiki/Moving-average_model)
- [Poisson point process](https://en.wikipedia.org/wiki/Poisson_point_process)
- [Optional stopping theorem](https://en.wikipedia.org/wiki/Optional_stopping_theorem)
- [Ornstein–Uhlenbeck process](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process)
- [Percolation theory](https://en.wikipedia.org/wiki/Percolation_theory)
- [Piecewise-deterministic Markov process](https://en.wikipedia.org/wiki/Piecewise-deterministic_Markov_process)
- [Pitman–Yor process](https://en.wikipedia.org/wiki/Pitman%E2%80%93Yor_process)
- [Point process](https://en.wikipedia.org/wiki/Point_process)
- [Poisson point process](https://en.wikipedia.org/wiki/Poisson_point_process)
- [Potts model](https://en.wikipedia.org/wiki/Potts_model)
- [Predictable process](https://en.wikipedia.org/wiki/Predictable_process)
- [Probability density function](https://en.wikipedia.org/wiki/Probability_density_function)
- [Probability theory](https://en.wikipedia.org/wiki/Probability_theory)
- [Progressively measurable process](https://en.wikipedia.org/wiki/Progressively_measurable_process)
- [Prokhorov's theorem](https://en.wikipedia.org/wiki/Prokhorov%27s_theorem)
- [Quadratic variation](https://en.wikipedia.org/wiki/Quadratic_variation)
- [Queueing theory](https://en.wikipedia.org/wiki/Queueing_theory)
- [Queueing theory](https://en.wikipedia.org/wiki/Queueing_theory)
- [Random dynamical system](https://en.wikipedia.org/wiki/Random_dynamical_system)
- [Random field](https://en.wikipedia.org/wiki/Random_field)
- [Random graph](https://en.wikipedia.org/wiki/Random_graph)
- [Random variable](https://en.wikipedia.org/wiki/Random_variable)
- [Random walk](https://en.wikipedia.org/wiki/Random_walk)
- [Reflection principle (Wiener process)](https://en.wikipedia.org/wiki/Reflection_principle_(Wiener_process))
- [Regenerative process](https://en.wikipedia.org/wiki/Regenerative_process)
- [Rendleman–Bartter model](https://en.wikipedia.org/wiki/Rendleman%E2%80%93Bartter_model)
- [Renewal theory](https://en.wikipedia.org/wiki/Renewal_theory)
- [Renewal theory](https://en.wikipedia.org/wiki/Renewal_theory)
- [Ruin theory](https://en.wikipedia.org/wiki/Ruin_theory)
- [Ruin theory](https://en.wikipedia.org/wiki/Ruin_theory)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [SABR volatility model](https://en.wikipedia.org/wiki/SABR_volatility_model)
- [Sample-continuous process](https://en.wikipedia.org/wiki/Sample-continuous_process)
- [Sanov's theorem](https://en.wikipedia.org/wiki/Sanov%27s_theorem)
- [Schramm–Loewner evolution](https://en.wikipedia.org/wiki/Schramm%E2%80%93Loewner_evolution)
- [Self-avoiding walk](https://en.wikipedia.org/wiki/Self-avoiding_walk)
- [Self-similar process](https://en.wikipedia.org/wiki/Self-similar_process)
- [Semimartingale](https://en.wikipedia.org/wiki/Semimartingale)
- [Sigma-martingale](https://en.wikipedia.org/wiki/Sigma-martingale)
- [Signal processing](https://en.wikipedia.org/wiki/Signal_processing)
- [Skorokhod's representation theorem](https://en.wikipedia.org/wiki/Skorokhod%27s_representation_theorem)
- [Skorokhod integral](https://en.wikipedia.org/wiki/Skorokhod_integral)
- [Càdlàg](https://en.wikipedia.org/wiki/C%C3%A0dl%C3%A0g)
- [Snell envelope](https://en.wikipedia.org/wiki/Snell_envelope)
- [Ruin theory](https://en.wikipedia.org/wiki/Ruin_theory)
- [Stable process](https://en.wikipedia.org/wiki/Stable_process)
- [Stationary process](https://en.wikipedia.org/wiki/Stationary_process)
- [Statistics](https://en.wikipedia.org/wiki/Statistics)
- [Steven L. Heston](https://en.wikipedia.org/wiki/Steven_L._Heston)
- [Stochastic calculus](https://en.wikipedia.org/wiki/Stochastic_calculus)
- [Stochastic chains with memory of variable length](https://en.wikipedia.org/wiki/Stochastic_chains_with_memory_of_variable_length)
- [Stochastic control](https://en.wikipedia.org/wiki/Stochastic_control)
- [Stochastic differential equation](https://en.wikipedia.org/wiki/Stochastic_differential_equation)
- [Stochastic drift](https://en.wikipedia.org/wiki/Stochastic_drift)
- [Stochastic process](https://en.wikipedia.org/wiki/Stochastic_process)
- [Stochastic volatility](https://en.wikipedia.org/wiki/Stochastic_volatility)
- [Stopping time](https://en.wikipedia.org/wiki/Stopping_time)
- [Stratonovich integral](https://en.wikipedia.org/wiki/Stratonovich_integral)
- [Martingale (probability theory)](https://en.wikipedia.org/wiki/Martingale_(probability_theory))
- [Martingale (probability theory)](https://en.wikipedia.org/wiki/Martingale_(probability_theory))
- [Superprocess](https://en.wikipedia.org/wiki/Superprocess)
- [Tanaka equation](https://en.wikipedia.org/wiki/Tanaka_equation)
- [Telegraph process](https://en.wikipedia.org/wiki/Telegraph_process)
- [Time reversibility](https://en.wikipedia.org/wiki/Time_reversibility)
- [Time series](https://en.wikipedia.org/wiki/Time_series)
- [Time series](https://en.wikipedia.org/wiki/Time_series)
- [Uniform integrability](https://en.wikipedia.org/wiki/Uniform_integrability)
- [Filtration (probability theory)](https://en.wikipedia.org/wiki/Filtration_(probability_theory))
- [Variance](https://en.wikipedia.org/wiki/Variance)
- [Variance gamma process](https://en.wikipedia.org/wiki/Variance_gamma_process)
- [Vasicek model](https://en.wikipedia.org/wiki/Vasicek_model)
- [Volatility smile](https://en.wikipedia.org/wiki/Volatility_smile)
- [White noise](https://en.wikipedia.org/wiki/White_noise)
- [Wiener process](https://en.wikipedia.org/wiki/Wiener_process)
- [Wiener sausage](https://en.wikipedia.org/wiki/Wiener_sausage)
- [Classical Wiener space](https://en.wikipedia.org/wiki/Classical_Wiener_space)
- [Wilkie investment model](https://en.wikipedia.org/wiki/Wilkie_investment_model)
- [Zero–one law](https://en.wikipedia.org/wiki/Zero%E2%80%93one_law)
- [Template:Stochastic processes](https://en.wikipedia.org/wiki/Template:Stochastic_processes)
- [Template talk:Stochastic processes](https://en.wikipedia.org/wiki/Template_talk:Stochastic_processes)
- [Category:Stochastic processes](https://en.wikipedia.org/wiki/Category:Stochastic_processes)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:37:39.989185+00:00_