import sqlite3

#conn = sqlite3.connect(":memory:") -> This will create a database on memory.
#Creating a company database on SQLite.

conn = sqlite3.connect("customer.db") 

#Create a cursor
c = conn.cursor()

#Query the Database
c.execute("SELECT * FROM customers WHERE LIKE first_name = 'Joao'")
c.execute("SELECT * FROM customers WHERE email LIKE '%github.com'")

items = c.fetchall()
for item in items:
    print(item)

#Commit our command
conn.commit()

#Close our connection
conn.close()