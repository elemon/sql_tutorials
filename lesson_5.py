'''
**************************************************************
  Program  lessson_5.py
  Author   Baba
  Date     March 13, 2021

  Description:
  This program is used to introduce Geniuses to using a 
  database Structured Query Language (SQL).  The program
  imports the sqlite3 module which allows you to create
  and interact with an SQL Database

  - The create_connection function is passed the
    path of the SQLite database file then it connects 
    the app to an exixting SQLite3 database named hgp_pods 
    or if it;s not present it creates the database file
  
  - The execute_query function is passed the path and the 
    query to implement; create_staff_member_table query and
    add_staff_member query

  - The execute_read function is passed the path and 
    the display_staff_member query
**************************************************************

'''

import sqlite3
from sqlite3 import Error

############### Function Definitions *******************
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

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


###################  Connect to The Database File *********************
connection = create_connection("/users/eugenelemon/documents/sql_tutorial/oak8_pods.sqlite")


##########################  Create And Execute Queries ################
create_staff_member_table_query = """
CREATE TABLE IF NOT EXISTS staff (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""
execute_query(connection, create_staff_member_table_query) 

add_staff = """
INSERT INTO
  staff (name,cell,position)
VALUES
  ('Baba','510.205.0980)','Senior Innovation Educator'),
  ('Brandon','111.111.1111', 'Executive Director'),
  ('Hodari','(510) 435-2594','Curriculum Lead'),
  ('Akeem','(415) 684-0505','Programs Director');
"""
execute_query(connection, add_staff)


########################### Display staff_member Query ##################### 
display_staff_query = "SELECT * from staff"
staff = execute_read_query(connection, display_staff_query)
  
for user in staff:
	print(user)


