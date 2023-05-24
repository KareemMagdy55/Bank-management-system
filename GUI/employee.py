import customer
import customtkinter as tk
from tkinter import messagebox
# import module in ../Views/Employee.py
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Views.Employee import *
import admin

global empObj

def updateLoansPage(root, frame):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)
    # Add Header
    updateLoanLabel = tk.CTkLabel(frame, text="Update Loan", font=("Arial", 30))
    updateLoanLabel.grid(row=0, column=0, pady=10, padx=10)
    # Search for loan
    loanIDLabel = tk.CTkLabel(frame, text="Loan ID")
    loanIDLabel.grid(row=1, column=0, pady=2, padx=10)
    loanIDEntry = tk.CTkEntry(frame)
    loanIDEntry.grid(row=1, column=1, pady=2, padx=10)

    def searchLoan(root, frame):
        loanID = loanIDEntry.get()
        loanDetails = empObj.db.sendQuery(f"SELECT * FROM Loan WHERE id = {loanID}")
        if len(loanDetails) == 0:
            messagebox.showerror("Loan Search", "Loan not found")
            return
        loanBal = loanDetails[0][0]
        loanStatus = loanDetails[0][1]
        loanEmpSSN = loanDetails[0][2]
        loanCustSSN = loanDetails[0][3]
        loanPaidBal = loanDetails[0][4]
        if loanPaidBal == None:
            loanPaidBal = 0
        loanTypeID = loanDetails[0][6]

        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)

        # Add Header
        titleLabel = tk.CTkLabel(frame, text="Update Loan", font=("Arial", 30))
        titleLabel.grid(row=0, column=0, pady=10, padx=10)

        # Add Labels and Entry Boxes
        loanCustSSNLabel = tk.CTkLabel(frame, text="Customer SSN")
        loanCustSSNLabel.grid(row=1, column=0, pady=2, padx=10)
        loanCustSSNEntry = tk.CTkEntry(frame)
        loanCustSSNEntry.grid(row=1, column=1, pady=2, padx=10)
        loanCustSSNEntry.insert(0, loanCustSSN)
        loanCustSSNEntry.configure(state="disabled")

        loanEmpSSNLabel = tk.CTkLabel(frame, text="Employee SSN")
        loanEmpSSNLabel.grid(row=2, column=0, pady=2, padx=10)
        loanEmpSSNEntry = tk.CTkEntry(frame)
        loanEmpSSNEntry.grid(row=2, column=1, pady=2, padx=10)
        loanEmpSSNEntry.insert(0, loanEmpSSN)
        loanEmpSSNEntry.configure(state="disabled")

        loanIDLabel = tk.CTkLabel(frame, text="Loan ID")
        loanIDLabel.grid(row=3, column=0, pady=2, padx=10)
        loanIDEntryfield = tk.CTkEntry(frame)
        loanIDEntryfield.grid(row=3, column=1, pady=2, padx=10)
        loanIDEntryfield.insert(0, loanID)
        loanIDEntryfield.configure(state="disabled")
        # Get loan type name from loan type id
        loanTypes_raw = empObj.showLoansType()
        loanTypes = []
        for loan in loanTypes_raw:
            loanTypes.append(loan[0])
        
        loanTypeLabel = tk.CTkLabel(frame, text="Loan Type")
        loanTypeLabel.grid(row=4, column=0, pady=2, padx=10)
        loanTypeMenu = tk.CTkOptionMenu(frame, values = loanTypes, state="disabled")
        loanTypeMenu.grid(row=4, column=1, pady=2, padx=10)
        loanTypeMenu.set(loanTypes[loanTypeID-1])

        loanBalLabel = tk.CTkLabel(frame, text="Loan Balance")
        loanBalLabel.grid(row=5, column=0, pady=2, padx=10)
        loanBalEntry = tk.CTkEntry(frame)
        loanBalEntry.grid(row=5, column=1, pady=2, padx=10)
        loanBalEntry.insert(0, loanBal)
        loanBalEntry.configure(state="disabled")

        loanPaidBalLabel = tk.CTkLabel(frame, text="Paid Balance")
        loanPaidBalLabel.grid(row=6, column=0, pady=2, padx=10)
        loanPaidBalEntry = tk.CTkEntry(frame)
        loanPaidBalEntry.grid(row=6, column=1, pady=2, padx=10)
        loanPaidBalEntry.insert(0, loanPaidBal)
        loanPaidBalEntry.configure(state="disabled")

        loanStatusLabel = tk.CTkLabel(frame, text="Loan Status")
        loanStatusLabel.grid(row=7, column=0, pady=2, padx=10)
        loanStatusList = ["ACT", "NACT", "REQ", "REJ"]
        loanStatusMenu = tk.CTkOptionMenu(frame, values = loanStatusList)
        loanStatusMenu.grid(row=7, column=1, pady=2, padx=10)
        loanStatusMenu.set(loanStatus)

        # Function to handle the 'Update' button click
        def updateLoan(root, frame):
            
            loanStatus = loanStatusMenu.get()
            loanID = loanIDEntryfield.get()
            if not loanID.isdigit():
                messagebox.showerror("Loan Search", "Invalid Loan ID")
                return
            empObj.updateLoan(loanID, loanStatus)
            messagebox.showinfo("Loan Update", "Loan updated successfully")
            console(root, frame)
        
        # Add Update Button
        updateButton = tk.CTkButton(frame, text="Update", command=lambda:updateLoan(root, frame))
        updateButton.grid(row=8, column=0, pady=10, padx=10, columnspan=2, sticky="EW")
        backButton = tk.CTkButton(frame, text="Back", command=lambda:console(root, frame))
        backButton.grid(row=9, column=0, pady=10, padx=10, columnspan=2, sticky="EW")

    searchbtn = tk.CTkButton(frame, text="Search", command=lambda:searchLoan(root, frame))
    searchbtn.grid(row=2, column=0, pady=10, padx=10, columnspan=2, sticky="EW")
    
    backButton = tk.CTkButton(frame, text="Back", command=lambda:console(root, frame))
    backButton.grid(row=3, column=0, pady=10, padx=10, columnspan=2, sticky="EW")

