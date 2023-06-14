#!/usr/bin/python3

# a function that deletes keys with a specific value in a dictionary.

def complex_delete(a_dictionary, value):
    for key in list(a_dictionary):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
