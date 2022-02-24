import sqlite3

#conn = sqlite3.connect(":memory:") -> This will create a database on memory.
#Creating a company database on SQLite.

conn = sqlite3.connect("customer.db") 

#Create a cursor
c = conn.cursor()

#Query The Database - LIMITING the RESULTS
c.execute("SELECT rowid, * FROM customers LIMIT 3")
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 3")

items = c.fetchall()

for item in items:
    print(item)

#Commit our command
conn.commit()

#Close our connection
conn.close()