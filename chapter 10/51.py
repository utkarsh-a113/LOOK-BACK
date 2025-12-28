import random
class train:
    def __init__(self, name, ticketno, fro, to):
        self.name = name
        self.ticketno = ticketno
        self.fro = fro
        self.to = to
    def bookTicket(self):
        print(f"Ticket booked for {self.name}, Ticket No: {self.ticketno}")
    def traininfo(self):
        print(f"{self.name} with {self.ticketno} is running {self.fro} to {self.to}")
    def fareinfo(self):
         print(f"{self.ticketno} costs {random.randint(1,100)}")
p = train("shatabdi", 1234, "dgp", "hwh")
p.bookTicket()
p.traininfo()
p.fareinfo()