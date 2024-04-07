---
title: Introduction to String and Text Algorithms
description: Key terms and key ideas for string and text algorithms
---

## Key Terms

An **alphabet** is a set of **symbols**; we might write

$$
\Sigma = {A, B, C}
$$

A **string** in an alphabet is an

let $S$ and $T$ be two strings; then:
- $|S|$ is the length of $S$
- $S(i)$ is the $i^{\text{th}}$ character symbol of $S$.
- $S(i..j)$ denotes the substring from positions $i$ to $j$ in $S$; formally:
	$S(i..j) = S(i)S(i+1)...S(j)$
- $ST$ is the concatenation of the two strings
- $\varepsilon$ is the empty string, and has length 0.

By convention, strings are index from 1

A substring of $S$ is $\varepsilon$ or $S(i..j); i \leq j$ 
$U$ is a substring of $S$ if and only if $S = TUV$ for some strings $T$ and $V$.

A common substring $U$ of two strings $S$ and $T$ is a string which is a substring of both $S$ and $T$.

A subsequence of a string $S$ is obtained by deleting zero or more characters from $S$.

A common subsequence $U$ of two strings $S$ and $T$ is a subsequence of both $S$ and $T$.


A prefix is a substring at the start of the string; formally a string $U$ is a substring of $S$ if $U = S(1..k)$ for some $1 \leq k \leq |S|$.

A suffix is a substring at the end of the string; formally a string $U$ is a substring of $S$ if $U = S(k..|S|)$ for some $1 \leq k \leq |S|$.

The $k^{\text{th}}$ suffix of $S$ is the last $k$ characters of $S$; $S(k..|S|)$

$\Sigma^*$ is the set of all strings composed of symbols in $\Sigma$.


---

Some tree terminology:
- a Leaf node has no children
- a branch node has one or more children.
- a unary node has exactly one child
- a binary node has exactly two children




