When we divide two numbers, we get an equation in the form:
$$
\frac{A}{B} = Q \text{ remainder } R
$$
The remainder, $R$, can take on a limited set of values; Its an integer in the range $[0,\ B-1]$.

The modulo operator (in mathematics written as $a \mod b$, and in most programming languages as `a % b`) takes the remainder of $\frac{a}{b}$. 

In modular arithmetic, if $a\equiv a \mod n$, and $x$ is its inverse, $a$ and $x$ satisfy the following equation:

$$
ax \equiv 1 \mod n
$$
In general, Modular arithmetic does not guarantee that inverses exist; for example, consider the inverse of $2 \mod 4$. No remainder is possible:
$$
\begin{align}
0\cdot2 = 0 \equiv 0 \mod 4\\
1\cdot2 = 2 \equiv 2 \mod 4\\
2\cdot2 = 4 \equiv 0 \mod 4\\
3\cdot2 = 6 \equiv 2 \mod 4\\
\end{align}
$$
A number $a$ has a multiplicative inverse in modular arithmetic when its greatest common divisor with the base ($n$) is 1; 
in other words, when $a$ and $n$ have no common factors, $a$ will have an inverse $\mod n$.

If $n$ is a prime, then all numbers $a$ will have an inverse!

---

## The homomorphism Theorem

We can perform the modulus operation whenever it is convenient - the answer is always the same.

This should hopefully be obvious for addition & subtraction.
However it also works for multiplication!

for example:
$$
\begin{align}
(20 \cdot 11)\mod 7\\\\
20 \cdot 11 = 220\\
220 \mod 7 = 3\\\\
20 \mod 7 = 6\\
11 \mod 7 = 4\\


6 \cdot 4 = 24 \\
24 \mod 7 = 3
\end{align}
$$

