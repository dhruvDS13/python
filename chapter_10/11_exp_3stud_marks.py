# Incapsulation
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum =0
        for val in self.marks :
            sum += val
        print("Hi", self.name, "your avg score is:" ,sum/3)

s1=Student("tony stark",[78,56,88])
s1.get_avg()

s1.name= "iron man"
s1.get_avg()