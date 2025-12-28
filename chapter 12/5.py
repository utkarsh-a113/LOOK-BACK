n=int(input("Enter a number: "))
table=[f"{n}x{i}={n*i}" for i in range(1,11)]
with open("Tables.txt",'w+') as f:
    f.write("\n".join(table))
print(f"Multiplication table of {n} stored in Tables.txt")