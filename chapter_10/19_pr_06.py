# can change the self parameter and it works or not?
class Sample:
    def __init__(Dhruv,name):
        Dhruv.name = name

Obj = Sample("Dhruv")
print(Obj.name)
