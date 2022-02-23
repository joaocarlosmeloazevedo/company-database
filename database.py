import sqlite3

#conn = sqlite3.connect(":memory:") -> This will create a database on memory.
#Creating a company database on SQLite.

conn = sqlite3.connect("customer.db") 

#Create a cursor
c = conn.cursor()

#Inserting many items to a Table.
many_customers = [
                    ('Cas', 'Cão', 'cascao@github.com'),
                    ('Maga', 'Li', 'magali@github.com'),
                    ('Mon','Ica','monica@github.com'),
]        
print("Command executed succesfully!")

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

#Commit our command
conn.commit()

#Close our connection
conn.close()