class Employee:
    def __init__(self,salary,increment):
        self.salary=salary
        self.increment=increment
    def apply_increment(self):
        self.salary=self.salary+(self.salary*self.increment/100)
        return self.salary
    def show_details(self):
        print(f"salary: {self.salary}, Increment: {self.increment}%")
emp1 = Employee(50000, 10)   # salary=50,000, increment=10%
emp1.show_details()
new_salary = emp1.apply_increment()
print("New Salary:", new_salary)
    