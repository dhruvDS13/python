class Employee:
    companye = "Google"
    salary = 100
    location = "Delhi"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal # change the attr of class [self.___class__.attr] =[Employee.attr]
        #__class__ is called dander class
    
    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(450)
print(e.salary)
print(Employee.salary)