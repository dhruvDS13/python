class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass =acc_pass

    def reset_pass(self):
            print(self.__acc_pass)

acc1 = Account("12345" , "abcsde")

print(acc1.acc_no)
# print(acc1.__acc_pass) #####AttributeError: 'Account' object has no attribute '__acc_pass'########
# __acc_pass isme private bana dega kewal class wala hi access karega 

print(acc1.reset_pass())