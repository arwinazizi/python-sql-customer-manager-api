import sqlite3


DATABASE_NAME = "customers.db"


def create_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection


def row_to_customer(row):
    customer = {
        "id": row[0],
        "name": row[1],
        "email": row[2],
        "phone": row[3],
        "company": row[4],
        "created_at": row[5]
    }

    return customer


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
        customer = row_to_customer(row)
        customers.append(customer)

    connection.close()

    return customers


def get_customer_by_id(customer_id):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email, phone, company, created_at
        FROM customers
        WHERE id = ?
    """, (customer_id,))

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return None

    return row_to_customer(row)


def update_customer(customer_id, name, email, phone, company):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE customers
        SET name = ?, email = ?, phone = ?, company = ?
        WHERE id = ?
    """, (name, email, phone, company, customer_id))

    connection.commit()

    updated_rows = cursor.rowcount

    connection.close()

    if updated_rows == 0:
        return None

    return get_customer_by_id(customer_id)


def delete_customer(customer_id):
    customer = get_customer_by_id(customer_id)

    if customer is None:
        return None

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM customers
        WHERE id = ?
    """, (customer_id,))

    connection.commit()
    connection.close()

    return customer


if __name__ == "__main__":
    create_customers_table()

    new_customer_id = create_customer(
        "Delete Test",
        "delete.test@example.com",
        "0704444444",
        "Delete Company"
    )

    deleted_customer = delete_customer(new_customer_id)

    print(deleted_customer)
    print(get_customer_by_id(new_customer_id))