The message digest is a smaller *fingerprint* of a message that can still uniquely identify the message.

A message digest can be signed with a secret key - the Message Authentication Code (MAC). This is often known as the hash or the checksum.

It will be just as valid as a signed version of the original document,
provided that a different document with the same digest cannot be created.

Also related is the idea of a digital signature.

# Requirements of the message digest
1. given a message, it should be easy to compute the digest
2. given a digest, it should be difficult to compute the message
3. given a message $M$, it is hard to find another message $M'$ with the same digest
	1. also called a pre-image collision attack
4. it should be hard to find to random messages $M$ and $M'$ with the same message digest
	1. also called a collision attack or birthday attack.

3 & 4 can be summarised as a message digest should be Effectively unique

3 is vital because it prevents one document whose MD has been signed from being replaced by another document with the same MD - we cannot substitute out messages

4 is vital because and relies on the following statistical facts:

>[!info] Birthday statistics
> How many peopled must be in a room before there is a chance better than even (i.e. >= 50%) that one of them shares a birthday with me?
> 
> answer: 182
> 
> ---
> How many people must be in a room before there is a greater than even chance that two of them share a birthday?
>
> answer: 23

It is much easier to find two random people with the same birthday than it is to find someone with the same birthday as a specified person.


hash functions

Hash functions create message digests;

hash functions have to reduce the size of a document, and usually work by first breaking the document into blocks, each the same length as the hash value.


a function is defined that takes two blocks as input and one as output; we can then call it iteratively, shrinking the message a block at a time to produce a single resulting hash block.