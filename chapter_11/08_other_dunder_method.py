class Number:
    def __init__(self,num):
        self.number = num

    def __add__(self,num2):
        print("Lets add")
        return self.number + num2.number
    
    def __mul__(self,num2):
        print("Lets Multiply")
        return self.number * num2.number

    def __str__(self):
        return f"Decimal Number: {self.number}"
    
    def __len__(self):
        return 1
    
n = Number(9)
print(n)
print(len(n))