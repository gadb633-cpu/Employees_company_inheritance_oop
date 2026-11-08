from employee import Employee
class Manager(Employee):
    def __init__(self, name, salary,bonus):
        super().__init__(name, salary,bonus)
        self.__bonus = bonus
    def title(self):
            return "Manager"
    def monthly_cost(self):
        return self.__salary + self.__bonus
    