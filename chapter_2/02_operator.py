a=4
b=5

print(id(a))
print(id(b))
#Arithmetic operators
print("The value of 4+5 is:",a+b)
print("The value of 4-5 is:",a-b)
print("The value of 4*5 is:",a*b)
print("The value of 4/5 is:",a/b)

#Assignment operators
a=45
a+=2
#a-=2
#a*=2
#a/=2
print(a)

#Comparision operators
b=(14>7)
# b=(14<7)
# b=(14>=7)
# b=(14<=7)
# b=(14==7)
#b=(14!=7)
print(b)

#Logical operators
bool1=True
bool2=False

print("The value of bool1 and bool2:",(bool1 and bool2))
print("The value of bool1 or bool2:",(bool1 or bool2))
print("The value of not bool2 is:",(not bool2))