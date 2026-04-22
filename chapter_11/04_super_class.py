class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person...\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init___()
        print("Initializing Employee...\n")    
    
    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am Luckey breathing...")  

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        # super().__init___()
        print("Initializing Programmer...\n")   

    def getSalary(self):
        print(f"No salary to programmer")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am a Programmer so I am breathing++...")

# p = Person()
# p.takeBreath()


e = Employee()
# e.takeBreath()


# pr = Programmer()
# pr.takeBreath()
