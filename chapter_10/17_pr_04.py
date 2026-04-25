#  make a Calculator using staticmethod
class Calculator:
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"The square of number {self.number} is {self.number **2}")

    def squareRoot(self):
        print(f"The squareRoot of number {self.number} is {self.number **0.5}")

    def cubicRoot(self):
        print(f"The cube of number {self.number} is {self.number **3}")

    @staticmethod
    def geet():
        print("*******Hello there Welcome to the best calculator in the World*******")

a = Calculator(int(input("Enter the value: ")))
a.geet()
a.square()
a.squareRoot()
a.cubicRoot()