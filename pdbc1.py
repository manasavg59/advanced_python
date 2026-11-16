#checking database connectivity

import pymysql


try:
    con=pymysql.connect(
        host='localhost',
        user='root',
        password='Amma@0000',
        database='products'
    )
    print("Connection established successfully...")
    con.close()


except:
    print("Some problem occurred....")