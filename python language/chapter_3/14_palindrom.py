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
'''

'''# palindrome pyramid
n = 5
for i in range(1, n+1):
    left_half = " ".join(str(j) for j in range(1, i+1))
    right_half = " ".join(str(j) for j in range(i-1, 0, -1))
    row = left_half + " " + right_half if right_half else left_half
    print(" " * (n - i) + row)
    
