customers = []

customer1 = {
    "id": 1,
    "name": "Ali Hassan",
    "email": "ali@example.com",
    "phone": "0701234567",
    "company": "Ali Consulting"
}

customer2 = {
    "id": 2,
    "name": "Sara Ahmed",
    "email": "sara@example.com",
    "phone": "0707654321",
    "company": "Sara Design"
}

customer3 = {
    "id": 3,
    "name": "Lina Josef",
    "email": "lina@example.com",
    "phone": "0707454321",
    "company": "Lina AI"
}

customers.append(customer1)
customers.append(customer2)
customers.append(customer3)


def list_customers():
    return customers


def get_customer_by_id(customer_id):
    for customer in customers:
        if customer["id"] == customer_id:
            return customer

    return None


print(list_customers())
print(get_customer_by_id(2))
print(get_customer_by_id(99))