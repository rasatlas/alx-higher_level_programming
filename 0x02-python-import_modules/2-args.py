#!/usr/bin/python3
if __name__ == "__main__":
    import sys

listlen = (len(sys.argv) - 1)

if listlen == 0:
    print("0 arguments.")
elif listlen == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(listlen))
for i in range(listlen):
    print("{} : {}".format(i + 1, sys.argv[i + 1]))
