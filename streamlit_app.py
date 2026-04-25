import streamlit as st
import requests

APP_URL = "http://localhost:8000"

st.title("Employee Management System")

menu = st.sidebar.selectbox("Menu", [
    "View All Employees",
    "Add Employee",
    "Update Employee",
    "Delete Employee",
    "Statistics"
])

# View All Employees
if menu == "View All Employees":
    st.subheader("All Employees")
    response = requests.get(f"{APP_URL}/employees")
    employees = response.json()
    employees = sorted(employees, key=lambda x: x["id"])
    st.dataframe(employees)

# Add Employee
elif menu == "Add Employee":
    st.subheader("Add New Employee")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, max_value=100)
    salary = st.number_input("Salary", min_value=0)

    if st.button("Add Employee"):
        requests.post(f"{APP_URL}/employee", json={
            "name": name,
            "age": age,
            "salary": salary
        })
        st.success("Employee added successfully!")

# Update Employee
elif menu == "Update Employee":
    st.subheader("Update Employee")

    emp_id = st.number_input("Employee ID to update", min_value=1)
    new_name = st.text_input("Name")
    new_age = st.number_input("Age", min_value=18)
    new_salary = st.number_input("Salary", min_value=0)

    if st.button("Update"):
        requests.put(f"{APP_URL}/employee/{emp_id}", json={
            "name": new_name,
            "age": new_age,
            "salary": new_salary
        })
        st.success("Employee updated!")

# Delete Employee
elif menu == "Delete Employee":
    st.subheader("Delete Employee")

    emp_id = st.number_input("Employee ID to delete", min_value=1)

    if st.button("Delete"):
        requests.delete(f"{APP_URL}/employee/{emp_id}")
        st.success("Employee deleted!")

# Statistics
elif menu == "Statistics":
    st.subheader("Statistics")

    age_response = requests.get(f"{APP_URL}/stats/median-age")
    salary_response = requests.get(f"{APP_URL}/stats/median-salary")

    st.write("Median Age:", age_response.json()["median_age"])
    st.write("Median Salary:", salary_response.json()["median_salary"])