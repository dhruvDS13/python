class Account:
    def __init__(self, bal , acc):
        self.balance = bal
        self.account = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance()) 

    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount, "was credit")
        print("total balance = ", self.get_balance())   

    def get_balance(self):
        return self.balance

acc1= Account(10000,12345)    
print(acc1.balance)
print(acc1.account)

acc1.debit(1000)
acc1.credit(500)
acc1.credit(50000)