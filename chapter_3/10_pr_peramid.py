for i in range(1, 6): #LEFT SIDE PYRAMID
    print("*" * i)

print("PIRAMID STAR")
for i in range(1,6):
    print(" "*(5-i), end="")
    print("* "*i)

print("INVERTED PIRAMID STAR")    
for i in range(5, 0, -1):
    print("*" * i) # PYRAMID