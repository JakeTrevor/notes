# exclusive Or (XOR)
Exclusive Or ($\oplus$) is a binary Boolean operation which requires exactly one of its inputs to be true to return true;

Its truth table is identical to single-bit addition and subtraction (i.e. 1+1 = 10, but we throw away the first digit):

$$
\begin{align}
1 + 1 = 1 - 1 = 1 \oplus 1 = 0\\\\
1 + 0 = 1 - 0 = 1 \oplus 0 = 1\\\\
0 + 1 = 0 - 1 = 0 \oplus 1 = 1\\\\
0 + 0 = 0 - 0 = 0 \oplus 0 = 0
\end{align}
$$
Another way to think about this: `XOR` applies a bitwise mod 2 operation to its inputs.

`XOR` is equivalent to a !=; when the two values are the same, we get `0` (`false`), when the two values are different, we get `1` (`true`)

`XOR` can also be used to swap two variables without use of a third variable:
```js
//any values
a = 10 
b = 20 

a = a ^ b
b = a ^ b
a = a ^ b

print (a, b) // => 20, 10
```

In programming languages like Java, JavaScript, C, or C++, `XOR` uses the `^` (caret) operator.

NB XOR is also associative. Lets look at an example:
$$
0 \oplus 1 \oplus 0
$$
has different values depending on the order you evaluate it in.
$$
\begin{align}
0 \oplus (1 \oplus 0) = 0 \oplus 1 = 1\\
(0 \oplus 1) \oplus 0 = 1 \oplus 0 = 1
\end{align}
$$

