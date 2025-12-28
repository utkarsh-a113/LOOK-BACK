class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment  # in percentage (%)

    @property
    def salaryAfterIncrement(self):
        """Calculate salary after applying increment"""
        return self.salary + (self.salary * self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        """Update increment based on desired new salary"""
        self.increment = ((new_salary - self.salary) / self.salary) * 100

emp = Employee(50000, 10)

print("Original Salary:", emp.salary)
print("Increment %:", emp.increment)
print("Salary After Increment:", emp.salaryAfterIncrement)

# Now set a new salary directly
emp.salaryAfterIncrement = 60000   # this changes increment automatically

print("\nAfter Setter Update:")
print("New Increment %:", emp.increment)
print("Updated Salary After Increment:", emp.salaryAfterIncrement)
