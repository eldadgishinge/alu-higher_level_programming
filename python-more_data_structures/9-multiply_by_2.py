#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiply_by_2 = a_dictionary.copy()
    for values in multiply_by_2:
        multiply_by_2[values] = multiply_by_2[values] * 2
    return multiply_by_2
