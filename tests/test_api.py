from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_employee():
    # Test adding a new employee to the system
    new_employee = {
        "name": "John Smith",
        "age": 28,
        "salary": 55000
    }
    response = client.post("/employee", json=new_employee)
    assert response.status_code == 200
    assert response.json()["message"] == "Employee added successfully"


def test_get_all_employees():
    # Test retrieving all employees from the system
    response = client.get("/employees")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_median_age():
    # Test getting the median age of all employees
    response = client.get("/stats/median-age")
    assert response.status_code == 200
    assert "median_age" in response.json()


def test_get_median_salary():
    # Test getting the median salary of all employees
    response = client.get("/stats/median-salary")
    assert response.status_code == 200
    assert "median_salary" in response.json()


def test_update_employee():
    # Test updating an existing employee details
    updated_data = {
        "name": "John Smith Updated",
        "age": 29,
        "salary": 60000
    }
    response = client.put("/employee/1", json=updated_data)
    assert response.status_code == 200
    assert "updated" in response.json()["message"]


def test_delete_employee():
    # Test deleting an existing employee from the system
    response = client.delete("/employee/1")
    assert response.status_code == 200
    assert "deleted" in response.json()["message"]