# Hidden Markov model

## Metadata
- **Last Updated:** 2024-12-14 17:33:34 UTC
- **Original Article:** [Hidden Markov model](https://en.wikipedia.org/wiki/Hidden_Markov_model)
- **Language:** en
- **Page ID:** 98770

## Summary
A hidden Markov model (HMM) is a Markov model in which the observations are dependent on a latent (or hidden) Markov process (referred to as 
  
    
      
        X
      
    
    {\displaystyle X}
  
). An HMM requires that there be an observable process 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
 whose outcomes depend on the outcomes of 
  
    
      
        X
      
    
    {\displaystyle X}
  
 in a known way. Since 
  
    
      
        X
      
    
    {\displaystyle X}
  
 cannot be observed directly, the goal is to learn about state of 
  
    
      
        X
      
    
    {\displaystyle X}
  
 by observing 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
. By definition of being a Markov model, an HMM has an additional requirement that the outcome of 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
 at time 
  
    
      
        t
        =
        
          t
          
            0
          
        
      
    
    {\displaystyle t=t_{0}}
  
 must be "influenced" exclusively by the outcome of 
  
    
      
        X
      
    
    {\displaystyle X}
  
 at 
  
    
      
        t
        =
        
          t
          
            0
          
        
      
    
    {\displaystyle t=t_{0}}
  
 and that the outcomes of 
  
    
      
        X
      
    
    {\displaystyle X}
  
 and 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
 at 
  
    
      
        t
        <
        
          t
          
            0
          
        
      
    
    {\displaystyle t<t_{0}}
  
 must be conditionally independent of 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
 at 
  
    
      
        t
        =
        
          t
          
            0
          
        
      
    
    {\displaystyle t=t_{0}}
  
 given 
  
    
      
        X
      
    
    {\displaystyle X}
  
 at time 
  
    
      
        t
        =
        
          t
          
            0
          
        
      
    
    {\displaystyle t=t_{0}}
  
. Estimation of the parameters in an HMM can be performed using maximum likelihood estimation. For linear chain HMMs, the Baum–Welch algorithm can be used to estimate parameters.
Hidden Markov models are known for their applications to thermodynamics, statistical mechanics, physics, chemistry, economics, finance, signal processing, information theory, pattern recognition—such as speech, handwriting, gesture recognition, part-of-speech tagging, musical score following, partial discharges and bioinformatics.

## Categories
This article belongs to the following categories:

- Category:All articles with dead external links
- Category:Articles with dead external links from July 2022
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Bioinformatics
- Category:Commons category link is on Wikidata
- Category:Good articles
- Category:Hidden Markov models
- Category:Markov models
- Category:Pages containing links to subscription-only content
- Category:Short description matches Wikidata
- Category:Webarchive template wayback links

## Table of Contents

- Definition
- Examples
- Structural architecture
- Inference
- Learning
- Applications
- History
- Extensions
- Measure theory
- See also
- References
- External links

## Content

A hidden Markov model (HMM) is a Markov model in which the observations are dependent on a latent (or hidden) Markov process (referred to as 
  
    
      
        X
      
    
    {\displaystyle X}
  
). An HMM requires that there be an observable process 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
 whose outcomes depend on the outcomes of 
  
    
      
        X
      
    
    {\displaystyle X}
  
 in a known way. Since 
  
    
      
        X
      
    
    {\displaystyle X}
  
 cannot be observed directly, the goal is to learn about state of 
  
    
      
        X
      
    
    {\displaystyle X}
  
 by observing 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
. By definition of being a Markov model, an HMM has an additional requirement that the outcome of 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
 at time 
  
    
      
        t
        =
        
          t
          
            0
          
        
      
    
    {\displaystyle t=t_{0}}
  
 must be "influenced" exclusively by the outcome of 
  
    
      
        X
      
    
    {\displaystyle X}
  
 at 
  
    
      
        t
        =
        
          t
          
            0
          
        
      
    
    {\displaystyle t=t_{0}}
  
 and that the outcomes of 
  
    
      
        X
      
    
    {\displaystyle X}
  
 and 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
 at 
  
    
      
        t
        <
        
          t
          
            0
          
        
      
    
    {\displaystyle t<t_{0}}
  
 must be conditionally independent of 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
 at 
  
    
      
        t
        =
        
          t
          
            0
          
        
      
    
    {\displaystyle t=t_{0}}
  
 given 
  
    
      
        X
      
    
    {\displaystyle X}
  
 at time 
  
    
      
        t
        =
        
          t
          
            0
          
        
      
    
    {\displaystyle t=t_{0}}
  
. Estimation of the parameters in an HMM can be performed using maximum likelihood estimation. For linear chain HMMs, the Baum–Welch algorithm can be used to estimate parameters.
Hidden Markov models are known for their applications to thermodynamics, statistical mechanics, physics, chemistry, economics, finance, signal processing, information theory, pattern recognition—such as speech, handwriting, gesture recognition, part-of-speech tagging, musical score following, partial discharges and bioinformatics.

Definition
Let 
  
    
      
        
          X
          
            n
          
        
      
    
    {\displaystyle X_{n}}
  
 and 
  
    
      
        
          Y
          
            n
          
        
      
    
    {\displaystyle Y_{n}}
  
 be discrete-time stochastic processes and 
  
    
      
        n
        ≥
        1
      
    
    {\displaystyle n\geq 1}
  
. The pair 
  
    
      
        (
        
          X
          
            n
          
        
        ,
        
          Y
          
            n
          
        
        )
      
    
    {\displaystyle (X_{n},Y_{n})}
  
 is a hidden Markov model if

  
    
      
        
          X
          
            n
          
        
      
    
    {\displaystyle X_{n}}
  
 is a Markov process whose behavior is not directly observable ("hidden");

  
    
      
        
          
            P
          
        
        ⁡
        
          
            (
          
        
        
          Y
          
            n
          
        
        ∈
        A
         
        
          
            |
          
        
         
        
          X
          
            1
          
        
        =
        
          x
          
            1
          
        
        ,
        …
        ,
        
          X
          
            n
          
        
        =
        
          x
          
            n
          
        
        
          
            )
          
        
        =
        
          
            P
          
        
        ⁡
        
          
            (
          
        
        
          Y
          
            n
          
        
        ∈
        A
         
        
          
            |
          
        
         
        
          X
          
            n
          
        
        =
        
          x
          
            n
          
        
        
          
            )
          
        
      
    
    {\displaystyle \operatorname {\mathbf {P} } {\bigl (}Y_{n}\in A\ {\bigl |}\ X_{1}=x_{1},\ldots ,X_{n}=x_{n}{\bigr )}=\operatorname {\mathbf {P} } {\bigl (}Y_{n}\in A\ {\bigl |}\ X_{n}=x_{n}{\bigr )}}
  
,
for every 
  
    
      
        n
        ≥
        1
      
    
    {\displaystyle n\geq 1}
  
, 
  
    
      
        
          x
          
            1
          
        
        ,
        …
        ,
        
          x
          
            n
          
        
      
    
    {\displaystyle x_{1},\ldots ,x_{n}}
  
, and every Borel set 
  
    
      
        A
      
    
    {\displaystyle A}
  
.
Let 
  
    
      
        
          X
          
            t
          
        
      
    
    {\displaystyle X_{t}}
  
 and 
  
    
      
        
          Y
          
            t
          
        
      
    
    {\displaystyle Y_{t}}
  
 be continuous-time stochastic processes. The pair 
  
    
      
        (
        
          X
          
            t
          
        
        ,
        
          Y
          
            t
          
        
        )
      
    
    {\displaystyle (X_{t},Y_{t})}
  
 is a hidden Markov model if

  
    
      
        
          X
          
            t
          
        
      
    
    {\displaystyle X_{t}}
  
 is a Markov process whose behavior is not directly observable ("hidden");

  
    
      
        
          
            P
          
        
        ⁡
        (
        
          Y
          
            
              t
              
                0
              
            
          
        
        ∈
        A
        ∣
        {
        
          X
          
            t
          
        
        ∈
        
          B
          
            t
          
        
        
          }
          
            t
            ≤
            
              t
              
                0
              
            
          
        
        )
        =
        
          
            P
          
        
        ⁡
        (
        
          Y
          
            
              t
              
                0
              
            
          
        
        ∈
        A
        ∣
        
          X
          
            
              t
              
                0
              
            
          
        
        ∈
        
          B
          
            
              t
              
                0
              
            
          
        
        )
      
    
    {\displaystyle \operatorname {\mathbf {P} } (Y_{t_{0}}\in A\mid \{X_{t}\in B_{t}\}_{t\leq t_{0}})=\operatorname {\mathbf {P} } (Y_{t_{0}}\in A\mid X_{t_{0}}\in B_{t_{0}})}
  
,
for every 
  
    
      
        
          t
          
            0
          
        
      
    
    {\displaystyle t_{0}}
  
, every Borel set 
  
    
      
        A
      
    
    {\displaystyle A}
  
, and every family of Borel sets 
  
    
      
        {
        
          B
          
            t
          
        
        
          }
          
            t
            ≤
            
              t
              
                0
              
            
          
        
      
    
    {\displaystyle \{B_{t}\}_{t\leq t_{0}}}
  
.

Terminology
The states of the process 
  
    
      
        
          X
          
            n
          
        
      
    
    {\displaystyle X_{n}}
  
 (resp. 
  
    
      
        
          X
          
            t
          
        
        )
      
    
    {\displaystyle X_{t})}
  
 are called hidden states, and 
  
    
      
        
          
            P
          
        
        ⁡
        
          
            (
          
        
        
          Y
          
            n
          
        
        ∈
        A
        ∣
        
          X
          
            n
          
        
        =
        
          x
          
            n
          
        
        
          
            )
          
        
      
    
    {\displaystyle \operatorname {\mathbf {P} } {\bigl (}Y_{n}\in A\mid X_{n}=x_{n}{\bigr )}}
  
 (resp. 
  
    
      
        
          
            P
          
        
        ⁡
        
          
            (
          
        
        
          Y
          
            t
          
        
        ∈
        A
        ∣
        
          X
          
            t
          
        
        ∈
        
          B
          
            t
          
        
        
          
            )
          
        
        )
      
    
    {\displaystyle \operatorname {\mathbf {P} } {\bigl (}Y_{t}\in A\mid X_{t}\in B_{t}{\bigr )})}
  
 is called emission probability or output probability.

