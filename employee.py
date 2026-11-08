class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def title(self):
        return "Employee"
    def monthly_cost(self):
        return self.salary
    def describe(self):
        return f"name: {self.name} \ntitle: {self.title()} \nmonthly_cost: {self.monthly_cost()}"