from Views.BankUser import *


class Customer(BankUser):
    def __init__(self, name, ssn, password):
        super().__init__(name, ssn, password)
        self.db = DB()

    def validateCustomer(self):
        c = self.db.cursor
        query = "SELECT * FROM dbo.Customer WHERE SSN=? AND CustomerPassword=?;"
        c.execute(query, (self.ssn, self.password))
        row = c.fetchone()
        if row is not None:
            print("Customer Found:")
            self.name = row[0]
            self.bankCode = row[5]
            return True
        else:
            print("Customer not found !")
            return False;

    def requestLoan(self, loanTypeID, amount):
        query = "INSERT INTO dbo.Loan ( Balance, LoanTypeID, CustomerSSN,EmployeeSSN, LoanStatus, PaidBalance) VALUES ( ?, ?, ?,NULL, 'REQ', 0 );"
        params = ( amount, loanTypeID, self.ssn)
        self.db.sendQueryParams(query, params)

    def startLoan(self, loanNumber):
        query = "UPDATE Loan SET LoanStatus = 'ACT'where id = ? AND LoanStatus = 'NACT';"
        self.db.sendQueryParams(query, loanNumber)


# cus =  Customer("Kareem", "54", "123", "CIB")
#
# cus.startLoan('16')