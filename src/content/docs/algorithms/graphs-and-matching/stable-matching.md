---
title: Stable Matching
description: Matching With Preferences
---
Some matching problems include a notion of stability.


STable Marriage Problem:
Input: n students and n lecturers each participant ranks all n members of the other side in strict order of preference.

Output: a stable matching

Definitions: 
A matching is a set of n disjoint (student, lecturer) pairs.
A blocking pair for a matching $M$ is a student lecturer pair $(s, l)\not\in M$ such that $s$ and $l$ prefer each other over their assigned partner in $M$

A matching is stable if it has no blocking pairs.


## Stability Checking:
to test weather $M$ is stable:
```
stable(M: matching) {
	for (s in students) {
		ls = lecturers s prefers to M(s)
		for (l in ls) {
			if (l prefers s to M(l)) {
				return false;
			}
		}
	}
	return true;
}
```
With an appropriate data structure, this has time $O(n^2)$.

A stable matching always exists for a given instance of the stable marriage problem as defined here.
We can find one quickly ($O(n^2)$ time) using the Gale-Shapley algorithm

## Gale-Shapley Algorithm
```
freeStudents = students
while (not freeStudents.isEmpty()) {
	s = freeStudents.pop()
	l = first lecturer on s's preference list s has not yet applied to
	if (l is free){
		assign(s, l)
	} else if (l prefers s to their partner) {
		freeStudents.push(l.partner())
		assign(s, l)
	}
	freeStudents.push(s) // l rejects s; s remains free
}
```


The algorithm is non-deterministic. The students can apply in any order; the result will be the same.