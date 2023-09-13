#!/usr/bin/python3

name = "arya p unni"

print(name.capitalize())

print(name.replace("i", "y"))

print("alphabets" if name.isalpha() == True else "not alphabets")

print("digits" if name.isdigit() == True else "not not digits")

pieces = name.split(" ")

print(pieces)
print(name.split(" ")[0])

new_name = pieces[0]+pieces[1]+pieces[2]

print(new_name)
