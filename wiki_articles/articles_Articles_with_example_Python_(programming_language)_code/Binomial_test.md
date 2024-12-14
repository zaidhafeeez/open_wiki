# Binomial test

## Article Metadata

- **Last Updated:** 2024-12-14T19:33:56.140876+00:00
- **Original Article:** [Binomial test](https://en.wikipedia.org/wiki/Binomial_test)
- **Language:** en
- **Page ID:** 935655

## Summary

Binomial test is an exact test of the statistical significance of deviations from a theoretically expected distribution of observations into two categories using sample data.

## Categories

- Category:All articles needing additional references
- Category:Articles needing additional references from November 2016
- Category:Articles with example Java code
- Category:Articles with example MATLAB/Octave code
- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with short description
- Category:Short description is different from Wikidata
- Category:Statistical tests

## Table of Contents

- Usage
- Common use
- Large samples
- Example
- In statistical software packages
- See also
- References
- Further reading
- External links

## Content

Binomial test is an exact test of the statistical significance of deviations from a theoretically expected distribution of observations into two categories using sample data.

Usage
The binomial test is useful to test hypotheses about the probability (
  
    
      
        π
      
    
    {\displaystyle \pi }
  
) of success:

  
    
      
        
          H
          
            0
          
        
        :
        π
        =
        
          π
          
            0
          
        
      
    
    {\displaystyle H_{0}\colon \pi =\pi _{0}}
  

where 
  
    
      
        
          π
          
            0
          
        
      
    
    {\displaystyle \pi _{0}}
  
 is a user-defined value between 0 and 1.
If in a sample of size 
  
    
      
        n
      
    
    {\displaystyle n}
  
 there are 
  
    
      
        k
      
    
    {\displaystyle k}
  
 successes, while we expect 
  
    
      
        n
        
          π
          
            0
          
        
      
    
    {\displaystyle n\pi _{0}}
  
, the formula of the binomial distribution gives the probability of finding this value:

  
    
      
        Pr
        (
        X
        =
        k
        )
        =
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        
          p
          
            k
          
        
        (
        1
        −
        p
        
          )
          
            n
            −
            k
          
        
      
    
    {\displaystyle \Pr(X=k)={\binom {n}{k}}p^{k}(1-p)^{n-k}}
  

If the null hypothesis 
  
    
      
        
          H
          
            0
          
        
      
    
    {\displaystyle H_{0}}
  
 were correct, then the expected number of successes would be 
  
    
      
        n
        
          π
          
            0
          
        
      
    
    {\displaystyle n\pi _{0}}
  
. We find our 
  
    
      
        p
      
    
    {\displaystyle p}
  
-value for this test by considering the probability of seeing an outcome as, or more, extreme. For a one-tailed test, this is straightforward to compute. Suppose that we want to test if 
  
    
      
        π
        <
        
          π
          
            0
          
        
      
    
    {\displaystyle \pi <\pi _{0}}
  
. Then our 
  
    
      
        p
      
    
    {\displaystyle p}
  
-value would be,

  
    
      
        p
        =
        
          ∑
          
            i
            =
            0
          
          
            k
          
        
        Pr
        (
        X
        =
        i
        )
        =
        
          ∑
          
            i
            =
            0
          
          
            k
          
        
        
          
            
              (
            
            
              n
              i
            
            
              )
            
          
        
        
          π
          
            0
          
          
            i
          
        
        (
        1
        −
        
          π
          
            0
          
        
        
          )
          
            n
            −
            i
          
        
      
    
    {\displaystyle p=\sum _{i=0}^{k}\Pr(X=i)=\sum _{i=0}^{k}{\binom {n}{i}}\pi _{0}^{i}(1-\pi _{0})^{n-i}}
  

An analogous computation can be done if we're testing if 
  
    
      
        π
        >
        
          π
          
            0
          
        
      
    
    {\displaystyle \pi >\pi _{0}}
  
 using the summation of the range from 
  
    
      
        k
      
    
    {\displaystyle k}
  
 to 
  
    
      
        n
      
    
    {\displaystyle n}
  
 instead.
Calculating a 
  
    
      
        p
      
    
    {\displaystyle p}
  
-value for a two-tailed test is slightly more complicated, since a binomial distribution isn't symmetric if 
  
    
      
        
          π
          
            0
          
        
        ≠
        0.5
      
    
    {\displaystyle \pi _{0}\neq 0.5}
  
. This means that we can't just double the 
  
    
      
        p
      
    
    {\displaystyle p}
  
-value from the one-tailed test. Recall that we want to consider events that are as, or more, extreme than the one we've seen, so we should consider the probability that we would see an event that is as, or less, likely than 
  
    
      
        X
        =
        k
      
    
    {\displaystyle X=k}
  
. Let 
  
    
      
        
          
            I
          
        
        =
        {
        i
        :
        Pr
        (
        X
        =
        i
        )
        ≤
        Pr
        (
        X
        =
        k
        )
        }
      
    
    {\displaystyle {\mathcal {I}}=\{i\colon \Pr(X=i)\leq \Pr(X=k)\}}
  
 denote all such events. Then the two-tailed 
  
    
      
        p
      
    
    {\displaystyle p}
  
-value is calculated as,

  
    
      
        p
        =
        
          ∑
          
            i
            ∈
            
              
                I
              
            
          
        
        Pr
        (
        X
        =
        i
        )
        =
        
          ∑
          
            i
            ∈
            
              
                I
              
            
          
        
        
          
            
              (
            
            
              n
              i
            
            
              )
            
          
        
        
          π
          
            0
          
          
            i
          
        
        (
        1
        −
        
          π
          
            0
          
        
        
          )
          
            n
            −
            i
          
        
      
    
    {\displaystyle p=\sum _{i\in {\mathcal {I}}}\Pr(X=i)=\sum _{i\in {\mathcal {I}}}{\binom {n}{i}}\pi _{0}^{i}(1-\pi _{0})^{n-i}}

Common use
One common use of the binomial test is the case where the null hypothesizes that two categories occur with equal frequency (
  
    
      
        
          H
          
            0
          
        
        :
        π
        =
        0.5
      
    
    {\displaystyle H_{0}\colon \pi =0.5}
  
), such as a coin toss. Tables are widely available to give the significance observed numbers of observations in the categories for this case. However, as the example below shows, the binomial test is not restricted to this case.
When there are more than two categories, and an exact test is required, the multinomial test, based on the multinomial distribution, must be used instead of the binomial test.
Most common measures of effect size for Binomial tests are Cohen's h or Cohen's g.

Large samples
For large samples such as the example below, the binomial distribution is well approximated by convenient continuous distributions, and these are used as the basis for alternative tests that are much quicker to compute, such as Pearson's chi-squared test and the G-test.  However, for small samples these approximations break down, and there is no alternative to the binomial test.
The most usual (and easiest) approximation is through the standard normal distribution, in which a z-test is performed of the test statistic 
  
    
      
        Z
      
    
    {\displaystyle Z}
  
, given by

  
    
      
        Z
        =
        
          
            
              k
              −
              n
              π
            
            
              n
              π
              (
              1
              −
              π
              )
            
          
        
      
    
    {\displaystyle Z={\frac {k-n\pi }{\sqrt {n\pi (1-\pi )}}}}
  

where 
  
    
      
        k
      
    
    {\displaystyle k}
  
 is the number of successes observed in a sample of size 
  
    
      
        n
      
    
    {\displaystyle n}
  
 and 
  
    
      
        π
      
    
    {\displaystyle \pi }
  
 is the probability of success according to the null hypothesis. An improvement on this approximation is possible by introducing a continuity correction:

  
    
      
        Z
        =
        
          
            
              k
              −
              n
              π
              ±
              
                
                  1
                  2
                
              
            
            
              n
              π
              (
              1
              −
              π
              )
            
          
        
      
    
    {\displaystyle Z={\frac {k-n\pi \pm {\frac {1}{2}}}{\sqrt {n\pi (1-\pi )}}}}
  

For very large 
  
    
      
        n
      
    
    {\displaystyle n}
  
, this continuity correction will be unimportant, but for intermediate values, where the exact binomial test doesn't work, it will yield a substantially more accurate result.
In notation in terms of a measured sample proportion 
  
    
      
        
          
            
              p
              ^
            
          
        
      
    
    {\displaystyle {\hat {p}}}
  
, null hypothesis for the proportion 
  
    
      
        
          p
          
            0
          
        
      
    
    {\displaystyle p_{0}}
  
, and sample size 
  
    
      
        n
      
    
    {\displaystyle n}
  
, where 
  
    
      
        
          
            
              p
              ^
            
          
        
        =
        k
        
          /
        
        n
      
    
    {\displaystyle {\hat {p}}=k/n}
  
 and 
  
    
      
        
          p
          
            0
          
        
        =
        π
      
    
    {\displaystyle p_{0}=\pi }
  
, one may rearrange and write the z-test above as

  
    
      
        Z
        =
        
          
            
              
                
                  
                    p
                    ^
                  
                
              
              −
              
                p
                
                  0
                
              
            
            
              
                
                  
                    p
                    
                      0
                    
                  
                  (
                  1
                  −
                  
                    p
                    
                      0
                    
                  
                  )
                
                n
              
            
          
        
      
    
    {\displaystyle Z={\frac {{\hat {p}}-p_{0}}{\sqrt {\frac {p_{0}(1-p_{0})}{n}}}}}
  

by dividing by 
  
    
      
        n
      
    
    {\displaystyle n}
  
 in both numerator and denominator, which is a form that may be more familiar to some readers.

Example
Suppose we have a board game that depends on the roll of one die and attaches special importance to rolling a 6. In a particular game, the die is rolled 235 times, and 6 comes up 51 times. If the die is fair, we would expect 6 to come up 

  
    
      
        235
        ×
        1
        
          /
        
        6
        =
        39.17
      
    
    {\displaystyle 235\times 1/6=39.17}
  

times. We have now observed that the number of 6s is higher than what we would expect on average by pure chance had the die been a fair one. But, is the number significantly high enough for us to conclude anything about the fairness of the die? This question can be answered by the binomial test. Our null hypothesis would be that the die is fair (probability of each number coming up on the die is 1/6).
To find an answer to this question using the binomial test, we use the binomial distribution 

  
    
      
        B
        (
        N
        =
        235
        ,
        p
        =
        1
        
          /
        
        6
        )
      
    
    {\displaystyle B(N=235,p=1/6)}
  
  with pmf 
  
    
      
        f
        (
        k
        ,
        n
        ,
        p
        )
        =
        Pr
        (
        k
        ;
        n
        ,
        p
        )
        =
        Pr
        (
        X
        =
        k
        )
        =
        
          
            
              (
            
            
              n
              k
            
            
              )
            
          
        
        
          p
          
            k
          
        
        (
        1
        −
        p
        
          )
          
            n
            −
            k
          
        
      
    
    {\displaystyle f(k,n,p)=\Pr(k;n,p)=\Pr(X=k)={\binom {n}{k}}p^{k}(1-p)^{n-k}}
  
 .
As we have observed a value greater than the expected value, we could consider the probability of observing 51 6s or higher under the null, which would constitute a one-tailed test (here we are basically testing whether this die is biased towards generating more 6s than expected). In order to calculate the probability of 51 or more 6s in a sample of 235 under the null hypothesis we add up the probabilities of getting exactly 51 6s, exactly 52 6s, and so on up to probability of getting exactly 235 6s:

  
    
      
        
          ∑
          
            i
            =
            51
          
          
            235
          
        
        
          
            
              (
            
            
              235
              i
            
            
              )
            
          
        
        
          p
          
            i
          
        
        (
        1
        −
        p
        
          )
          
            235
            −
            i
          
        
        =
        0.02654
      
    
    {\displaystyle \sum _{i=51}^{235}{235 \choose i}p^{i}(1-p)^{235-i}=0.02654}
  

If we have a significance level of 5%, then this result (0.02654 < 5%) indicates that we have evidence that is significant enough to reject the null hypothesis that the die is fair.
Normally, when we are testing for fairness of a die, we are also interested if the die is biased towards generating fewer 6s than expected, and not only more 6s as we considered in the one-tailed test above. In order to consider both the biases, we use a two-tailed test. Note that to do this we cannot simply double the one-tailed p-value unless the probability of the event is 1/2. This is because the binomial distribution becomes asymmetric as that probability deviates from 1/2. There are two methods to define the two-tailed p-value. One method is to sum the probability that the total deviation in numbers of events in either direction from the expected value is either more than or less than the expected value. The probability of that occurring in our example is 0.0437. The second method involves computing the probability that the deviation from the expected value is as unlikely or more unlikely than the observed value, i.e. from a comparison of the probability density functions. This can create a subtle difference, but in this example yields the same probability of 0.0437. In both cases, the two-tailed test reveals significance at the 5% level, indicating that the number of 6s observed was significantly different for this die than the expected number at the 5% level.

In statistical software packages
Binomial tests are available in most software used for statistical purposes. E.g.

In R the above example could be calculated with the following code:
binom.test(51, 235, 1/6, alternative = "less") (one-tailed test)
binom.test(51, 235, 1/6, alternative = "greater") (one-tailed test)
binom.test(51, 235, 1/6, alternative = "two.sided") (two-tailed test)
In Java using the Apache Commons library:
new BinomialTest().binomialTest(235, 51, 1.0 / 6, AlternativeHypothesis.LESS_THAN) (one-tailed test)
new BinomialTest().binomialTest(235, 51, 1.0 / 6, AlternativeHypothesis.GREATER_THAN) (one-tailed test)
new BinomialTest().binomialTest(235, 51, 1.0 / 6, AlternativeHypothesis.TWO_SIDED) (two-tailed test)
In SAS the test is available in the Frequency procedure
In SPSS the test can be utilized through the menu Analyze > Nonparametric test > Binomial
In Python, use SciPy's binomtest:
scipy.stats.binomtest(51, 235, 1.0/6, alternative='greater') (one-tailed test)
scipy.stats.binomtest(51, 235, 1.0/6, alternative='two-sided') (two-tailed test)
In MATLAB, use myBinomTest, which is available via Mathworks' community File Exchange website. myBinomTest will directly calculate the p-value for the observations given the hypothesized probability of a success. [pout]=myBinomTest(51, 235, 1/6) (generally two-tailed, but can optionally perform a one-tailed test).
In Stata, use bitest.
In Microsoft Excel, use Binom.Dist. The function takes parameters (Number of successes, Trials, Probability of Success, Cumulative).  The "Cumulative" parameter takes a boolean True or False, with True giving the Cumulative probability of finding this many successes (a left-tailed test), and False the exact probability of finding this many successes.

See also
p-value
Cohen's g
Cohen's h
 Lady tasting tea experiment

References
Further reading
Dougherty, Edward R. (1990). "Testing a Proportion". Probability and Statistics for the Engineering, Computing, and Physical Sciences. Englewood Cliffs: Prentice Hall. pp. 417–423. ISBN 0-13-711995-X.

External links
Binomial Probability Calculator
"The binomial test". www.graphpad.com.

## Related Articles

### Internal Links

- [Apache Commons](https://en.wikipedia.org/wiki/Apache_Commons)
- [Binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution)
- [Board game](https://en.wikipedia.org/wiki/Board_game)
- [Effect size](https://en.wikipedia.org/wiki/Effect_size)
- [Cohen's h](https://en.wikipedia.org/wiki/Cohen%27s_h)
- [Continuity correction](https://en.wikipedia.org/wiki/Continuity_correction)
- [Probability distribution](https://en.wikipedia.org/wiki/Probability_distribution)
- [Dice](https://en.wikipedia.org/wiki/Dice)
- [Exact test](https://en.wikipedia.org/wiki/Exact_test)
- [G-test](https://en.wikipedia.org/wiki/G-test)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Lady tasting tea](https://en.wikipedia.org/wiki/Lady_tasting_tea)
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [Microsoft Excel](https://en.wikipedia.org/wiki/Microsoft_Excel)
- [Multinomial distribution](https://en.wikipedia.org/wiki/Multinomial_distribution)
- [Multinomial test](https://en.wikipedia.org/wiki/Multinomial_test)
- [Null hypothesis](https://en.wikipedia.org/wiki/Null_hypothesis)
- [One- and two-tailed tests](https://en.wikipedia.org/wiki/One-_and_two-tailed_tests)
- [P-value](https://en.wikipedia.org/wiki/P-value)
- [Pearson's chi-squared test](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test)
- [Probability mass function](https://en.wikipedia.org/wiki/Probability_mass_function)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [SAS (software)](https://en.wikipedia.org/wiki/SAS_(software))
- [SPSS](https://en.wikipedia.org/wiki/SPSS)
- [SciPy](https://en.wikipedia.org/wiki/SciPy)
- [Stata](https://en.wikipedia.org/wiki/Stata)
- [Statistical hypothesis test](https://en.wikipedia.org/wiki/Statistical_hypothesis_test)
- [Statistical significance](https://en.wikipedia.org/wiki/Statistical_significance)
- [Z-test](https://en.wikipedia.org/wiki/Z-test)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from November 2016](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_November_2016)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:33:56.140876+00:00_