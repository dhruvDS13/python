
#6.Even numbers pyramid upto 10
print("\n")
#method 1
n=5
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+2))
 
#method 2
n=5
for i in range(1, n+1):
    print(" "*(n-i)+"*"*(2*i))
