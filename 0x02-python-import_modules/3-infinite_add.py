#!/usr/bin/python3
if __name__ == "__main__":
    import sys

sum = 0
if len(sys.argv) != 1:
    for i in range(len(sys.argv)):
        if i != 0:
            sum += (int(sys.argv[i]))
print(sum)
