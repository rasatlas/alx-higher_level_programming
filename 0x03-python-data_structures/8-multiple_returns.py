#!/usr/bin/python3

# Write a function that returns a tuple with the length of a string
# and its first character.

def multiple_returns(sentence):
    new_tuple = ()
    if len(sentence) == 0:
        new_tuple = 0, "None"
    else:
        new_tuple = len(sentence), sentence[0]
        return new_tuple
