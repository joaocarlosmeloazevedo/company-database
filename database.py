import sqlite3

#conn = sqlite3.connect(":memory:") -> This will create a database on memory.
#Creating a company database on SQLite.

conn = sqlite3.connect("customer.db") 

#Create a cursor
c = conn.cursor()

#Update Records
c.execute("""UPDATE customers SET first_name = "Casquinho"
            WHERE rowid = 4
         """)

#Delete Records
c.execute("DELETE from customers WHERE rowid = 6")
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()
for item in items:
    print(item)

#Commit our command
conn.commit()

#Close our connection
conn.close()