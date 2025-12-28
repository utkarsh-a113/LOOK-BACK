total=0
for i in range(0,3):
    marks=int(input(f"enter the marks{i+1}: "))
    total+=marks
if(total>=40):
    print("pass")
else:
    print("failed")
