---
title: Stochastic dynamic programming
url: https://en.wikipedia.org/wiki/Stochastic_dynamic_programming
language: en
categories: ["Category:All articles to be expanded", "Category:Articles to be expanded from January 2017", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Dynamic programming", "Category:Optimal control", "Category:Optimization algorithms and methods", "Category:Pages using div col with small parameter", "Category:Short description matches Wikidata", "Category:Stochastic optimization"]
references: 0
last_modified: 2024-12-21T13:10:57Z
---

# Stochastic dynamic programming

## Summary

Originally introduced by Richard E. Bellman in (Bellman 1957), stochastic dynamic programming is a technique for modelling and solving problems of decision making under uncertainty. Closely related to stochastic programming and dynamic programming, stochastic dynamic programming represents the problem under scrutiny in the form of a Bellman equation. The aim is to compute a policy prescribing how to act optimally in the face of uncertainty.

## Full Content

Originally introduced by Richard E. Bellman in (Bellman 1957), stochastic dynamic programming is a technique for modelling and solving problems of decision making under uncertainty. Closely related to stochastic programming and dynamic programming, stochastic dynamic programming represents the problem under scrutiny in the form of a Bellman equation. The aim is to compute a policy prescribing how to act optimally in the face of uncertainty.

A motivating example: Gambling game
A gambler has $2, she is allowed to play a game of chance 4 times and her goal is to maximize her probability of ending up with a least $6. If the gambler bets $
  
    
      
        b
      
    
    {\displaystyle b}
  
 on a play of the game, then with probability 0.4 she wins the game, recoup the initial bet, and she increases her capital position by $
  
    
      
        b
      
    
    {\displaystyle b}
  
; with probability 0.6, she loses the bet amount $
  
    
      
        b
      
    
    {\displaystyle b}
  
; all plays are pairwise independent. On any play of the game, the gambler may not bet more money than she has available at the beginning of that play.
Stochastic dynamic programming can be employed to model this problem and determine a betting strategy that, for instance, maximizes the gambler's probability of attaining a wealth of at least $6 by the end of the betting horizon.
Note that if there is no limit to the number of games that can be played, the problem becomes a variant of the well known St. Petersburg paradox.

Formal background
Consider a discrete system defined on 
  
    
      
        n
      
    
    {\displaystyle n}
  
 stages in which each stage 
  
    
      
        t
        =
        1
        ,
        …
        ,
        n
      
    
    {\displaystyle t=1,\ldots ,n}
  
 is characterized by

an initial state 
  
    
      
        
          s
          
            t
          
        
        ∈
        
          S
          
            t
          
        
      
    
    {\displaystyle s_{t}\in S_{t}}
  
, where 
  
    
      
        
          S
          
            t
          
        
      
    
    {\displaystyle S_{t}}
  
 is the set of feasible states at the beginning of stage 
  
    
      
        t
      
    
    {\displaystyle t}
  
;
a decision variable 
  
    
      
        
          x
          
            t
          
        
        ∈
        
          X
          
            t
          
        
      
    
    {\displaystyle x_{t}\in X_{t}}
  
, where 
  
    
      
        
          X
          
            t
          
        
      
    
    {\displaystyle X_{t}}
  
 is the set of feasible actions at stage 
  
    
      
        t
      
    
    {\displaystyle t}
  
 – note that 
  
    
      
        
          X
          
            t
          
        
      
    
    {\displaystyle X_{t}}
  
 may be a function of the initial state 
  
    
      
        
          s
          
            t
          
        
      
    
    {\displaystyle s_{t}}
  
;
an immediate cost/reward function 
  
    
      
        
          p
          
            t
          
        
        (
        
          s
          
            t
          
        
        ,
        
          x
          
            t
          
        
        )
      
    
    {\displaystyle p_{t}(s_{t},x_{t})}
  
, representing the cost/reward at stage 
  
    
      
        t
      
    
    {\displaystyle t}
  
 if 
  
    
      
        
          s
          
            t
          
        
      
    
    {\displaystyle s_{t}}
  
 is the initial state and 
  
    
      
        
          x
          
            t
          
        
      
    
    {\displaystyle x_{t}}
  
 the action selected;
a state transition function 
  
    
      
        
          g
          
            t
          
        
        (
        
          s
          
            t
          
        
        ,
        
          x
          
            t
          
        
        )
      
    
    {\displaystyle g_{t}(s_{t},x_{t})}
  
 that leads the system towards state 
  
    
      
        
          s
          
            t
            +
            1
          
        
        =
        
          g
          
            t
          
        
        (
        
          s
          
            t
          
        
        ,
        
          x
          
            t
          
        
        )
      
    
    {\displaystyle s_{t+1}=g_{t}(s_{t},x_{t})}
  
.
Let 
  
    
      
        
          f
          
            t
          
        
        (
        
          s
          
            t
          
        
        )
      
    
    {\displaystyle f_{t}(s_{t})}
  
 represent the optimal cost/reward obtained by following an optimal policy over stages 
  
    
      
        t
        ,
        t
        +
        1
        ,
        …
        ,
        n
      
    
    {\displaystyle t,t+1,\ldots ,n}
  
. Without loss of generality in what follow we will consider a reward maximisation setting. In deterministic dynamic programming one usually deals with functional equations taking the following structure

  
    
      
        
          f
          
            t
          
        
        (
        
          s
          
            t
          
        
        )
        =
        
          max
          
            
              x
              
                t
              
            
            ∈
            
              X
              
                t
              
            
          
        
        {
        
          p
          
            t
          
        
        (
        
          s
          
            t
          
        
        ,
        
          x
          
            t
          
        
        )
        +
        
          f
          
            t
            +
            1
          
        
        (
        
          s
          
            t
            +
            1
          
        
        )
        }
      
    
    {\displaystyle f_{t}(s_{t})=\max _{x_{t}\in X_{t}}\{p_{t}(s_{t},x_{t})+f_{t+1}(s_{t+1})\}}
  

where 
  
    
      
        
          s
          
            t
            +
            1
          
        
        =
        
          g
          
            t
          
        
        (
        
          s
          
            t
          
        
        ,
        
          x
          
            t
          
        
        )
      
    
    {\displaystyle s_{t+1}=g_{t}(s_{t},x_{t})}
  
 and the boundary condition of the system is 

  
    
      
        
          f
          
            n
          
        
        (
        
          s
          
            n
          
        
        )
        =
        
          max
          
            
              x
              
                n
              
            
            ∈
            
              X
              
                n
              
            
          
        
        {
        
          p
          
            n
          
        
        (
        
          s
          
            n
          
        
        ,
        
          x
          
            n
          
        
        )
        }
        .
      
    
    {\displaystyle f_{n}(s_{n})=\max _{x_{n}\in X_{n}}\{p_{n}(s_{n},x_{n})\}.}
  

The aim is to determine the set of optimal actions that maximise 
  
    
      
        
          f
          
            1
          
        
        (
        
          s
          
            1
          
        
        )
      
    
    {\displaystyle f_{1}(s_{1})}
  
. Given the current state 
  
    
      
        
          s
          
            t
          
        
      
    
    {\displaystyle s_{t}}
  
 and the current action 
  
    
      
        
          x
          
            t
          
        
      
    
    {\displaystyle x_{t}}
  
, we know with certainty the reward secured during the current stage and – thanks to the state transition function 
  
    
      
        
          g
          
            t
          
        
      
    
    {\displaystyle g_{t}}
  
 – the future state towards which the system transitions.
In practice, however, even if we know the state of the system at the beginning of the current stage as well as the decision taken, the state of the system at the beginning of the next stage and the current period reward are often random variables that can be observed only at the end of the current stage.
Stochastic dynamic programming deals with problems in which the current period reward and/or the next period state are random, i.e. with multi-stage stochastic systems. The decision maker's goal is to maximise expected (discounted) reward over a given planning horizon.
In their most general form, stochastic dynamic programs deal with functional equations taking the following structure

  
    
      
        
          f
          
            t
          
        
        (
        
          s
          
            t
          
        
        )
        =
        
          max
          
            
              x
              
                t
              
            
            ∈
            
              X
              
                t
              
            
            (
            
              s
              
                t
              
            
            )
          
        
        
          {
          
            (
            
              expected reward during stage 
            
            t
            ∣
            
              s
              
                t
              
            
            ,
            
              x
              
                t
              
            
            )
            +
            α
            
              ∑
              
                
                  s
                  
                    t
                    +
                    1
                  
                
              
            
            Pr
            (
            
              s
              
                t
                +
                1
              
            
            ∣
            
              s
              
                t
              
            
            ,
            
              x
              
                t
              
            
            )
            
              f
              
                t
                +
                1
              
            
            (
            
              s
              
                t
                +
                1
              
            
            )
          
          }
        
      
    
    {\displaystyle f_{t}(s_{t})=\max _{x_{t}\in X_{t}(s_{t})}\left\{({\text{expected reward during stage }}t\mid s_{t},x_{t})+\alpha \sum _{s_{t+1}}\Pr(s_{t+1}\mid s_{t},x_{t})f_{t+1}(s_{t+1})\right\}}
  

where

  
    
      
        
          f
          
            t
          
        
        (
        
          s
          
            t
          
        
        )
      
    
    {\displaystyle f_{t}(s_{t})}
  
 is the maximum expected reward that can be attained during stages 
  
    
      
        t
        ,
        t
        +
        1
        ,
        …
        ,
        n
      
    
    {\displaystyle t,t+1,\ldots ,n}
  
, given state 
  
    
      
        
          s
          
            t
          
        
      
    
    {\displaystyle s_{t}}
  
 at the beginning of stage 
  
    
      
        t
      
    
    {\displaystyle t}
  
;

  
    
      
        
          x
          
            t
          
        
      
    
    {\displaystyle x_{t}}
  
 belongs to the set 
  
    
      
        
          X
          
            t
          
        
        (
        
          s
          
            t
          
        
        )
      
    
    {\displaystyle X_{t}(s_{t})}
  
 of feasible actions at stage 
  
    
      
        t
      
    
    {\displaystyle t}
  
 given initial state 
  
    
      
        
          s
          
            t
          
        
      
    
    {\displaystyle s_{t}}
  
;

  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 is the discount factor;

  
    
      
        Pr
        (
        
          s
          
            t
            +
            1
          
        
        ∣
        
          s
          
            t
          
        
        ,
        
          x
          
            t
          
        
        )
      
    
    {\displaystyle \Pr(s_{t+1}\mid s_{t},x_{t})}
  
 is the conditional probability that the state at the end of stage 
  
    
      
        t
      
    
    {\displaystyle t}
  
 is 
  
    
      
        
          s
          
            t
            +
            1
          
        
      
    
    {\displaystyle s_{t+1}}
  
 given current state 
  
    
      
        
          s
          
            t
          
        
      
    
    {\displaystyle s_{t}}
  
 and selected action 
  
    
      
        
          x
          
            t
          
        
      
    
    {\displaystyle x_{t}}
  
.
Markov decision processes represent a special class of stochastic dynamic programs in which the underlying stochastic process is a stationary process that features the Markov property.

Gambling game as a stochastic dynamic program
Gambling game can be formulated as a Stochastic Dynamic Program as follows: there are 
  
    
      
        n
        =
        4
      
    
    {\displaystyle n=4}
  
 games (i.e. stages) in the planning horizon

the state 
  
    
      
        s
      
    
    {\displaystyle s}
  
 in period 
  
    
      
        t
      
    
    {\displaystyle t}
  
 represents the initial wealth at the beginning of period 
  
    
      
        t
      
    
    {\displaystyle t}
  
;
the action given state 
  
    
      
        s
      
    
    {\displaystyle s}
  
 in period 
  
    
      
        t
      
    
    {\displaystyle t}
  
 is the bet amount 
  
    
      
        b
      
    
    {\displaystyle b}
  
;
the transition probability 
  
    
      
        
          p
          
            i
            ,
            j
          
          
            a
          
        
      
    
    {\displaystyle p_{i,j}^{a}}
  
 from state 
  
    
      
        i
      
    
    {\displaystyle i}
  
 to state 
  
    
      
        j
      
    
    {\displaystyle j}
  
 when action 
  
    
      
        a
      
    
    {\displaystyle a}
  
 is taken in state 
  
    
      
        i
      
    
    {\displaystyle i}
  
 is easily derived from the probability of winning (0.4) or losing (0.6) a game.
Let 
  
    
      
        
          f
          
            t
          
        
        (
        s
        )
      
    
    {\displaystyle f_{t}(s)}
  
 be the probability that, by the end of game 4, the gambler has at least $6, given that she has $
  
    
      
        s
      
    
    {\displaystyle s}
  
 at the beginning of game 
  
    
      
        t
      
    
    {\displaystyle t}
  
. 

the immediate profit incurred if action 
  
    
      
        b
      
    
    {\displaystyle b}
  
 is taken in state 
  
    
      
        s
      
    
    {\displaystyle s}
  
 is given by the expected value 
  
    
      
        
          p
          
            t
          
        
        (
        s
        ,
        b
        )
        =
        0.4
        
          f
          
            t
            +
            1
          
        
        (
        s
        +
        b
        )
        +
        0.6
        
          f
          
            t
            +
            1
          
        
        (
        s
        −
        b
        )
      
    
    {\displaystyle p_{t}(s,b)=0.4f_{t+1}(s+b)+0.6f_{t+1}(s-b)}
  
.
To derive the functional equation, define 
  
    
      
        
          b
          
            t
          
        
        (
        s
        )
      
    
    {\displaystyle b_{t}(s)}
  
 as a bet that attains 
  
    
      
        
          f
          
            t
          
        
        (
        s
        )
      
    
    {\displaystyle f_{t}(s)}
  
, then at the beginning of game 
  
    
      
        t
        =
        4
      
    
    {\displaystyle t=4}
  

if 
  
    
      
        s
        <
        3
      
    
    {\displaystyle s<3}
  
 it is impossible to attain the goal, i.e. 
  
    
      
        
          f
          
            4
          
        
        (
        s
        )
        =
        0
      
    
    {\displaystyle f_{4}(s)=0}
  
 for 
  
    
      
        s
        <
        3
      
    
    {\displaystyle s<3}
  
;
if 
  
    
      
        s
        ≥
        6
      
    
    {\displaystyle s\geq 6}
  
 the goal is attained, i.e. 
  
    
      
        
          f
          
            4
          
        
        (
        s
        )
        =
        1
      
    
    {\displaystyle f_{4}(s)=1}
  
 for 
  
    
      
        s
        ≥
        6
      
    
    {\displaystyle s\geq 6}
  
;
if 
  
    
      
        3
        ≤
        s
        ≤
        5
      
    
    {\displaystyle 3\leq s\leq 5}
  
 the gambler should bet enough to attain the goal, i.e. 
  
    
      
        
          f
          
            4
          
        
        (
        s
        )
        =
        0.4
      
    
    {\displaystyle f_{4}(s)=0.4}
  
 for 
  
    
      
        3
        ≤
        s
        ≤
        5
      
    
    {\displaystyle 3\leq s\leq 5}
  
.
For 
  
    
      
        t
        <
        4
      
    
    {\displaystyle t<4}
  
 the functional equation is 
  
    
      
        
          f
          
            t
          
        
        (
        s
        )
        =
        
          max
          
            
              b
              
                t
              
            
            (
            s
            )
          
        
        {
        0.4
        
          f
          
            t
            +
            1
          
        
        (
        s
        +
        b
        )
        +
        0.6
        
          f
          
            t
            +
            1
          
        
        (
        s
        −
        b
        )
        }
      
    
    {\displaystyle f_{t}(s)=\max _{b_{t}(s)}\{0.4f_{t+1}(s+b)+0.6f_{t+1}(s-b)\}}
  
, where 
  
    
      
        
          b
          
            t
          
        
        (
        s
        )
      
    
    {\displaystyle b_{t}(s)}
  
 ranges in 
  
    
      
        0
        ,
        .
        .
        .
        ,
        s
      
    
    {\displaystyle 0,...,s}
  
; the aim is to find 
  
    
      
        
          f
          
            1
          
        
        (
        2
        )
      
    
    {\displaystyle f_{1}(2)}
  
.
Given the functional equation, an optimal betting policy can be obtained via forward recursion or backward recursion algorithms, as outlined below.

Solution methods
Stochastic dynamic programs can be solved to optimality by using backward recursion or forward recursion algorithms. Memoization is typically employed to enhance performance. However, like deterministic dynamic programming also its stochastic variant suffers from the curse of dimensionality. For this reason approximate solution methods are typically employed in practical applications.

Backward recursion
Given a bounded state space, backward recursion (Bertsekas 2000) begins by tabulating 
  
    
      
        
          f
          
            n
          
        
        (
        k
        )
      
    
    {\displaystyle f_{n}(k)}
  
 for every possible state 
  
    
      
        k
      
    
    {\displaystyle k}
  
 belonging to the final stage 
  
    
      
        n
      
    
    {\displaystyle n}
  
. Once these values are tabulated, together with the associated optimal state-dependent actions 
  
    
      
        
          x
          
            n
          
        
        (
        k
        )
      
    
    {\displaystyle x_{n}(k)}
  
, it is possible to move to stage 
  
    
      
        n
        −
        1
      
    
    {\displaystyle n-1}
  
 and tabulate 
  
    
      
        
          f
          
            n
            −
            1
          
        
        (
        k
        )
      
    
    {\displaystyle f_{n-1}(k)}
  
 for all possible states belonging to the stage 
  
    
      
        n
        −
        1
      
    
    {\displaystyle n-1}
  
. The process continues by considering in a backward fashion all remaining stages up to the first one. Once this tabulation process is complete, 
  
    
      
        
          f
          
            1
          
        
        (
        s
        )
      
    
    {\displaystyle f_{1}(s)}
  
 – the value of an optimal policy given initial state 
  
    
      
        s
      
    
    {\displaystyle s}
  
 – as well as the associated optimal action 
  
    
      
        
          x
          
            1
          
        
        (
        s
        )
      
    
    {\displaystyle x_{1}(s)}
  
 can be easily retrieved from the table. Since the computation proceeds in a backward fashion, it is clear that backward recursion may lead to computation of a large number of states that are not necessary for the computation of 
  
    
      
        
          f
          
            1
          
        
        (
        s
        )
      
    
    {\displaystyle f_{1}(s)}
  
.

Example: Gambling game
Forward recursion
Given the initial state 
  
    
      
        s
      
    
    {\displaystyle s}
  
 of the system at the beginning of period 1, forward recursion (Bertsekas 2000) computes 
  
    
      
        
          f
          
            1
          
        
        (
        s
        )
      
    
    {\displaystyle f_{1}(s)}
  
 by progressively expanding the functional equation (forward pass). This involves recursive calls for all 
  
    
      
        
          f
          
            t
            +
            1
          
        
        (
        ⋅
        )
        ,
        
          f
          
            t
            +
            2
          
        
        (
        ⋅
        )
        ,
        …
      
    
    {\displaystyle f_{t+1}(\cdot ),f_{t+2}(\cdot ),\ldots }
  
 that are necessary for computing a given 
  
    
      
        
          f
          
            t
          
        
        (
        ⋅
        )
      
    
    {\displaystyle f_{t}(\cdot )}
  
. The value of an optimal policy and its structure are then retrieved via a (backward pass) in which these suspended recursive calls are resolved. A key difference from backward recursion is the fact that 
  
    
      
        
          f
          
            t
          
        
      
    
    {\displaystyle f_{t}}
  
 is computed only for states that are relevant for the computation of 
  
    
      
        
          f
          
            1
          
        
        (
        s
        )
      
    
    {\displaystyle f_{1}(s)}
  
.  Memoization is employed to avoid recomputation of states that have been already considered.

Example: Gambling game
We shall illustrate forward recursion in the context of the Gambling game instance previously discussed. We begin the forward pass by considering

  
    
      
        
          f
          
            1
          
        
        (
        2
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 1,2,3,4
                  
                
              
              
                
                  0
                
                
                  0.4
                  
                    f
                    
                      2
                    
                  
                  (
                  2
                  +
                  0
                  )
                  +
                  0.6
                  
                    f
                    
                      2
                    
                  
                  (
                  2
                  −
                  0
                  )
                
              
              
                
                  1
                
                
                  0.4
                  
                    f
                    
                      2
                    
                  
                  (
                  2
                  +
                  1
                  )
                  +
                  0.6
                  
                    f
                    
                      2
                    
                  
                  (
                  2
                  −
                  1
                  )
                
              
              
                
                  2
                
                
                  0.4
                  
                    f
                    
                      2
                    
                  
                  (
                  2
                  +
                  2
                  )
                  +
                  0.6
                  
                    f
                    
                      2
                    
                  
                  (
                  2
                  −
                  2
                  )
                
              
            
          
          
        
      
    
    {\displaystyle f_{1}(2)=\min \left\{{\begin{array}{rr}b&{\text{success probability in periods 1,2,3,4}}\\\hline 0&0.4f_{2}(2+0)+0.6f_{2}(2-0)\\1&0.4f_{2}(2+1)+0.6f_{2}(2-1)\\2&0.4f_{2}(2+2)+0.6f_{2}(2-2)\\\end{array}}\right.}
  

At this point we have not computed yet 
  
    
      
        
          f
          
            2
          
        
        (
        4
        )
        ,
        
          f
          
            2
          
        
        (
        3
        )
        ,
        
          f
          
            2
          
        
        (
        2
        )
        ,
        
          f
          
            2
          
        
        (
        1
        )
        ,
        
          f
          
            2
          
        
        (
        0
        )
      
    
    {\displaystyle f_{2}(4),f_{2}(3),f_{2}(2),f_{2}(1),f_{2}(0)}
  
, which are needed to compute 
  
    
      
        
          f
          
            1
          
        
        (
        2
        )
      
    
    {\displaystyle f_{1}(2)}
  
; we proceed and compute these items. Note that 
  
    
      
        
          f
          
            2
          
        
        (
        2
        +
        0
        )
        =
        
          f
          
            2
          
        
        (
        2
        −
        0
        )
        =
        
          f
          
            2
          
        
        (
        2
        )
      
    
    {\displaystyle f_{2}(2+0)=f_{2}(2-0)=f_{2}(2)}
  
, therefore one can leverage memoization and perform the necessary computations only once.

Computation of 
  
    
      
        
          f
          
            2
          
        
        (
        4
        )
        ,
        
          f
          
            2
          
        
        (
        3
        )
        ,
        
          f
          
            2
          
        
        (
        2
        )
        ,
        
          f
          
            2
          
        
        (
        1
        )
        ,
        
          f
          
            2
          
        
        (
        0
        )
      
    
    {\displaystyle f_{2}(4),f_{2}(3),f_{2}(2),f_{2}(1),f_{2}(0)}
  

  
    
      
        
          f
          
            2
          
        
        (
        0
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 2,3,4
                  
                
              
              
                
                  0
                
                
                  0.4
                  
                    f
                    
                      3
                    
                  
                  (
                  0
                  +
                  0
                  )
                  +
                  0.6
                  
                    f
                    
                      3
                    
                  
                  (
                  0
                  −
                  0
                  )
                
              
            
          
          
        
      
    
    {\displaystyle f_{2}(0)=\min \left\{{\begin{array}{rr}b&{\text{success probability in periods 2,3,4}}\\\hline 0&0.4f_{3}(0+0)+0.6f_{3}(0-0)\\\end{array}}\right.}
  

  
    
      
        
          f
          
            2
          
        
        (
        1
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 2,3,4
                  
                
              
              
                
                  0
                
                
                  0.4
                  
                    f
                    
                      3
                    
                  
                  (
                  1
                  +
                  0
                  )
                  +
                  0.6
                  
                    f
                    
                      3
                    
                  
                  (
                  1
                  −
                  0
                  )
                
              
              
                
                  1
                
                
                  0.4
                  
                    f
                    
                      3
                    
                  
                  (
                  1
                  +
                  1
                  )
                  +
                  0.6
                  
                    f
                    
                      3
                    
                  
                  (
                  1
                  −
                  1
                  )
                
              
            
          
          
        
      
    
    {\displaystyle f_{2}(1)=\min \left\{{\begin{array}{rr}b&{\text{success probability in periods 2,3,4}}\\\hline 0&0.4f_{3}(1+0)+0.6f_{3}(1-0)\\1&0.4f_{3}(1+1)+0.6f_{3}(1-1)\\\end{array}}\right.}
  

  
    
      
        
          f
          
            2
          
        
        (
        2
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 2,3,4
                  
                
              
              
                
                  0
                
                
                  0.4
                  
                    f
                    
                      3
                    
                  
                  (
                  2
                  +
                  0
                  )
                  +
                  0.6
                  
                    f
                    
                      3
                    
                  
                  (
                  2
                  −
                  0
                  )
                
              
              
                
                  1
                
                
                  0.4
                  
                    f
                    
                      3
                    
                  
                  (
                  2
                  +
                  1
                  )
                  +
                  0.6
                  
                    f
                    
                      3
                    
                  
                  (
                  2
                  −
                  1
                  )
                
              
              
                
                  2
                
                
                  0.4
                  
                    f
                    
                      3
                    
                  
                  (
                  2
                  +
                  2
                  )
                  +
                  0.6
                  
                    f
                    
                      3
                    
                  
                  (
                  2
                  −
                  2
                  )
                
              
            
          
          
        
      
    
    {\displaystyle f_{2}(2)=\min \left\{{\begin{array}{rr}b&{\text{success probability in periods 2,3,4}}\\\hline 0&0.4f_{3}(2+0)+0.6f_{3}(2-0)\\1&0.4f_{3}(2+1)+0.6f_{3}(2-1)\\2&0.4f_{3}(2+2)+0.6f_{3}(2-2)\\\end{array}}\right.}
  

  
    
      
        
          f
          
            2
          
        
        (
        3
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 2,3,4
                  
                
              
              
                
                  0
                
                
                  0.4
                  
                    f
                    
                      3
                    
                  
                  (
                  3
                  +
                  0
                  )
                  +
                  0.6
                  
                    f
                    
                      3
                    
                  
                  (
                  3
                  −
                  0
                  )
                
              
              
                
                  1
                
                
                  0.4
                  
                    f
                    
                      3
                    
                  
                  (
                  3
                  +
                  1
                  )
                  +
                  0.6
                  
                    f
                    
                      3
                    
                  
                  (
                  3
                  −
                  1
                  )
                
              
              
                
                  2
                
                
                  0.4
                  
                    f
                    
                      3
                    
                  
                  (
                  3
                  +
                  2
                  )
                  +
                  0.6
                  
                    f
                    
                      3
                    
                  
                  (
                  3
                  −
                  2
                  )
                
              
              
                
                  3
                
                
                  0.4
                  
                    f
                    
                      3
                    
                  
                  (
                  3
                  +
                  3
                  )
                  +
                  0.6
                  
                    f
                    
                      3
                    
                  
                  (
                  3
                  −
                  3
                  )
                
              
            
          
          
        
      
    
    {\displaystyle f_{2}(3)=\min \left\{{\begin{array}{rr}b&{\text{success probability in periods 2,3,4}}\\\hline 0&0.4f_{3}(3+0)+0.6f_{3}(3-0)\\1&0.4f_{3}(3+1)+0.6f_{3}(3-1)\\2&0.4f_{3}(3+2)+0.6f_{3}(3-2)\\3&0.4f_{3}(3+3)+0.6f_{3}(3-3)\\\end{array}}\right.}
  

  
    
      
        
          f
          
            2
          
        
        (
        4
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 2,3,4
                  
                
              
              
                
                  0
                
                
                  0.4
                  
                    f
                    
                      3
                    
                  
                  (
                  4
                  +
                  0
                  )
                  +
                  0.6
                  
                    f
                    
                      3
                    
                  
                  (
                  4
                  −
                  0
                  )
                
              
              
                
                  1
                
                
                  0.4
                  
                    f
                    
                      3
                    
                  
                  (
                  4
                  +
                  1
                  )
                  +
                  0.6
                  
                    f
                    
                      3
                    
                  
                  (
                  4
                  −
                  1
                  )
                
              
              
                
                  2
                
                
                  0.4
                  
                    f
                    
                      3
                    
                  
                  (
                  4
                  +
                  2
                  )
                  +
                  0.6
                  
                    f
                    
                      3
                    
                  
                  (
                  4
                  −
                  2
                  )
                
              
            
          
          
        
      
    
    {\displaystyle f_{2}(4)=\min \left\{{\begin{array}{rr}b&{\text{success probability in periods 2,3,4}}\\\hline 0&0.4f_{3}(4+0)+0.6f_{3}(4-0)\\1&0.4f_{3}(4+1)+0.6f_{3}(4-1)\\2&0.4f_{3}(4+2)+0.6f_{3}(4-2)\end{array}}\right.}
  

We have now computed 
  
    
      
        
          f
          
            2
          
        
        (
        k
        )
      
    
    {\displaystyle f_{2}(k)}
  
 for all 
  
    
      
        k
      
    
    {\displaystyle k}
  
 that are needed to compute 
  
    
      
        
          f
          
            1
          
        
        (
        2
        )
      
    
    {\displaystyle f_{1}(2)}
  
. However, this has led to additional suspended recursions involving 
  
    
      
        
          f
          
            3
          
        
        (
        4
        )
        ,
        
          f
          
            3
          
        
        (
        3
        )
        ,
        
          f
          
            3
          
        
        (
        2
        )
        ,
        
          f
          
            3
          
        
        (
        1
        )
        ,
        
          f
          
            3
          
        
        (
        0
        )
      
    
    {\displaystyle f_{3}(4),f_{3}(3),f_{3}(2),f_{3}(1),f_{3}(0)}
  
. We proceed and compute these values.

Computation of 
  
    
      
        
          f
          
            3
          
        
        (
        4
        )
        ,
        
          f
          
            3
          
        
        (
        3
        )
        ,
        
          f
          
            3
          
        
        (
        2
        )
        ,
        
          f
          
            3
          
        
        (
        1
        )
        ,
        
          f
          
            3
          
        
        (
        0
        )
      
    
    {\displaystyle f_{3}(4),f_{3}(3),f_{3}(2),f_{3}(1),f_{3}(0)}
  

  
    
      
        
          f
          
            3
          
        
        (
        0
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 3,4
                  
                
              
              
                
                  0
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  0
                  +
                  0
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  0
                  −
                  0
                  )
                
              
            
          
          
        
      
    
    {\displaystyle f_{3}(0)=\min \left\{{\begin{array}{rr}b&{\text{success probability in periods 3,4}}\\\hline 0&0.4f_{4}(0+0)+0.6f_{4}(0-0)\\\end{array}}\right.}
  

  
    
      
        
          f
          
            3
          
        
        (
        1
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 3,4
                  
                
              
              
                
                  0
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  1
                  +
                  0
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  1
                  −
                  0
                  )
                
              
              
                
                  1
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  1
                  +
                  1
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  1
                  −
                  1
                  )
                
              
            
          
          
        
      
    
    {\displaystyle f_{3}(1)=\min \left\{{\begin{array}{rr}b&{\text{success probability in periods 3,4}}\\\hline 0&0.4f_{4}(1+0)+0.6f_{4}(1-0)\\1&0.4f_{4}(1+1)+0.6f_{4}(1-1)\\\end{array}}\right.}
  

  
    
      
        
          f
          
            3
          
        
        (
        2
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 3,4
                  
                
              
              
                
                  0
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  2
                  +
                  0
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  2
                  −
                  0
                  )
                
              
              
                
                  1
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  2
                  +
                  1
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  2
                  −
                  1
                  )
                
              
              
                
                  2
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  2
                  +
                  2
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  2
                  −
                  2
                  )
                
              
            
          
          
        
      
    
    {\displaystyle f_{3}(2)=\min \left\{{\begin{array}{rr}b&{\text{success probability in periods 3,4}}\\\hline 0&0.4f_{4}(2+0)+0.6f_{4}(2-0)\\1&0.4f_{4}(2+1)+0.6f_{4}(2-1)\\2&0.4f_{4}(2+2)+0.6f_{4}(2-2)\\\end{array}}\right.}
  

  
    
      
        
          f
          
            3
          
        
        (
        3
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 3,4
                  
                
              
              
                
                  0
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  3
                  +
                  0
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  3
                  −
                  0
                  )
                
              
              
                
                  1
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  3
                  +
                  1
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  3
                  −
                  1
                  )
                
              
              
                
                  2
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  3
                  +
                  2
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  3
                  −
                  2
                  )
                
              
              
                
                  3
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  3
                  +
                  3
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  3
                  −
                  3
                  )
                
              
            
          
          
        
      
    
    {\displaystyle f_{3}(3)=\min \left\{{\begin{array}{rr}b&{\text{success probability in periods 3,4}}\\\hline 0&0.4f_{4}(3+0)+0.6f_{4}(3-0)\\1&0.4f_{4}(3+1)+0.6f_{4}(3-1)\\2&0.4f_{4}(3+2)+0.6f_{4}(3-2)\\3&0.4f_{4}(3+3)+0.6f_{4}(3-3)\\\end{array}}\right.}
  

  
    
      
        
          f
          
            3
          
        
        (
        4
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 3,4
                  
                
              
              
                
                  0
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  4
                  +
                  0
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  4
                  −
                  0
                  )
                
              
              
                
                  1
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  4
                  +
                  1
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  4
                  −
                  1
                  )
                
              
              
                
                  2
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  4
                  +
                  2
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  4
                  −
                  2
                  )
                
              
            
          
          
        
      
    
    {\displaystyle f_{3}(4)=\min \left\{{\begin{array}{rr}b&{\text{success probability in periods 3,4}}\\\hline 0&0.4f_{4}(4+0)+0.6f_{4}(4-0)\\1&0.4f_{4}(4+1)+0.6f_{4}(4-1)\\2&0.4f_{4}(4+2)+0.6f_{4}(4-2)\end{array}}\right.}
  

  
    
      
        
          f
          
            3
          
        
        (
        5
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 3,4
                  
                
              
              
                
                  0
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  5
                  +
                  0
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  5
                  −
                  0
                  )
                
              
              
                
                  1
                
                
                  0.4
                  
                    f
                    
                      4
                    
                  
                  (
                  5
                  +
                  1
                  )
                  +
                  0.6
                  
                    f
                    
                      4
                    
                  
                  (
                  5
                  −
                  1
                  )
                
              
            
          
          
        
      
    
    {\displaystyle f_{3}(5)=\min \left\{{\begin{array}{rr}b&{\text{success probability in periods 3,4}}\\\hline 0&0.4f_{4}(5+0)+0.6f_{4}(5-0)\\1&0.4f_{4}(5+1)+0.6f_{4}(5-1)\end{array}}\right.}
  

Since stage 4 is the last stage in our system, 
  
    
      
        
          f
          
            4
          
        
        (
        ⋅
        )
      
    
    {\displaystyle f_{4}(\cdot )}
  
 represent boundary conditions that are easily computed as follows.

Boundary conditions

  
    
      
        
          
            
              
                
                  f
                  
                    4
                  
                
                (
                0
                )
                =
                0
              
              
                
                  b
                  
                    4
                  
                
                (
                0
                )
                =
                0
              
            
            
              
                
                  f
                  
                    4
                  
                
                (
                1
                )
                =
                0
              
              
                
                  b
                  
                    4
                  
                
                (
                1
                )
                =
                {
                0
                ,
                1
                }
              
            
            
              
                
                  f
                  
                    4
                  
                
                (
                2
                )
                =
                0
              
              
                
                  b
                  
                    4
                  
                
                (
                2
                )
                =
                {
                0
                ,
                1
                ,
                2
                }
              
            
            
              
                
                  f
                  
                    4
                  
                
                (
                3
                )
                =
                0.4
              
              
                
                  b
                  
                    4
                  
                
                (
                3
                )
                =
                {
                3
                }
              
            
            
              
                
                  f
                  
                    4
                  
                
                (
                4
                )
                =
                0.4
              
              
                
                  b
                  
                    4
                  
                
                (
                4
                )
                =
                {
                2
                ,
                3
                ,
                4
                }
              
            
            
              
                
                  f
                  
                    4
                  
                
                (
                5
                )
                =
                0.4
              
              
                
                  b
                  
                    4
                  
                
                (
                5
                )
                =
                {
                1
                ,
                2
                ,
                3
                ,
                4
                ,
                5
                }
              
            
            
              
                
                  f
                  
                    4
                  
                
                (
                d
                )
                =
                1
              
              
                
                  b
                  
                    4
                  
                
                (
                d
                )
                =
                {
                0
                ,
                …
                ,
                d
                −
                6
                }
                
                   for 
                
                d
                ≥
                6
              
            
          
        
      
    
    {\displaystyle {\begin{array}{ll}f_{4}(0)=0&b_{4}(0)=0\\f_{4}(1)=0&b_{4}(1)=\{0,1\}\\f_{4}(2)=0&b_{4}(2)=\{0,1,2\}\\f_{4}(3)=0.4&b_{4}(3)=\{3\}\\f_{4}(4)=0.4&b_{4}(4)=\{2,3,4\}\\f_{4}(5)=0.4&b_{4}(5)=\{1,2,3,4,5\}\\f_{4}(d)=1&b_{4}(d)=\{0,\ldots ,d-6\}{\text{ for }}d\geq 6\end{array}}}
  

At this point it is possible to proceed and recover the optimal policy and its value via a backward pass involving, at first, stage 3

Backward pass involving 
  
    
      
        
          f
          
            3
          
        
        (
        ⋅
        )
      
    
    {\displaystyle f_{3}(\cdot )}
  

  
    
      
        
          f
          
            3
          
        
        (
        0
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 3,4
                  
                
              
              
                
                  0
                
                
                  0.4
                  (
                  0
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0
                
              
            
          
          
        
      
    
    {\displaystyle f_{3}(0)=\min \left\{{\begin{array}{rr}b&{\text{success probability in periods 3,4}}\\\hline 0&0.4(0)+0.6(0)=0\\\end{array}}\right.}
  

  
    
      
        
          f
          
            3
          
        
        (
        1
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 3,4
                  
                
                
                  
                    
                      max
                    
                  
                
              
              
                
                  0
                
                
                  0.4
                  (
                  0
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0
                
                
                  ←
                  
                    b
                    
                      3
                    
                  
                  (
                  1
                  )
                  =
                  0
                
              
              
                
                  1
                
                
                  0.4
                  (
                  0
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0
                
                
                  ←
                  
                    b
                    
                      3
                    
                  
                  (
                  1
                  )
                  =
                  1
                
              
            
          
          
        
      
    
    {\displaystyle f_{3}(1)=\min \left\{{\begin{array}{rrr}b&{\text{success probability in periods 3,4}}&{\mbox{max}}\\\hline 0&0.4(0)+0.6(0)=0&\leftarrow b_{3}(1)=0\\1&0.4(0)+0.6(0)=0&\leftarrow b_{3}(1)=1\\\end{array}}\right.}
  

  
    
      
        
          f
          
            3
          
        
        (
        2
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 3,4
                  
                
                
                  
                    
                      max
                    
                  
                
              
              
                
                  0
                
                
                  0.4
                  (
                  0
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0
                
              
              
                
                  1
                
                
                  0.4
                  (
                  0.4
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0.16
                
                
                  ←
                  
                    b
                    
                      3
                    
                  
                  (
                  2
                  )
                  =
                  1
                
              
              
                
                  2
                
                
                  0.4
                  (
                  0.4
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0.16
                
                
                  ←
                  
                    b
                    
                      3
                    
                  
                  (
                  2
                  )
                  =
                  2
                
              
            
          
          
        
      
    
    {\displaystyle f_{3}(2)=\min \left\{{\begin{array}{rrr}b&{\text{success probability in periods 3,4}}&{\mbox{max}}\\\hline 0&0.4(0)+0.6(0)=0\\1&0.4(0.4)+0.6(0)=0.16&\leftarrow b_{3}(2)=1\\2&0.4(0.4)+0.6(0)=0.16&\leftarrow b_{3}(2)=2\\\end{array}}\right.}
  

  
    
      
        
          f
          
            3
          
        
        (
        3
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 3,4
                  
                
                
                  
                    
                      max
                    
                  
                
              
              
                
                  0
                
                
                  0.4
                  (
                  0.4
                  )
                  +
                  0.6
                  (
                  0.4
                  )
                  =
                  0.4
                
                
                  ←
                  
                    b
                    
                      3
                    
                  
                  (
                  3
                  )
                  =
                  0
                
              
              
                
                  1
                
                
                  0.4
                  (
                  0.4
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0.16
                
              
              
                
                  2
                
                
                  0.4
                  (
                  0.4
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0.16
                
              
              
                
                  3
                
                
                  0.4
                  (
                  1
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0.4
                
                
                  ←
                  
                    b
                    
                      3
                    
                  
                  (
                  3
                  )
                  =
                  3
                
              
            
          
          
        
      
    
    {\displaystyle f_{3}(3)=\min \left\{{\begin{array}{rrr}b&{\text{success probability in periods 3,4}}&{\mbox{max}}\\\hline 0&0.4(0.4)+0.6(0.4)=0.4&\leftarrow b_{3}(3)=0\\1&0.4(0.4)+0.6(0)=0.16\\2&0.4(0.4)+0.6(0)=0.16\\3&0.4(1)+0.6(0)=0.4&\leftarrow b_{3}(3)=3\\\end{array}}\right.}
  

  
    
      
        
          f
          
            3
          
        
        (
        4
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 3,4
                  
                
                
                  
                    
                      max
                    
                  
                
              
              
                
                  0
                
                
                  0.4
                  (
                  0.4
                  )
                  +
                  0.6
                  (
                  0.4
                  )
                  =
                  0.4
                
                
                  ←
                  
                    b
                    
                      3
                    
                  
                  (
                  4
                  )
                  =
                  0
                
              
              
                
                  1
                
                
                  0.4
                  (
                  0.4
                  )
                  +
                  0.6
                  (
                  0.4
                  )
                  =
                  0.4
                
                
                  ←
                  
                    b
                    
                      3
                    
                  
                  (
                  4
                  )
                  =
                  1
                
              
              
                
                  2
                
                
                  0.4
                  (
                  1
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0.4
                
                
                  ←
                  
                    b
                    
                      3
                    
                  
                  (
                  4
                  )
                  =
                  2
                
              
            
          
          
        
      
    
    {\displaystyle f_{3}(4)=\min \left\{{\begin{array}{rrr}b&{\text{success probability in periods 3,4}}&{\mbox{max}}\\\hline 0&0.4(0.4)+0.6(0.4)=0.4&\leftarrow b_{3}(4)=0\\1&0.4(0.4)+0.6(0.4)=0.4&\leftarrow b_{3}(4)=1\\2&0.4(1)+0.6(0)=0.4&\leftarrow b_{3}(4)=2\\\end{array}}\right.}
  

  
    
      
        
          f
          
            3
          
        
        (
        5
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 3,4
                  
                
                
                  
                    
                      max
                    
                  
                
              
              
                
                  0
                
                
                  0.4
                  (
                  0.4
                  )
                  +
                  0.6
                  (
                  0.4
                  )
                  =
                  0.4
                
              
              
                
                  1
                
                
                  0.4
                  (
                  1
                  )
                  +
                  0.6
                  (
                  0.4
                  )
                  =
                  0.64
                
                
                  ←
                  
                    b
                    
                      3
                    
                  
                  (
                  5
                  )
                  =
                  1
                
              
            
          
          
        
      
    
    {\displaystyle f_{3}(5)=\min \left\{{\begin{array}{rrr}b&{\text{success probability in periods 3,4}}&{\mbox{max}}\\\hline 0&0.4(0.4)+0.6(0.4)=0.4\\1&0.4(1)+0.6(0.4)=0.64&\leftarrow b_{3}(5)=1\\\end{array}}\right.}
  

and, then, stage 2.

Backward pass involving 
  
    
      
        
          f
          
            2
          
        
        (
        ⋅
        )
      
    
    {\displaystyle f_{2}(\cdot )}
  

  
    
      
        
          f
          
            2
          
        
        (
        0
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 2,3,4
                  
                
                
                  
                    
                      max
                    
                  
                
              
              
                
                  0
                
                
                  0.4
                  (
                  0
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0
                
                
                  ←
                  
                    b
                    
                      2
                    
                  
                  (
                  0
                  )
                  =
                  0
                
              
            
          
          
        
      
    
    {\displaystyle f_{2}(0)=\min \left\{{\begin{array}{rrr}b&{\text{success probability in periods 2,3,4}}&{\mbox{max}}\\\hline 0&0.4(0)+0.6(0)=0&\leftarrow b_{2}(0)=0\\\end{array}}\right.}
  

  
    
      
        
          f
          
            2
          
        
        (
        1
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 2,3,4
                  
                
                
                  
                    
                      max
                    
                  
                
              
              
                
                  0
                
                
                  0.4
                  (
                  0
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0
                
              
              
                
                  1
                
                
                  0.4
                  (
                  0.16
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0.064
                
                
                  ←
                  
                    b
                    
                      2
                    
                  
                  (
                  1
                  )
                  =
                  1
                
              
            
          
          
        
      
    
    {\displaystyle f_{2}(1)=\min \left\{{\begin{array}{rrr}b&{\text{success probability in periods 2,3,4}}&{\mbox{max}}\\\hline 0&0.4(0)+0.6(0)=0\\1&0.4(0.16)+0.6(0)=0.064&\leftarrow b_{2}(1)=1\\\end{array}}\right.}
  

  
    
      
        
          f
          
            2
          
        
        (
        2
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 2,3,4
                  
                
                
                  
                    
                      max
                    
                  
                
              
              
                
                  0
                
                
                  0.4
                  (
                  0.16
                  )
                  +
                  0.6
                  (
                  0.16
                  )
                  =
                  0.16
                
                
                  ←
                  
                    b
                    
                      2
                    
                  
                  (
                  2
                  )
                  =
                  0
                
              
              
                
                  1
                
                
                  0.4
                  (
                  0.4
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0.16
                
                
                  ←
                  
                    b
                    
                      2
                    
                  
                  (
                  2
                  )
                  =
                  1
                
              
              
                
                  2
                
                
                  0.4
                  (
                  0.4
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0.16
                
                
                  ←
                  
                    b
                    
                      2
                    
                  
                  (
                  2
                  )
                  =
                  2
                
              
            
          
          
        
      
    
    {\displaystyle f_{2}(2)=\min \left\{{\begin{array}{rrr}b&{\text{success probability in periods 2,3,4}}&{\mbox{max}}\\\hline 0&0.4(0.16)+0.6(0.16)=0.16&\leftarrow b_{2}(2)=0\\1&0.4(0.4)+0.6(0)=0.16&\leftarrow b_{2}(2)=1\\2&0.4(0.4)+0.6(0)=0.16&\leftarrow b_{2}(2)=2\\\end{array}}\right.}
  

  
    
      
        
          f
          
            2
          
        
        (
        3
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 2,3,4
                  
                
                
                  
                    
                      max
                    
                  
                
              
              
                
                  0
                
                
                  0.4
                  (
                  0.4
                  )
                  +
                  0.6
                  (
                  0.4
                  )
                  =
                  0.4
                
                
                  ←
                  
                    b
                    
                      2
                    
                  
                  (
                  3
                  )
                  =
                  0
                
              
              
                
                  1
                
                
                  0.4
                  (
                  0.4
                  )
                  +
                  0.6
                  (
                  0.16
                  )
                  =
                  0.256
                
              
              
                
                  2
                
                
                  0.4
                  (
                  0.64
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0.256
                
              
              
                
                  3
                
                
                  0.4
                  (
                  1
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0.4
                
                
                  ←
                  
                    b
                    
                      2
                    
                  
                  (
                  3
                  )
                  =
                  3
                
              
            
          
          
        
      
    
    {\displaystyle f_{2}(3)=\min \left\{{\begin{array}{rrr}b&{\text{success probability in periods 2,3,4}}&{\mbox{max}}\\\hline 0&0.4(0.4)+0.6(0.4)=0.4&\leftarrow b_{2}(3)=0\\1&0.4(0.4)+0.6(0.16)=0.256\\2&0.4(0.64)+0.6(0)=0.256\\3&0.4(1)+0.6(0)=0.4&\leftarrow b_{2}(3)=3\\\end{array}}\right.}
  

  
    
      
        
          f
          
            2
          
        
        (
        4
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 2,3,4
                  
                
                
                  
                    
                      max
                    
                  
                
              
              
                
                  0
                
                
                  0.4
                  (
                  0.4
                  )
                  +
                  0.6
                  (
                  0.4
                  )
                  =
                  0.4
                
              
              
                
                  1
                
                
                  0.4
                  (
                  0.64
                  )
                  +
                  0.6
                  (
                  0.4
                  )
                  =
                  0.496
                
                
                  ←
                  
                    b
                    
                      2
                    
                  
                  (
                  4
                  )
                  =
                  1
                
              
              
                
                  2
                
                
                  0.4
                  (
                  1
                  )
                  +
                  0.6
                  (
                  0.16
                  )
                  =
                  0.496
                
                
                  ←
                  
                    b
                    
                      2
                    
                  
                  (
                  4
                  )
                  =
                  2
                
              
            
          
          
        
      
    
    {\displaystyle f_{2}(4)=\min \left\{{\begin{array}{rrr}b&{\text{success probability in periods 2,3,4}}&{\mbox{max}}\\\hline 0&0.4(0.4)+0.6(0.4)=0.4\\1&0.4(0.64)+0.6(0.4)=0.496&\leftarrow b_{2}(4)=1\\2&0.4(1)+0.6(0.16)=0.496&\leftarrow b_{2}(4)=2\\\end{array}}\right.}
  

We finally recover the value 
  
    
      
        
          f
          
            1
          
        
        (
        2
        )
      
    
    {\displaystyle f_{1}(2)}
  
 of an optimal policy

  
    
      
        
          f
          
            1
          
        
        (
        2
        )
        =
        min
        
          {
          
            
              
                
                  b
                
                
                  
                    success probability in periods 1,2,3,4
                  
                
                
                  
                    
                      max
                    
                  
                
              
              
                
                  0
                
                
                  0.4
                  (
                  0.16
                  )
                  +
                  0.6
                  (
                  0.16
                  )
                  =
                  0.16
                
              
              
                
                  1
                
                
                  0.4
                  (
                  0.4
                  )
                  +
                  0.6
                  (
                  0.064
                  )
                  =
                  0.1984
                
                
                  ←
                  
                    b
                    
                      1
                    
                  
                  (
                  2
                  )
                  =
                  1
                
              
              
                
                  2
                
                
                  0.4
                  (
                  0.496
                  )
                  +
                  0.6
                  (
                  0
                  )
                  =
                  0.1984
                
                
                  ←
                  
                    b
                    
                      1
                    
                  
                  (
                  2
                  )
                  =
                  2
                
              
            
          
          
        
      
    
    {\displaystyle f_{1}(2)=\min \left\{{\begin{array}{rrr}b&{\text{success probability in periods 1,2,3,4}}&{\mbox{max}}\\\hline 0&0.4(0.16)+0.6(0.16)=0.16\\1&0.4(0.4)+0.6(0.064)=0.1984&\leftarrow b_{1}(2)=1\\2&0.4(0.496)+0.6(0)=0.1984&\leftarrow b_{1}(2)=2\\\end{array}}\right.}
  

This is the optimal policy that has been previously illustrated. Note that there are multiple optimal policies leading to the same optimal value 
  
    
      
        
          f
          
            1
          
        
        (
        2
        )
        =
        0.1984
      
    
    {\displaystyle f_{1}(2)=0.1984}
  
; for instance, in the first game one may either bet $1 or $2.
Python implementation. The one that follows is a complete Python implementation of this example.

Java implementation. GamblersRuin.java is a standalone Java 8 implementation of the above example.

Approximate dynamic programming
An introduction to approximate dynamic programming is provided by (Powell 2009).

Further reading
Bellman, R. (1957), Dynamic Programming, Princeton University Press, ISBN 978-0-486-42809-3. Dover paperback edition (2003).
Ross, S. M.; Bimbaum, Z. W.; Lukacs, E. (1983), Introduction to Stochastic Dynamic Programming, Elsevier, ISBN 978-0-12-598420-1.
Bertsekas, D. P. (2000), Dynamic Programming and Optimal Control (2nd ed.), Athena Scientific, ISBN 978-1-886529-09-0. In two volumes.
Powell, W. B. (2009), "What you should know about approximate dynamic programming", Naval Research Logistics, 56 (1): 239–249, CiteSeerX 10.1.1.150.1854, doi:10.1002/nav.20347, S2CID 7134937

See also


== References ==
