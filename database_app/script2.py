import psycopg2

#Interacting with a database:
#1. Connect to a databse
#2. Create a cursor object
#3. Write an SQL query
#4. Commit changes to the db
#5. Close db connection

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'") #1
    cur=conn.cursor() #2
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #3
    conn.commit() #4
    conn.close() #5

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'") #1
    cur=conn.cursor() #2
    #cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item,quantity,price)) #3 vulnerable a sql injections
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
    conn.commit() #4
    conn.close() #5


def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item)) 
    conn.commit()
    conn.close()

#create_table()    
#delete("Orange")
#insert("Coffee Cup",10,5)
#update(11,6,"Water Glass")
update(20,15.0,"Apple")
print(view())