---
title: Furthest Pair
description: Find the furthest pair of points in a cloud.
---

## Problem Description

Given a point cloud $S$, we want to find the pair of points in that cloud $p, q$ which are the furthest apart.

There can be more than one such pair; for example, consider if all the points in the cloud were in pairs, lying on opposite sides of a circle. Each pair would be a valid solution.

## Naive solution

A simple solution might be to compare every pair of points in the cloud. This is $O(n^2)$ on the number of points in the cloud - quite slow, and we can do better!

The first observation is that the furthest pair of points will always lie on the convex hull of the cloud. So a small improvement is to compare only the points on convex hull. This is marginally better - its $O(n^2)$ on the number of points on the hull. However, in the worst case every point in the cloud is on the hull.

One observation to make is that two 'adjacent' points are not going to be further apart than two that lie on opposite sides of the hull. How can we capture that intuition?

## Rotating Calipers method

The first step in finding the furthest pair then is computing the convex hull. This can be done in $O(n \log n)$ time.

Choose two points $p$ and $q$ on the convex hull, such that they have the maximum and minimum y coordinate in the cloud, respectively.

We draw a horizontal line through each of $p$ and $q$ (call them $l_1, l_2$), and record the distance between the two points. These lines form the 'calipers'

we then rotate the calipers, ensuring they are always parallel. When one encounters a new point on the hull, the line should then pivot about that point instead. We should also check the distance between the new pivot and the other point and record it.

We do this until the calipers have rotated 180 degrees - at which point they will have swapped pivots. The furthest pair of points are the ones with the greatest distance between them.
