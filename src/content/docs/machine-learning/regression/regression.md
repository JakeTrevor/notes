---
title: Regression
description: A quick reference/recap for basic regression
---

Finished the worksheet? Let's recap the key ideas quickly. Nothing here should be too surprising.

Let's say that we have some data that comes in pairs of values ($x_{n}, t_{n}$). In regression, we assume it takes the form:

$$
t_{n} = f(x_{n} | w)
$$

Where $f$ is a continuous function, and $w$ is a collection of parameters to that function. $f$ and $w$ together form our model.

## Loss ($\mathcal{L}$)

We want a way of assessing how good our model is. To do we find the difference between the true value the prediction of the model at some point $n$:

$$
\mathcal{l}_{n} = t_{n} - f(x_{n}|w)
$$

This is called the loss. We want this value to be a measure of 'wrongness' - it should be positive if the prediction is either more or less than the true value. We can accomplish by just squaring the loss:

$$
\mathcal{L}_{n} = (t_{n} - f(x_{n}|w))^{2}
$$

Finally, we want to know how our model performs as a whole across all our data; so we take the mean of the loss:

$$
\mathcal{L} = \frac{1}{N}\sum_{n=1}^N (t_{n} - f(x_{n}|w))^{2}
$$

This is called the mean squared error (MSE). This gives us a measure of how good the model is, and so it works as a kind of loss. The higher the loss, the worse the model.

## Optimising a model

We want to get the best model we can. Lets ignore how we would choose $f$ for now and focus only on $w$. We want to minimise the loss with respect to $w$. This is the principal question at the heart of regression, and it takes the form:

:::tip
_Find the parameters $w$ to the model that minimises the loss_

$$\argmin_{w}\ \mathcal{L} \left(w | x, t\right)$$
:::

There are several ways to go about doing this. Often, its possible to find a perfect analytical solution; Checkout [[Linear Regression - Analytical Solution]] for a worked example. For simple linear models, the equations are:

$$
\begin{align}
w_{0} & =\bar{t} - \left(\frac{\bar{tx} - \bar{t}\bar{x} }{\bar{x^{2}} -\bar{x}^{2}} \right)\bar{x} \\ \\
w_{1} &= \frac{\bar{tx} - \bar{t}\bar{x} }{\bar{x^{2}} -\bar{x}^{2}}
\end{align}
$$
