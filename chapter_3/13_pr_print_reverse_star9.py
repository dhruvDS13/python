n=9
space=0
for i in range(n,0,-1):
    if i%2!=0:
        print(" "*space + "*"*(i))
        if i==True:
            print(i)
        space+=1

i=5
if i% 2!=0:
    print("odd")
else:
    print("even")
    
n=5
space=0
for i in range(1,n+1):
    print(" "*(n-i)+ "*"*(2*i-1))


