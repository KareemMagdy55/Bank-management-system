from Views.BankUser import *


class Customer(BankUser):
    def __init__(self, name, ssn, password, bankCode):
        super().__init__(name, ssn, password, bankCode)
        self.db = DB()
        self.validateCustomer()

    def validateCustomer(self):
        c = self.db.cursor
        query = "SELECT * FROM dbo.Customer WHERE CustomerName=? AND SSN=? AND CustomerPassword=? AND BankCode=?;"
        c.execute(query, (self.name, self.ssn, self.password, self.bankCode))
        row = c.fetchone()
        if row is not None:
            print("Customer Found:")
            return True
        else:
            print("Customer not found !")
            return False;

    def requestLoan(self, loanType, loanTypeID, amount):
        query = "INSERT INTO dbo.Loan ( Balance, LoanTypeID, CustomerSSN,EmployeeSSN, LoanStatus, PaidBalance) VALUES ( ?, ?, ?,NULL, 'REQ', 0 );"
        params = ( amount, loanTypeID, self.ssn)
        self.db.sendQueryParams(query, params)

    def startLoan(self, loanNumber, accountNumber):
        query = "update dbo.Loan set LoanStatus = ? where id = ? AND LoanStatus = 'APR';"
        self.db.sendQueryParams(query, ('START', loanNumber))
        getBalance = "Select Balance, CustomerSSN from dbo.Loan where id = ?;"
        self.db.cursor.execute(getBalance, loanNumber)
        row = self.db.cursor.fetchall()

        balance = row[0]
        cSSN = row[1]

        updateAccBalance = "update dbo.Account set Balance = Balance + ? where CustomerSSN = ? AND Number = ?;"
        self.db.sendQueryParams(updateAccBalance, (balance, cSSN, accountNumber))

    # def startLoan(self):
