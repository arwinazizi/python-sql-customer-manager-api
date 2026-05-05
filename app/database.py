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


if __name__ == "__main__":
    create_customers_table()

    customer_id = create_customer(
        "Ali Hassan",
        "ali@example.com",
        "0701234567",
        "Ali Consulting"
    )

    print(f"Created customer with ID: {customer_id}")