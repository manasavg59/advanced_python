#inserting single values

import pymysql

try:
    query="INSERT INTO  items(id,iname,price) VALUES(%s,%s,%s)"

    v=[
        (11,'monitor',2999),
        (12,'keyboard',9008)
    ]
    
    con=pymysql.connect(
        host='localhost',
        user='root',
        password='Amma@0000',
        database='products'
    )
    print("Connection established successfully...")
    cursor=con.cursor()
    cursor.executemany(query,v)
    con.commit()
    print("data inserted successfully.")
    cursor.close()
    con.close()


except:
    print("Some problem occurred....")