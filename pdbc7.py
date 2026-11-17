#deleting entire table
import pymysql

try:
    query="DROP TABLE items"
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
    print("table deleted successfully...")
    cursor.close()
    con.close()
except:
    print("Some problem occurred....")