def loansPage(root, frame):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)
    
    def show_loans(root, frame):
        rows = empObj.showLoansDetails()
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)
        # Add Header
        showLoans = tk.CTkLabel(frame, text="All Loans", font=("Arial", 30))
        showLoans.pack(anchor=tk.CENTER, pady=10)
        rows.insert(0, ['EmployeeName', 'Customer Name', 'Loan Type', 'Balance', 'Status', 'EmployeeSSN', 'CustomerSSN', 'PaidBalance', 'Loan ID', 'LoanTypeID'])
        height = len(rows)
        width = len(rows[0])
        loanFrame = tk.CTkScrollableFrame(frame,width=920)
        loanFrame.pack(pady=10)
        for i in range(height): #Rows
            for j in range(width): #Columns
                b = tk.CTkLabel(loanFrame, text=rows[i][j])
                b.grid(row=i, column=j,padx=10, pady=10)
        # Add Back Button
        backButton = tk.CTkButton(frame, text="Back", command=lambda:console(root, frame))
        backButton.pack(anchor=tk.CENTER, pady=10)

    def show_loans_type(root, frame):
        rows = empObj.showLoansType()
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)
        # Add Header
        showLoans = tk.CTkLabel(frame, text="All Loan Types", font=("Arial", 30))
        showLoans.pack(anchor=tk.CENTER, pady=10)
        rows.insert(0, ['Loan Type Name'])
        height = len(rows)
        width = len(rows[0])
        loanFrame = tk.CTkScrollableFrame(frame,width=150)
        loanFrame.pack(pady=10)
        for i in range(height):
            for j in range(width):
                b = tk.CTkLabel(loanFrame, text=rows[i][j])
                b.grid(row=i, column=j,padx=10, pady=10)
        # Add Back Button
        backButton = tk.CTkButton(frame, text="Back", command=lambda:console(root, frame))
        backButton.pack(anchor=tk.CENTER, pady=10)

    updateLoans = tk.CTkButton(frame, text="Update Loans", command=lambda:updateLoansPage(root, frame))        
    updateLoans.pack(anchor=tk.CENTER, pady=10)

    showLoans = tk.CTkButton(frame, text="Show Loans", command=lambda:show_loans(root, frame))
    showLoans.pack(anchor=tk.CENTER, pady=10)

    showLoansType = tk.CTkButton(frame, text="Show Loan Types", command=lambda:show_loans_type(root, frame))
    showLoansType.pack(anchor=tk.CENTER, pady=10)

