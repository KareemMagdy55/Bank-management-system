from Views.BankUser import *


class Admin(BankUser):
    def __init__(self, name, ssn, password):
        super().__init__(name, ssn, password, bankCode=None)
        self.db = DB()

    def validateAdmin(self):
        c = self.db.cursor
        query = "SELECT * FROM Employee WHERE SSN=? AND EmployeePassword=? AND AccessLevel = 10;"
        c.execute(query, (self.ssn, self.password))
        row = c.fetchone()
        if row is not None:
            print("Admin Found")
            self.name = row[0]
            return True
        else:
            print("Admin not found !")
            return False

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

    def deleteBank(self, bankCode):
        query = "DELETE FROM Bank WHERE Code = ?;"
        params = (bankCode,)
        self.db.sendQueryParams(query, params)

    def deleteBranch(self, branchNum, bankCode):
        query = "DELETE FROM Branch WHERE BranchNumber = ? AND BankCode = ?;"
        params = (branchNum, bankCode)
        self.db.sendQueryParams(query, params)

    def addAccount(self, accountType, accountNumber, balance, customerSSN):
        employeeID = self.ssn
        query = "INSERT INTO Account (AccountType, Number, Balance, CustomerSSN, EmployeeID) VALUES (?, ?, ?, ?, ?);"
        params = (accountType, accountNumber, balance, customerSSN, employeeID)
        self.db.sendQueryParams(query, params)

    def addLoan(self, loanType, balance, loanStatus, employeeSSN, customerSSN):
        query = "INSERT INTO Loan (LoanTypeID, Balance, LoanStatus, EmployeeSSN, CustomerSSN) VALUES (?, ?, ?, ?, ?);"
        params = (loanType, balance, loanStatus, employeeSSN, customerSSN)
        self.db.sendQueryParams(query, params)

    def updateCustomer(self, ossn, cname, ssn, address, phone, password, bankCode, branchCode):
        query = "UPDATE Customer SET CustomerName = ?, SSN = ?, CustomerAddress = ?, Phone = ?, CustomerPassword = ?, BankCode = ?, BranchCode = ? WHERE SSN = ?;"
        params = (cname, ssn, address, phone, password, bankCode, branchCode, ossn)
        self.db.sendQuery(query, params)

    def updateEmployee(self, ossn, ename, ssn, password, accessLevel, bankCode, branchCode):
        query = "UPDATE Employee SET EmployeeName = ?, SSN = ?, EmployeePassword = ?, AccessLevel = ?, BankCode = ?, BranchCode = ? WHERE SSN = ?;"
        params = (ename, ssn, password, accessLevel, bankCode, branchCode, ossn)
        self.db.sendQueryParams(query, params)

    def updateLoan(self, loanNumber, loanStatus):
        query = " UPDATE Loan SET LoanStatus = ?, EmployeeSSN = ? where id = ?;"
        params = (loanStatus, self.ssn, loanNumber)
        self.db.sendQueryParams(query, params)

    def showLoansDetails(self):
        return self.db.sendQuery('''SELECT DISTINCT Employee.EmployeeName AS EmployeeName, Customer.CustomerName AS CustomerName, LoanType.LoanType AS LoanType, Loan.*
                                    FROM Employee
                                    JOIN Loan ON Employee.SSN = Loan.EmployeeSSN
                                    JOIN Customer ON Loan.CustomerSSN = Customer.SSN
                                    JOIN LoanType ON Loan.LoanTypeID = LoanType.LoanTypeID;''')

    def showLoansType(self):
        return self.db.sendQuery("SELECT LoanType FROM dbo.LoanType;")

    def showCustomers(self):
        return self.db.sendQuery("SELECT * FROM dbo.Customer;")

    def showEmployees(self):
        return self.db.sendQuery("SELECT * FROM dbo.Employee;")

Admn = Admin("karson" , "123", "123")
Admn.db.sendQuery("select * from Loan ")
# Admn.updateLoan('18', 'NACT')