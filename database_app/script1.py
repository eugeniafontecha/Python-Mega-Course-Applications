import sqlite3

#Interacting with a database:
#1. Connect to a databse
#2. Create a cursor object
#3. Write an SQL query
#4. Commit changes to the db
#5. Close db connection

def create_table():
    conn=sqlite3.connect("lite.db") #1
    cur=conn.cursor() #2
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #3
    conn.commit() #4
    conn.close() #5

def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db") #1
    cur=conn.cursor() #2
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price)) #3
    conn.commit() #4
    conn.close() #5


def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()
    
#delete("Wine Glass")
#insert("Coffee Cup",10,5)

update(11,6,"Water Glass")
print(view())