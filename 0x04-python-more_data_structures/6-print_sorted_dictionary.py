#!/usr/bin/python3

# a function that prints a dictionary by ordered keys.

def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary):
        print("{:s}: {}".format(i, a_dictionary[i]))
