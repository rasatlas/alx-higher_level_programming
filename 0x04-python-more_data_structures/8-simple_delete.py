#!/usr/bin/python3

# a function that returns a new dictionary with all values multiplied by 2

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
