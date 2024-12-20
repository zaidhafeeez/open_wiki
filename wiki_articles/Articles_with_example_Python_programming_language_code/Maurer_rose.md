---
title: Maurer rose
url: https://en.wikipedia.org/wiki/Maurer_rose
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Curves", "Category:Eponymous curves", "Category:Polygons", "Category:Short description matches Wikidata"]
references: 0
last_modified: 2024-12-19T14:18:15Z
---

# Maurer rose

## Summary

In geometry, the concept of a Maurer rose was introduced by Peter M. Maurer in his article titled A Rose is a Rose...[1]. A Maurer rose consists of some lines that connect some points on a rose curve.

## Full Content

In geometry, the concept of a Maurer rose was introduced by Peter M. Maurer in his article titled A Rose is a Rose...[1]. A Maurer rose consists of some lines that connect some points on a rose curve.

Definition
Let r = sin(nθ) be a rose in the polar coordinate system, where n is a positive integer. The rose has n petals if n is odd, and 2n petals if n is even.
We then take 361 points on the rose:

(sin(nk), k) (k = 0, d, 2d, 3d, ..., 360d),
where d is a positive integer and the angles are in degrees, not radians.

Explanation
A Maurer rose of the rose r = sin(nθ) consists of the 360 lines successively connecting the above 361 points. Thus a Maurer rose is a polygonal curve with vertices on a rose.
A Maurer rose can be described as a closed route in the polar plane. A walker starts a journey from the origin, (0, 0), and walks along a line to the point (sin(nd), d). Then, in the second leg of the journey, the walker walks along a line to the next point, (sin(n·2d), 2d), and so on. Finally, in the final leg of the journey, the walker walks along a line, from (sin(n·359d), 359d) to the ending point, (sin(n·360d), 360d). The whole route is the Maurer rose of the rose r = sin(nθ). A Maurer rose is a closed curve since the starting point, (0, 0) and the ending point, (sin(n·360d), 360d), coincide.
The following figure shows the evolution of a Maurer rose (n = 2, d = 29°).

Images
The following are some Maurer roses drawn with some values for n and d:

Example implementation
Using Python:

References
Maurer, Peter M. (August–September 1987). "A Rose is a Rose...". The American Mathematical Monthly. 94 (7): 631–645. CiteSeerX 10.1.1.97.8141. doi:10.2307/2322215. JSTOR 2322215.
Weisstein, Eric W. "Maurer roses". MathWorld. (Interactive Demonstrations)

External links
Interactive Demonstration: https://codepen.io/Igor_Konovalov/full/ZJwPQv/
Explorer: https://filip26.github.io/maurer-rose-explorer/ [source code]
Draw from values and create vector graphics: https://www.sqrt.ch/Buch/Maurer/maurerroses.html
