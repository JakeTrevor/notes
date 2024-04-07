---
title: Vectorised Regression
description: How do we vectorise linear regression?
---

On the last sheet, we looked at a formulation for regression that worked on single points (a 'pointwise' description). In this sheet we will look at how we can describe linear regression instead in terms of vectors.

Recall the formula for simple linear regression:

$$
y = w_0 + w_1 x
$$

## Background: Linear Algebra

To understand how we can use vectors to model this, we need to think about matrix multiplication. Let's start with a very simple example:

$$
\begin{bmatrix}
    a & 0 \\ 0 & b\\
\end{bmatrix}
\begin{bmatrix}
    x\\
    y\\
\end{bmatrix}
$$

What does that mean? A simple intuition is that each column in the matrix describes how each row in the vector should be transformed. We can expand out the result as so:

$$
\begin{bmatrix}
    xa + 0y\\
    0a + by
\end{bmatrix} =
\begin{bmatrix}
    ax\\
    by\\
\end{bmatrix}
$$

So, every row in the matrix corresponds to a row in the resulting vector. An interesting result: if we have only a single row in the matrix, then the result is a single number. Let's look at annother example:

$$
\begin{bmatrix}
    a & b
\end{bmatrix}
\begin{bmatrix}
    x\\
    y\\
\end{bmatrix} = ax + by
$$

Now, that might look familiar; if we rename the variables in our vectors a little bit here, something interesting happens:

$$
\begin{bmatrix}
    w_0 & w_1
\end{bmatrix}
\begin{bmatrix}
    1\\
    x\\
\end{bmatrix} = w_0 + w_1 x
$$

This is exactly the same as our definition of simple linear regression! We have represented regression with vectors!

We typically give these vectors names; for example:

$$
\text{parameters} = w = \begin{bmatrix}
    w_0\\
    w_1
\end{bmatrix}
$$

and

$$
\text{data} = x = \begin{bmatrix}
1\\
x
\end{bmatrix}
$$

Note that to get the multiplication to work like we want, we need to use the transpose of the parameters vector; Thus we can re-write our model as:

$$
y = w^\intercal x
$$

## Going Further

This is quite useful, but can we go further? What if we tried to compute all our predictions at once? First lets think about the format we want our answer to be in:

$$
Y = \begin{bmatrix}
    y_1\\
    y_2\\
    y_3\\
    \vdots\\
    y_n
\end{bmatrix}
$$

We can stack all our values one on top of the other. So then how should our input data look?

$$
X = \begin{bmatrix}
    1 & x_1\\
    1 & x_2\\
    1 & x_3\\
    \vdots & \vdots\\
    1 & x_n
\end{bmatrix}
$$

Then, if we multiply this by $w$ from above:

$$
Xw = \begin{bmatrix}
    w_0 + w_1x_1\\
    w_0 + w_1x_2\\
    w_0 + w_1x_3\\
    \vdots\\
    w_0 + w_1x_n\\
\end{bmatrix}
$$

Which is exactly what we wanted. Note the difference with our earlier definition: its $Xw$, not $w^\intercal x$. If you don't understand why, try writing out some small matrices and doing the calculation by hand.

Our input data $X$ is called a design matrix, and as we will see, we can mess around with it to acheive all sorts of effects.

## Vectorised loss

We'd also like to vectorise our loss; Recall that it looks like;

$$
\mathcal{L} = \frac{1}{N}\sum_{n=1}^N (t_{n} - w_{0}-w_{1}x_{n})
$$

We can re-write this a bit with our vectorized form for $t_{n}$:

$$
\mathcal{L} = \frac{1}{N}\sum_{n=1}^N (t_{n} - \vec{x}^\top w)^{2}
$$

:::note[A nice mathematical fact:]
Let $q_{n}$ be a row in matrix $Q$ with $D$ rows. Then:

$$
\sum_{n=1}^D(q_{n})^{2} = Q^\top Q
$$

:::

In our expression for loss, it looks like we have a row in the following matrix:

$$
(t_{n} - \vec{x}^\top w) \in t - X\vec{w}
$$

This allows us to re-write loss in a nice vector form:

$$
\mathcal{L} = \frac{1}{N} (t-X\vec{w})^\top (t-X\vec{w})
$$

## Minimising loss:

Remember, we want to minimise the loss to get the optimal value. This in general fulfils the equation:

$$
\frac{ \partial \mathcal{L} }{ \partial w }  = \nabla_{w}\mathcal{L} = 0
$$

Through the power of _don't worry about it_ and _maths_, we can find optimal $w$:

$$
\hat{w}=(X^\top X)^{-1} X^\top t
$$

Deriving this is outside the scope of the course. If you're interested, there's a derivation [[vectorised lin reg|here]].
