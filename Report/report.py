from DBMS.handleDB import DB

db = DB()


def get_table_counts():
    table_names = ['Bank', 'Branch', 'Account', 'Admin', 'Customer', 'Employee', 'Loan', 'LoanType']
    table_counts = {}
    for table_name in table_names:
        db.cursor.execute(f'SELECT COUNT(*) FROM {table_name}')
        count = db.cursor.fetchone()[0]
        table_counts[table_name] = f"Number of {table_name}s: {count}"
    return table_counts


def get_most_used_loan_type():
    db.cursor.execute('SELECT TOP 1 LoanType, COUNT(*) AS LoanCount FROM LoanType '
                      'INNER JOIN Loan ON LoanType.LoanTypeID = Loan.LoanTypeID '
                      'GROUP BY LoanType ORDER BY LoanCount DESC')
    result = db.cursor.fetchone()
    loan_type = result.LoanType
    loan_count = result.LoanCount
    return f"The most used loan type: '{loan_type}' ({loan_count} loans)"


def get_bank_with_most_customers():
    db.cursor.execute(
        "SELECT TOP 1 BankName, BranchNumber, COUNT(*) AS CustomerCount FROM Bank "
        "INNER JOIN Branch ON Bank.Code = Branch.BankCode "
        "INNER JOIN Customer ON Branch.BranchNumber = Customer.BranchCode "
        "GROUP BY BankName, BranchNumber ORDER BY CustomerCount DESC")
    result = db.cursor.fetchone()
    bank_name = result[0]
    branch_number = result[1]
    customer_count = result[2]
    return f"The bank with the most customers: {bank_name} (Branch Number: {branch_number}) with {customer_count} customers"


def get_bank_with_least_customers():
    db.cursor.execute(
        "SELECT TOP 1 BankName, BranchNumber, COUNT(*) AS CustomerCount FROM Bank "
        "INNER JOIN Branch ON Bank.Code = Branch.BankCode "
        "INNER JOIN Customer ON Branch.BranchNumber = Customer.BranchCode "
        "GROUP BY BankName, BranchNumber ORDER BY CustomerCount ASC")
    result = db.cursor.fetchone()
    bank_name = result[0]
    branch_number = result[1]
    customer_count = result[2]
    return f"The bank with the least customers: {bank_name} (Branch Number: {branch_number}) with {customer_count} customers"


def get_account_types_counts():
    db.cursor.execute(
        'SELECT AccountType, COUNT(*) AS AccountCount FROM Account GROUP BY AccountType ORDER BY AccountCount DESC')
    results = db.cursor.fetchall()
    account_types_counts = []
    for result in results:
        account_type = result[0]
        account_count = result[1]
        account_types_counts.append(f"{account_type} Count: {account_count}")
    return account_types_counts


def get_average_loan_balance():
    db.cursor.execute('SELECT AVG(Balance) AS AverageBalance FROM Loan')
    result = db.cursor.fetchone()
    average_balance = result[0]
    return f"The average balance of loans: {average_balance}"


def get_bank_with_min_loan_balance():
    db.cursor.execute('SELECT BankName, MIN(Balance) AS MinBalance FROM Loan, Bank '
                      'WHERE Loan.BankCode = Bank.Code GROUP BY BankName')
    result = db.cursor.fetchone()
    bank_name = result[0]
    min_balance = result[1]
    return f"The bank with the minimum loans balance: {bank_name} with a balance of {min_balance}"


def get_bank_with_max_loan_balance():
    db.cursor.execute('SELECT BankName, MAX(Balance) AS MaxBalance FROM Loan, Bank '
                      'WHERE Loan.BankCode = Bank.Code GROUP BY BankName')
    result = db.cursor.fetchone()
    bank_name = result[0]
    max_balance = result[1]
    return f"The bank with the maximum loans balance: {bank_name} with a balance of {max_balance}"


def get_bank_with_highest_employees():
    db.cursor.execute('SELECT BankName, COUNT(*) AS nEmps FROM Bank '
                      'INNER JOIN Employee ON Bank.Code = Employee.BankCode '
                      'GROUP BY BankName ORDER BY nEmps DESC')
    result = db.cursor.fetchone()
    bank_name = result[0]
    employee_count = result[1]
    return f"The bank with the highest number of employees: {bank_name} with {employee_count} employees"


def get_bank_with_lowest_employees():
    db.cursor.execute('SELECT BankName, COUNT(*) AS nEmps FROM Bank '
                      'INNER JOIN Employee ON Bank.Code = Employee.BankCode '
                      'GROUP BY BankName ORDER BY nEmps ASC')
    result = db.cursor.fetchone()
    bank_name = result[0]
    employee_count = result[1]
    return f"The bank with the lowest number of employees: {bank_name} with {employee_count} employees"


def get_banks_total_loans():
    db.cursor.execute('SELECT SUM(Balance) AS totalLoans FROM Loan;')

    result = db.cursor.fetchone()

    totalLoans = result[0]

    return (f"Total loans balance of all banks is: {totalLoans}")


