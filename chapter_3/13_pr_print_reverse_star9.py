n=9
space=0
for i in range(n,0,-1):
    if i%2!=0:
        print(" "*space + "*"*(i))
        space+=1

n=9
space=0
for i in range(1,n+1):
    print(" "*(n-i)+ "*"*(2*i-1))