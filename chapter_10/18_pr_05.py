# make a check train status, booking, cancellation 
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    
    def getStatus(self):
        print("*************")
        print(f"The name of the Train is {self.name}")
        print(f"The no. of the seats avilable in Train is {self.seats}")
        print("*************")

    def getfareInfo(self):
        print(f"The fare of the Train is Rs.{self.fare}")
    
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat no. is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self):
        if(self.seats<=0):
            print(f"Cancelation Process is done Your seat is reduce to {self.seats}")
            self.seats = self.seats + 1
        else:
            print("Cancellation process is over!")

name = Train("Intertercity Express 14019",400,2)
name.getStatus()
name.getfareInfo()
name.bookTicket()
name.getStatus()
name.bookTicket()
name.getStatus()
name.bookTicket()
name.cancelTicket()
name.getStatus()