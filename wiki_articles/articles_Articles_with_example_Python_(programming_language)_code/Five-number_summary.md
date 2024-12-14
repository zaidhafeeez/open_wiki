# Five-number summary

## Article Metadata

- **Last Updated:** 2024-12-14T19:37:03.061098+00:00
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
In addition to the median of a single set of data there are two related statistics called the upper and lower quartiles. If data are placed in order, t

## Categories

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

## Related Articles

### Internal Links

- [Box plot](https://en.wikipedia.org/wiki/Box_plot)
- [Box plot](https://en.wikipedia.org/wiki/Box_plot)
- [Cambridge University Press and Assessment](https://en.wikipedia.org/wiki/Cambridge_University_Press_and_Assessment)
- [Descriptive statistics](https://en.wikipedia.org/wiki/Descriptive_statistics)
- [Frederick Mosteller](https://en.wikipedia.org/wiki/Frederick_Mosteller)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive)
- [Interquartile range](https://en.wikipedia.org/wiki/Interquartile_range)
- [John Tukey](https://en.wikipedia.org/wiki/John_Tukey)
- [L-estimator](https://en.wikipedia.org/wiki/L-estimator)
- [Library of Congress Control Number](https://en.wikipedia.org/wiki/Library_of_Congress_Control_Number)
- [Level of measurement](https://en.wikipedia.org/wiki/Level_of_measurement)
- [Median](https://en.wikipedia.org/wiki/Median)
- [Mid-range](https://en.wikipedia.org/wiki/Mid-range)
- [Midhinge](https://en.wikipedia.org/wiki/Midhinge)
- [OCLC](https://en.wikipedia.org/wiki/OCLC)
- [Open Library](https://en.wikipedia.org/wiki/Open_Library)
- [Order statistic](https://en.wikipedia.org/wiki/Order_statistic)
- [Percentile](https://en.wikipedia.org/wiki/Percentile)
- [Probability distribution](https://en.wikipedia.org/wiki/Probability_distribution)
- [Quartile](https://en.wikipedia.org/wiki/Quartile)
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Range (statistics)](https://en.wikipedia.org/wiki/Range_(statistics))
- [SAS (software)](https://en.wikipedia.org/wiki/SAS_(software))
- [Sample maximum and minimum](https://en.wikipedia.org/wiki/Sample_maximum_and_minimum)
- [Sample maximum and minimum](https://en.wikipedia.org/wiki/Sample_maximum_and_minimum)
- [Seven-number summary](https://en.wikipedia.org/wiki/Seven-number_summary)
- [Solar System](https://en.wikipedia.org/wiki/Solar_System)
- [Three-point estimation](https://en.wikipedia.org/wiki/Three-point_estimation)
- [Trimean](https://en.wikipedia.org/wiki/Trimean)
- [Univariate](https://en.wikipedia.org/wiki/Univariate)
- [Wiley (publisher)](https://en.wikipedia.org/wiki/Wiley_(publisher))
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from January 2013](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_January_2013)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:37:03.061098+00:00_