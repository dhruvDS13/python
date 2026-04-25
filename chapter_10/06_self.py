class Employee:
    company = "Google"
    def getSalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")

# remove "self" 
# TypeError: Employee.getSalary() takes 0 positional arguments but 1 was given

dhruv = Employee()
dhruv.salary = 100000
dhruv.getSalary() # Employee.getSalary(dhruv)

# u can use self as instance attribute and class attribute