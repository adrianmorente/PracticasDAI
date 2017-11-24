#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

# thinking the number...
print ("I'm thinking a number between 1 and 100...")
thought_number = randint(1, 100)
print ("Got it!")
print ("..................")

# 10 attempts to go
input_number = 0
count = 0
while (input_number != thought_number) and (count != 10) :
    print ("\n--- YOU ONLY HAVE " + str(10-count) + " ATTEMPTS ----")
    count += 1

    # let's check that the user writes a number and not a string
    try:
        input_number = int(input("Write a number (1-100) --> "))
        # let's check the inserted value
        if input_number > thought_number :
            print ("My number is lesser than yours...")
        elif input_number < thought_number :
            print ("My number is greater than yours...")
        elif input_number < 1 or input_number > 100 :
            print ("I said a number between 1 and 100!!")
    except ValueError:
        print("Hey, that's not a number!")


# end of the game
if (count >= 10):
    print ("\nYou already failed 10 times...\n")
else:
    print ("\nYup! It was the " + str(thought_number) + ".\n")
