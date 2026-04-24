
'''#6.Even numbers pyramid upto 10
print("\n")
#method 1
n=5
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+2))
    
print("\n")
#method 2
n=5
for i in range(1, n+1):
    print(" "*(n-i)+"*"*(2*i))


#7. Odd numbers pyramid upto 10
print("method 1","\n") 
#method 1
n=5
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))
    
print("Method 2","\n")
#method 2
n=5
for i in range(1, n+1):
    print(" "*(n-i)+"*"*(2*i-1))
'''
'''
# palindrome pyramid
n = 5
for i in range(1, n+1): 
    left_half = " ".join(str(j) for j in range(1, i+1))
    right_half = " ".join(str(j) for j in range(i-1, 0, -1))
    row = left_half + " " + right_half if right_half else left_half
    print(" " * (n - i) + row)
 
#8. even Number print in pyramid less number of printed in each row
n = 5
for i in range(1, n+1):
    row = " ".join(str(2*j) for j in range(1, i+1))
    print(" " * (n - i) + row)

#9. Odd Number print in pyramid less number of printed in each row
n = 5
for i in range(1, n+1):
    row = " ".join(str(2*j - 1) for j in range(1, i+1))
    print(" " * (n - i) + row)

#10. Odd Number print in pyramid more number of printed in each row
n = 5
for i in range(1, n+1): 
    row = " ".join(str(2*j - 1) for j in range(1, 2*i))
    print(" " * (n - i) + row)
    
# palindrome pyramid
n = 5
for i in range(1, n+1):
    left_half = " ".join(str(j) for j in range(1, i+1))
    right_half = " ".join(str(j) for j in range(i-1, 0, -1))
    row = left_half + " " + right_half if right_half else left_half
    print(" " * (n - i) + row)
    
'''
num = int(input("Enter number: "))

if num < 0:
    print("Not Palindrome")
else:
    temp = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    if temp == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")