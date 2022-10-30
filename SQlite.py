import sqlite3 as sq
from employees import employee

getinput = employee()

getinput.getalldetails()

name = getinput.name
surname = getinput.surname
age = getinput.age
occupation = getinput.occupation 



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

# c.execute("INSERT INTO employees VALUES (name, surname, age, occupation, ?)")
c.execute("INSERT INTO employees VALUES ("+name+", "+surname+", "+age+", "+occupation+", 'email@gmail.com')")

conn.commit()
#screw almal
#conn.close()
