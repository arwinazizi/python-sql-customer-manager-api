from fastapi import FastAPI, HTTPException

from app.database import (
    create_customers_table,
    get_all_customers,
    get_customer_by_id
)


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


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    customer = get_customer_by_id(customer_id)

    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    return customer