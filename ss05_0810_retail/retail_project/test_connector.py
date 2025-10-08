import traceback

import mysql.connector

server="localhost"
port=3306
database="k23416_retail"
username="root"
password="@Dnb24042004"
try:
    conn = mysql.connector.connect(
                    host=server,
                    port=port,
                    database=database,
                    user=username,
                    password=password)
except:
    traceback.print_exc()
print("Successfully connected to MySQL server")

# #Q1: Login for Customer
# def login_customer (email, pwd):
#     cursor = conn.cursor()
#     sql = "SELECT * FROM customer where Email='"+email +"' and Password ='"+pwd+"'"
#     print(sql)
#     cursor.execute(sql)
#     dataset = cursor.fetchone()
#     if dataset != None:
#         print(dataset)
#     else:
#         print("Login Failed")
#     cursor.close()
# login_customer("japando2004@gmail.com","24042004")

def login_employee (email, pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM employee where Email=%s and Password=%s"
    val = (email, pwd)
    cursor.execute(sql, val)
    dataset = cursor.fetchone()
    if dataset != 0:
        print(dataset)
    else:
        print("Login Failed")
    cursor.close()
login_employee("johndo24@gmail.com","24042004")

