import os

# create "tables" folder if it doesn't exist
os.makedirs("tables", exist_ok=True)

def tables(n):
    x = ""
    for i in range(1, 11):
        x += f"{n} * {i} = {n*i}\n"
        
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(x)

for i in range(2, 21):
    tables(i)
