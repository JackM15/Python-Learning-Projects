#import sqlite3
import sqlite3

#first connect to the database, give it a name to create the file
conn = sqlite3.connect("lite.db")

#create a cursor object (selects stuff in database)
cur=conn.cursor()

#insert your sql code, always goes inside quotes, its always a string!
#sql is usually caps!
#use the cursor to execute the sql code, in the example below we are creating a table called "store" as we are making a store (IF IT DOESNT EXIST!)
#then the store table has columns for items which use text (strings in python)
#quantity column always takes integers and the price takes REAL (floats in python)
cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")

#then add some data to the table :D
cur.execute("INSERT INTO store VALUES ('Wine Glass', 8, 10.5)")

#then we commit the changes to the database
conn.commit()

#then we close the connection
conn.close()
