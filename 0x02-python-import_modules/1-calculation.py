#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
a = 10
b = 5
print(f""+"{} + {} = {}".format(a, b, add(a, b)))
print(f""+"{} + {} = {}".format(a, b, sub(a, b)))
print(f""+"{} + {} = {}".format(a, b, mul(a, b)))
print(f""+"{} + {} = {}".format(a, b, div(a, b)))
