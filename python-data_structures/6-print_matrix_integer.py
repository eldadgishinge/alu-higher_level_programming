#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    b = ""
    if matrix is None:
        return "$"
    for i in range(3):
        for j in range(3):
            b += chr(matrix[i][j] + 48) + '\t'
        print(b)
        b = ""

