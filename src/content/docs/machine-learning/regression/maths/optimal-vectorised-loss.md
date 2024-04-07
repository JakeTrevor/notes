---
title: Analytic loss optimisation for vectors
description: An analytic solution for optimal loss with a simple linear vector model
---

## Fist, some rules:

$$
\begin{align} \\
(1) &  & (\vec{a}+\vec{b})^\top &= \vec{a}^\top + \vec{b}^\top &  & \text{sum associativity} \\
(2) &  & \left(\vec{a} * \vec{b}\right)^\top &= \vec{b}^\top * \vec{a}^\top &  & \text{product associativity} \\  &  &  &  &  & \text{note that the order reverses}\\
(3) &  & \frac{ \partial  }{ \partial x } \vec{x}^\top a &= a \\ \\
(4) &  & \frac{ \partial  }{ \partial x } a\vec{x} &= a^\top \\ \\
(5) &  & \frac{ \partial  }{ \partial x } \vec{x}^\top\vec{x} &= 2\vec{x} \\ \\
(6) &  & \frac{ \partial  }{ \partial x } \vec{x}^\top a \vec{x} &= 2a\vec{x} \\ \\
\end{align}
$$

First, We need to expand the expression for loss into something we can work with:

$$
\begin{align}
\mathcal{L}

 & = \frac{1}{N} (t-X\vec{w})^\top (t-X\vec{w}) \\


 & = \frac{1}{N} (t^\top-(X\vec{w})^\top) (t-X\vec{w})  & \text{by (1)}\\


 & = \frac{1}{N} (t^\top-\vec{w}^\top X^\top) (t-X\vec{w})  & \text{by (2)}\\


 & = \frac{1}{N} \left( t^\top t - \vec{w}^\top X^\top t - t^\top X\vec{w} + \vec{w}^\top X^\top X\vec{w} \right)

\end{align}
$$

Next, we need the derivative $\frac{ \partial \mathcal{L} }{ \partial \vec{w} }$

$$
\begin{align}
\frac{ \partial \mathcal{L} }{ \partial \vec{w} }

 & =\frac{ \partial}{ \partial \vec{w} }  \frac{1}{N} \left( t^\top t - \vec{w}^\top X^\top t - t^\top X\vec{w} + \vec{w}^\top X^\top X\vec{w} \right) \\

 & = \frac{1}{N} \frac{ \partial }{ \partial \vec{w} } \left( t^\top t - \vec{w}^\top X^\top t - t^\top X\vec{w} + \vec{w}^\top X^\top X\vec{w} \right) \\
\end{align}
$$

Note that there are four terms added together. We can differentiate these separately:

$$
\begin{align}
\frac{ \partial  }{ \partial \vec{w} } (t^\top t) & = 0 \\
\frac{ \partial  }{ \partial \vec{w} } \left( -\vec{w}^\top X^\top t \right)  & = -X^\top t & \text{by (3)}\\
\frac{ \partial  }{ \partial \vec{w} } (-t^\top X \vec{w}) &= (-t^\top X)^\top  & \text{by (4)}\\
 & = -X^\top t  & \text{by (2)}\\
\frac{ \partial  }{ \partial \vec{w} } \left( \vec{w}^\top X^\top X\vec{w} \right)  & = 2 X^\top X \vec{w} & \text{by (6)}
\end{align}
$$

And then add the terms back together, so we get:

$$
\begin{align}
\frac{ \partial \mathcal{L} }{ \partial \vec{w} }
&= \frac{1}{N}  \left( 0 - X^\top t   - X^\top t + 2X^\top X\vec{w} \right)\\
&= \frac{1}{N}  \left( 2X^\top X\vec{w} -2 X^\top t \right)\\
&= \frac{2}{N}  \left( X^\top X\vec{w} - X^\top t \right)\\
\end{align}
$$

### Finally, some simple algebra to solve:

$$
\begin{align}
\frac{ \partial \mathcal{L} }{ \partial \vec{w} }  & = 0 \\
\frac{2}{N}  \left( X^\top X\vec{w} - X^\top t \right)  & = 0\\
X^\top X\vec{w} - X^\top t  & = 0\\
X^\top X\vec{w} & = X^\top t  \\
\cancel{(X^\top X)^{-1}X^\top X}\vec{w} & = (X^\top X)^{-1}X^\top t  \\
\hat{w} & = (X^\top X)^{-1} X^\top t
\end{align}
$$
