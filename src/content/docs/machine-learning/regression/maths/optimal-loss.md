---
title: Analytic loss optimisation
description: An analytic solution for optimal loss with a simple linear model
---

With linear regression, our model has the form

$$
t = w_{0} + w_{1}x
$$

The loss therefore has the form:

$$
\mathcal{L} = \frac{1}{N}\sum_{n=1}^{N} (t_{n} - (w_{0} + w_{1}x_{n}))^{2}
$$

This is a quadratic equation in both $w_0$ and $w_{1}$ so we can minimise it with with the following:

$$
\frac{ \partial \mathcal{L} }{ \partial w_{0} } =0; \frac{ \partial \mathcal{l} }{ \partial w_{1} } =0;
$$

:::tip[Two keys rules]

### The sum rule:

$$
\frac{ d }{ dx } \sum f(x) = \sum \frac{ d }{ dx }  f(x)
$$

### The chain rule:

$$
\frac{ dy }{ dx } =\frac{ dy }{ du } \frac{ du }{ dx }
$$

Or put another way:

$$
\frac{ d }{ dx } f(g(x)) = g'(x) \cdot f'(g(x))
$$

:::

# Have a go at this now, yourself, if you like.

$$
\begin{align}
\frac{ \partial \mathcal{L} }{ \partial w_{0} } &= \frac{ \partial }{ \partial w_{0} }  \frac{1}{N}\sum_{n=1}^{N} (t_{n} - (w_{0} + w_{1}x_{n}))^{2} \\
&=\frac{1}{N}\sum_{n=1}^{N} \frac{ \partial }{ \partial w_{0} } (t_{n} - w_{0} - w_{1}x_{n})^{2} & \text{by sum rule} \\
&= \frac{1}{N}\sum_{n=1}^{N} -2(t_{n} - w_{0} - w_{1}x_{n})  & \text{by chain rule} \\
&= \frac{-2}{N}\sum_{n=1}^{N} (t_{n} - w_{0} - w_{1}x_{n})
\end{align}
$$

Now we can solve this for $w_0$:

$$
\begin{align}
0 & = \frac{-2}{N}\sum_{n=1}^{N} (t_{n} - w_{0} - w_{1}x_{n})\\
 & = \frac{-2}{N}\sum_{n=1}^{N}t_{n} - \frac{-2}{N}\sum_{n=1}^{N} w_{0} - \frac{-2}{N}\sum_{n=1}^{N}w_{1}x_{n} \\
  \frac{-2}{N}\sum_{n=1}^{N} w_{0} & = \frac{-2}{N}\sum_{n=1}^{N}t_{n} - \frac{-2}{N}\sum_{n=1}^{N}w_{1}x_{n}  \\
-2 w_{0} & = \frac{-2}{N}\sum_{n=1}^{N}t_{n} - \frac{-2}{N}\sum_{n=1}^{N}w_{1}x_{n}  \\ \\
-2 w_{0} & = -2 \bar{t} - (-2)\cdot w_{1}\bar{x} \\ \\
w_{0} & =\bar{t} - w_{1}\bar{x} \\
\end{align}
$$

Next, we take the derivative with respect to $w_1$.

$$
\begin{align}
\frac{ \partial \mathcal{L} }{ \partial w_{1} } &= \frac{ \partial }{ \partial w_{1} }  \frac{1}{N}\sum_{n=1}^{N} (t_{n} - (w_{0} + w_{1}x_{n}))^{2} \\
&=\frac{1}{N}\sum_{n=1}^{N} \frac{ \partial }{ \partial w_{1} } (t_{n} - w_{0} - w_{1}x_{n})^{2} & \text{by sum rule} \\
&= \frac{1}{N}\sum_{n=1}^{N} -2x_{n}(t_{n} - w_{0} - w_{1}x_{n})  & \text{by chain rule} \\
&= \frac{-2}{N}\sum_{n=1}^{N} x_{n}(t_{n} - w_{0} - w_{1}x_{n}) \\
&= \frac{-2}{N}\sum_{n=1}^{N} (t_{n}x_{n} - w_{0}x_{n} - w_{1}x_{n}^{2})
\end{align}
$$

We can now solve for $w_{1}$:

$$
\begin{align} \\
0 &= \frac{-2}{N}\sum_{n=1}^{N} (t_{n}x_{n} - w_{0}x_{n} - w_{1}x_{n}^{2}) \\
&= \frac{-2}{N}\sum_{n=1}^{N}t_{n}x_{n} - \frac{-2}{N}\sum_{n=1}^{N}w_{0}x_{n} - \frac{-2}{N}\sum_{n=1}^{N}w_{1}x_{n}^{2} \\
\frac{-2}{N}\sum_{n=1}^{N}w_{1}x_{n}^{2} &= \frac{-2}{N}\sum_{n=1}^{N}t_{n}x_{n} - \frac{-2}{N}\sum_{n=1}^{N}w_{0}x_{n} \\
\frac{1}{N}\sum_{n=1}^{N}w_{1}x_{n}^{2} &= \frac{1}{N}\sum_{n=1}^{N}t_{n}x_{n} - \frac{1}{N}\sum_{n=1}^{N}w_{0}x_{n} \\
w_{1}\bar{x^{2}} &= \bar{tx} - w_{0}\bar{x}
\end{align}
$$

and substitute in $w_{0}$:

$$
\begin{align}
w_{0} & =\bar{t} - w_{1}\bar{x} \\
w_{1}\bar{x^{2}} &= \bar{tx} - (\bar{t} - w_{1}\bar{x})\bar{x} \\
w_{1}\bar{x^{2}} &= \bar{tx} - \bar{t}\bar{x} + w_{1}\bar{x}^{2} \\
w_{1}\bar{x^{2}} - w_{1}\bar{x}^{2} &= \bar{tx} - \bar{t}\bar{x} \\
w_{1} (\bar{x^{2}} -\bar{x}^{2}) &= \bar{tx} - \bar{t}\bar{x}  \\ \\
w_{1} &= \frac{\bar{tx} - \bar{t}\bar{x} }{\bar{x^{2}} -\bar{x}^{2}}
\end{align}
$$

We now have a value for $w_{1}$ in terms of $x$ and $t$; substituting this value back into $w_{0}$, we get the pair of equations:

$$
\begin{align}
w_{0} & =\bar{t} - \left(\frac{\bar{tx} - \bar{t}\bar{x} }{\bar{x^{2}} -\bar{x}^{2}} \right)\bar{x} \\ \\
w_{1} &= \frac{\bar{tx} - \bar{t}\bar{x} }{\bar{x^{2}} -\bar{x}^{2}}
\end{align}
$$
