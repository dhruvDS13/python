#dimond
n=3
#upper Part
for i in range(n):
    print(" "*(n-i-1)+ "*"*(2*i+1))
#Lower Part
for i in range(n-2,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))
    
#Hollow Pyramid (with spaces)
n = 5
for i in range(n):
    for j in range(2 * n - 1):
        if j == n - i - 1 or j == n + i - 1 or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
# Number Pyramid   
n = 4

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()