# Find a Prime no.
num = int(input("Enter a number: "))
prime = True
for i in range(2,num):
    if(num%i == 0):
        prime = True
        break
if prime:
    print("This number is prime ")

else:
    print("This number is not prime ")
