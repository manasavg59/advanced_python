#inserting single values

import pymysql

try:
    query="INSERT INTO  items(id,iname,price) VALUES(10,'mouse',2900)"
    
    con=pymysql.connect(
        host='localhost',
        user='root',
        password='Amma@0000',
        database='products'
    )
    print("Connection established successfully...")
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    print("data inserted successfully.")
    cursor.close()
    con.close()


except:
    print("Some problem occurred....")