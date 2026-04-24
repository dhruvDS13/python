#1. Simple Star Pattern
for i in range(1, 6): #LEFT SIDE PYRAMID
    print("*" * i)
    
#2. Right Side Pyramid
for i in range(1,6):
    print(" "*(5-i), end="")
    print("*" * i)

#3 Simple reverse pyramid
print("\n")
for i in range(5, 0, -1):   # -1 is used to decrease the value of i by 1 in each iteration
    print("*" * i)

#4. Reverse right side pyramid
print("\n") 
for i in range(5,0, -1):
    print(" "*(5-i), end=" ")
    print("*" *i)