import pyodbc


# Database management class
class DBM:
    # connect to server
    def __init__(self):
        server = 'sql5110.site4now.net,1433'
        database = 'db_a998ac_bdbserver001'
        username = 'db_a998ac_bdbserver001_admin'
        password = 'databaseproj123'
        self.cursor = None
        self.db = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';ENCRYPT=no;UID=' + username + ';PWD=' + password)

    def sendQuery(self, sqlQuery):
        self.cursor = self.db.cursor()
        self.cursor.execute(sqlQuery)

        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    # destructor
    def __del__(self):
        self.db.close()
