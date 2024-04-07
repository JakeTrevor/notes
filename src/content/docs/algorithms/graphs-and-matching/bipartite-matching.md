---
title: Matching in bipartite graphs
description: title still says it all.
---

## Problem Definition

### Terminology

A bipartite graph is a graph $G=(V,E)$ where $V$ can be partitioned into a left $U$ and right $W$ such that every edge in $E$ joins a vertex in $U$ to a vertex in $W$.

A matching in $G$ is a subset $M$ of $E$ such that no two edges in $M$ have a vertex in common.

A Maximum cardinality Matching in $G$ is a matching that contains the largest number of edges possible.

It is _perfect_ if every vertex is incident to an edge; if $|M| = |V| / 2$

Let's call the left hand side students, and the right hand side projects.

### Maximum Matching problem:

Given a bipartite graph $G$, output a maximum cardinality matching $M$ in $G$.

## Naive

Brute force - try all assignments. Let's assume that we have $n$ students and $n$ projects.

For each assignment, we need to check if it is a matching, and then we need to select the largest one we find. There are more than $n!$ possible assignments to try. This is not a feasible growth rate; the problem becomes intractable very quickly.

## Augmenting Paths

given a matching $M$ in a bipartite graph $G$:

a vertex $u$ is matched if $\{u, v\} \in M$ for some vertex $v$. We say that $u$ and $v$ are _mates_.

a vertex is _exposed_ if it is not matched;

An alternating path contains edges that are in $M$ and not in $M$ alternately.

An augmenting path for $M$ is an alternating path which starts and ends at exposed vertices.

We can _augment_ along an augmenting path by removing from $M$ the edges in the path which are already in $M$ and replacing them with the edges that are not currently in $M$.

_Critically_, this new matching always has a larger cardinality. Augmenting along an AP makes the matching bigger.

### Augmenting Path Theorem:

A matching $M$ is of maximum cardinality if and only if it permits no augmenting path.

Proof:
If $M$ permits an augmenting path, then it cannot be maximum cardinality, as we have seen.

the converse is too hard and I dont understand it. // TODO fix that...

## Augmenting Path Algorithm

The key idea is to perform a kind of breadth-first search; starting with exposed nodes in the left hand side. We traverse left-to-right using edges not in the matching; and right-to-left using edges in the matching. We keep searching until we find an agumenting path (i.e. a path which starts and ends on an exposed vertex).

```
augmentingPath(G: Bipartite) {
    matching = {}
    path = findAugmentingPath(G, M)
    while (path) {
        M = augment(M, path)
        path = findAugmentingPath(G, M)
    }
    return M
}
```

## Analysis

- Searching for an augmenting path takes $O(|U| + |E|)$ time.
- Augmenting along that path takes $O(|E|)$ time.
- there are at most $|U|$ iterations of this;
- thus overall we have $O(|U| \cdot (|U| + |E|))$ time;
- $|U| \propto n$, and $|E| \propto n^2$;
- therefore overall: $O(n^3)$ time.
