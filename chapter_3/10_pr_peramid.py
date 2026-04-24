#1. Simple Star Pattern
for i in range(1, 6): #LEFT SIDE PYRAMID
    print("*" * i)
    
#2 Simple reverse peramid
for i in range(5, 0, -1):   # -1 is used to decrease the value of i by 1 in each iteration
    print("*" * i)

#.  Pyramid
for i in range(1,6):
    print(" "*(5-i), end="")
    print("* "*i)

