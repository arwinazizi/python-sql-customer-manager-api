# Python SQL Customer Manager API

A small backend API built with Python, FastAPI, SQLite, and raw SQL.

The goal of this project is to demonstrate practical backend fundamentals for a junior Python/SQL developer role.

## Tech stack

- Python
- FastAPI
- SQLite
- Raw SQL
- Pydantic validation
- Git / GitHub

## Features

- Create customer
- List customers
- Get customer by ID
- Update customer
- Delete customer
- Search customers
- Validate request data
- Handle duplicate email errors
- Store customer data in a relational database

## Project structure

```txt
app/
├── __init__.py
├── main.py
├── database.py
├── routes.py
└── schemas.py
```

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Root message |
| GET | `/customers` | List all customers |
| GET | `/customers/search?query=ali` | Search customers |
| GET | `/customers/{customer_id}` | Get customer by ID |
| POST | `/customers` | Create customer |
| PUT | `/customers/{customer_id}` | Update customer |
| DELETE | `/customers/{customer_id}` | Delete customer |

## Example request

POST `/customers`

```json
{
  "name": "Ali Hassan",
  "email": "ali@example.com",
  "phone": "0701234567",
  "company": "Ali Consulting"
}
```

## Example response

```json
{
  "id": 1,
  "name": "Ali Hassan",
  "email": "ali@example.com",
  "phone": "0701234567",
  "company": "Ali Consulting",
  "created_at": "2026-05-09 12:00:00"
}
```

## Database

The project uses SQLite and raw SQL.

Main table:

```sql
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    company TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Setup

Clone the repository:

```bash
git clone https://github.com/arwinazizi/python-sql-customer-manager-api.git
cd python-sql-customer-manager-api
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Open Swagger docs:

```txt
http://127.0.0.1:8000/docs
```

## What this project demonstrates

This project demonstrates:

- Python fundamentals
- CRUD operations
- SQL basics
- SQLite database usage
- API design with FastAPI
- Request validation with Pydantic
- Error handling
- Git workflow with small commits
- Separation of concerns between routes, schemas, and database logic

## Next improvements

Potential improvements:

- Add automated tests
- Add a second table such as notes or orders
- Add SQL JOIN examples
- Add PostgreSQL support
- Add pagination