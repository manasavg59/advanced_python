#creating item table

import pymysql

try:
    query="CREATE TABLE IF NOT EXISTS items(id INT,iname VARCHAR(20),price FLOAT)"
    
    con=pymysql.connect(
        host='localhost',
        user='root',
        password='Amma@0000',
        database='products'
    )
    print("Connection established successfully...")
    cursor=con.cursor()
    cursor.execute(query)
    print("table created successfully.")
    cursor.close()
    con.close()


except:
    print("Some problem occurred....")