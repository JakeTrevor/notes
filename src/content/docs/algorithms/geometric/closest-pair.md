---
title: Closest Pair
description: Find the closest pair of points in a cloud.
---

## Problem definition

Given a cloud $P$ of $n$ points, find the pair with the least distance between them.

## Naive algorithm

Check each pair. This would be $O(n^2)$.

## Divide and conquer

A much better approach to this problem is to use a divide and conquer approach, based on the main ideas in merge sort. The basic idea is as follows:

1. First, we sort $P$ by x-coordinate once, at the outset.
2. We then divide $P$ into equally sized subsets $Q$ and $R$, again based on x-coordinate.
3. In each subset, we find the closest pair (by recursively appling this algorithm).
4. We then combine these results to find the closest pair in the overall set.

### Combining sets

When we combine the sets, there are three cases to consider. the closes pair $p$ and $q$ are:

1. Both in $Q$
2. Both in $R$
3. One is in $Q$ and one is in $R$.

How do we efficiently deal with case 3?

First, note that there will be some minimum distance $d$ within $Q$ and $R$ - they will have a closest pair of points within their own sets, even if that is not the global case. Thus, the true true closest pair will have a distance $\leq d$.

Note also that if the closet pair are split across $Q$ and $R$, then the pair must be close to the border between the two. Thus, we can eliminate all points in $Q$ and $R$ that are further than $d$ from the border between the two sets. This area, within a distance $d$ of the boarder, is called the strip.

If we sort the points in the strip by their $y$ coordinate, then we only need to check the 5 points after each point to be sure.

If we do this sorting each time, we end up with an $O(n \log ^2 n)$ time algorithm. However, we can do better!

the trick is to mimic merge sort further; if we assume that the points in $Q$ and $R$ are sorted by increasing order of $y$ coordinate, then we can combine them with a merge procedure. This merging ensures that the overall set $P$ is sorted wrt $y$ coordinate. Thus, the sorting actually happens naturally, when applying the closest pair algorithm!

This results in an even better $O(n \log n)$ time algorithm.

## Implementation

```
closestPair(p: Cloud) {
    p = sortOnXCoord(p)
    return closestPairRecursive(p, 0, p.length-1)
}

closestPairRecursive(p: point[], left: int, right: int) {
    if (left == right) return MAX_VALUE

    midpoint = (left+right) /2

    border = (p[midpoint] + p[midpoint +1]) /2

    dist_left = closestPairRecursive(p, left, midpoint)
    dist_right = closestPairRecursive(p, midpoint +1, right)

    merge(p, left, midpoint, right)

    d = min(dist_left, dist_right)

    strip = filter(p, left, right, d, border) // return all points within the strip (border +- d)

    m = strip.length
    for (i in [0..m]) {
        for (j in [0.. min(i+5, m)]) {
            if (dist(strip[i], strip[j]) < d) {
                d = dist(strip[i], strip[j])
            }

        }
    }

    return d;
}
```
