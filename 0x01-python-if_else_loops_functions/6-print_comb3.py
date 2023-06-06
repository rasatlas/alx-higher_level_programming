#!/usr/bin/python3
str = ", "
for num in range(0, 100):
    digit2 = num % 10
    digit1 = num / 10
    if num < 10:
        print("{}{}".format(0, num), end=str)
    elif digit1 < digit2:
        if num == 89:
            str = "\n"
        print(num, end=str)
