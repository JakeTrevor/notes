---
title: Network flow
description: using network flow
---

## Problem definition

### Networks

A Network is a directed graph (digraph) $G = (V, E)$ such that:

- there is a vertex $s$ (the source) which has indegree 0
- there is a vertex $t$ (the sink) which has outdegree 0
- each edge $(u, v) \in E$ has a non-negative capacity $c(u, v) \in \mathbb{R}$.
- Every vertex lies on some path from $s$ to $t$
- non-existant edges have capacity 0;

### Flows

A flow in a network $G$ is a function $f : E \rightarrow \mathbb{R}$ that respects two constraints:

1. Capacity constraint:
   for every edge $(u, v)$, the flow on that edge respects $0 \leq f(u,v) \leq c(u,v)$.
2. Flow Conservation constraint:
   for every vertex other than $s$ and $t$, the incoming flow is equal to the outgoing flow.

The slack on an edge is the difference between its capacity and its flow; $s(u,v) = c(u,v) - f(u,v)$.
Logically, this represents how much more flow the edge can accept.

The value of a flow $\text{val}(f)$ is the total flow out from $s$ - or equivalently, the total flow into $t$.
A flow is _saturating_ if $f(s, v) = c(s, v)$ for all $v$.

A _maximum flow_ is a flow whose value is maximum



## Maximum Flow Problem:
input: A network $G = (V, E)$ with capacity function $c$.
output: A maximum flow $f$ in $G$.


## Augmenting Paths
The idea of augmenting paths applies in network flow too; although their definition is of course different.

An augmenting path with respect to a flow $f$ in a network $G$ is a path from $s$ to $t$ comprising edges of $G$ but not necessarily directed as in $G$.

Each edge $(u, v)$ in the path must satisfy one of the two following conditions:
1. A forwards edge: $(u,v) \in E$ (i.e. $(u,v)$ is in the same direction as in $G$) and $f(u, v) < c(u,v)$
2. A backwards edge: $(v, u) \in E$ (i.e. $(u,v)$ is opposite in direction to an edge in $G$) and $f(v, u) > 0$


## Augmenting Path theorem
A flow is maximum if and only if it admits not augmenting path.

**proof**:

Suppose a flow $f$ admits an augmenting path $P$
- this means we can push an additional flow of $m_i$ along each forwards edge
- We borrow flow from backwards edges (i.e. decrease the flow along backwards edges)


## Cuts
A cut is a set of edges separating the source from the sink
Formally:

let $V$ be partitioned into $A$ and $B$ where $s \in A$ and $t \in B$; $A \subseteq V$ and $B = V \setminus A$.
The cut is then the set of edges $C$ such that:
$$
C = \{ (u, v) \in E : u \in A \text{ and } v \in B\}
$$

The *capacity* of a cut $\text{cap}(C)$  is the sum of the capacities of the edges in $C$. 

A minimum cut is a cut whose capacity is minimum among all possible cuts.

We can use cuts to prove the 'if' part of the augmenting path theorem.
If we define a cut such that $\text{cap}(C) = \text{val}(f)$, then $f$ must be maximum, because no additional flow can get from $s$ to $t$, by definition of a cut.


suppose that $f$ admits no augmenting path;
Let $A \subseteq V$ be the set of vertices we can reach along a partial augmenting path from $s$, and let $B=V\setminus A$ so the absence of a complete augmenting path implies that $s \in A$ and $t \in B$.


// todo maybe fill in the proof here...

## Residual Graph
let $G = (V,E)$ be a network with capacity function $c$ and let $f$ be a flow in $G$.

the residual graph $G' =  (V', E')$ with respect to $G$ and $f$ is a directed graph defined such that:

$V' = V$ - the vertices of $G'$ are the same as those in $G$.

$(u, v) \in E'$ if and only if:
1. $(u, v) \in E$ and $f(u,v) < c(u, v)$ 
	1. I.e. The edge can be a forward edge in an AP
	2. the Capacity of such an edge is its slack; $c'(u, v) = c(u,v) - f(u,v) = s(u, v)$
2. $(v, u) \in E$ and $f(v,u) > 0$
	1. i.e. the edge can be a backwards edge in an AP
	2. the capacity of such an edge is the flow along it: $c'(u, v) = f(v, u)$


## Ford-Fulkerson Algorithm

We now have all the tools required to construct an algorithm to solve this problem. The Ford-Fulkerson algorithm works broadly by:
1. set flow of all edges in the matching to 0
2. search for an augmenting path
3. augment along that path
4. repeat until no augmenting path can be found.

Searching for an augmenting path is done with a residual graph. You can simply search from the source, looking for the sink. any such path found in the residual graph is an augmenting path for the matching. 

If we use BFS for this then the overall complexity becomes $O(|V|\ |E|^2)$. The absolute fastest algorithm to Date is $O(|V|\ |E|)$. 

