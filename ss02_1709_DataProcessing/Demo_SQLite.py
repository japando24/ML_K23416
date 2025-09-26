import sqlite3
import pandas as pd

try:
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('../datasets/databases/Chinook_Sqlite.sqlite')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # Write a query and execute it with cursor
    query = "SELECT * FROM InvoiceLine LIMIT 5;"
    cursor.execute(query)

    # Fetch data
    rows = cursor.fetchall()

    # Get column names from cursor.description
    col_names = [description[0] for description in cursor.description]

    # Create DataFrame with column names
    df = pd.DataFrame(rows, columns=col_names)
    print(df)

except sqlite3.Error as error:
    print('Error occurred -', error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection Closed')

















#NO COLUMB NAME
# import sqlite3
# import pandas as pd
# try:
#     #Connect to DB and create a cursor
#     sqliteConnection = sqlite3.connect('../datasets/databases/Chinook_Sqlite.sqlite')
#     cursor = sqliteConnection.cursor()
#     print('DB Init')
#     #Write a query and execute it with cursor
#     query = "SELECT * FROM InvoiceLine LIMIT 5;"
#     cursor.execute(query)
#     #Fetch and output result
#     df = pd.DataFrame(cursor.fetchall())
#     print(df)
#     #Close the cursor
# #Handle errors
# except sqlite3.Error as error:
#     print('Error occurred -',error)
# #Close DB Connection irrespective of success or failure
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print('SQLite Connection Closed')