#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
numlen = len(str(number))
if number >= 0:
    numlen = len(str(number))
else:
    numlen = ((len(str(number))) - 1)
if numlen == 1:
    if number > 5:
        print(f"Last digit of {number} is {number} and is greater than 5")
    elif number == 0:
        print(f"Last digit of {number} is {number} and is 0")
    else:
        print(f"Last digit of {number} is {number} \
                and is less than 6 and not 0")
else:
    if number > 0:
        last_digit = (number % 10)
    else:
        last_digit = math.fmod(number, 10)
    if last_digit > 5:
        print(f"Last digit of {number} is {last_digit:.0f} \
                and is greater than 5")
    elif last_digit == 0:
        print(f"Last digit of {number} is {last_digit:.0f} and is 0")
    else:
        print(f"Last digit of {number} is {last_digit:.0f} \
                and is less than 6 and not 0")
