import sqlite3

#conn = sqlite3.connect(":memory:") -> This will create a database on memory.
#Creating a company database on SQLite.

conn = sqlite3.connect("customer.db") 

#Create a cursor
c = conn.cursor()

#Order Data

c.execute("SELECT * FROM customers ORDER BY last_name DESC") #Ordering alphabetically descending
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")

items = c.fetchall()
for item in items:
    print(item)

#Commit our command
conn.commit()

#Close our connection
conn.close()