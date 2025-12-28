#Attributes = variables inside class (like car’s color, brand).
#Methods = functions inside class (like start, stop).
class Car:
    def __init__(self,brand,colour): # Constructor (special method to initialize objects)
        self.brand=brand #attribute
        self.colour=colour #attribute
    #method
    def drive(self):
        print(f"{self.brand} is revving")

#creating 2 objects
car1=Car("Tesla","Red") #tesla red
car2=Car("BMW","black") #BMW CAr is Driving
car3=Car("lamborgini","grey")
car3.drive()
print(car1.brand,car1.colour)
car2.drive()