Examples
Drawing balls from hidden urns
In its discrete form, a hidden Markov process can be visualized as a generalization of the urn problem with replacement (where each item from the urn is returned to the original urn before the next step). Consider this example: in a room that is not visible to an observer there is a genie. The room contains urns X1, X2, X3, ... each of which contains a known mix of balls, with each ball having a unique label y1, y2, y3, ... . The genie chooses an urn in that room and randomly draws a ball from that urn. It then puts the ball onto a conveyor belt, where the observer can observe the sequence of the balls but not the sequence of urns from which they were drawn. The genie has some procedure to choose urns; the choice of the urn for the n-th ball depends only upon a random number and the choice of the urn for the (n − 1)-th ball. The choice of urn does not directly depend on the urns chosen before this single previous urn; therefore, this is called a Markov process. It can be described by the upper part of Figure 1.
The Markov process cannot be observed, only the sequence of labeled balls, thus this arrangement is called a hidden Markov process. This is illustrated by the lower part of the diagram shown in Figure 1, where one can see that balls y1, y2, y3, y4 can be drawn at each state. Even if the observer knows the composition of the urns and has just observed a sequence of three balls, e.g. y1, y2 and y3 on the conveyor belt, the observer still cannot be sure which urn (i.e., at which state) the genie has drawn the third ball from. However, the observer can work out other information, such as the likelihood that the third ball came from each of the urns.

