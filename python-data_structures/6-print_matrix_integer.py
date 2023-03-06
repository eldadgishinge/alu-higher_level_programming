#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    b = ""
    for i in range(3):
        for j in range(3):
            b += str(matrix[i][j]) + '\t'
        print(b)
        b = ""
