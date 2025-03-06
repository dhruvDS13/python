#  Make a calculator to find square, sqRoot, cubicRoot of a number
class Calculator:
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"The square of number {self.number} is {self.number **2}")

    def squareRoot(self):
        print(f"The squareRoot of number {self.number} is {self.number **0.5}")

    def cubicRoot(self):
        print(f"The cube of number {self.number} is {self.number **3}")

a = Calculator(int(input("Enter the value: ")))
a.square()
a.squareRoot()
a.cubicRoot()
# class Calculator:
#      def __init__(self,num):
#         self.number = num
#         print(f"The value of number is {self.number}.\nwhose square is {self.number **2}, squareRoot is {self.number **0.5} and cube is {self.number **3}")

# a = Calculator(int(input("Enter the value: ")))