#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length =0
    i = 0
    j = 0
    try:
        for i in my_list:
            length += 1
        if x <= length:
            while j < x:
                print(my_list[j], end="")
                j += 1
            print("\n")
    except IndexError:
        print("Trying to access value out of bound.")
