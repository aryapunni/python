#!/usr/bin/env python3

a = [] #one way of declaration

b = ["mark", "katarina", "jessica"]

c = []

del b[0]

print(b)

for val in range(10):

    a.append(val)

print(a)

for name in b:
    print(name)
    for letter in name:
        c.append(letter)

print(c)

