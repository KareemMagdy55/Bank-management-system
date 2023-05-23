# from Views import Admin, Customer, Employee
from Views.Admin import *
# from DBMS.handleDB import *

admin = Admin('kareem', '123', '123')
# db = DB()
# db.sendQuery("SELECT * FROM dbo.Admin;")

admin.showLoansType()
