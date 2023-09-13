#!/usr/bin/env python3
def add_border(message, border="_"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

if __name__ == "__main__":

    add_border("hello there", "*")
