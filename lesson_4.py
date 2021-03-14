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

connection = create_connection("/users/eugenelemon/documents/sql_tutorial/hgp_pods.sqlite")


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
CREATE TABLE IF NOT EXISTS members (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL
);
"""

execute_query(connection, create_user_table) 


add_member = """
INSERT INTO
  members (name,cell)
VALUES
  ('Baba','510.205.0980)'),
  ('Brandon','510.111.1111'),
  ('Hodari','England'),
  ('Akeem','222.333.4444');
"""

execute_query(connection, add_member)

display_members = "SELECT * from members"
members = execute_read_query(connection, display_members)

for user in members:
	print(user)


