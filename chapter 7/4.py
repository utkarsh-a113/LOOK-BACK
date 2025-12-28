a=int(input("enter the number: "))
for i in range(2,a):
    if (a%i)==0:
        print(f"not prime number")
        break
else:
        print("prime")
