from Views.BankUser import *


class Admin(BankUser):
    def __init__(self, name, ssn, password):
        super().__init__(name, ssn, password, bankCode=None)
        self.db = DB()

    def signUpCustomer(self, cname, ssn, address, phone, password, bankCode, branchCode):
        query = "INSERT INTO Customer (CustomerName, SSN, CustomerAddress, Phone, CustomerPassword, BankCode, BranchCode) VALUES (?, ?, ?, ?, ?, ?, ?);"
        params = (cname, ssn, address, phone, password, bankCode, branchCode)
        self.db.sendQueryParams(query, params)

    def signUpEmployee(self, ename, ssn, password, accssLvl, bankCode, branchCode):
        query = "INSERT INTO Employee (EmployeeName, SSN, EmployeePassword, AccessLevel, BankCode, BranchCode) VALUES (?, ?, ?, ?, ?, ?);"
        params = (ename, ssn, password, accssLvl, bankCode, branchCode)
        self.db.sendQueryParams(query, params)

    def addBank(self, bankName, bankCode, bankAddress):
        query = "INSERT INTO Bank (BankName, Code, BankAddress) VALUES (?, ?, ?);"
        params = (bankName, bankCode, bankAddress)
        self.db.sendQueryParams(query, params)

    def addBranch(self, branchNum, branchAddress, bankCode):
        query = "INSERT INTO Branch (BranchNumber, BranchAddress, BankCode) VALUES (?, ?, ?);"
        params = (branchNum, branchAddress, bankCode)
        self.db.sendQueryParams(query, params)

    def addAccount(self, accountType, accountNumber, balance, customerSSN, employeeID):
        query = "INSERT INTO Account (AccountType, Number, Balance, CustomerSSN, EmployeeID) VALUES (?, ?, ?, ?, ?);"
        params = (accountType, accountNumber, balance, customerSSN, employeeID)
        self.db.sendQueryParams(query, params)

    def addLoan(self, loanType, loanNumber, balance, loanStatus, employeeSSN, customerSSN):
        query = "INSERT INTO Loan (LoanType, Number, Balance, LoanStatus, EmployeeSSN, CustomerSSN) VALUES (?, ?, ?, ?, ?, ?);"
        params = (loanType, loanNumber, balance, loanStatus, employeeSSN, customerSSN)
        self.db.sendQueryParams(query, params)


    def showLoansDetails(self):
        self.db.sendQuery("SELECT * FROM dbo.Loan;")


    def showLoansType(self):
        self.db.sendQuery("SELECT LoanType FROM dbo.Loan;")

    def showCustomers(self):
        self.db.sendQuery("SELECT * FROM dbo.Customer;")

    def showEmployees(self):
        self.db.sendQuery("SELECT * FROM dbo.Employee;")



