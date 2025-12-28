greatest=None
for i in range(4):
    num=int(input(f"enter the number {i}: "))
    if greatest is None or num >greatest:
        greatest=num

print(f"{greatest} is the greatest number")
