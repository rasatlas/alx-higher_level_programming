#!/usr/bin/python3
str = ", "
for num in range(0, 100):
    if num < 10:
        print("{}{}".format(0, num), end=str)
    else:
        if num == 99:
            str = "\n"
        print(num, end=str)