def customerPage(root, frame):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)
    # Welcome message
    empName = empObj.name;
    label = tk.CTkLabel(frame, text="Welcome, " + empName, font=("Arial", 20))
    label.pack(anchor=tk.CENTER, pady=10, padx=10)

    def addCustomer(root, frame):
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)

        # Fields for CustomerName, SSN, CustomerAddress, Phone, CustomerPassword, BankCode, BranchCode
        nameLabel = tk.CTkLabel(frame, text="Customer Name")
        nameLabel.grid(row=0, column=0, padx=10, pady=2)
        customerNameField = tk.CTkEntry(frame)
        customerNameField.grid(row=1, column=0, padx=10, pady=2)

        ssnLabel = tk.CTkLabel(frame, text="SSN")
        ssnLabel.grid(row=4, column=0, padx=10, pady=2)
        ssnField = tk.CTkEntry(frame)
        ssnField.grid(row=5, column=0, padx=10, pady=2)

        customerAddressLabel = tk.CTkLabel(frame, text="Customer Address")
        customerAddressLabel.grid(row=0, column=1, padx=10, pady=2)
        customerAddressField = tk.CTkEntry(frame)
        customerAddressField.grid(row=1, column=1, padx=10, pady=2)

        phoneLabel = tk.CTkLabel(frame, text="Phone")
        phoneLabel.grid(row=2, column=0, padx=10, pady=2, columnspan=2)
        phoneField = tk.CTkEntry(frame)
        phoneField.grid(row=3, column=0, padx=10, pady=2, columnspan=2)

        customerPasswordLabel = tk.CTkLabel(frame, text="Customer Password")
        customerPasswordLabel.grid(row=4, column=1, padx=10, pady=2)
        customerPasswordField = tk.CTkEntry(frame)
        customerPasswordField.grid(row=5, column=1, padx=10, pady=2)


        selbanklabel = tk.CTkLabel(frame, text="Select Bank")
        selbanklabel.grid(row=6, column=0, padx=10, pady=2)
        banks = [empObj.bankCode]
        bankMenu = tk.CTkOptionMenu(frame, values = banks)
        bankMenu.grid(row=7, column=0, padx=10, pady=2)
        bankMenu.set(empObj.bankCode)
        bankMenu.configure(state="disabled")
        
       

        branches = [empObj.branchCode]
        selbranchlabel = tk.CTkLabel(frame, text="Select Branch")
        selbranchlabel.grid(row=6, column=1, padx=10, pady=2)

        selectbranch = tk.CTkOptionMenu(frame,values=branches, state="normal")
        selectbranch.set(branches[0])
        selectbranch.grid(row=7, column=1, padx=10, pady=2)
        selectbranch.configure(state="disabled")
        
         # Button to finalize signup
        def finalizeSignup():
            #CustomerName, SSN, CustomerAddress, Phone, CustomerPassword, BankCode, BranchCode
            name = customerNameField.get()
            if name == "":
                messagebox.showerror("Customer Signup", "Customer name cannot be empty")
                return
            ssn = ssnField.get()
            if len(ssn) != 9 or not ssn.isdigit():
                messagebox.showerror("Customer Signup", "SSN must be 9 digits long")
                return
            password = customerPasswordField.get()
            if password == "":
                messagebox.showerror("Customer Signup", "Customer password cannot be empty")
                return
            phone = phoneField.get()
            if len(phone) != 10 or not phone.isdigit():
                messagebox.showerror("Customer Signup", "Phone must be 10 digits long")
                return
            address = customerAddressField.get()
            if address == "":
                messagebox.showerror("Customer Signup", "Customer address cannot be empty")
                return
            empObj.signUpCustomer(name, ssn, address, phone, password)
            messagebox.showinfo("Customer Signup", "Customer signed up successfully")
            console(root, frame)
        finalizeSignupButton = tk.CTkButton(frame, text="Finalize Signup", command=finalizeSignup)
        finalizeSignupButton.grid(row=8, column=0, columnspan=2, pady=10, sticky ="EW")
        BackButton = tk.CTkButton(frame, text="Back", command=lambda:console(root, frame))
        BackButton.grid(row=9, column=0, columnspan=2, pady=10, sticky ="EW")


    # Add Customer Button
    addCustomerButton = tk.CTkButton(frame, text="Add Customer", command=lambda:addCustomer(root, frame))
    addCustomerButton.pack(anchor=tk.CENTER, pady=10)

    def updateCustomer(root, frame):

        def updateCustomerInfo(root, frame, custssn):
            custrow = empObj.db.sendQuery("SELECT * FROM Customer WHERE SSN = '" + custssn + "';")
            if len(custrow) == 0:
                messagebox.showerror("Customer Update", "Customer not found")
                return
            custname = custrow[0][0]
            custaddress = custrow[0][2]
            custphone = custrow[0][3]
            custpassword = custrow[0][4]
            custbankcode = custrow[0][5]
            custbranchcode = custrow[0][6]

            frame.destroy()
            frame = tk.CTkFrame(root)
            frame.pack(expand=True)
            
            # Fields for CustomerName, SSN, CustomerAddress, Phone, CustomerPassword, BankCode, BranchCode
            nameLabel = tk.CTkLabel(frame, text="Customer Name")
            nameLabel.pack(anchor=tk.CENTER)
            customerNameField = tk.CTkEntry(frame)
            customerNameField.insert(0, custname)
            customerNameField.pack(anchor=tk.CENTER)

            ssnLabel = tk.CTkLabel(frame, text="SSN")
            ssnLabel.pack(anchor=tk.CENTER)
            ssnField = tk.CTkEntry(frame)
            ssnField.insert(0, custssn)
            ssnField.pack(anchor=tk.CENTER)

            customerAddressLabel = tk.CTkLabel(frame, text="Customer Address")
            customerAddressLabel.pack(anchor=tk.CENTER)
            customerAddressField = tk.CTkEntry(frame)
            customerAddressField.insert(0, custaddress)
            customerAddressField.pack(anchor=tk.CENTER)

            phoneLabel = tk.CTkLabel(frame, text="Phone")
            phoneLabel.pack(anchor=tk.CENTER)
            phoneField = tk.CTkEntry(frame)
            phoneField.insert(0, custphone)
            phoneField.pack(anchor=tk.CENTER)

            customerPasswordLabel = tk.CTkLabel(frame, text="Customer Password")
            customerPasswordLabel.pack(anchor=tk.CENTER)
            customerPasswordField = tk.CTkEntry(frame)
            customerPasswordField.insert(0, custpassword)
            customerPasswordField.pack(anchor=tk.CENTER)

            def setBranches(bank):
                branches_raw = empObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + bank + "';")
                branches = []
                for branch in branches_raw:
                    branches.append(branch[0])
                if len(branches) == 0:
                    branches.append("No Branches")
                    selectbranch.configure(values=branches, state="disabled")
                    selectbranch.set("No Branches")
                else:
                    selectbranch.configure(values=branches, state="normal")
                    selectbranch.set(custbranchcode)

            # Banks Menu
            banks_raw = empObj.db.sendQuery("SELECT Code FROM Bank")
            banks = []
            for bank in banks_raw:
                banks.append(bank[0])
            selbanklabel = tk.CTkLabel(frame, text="Select Bank")
            selbanklabel.pack(anchor=tk.CENTER, pady=10)
            selectbank = tk.CTkOptionMenu(frame,values= banks,command=setBranches)
            selectbank.pack(anchor=tk.CENTER, pady=10)
            selectbank.set(custbankcode)
            
            # Branches Menu
            branches_raw = empObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + selectbank.get() + "';")
            branches = []
            for branch in branches_raw:
                branches.append(branch[0])
            selbranchlabel = tk.CTkLabel(frame, text="Select Branch")
            selbranchlabel.pack(anchor=tk.CENTER, pady=10)

            if len(branches) == 0:
                branches.append("No Branches")
                selectbranch = tk.CTkOptionMenu(frame,values=branches, state="disabled")
                selectbranch.set("No Branches")
            else:
                selectbranch = tk.CTkOptionMenu(frame,values=branches, state="normal")
                selectbranch.set(custbranchcode)
            selectbranch.pack(anchor=tk.CENTER, pady=10)
            
            # Button to finalize signup
            def finalizeUpdate():
                #CustomerName, SSN, CustomerAddress, Phone, CustomerPassword, BankCode, BranchCode
                name = customerNameField.get()
                ssn = ssnField.get()
                password = customerPasswordField.get()
                phone = phoneField.get()
                address = customerAddressField.get()
                bank = selectbank.get()
                branch = selectbranch.get()

                empObj.updateCustomer(ssn, name, ssn, address, phone, password, bank, branch)
                messagebox.showinfo("Customer Signup", "Customer signed up successfully")
                console(root, frame)
            finalizeUpdateButton = tk.CTkButton(frame, text="Finalize Signup", command=finalizeUpdate)
            finalizeUpdateButton.pack(anchor=tk.CENTER, pady=10)
            BackButton = tk.CTkButton(frame, text="Back", command=lambda:console(root, frame))
            BackButton.pack(anchor=tk.CENTER, pady=10)
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)

        idField = tk.CTkEntry(frame, placeholder_text="SSN")
        idField.pack(anchor=tk.CENTER, pady=10)
        updateCustbtn = tk.CTkButton(frame, text="Update Customer", command=lambda:updateCustomerInfo(root, frame, idField.get()))
        updateCustbtn.pack(anchor=tk.CENTER, pady=10)
        BackButton = tk.CTkButton(frame, text="Back", command=lambda:console(root, frame))
        BackButton.pack(anchor=tk.CENTER, pady=10)
    # Update Customer Button
    updateCustomerButton = tk.CTkButton(frame, text="Update Customer", command=lambda:updateCustomer(root, frame))
    updateCustomerButton.pack(anchor=tk.CENTER, pady=10)

    def showCustomer(root, frame):
        rows = empObj.showCustomers()
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)
        # Add Header
        showCustomers = tk.CTkLabel(frame, text="All Customers", font=("Arial", 30))
        showCustomers.pack(anchor=tk.CENTER, pady=10)
        rows.insert(0, ['Name', 'SSN', 'Address', 'Phone', 'Password', 'BankCode', 'BranchCode'])
        height = len(rows)
        width = len(rows[0])
        custFrame = tk.CTkScrollableFrame(frame, width=650)
        custFrame.pack(anchor=tk.CENTER, pady=10)
        for i in range(height): #Rows
            for j in range(width): #Columns
                b = tk.CTkLabel(custFrame, text=rows[i][j])
                b.grid(row=i, column=j,padx=10, pady=10)
        # Add Back Button
        backButton = tk.CTkButton(frame, text="Back", command=lambda:console(root, frame))
        backButton.pack(anchor=tk.CENTER, pady=10)

    # Show Customer Button
    showCustomerButton = tk.CTkButton(frame, text="Show All Customers", command=lambda:showCustomer(root, frame))
    showCustomerButton.pack(anchor=tk.CENTER, pady=10)


    # Back Button
    backButton = tk.CTkButton(frame, text="Back", command=lambda:console(root, frame))
    backButton.pack(anchor=tk.CENTER, pady=10)


