#!/usr/bin/python3

# Write a function that removes all characters c and C from a string.

def no_c(my_string):
    new_str = my_string.replace("c", "").replace("C", "")
    return new_str
