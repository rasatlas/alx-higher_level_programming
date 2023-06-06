#!/usr/bin/python3
def uppercase(str):
    tmpstr = ""
    for ch in str:
        if ord(ch) > 96 and ord(ch) < 123:
            tmpstr += chr(ord(ch)-32)
        else:
            tmpstr += ch
    print("{}".format(tmpstr))
