---
title: Peirce's criterion
url: https://en.wikipedia.org/wiki/Peirce%27s_criterion
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Articles with example R code", "Category:CS1: long volume value", "Category:Statistical outliers"]
references: 0
last_modified: 2024-12-16T23:48:28Z
---

# Peirce's criterion

## Summary

In robust statistics, Peirce's criterion  is a rule for eliminating outliers from data sets, which was devised by Benjamin Peirce.

## Full Content

In robust statistics, Peirce's criterion  is a rule for eliminating outliers from data sets, which was devised by Benjamin Peirce.

Outliers removed by Peirce's criterion
The problem of outliers
In data sets containing real-numbered measurements, the suspected outliers are the measured values that appear to lie outside the cluster of most of the other data values. The outliers would greatly change the estimate of location if the arithmetic average were to be used as a summary statistic of location. The problem is that the arithmetic mean is very sensitive to the inclusion of any outliers; in statistical terminology, the arithmetic mean is not robust.
In the presence of outliers, the statistician has two options. First, the statistician may remove the suspected outliers from the data set and then use the arithmetic mean to estimate the location parameter. Second, the statistician may use a robust statistic, such as the median statistic.
Peirce's criterion is a statistical procedure for eliminating outliers.

Uses of Peirce's criterion
The statistician and historian of statistics Stephen M. Stigler wrote the following about Benjamin Peirce:

"In 1852 he published the first significance test designed to tell an investigator whether an outlier should be rejected (Peirce 1852, 1878). The test, based on a likelihood ratio type of argument, had the distinction of producing an international debate on the wisdom of such actions (Anscombe, 1960, Rider, 1933, Stigler, 1973a)." 

Peirce's criterion is derived from a statistical analysis of the Gaussian distribution. Unlike some other criteria for removing outliers, Peirce's method can be applied to identify two or more outliers.

"It is proposed to determine in a series of 
  
    
      
        m
      
    
    {\displaystyle m}
  
 observations the limit of error, beyond which all observations involving so great an error may be rejected, provided there are as many as 
  
    
      
        n
      
    
    {\displaystyle n}
  
 such observations. The principle upon which it is proposed to solve this problem is, that the proposed observations should be rejected when the probability of the system of errors obtained by retaining them is less than that of the system of errors obtained by their rejection multiplied by the probability of making so many, and no more, abnormal observations."

Hawkins provides a formula for the criterion.
Peirce's criterion was used for decades at the United States Coast Survey, which was renamed the United States Coast and Geodetic Survey in 1878:

"From 1852 to 1867 he served as the director of the longitude determinations of the U. S. Coast Survey and from 1867 to 1874 as superintendent of the Survey. During these years his test was consistently employed by all the clerks of this, the most active and mathematically inclined statistical organization of the era."

Peirce's criterion was discussed in William Chauvenet's book.

Applications
An application for Peirce's criterion is removing poor data points from observation pairs in order to perform a regression between the two observations (e.g., a linear regression).  Peirce's criterion does not depend on observation data (only characteristics of the observation data), therefore making it a highly repeatable process that can be calculated independently of other processes. This feature makes Peirce's criterion for identifying outliers ideal in computer applications because it can be written as a call function.

