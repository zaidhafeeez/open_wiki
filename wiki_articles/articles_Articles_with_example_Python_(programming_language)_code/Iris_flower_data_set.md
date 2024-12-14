# Iris flower data set

## Article Metadata

- **Last Updated:** 2024-12-14T19:39:00.334602+00:00
- **Original Article:** [Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
- **Language:** en
- **Page ID:** 10477224

## Summary

The Iris flower data set or Fisher's Iris data set is a multivariate data set used and made famous by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Pe

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with short description
- Category:Datasets in machine learning
- Category:Ronald Fisher
- Category:Short description is different from Wikidata
- Category:Statistical data sets

## Table of Contents

- Use of the data set
- Data set
- See also
- References
- External links

## Content

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

## Related Articles

### Internal Links

- [A. J. Bliss](https://en.wikipedia.org/wiki/A._J._Bliss)
- [Alexander Gorban](https://en.wikipedia.org/wiki/Alexander_Gorban)
- [American Iris Society](https://en.wikipedia.org/wiki/American_Iris_Society)
- [Annals of Human Genetics](https://en.wikipedia.org/wiki/Annals_of_Human_Genetics)
- [Annals of the Missouri Botanical Garden](https://en.wikipedia.org/wiki/Annals_of_the_Missouri_Botanical_Garden)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Association for Computing Machinery](https://en.wikipedia.org/wiki/Association_for_Computing_Machinery)
- [Banknotes of the Japanese yen](https://en.wikipedia.org/wiki/Banknotes_of_the_Japanese_yen)
- [Banshu Yamasaki Iris Garden](https://en.wikipedia.org/wiki/Banshu_Yamasaki_Iris_Garden)
- [Biologist](https://en.wikipedia.org/wiki/Biologist)
- [Cedric Morris](https://en.wikipedia.org/wiki/Cedric_Morris)
- [Cluster analysis](https://en.wikipedia.org/wiki/Cluster_analysis)
- [Data mining](https://en.wikipedia.org/wiki/Data_mining)
- [Data set](https://en.wikipedia.org/wiki/Data_set)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Edgar Anderson](https://en.wikipedia.org/wiki/Edgar_Anderson)
- [Jean Stevens](https://en.wikipedia.org/wiki/Jean_Stevens)
- [ELKI](https://en.wikipedia.org/wiki/ELKI)
- [Ethel Anson Peckham](https://en.wikipedia.org/wiki/Ethel_Anson_Peckham)
- [Feature (machine learning)](https://en.wikipedia.org/wiki/Feature_(machine_learning))
- [Fleur-de-lis](https://en.wikipedia.org/wiki/Fleur-de-lis)
- [Gaspé Peninsula](https://en.wikipedia.org/wiki/Gasp%C3%A9_Peninsula)
- [George Gessert](https://en.wikipedia.org/wiki/George_Gessert)
- [George Yeld](https://en.wikipedia.org/wiki/George_Yeld)
- [Giardino dell'Iris](https://en.wikipedia.org/wiki/Giardino_dell%27Iris)
- [Grace Sturtevant](https://en.wikipedia.org/wiki/Grace_Sturtevant)
- [Greeneville, Tennessee](https://en.wikipedia.org/wiki/Greeneville,_Tennessee)
- [Hans-Peter Kriegel](https://en.wikipedia.org/wiki/Hans-Peter_Kriegel)
- [Handle System](https://en.wikipedia.org/wiki/Handle_System)
- [Iris (plant)](https://en.wikipedia.org/wiki/Iris_(plant))
- [Iris albicans](https://en.wikipedia.org/wiki/Iris_albicans)
- [Iris aphylla](https://en.wikipedia.org/wiki/Iris_aphylla)
- [Iris confusa](https://en.wikipedia.org/wiki/Iris_confusa)
- [Iris cristata](https://en.wikipedia.org/wiki/Iris_cristata)
- [Iris × germanica](https://en.wikipedia.org/wiki/Iris_%C3%97_germanica)
- [Iris lacustris](https://en.wikipedia.org/wiki/Iris_lacustris)
- [Iris latifolia](https://en.wikipedia.org/wiki/Iris_latifolia)
- [Iris pallida](https://en.wikipedia.org/wiki/Iris_pallida)
- [Iris prismatica](https://en.wikipedia.org/wiki/Iris_prismatica)
- [Iris pseudacorus](https://en.wikipedia.org/wiki/Iris_pseudacorus)
- [Iris ruthenica](https://en.wikipedia.org/wiki/Iris_ruthenica)
- [Iris sanguinea](https://en.wikipedia.org/wiki/Iris_sanguinea)
- [Iris ser. Californicae](https://en.wikipedia.org/wiki/Iris_ser._Californicae)
- [Iris ser. Chinenses](https://en.wikipedia.org/wiki/Iris_ser._Chinenses)
- [Iris ser. Longipetalae](https://en.wikipedia.org/wiki/Iris_ser._Longipetalae)
- [Iris ser. Sibiricae](https://en.wikipedia.org/wiki/Iris_ser._Sibiricae)
- [Iris setosa](https://en.wikipedia.org/wiki/Iris_setosa)
- [Iris subg. Hermodactyloides](https://en.wikipedia.org/wiki/Iris_subg._Hermodactyloides)
- [Iris subg. Iris](https://en.wikipedia.org/wiki/Iris_subg._Iris)
- [Iris subg. Limniris](https://en.wikipedia.org/wiki/Iris_subg._Limniris)
- [Iris subg. Nepalensis](https://en.wikipedia.org/wiki/Iris_subg._Nepalensis)
- [Iris subg. Scorpiris](https://en.wikipedia.org/wiki/Iris_subg._Scorpiris)
- [Iris subg. Xiphium](https://en.wikipedia.org/wiki/Iris_subg._Xiphium)
- [Iris variegata](https://en.wikipedia.org/wiki/Iris_variegata)
- [Iris versicolor](https://en.wikipedia.org/wiki/Iris_versicolor)
- [Iris virginica](https://en.wikipedia.org/wiki/Iris_virginica)
- [Iris xiphium](https://en.wikipedia.org/wiki/Iris_xiphium)
- [Iris × hollandica](https://en.wikipedia.org/wiki/Iris_%C3%97_hollandica)
- [Irises (painting)](https://en.wikipedia.org/wiki/Irises_(painting))
- [Irone](https://en.wikipedia.org/wiki/Irone)
- [Itako, Ibaraki](https://en.wikipedia.org/wiki/Itako,_Ibaraki)
- [J. Marion Shull](https://en.wikipedia.org/wiki/J._Marion_Shull)
- [JSTOR](https://en.wikipedia.org/wiki/JSTOR)
- [Japanese iris](https://en.wikipedia.org/wiki/Japanese_iris)
- [Jennifer Dy](https://en.wikipedia.org/wiki/Jennifer_Dy)
- [John Caspar Wister](https://en.wikipedia.org/wiki/John_Caspar_Wister)
- [K-means clustering](https://en.wikipedia.org/wiki/K-means_clustering)
- [Keizer, Oregon](https://en.wikipedia.org/wiki/Keizer,_Oregon)
- [Linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)
- [List of Iris species](https://en.wikipedia.org/wiki/List_of_Iris_species)
- [List of datasets for machine-learning research](https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research)
- [Louisiana iris](https://en.wikipedia.org/wiki/Louisiana_iris)
- [Lowell Fitz Randolph](https://en.wikipedia.org/wiki/Lowell_Fitz_Randolph)
- [Ludmila Kuncheva](https://en.wikipedia.org/wiki/Ludmila_Kuncheva)
- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
- [Mary Helen Wingate Lloyd](https://en.wikipedia.org/wiki/Mary_Helen_Wingate_Lloyd)
- [Michael Foster (physiologist)](https://en.wikipedia.org/wiki/Michael_Foster_(physiologist))
- [Morphology (biology)](https://en.wikipedia.org/wiki/Morphology_(biology))
- [Mototeru Kamo](https://en.wikipedia.org/wiki/Mototeru_Kamo)
- [Multivariate statistics](https://en.wikipedia.org/wiki/Multivariate_statistics)
- [Orris oil](https://en.wikipedia.org/wiki/Orris_oil)
- [Orris root](https://en.wikipedia.org/wiki/Orris_root)
- [Petal](https://en.wikipedia.org/wiki/Petal)
- [Pie chart](https://en.wikipedia.org/wiki/Pie_chart)
- [Presby Memorial Iris Gardens](https://en.wikipedia.org/wiki/Presby_Memorial_Iris_Gardens)
- [Principal component analysis](https://en.wikipedia.org/wiki/Principal_component_analysis)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher)
- [Special Interest Group on Knowledge Discovery and Data Mining](https://en.wikipedia.org/wiki/Special_Interest_Group_on_Knowledge_Discovery_and_Data_Mining)
- [Scatter plot](https://en.wikipedia.org/wiki/Scatter_plot)
- [Scikit-learn](https://en.wikipedia.org/wiki/Scikit-learn)
- [Sepal](https://en.wikipedia.org/wiki/Sepal)
- [Statistical classification](https://en.wikipedia.org/wiki/Statistical_classification)
- [Statistician](https://en.wikipedia.org/wiki/Statistician)
- [Support vector machine](https://en.wikipedia.org/wiki/Support_vector_machine)
- [Swan Lake Iris Gardens](https://en.wikipedia.org/wiki/Swan_Lake_Iris_Gardens)
- [Sydney B. Mitchell](https://en.wikipedia.org/wiki/Sydney_B._Mitchell)
- [Vincent van Gogh](https://en.wikipedia.org/wiki/Vincent_van_Gogh)
- [William Rickatson Dykes](https://en.wikipedia.org/wiki/William_Rickatson_Dykes)
- [Template:Iris](https://en.wikipedia.org/wiki/Template:Iris)
- [Template talk:Iris](https://en.wikipedia.org/wiki/Template_talk:Iris)
- [Category:Iris (plant)](https://en.wikipedia.org/wiki/Category:Iris_(plant))

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:39:00.334602+00:00_