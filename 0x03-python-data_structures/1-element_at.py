#!/usr/bin/python3
# Write a function that retrieves an element from a list like in C.
def element_at(my_list, idx):
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]
