---
title: Simple Polygon Construction
description: Constructing a Simple Polygon from a set of points
---

## Problem Description

Given a set of $n$ points in the plane, connect them to form a simple polygon.

Using a naive method where we connect the points in any order does not work in general - we can't guarantee we will get a simple polygon.

## Idea 1: Circular scan

choose a point $p$ as a pivot; compute the angle from that point to each other point; sort by the angle.

This works so long as $p$ is one of the points in the cloud - for example, the one with the largest x coordinate. We then start and end the path with this point.

Computing the angle is constant time; we need to do this for each point in the cloud. Thus we have a complexity of $O(n)$. The sort can happen in $O(n \log n)$. Thus, overall this has time $O(n \log n)$.

A complication occurs if some number of points are collinear; to solve this, we sort the points additionally by increasing order of distance from the pivot.

There is one further special case: if the final run of points are collinear, then we need them to be sorted in decreasing order of distance to the pivot.
