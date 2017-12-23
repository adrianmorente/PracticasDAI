#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# we'll read a number `n` from a file, and we'll write
#the n-th number of the Fibonnaci sequence in another one.
def write_number_to_file(number, file):
    dest_file = open(file, 'w')
    dest_file.write(str(number))
    dest_file.close()

# Fibonnaci sequence. It prints the whole sequence until max,
#and it writes the n-th number in the specified file
def get_n_number_fibonacci(max, dest_file):
    fibonacci = []
    x=0
    y=1
    for i in range(max):
        fibonacci.append(x+y)
        aux = x+y
        x   = y
        y   = aux
    print(fibonacci)
    write_number_to_file(fibonacci[max-1], dest_file)

# path to the starter file
path = './ejercicio4-start.txt'

# opening the starter file:
#   · 'w' --> for writing
#   · 'r' --> used for reading
#   · 'r+' -> for reading and writing to the same file
#   · 'a' --> for appending to an existing file
#   · 'x' --> for writing to a new created file
number_file = open(path, 'r')

# the file only contains a number, so we read it like this
number = int(number_file.readline())
number_file.close()

# we call the fibonacci function and print the result
dest_path = './ejercicio4-end.txt'
get_n_number_fibonacci(number, dest_path)
