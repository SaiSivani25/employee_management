import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")

    )
    return conn

def add_employee(name, age, salary):
    conn = get_connection()
    cur = conn.cursor()

    query = "INSERT INTO employees (name, age, salary) VALUES (%s, %s, %s)"
    values = (name, age, salary)
    cur.execute(query, values)

    conn.commit()
    cur.close()
    conn.close()

def get_all_employees():
    conn = get_connection()
    cur = conn.cursor()

    query = "SELECT * FROM employees"
    cur.execute(query)
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows

def delete_employee_by_id(employee_id):
    conn = get_connection()
    cur = conn.cursor()

    query = "DELETE FROM employees WHERE id = %s"
    cur.execute(query, (employee_id,))

    conn.commit()
    cur.close()
    conn.close()

def get_median_age():
    conn = get_connection()
    cur = conn.cursor()

    query = "SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY age) FROM employees"
    cur.execute(query)
    result = cur.fetchone()[0]

    cur.close()
    conn.close()
    return result

def get_median_salary():
    conn = get_connection()
    cur = conn.cursor()

    query = "SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees"
    cur.execute(query)
    result = cur.fetchone()[0]

    cur.close()
    conn.close()
    return result


def update_employee(employee_id, name, age, salary):
    conn = get_connection()
    cur = conn.cursor()

    query = "UPDATE employees SET name = %s, age = %s, salary = %s WHERE id = %s"
    values = (name, age, salary, employee_id)
    cur.execute(query, values)

    conn.commit()
    cur.close()
    conn.close()