import sqlite3

#conn = sqlite3.connect(":memory:") -> This will create a database on memory.
#Creating a company database on SQLite.

conn = sqlite3.connect("customer.db") 

#Create a cursor
c = conn.cursor()

#Query the Database
c.execute("SELECT * FROM customers")


#print(c.fetchone()[2]) -> This'll fetch the first item of the table and you can bring a specific record from the tuple.
#print(c.fetchmany(3))-> This'll fetch the number that we want.
print(c.fetchall()) #-> This'll fetch all.

items = c.fetchall()

print("NAME " + "        \t\tEMAIL")
print("------" + "         \t\t-----")

for item in items:
    print(item[0]) #-> you can print only the first valeu of any row.
    print(item[0] + " " + item[1] + "\t\t" + item[2])

#Commit our command
conn.commit()

#Close our connection
conn.close()