---
Title: Sorting Algorithms
Description: Sorting algorithms
---

Insertion sort is one of the simplest sorting algorithms that exist;

The key idea behind insertion sort is that

```
fn <comparable T> insertSorted(list: [T], item: T) -> [T] {
    if list.lenth == 0 return [item]

    const idx = list.length;
    while (list[idx] > item){
        list[idx+1] = list[idx]
        // move the item up

        // if we reach the end of the list, quit
        if idx == 0 break;

        // otherwise look at the next position in the array
        idx -= 1;
    }

    list[idx] = item

    return list
}
```

```
fn <comparable T> insertionSort(list: [T]) -> [T] {
    newList = []

    for item in list {
        newList = insertSorted(newList, item)
    }

    return newList
}
```

## Analysis

In the worst case, the list we receive is backwards.
So the complexity of insertion sort is $O(n^2)$ - we can do better!

Generics:

generics are a very important idea; they aren't that complicated, but still seem to confuse people. so lets go over them now.

Often I want to write a function that operates on more than one kind of thing; for example, I want append to the end of a list. The logic here will be the same for every kind of list - make sure you have enough space, and then set the end index to the new object. We can easily write this:

```
fn append(list:[Int], x: Int) -> [Int] {
    if (list.length == list.capacity)
        Error ("List Full")

    list[list.length] = x
    return list
}
```

But this version only works for integers - even though it would be the same for strings, floats, and every other type of thing you could imagine. It would be really annoying if we had to write the same function several times for every different type of thing.

So we don't - instead, we write a generic function that works on all lists. In a generic function, we say that it operates on a list with some type T, like so;

```
fn <T> append(list:[T], x: T) -> [T] {
    //... (the same logic as before)
}
```

Here, T is a _type variable_ - it represents a type we don't know yet - and one which we don't care about. This allows us to reason about lists _in general_, without worrying about what their content is.

Sometimes, however, we do care about the type - at least a little bit. Consider the case

To solve this problem, we can use generics with constraints. For example, lets imagine we want a function that checks if a list is sorted; Obviously, we need the items in the list to have some sense of ordering - we need to be able to say one is greater than the other. So, we add a constraint to our type variable T; We say that T must be `comparable`, like so:

```
fn <comparable T> isSorted(list:[T]) -> boolean {
    idx = 1
    while (idx < list.length) {
        if (list[idx] < list[idx-1])
            return false
    }
    return true
}
```

Generics are a way of doing polymorphism - allowing one function to do many different things; this might seem confusing - after all, the whole point of generics is that we use the same code for different types. The key insight is that the compiled code looks different; for example, integers and strings require different `<` implementations.

I'm describing generics in quite a broad manner here - the exact implementation varies language to language.

In Java, they look quite similar. Type constraints work by saying that the variable `extends` some target interface.

In haskell, you can write 'parametric polymorphic' functions - generics with no constraints on the variables - by just using lower case names. Type constraints are implemented with typeclasses.

Loose, dynamically typed languages like python and javascript can also do generics, but they usually don't require any annotation - they work it out, dynamically, as the program runs.

The details here are not imperative - the point is that most languages have some way of doing generics - and they're an extremely useful concept. Hopefully, I've shown that they are also not that scary. :)
