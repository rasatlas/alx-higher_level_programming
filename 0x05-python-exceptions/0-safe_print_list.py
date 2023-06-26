#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    i = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            i += 1
        except IndexError:
            break
    print("")
    return(i)