Previous attempts
In 1855, B. A. Gould attempted to make Peirce's criterion easier to apply by creating tables of values representing values from Peirce's equations. A disconnect still exists between Gould's algorithm and the practical application of Peirce's criterion.
In 2003, S. M. Ross (University of New Haven) re-presented Gould's algorithm (now called "Peirce's method") with a new example data set and work-through of the algorithm. This methodology still relies on using look-up tables, which have been updated in this work (Peirce's criterion table).
In 2008, an attempt to write a pseudo-code was made by a Danish geologist K. Thomsen.  While this code provided some framework for Gould's algorithm, users were unsuccessful in calculating values reported by either Peirce or Gould.
In 2012, C. Dardis released the R package "Peirce" with various methodologies (Peirce's criterion and the Chauvenet method) with comparisons of outlier removals. Dardis and fellow contributor Simon Muller successfully implemented Thomsen's pseudo-code into a function called "findx". The code is presented in the R implementation section below. References for the R package are available online as well as an unpublished review of the R package results.
In 2013, a re-examination of Gould's algorithm and the utilisation of advanced Python programming modules (i.e., numpy and scipy) has made it possible to calculate the squared-error threshold values for identifying outliers.

Python implementation
In order to use Peirce's criterion, one must first understand the input and return values.  Regression analysis (or the fitting of curves to data) results in residual errors (or the difference between the fitted curve and the observation points).  Therefore, each observation point has a residual error associated with a fitted curve.  By taking the square (i.e., residual error raised to the power of two), residual errors are expressed as positive values.  If the squared error is too large (i.e., due to a poor observation) it can cause problems with the regression parameters (e.g., slope and intercept for a linear curve) retrieved from the curve fitting.
It was Peirce's idea to statistically identify what constituted an error as "too large" and therefore being identified as an "outlier" which could be removed from the observations to improve the fit between the observations and a curve.  K. Thomsen identified that three parameters were needed to perform the calculation: the number of observation pairs (N), the number of outliers to be removed (n), and the number of regression parameters (e.g., coefficients) used in the curve-fitting to get the residuals (m).  The end result of this process is to calculate a threshold value (of squared error) whereby observations with a squared error smaller than this threshold should be kept and observations with a squared error larger than this value should be removed (i.e., as an outlier).
Because Peirce's criterion does not take observations, fitting parameters, or residual errors as an input, the output must be re-associated with the data. Taking the average of all the squared errors (i.e., the mean-squared error) and multiplying it by the threshold squared error (i.e., the output of this function) will result in the data-specific threshold value used to identify outliers.
The following Python code returns x-squared values for a given N (first column) and n (top row) in Table 1 (m = 1) and Table 2 (m = 2) of Gould 1855. Due to the Newton-method of iteration, look-up tables, such as N versus log Q (Table III in Gould, 1855) and x versus log R (Table III in Peirce, 1852 and Table IV in Gould, 1855) are no longer necessary.

Python code
Java code
R implementation
Thomsen's code has been successfully written into the following function call, "findx" by C. Dardis and S. Muller in 2012 which returns the maximum error deviation, 
  
    
      
        x
      
    
    {\displaystyle x}
  
.  To complement the Python code presented in the previous section, the R equivalent of "peirce_dev" is also presented here which returns the squared maximum error deviation, 
  
    
      
        
          x
          
            2
          
        
      
    
    {\displaystyle x^{2}}
  
.  These two functions return equivalent values by either squaring the returned value from the "findx" function or by taking the square-root of the value returned by the "peirce_dev" function.  Differences occur with error handling.  For example, the "findx" function returns NaNs for invalid data while "peirce_dev" returns 0 (which allows for computations to continue without additional NA value handling).  Also, the "findx" function does not support any error handling when the number of potential outliers increases towards the number of observations (throws missing value error and NaN warning).
Just as with the Python version, the squared-error (i.e., 
  
    
      
        
          x
          
            2
          
        
      
    
    {\displaystyle x^{2}}
  
) returned by the "peirce_dev" function must be multiplied by the mean-squared error of the model fit to get the squared-delta value (i.e., Δ2).  Use Δ2 to compare the squared-error values of the model fit.  Any observation pairs with a squared-error greater than Δ2 are considered outliers and can be removed from the model.  An iterator should be written to test increasing values of n until the number of outliers identified (comparing Δ2 to model-fit squared-errors) is less than those assumed (i.e., Peirce's n).

R code
Notes
References
Peirce, Benjamin, "Criterion for the Rejection of Doubtful Observations", Astronomical Journal II 45 (1852) and Errata to the original paper.
Peirce, Benjamin (May 1877 – May 1878). "On Peirce's criterion". Proceedings of the American Academy of Arts and Sciences. 13: 348–351. doi:10.2307/25138498. JSTOR 25138498.
Peirce, Charles Sanders (1870) [published 1873]. "Appendix No. 21. On the Theory of Errors of Observation". Report of the Superintendent of the United States Coast Survey Showing the Progress of the Survey During the Year 1870: 200–224.. NOAA PDF Eprint (goes to Report p. 200, PDF's p. 215). U.S. Coast and Geodetic Survey Annual Reports links for years 1837–1965.
Peirce, Charles Sanders (1982). "On the Theory of Errors of Observation". In Kloesel, Christian J. W.; et al. (eds.). Writings of Charles S. Peirce: A Chronological Edition. Vol. 3, 1872–1878. Bloomington, Indiana: Indiana University Press. pp. 140–160. ISBN 0-253-37201-1.
Ross, Stephen, "Peirce's Criterion for the Elimination of Suspect Experimental Data", J. Engr. Technology, vol. 20 no.2, Fall, 2003. [1]
Stigler, Stephen M. (March 1978). "Mathematical Statistics in the Early States". Annals of Statistics. 6 (2): 239–265. doi:10.1214/aos/1176344123. JSTOR 2958876. MR 0483118.
Stigler, Stephen M. (1980). "Mathematical Statistics in the Early States". In Stephen M. Stigler (ed.). American Contributions to Mathematical Statistics in the Nineteenth Century, Volumes I & II. Vol. I. New York: Arno Press.
Stigler, Stephen M. (1989). "Mathematical Statistics in the Early States". In Peter Duren (ed.). A Century of Mathematics in America. Vol. III. Providence, RI: American Mathematical Society. pp. 537–564.
Hawkins, D.M. (1980). Identification of outliers. Chapman and Hall, London. ISBN 0-412-21900-X
Chauvenet, W. (1876) A Manual of Spherical and Practical Astronomy. J.B.Lippincott, Philadelphia. (reprints of various editions: Dover, 1960; Peter Smith Pub, 2000, ISBN 0-8446-1845-4; Adamant Media Corporation (2 Volumes), 2001, ISBN 1-4021-7283-4, ISBN 1-4212-7259-8; BiblioBazaar, 2009, ISBN 1-103-92942-9 )
