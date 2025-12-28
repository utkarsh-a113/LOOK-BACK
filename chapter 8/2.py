# c/5=(f-32)/9
def ctof(c):
    f= (9*(c/5))+32
    return f
a=int(input("enter the temperature in celsius: "))
print(ctof(a))