Weather guessing game
Consider two friends, Alice and Bob, who live far apart from each other and who talk together daily over the telephone about what they did that day. Bob is only interested in three activities: walking in the park, shopping, and cleaning his apartment. The choice of what to do is determined exclusively by the weather on a given day. Alice has no definite information about the weather, but she knows general trends. Based on what Bob tells her he did each day, Alice tries to guess what the weather must have been like.
Alice believes that the weather operates as a discrete Markov chain. There are two states, "Rainy" and "Sunny", but she cannot observe them directly, that is, they are hidden from her. On each day, there is a certain chance that Bob will perform one of the following activities, depending on the weather: "walk", "shop", or "clean". Since Bob tells Alice about his activities, those are the observations. The entire system is that of a hidden Markov model (HMM).
Alice knows the general weather trends in the area, and what Bob likes to do on average. In other words, the parameters of the HMM are known. They can be represented as follows in Python:

In this piece of code, start_probability represents Alice's belief about which state the HMM is in when Bob first calls her (all she knows is that it tends to be rainy on average). The particular probability distribution used here is not the equilibrium one, which is (given the transition probabilities) approximately {'Rainy': 0.57, 'Sunny': 0.43}. The transition_probability represents the change of the weather in the underlying Markov chain. In this example, there is only a 30% chance that tomorrow will be sunny if today is rainy. The emission_probability represents how likely Bob is to perform a certain activity on each day. If it is rainy, there is a 50% chance that he is cleaning his apartment; if it is sunny, there is a 60% chance that he is outside for a walk.

