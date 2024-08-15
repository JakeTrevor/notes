
Let us assume that our text uses an alphabet consisting of the 26 letters of the English alphabet and three other characters (" ", "-", ".") (29 letters in total). We can defined our alphabet like this:

```js

object alphabet {
	letters = ["a" to "z", "-", " ", "."]
	size = letters.length // 29
	
	function toNumber(letter:string){
		return letters.find(letter)
	}
	
	function toLetter(code:int) {
		return letters[code % size]
	}
}

```

Our encryption scheme can simply be to take each letter, turn it into its integer representation, and multiply it by some number between 2 and 28; This number is our secret key.

```js
function encrypt(plainText:string, key:number) {
	cipherText = new string[ plainText.length ]
	
	for letter, idx in plainText {
		cipherText[idx] = alphabet.toLetter(
			key * alphabet.toNumber(letter)
		)
	}
}
```

Question: How do we reverse this encryption?

We need to know the inverse of our secret key for the size of our alphabet. In our case, the alphabet is 29. 29 is prime - so all secret keys will have an inverse!


## Computing the inverse 
First note that it is trivially true that any number times the base is congruent to the base:
$$
xn \equiv n \mod n
$$
Recall the property of $x$ we are looking for:
$$
xa \equiv 1 \mod n
$$
We know $n$ and $a$ - we can therefore use this set of simultaneous equations to find $x$. First, taking the second equation from the first we get:
$$
x(n-a) \equiv (n-1) \mod n
$$

This can be repeated until we get an equation in the form:
$$
x \equiv \ ? \mod n
$$
```js
function computeInverse(key:number, n:number):number {
	oldLeft = k
	oldRight = 1
	newLeft = n-k
	newRight = n-1
	
	while (newLeft != 1) {
		t = newLeft
		newLeft = (oldLeft - newLeft) % n
		oldLeft = t
		
		t = newRight;
		newRight = (oldRight - newRight) % n
		oldRight = t
	}
	return right
}
```
Other (better, faster) solutions for finding $x$ do exist, but they are more complicated.


We can put this together and produce a decryption function like so:
```js
function decrypt(cipherText:string, key:number){
	key = computeInverse(key, alphabet.size)
	plainText = new string[ cipherText.length ]
	
	for letter, idx in cipherText {
		plainText[idx] = alphabet.toLetter(
			(key * alphabet.toNumber(letter))
		)
	}	
}
```
