---
title: Introduction to Geometric algorithms
description: An introduction to geometric algorithms; some key terms and definitions
---

# Key terms, notation

A point $p$ is a point in 2D space, with attributes $x$ and $y$. We refer to them as $p.x$ and $p.y$.

A line is an infinite line in 2D space, described by two points p and q. We notate it $-p-q-$.

A line segment (or just a segment) is a finite section of an infinite line, notated $p-q$, where $p$ and $q$ are the endpoints.

A path is a sequence of distinct points $p_1, p_2, ... p_n$.

A polygon is a closed path --- i.e. one where $p_1 = p_n$.

A simple polygon is a polygon with no self-intersections; it encloses a region, its' inside.

a convex polygon is one where for every pair of points $p, q$ inside the polygon, no point on the segment between the two is outside the polygon.

Intuitively, convex polygons have no 'indents' in their surface.
