Another type of cipher is a substitution cipher; here, we exchange letters for each other. Here is a simple implementation in python:


```py
# substitution.py

def substitute(letter:char, key:int):
	code = ord (letter) - 65
	code = code + key % 26
	return chr (code + 65)
	
def encrypt (text: str, k: Int ):
	return [substitute(l, k) for l in text]

def decrypt (text:str, k: int):
	return [substitute(l, -k) for l in text]
```

In general, the cipher takes the form:
$$
c = p + k \mod n
$$
where $p$ is the letter code from the plain text, $k$ is the key, $n$ is the alphabet size, and $c$ is the letter code in the ciphertext. Decryption is as simple as the inverse:
$$
p = c - k \mod n
$$
this is a shift-based substitution cipher; letters are shifted along the alphabet. This kidn of cipher is also called a caesar cipher.

Multiplicative ciphers also exist; they have the form:
$$
\begin{align}
c = p \times k&  \mod n\\
p = c \times k'&  \mod n\\
\text{where}&\\
kk' = 1& \mod n
\end{align}
$$
Though here, we need to make sure that $n$ is a prime number, so that any value of $k$ can be used (i.e. $k'$ is well defined).

We can also combine shift and multiplicative ciphers together:
$$
\begin{align}
c = p \times k1 + k2 \mod n\\
p = c \times k1' - k2 \mod n
\end{align}
$$


# Analysis
These ciphers are also not very good. The diffusion for this cipher is poor - changing a single letter in the plaintext only changes a single letter in the ciphertext - although the confusion is good.



This cipher is also vulnerable to statistical letter-frequency attacks, because each letter is always transformed into the same value. So in English, we could look for the most common letter in the ciphertext and guess that it means e; we have a good chance of being right, and its quick to a) check and b) try another guess if we were wrong.
