arr = [10, 20, 30, 40, 50]

for i in range(len(arr)):
    print(arr[i]) 

for i in range(len(arr)):
    print(arr[i], end=" ") # end is used to print in same line with space
    
for i in range(len(arr)-1, -1, -1):
    print(arr[i]) 