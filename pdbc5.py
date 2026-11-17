#updating data

import pymysql

try:
    query="UPDATE items SET price=%s WHERE id=%d"

    
    con=pymysql.connect(
        host='localhost',
        user='root',
        password='Amma@0000',
        database='products'
    )
    print("Connection established successfully...")
    cursor=con.cursor()
    n=int(input("Enter id :"))
    price=int(input("Enter price for updation :"))
    cursor.execute(query%(price,n))
    con.commit()
    print("data updated successfully.")
    cursor.close()
    con.close()


except:
    print("Some problem occurred....")