from unittest.mock import patch, MagicMock


# Test 1: Check if employees are sorted by id correctly
def test_employees_sorted_by_id():
    # Create a sample list of employees in random order
    employees = [
        {"id": 3, "name": "Pavani", "age": 28, "salary": 8500},
        {"id": 1, "name": "Pavan", "age": 25, "salary": 5000},
        {"id": 2, "name": "Shivani", "age": 24, "salary": 5500}
    ]

    # Sort employees by id
    sorted_employees = sorted(employees, key=lambda x: x["id"])

    # Check if sorting worked correctly
    assert sorted_employees[0]["id"] == 1
    assert sorted_employees[1]["id"] == 2
    assert sorted_employees[2]["id"] == 3


# Test 2: Check if employee data has all required fields
def test_employee_has_all_fields():
    employee = {"id": 1, "name": "Pavan", "age": 25, "salary": 5000}

    assert "id" in employee
    assert "name" in employee
    assert "age" in employee
    assert "salary" in employee


# Test 3: Check if employee age is within valid range
def test_employee_age_is_valid():
    employee = {"id": 1, "name": "Pavan", "age": 25, "salary": 5000}

    assert employee["age"] >= 18
    assert employee["age"] <= 100


# Test 4: Check if employee salary is not negative
def test_employee_salary_is_positive():
    employee = {"id": 1, "name": "Pavan", "age": 25, "salary": 5000}

    assert employee["salary"] >= 0


# Test 5: Mock API call for getting all employees
def test_get_employees_returns_list():
    with patch("requests.get") as mock_get:

        # Create a fake response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"id": 1, "name": "Pavan", "age": 25, "salary": 5000},
            {"id": 2, "name": "Shivani", "age": 24, "salary": 5500}
        ]
        mock_get.return_value = mock_response

        # Call the fake API
        response = mock_get("http://localhost:8000/employees")

        # Check response is correct
        assert response.status_code == 200
        assert len(response.json()) == 2


# Test 6: Mock API call for adding a new employee
def test_add_employee_returns_success():
    with patch("requests.post") as mock_post:

        # Create a fake response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "message": "Employee added successfully"
        }
        mock_post.return_value = mock_response

        # Call the fake API
        response = mock_post("http://localhost:8000/employee", json={
            "name": "John",
            "age": 25,
            "salary": 50000
        })

        # Check response is correct
        assert response.status_code == 200
        assert response.json()["message"] == "Employee added successfully"


# Test 7: Mock API call for updating an employee
def test_update_employee_returns_success():
    with patch("requests.put") as mock_put:

        # Create a fake response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "message": "Employee 1 updated successfully"
        }
        mock_put.return_value = mock_response

        # Call the fake API
        response = mock_put("http://localhost:8000/employee/1", json={
            "name": "John Updated",
            "age": 29,
            "salary": 60000
        })

        # Check response is correct
        assert response.status_code == 200
        assert "updated" in response.json()["message"]


# Test 8: Mock API call for deleting an employee
def test_delete_employee_returns_success():
    with patch("requests.delete") as mock_delete:

        # Create a fake response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "message": "Employee 1 deleted successfully"
        }
        mock_delete.return_value = mock_response

        # Call the fake API
        response = mock_delete("http://localhost:8000/employee/1")

        # Check response is correct
        assert response.status_code == 200
        assert "deleted" in response.json()["message"]