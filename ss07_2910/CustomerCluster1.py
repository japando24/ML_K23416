from flask import Flask
from flaskext.mysql import MySQL
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans
import numpy as np


app = Flask(__name__)
def getConnect (server, port, database, username, password):
    try:
        mysql = MySQL()
        #My SQL configurations
        app.config['MYSQL_DATABASE_HOST'] = server
        app.config['MYSQL_DATABASE_PORT'] = port
        app.config['MYSQL_DATABASE_DB'] = database
        app.config['MYSQL_DATABASE_USER'] = username
        app.config['MYSQL_DATABASE_PASSWORD'] = password
        mysql.init_app(app)
        conn = mysql.connect()
        return conn
    except mysql.connect.Error as e:
        print ("Error = ",e)
    return None
def closeConnection(conn):
    if conn != None:
        conn.close()
def queryDataset(conn, sql):
    cursor = conn.cursor()

    cursor.execute(sql)
    df = pd.DataFrame(cursor.fetchall())
    return df

conn = getConnect('localhost', 3306, 'salesdatabase','root','@Dnb24042004')

sql1="select * from customer"
df1 = queryDataset(conn, sql1)
print(df1)


sql2 = """
        SELECT DISTINCT c.CustomerID, c.Age, cs.Annual_Income, cs.Spending_Score
        FROM customer c
        JOIN customer_spend_score cs ON c.CustomerID = cs.CustomerID
    """

df2 = queryDataset(conn, sql2)
df2.columns = ['CustomerId', 'Age', 'Annual Income', 'Spending Score']
print(df2)
print(df2.head())
print(df2.describe())

def showHistogram(df, columns):
    plt.figure(1, figsize = (7,8))
    n = 0
    for column in columns:
        n += 1
        plt.subplot(3, 1, n)
        plt.subplots_adjust(hspace = 0.5,wspace=0.5)
        sns.distplot(df[column], bins=32)
        plt.title(f'Histogram of {column}')
    plt.show()

showHistogram(df2,df2.columns[1:])