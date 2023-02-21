#!/usr/bin/python3
# calculator
from  calculator_1 import add, sub, mul, div
"__main__"
"__name__"
a = 10
b = 5

ZE = add(a, b)
PE = sub(a, b)
GE = mul(a, b)
FE = div(a, b)

print("{} + {} = {}".format(a, b, ZE))
print("{} - {} = {}".format(a, b, PE))
print("{} * {} = {}".format(a, b, GE))
print("{} / {} = {}".format(a, b, FE))
