# Balanced histogram thresholding

_Last updated: 2024-12-14T15:39:32.368196_

**Original Article:** [Balanced histogram thresholding](https://en.wikipedia.org/wiki/Balanced_histogram_thresholding)

**Summary:** In image processing, the balanced histogram thresholding method (BHT), is a very simple method used for automatic image thresholding. Like Otsu's Method and the Iterative Selection Thresholding Method, this is a histogram based thresholding method. This approach assumes that the image is divided in two main classes: The background and the foreground. The BHT method tries to find the optimum threshold level that divides the histogram in two classes.

This method weighs the histogram, checks which

## Categories
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Image segmentation
- Category:Short description matches Wikidata
- Category:Webarchive template wayback links

## Content

In image processing, the balanced histogram thresholding method (BHT), is a very simple method used for automatic image thresholding. Like Otsu's Method and the Iterative Selection Thresholding Method, this is a histogram based thresholding method. This approach assumes that the image is divided in two main classes: The background and the foreground. The BHT method tries to find the optimum threshold level that divides the histogram in two classes.

This method weighs the histogram, checks which of the two sides is heavier, and removes weight from the heavier side until it becomes the lighter. It repeats the same operation until the edges of the weighing scale meet.
Given its simplicity, this method is a good choice as a first approach when presenting the subject of automatic image thresholding.

Algorithm
The following listing, in C notation, is a simplified version of the Balanced Histogram Thresholding method:

The following, is a possible implementation in the Python language:

References
External links
ImageJ Plugin Archived 2013-10-17 at the Wayback Machine
Otsu vs. BHT