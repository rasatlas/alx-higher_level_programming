#!/usr/bin/python3

# A function that computes the square value of all integers of a matrix.

def square_matrix_simple(matrix=[]):
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix
