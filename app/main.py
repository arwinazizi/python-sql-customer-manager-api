from fastapi import FastAPI

from app.database import create_customers_table


app = FastAPI()


@app.on_event("startup")
def startup():
    create_customers_table()


@app.get("/")
def root():
    return {
        "message": "Python SQL Customer Manager API"
    }