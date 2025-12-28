marks = int(input("Enter the student's marks (0-100): "))
if 90 <= marks <= 100:
    grade = "Ex"
elif 80 <= marks < 90:
    grade = "A"
elif 70 <= marks < 80:
    grade = "B"
elif 60 <= marks < 70:
    grade = "C"
elif 50 <= marks < 60:
    grade = "D"
elif 0 <= marks < 50:
    grade = "F"
else:
    grade = "Invalid marks! Please enter between 0 and 100"
print("Grade:", grade)