A similar example is further elaborated in the Viterbi algorithm page.

Structural architecture
The diagram below shows the general architecture of an instantiated HMM. Each oval shape represents a random variable that can adopt any of a number of values. The random variable x(t) is the hidden state at time t (with the model from the above diagram, x(t) ∈ { x1, x2, x3 }). The random variable y(t) is the observation at time t (with y(t) ∈ { y1, y2, y3, y4 }). The arrows in the diagram (often called a trellis diagram) denote conditional dependencies.
From the diagram, it is clear that the conditional probability distribution of the hidden variable x(t) at time t, given the values of the hidden variable x at all times, depends only on the value of the hidden variable x(t − 1); the values at time t − 2 and before have no influence. This is called the Markov property. Similarly, the value of the observed variable y(t) depends on only the value of the hidden variable x(t) (both at time t).
In the standard type of hidden Markov model considered here, the state space of the hidden variables is discrete, while the observations themselves can either be discrete (typically generated from a categorical distribution) or continuous (typically from a Gaussian distribution). The parameters of a hidden Markov model are of two types, transition probabilities and emission probabilities (also known as output probabilities). The transition probabilities control the way the hidden state at time t is chosen given the hidden state at time 
  
    
      
        t
        −
        1
      
    
    {\displaystyle t-1}
  
.
The hidden state space is assumed to consist of one of N possible values, modelled as a categorical distribution. (See the section below on extensions for other possibilities.) This means that for each of the N possible states that a hidden variable at time t can be in, there is a transition probability from this state to each of the N possible states of the hidden variable at time 
  
    
      
        t
        +
        1
      
    
    {\displaystyle t+1}
  
, for a total of 
  
    
      
        
          N
          
            2
          
        
      
    
    {\displaystyle N^{2}}
  
 transition probabilities. The set of transition probabilities for transitions from any given state must sum to 1. Thus, the 
  
    
      
        N
        ×
        N
      
    
    {\displaystyle N\times N}
  
 matrix of transition probabilities is a Markov matrix. Because any transition probability can be determined once the others are known, there are a total of 
  
    
      
        N
        (
        N
        −
        1
        )
      
    
    {\displaystyle N(N-1)}
  
 transition parameters.
In addition, for each of the N possible states, there is a set of emission probabilities governing the distribution of the observed variable at a particular time given the state of the hidden variable at that time. The size of this set depends on the nature of the observed variable. For example, if the observed variable is discrete with M possible values, governed by a categorical distribution, there will be 
  
    
      
        M
        −
        1
      
    
    {\displaystyle M-1}
  
 separate parameters, for a total of 
  
    
      
        N
        (
        M
        −
        1
        )
      
    
    {\displaystyle N(M-1)}
  
 emission parameters over all hidden states. On the other hand, if the observed variable is an M-dimensional vector distributed according to an arbitrary multivariate Gaussian distribution, there will be M parameters controlling the means and 
  
    
      
        
          
            
              M
              (
              M
              +
              1
              )
            
            2
          
        
      
    
    {\displaystyle {\frac {M(M+1)}{2}}}
  
 parameters controlling the covariance matrix, for a total of 
  
    
      
        N
        
          (
          
            M
            +
            
              
                
                  M
                  (
                  M
                  +
                  1
                  )
                
                2
              
            
          
          )
        
        =
        
          
            
              N
              M
              (
              M
              +
              3
              )
            
            2
          
        
        =
        O
        (
        N
        
          M
          
            2
          
        
        )
      
    
    {\displaystyle N\left(M+{\frac {M(M+1)}{2}}\right)={\frac {NM(M+3)}{2}}=O(NM^{2})}
  
 emission parameters. (In such a case, unless the value of M is small, it may be more practical to restrict the nature of the covariances between individual elements of the observation vector, e.g. by assuming that the elements are independent of each other, or less restrictively, are independent of all but a fixed number of adjacent elements.)

Inference
Several inference problems are associated with hidden Markov models, as outlined below.

Probability of an observed sequence
The task is to compute in a best way, given the parameters of the model, the probability of a particular output sequence. This requires summation over all possible state sequences:
The probability of observing a sequence

  
    
      
        Y
        =
        y
        (
        0
        )
        ,
        y
        (
        1
        )
        ,
        …
        ,
        y
        (
        L
        −
        1
        )
      
    
    {\displaystyle Y=y(0),y(1),\dots ,y(L-1)}
  
