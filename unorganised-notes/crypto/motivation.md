
# Why bother with Encryption?

Imagine Alice and Bob want to exchange messages over a public network, without revealing the message to anyone other than the intended recipient.

Cryptography is the solution!

In cryptography, we hide the information we are trying to exchange behind some *encryption* so that only those in the know can read the message.


## A note on representation:
In a computer, all data is represented numerically; this includes text. We can convert a letter to a number with some scheme (i.e. [ASCII](https://en.wikipedia.org/wiki/ASCII), where `A` is `65`)
For a larger text, we can split the text into chunks and treat them as single, very large integers.

