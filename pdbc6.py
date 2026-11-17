#deleting 1 row 

import pymysql

try:
    query="DELETE FROM items WHERE id=%d"

   
    
    con=pymysql.connect(
        host='localhost',
        user='root',
        password='Amma@0000',
        database='products'
    )
    print("Connection established successfully...")
    cursor=con.cursor()
    n=int(input("ENTER ID:"))
    cursor.execute(query%(n))
    con.commit()
    print("data deleted successfully.")
    cursor.close()
    con.close()


except:
    print("Some problem occurred....")