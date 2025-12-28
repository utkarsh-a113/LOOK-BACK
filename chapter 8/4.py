n=int(input("enter the number: "))
def sumN(n):
    i=1
    sum=0
    while(i<=n):
        sum+=i
        i=i+1
    return sum
print(sumN(n))