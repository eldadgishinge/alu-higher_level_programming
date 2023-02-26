#!/usr/bin/python3
import sys
if __name__ == "__main__":
    nu = sys.argv[1:]
    nu_nu = len(nu)
    if nu_nu == 0:
        print("0")
        print(type(nu))
    else:
        add = sum(int(i) for i in nu)
        print(add)
