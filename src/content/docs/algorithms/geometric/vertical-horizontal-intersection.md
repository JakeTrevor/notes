---
title: Intersection of Vertical and Horizontal Segments
description: finding all the intersections of a set of vertical and horizontal lines.
---

## Problem Definition

Given a set of $h$ horizontal lines and $v$ vertical lines, find all intersections.

Let us also assume that no two horizontal lines intersect, and no two vertical lines intersect.

## Naive solution

Examine all pairs. Each pair can be checked in $O(1)$ time, but this is still $O(hv)$. No algorithm can be better than this in the worst case - after all, every pair of lines could intersect.

However, we can do better when the number of intersections $p$ is small.

## Line Sweep

Line sweep is a powerful general technique. We will show how to use it for this problem, but you can apply its main ideas for many other geometric algorithms.

In this case, our algorithm will have time $O(n \log n + p)$ where $n = h + v$.

Imagine a line sweeping across the plane, left to right. This will hit each vertical line once; and each horizontal line twice (at its beginning and end).

To simulate this for our algorithm, we create a set of endpoints. Each vertical line is represented once, and each horizontal line by its two end points. This list is then sorted by x-coordinate, but on ties we need to use the order:

1. horizontal staring points
2. vertical lines
3. horizontal end points

This ensures that we catch intersections with the endpoints of lines.

We simulate the sweep by processing this list of lines. As we move through the list, we maintain a candidate list of horizontal lines that are currently 'open'. Segments are added to the list when we encounter their start point, and removed when we encounter their end point.

When a vertical line is encountered, we need only check those lines in the candidate set. In many cases, this provides a real speed up.

### Range search

How can we represent a candidate set so that we don't have to compare all candidates?

When we check for intersections with this method, we already know that the segments have the right x-coordinates to intersect; so we only need to check the y coordinate. Vertical lines have a minimum y and maximum y; we know it will intersect with all horizontal lines in the candidate set with a y in that range. So we want to perform a range search. How can we do this?

A naive method is to simply perform a binary search for the low and high y coordinates in a sorted list. This would have time $O(\log n)$ on the number of candidates - $O(\log h)$ in the worst case. However, there is a problem; for this to work, the candidate list would need to be kept sorted. This would be slow - in general $O(n)$. We can do better!

The solution is to use an alternate data structure: an AVL Tree. An AVL tree is a balanced binary search tree. For each node, the heights of its children differ by at most 1.

Search, insertion and deletion are all $O(n)$ on the number of horizontal lines.

The range search of $O(k + \log h)$; where $k$ is the actual number of intersections.

// TODO: a worked example of this; why is it K + log n and not 2 log n?

If we use an AVL tree, then our vertical-horizontal intersection check becomes $O(n \log n + p)$ overall.
