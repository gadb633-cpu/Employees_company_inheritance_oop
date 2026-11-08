from employee import Employee
class Intern(Employee):
    def __init__(self, name, salary,months):
        super().__init__(name, salary)
        if 1 < months or months>12:
            self.months =months
        else:
            raise ValueError("months must be 1-12") 
    def title(self):
        return "Intern"    