,
of length L is given by

  
    
      
        P
        (
        Y
        )
        =
        
          ∑
          
            X
          
        
        P
        (
        Y
        ∣
        X
        )
        P
        (
        X
        )
      
    
    {\displaystyle P(Y)=\sum _{X}P(Y\mid X)P(X)}
  
,
where the sum runs over all possible hidden-node sequences

  
    
      
        X
        =
        x
        (
        0
        )
        ,
        x
        (
        1
        )
        ,
        …
        ,
        x
        (
        L
        −
        1
        )
      
    
    {\displaystyle X=x(0),x(1),\dots ,x(L-1)}
  
.
Applying the principle of dynamic programming, this problem, too, can be handled efficiently using the forward algorithm.

Probability of the latent variables
A number of related tasks ask about the probability of one or more of the latent variables, given the model's parameters and a sequence of observations 
  
    
      
        y
        (
        1
        )
        ,
        …
        ,
        y
        (
        t
        )
      
    
    {\displaystyle y(1),\dots ,y(t)}
  
.

Filtering
The task is to compute, given the model's parameters and a sequence of observations, the distribution over hidden states of the last latent variable at the end of the sequence, i.e. to compute 
  
    
      
        P
        (
        x
        (
        t
        )
         
        
          |
        
         
        y
        (
        1
        )
        ,
        …
        ,
        y
        (
        t
        )
        )
      
    
    {\displaystyle P(x(t)\ |\ y(1),\dots ,y(t))}
  
. This task is used when the sequence of latent variables is thought of as the underlying states that a process moves through at a sequence of points in time, with corresponding observations at each point. Then, it is natural to ask about the state of the process at the end.
This problem can be handled efficiently using the forward algorithm. An example is when the algorithm is applied to a Hidden Markov Network to determine 
  
    
      
        
          P
        
        
          
            (
          
        
        
          h
          
            t
          
        
         
        
          |
        
        
          v
          
            1
            :
            t
          
        
        
          
            )
          
        
      
    
    {\displaystyle \mathrm {P} {\big (}h_{t}\ |v_{1:t}{\big )}}
  
.

Smoothing
This is similar to filtering but asks about the distribution of a latent variable somewhere in the middle of a sequence, i.e. to compute 
  
    
      
        P
        (
        x
        (
        k
        )
         
        
          |
        
         
        y
        (
        1
        )
        ,
        …
        ,
        y
        (
        t
        )
        )
      
    
    {\displaystyle P(x(k)\ |\ y(1),\dots ,y(t))}
  
 for some 
  
    
      
        k
        <
        t
      
    
    {\displaystyle k<t}
  
. From the perspective described above, this can be thought of as the probability distribution over hidden states for a point in time k in the past, relative to time t.
The forward-backward algorithm is a good method for computing the smoothed values for all hidden state variables.

Most likely explanation
The task, unlike the previous two, asks about the joint probability of the entire sequence of hidden states that generated a particular sequence of observations (see illustration on the right). This task is generally applicable when HMM's are applied to different sorts of problems from those for which the tasks of filtering and smoothing are applicable. An example is part-of-speech tagging, where the hidden states represent the underlying parts of speech corresponding to an observed sequence of words. In this case, what is of interest is the entire sequence of parts of speech, rather than simply the part of speech for a single word, as filtering or smoothing would compute.
This task requires finding a maximum over all possible state sequences, and can be solved efficiently by the Viterbi algorithm.

Statistical significance
For some of the above problems, it may also be interesting to ask about statistical significance. What is the probability that a sequence drawn from some null distribution will have an HMM probability (in the case of the forward algorithm) or a maximum state sequence probability (in the case of the Viterbi algorithm) at least as large as that of a particular output sequence?  When an HMM is used to evaluate the relevance of a hypothesis for a particular output sequence, the statistical significance indicates the false positive rate associated with failing to reject the hypothesis for the output sequence.

Learning
The parameter learning task in HMMs is to find, given an output sequence or a set of such sequences, the best set of state transition and emission probabilities. The task is usually to derive the maximum likelihood estimate of the parameters of the HMM given the set of output sequences. No tractable algorithm is known for solving this problem exactly, but a local maximum likelihood can be derived efficiently using the Baum–Welch algorithm or the Baldi–Chauvin algorithm. The Baum–Welch algorithm is a special case of the expectation-maximization algorithm. 
If the HMMs are used for time series prediction, more sophisticated Bayesian inference methods, like Markov chain Monte Carlo (MCMC) sampling are proven to be favorable over finding a single maximum likelihood model both in terms of accuracy and stability. Since MCMC imposes significant computational burden, in cases where computational scalability is also of interest, one may alternatively resort to variational approximations to Bayesian inference, e.g. Indeed, approximate variational inference offers computational efficiency comparable to expectation-maximization, while yielding an accuracy profile only slightly inferior to exact MCMC-type Bayesian inference.

