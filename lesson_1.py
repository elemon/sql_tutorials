'''
****************  Steps to Connect to an SQLite3 Database **********************
1.  Create a new folder in the documents folder and name it sql_tutorial
2.  Create a Python file in the sql_tutorial folder and name it lesson_1.py
3.  Copy the below code and paste it into your lesson_1.py file
4.  In the create_connection function replace username with your own username
5.  From the sql_tutorial folder type python3 lesson_1 to run the program
6.  The Terminal will say; Connection to SQLite DB successful

'''

import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("/Users/eugenelemon/documents/sql_tutorial/sm_app.sqlite")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



create_user_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL
);
"""

execute_query(connection, create_user_table) 


create_members = """
INSERT INTO
  pod (name,cell)
VALUES
  ('Baba','510.205.0980)'),
  ('Brandon','510.111.1111'),
  ('Hodari','England'),
  ('Akeem','222.333.4444');
"""

execute_query(connection, create_members)

select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)

for user in users:
	print(user)






