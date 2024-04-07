---
title: Gradient Descent
description: Using gradient descent to solve regression
---

# Gradients

Lets say we have some function $f$ on some set of values $w_{1}, w_{2}, \dots w_{n}$.
Then its gradient ($\nabla f$) is given by:

$$
\nabla f = \begin{pmatrix}
\frac{ \partial f }{ \partial w_{1} }  \\
\frac{ \partial f }{ \partial w_{2} }  \\
\dots \\
\frac{ \partial f }{ \partial w_{n} }
\end{pmatrix}
$$

> [!info] notice:
> $f$ is a function that operates on a list (or a vector) of values, so its gradient is also a list (or a vector) of values.

The gradient of $f$ points in the direction of steepest ascent; therefore, the **opposite direction** is direction of steepest descent.

## Gradient Descent

The idea of gradient descent is to descend the curve as quickly as possible, hopefully moving towards its minimum.

Gradient descent isn't an exact, analytical solution. It's imprecise and iterative. Ideally, each iteration of gradient descent will get you closer and closer to the exact solution, even if you never actually reach it.

One iteration or 'pass' of gradient descent looks like this:

$$
w_{\text{new}} = w_{\text{old}} - \alpha \nabla f
$$

The only new thing here is $\alpha$. $\alpha$ is the learning rate - a hyper-parameter that controls the size of the step we take on each pass.

Intuitively, higher values of alpha will move us towards the solution quicker, but too high a value can cause you to overshoot. Picking the right $\alpha$ is an optimisation value.

We can write the whole gradient descent algorithm like so:

```pa
w = [1, 3, /* ... */]
alpha = 0.01 // learning rate
notConverged = true

while notConverged {
		for i in [0 to w.length] {
			g = (d Loss(w)/ d w[i]) // not accurate to life
			w[i] = w[i] - alpha * g
		}
		notConverged = checkConvergence()
}
```
