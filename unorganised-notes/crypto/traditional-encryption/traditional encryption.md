
encryption schemes from before the invention of the electronic computer

all traditional schemes are single-key schemes, with two main variants:

substitution ciphers - swap instances of character $c$ for some new character $c'$
transposition ciphers - re-order the text

these two variants can be combined.

## Types of Attacks:
1. ciphertext only
2. known plaintext - know part of the input to find out the key
3. chosen plaintext - choose some 

## Attack Methods:

Brute force:
	exhaustively search all keys

letter frequency:
	a statistical attack - analyse the letter frequencies in the ciphertext and compare them to real letter frequencies in typical language sample

di-gram and tri-gram frequencies
	look at the frequencies of pairs and triplets of letters

