class Employee:
    company = "visa"
    ecode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level +1

class Programmer(Employee,Freelancer): 
    name = "Rohit"

p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company) #visa is first bcz we use Employee class in first in programmer class