# print("Counting Pyramid 1 to 5 * with spacing")
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i) + "* "*(i)) 



'''
print("forword align pyramid")
n = 1
i = 50 #(condition ka adha kerna hai)
while n<=100:
    print("b"*i + "*"*n)
    n+=2 #number of element
    i-=1 #(space)
'''
'''
print("riverse pyramid")
k = 101
l = 1
while k>=1:
    print(" "*l + "*"*k)
    k-=2
    l+=1
'''
print("riverse pyramid")
k = 7
l = 1
while k>=1:
    print(" "*l + "*"*k)
    k-=2
   # l+=0 left align
    l+=1 #center align
   # l+=2 #right align
   

# #1. Left Star Pattern
# print("Left Star Pattern")
# for i in range(1, 6): #LEFT SIDE PYRAMID
#     print("*" * i)

# print("Right Side Pyramid")    
# #2. Right Side Pyramid
# for i in range(1,6):
#     print(" "*(5-i), end="")
#     print("*" * i)

# print("right align")
# # right align
# n=5
# for i in range(1,6):
#     print(" "*(n-i) + "*"*(i)) # if "* " if used then it will make it center align


# #3 left reverse pyramid
# print("left reverse pyramid")
# print("\n")
# for i in range(5, 0, -1):   # -1 is used to decrease the value of i by 1 in each iteration
#     print("*" * i)

# print("Reverse right side pyramid")
# #4. Reverse right side pyramid
# print("\n") 
# for i in range(5,0, -1):
#     print(" "*(5-i), end=" ")
#     print("*" *i)
