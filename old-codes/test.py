print("hello world!")
a = 2
while a != 0:
    b = input("input b: ")
    while True:
        c = input("input something greater than a and b")
        if int(c) > a and int(c)  > int(b):
            break
    print(a)
    a -= 1
