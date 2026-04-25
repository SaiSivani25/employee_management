from models.person import Person

class Employee(Person):
    def __init__(self, name: str, age: int, salary: float, employee_id: int = None):
        super().__init__(name, age)
        self.salary = salary
        self.employee_id = employee_id