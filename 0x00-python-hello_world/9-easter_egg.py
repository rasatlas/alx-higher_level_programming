#!/usr/bin/python3
import os
fn = 'zen.txt'
with open(fn, 'r') as f:
    print(f.read().rstrip())
