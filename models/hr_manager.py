from models.employee import Employee

class HRManager(Employee):
    def __init__(self, name: str, age: int, salary: float, employee_id: int = None):
        super().__init__(name, age, salary, employee_id)

    def hire(self, employee_name: str):
        return f"{self.name} hired {employee_name}"
    
    def fire(self, employee_name: str):
        return f"{self.name} fired {employee_name}"