#!/usr/bin/python3
for alphabet in range(122, 96, -1):
    char = alphabet
    if alphabet % 2 != 0:
        char = char - 32
    print("{:c}".format(char), end="")
