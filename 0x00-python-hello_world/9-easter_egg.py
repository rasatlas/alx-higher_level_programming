#!/usr/bin/python3
import os

filename = 'zenofpython.txt'

if os.path.isfile(filename):
    with open(filename, 'r') as f:
        print(f.read())
else:
    print(filename + ' does not exist.')
