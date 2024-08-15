Information theory helps us examine situations where there are many possible messages;

The entropy of a set of messages is the number of bits required to encode every unique message with an optimal encoding.

If $X = \{x_i\}$ is the set of all possible messages, with message $x_i$ appearing with probability $p(x_i)$, then the entropy is defined as:
$$
H(X) = \sum_{x_i\in X} p(x_i) \log\left(\frac{1}{p(x_i)}\right)
$$
consider e.g. the gender field in a database; there are two values (`male` and `female`) that both appear with equal probability; therefore we get:

$$
H(\text{gender}) = 0.5 * \log(2) + 0.5 * \log(2) = 1
$$
So we need one bit to store this data; not a surprise!

When there is an imbalance (for example more `male` entries than `female`) then the entropy of the system decreases - we need fewer bits to encode the same information.

In practise, this means we could group users into larger sets (say of size $n$) and describe that set with fewer than $n$ bits.

When all values are equally likely, we can simplify the formula above to:

$$
H(X) = \log(|X|)
$$
## Redundancy
All ways of encoding data have structure which makes them different from purely random data. 

For example, English is highly structured with lots of redundancy. Compressing a file of English text reduces the redundancy, but there is still some structure in the compression encoding table.

Information theory provides quantitative estimates of the amount of redundancy.

Code breaking attacks that exploit this redundancy are called statistical attacks.



## Absolute Rate ($R$)
The absolute rate of an alphabet ($R$) is the maximum number of bits that can be encoded in a single character assuming all characters are equally likely; 
$$
R = \log (L)
$$
where $L$ is the number of letters in the alphabet; for english:
$$
R = \log(26) \approx 4.7
$$
## Actual Rate ($r$)
The actual rate of a language ($r$) is defines as the average number of bits of information are encoded per character. Essentially, it is the per-character entropy.

We compute this by looking at the pre-character rate of each character in strings of some length $n$. In terms of entropy:

$$
r_{n} = \frac{H(S_{n})}{n}
$$
where $S_{n}$ are all meaningful strings of length $n$.

As $n$ increases, $r_n$ decreases because there are fewer possible choices, and some are more likely than others.

In English, for large $n$, $r_{n}$ is between 1 and 1.5. We will assume $r=1.5$


The redundancy of a language ($D$) is defined
$$
D = R- r
$$
In English, $D$ is about 3.2 - which corresponds to about 68% redundancy.

> u cn rmv abt 68 pct of ltrs nd stl b ndrstd.


## Unicity Distance

The unicity distance tells us how much ciphertext we must decode to be confident that we have decoded it successfully. 

If we have an alphabet of $L$ symbols, recall that $L = 2^R$; therefore the number of possible messages of length $n$ is $L^n = 2^{Rn}$.

The number of apparently meaningful messages is $2rn$;
therefore the probability of getting a meaningful message by chance is:

$$
\frac{2^{rn}}{2^{Rn}}=2^{(r-R)n} = 2^{-Dn}
$$
### Key space

let $k$ be the set of all possible keys.
the number keys we need to consider is $2^{H(k)}$ since there may be some redundancy in the keys (i.e. some may produce the same result).

The expected number of wrong keys is:
$$
o = 2^{H(k)} -1 \approx 2^{H(k)}
$$
The approximation works for large sized $k$, if we assume that only one of our keys is correct.


The expected number of false solutions that look almost correct:
$$
\begin{align}
& \text{\# wrong keys} \cdot \text{chance of meaningful message}\\
=&  2^{H(k)} \cdot 2^{-Dn}\\
=& 2^{H(k)  - Dn}
\end{align}
$$
This is a rapidly decreasing function of $n$; we can define the unicity distance as when this whole expression $=1$, or when the exponent $=0$:

$$
\begin{align}
0 &= H(k) - DN_{u} \\
DN_{U} &= H(k) \\
N_{u} &= H(k) / D
\end{align}
$$
if $n > N_{u}$, then the chance of getting a false positive is negligible, since the number of correct-looking false messages is less than 1.

on the other hand, if $N_{u} > n$, then there may be many false-positives.


Note that the unicity distance in and of itself does not provide a way to break encryption; It just indicates how much information we must gather before we can attempt to break it.

it is based on the rate of the language, a statistical concept, which is less valid for shorter sections of text.

## Example: DES

DES uses 56-bit keys. If the keys are chosen at random then $H(k) = 56$.

If we assume that an English document is used and we use one byte per letter:
$$
\begin{align}
R &= 8 & &  \text{since it requires 8 bits for 1 letter} \\
r &= 1.5 \\
D &= 6.5 \\
N_{u} &= \frac{H(k)}{D}  \\
&= \frac{56}{6.5} = 8.6
\end{align}
$$
So we need about 9 characters to be confident that we have decrypted the message correctly.


Note: Reducing redundancy increases the unicity distance - and therefore makes the code harder to break.

If the data is nearly random, then D is very small and the unicity distance much higher. Thus, compressing the message before encrypting it increases the unicity distance.


## Random encryption
This all assumes a random encryption system where:
- there is no relation between keys and ciphertext
- there is no relation between plaintext and ciphertext
when these assumptions are broken, the unicity distance is smaller.


This random concept is usually expressed in terms of Confusion and diffusion

An encryption system has good confusion if changing one bit in the key changes roughly half the bits in the ciphertext;

an encryption system has good diffusion if changing one bit in the plaintext changes roughly half the bits in the ciphertext.
