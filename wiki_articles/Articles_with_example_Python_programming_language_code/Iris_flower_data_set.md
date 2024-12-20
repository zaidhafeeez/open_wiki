---
title: Iris flower data set
url: https://en.wikipedia.org/wiki/Iris_flower_data_set
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Articles with example R code", "Category:Articles with short description", "Category:Datasets in machine learning", "Category:Ronald Fisher", "Category:Short description is different from Wikidata", "Category:Statistical data sets"]
references: 0
last_modified: 2024-12-19T14:02:49Z
---

# Iris flower data set

## Summary

The Iris flower data set or Fisher's Iris data set is a multivariate data set used and made famous by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Pe

## Full Content

The Iris flower data set or Fisher's Iris data set is a multivariate data set used and made famous by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish each species. Fisher's paper was published in the Annals of Eugenics (today the Annals of Human Genetics).

Use of the data set
Originally used as an example data set on which Fisher's linear discriminant analysis was applied, it became a typical test case for many statistical classification techniques in machine learning such as support vector machines.
The use of this data set in cluster analysis however is not common, since the data set only contains two clusters with rather obvious separation. One of the clusters contains Iris setosa, while the other cluster contains both Iris virginica and Iris versicolor and is not separable without the species information Fisher used. This makes the data set a good example to explain the difference between supervised and unsupervised techniques in data mining: Fisher's linear discriminant model can only be obtained when the object species are known: class labels and clusters are not necessarily the same.
Nevertheless, all three species of Iris are separable in the projection on the nonlinear and branching principal component. The data set is approximated by the closest tree with some penalty for the excessive number of nodes, bending and stretching. Then the so-called "metro map" is constructed. The data points are projected into the closest node. For each node the pie diagram of the projected points is prepared. The area of the pie is proportional to the number of the projected points. It is clear from the diagram (left) that the absolute majority of the samples of the different Iris species belong to the different nodes. Only a small fraction of Iris-virginica is mixed with Iris-versicolor (the mixed blue-green nodes in the diagram). Therefore, the three species of Iris (Iris setosa, Iris virginica and Iris versicolor) are separable by the unsupervising procedures of nonlinear principal component analysis. To discriminate them, it is sufficient just to select the corresponding nodes on the principal tree.

Data set
The dataset contains a set of 150 records under five attributes: sepal length, sepal width, petal length, petal width and species.

The iris data set is widely used as a beginner's dataset for machine learning purposes. The dataset is included in R base and Python in the machine learning library scikit-learn, so that users can access it without having to find a source for it.
Several versions of the dataset have been published.

R code illustrating usage
The example R code shown below reproduce the scatterplot displayed at the top of this article:

Python code illustrating usage
This code gives:

See also
Classic data sets
List of datasets for machine-learning research

References
External links
"Fisher's Iris Data". (Contains two errors which are documented). UCI Machine Learning Repository: Iris Data Set.
