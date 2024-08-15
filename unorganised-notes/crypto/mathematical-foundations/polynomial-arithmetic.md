Polynomials are algebraic expressions that consist of variables and coefficients. For example:
$$
x^2 + x -12
$$
Here there are three terms: $x^2$, $x$ and $12$.

We can perform arithmetic on polynomials (E.g. addition, subtraction, multiplication, exponentiation)

Polynomial arithmetic is more convenient when converting to and from a bit string; for example, [[AES]] uses Polynomial Arithmetic.

However, we are interested in a more limited set of polynomials; usually those with coefficients $\mod n$. For AES $\mod 2$ - for more advanced use cases (RSA, DH) $\mod n$. 

Addition and subtraction are very easy when we use coefficients $\mod 2$ - we just use `XOR`.

Multiplication is also straightforward, but results in bigger polynomials. This should be familiar from high-school maths!

Division is a bit harder; but not too bad for polynomials on the integers $\mod 2$.


Some polynomials cannot be written as the product of smaller polynomials; These are called Irreducible Polynomials and they are analogous to prime numbers.

The algorithm for computing Polynomial inverses is the sameas one for $\mathbb{Z}\mod n$:

let $p$ be a polynomial. let $z$ be its inverse. This means:
$$pz\equiv1 \mod IP$$
You can then use polynomial arithmetic to follow the algorithm we defined for integers.

this can get quite complicated, so its often easier to use a multiplication table to compute the products of each pair of polynomial, and look for the desired outcome.

Many algorithms work with 8-bit polynomials, since that can represent a single byte.
## Galois Fields (or Finite fields)
all Finite fields of the same size are isomorphic - they are guaranteed to have the same internal structure.

The integers $\mod p$ where $p$ is prime form a finite field - known as $GF(p)$ (Galois field).

The polynomials $\mod N$ where $N$ is a irreducible polynomial of degree $n+1$ (and therefore the polynomials have degree $n$) form the field $GF(2^n)$.



Homomorphism 
a structure preserving transformation; $f$ is homomorphic if $f(a*b) = f(a) *' f(b)$

Isomorphism
A homomorphism that is also a bijection (1-to-1, onto); every element in A and B is in a unique pairing.

