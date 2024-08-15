<style> *{ font-family: 'FiraCode NF'; } </style>

# Diversity 

---

## Ambiguity

Imagine I search for 'rio'

What am I searching for?
- the movie?
- the place?

Many possibilities...

---

## Repetetive results

imagine searching for rio and only geting results for the city

Is that useful?

Would getting other results be more useful?

---

## Diversity

We use diversity to:
- deal with the ambiguity of queries
- reduce redundancy

---

### In Recommender systems

Obviously, we don't really have search queries
-> this isnt IR!

instead, our goals are a bit different

> Avoid redundancy of possible user intents (aspects) as a means to cope with the ambiguity in the observed evidence of user interests


---
### Why bother?

- increases the chance of a 'lucky guess' -> system effectiveness
- help users 'broaden their horizons' -> discovery
- broaden sales diversity -> business performance

---

## How to diversify Recommendations

- rec-sys approaches essentially 'rank' a bunch of items individually (independently of each other)
- key idea of diversity: items depend on each other -> no independence
- most diversification methods *re-rank* the retrieved items

(can you tell this is very much related to IR?)

---

## Greedy approach (Best first search)

- Each iteration, select the item that maximises *diversity*
- Problem: we still need to incorporate our relevance score...
- Each iteration, select the item that maximises ~~*diversity*~~ *some scoring function* `F`


---

### Greedy algorithm:

```
options = set of all items
selected = {}
while (|selected| < threshold) {
	next_item = item i in options that maximises F(i)
	selected.add(next_item)
	options.remove(next_item)
}
```

---
### MMR

One implementation of this greedy approach is Maximal Marginal Relevance
-> maximise the relevance of the *next item*

Turns out to be basically state-of-the-art

$$
f_{mmr}(u, i, S) = \lambda \text{rel}(u ,i) - (1-\lambda) \max_{\forall j\in S} \{ \text{sim}(i, j) \}
$$

Where $u$ is the user, $i$ is the item, and $S$ is the set of selected items. 

note that $\lambda$ is a normalisation term between 0 and 1 that controls how much weight we give to the relevance vs the similarity.


---

In general, diversification is NP-hard
we need to consider all combinations to find the true optimum...

but a greedy approximation is:
- fast to compute
- good enough

Note that the most relevant item is always selected first, since the `selected` starts empty

---

## Category coverage

Another option for diversification;  again applied via greedy search
Basic idea: score an item according to the categories it covers

$$
f_\text{IA-Select} (u, i, S) = \sum_{c \in T} f(c | i, S) f(i | u, c)
$$

Where $u$ is the user, $i$ is the item, and $S$ is the set of selected items. 

$f(c | i, S)$ is the category coverage - a measure of how well the category $c$ is already represented in $S$.

$f(i|u, c)$ is the category utility - a measure of how useful the item $i$ is in the category $c$

---

IA-Select picks items that:
- cover categories useful to the user
- are in a category that is not well represented in the set already


---

## Aspect diversification

Similar to IA-Select
idea: use user & item features as categories!

---

# Evaluation

---
## RecSys novelty & diversity metrics...
- are not defined in terms of ranking
- do not involve relevance

we use different metrics for different things
metrics include:
- intra-list diversity
- unexpectedness
- inverse popularity
- others (we won't cover)

---

### Intra-list diversity (ILD)
> average pairwise distance

$$
\text{ILD} = \frac{2}{|R| (|R| - 1)} \sum_{i,j \in R.\ i\neq j} d(i, j)
$$
where $d$ is some distance measure; we can use:
$1-\text{sim} (i, j)$, with $\text{sim}$ = cosine, Jaccard, etc. on item features


---
### Unexpectedness
> average distance to items the user has already seen
$$
\text{Unexp} = \frac{1}{|R|, |u|} \sum_{(i, j) \in R\times u} d(i,j)
$$

- $u$ is the set of items the user has seen

---

### Inverse Populairty 
> "mean self-information"
> no that doesn't mean anything to me either
> score is high if it recommends 'niche' items (i.e. items in the long tail)


$$
\text{MSI} = - \frac{1}{|R|} \sum_{i\in R} \log_2 \text{pop}(i)
$$

where $\text{pop}$ is the popularity of $i$
definition is weird, check slides


---

### Temporal Diversity
does the recsys evolve over time?

$$
\begin{align*}
\text{tempdiv} = \frac{| R_{t} - U_{t'}R_{t'}| }{|R_{t}|} && \text{where $t' < t$}
\end{align*}
$$
i.e. where $t'$ is before $t$
Literally:
> what proportion of our recommendations are new?