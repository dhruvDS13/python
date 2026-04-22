class Employee:
    Company = "Google"
    salary = 5600
    Salarybonus = 400 # int(input("The add bonou to your salary: "))
    # totalSalary = 6000

    @property #@getters method
    def totalSalary(self):
        return self.salary + self.Salarybonus
    
    @totalSalary.setter
    def totalSalary(self, val):
        self.Salarybonus = val - self.salary 
    

e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.Salarybonus)