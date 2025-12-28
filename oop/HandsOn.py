class Student:
    def __init__(self,name,roll):# what is going inside these brackets 
        self.name=name
        self.roll=roll
    #yeh humney class define kiya 
#abb objects define karenge aur yeh class key bahar rahega
s1=Student("Utkarsh",101) #value pass ho rahi hai
s2=Student("Rawnak",102)

#abb main inko call karunga
print(s1.name,s1.roll)
print(s2.name,s2.roll)
