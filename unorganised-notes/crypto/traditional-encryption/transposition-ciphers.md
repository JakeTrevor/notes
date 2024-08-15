
A transposition cipher works as so:

1. split the plaintext into blocks of a fixed length $d$
2. re-arrange the characters inside the block

We re-arranged the characters in the block based on a 'permutation' generated from the key;
decryption just requires us to use the inverse permutation.

An example permutation: 1302
the inverse of this permutation: 2031

here is a simple implementation of a transposition cipher:

```python
def permute(x:str, key:str) -> str:
	perm = [int(x) for x in key]
	return "".join([x[i] for i in perm])

def encrypt(plaintext: str, key: str) -> str:
	BLOCK_SIZE = len(key)
	
	# pad the plaintext so that it fits nicely into blocks
	xtra = len(plaintext) % BLOCK_SIZE
	plaintext += (-xtra % BLOCK_SIZE)  * " "
	
	blocks = [plaintext[i:i+BLOCK_SIZE] for i in range(0, len(plaintext), BLOCK_SIZE)]
	transposed_blocks = [permute(block, key) for block in blocks]
	return "".join(transposed_blocks)
```


for a block of length $d$, there are $d!$ possible permutations/keys. If all of these are equally likely
if all permutations are equally likely (i.e. all encryption keys are equally likely) then there 

Transposition ciphers are vulnerable to letter frequency attacks.

We start by guessing the block length of the message; We then look for common bi-grams or trigrams within that block. We know for instance that if we see a `a-n-d` triple, then its likely to be the word `and`. We can use this to narrow down the number of possible permutations. We can then try decrypting a longer section of text (longer than the unicity distance) and then just read it. If it looks like English, then its very likely to be the correct decryption.