Applications
HMMs can be applied in many fields where the goal is to recover a data sequence that is not immediately observable (but other data that depend on the sequence are). Applications include:

Computational finance
Single-molecule kinetic analysis
Neuroscience
Cryptanalysis
Speech recognition, including Siri
Speech synthesis
Part-of-speech tagging
Document separation in scanning solutions
Machine translation
Partial discharge
Gene prediction
Handwriting recognition
Alignment of bio-sequences
Time series analysis
Activity recognition
Protein folding
Sequence classification
Metamorphic virus detection
Sequence motif discovery (DNA and proteins)
DNA hybridization kinetics
Chromatin state discovery
Transportation forecasting
Solar irradiance variability

History
Hidden Markov models were described in a series of statistical papers by Leonard E. Baum and other authors in the second half of the 1960s. One of the first applications of HMMs was speech recognition, starting in the mid-1970s. From the linguistics point of view, hidden Markov models are equivalent to stochastic regular grammar.
In the second half of the 1980s, HMMs began to be applied to the analysis of biological sequences, in particular DNA. Since then, they have become ubiquitous in the field of bioinformatics.

Extensions
General state spaces
In the hidden Markov models considered above, the state space of the hidden variables is discrete, while the observations themselves can either be discrete (typically generated from a categorical distribution) or continuous (typically from a Gaussian distribution). Hidden Markov models can also be generalized to allow continuous state spaces. Examples of such models are those where the Markov process over hidden variables is a linear dynamical system, with a linear relationship among related variables and where all hidden and observed variables follow a Gaussian distribution. In simple cases, such as the linear dynamical system just mentioned, exact inference is tractable (in this case, using the Kalman filter); however, in general, exact inference in HMMs with continuous latent variables is infeasible, and approximate methods must be used, such as the extended Kalman filter or the particle filter.
Nowadays, inference in hidden Markov models is performed in nonparametric settings, where the dependency structure enables  identifiability of the model and the learnability limits are still under exploration.

Bayesian modeling of the transitions probabilities
Hidden Markov models are generative models, in which the joint distribution of observations and hidden states, or equivalently both the prior distribution of hidden states (the transition probabilities) and conditional distribution of observations given states (the emission probabilities), is modeled. The above algorithms implicitly assume a uniform prior distribution over the transition probabilities. However, it is also possible to create hidden Markov models with other types of prior distributions. An obvious candidate, given the categorical distribution of the transition probabilities, is the Dirichlet distribution, which is the conjugate prior distribution of the categorical distribution. Typically, a symmetric Dirichlet distribution is chosen, reflecting ignorance about which states are inherently more likely than others. The single parameter of this distribution (termed the concentration parameter) controls the relative density or sparseness of the resulting transition matrix. A choice of 1 yields a uniform distribution. Values greater than 1 produce a dense matrix, in which the transition probabilities between pairs of states are likely to be nearly equal. Values less than 1 result in a sparse matrix in which, for each given source state, only a small number of destination states have non-negligible transition probabilities. It is also possible to use a two-level prior Dirichlet distribution, in which one Dirichlet distribution (the upper distribution) governs the parameters of another Dirichlet distribution (the lower distribution), which in turn governs the transition probabilities. The upper distribution governs the overall distribution of states, determining how likely each state is to occur; its concentration parameter determines the density or sparseness of states. Such a two-level prior distribution, where both concentration parameters are set to produce sparse distributions, might be useful for example in unsupervised part-of-speech tagging, where some parts of speech occur much more commonly than others; learning algorithms that assume a uniform prior distribution generally perform poorly on this task. The parameters of models of this sort, with non-uniform prior distributions, can be learned using Gibbs sampling or extended versions of the expectation-maximization algorithm.
An extension of the previously described hidden Markov models with Dirichlet priors uses a Dirichlet process in place of a Dirichlet distribution. This type of model allows for an unknown and potentially infinite number of states. It is common to use a two-level Dirichlet process, similar to the previously described model with two levels of Dirichlet distributions. Such a model is called a hierarchical Dirichlet process hidden Markov model, or HDP-HMM for short. It was originally described under the name "Infinite Hidden Markov Model" and was further formalized in "Hierarchical Dirichlet Processes".

