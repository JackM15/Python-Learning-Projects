#import sqlite3
import sqlite3

#create a table
def create_table():
    #first connect to the database, give it a name to create the file
    conn = sqlite3.connect("lite.db")
    #create a cursor object (selects stuff in database)
    cur=conn.cursor()
    #insert your sql code
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    #then we commit the changes to the database
    conn.commit()
    #then we close the connection
    conn.close()

#insert data
def insert(item, quantity, price):
    #connect to the database
    conn = sqlite3.connect("lite.db")
    #set the cursor up
    cur = conn.cursor()
    #then add some data to the table using ? as placeholders for security then the parameters/argument names to fill in the ? data
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    #comit the data to the database table
    conn.commit()
    #close the connection to the database
    conn.close()

#lets view our database
def viewresults():
    #first connect to the database
    conn = sqlite3.connect("lite.db")
    #create a cursor
    cur = conn.cursor()
    #select everything in the store database table (* selects all)
    cur.execute("SELECT * FROM store")
    #fetch the data and store in a variable
    rows = cur.fetchall()
    #close the connection
    conn.close()
    #return the rows variable
    return rows

#print the rows variable list (viewresults function) on seperate lines
def printresults():
    counter = 0
    for item in viewresults():
        print("Row {}: ".format(counter) + str(item) )
        counter+=1

#execute the results printing function
printresults()
