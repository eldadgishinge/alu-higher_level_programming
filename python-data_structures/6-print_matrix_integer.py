#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for h in matrix:
        print(" ".join("{:d}".format(z) for z in h))
