#!/usr/bin/python3

# Write a function that finds the biggest integer of a list.

def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max_val = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > max_val:
                max_val = my_list[i]
        return max_val
