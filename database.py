import sqlite3

#conn = sqlite3.connect(":memory:") -> This will create a database on memory.
#Creating a company database on SQLite.

conn = sqlite3.connect("customer.db") 

#Create a cursor
c = conn.cursor()

#Query The Database - AND/OR
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' AND rowid = 3")#(3, 'Mary', 'Brown', 'mary@codemy.com')
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 3")#(3, 'Mary', 'Brown', 'mary@codemy.com'), (4, 'Wes', 'Brown', 'wes@brown.com')

items = c.fetchall()

for item in items:
    print(item)

#Commit our command
conn.commit()

#Close our connection
conn.close()