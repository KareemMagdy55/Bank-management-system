import pyodbc


#
# server = 'sql5110.site4now.net,1433'
# database = 'db_a998ac_bdbserver001'
# username = 'db_a998ac_bdbserver001_admin'
# password = 'databaseproj123'
class DB:
    def __init__(self):
        try:

            self.connection = pyodbc.connect(
                'Driver={SQL Server};'
                'Server=sql5110.site4now.net,1433;'
                'Database=db_a998ac_bdbserver001;'
                'UID=db_a998ac_bdbserver001_admin;'
                'PWD=databaseproj123;'
            )
            self.cursor = self.connection.cursor()
            print("Connected to the database successfully!")
            print("=========================================")
        except pyodbc.Error as e:
            print(f"Error occurred while connecting to the database: {e}")
            print("=========================================")

    def sendQuery(self, sqlQuery):
        try:
            cursor = self.cursor.execute(sqlQuery)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("=========================================")
        except pyodbc.Error as e:
            print(f"Error occurred while executing the query: {e}")
            print("=========================================")

    def sendQueryParams(self, sqlQuery, params):
        self.cursor.execute(sqlQuery, params)
        self.connection.commit()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        print("Connection closed successfully!")
        print("=========================================")
