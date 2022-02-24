import sqlite3

#conn = sqlite3.connect(":memory:") -> This will create a database on memory.
#Creating a company database on SQLite.

conn = sqlite3.connect("customer.db") 

#Create a cursor
c = conn.cursor()

#DROP TABLE
c.execute("DROP TABLE customers")
conn.commit()

c.execute("SELECT rowid, * FROM customers")


items = c.fetchall()

for item in items:
    print(item)

#Commit our command
conn.commit()

#Close our connection
conn.close()