Discriminative approach
A different type of extension uses a discriminative model in place of the generative model of standard HMMs. This type of model directly models the conditional distribution of the hidden states given the observations, rather than modeling the joint distribution. An example of this model is the so-called maximum entropy Markov model (MEMM), which models the conditional distribution of the states using logistic regression (also known as a "maximum entropy model"). The advantage of this type of model is that arbitrary features (i.e. functions) of the observations can be modeled, allowing domain-specific knowledge of the problem at hand to be injected into the model. Models of this sort are not limited to modeling direct dependencies between a hidden state and its associated observation; rather, features of nearby observations, of combinations of the associated observation and nearby observations, or in fact of arbitrary observations at any distance from a given hidden state can be included in the process used to determine the value of a hidden state. Furthermore, there is no need for these features to be statistically independent of each other, as would be the case if such features were used in a generative model. Finally, arbitrary features over pairs of adjacent hidden states can be used rather than simple transition probabilities. The disadvantages of such models are: (1) The types of prior distributions that can be placed on hidden states are severely limited; (2) It is not possible to predict the probability of seeing an arbitrary observation. This second limitation is often not an issue in practice, since many common usages of HMM's do not require such predictive probabilities.
A variant of the previously described discriminative model is the linear-chain conditional random field. This uses an undirected graphical model (aka Markov random field) rather than the directed graphical models of MEMM's and similar models. The advantage of this type of model is that it does not suffer from the so-called label bias problem of MEMM's, and thus may make more accurate predictions. The disadvantage is that training can be slower than for MEMM's.

Other extensions
Yet another variant is the factorial hidden Markov model, which allows for a single observation to be conditioned on the corresponding hidden variables of a set of 
  
    
      
        K
      
    
    {\displaystyle K}
  
 independent Markov chains, rather than a single Markov chain. It is equivalent to a single HMM, with 
  
    
      
        
          N
          
            K
          
        
      
    
    {\displaystyle N^{K}}
  
 states (assuming there are 
  
    
      
        N
      
    
    {\displaystyle N}
  
 states for each chain), and therefore, learning in such a model is difficult: for a sequence of length 
  
    
      
        T
      
    
    {\displaystyle T}
  
, a straightforward Viterbi algorithm has complexity 
  
    
      
        O
        (
        
          N
          
            2
            K
          
        
        
        T
        )
      
    
    {\displaystyle O(N^{2K}\,T)}
  
. To find an exact solution, a junction tree algorithm could be used, but it results in an 
  
    
      
        O
        (
        
          N
          
            K
            +
            1
          
        
        
        K
        
        T
        )
      
    
    {\displaystyle O(N^{K+1}\,K\,T)}
  
 complexity. In practice, approximate techniques, such as variational approaches, could be used.
All of the above models can be extended to allow for more distant dependencies among hidden states, e.g. allowing for a given state to be dependent on the previous two or three states rather than a single previous state; i.e. the transition probabilities are extended to encompass sets of three or four adjacent states (or in general 
  
    
      
        K
      
    
    {\displaystyle K}
  
 adjacent states). The disadvantage of such models is that dynamic-programming algorithms for training them have an 
  
    
      
        O
        (
        
          N
          
            K
          
        
        
        T
        )
      
    
    {\displaystyle O(N^{K}\,T)}
  
 running time, for 
  
    
      
        K
      
    
    {\displaystyle K}
  
 adjacent states and 
  
    
      
        T
      
    
    {\displaystyle T}
  
 total observations (i.e. a length-
  
    
      
        T
      
    
    {\displaystyle T}
  
 Markov chain). This extension has been widely used in bioinformatics, in the modeling of DNA sequences.
