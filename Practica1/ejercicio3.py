#!/usr/bin/python
# -*- coding: utf-8 -*-

# we'll have an empty set in which we'll be adding all the numbers
#being multiple of another one. If the number we're iterating on (i)
#is not in the current set, we display it as a prime number.
def criba_eratostenes(max):
    multiples = set()
    for i in range(2, max+1):
        if i not in multiples:
            print (i, end=", ")
            multiples.update(range(i*i, max+1, i))
    print("\n")

criba_eratostenes(1000)
