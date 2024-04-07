---
title: Line Segment Intersection
description: Given two line segments, do they intersect?
---

## Problem definition:

Let us say that we have two line segments p-q and r-s. Do they intersect?

We can break this problem down into two sub-problems: the opposite sides test, and the bounding box text.

## Opposite sides test:

:::note
Are points q & p on opposite sides of the line r-s?
:::

We can define a function that tells us how close a given point is to the line; as follows:

$$
d = (l.p2.x - l.p1.x)(y - l.p1.y) - (l.p2.y - l.p1.y)(x - l.p1.x)
$$

When this function is 0, then the point lies on the line. Note however that this function is signed - when it is positive, the point is above the line, and when it is negative the point is below the line.

We can use this to solve our problem; First, let's translate the equation above into a function which tells us side of a line `l` a point`p` is on:

```
side(l: line, p: point) {
    return (l.p2.x - l.p1.x)(p.y - l.p1.y) - (l.p2.y - l.p1.y)(p.x - l.p1.x)
}
```

We can then check if two points are on opposite sides like so:

```
oppositeSides(l:line, p: point, q: point) {
    pSide = side(p)
    qSide = side(q)
    return pSide * qSide <= 0
}
```

## The bounding box

:::note
Given two lines, do their bounding boards intersect?
:::

```py
def boundingBoxIntersect(l1:segment, l3:segment) {
    l1_bottom =  min(l1.p1.x, l1.p2.x)
    l1_top =  max(l1.p1.x, l1.p2.x)
    l1_left =  min(l1.p1.y, l1.p2.y)
    l1_right =  max(l1.p1.y, l1.p2.y)

    l2_bottom =  min(l2.p1.x, l2.p2.x)
    l2_top =  max(l2.p1.x, l2.p2.x)
    l2_left =  min(l2.p1.y, l2.p2.y)
    l2_right =  max(l2.p1.y, l2.p2.y)

    return (
           l2_top >= l1_bottom
        && l2_right >= l1_left
        && l1_top >= l2_bottom
        && l1_right >= l2_left
    )
}
```

## Why?

We need both these tests to cover an edge case; The opposite sides test can check all cases of two line segments except when they are collinear. This can only be resolved with the bounding box test.
