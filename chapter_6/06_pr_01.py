# Write a python program to find greatest of four numbers extered by the user

num1 = int(input("Enter the value 1: "))
num2 = int(input("Enter the value 2: "))
num3 = int(input("Enter the value 3: "))
num4 = int(input("Enter the value 4: "))

if (num1>num4):
    f1= num1
else:
    f1=num4
if (num2>num3):
    f2= num2
else:
    f2= num3

if f1>f2:
    print(str(f1), "is greatest")
else:
    print(str(f2), "is greatest")