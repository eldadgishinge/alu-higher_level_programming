#!/usr/bin/python3
from calculator_1 import  add,sub,div,mul
from sys import argv
if __name__ == "__main__":
    num = argv
    num_arg = len(num)-1
    op = {"+": add, "-": sub, "*": mul, "/": div}

    if num_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
        if sys.argv[2] not in list(op.keys()):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

a = int(argv[1])
b = int(argv[3])
print("{} {} {} = {}".format(a, argv[2], b, op[argv[2]](a, b)))



