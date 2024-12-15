# Hit-testing

## Article Metadata

- **Last Updated:** 2024-12-15T04:29:34.059410+00:00
- **Original Article:** [Hit-testing](https://en.wikipedia.org/wiki/Hit-testing)
- **Language:** en
- **Page ID:** 30001250

## Summary

In computer graphics programming, hit-testing (hit detection, picking, or pick correlation) is the process of determining whether a user-controlled cursor (such as a mouse cursor or touch-point on a touch-screen interface) intersects a given graphical object (such as a shape, line, or curve) drawn on the screen. Hit-testing may be performed on the movement or activation of a mouse or other pointing device.
Hit-testing is used by GUI environments to respond to user actions, such as selecting a me

## Categories

- Category:Articles with example Python (programming language) code
- Category:Computer graphics
- Category:User interfaces
- Category:Video game development

## Table of Contents

- Algorithm
- See also
- References
- External links

## Content

In computer graphics programming, hit-testing (hit detection, picking, or pick correlation) is the process of determining whether a user-controlled cursor (such as a mouse cursor or touch-point on a touch-screen interface) intersects a given graphical object (such as a shape, line, or curve) drawn on the screen. Hit-testing may be performed on the movement or activation of a mouse or other pointing device.
Hit-testing is used by GUI environments to respond to user actions, such as selecting a menu item or a target in a game based on its visual location. In web programming languages such as HTML, SVG, and CSS, this is associated with the concept of pointer-events (e.g. user-initiated cursor movement or object selection).
Collision detection is a related concept for detecting intersections of two or more different graphical objects, rather than intersection of a cursor with one or more graphical objects.

Algorithm
There are many different algorithms that may be used to perform hit-testing, with different performance or accuracy outcomes. One common hit-test algorithm for axis aligned bounding boxes. A key idea is that the box being tested must be either entirely above, entirely below, entirely to the right or left of the current box.  If this is not possible, they are colliding.  Example logic is presented in the pseudo-code below:

In Python:

See also
Point in polygon
Computational geometry
Collision detection
User interface

References
External links
MSDN: Hit Testing in the Visual Layer
MSDN: Hit Testing Lines and Curves

## Related Articles

### Internal Links

- [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Collision detection](https://en.wikipedia.org/wiki/Collision_detection)
- [Computational geometry](https://en.wikipedia.org/wiki/Computational_geometry)
- [Computer Graphics: Principles and Practice](https://en.wikipedia.org/wiki/Computer_Graphics:_Principles_and_Practice)
- [Graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface)
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [Point in polygon](https://en.wikipedia.org/wiki/Point_in_polygon)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [SVG](https://en.wikipedia.org/wiki/SVG)
- [User interface](https://en.wikipedia.org/wiki/User_interface)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:29:34.059410+00:00_