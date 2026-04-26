print("P1 % USed","\n")
n=9
space=0
for i in range(n,0,-1):
    if i%2!=0:
        print(" "*space + "*"*(i))
        space+=1
# check if n is odd or even
print("P2","\n")
i=5
if i% 2!=0:
    print("odd")
else:
    print("even")
    
# Basic method
print("P3","\n")
n=5 # ye 9 star tak print karega
for i in range(1,n+1,-1):
    print(" "*(n-i)+ "*"*(2*i-1))

# Direct formula
print("P4 Direct Formula","\n")
n=5
for i in range(n,0,-1):
    print(" "*(n-i)+ "*"*(2*i-1))

# Using while loop
print("P5 Using While Loop","\n")
n=9
space =0 
while n>0:
    print(" "*space + "*"*n)
    n-=2
    space+=1

# Using List + Join
print("P6 Using List + Join","\n")
n = 5
for i in range(n, 0, -1):
    spaces = [" "] * (n - i)
    stars = ["*"] * (2*i - 1)
    print("".join(spaces + stars))

# Using String Center Method
print("P6 Using String","\n")
n = 5
for i in range(n, 0, -1):
    stars = "*" * (2*i - 1)
    print(stars.center(2*n - 1))