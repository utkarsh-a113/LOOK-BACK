# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.
class programmer:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        # print(f"{name} is earning {salary}")
    def microsoft(self,name,salary):
        print(f"{self.name} is earning {self.salary}")
p=programmer("utkarsh",1000000)
p.microsoft("rawnak",1200000)
