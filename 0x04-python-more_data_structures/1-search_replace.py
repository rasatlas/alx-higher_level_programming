#!/usr/bin/python3

# a function that replaces all occurrences of an element by another
# in a new list.

def search_replace(my_list, search, replace):
    copy = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            copy.append(replace)
        else:
            copy.append(my_list[i])
    return copy
