#Single Inheritance
class Employee: #baesd/ Parent class
    company = "Google"
    def showDetails(self):
        print("This is an employee")
    
class Programmer(Employee): # derived class
    language = "python"
    company = "Youtube"

    def getlanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self): # overriding
        print("This is an employee")

e = Employee()
e.showDetails()
p= Programmer()
p.showDetails()
print(p.company)
print(e.company)