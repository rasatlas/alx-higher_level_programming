#!/usr/bin/python3
def remove_char_at(str, n):
    tmpstr = ""
    cont = 0
    for ch in str:
        if cont == n:
            pass
        else:
            tmpstr += ch
        cont += 1
    return tmpstr
