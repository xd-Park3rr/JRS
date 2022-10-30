import sqlite3

conn = sqlite3.connect("Employees.db")

c = conn.cursor()

# c.execute("""CREATE TABLE
# name TEXT,
# surname TEXT, 
# age INTEGER, 
# occupation TEXT, 
# email TEXT, 
# """)

conn.commit()