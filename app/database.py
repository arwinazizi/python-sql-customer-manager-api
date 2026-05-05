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


if __name__ == "__main__":
    create_customers_table()
    print("Customers table created successfully.")