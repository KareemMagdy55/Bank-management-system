from DBMS.handleDB import DBM

# Create an instance of the DBM class
tempDB = DBM()

# Send a query
tempDB.sendQuery("SELECT * FROM dbo.Bank;")
