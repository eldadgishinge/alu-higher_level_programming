#!/usr/bin/python3
# calculator
import calculator_1

a = 10
b = 5

ZE = calculator_1.add(a, b)
PE = calculator_1.sub(a, b)
GE = calculator_1.mul(a, b)
FE = calculator_1.div(a, b)

print("{} + {} = {}".format(a, b, ZE))
print("{} - {} = {}".format(a, b, PE))
print("{} * {} = {}".format(a, b, GE))
print("{} / {} = {}".format(a, b, FE))
