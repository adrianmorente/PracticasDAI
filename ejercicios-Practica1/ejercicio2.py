#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
from time import time

loops = 100
list_of_numbers = list(range(loops))

# random initialization of the numbers
def generate_matrix():
    count = 0
    while count < loops :
        list_of_numbers[count] = randint(1, 2000)
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
    for i in range(len(n_list)-1, 0, -1):
        max_index=0
        for index in range(1, i+1):
            if n_list[index] > n_list[max_index]:
                max_index = index
        tmp = n_list[i]
        n_list[i] = n_list[max_index]
        n_list[max_index] = tmp

# -------------------------------------------------------------- #

generate_matrix()
list_of_numbers_2 = list_of_numbers
print ("STARTER LIST:")
print (list_of_numbers)
print ("\n\n- BUBBLE SORT -")
start = time()
bubble_sort(list_of_numbers)
end = time()
print (list_of_numbers)
print ("--> Invested time: " + str(end - start) + "s.")

print ("\n- SELECTION SORT -")
start = time()
selection_sort(list_of_numbers_2)
end = time()
print (list_of_numbers_2)
print ("--> Invested time: " + str(end - start) + "s.")
