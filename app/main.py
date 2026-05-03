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


def create_customer(name, email, phone, company):
    new_id = len(customers) + 1

    new_customer = {
        "id": new_id,
        "name": name,
        "email": email,
        "phone": phone,
        "company": company
    }

    customers.append(new_customer)

    return new_customer


def update_customer(customer_id, name, email, phone, company):
    for customer in customers:
        if customer["id"] == customer_id:
            customer["name"] = name
            customer["email"] = email
            customer["phone"] = phone
            customer["company"] = company

            return customer

    return None


print(get_customer_by_id(2))

updated_customer = update_customer(
    2,
    "Sara Andersson",
    "sara.andersson@example.com",
    "0701112222",
    "Andersson Design"
)

print(updated_customer)
print(get_customer_by_id(2))