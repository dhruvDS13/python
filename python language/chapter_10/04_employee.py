class Employee:
    company = "Google"
    salary = "300"

dhruv = Employee()
ranjeet = Employee()

dhruv.salary = "450"
ranjeet.salary = "600"

print(dhruv.company)
print(ranjeet.company)

Employee.company = "Youtube" 
print(dhruv.company)
print(ranjeet.company)
print(dhruv.salary)
print(ranjeet.salary)
