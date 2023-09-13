#!/usr/bin/python3

import math
import cmath

def quadratic(a, b, c):
    print(f"a = {a}, b={b}, c={c}")
    if a == 0:
        raise ValueError("a cannot be 0")
    det = b**2 - 4 * a * c
    is_real = True
    if det > 0:
        sol1 = (-b + math.sqrt(det))/(2*a)
        sol2 = (-b - math.sqrt(det))/(2*a)
        return sol1, sol2
    elif det == 0:
        return -b / (2*a)
    else:
        sol1 = (-b + cmath.sqrt(det))/(2*a)
        sol2 = (-b - cmath.sqrt(det))/(2*a)
        return sol1, sol2

if __name__ == '__main__':
    import sys
    print(quadratic(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])))
