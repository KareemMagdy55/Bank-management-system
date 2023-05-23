from Views.BankUser import *


class Employee(BankUser):
    def __init__(self, name, ssn, password, bankCode, branchCode):
        super().__init__(name, ssn, password, bankCode)
        self.branchCode = branchCode
        self.db = DB()
        self.validateEmployee()

    def validateEmployee(self):
        c = self.db.cursor
        query = "SELECT * FROM Employee WHERE EmployeeName=? AND SSN=? AND EmployeePassword=? AND BankCode =? AND BranchCode = ? AND AccessLevel = '1';"
        c.execute(query, (self.name, self.ssn, self.password, self.bankCode, self.branchCode))
        row = c.fetchone()
        if row is not None:
            print("Employee Found")
        else:
            print("Employee not found !")

    def signUpCustomer(self, cname, ssn, address, phone, password):
        query = "INSERT INTO Customer (CustomerName, SSN, CustomerAddress, Phone, CustomerPassword, BankCode, BranchCode) VALUES (?, ?, ?, ?, ?, ?, ?);"
        params = (cname, ssn, address, phone, password, self.bankCode, self.branchCode)
        self.db.sendQueryParams(query, params)

    def updateCustomer(self, ossn, cname, ssn, address, phone, password, bankCode, branchCode):
        query = "UPDATE Customer SET CustomerName = ?, SSN = ?, CustomerAddress = ?, Phone = ?, CustomerPassword = ?, BankCode = ?, BranchCode = ? WHERE SSN = ?;"
        params = (cname, ssn, address, phone, password, bankCode, branchCode, ossn)
        self.db.sendQuery(query, params)

    def updateLoan(self, loanNumber, loanStatus):
        query = " UPDATE Loan SET LoanStatus = ?, EmployeeSSN = ?where LoanType = ?;"
        params = (loanStatus, self.ssn, loanNumber)
        self.db.sendQueryParams(query, params)

    def showLoansDetails(self):
        self.db.sendQuery('''SELECT DISTINCT Employee.EmployeeName AS EmployeeName, Customer.CustomerName AS CustomerName, LoanType.LoanType AS LoanType, Loan.*
FROM Employee
JOIN Loan ON Employee.SSN = Loan.EmployeeSSN
JOIN Customer ON Loan.CustomerSSN = Customer.SSN
JOIN LoanType ON Loan.LoanTypeID = LoanType.LoanTypeID;''')

    def showLoansType(self):
        self.db.sendQuery("SELECT LoanType FROM dbo.LoanType;")

    def showCustomers(self):
        self.db.sendQuery("SELECT * FROM dbo.Customer;")


