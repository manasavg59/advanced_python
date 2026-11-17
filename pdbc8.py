# Example program for rollback()

import pymysql

try:
    connnn = pymysql.connect(
        host='localhost',
        user='root',
        password='Amma@0000',
        database='products'
    )

    print("Database connected successfully...")

    cursor = connnn.cursor()

    # Insert a record
    query = "INSERT INTO items(id, iname, price) VALUES(20, 'Keyboard', 1500)"

    cursor.execute(query)

    print("Data inserted temporarily...")

    # Rollback the changes
    connnn.rollback()

    print("Changes cancelled successfully...")

    cursor.close()
    connnn.close()

except Exception as e:
    print("Some problem occurred:", e)