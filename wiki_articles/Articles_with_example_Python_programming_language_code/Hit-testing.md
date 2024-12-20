---
title: Hit-testing
url: https://en.wikipedia.org/wiki/Hit-testing
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Computer graphics", "Category:User interfaces", "Category:Video game development"]
references: 0
last_modified: 2024-11-09T01:05:39Z
---

# Hit-testing

## Summary

In computer graphics programming, hit-testing (hit detection, picking, or pick correlation) is the process of determining whether a user-controlled cursor (such as a mouse cursor or touch-point on a touch-screen interface) intersects a given graphical object (such as a shape, line, or curve) drawn on the screen. Hit-testing may be performed on the movement or activation of a mouse or other pointing device.
Hit-testing is used by GUI environments to respond to user actions, such as selecting a me

## Full Content

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
