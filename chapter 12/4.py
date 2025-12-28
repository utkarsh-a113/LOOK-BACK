try:
    a=int(input("enter numerator: "))
    b=int(input("enter denominator: "))
    result=a/b
    print(f"{a}/{b}={result}")
except ZeroDivisionError:
    print("Result=infinite can't divide")