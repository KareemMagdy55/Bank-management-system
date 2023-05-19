import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'sql5110.site4now.net,1433' 
database = 'db_a998ac_bdbserver001' 
username = 'db_a998ac_bdbserver001_admin' 
password = 'databaseproj123' 
print("Connecting to server...")
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
print("Connected to server.")
# Sample select query
print ('Reading data from table accounts')
tsql = "SELECT * FROM dbo.Account;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    # Print row
    while row:
        print (str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()
print("Done reading data from table accounts")
