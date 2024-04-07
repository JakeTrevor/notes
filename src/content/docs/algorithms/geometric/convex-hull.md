---
title: Computing the Convex Hull
description: Given a cloud of points, compute their convex hull.
---

## Problem Definition

The convex hull of a cloud of points is the smallest polygon that contains all the points. Smallest here means smallest area or perimeter - they are equivalent in this case.

Given a cloud of points, compute their convex hull.

## Observation

one key observation: every vertex of the polygon that forms the convex hull will itself be a point in the point cloud.

The points with the largest and smallest x or y coordinates must be in the hull. The furthest pair of points in the cloud will also be on the hull.

## Graham Scan

Choose a point that must be on the hull (e.g. that with the largest x coordinate, breaking ties with largest y coordinate).

Scan the remaining points by order of their angle to the pivot (i.e. the order we would use when constructing a simple polygon from the last chapter).
For each point, temporarily include it in a temporary hull, and exclude any of its ancestors.

When we build the hull, we should always be turning left; If we turn right, we should exclude some number of previous points. Lets first define some terms; let $p_{new}$ be a new candidate point. let $p_{-1}$ be the previous point, $p_{-2}$ be the one before that, and so on.

We need to compare the angle between two lines: $-p_{new}-p_{-1}-$ and $-p_{-1}-p_{-2}-$. if this angle is greater than 180 degrees, then we know we have 'turned right' and we can exclude $p_{-1}$ from the hull. We repeat this until we find a predecessor we should not exclude.

The simple polygon algorithm has complexity $O(n \log n)$. The angle function has complexity $O(1)$ - though its implementation is outside the scope of this course.

:::note
check if this is true...!
:::

Every point is eliminated at most once, so the complexity of checking the angles is at most $O(n)$. Thus overall we have a time of $O(n \log n)$. Once again, the sorting dominates.

## Gift Wrapping

// todo - althought not sure might be outside course scope.
