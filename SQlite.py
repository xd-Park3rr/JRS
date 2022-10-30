import sqlite3 as sq
import employees

getinput = employees()



conn = sq.connect("Employees.db")

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#     name TEXT,
#     surname TEXT,
#     age INTEGER,
#     occupation TEXT,
#     email TEXT,
#     )"""
# )

c.execute("INSERT INTO employees VALUES ('mark', 20, 1.9)")

conn.commit()

#conn.close()