def console(root, frame):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)
    # Welcome message
    empName = empObj.name;
    label = tk.CTkLabel(frame, text="Welcome, " + empName, font=("Arial", 20))
    label.pack(anchor=tk.CENTER, pady=10, padx=10)

    # Loan operations button
    loanButton = tk.CTkButton(frame, text="Loan Operations", command=lambda:loansPage(root, frame))
    loanButton.pack(anchor=tk.CENTER, pady=10)

    # Button to go to the customer page
    customerButton = tk.CTkButton(frame, text="Customer Operations", command=lambda:customerPage(root, frame))
    customerButton.pack(anchor=tk.CENTER, pady=10)

    # Button to go back to the previous page
    logoutButton = tk.CTkButton(frame, text="Logout", command=lambda:LoginPage(root, frame))
    logoutButton.pack(anchor=tk.CENTER, pady=10)

def LoginPage(root, frame):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)

    
    # Field to enter employee ID
    empIDField = tk.CTkEntry(frame, placeholder_text="Employee ID")
    empIDField.pack(anchor=tk.CENTER, pady=10)
    # Field to enter employee password
    empPasswordField = tk.CTkEntry(frame, placeholder_text="Password", show="*")
    empPasswordField.pack(anchor=tk.CENTER, pady=10)

    def login(root, frame):
        
        global empObj
        empObj = Employee("",empIDField.get(), empPasswordField.get())
        if empObj.validateEmployee():
            console(root, frame)
        else: 
            messagebox.showerror("Error", "Invalid credentials")
    # Button to login
    loginButton = tk.CTkButton(frame, text="Login", command=lambda:login(root, frame))
    loginButton.pack(anchor=tk.CENTER, pady=10)

