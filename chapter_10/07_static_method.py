class Employee:
    company = "Google"
    def getSalary(self,signature):
        print(f"salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good morning,Sir")
    
    @staticmethod
    def time():
        print("The time is 9AM in the morning")
        
dhruv = Employee()
dhruv.salary = 100000
dhruv.greet() # Employee.greet()
dhruv.getSalary("Thanks!") # Employee.getSalary(dhruv)
