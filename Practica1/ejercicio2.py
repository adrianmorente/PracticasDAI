#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
from time import time

loops = 10
list_of_numbers = range(loops)

# random initialization of the numbers
def generate_matrix():
    count = 0
    while count < loops :
        list_of_numbers[count] = randint(1, 100)
        count += 1

# bubble sort implementation
def bubble_sort(n_list):
    for i in range(len(n_list)-1, 0, -1):
        for j in range(i):
            if n_list[j] > n_list[j+1] :
                aux = n_list[j]
                n_list[j] = n_list[j+1]
                n_list[j+1] = aux

# selection sort implementation
def selection_sort(n_list):
    for i in range(1, len(n_list)-1):
        minimum = i
        for j in range(i+1, len(n_list)):
            if(n_list[j] < n_list[minimum]):
                minimum = j;
        aux = n_list[i]
        n_list[i] = n_list[minimum]
        n_list[minimum] = aux

# -------------------------------------------------------------- #

generate_matrix()
print ("Generated list: ")
print (list_of_numbers)
start = time()
bubble_sort(list_of_numbers)
end = time()
print ("\nSorted list (by bubble): ")
print (list_of_numbers)
print ("Invested time: " + str(end - start) + "s.")

generate_matrix()
print ("\n\nGenerated list: ")
print (list_of_numbers)
start = time()
selection_sort(list_of_numbers)
end = time()
print ("\nSorted list (by selection): ")
print (list_of_numbers)
print ("Invested time: " + str(end - start) + "s.")
