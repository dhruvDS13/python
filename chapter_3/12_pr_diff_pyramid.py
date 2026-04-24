#dimond
n=3
#upper Part
for i in range(n):
    print(" "*(n-i-1)+ "*"*(2*i+1))
#Lower Part
for i in range(n-2,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))