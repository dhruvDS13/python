class Employee:
    company = "Google"
    salary = "300"

dhruv = Employee()
ranjeet = Employee()
ranjeet.salary = "450"
print(dhruv.salary)
print(ranjeet.salary)
# Below line Throws an error as address is not present in isinstance/class
# print(ranjeet.address)