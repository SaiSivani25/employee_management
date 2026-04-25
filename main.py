from fastapi import FastAPI
from pydantic import BaseModel
from db.db_utils import (
    add_employee,
    get_all_employees,
    delete_employee_by_id,
    get_median_age,
    get_median_salary,
    update_employee

)

app = FastAPI()


class EmployeeInput(BaseModel):
    name: str
    age: int
    salary: float

# Add a new employee
@app.post("/employee")
def create_employee(emp: EmployeeInput):
    add_employee(emp.name, emp.age, emp.salary)
    return {"message": "Employee added successfully"}


# Get all employees
@app.get("/employees")
def read_employees():
    rows = get_all_employees()
    employees = []
    for r in rows:
        employee = {"id":r[0], "name": r[1], "age": r[2], "salary": r[3]}
        employees.append(employee)
    return employees

# delete an employee by ID
@app.delete("/employee/{id}")
def remove_employee(id: int):
    delete_employee_by_id(id)
    return {"message": f"Employee {id} deleted successfully"}

# get median age of all employees
@app.get("/stats/median-age")
def median_age():
    age = get_median_age()
    return {"median_age": age}

#Get median salary of all employees
@app.get("/stats/median-salary")
def median_salary():
    salary = get_median_salary()
    return {"median_salary": salary}


# Update an employee
@app.put("/employee/{id}")
def update_employee_route(id: int, emp: EmployeeInput):
    update_employee(id, emp.name, emp.age, emp.salary)
    return {"message": f"Employee {id} updated successfully"}


