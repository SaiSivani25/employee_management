# Employee Management System

A full-stack Employee Management System built with FastAPI, PostgreSQL, and Streamlit.

## What This App Does
- Add, view, update, and delete employees
- View median age and salary statistics
- Built with a FastAPI backend and interactive Streamlit frontend UI

## Tech Stack
| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| FastAPI | Backend API framework |
| PostgreSQL | Database |
| psycopg2 | Database connector (no ORM) |
| Streamlit | Frontend UI |
| pytest | Unit testing |
| Postman | API testing |
| Snyk | Security scanning |
| dotenv | Environment variables |

## Project Structure
```
employee_management/
├── models/
│   ├── person.py
│   ├── employee.py
│   └── hr_manager.py
├── db/
│   └── db_utils.py
├── tests/
│   ├── test_api.py
│   └── test_ui_logic.py
├── main.py
├── streamlit_app.py
├── .env.example
├── requirements.txt
└── snyk_report.md
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /employee | Add new employee |
| GET | /employees | Get all employees |
| PUT | /employee/{id} | Update employee |
| DELETE | /employee/{id} | Delete employee |
| GET | /stats/median-age | Get median age |
| GET | /stats/median-salary | Get median salary |

## How to Run

### Step 1: Create virtual environment
```
python -m venv venv
venv\Scripts\activate
```

### Step 2: Install dependencies
```
pip install -r requirements.txt
```

### Step 3: Create .env file
```
DB_HOST=localhost
DB_NAME=employee_db
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_PORT=5432
```

### Step 4: Start FastAPI Backend
```
uvicorn main:app --reload
```

### Step 5: Start Streamlit Frontend
```
streamlit run streamlit_app.py
```

### Step 6: View Swagger UI
```
http://localhost:8000/docs
```

### Step 7: View Streamlit UI
```
http://localhost:8501
```

## Running Tests
```
$env:PYTHONPATH = "."; pytest tests/ -v
```

## Security Scan
Snyk security scan performed - no vulnerabilities found!
```
snyk test --file=requirements.txt
```

## GitHub Repository
Push code to GitHub:
```
git init
git add .
git commit -m "Employee Management System"
git branch -M main
git remote add origin https://github.com/yourusername/employee-management.git
git push -u origin main
```