from random import randint

class train():
    def __init__(self,trainNo):
        self.trainNo=trainNo
        pass
    def book(self,fro,to):
        print(f"ticket is booked in train number: {self.trainNo} from {fro} to {to}")
    def getstatus(self,trainNo, fro,to):
        print(f"Train No.: {trainNo} is running on time")
    def getFare(self,trainNo, fro,to):
        print(f"ticket fare in train number: {trainNo} from {fro} to {to} is {randint(222,5555)}")
t=train(12312)
t.book("dgp", "pun")
t.getstatus(12321,"dgp", "pun")
t.getFare(12321,"dgp", "pun")