print("Old way")
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])

print("Better way")
for i, fruit in enumerate(fruits):
    print(i, fruit)
