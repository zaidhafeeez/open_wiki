# Five-number summary

## Metadata
- **Last Updated:** 2024-12-03 06:51:57 UTC
- **Original Article:** [Five-number summary](https://en.wikipedia.org/wiki/Five-number_summary)
- **Language:** en
- **Page ID:** 160963

## Summary
The five-number summary is a set of descriptive statistics that provides information about a dataset. It consists of the five most important sample percentiles:

the sample minimum (smallest observation)
the lower quartile or first quartile
the median (the middle value)
the upper quartile or third quartile
the sample maximum (largest observation)
In addition to the median of a single set of data there are two related statistics called the upper and lower quartiles. If data are placed in order, then the lower quartile is central to the lower half of the data and the upper quartile is central to the upper half of the data. These quartiles are used to calculate the interquartile range, which helps to describe the spread of the data, and determine whether or not any data points are outliers.
In order for these statistics to exist, the observations must be from a univariate variable that can be measured on an ordinal, interval or ratio scale.

## Categories
This article belongs to the following categories:

- Category:All articles needing additional references
- Category:Articles needing additional references from January 2013
- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with short description
- Category:Short description is different from Wikidata
- Category:Summary statistics

## Table of Contents

- Use and representation
- Example
- See also

## Content

The five-number summary is a set of descriptive statistics that provides information about a dataset. It consists of the five most important sample percentiles:

the sample minimum (smallest observation)
the lower quartile or first quartile
the median (the middle value)
the upper quartile or third quartile
the sample maximum (largest observation)
In addition to the median of a single set of data there are two related statistics called the upper and lower quartiles. If data are placed in order, then the lower quartile is central to the lower half of the data and the upper quartile is central to the upper half of the data. These quartiles are used to calculate the interquartile range, which helps to describe the spread of the data, and determine whether or not any data points are outliers.
In order for these statistics to exist, the observations must be from a univariate variable that can be measured on an ordinal, interval or ratio scale.

Use and representation
The five-number summary provides a concise summary of the distribution of the observations. Reporting five numbers avoids the need to decide on the most appropriate summary statistic. The five-number summary gives information about the location (from the median), spread (from the quartiles) and range (from the sample minimum and maximum) of the observations. Since it reports order statistics (rather than, say, the mean) the five-number summary is appropriate for ordinal measurements, as well as interval and ratio measurements.
It is possible to quickly compare several sets of observations by comparing their five-number summaries, which can be represented graphically using a boxplot.
In addition to the points themselves, many L-estimators can be computed from the five-number summary, including interquartile range, midhinge, range, mid-range, and trimean.
The five-number summary is sometimes represented as in the following table:

Example
This example calculates the five-number summary for the following set of observations: 0, 0, 1, 2, 63, 61, 27, 13.
These are the number of moons of each planet in the Solar System.
It helps to put the observations in ascending order: 0, 0, 1, 2, 13, 27, 61, 63. There are eight observations, so the median is the mean of the two middle numbers, (2 + 13)/2 = 7.5. Splitting the observations either side of the median gives two groups of four observations. The median of the first group is the lower or first quartile, and is equal to (0 + 1)/2 = 0.5. The median of the second group is the upper or third quartile, and is equal to (27 + 61)/2 = 44.
The smallest and largest observations are 0 and 63.
So the five-number summary would be 0, 0.5, 7.5, 44, 63.

Example in R
It is possible to calculate the five-number summary in the R programming language using the fivenum function. The summary function, when applied to a vector, displays the five-number summary together with the mean (which is not itself a part of the five-number summary). The fivenum uses a different method to calculate percentiles than the summary function.

Example in Python
This python example uses the percentile function from the numerical library numpy and works in Python 2 and 3.

Example in SAS
You can use PROC UNIVARIATE in SAS to get the five number summary:

Example in Stata
See also
Seven-number summary
Three-point estimation
Box plot


== References ==

## Archive Info
- **Archived on:** 2024-12-15 21:04:24 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 3367 bytes
- **Word Count:** 555 words
