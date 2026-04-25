class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"
    
    def getSalary(self):
        print(f"Salary is {self.salary}")

    # def takeBreath(self):
    #     print("I am an Employee so I am Luckey breathing...")  

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmer")
    
    def takeBreath(self):
        print("I am a Programmer so I am breathing++...")

p = Person()
p.takeBreath()
# p.company() #throw an Error

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.country)