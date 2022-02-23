import sqlite3

#conn = sqlite3.connect(":memory:") -> This will create a database on memory.
#Creating a company database on SQLite.

conn = sqlite3.connect("customer.db") 

#Create a cursor
c = conn.cursor()

#Create a table
c.execute("""CREATE TABLE customers(
        first_name text,
        last_name text,
        email text
    )""")

# *data types*
#NULL: does exits or not exits. (not NULL or NULL) 
#INTEGER: numbers.
#REAL: decimal numbers.
#TEXT: literal text.
#BLOB: images, mp3 files and etc.

#Commit our command
conn.commit()

#Close our connection
conn.close()