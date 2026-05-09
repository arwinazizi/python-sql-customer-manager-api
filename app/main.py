from fastapi import FastAPI, HTTPException

from app.database import (
    create_customers_table,
    create_customer,
    delete_customer,
    get_all_customers,
    get_customer_by_id,
    update_customer
)
from app.schemas import CustomerCreate


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


@app.post("/customers", status_code=201)
def create_customer_endpoint(customer: CustomerCreate):
    new_customer_id = create_customer(
        customer.name,
        customer.email,
        customer.phone,
        customer.company
    )

    new_customer = get_customer_by_id(new_customer_id)

    return new_customer


@app.put("/customers/{customer_id}")
def update_customer_endpoint(customer_id: int, customer: CustomerCreate):
    updated_customer = update_customer(
        customer_id,
        customer.name,
        customer.email,
        customer.phone,
        customer.company
    )

    if updated_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    return updated_customer


@app.delete("/customers/{customer_id}")
def delete_customer_endpoint(customer_id: int):
    deleted_customer = delete_customer(customer_id)

    if deleted_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    return deleted_customer