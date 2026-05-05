import sqlite3


DATABASE_NAME = "customers.db"


def create_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection


def create_customers_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT,
            company TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def create_customer(name, email, phone, company):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO customers (name, email, phone, company)
        VALUES (?, ?, ?, ?)
    """, (name, email, phone, company))

    connection.commit()

    new_customer_id = cursor.lastrowid

    connection.close()

    return new_customer_id


def get_all_customers():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email, phone, company, created_at
        FROM customers
    """)

    rows = cursor.fetchall()

    customers = []

    for row in rows:
        customer = {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "phone": row[3],
            "company": row[4],
            "created_at": row[5]
        }

        customers.append(customer)

    connection.close()

    return customers


if __name__ == "__main__":
    create_customers_table()

    customers = get_all_customers()

    print(customers)