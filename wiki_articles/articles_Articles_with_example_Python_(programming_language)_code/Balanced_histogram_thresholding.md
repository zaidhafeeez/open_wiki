# Balanced histogram thresholding

## Article Metadata

- **Last Updated:** 2024-12-14T19:33:16.831364+00:00
- **Original Article:** [Balanced histogram thresholding](https://en.wikipedia.org/wiki/Balanced_histogram_thresholding)
- **Language:** en
- **Page ID:** 29817825

## Summary

In image processing, the balanced histogram thresholding method (BHT), is a very simple method used for automatic image thresholding. Like Otsu's Method and the Iterative Selection Thresholding Method, this is a histogram based thresholding method. This approach assumes that the image is divided in two main classes: The background and the foreground. The BHT method tries to find the optimum threshold level that divides the histogram in two classes.

This method weighs the histogram, checks which

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Image segmentation
- Category:Short description matches Wikidata
- Category:Webarchive template wayback links

## Table of Contents

- Algorithm
- References
- External links

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

## Related Articles

### Internal Links

- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Histogram](https://en.wikipedia.org/wiki/Histogram)
- [Digital image processing](https://en.wikipedia.org/wiki/Digital_image_processing)
- [Otsu's method](https://en.wikipedia.org/wiki/Otsu%27s_method)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Thresholding (image processing)](https://en.wikipedia.org/wiki/Thresholding_(image_processing))
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Weighing scale](https://en.wikipedia.org/wiki/Weighing_scale)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:33:16.831364+00:00_