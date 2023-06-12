#!/usr/bin/python3

# Write a function that replaces an element in a list at a specific
# position without modifying the original list

def new_in_list(my_list, idx, element):
    if my_list:
        if idx < 0 or idx >= len(my_list):
            return my_list.copy()
        else:
            new_list = my_list.copy()
            new_list[idx] = element
            return new_list
