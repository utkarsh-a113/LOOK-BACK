class Animals:
    def __init__(self, w):
        self.w = w

class Pets(Animals):
    def __init__(self, w):
        super().__init__(w)
    
    def show(self):
        return f"{self.w} is a good pet!"

class Dogs(Pets):
    def __init__(self, w):
        super().__init__(w)

    @staticmethod
    def bark():
        print("Woof woof 🐶")

# Create objects
p = Pets("Anteater")
print(p.show())

d = Dogs("Bulldog")
print(d.show())
d.bark()
