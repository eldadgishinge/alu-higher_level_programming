#!/usr/bin/python3
from calculator_1 import  add,sub,div,mul
import sys
if __name__ == "__main__":
    num = sys.argv
    num_arg = len(num)-1
    op = {"+": add, "-": sub, "*": mul, "/": div}

    if num_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("1")
        if sys.argv[2] not in list(op.keys()):
            print("Unknown operator. Available operators: +, -, * and /")
            print("1")

a = int(sys.argv[1])
b = int(sys.argv[3])
print("{} {} {} = {}".format(a, sys.argv[2], b, op[sys.argv[2]](a, b)))



