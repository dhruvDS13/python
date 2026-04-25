class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    # def showNumber(self):
    #     print(self.real,"i +", self.img,"j")
    
    # def __add__(self, num2):
    #     newReal = self.real + num2.img
    #     newImg = self.real + num2.img
    #     return Complex(newReal,newImg)
    
    # def __sub__(self, num2):
    #     newReal = self.real - num2.img
    #     newImg = self.real - num2.img
    #     return Complex(newReal,newImg)
    
    # def __mul__(self, num2):
    #     newReal = self.real * num2.img
    #     newImg = self.real * num2.img
    #     return Complex(newReal,newImg)

    def __add__(self,c):
        return Complex(self.real + c.real, self.img + c.img)
    
    def __mul__(self,c): #(a+bi)(c+di) = (ac-bd) + (ad +bc)i
        mulReal = self.real*c.real - self.img*c.img
        mulImg = self.real*c.img + self.img*c.real
        return Complex(mulReal , mulImg)
    
    def __str__(self,):
        if self.img<0:
           return f"{self.real} - {-self.img}i" 
        else:
            return f"{self.real} + {self.img}i"

num1 = Complex(1, -4)
# num1.showNumber()

num2 = Complex(331, -37)
# num2.showNumber()

num3 = num1 + num2
print(num3)
num3 = num1 * num2
#num3.showNumber()
print(num3)