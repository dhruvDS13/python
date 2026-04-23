#1. Simple Star Pattern
for i in range(1, 6): #LEFT SIDE PYRAMID
    print("*" * i)
#2 Simple reverse peramid
for i in range(5, 0, -1):
    print("*"*i)

#3.  Pyramid
for i in range(1,6):
    print(" "*(5-i), end="")
    print("* "*i)