Another recent extension is the triplet Markov model, in which an auxiliary underlying process is added to model some data specificities. Many variants of this model have been proposed. One should also mention the interesting link that has been established between the theory of evidence and the triplet Markov models and which allows to fuse data in Markovian context and to model nonstationary data. Alternative multi-stream data fusion strategies have also been proposed in recent literature, e.g.,
Finally, a different rationale towards addressing the problem of modeling nonstationary data by means of hidden Markov models was suggested in 2012. It consists in employing a small recurrent neural network (RNN), specifically a reservoir network, to capture the evolution of the temporal dynamics in the observed data. This information, encoded in the form of a high-dimensional vector, is used as a conditioning variable of the HMM state transition probabilities. Under such a setup, eventually is obtained a nonstationary HMM, the transition probabilities of which evolve over time in a manner that is inferred from the data, in contrast to some unrealistic ad-hoc model of temporal evolution.
In 2023, two innovative algorithms were introduced for the Hidden Markov Model. These algorithms enable the computation of the posterior distribution of the HMM without the necessity of explicitly modeling the joint distribution, utilizing only the conditional distributions. Unlike traditional methods such as the Forward-Backward and Viterbi algorithms, which require knowledge of the joint law of the HMM and can be computationally intensive to learn, the Discriminative Forward-Backward and Discriminative Viterbi algorithms circumvent the need for the observation's law. This breakthrough allows the HMM to be applied as a discriminative model, offering a more efficient and versatile approach to leveraging Hidden Markov Models in various applications.
The model suitable in the context of longitudinal data is named latent Markov model. The basic version of this model has been extended to include individual covariates, random effects and to model more complex data structures such as multilevel data. A complete overview of the latent Markov models, with special attention to the model assumptions and  to their practical use is provided in

Measure theory
Given a Markov transition matrix and an invariant distribution on the states, a probability measure can be imposed on the set of subshifts. For example, consider the Markov chain given on the left on the states 
  
    
      
        A
        ,
        
          B
          
            1
          
        
        ,
        
          B
          
            2
          
        
      
    
    {\displaystyle A,B_{1},B_{2}}
  
, with invariant distribution 
  
    
      
        π
        =
        (
        2
        
          /
        
        7
        ,
        4
        
          /
        
        7
        ,
        1
        
          /
        
        7
        )
      
    
    {\displaystyle \pi =(2/7,4/7,1/7)}
  
. By ignoring the distinction between 
  
    
      
        
          B
          
            1
          
        
        ,
        
          B
          
            2
          
        
      
    
    {\displaystyle B_{1},B_{2}}
  
, this space of subshifts is projected on 
  
    
      
        A
        ,
        
          B
          
            1
          
        
        ,
        
          B
          
            2
          
        
      
    
    {\displaystyle A,B_{1},B_{2}}
  
 into another space of subshifts on 
  
    
      
        A
        ,
        B
      
    
    {\displaystyle A,B}
  
, and this projection also projects the probability measure down to a probability measure on the subshifts on 
  
    
      
        A
        ,
        B
      
    
    {\displaystyle A,B}
  
.
The curious thing is that the probability measure on the subshifts on 
  
    
      
        A
        ,
        B
      
    
    {\displaystyle A,B}
  
 is not created by a Markov chain on 
  
    
      
        A
        ,
        B
      
    
    {\displaystyle A,B}
  
, not even multiple orders. Intuitively, this is because if one observes a long sequence of 
  
    
      
        
          B
          
            n
          
        
      
    
    {\displaystyle B^{n}}
  
, then one would become increasingly sure that the 
  
    
      
        P
        r
        (
        A
        
          |
        
        
          B
          
            n
          
        
        )
        →
        
          
            2
            3
          
        
      
    
    {\displaystyle Pr(A|B^{n})\to {\frac {2}{3}}}
  
, meaning that the observable part of the system can be affected by something infinitely in the past.
Conversely, there exists a space of subshifts on 6 symbols, projected to subshifts on 2 symbols, such that any Markov measure on the smaller subshift has a preimage measure that is not Markov of any order (example 2.6).

See also
References
External links
Concepts
Teif, V. B.; Rippe, K. (2010). "Statistical–mechanical lattice models for protein–DNA binding in chromatin". J. Phys.: Condens. Matter. 22 (41): 414105. arXiv:1004.5514. Bibcode:2010JPCM...22O4105T. doi:10.1088/0953-8984/22/41/414105. PMID 21386588. S2CID 103345.
A Revealing Introduction to Hidden Markov Models by Mark Stamp, San Jose State University.
Fitting HMM's with expectation-maximization – complete derivation
A step-by-step tutorial on HMMs Archived 2017-08-13 at the Wayback Machine (University of Leeds)
Hidden Markov Models (an exposition using basic mathematics)
Hidden Markov Models (by Narada Warakagoda)
Hidden Markov Models: Fundamentals and Applications Part 1, Part 2 (by V. Petrushin)
Lecture on a Spreadsheet by Jason Eisner, Video and interactive spreadsheet

## Archive Info
- **Archived on:** 2024-12-15 21:04:42 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 41030 bytes
- **Word Count:** 4873 words
