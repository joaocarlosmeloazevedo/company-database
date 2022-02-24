import sqlite3

#conn = sqlite3.connect(":memory:") -> This will create a database on memory.
#Creating a company database on SQLite.

conn = sqlite3.connect("customer.db") 

#Create a cursor
c = conn.cursor()

#Query The Database - AND/OR
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()
pk = 1
for item in items:
    while pk < 6:
        print("We're in the ",pk,"º Column:")
        updt_firstname = input("Type the First Name.\n")
        c.execute(f"UPDATE customers SET first_name =? WHERE rowid =?",
                  (updt_firstname,pk))
        pk += 1
    print(item)

pk = 1
for item in items:
    while pk < 6:
        print("We're in the ", pk, "º Column:")
        updt_lastname = input("Type the Last Name.\n")
        c.execute(f"UPDATE customers SET last_name=? WHERE rowid =?",
                  (updt_lastname, pk))
        pk += 1
    print(item)

pk = 1
for item in items:
    while pk < 6:
        print("We're in the ", pk, "º Column:")
        updt_email = input("Type the E-mail.")
        c.execute(f"UPDATE customers SET email =? WHERE rowid =?",
                  (updt_email, pk))

        pk += 1
    print(item)

for item in items:
    print(item)

#Commit our command
conn.commit()

#Close our connection
conn.close()