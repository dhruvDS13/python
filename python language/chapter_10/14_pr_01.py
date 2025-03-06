class Programmer:
    company = "Microsoft"
    
    def __init__(self,name,product):
        self.name = name
        self.product = product
        print(f"The name of the {self.company} programmer is {self.name} Develop product {self.product}.")

s1 = Programmer("Dhruv","Github")
s2 = Programmer("Shubham","skype")
s2 = Programmer("Ravi", "office package" )