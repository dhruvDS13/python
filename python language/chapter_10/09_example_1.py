class Student:
    college_name = "ABCD college"

    # default consturctors/call by itself
    def __init__(self):
        pass

    name = "anonymous" # class attribute

    # Parameterized consturctors
    def __init__(self, name, marks):
        self.name = name  #obj attr>>class attr
        self.marks = marks
        print("Add new student in Database..")

s1 = Student("dhruv" ,97)
print(s1.name, s1.marks)
'''# Self-->is a reference to the current instance of the class,
# and is used to access variables theat belongs to the class
'''
s2 = Student("rohit",86)
print(s2.name,s2.marks)

print(Student.college_name)