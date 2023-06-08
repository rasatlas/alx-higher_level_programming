#!/usr/bin/python3
if __name__ == "__main__":
    import sys
result = sys.argv
listlen = (len(result) - 1)
if listlen == 0:
    print("0 arguments.")
elif listlen == 1:
    print(f"{listlen} argument:")
    print(f"{listlen}: {result[1]}")
else:
    print(f"{listlen} arguments:")
    for i, r in enumerate(result):
        if i != 0:
            print(f"{i} : {result[i]}")
