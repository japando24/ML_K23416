import traceback

import mysql.connector

from ss05_0810_retail.retail_project.models.customer import Customer

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

#Q1: Login for Customer
def login_customer (email, pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM customer where Email='"+email +"' and Password ='"+pwd+"'"
    cust=None
    cursor.execute(sql)
    dataset = cursor.fetchone()
    if dataset != None:
        cust = Customer(dataset[0],dataset[1],dataset[2],dataset[3],dataset[4],dataset[5])
        #cust.ID,cust.Name,cust.Phone,cust.Email,cust.Password,cust.IsDeleted = dataset
    cursor.close()
    return cust
cust= login_customer("japando2004@gmail.com","24042004")
if cust==None:
    print("Login failed")
else:
    print("Login successful")
    print(cust)
