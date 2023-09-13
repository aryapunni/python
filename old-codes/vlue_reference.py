#!/usr/bin/env python3
def check_id(a, b):
    if id(a) == id(b):
        print(f"{a} and {b} point to same objects")
    else:
        print(f"{a} and {b} does not point to same objects")

def integer_obj():
    a = 2
    b = a
    print(id(a), id(b))
    check_id(a , b)

    x = 10
    y = 10
    print(id(x), id(y))
    check_id(x , y)


def list_obj():
    a = [1, 2, 3]
    b = a
    print(id(a), id(b))
    check_id(a, b)

    x = [7, 8, 9]
    y = [7, 8, 9]
    check_id(x, y)
if __name__ == '__main__':
    integer_obj()
    list_obj()
