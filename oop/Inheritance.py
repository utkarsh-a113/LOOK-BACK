class Vehicle:
    def __init__(self, brand): #constructor
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

# Car inherits from Vehicle that is the above class wahan sey inheritance aa raha hai down here

class Car(Vehicle):
    def honk(self):
        print("Beep beep!")
#objects yahan hai
car1 = Car("Toyota")
car1.start()  # Toyota is starting...
car1.honk()   # Beep beep!
