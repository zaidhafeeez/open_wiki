---
title: Winsorizing
url: https://en.wikipedia.org/wiki/Winsorizing
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Articles with example R code", "Category:Articles with short description", "Category:Robust statistics", "Category:Short description matches Wikidata", "Category:Statistical data transformation"]
references: 0
last_modified: 2024-12-19T13:48:54Z
---

# Winsorizing

## Summary

Winsorizing or winsorization is the transformation of statistics by limiting extreme values in the statistical data to reduce the effect of possibly spurious outliers. It is named after the engineer-turned-biostatistician Charles P. Winsor (1895–1951). The effect is the same as clipping in signal processing.
The distribution of many statistics can be heavily influenced by outliers, values that are 'way outside' the bulk of the data. A typical strategy to account for, without eliminating altogeth

## Full Content

Winsorizing or winsorization is the transformation of statistics by limiting extreme values in the statistical data to reduce the effect of possibly spurious outliers. It is named after the engineer-turned-biostatistician Charles P. Winsor (1895–1951). The effect is the same as clipping in signal processing.
The distribution of many statistics can be heavily influenced by outliers, values that are 'way outside' the bulk of the data. A typical strategy to account for, without eliminating altogether, these outlier values is to 'reset' outliers to a specified percentile (or an upper and lower percentile) of the data.  For example, a 90% winsorization would see all data below the 5th percentile set to the 5th percentile, and all data above the 95th percentile set to the 95th percentile. Winsorized estimators are usually more robust to outliers than their more standard forms, although there are alternatives, such as trimming (see below), that will achieve a similar effect.

Example
Consider a simple data set consisting of:

{92, 19, 101, 58, 1053, 91, 26, 78, 10, 13, −40, 101, 86, 85, 15, 89, 89, 28, −5, 41}
(N = 20, mean = 101.5)
The data below the 5th percentile lie between −40 and −5 inclusive, while the data above the 95th percentile lie between 101 and 1053 inclusive (pertinent values are shown in bold). Winsorization effectively resets the outlier values to the values of the data at the 5th and 95th percentiles.  Accordingly, a 90% winsorization would result in the following data set:

{92, 19, 101, 58, 101, 91, 26, 78, 10, 13, −5, 101, 86, 85, 15, 89, 89, 28, −5, 41}
(N = 20, mean = 55.65)
After winsorization the mean has dropped to nearly half its previous value, and is consequently more in line or congruent with the data set from which it is calculated.

Explanation, and distinction from trimming/truncation
Note that winsorizing is not equivalent to simply excluding data, which is a simpler procedure, called trimming or truncation, but is a method of censoring data.
In a trimmed estimator, the extreme values are discarded; in a winsorized estimator, the extreme values are instead replaced by certain percentiles (the trimmed minimum and maximum).
Thus a winsorized mean is not the same as a truncated or trimmed mean. For instance, the 10% trimmed mean is the average of the 5th to 95th percentile of the data, while the 90% winsorized mean sets the bottom 5% to the 5th percentile, the top 5% to the 95th percentile, and then averages the data.  Winsorizing thus does not change the total number of values in the data set, N.  In the example given above, the trimmed mean would be obtained from the smaller (truncated) set:

{92, 19, 101, 58,       91, 26, 78, 10, 13,       101, 86, 85, 15, 89, 89, 28, −5, 41}      
(N = 18, trimmed mean = 56.5)
In this case, the winsorized mean can equivalently be expressed as a weighted average of the 5th percentile, the truncated mean, and the 95th percentile (for this case of a 10% winsorized mean: 0.05 times the 5th percentile, 0.9 times the 10% trimmed mean, and 0.05 times the 95th percentile). However, in general, winsorized statistics need not be expressible in terms of the corresponding trimmed statistic.
More formally, they are distinct because the order statistics are not independent.

Uses
Winsorization is used in the survey methodology context in order to "trim" extreme survey non-response weights.
It is also used in the construction of some stock indexes when looking at the range of certain factors (for example growth and value) for particular stocks.

Coding methods
Python can winsorize data using SciPy library:

R can winsorize data using the DescTools package:

See also
Trimmed estimator
Huber loss
Robust regression

References
Hastings, Jr., Cecil; Mosteller, Frederick; Tukey, John W.; Winsor, Charles P. (1947). "Low moments for small samples: a comparative study of order statistics". Annals of Mathematical Statistics. 18 (3): 413–426. doi:10.1214/aoms/1177730388.
Dixon, W. J. (1960). "Simplified Estimation from Censored Normal Samples". Annals of Mathematical Statistics. 31 (2): 385–391. doi:10.1214/aoms/1177705900.
Tukey, J. W. (1962). "The Future of Data Analysis". Annals of Mathematical Statistics. 33 (1): 1–67 [p. 18]. doi:10.1214/aoms/1177704711. JSTOR 2237638.

External links
"Winsorization". R-bloggers. June 30, 2011.
