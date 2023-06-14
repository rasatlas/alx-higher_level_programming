#!/usr/bin/python3

# a function that returns a list with all values multiplied
# by a number without using any loops.

def multiply_list_map(my_list=[], number=0):
    return (list(map((lambda i: i * number), my_list)))
