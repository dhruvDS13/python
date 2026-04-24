'''
#1. Left Star Pattern
for i in range(1, 6): #LEFT SIDE PYRAMID
    print("*" * i)
    
#2. Right Side Pyramid
for i in range(1,6):
    print(" "*(5-i), end="")
    print("*" * i)

#3 left reverse pyramid
print("\n")
for i in range(5, 0, -1):   # -1 is used to decrease the value of i by 1 in each iteration
    print("*" * i)

#4. Reverse right side pyramid
print("\n") 
for i in range(5,0, -1):
    print(" "*(5-i), end=" ")
    print("*" *i)
    '''

#5.  Pyramid
print("\n")

'''
Method 1 Basic
    for i in range(1,6):
        print(" "*(5-i), end="")
        print("*" * (2*i-1))
        
#Method 2 
n=5
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))

n=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
    
'''  
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
    '''  