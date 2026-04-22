# n! = 1x2x3x4x5......xn
# 5! = 1x2x3x4x5
num = int(input("Enter a number: "))
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i
print(f"The factorial of {num} is {factorial}")