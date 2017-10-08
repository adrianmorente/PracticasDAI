#!/usr/bin/python
# -*- coding: utf-8 -*-

tope = 200

list_of_numbers = range(tope)

def criba_eratostenes(tope):
    for i in range(0, tope):
        list_of_numbers[i] = 0
    for i in range(2, tope):
        for j in range(i, tope, i):
            list_of_numbers[j] = 1

criba_eratostenes(tope)
