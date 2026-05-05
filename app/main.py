from fastapi import FastAPI

from app.database import create_customers_table, get_all_customers


app = FastAPI()


@app.on_event("startup")
def startup():
    create_customers_table()


@app.get("/")
def root():
    return {
        "message": "Python SQL Customer Manager API"
    }


@app.get("/customers")
def list_customers():
    customers = get_all_customers()
    return customers