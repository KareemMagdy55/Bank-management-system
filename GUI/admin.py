import customtkinter as tk
import tkinter.messagebox as messagebox
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Views.Admin import *
from employee import displayAllLoans
global adminObj

def adminPage(root, frame):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)
    # Function to handle the 'Sign up' button click
    def sign_up(root, frame):
        def signup_employee(root, frame):
            frame.destroy()
            frame = tk.CTkFrame(root)
            frame.pack(expand=True)
            # Fields for EmployeeName, SSN, EmployeePassword, AccessLevel, BankCode, BranchCode
            employeeIDField = tk.CTkEntry(frame, placeholder_text="Employee ID")
            employeeIDField.pack(anchor=tk.CENTER, pady=10)
            employeeNameField = tk.CTkEntry(frame, placeholder_text="Employee Name")
            employeeNameField.pack(anchor=tk.CENTER, pady=10)
            ssnField = tk.CTkEntry(frame, placeholder_text="SSN")
            ssnField.pack(anchor=tk.CENTER, pady=10)
            employeePasswordField = tk.CTkEntry(frame, placeholder_text="Employee Password")
            employeePasswordField.pack(anchor=tk.CENTER, pady=10)
            accessLevelField = tk.CTkEntry(frame, placeholder_text="Access Level")
            accessLevelField.pack(anchor=tk.CENTER, pady=10)
            

            def setBranches(bank):
                branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + bank + "';")
                branches = []
                for branch in branches_raw:
                    branches.append(branch[0])
                if len(branches) == 0:
                    branches.append("No Branches")
                    selectbranch.configure(values=branches, state="disabled")
                    selectbranch.set("No Branches")
                else:
                    selectbranch.configure(values=branches, state="normal")
                    selectbranch.set(branches[0])

            # Banks Menu
            banks_raw = adminObj.db.sendQuery("SELECT Code FROM Bank")
            banks = []
            for bank in banks_raw:
                banks.append(bank[0])
            selbanklabel = tk.CTkLabel(frame, text="Select Bank")
            selbanklabel.pack(anchor=tk.CENTER, pady=10)
            selectbank = tk.CTkOptionMenu(frame,values= banks,command=setBranches)
            selectbank.pack(anchor=tk.CENTER, pady=10)
            
            # Branches Menu
            branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + selectbank.get() + "';")
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
                selectbranch.set(branches[0])
            selectbranch.pack(anchor=tk.CENTER, pady=10)
            
            # Button to finalize signup
            def finalizeSignup():
                name = employeeNameField.get()
                ssn = ssnField.get()
                password = employeePasswordField.get()
                accessLevel = accessLevelField.get()
                bank = selectbank.get()
                branch = selectbranch.get()
                # ename: Any,
                # sn: Any,
                # assword: Any,
                # ccssLvl: Any,
                # ankCode: Any,
                # ranchCode: Any
                adminObj.signUpEmployee(name, ssn, password, accessLevel, bank, branch)
                messagebox.showinfo("Employee Signup", "Employee signed up successfully")
                adminPage(root, frame)
            finalizeSignupButton = tk.CTkButton(frame, text="Finalize Signup", command=finalizeSignup)
            finalizeSignupButton.pack(anchor=tk.CENTER, pady=10)
        def signup_customer(root, frame):
            frame.destroy()
            frame = tk.CTkFrame(root)
            frame.pack(expand=True)

            # Fields for CustomerName, SSN, CustomerAddress, Phone, CustomerPassword, BankCode, BranchCode
            customerNameField = tk.CTkEntry(frame, placeholder_text="Customer Name")
            customerNameField.pack(anchor=tk.CENTER, pady=10)
            ssnField = tk.CTkEntry(frame, placeholder_text="SSN")
            ssnField.pack(anchor=tk.CENTER, pady=10)
            customerAddressField = tk.CTkEntry(frame, placeholder_text="Customer Address")
            customerAddressField.pack(anchor=tk.CENTER, pady=10)
            phoneField = tk.CTkEntry(frame, placeholder_text="Phone")
            phoneField.pack(anchor=tk.CENTER, pady=10)
            customerPasswordField = tk.CTkEntry(frame, placeholder_text="Customer Password")
            customerPasswordField.pack(anchor=tk.CENTER, pady=10)

            def setBranches(bank):
                branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + bank + "';")
                branches = []
                for branch in branches_raw:
                    branches.append(branch[0])
                if len(branches) == 0:
                    branches.append("No Branches")
                    selectbranch.configure(values=branches, state="disabled")
                    selectbranch.set("No Branches")
                else:
                    selectbranch.configure(values=branches, state="normal")
                    selectbranch.set(branches[0])

            # Banks Menu
            banks_raw = adminObj.db.sendQuery("SELECT Code FROM Bank")
            banks = []
            for bank in banks_raw:
                banks.append(bank[0])
            selbanklabel = tk.CTkLabel(frame, text="Select Bank")
            selbanklabel.pack(anchor=tk.CENTER, pady=10)
            selectbank = tk.CTkOptionMenu(frame,values= banks,command=setBranches)
            selectbank.pack(anchor=tk.CENTER, pady=10)
            
            # Branches Menu
            branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + selectbank.get() + "';")
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
                selectbranch.set(branches[0])
            selectbranch.pack(anchor=tk.CENTER, pady=10)
            
            # Button to finalize signup
            def finalizeSignup():
                #CustomerName, SSN, CustomerAddress, Phone, CustomerPassword, BankCode, BranchCode
                name = customerNameField.get()
                ssn = ssnField.get()
                password = customerPasswordField.get()
                phone = phoneField.get()
                address = customerAddressField.get()
                bank = selectbank.get()
                branch = selectbranch.get()
                # cname: Any,
                # ssn: Any,
                # address: Any,
                # phone: Any,
                # password: Any,
                # bankCode: Any,
                # branchCode: Any
                adminObj.signUpCustomer(name, ssn, address, phone, password, bank, branch)
                messagebox.showinfo("Customer Signup", "Customer signed up successfully")
                adminPage(root, frame)
            finalizeSignupButton = tk.CTkButton(frame, text="Finalize Signup", command=finalizeSignup)
            finalizeSignupButton.pack(anchor=tk.CENTER, pady=10)
            pass
        
        # Page with buttons to add customer, add employee
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)
        # Button to add a customer
        addCustomerButton = tk.CTkButton(frame, text="Add Customer", command=lambda:signup_customer(root, frame))
        addCustomerButton.pack(anchor=tk.CENTER, pady=10)
        # Button to add an employee
        addEmployeeButton = tk.CTkButton(frame, text="Add Employee", command=lambda:signup_employee(root, frame))
        addEmployeeButton.pack(anchor=tk.CENTER, pady=10)
        

    # Function to handle the 'Update user details' button click
    def update_user_details(root,frame):
        def update_Employee(root, frame, empssn):
            emprow = adminObj.db.sendQuery("SELECT * FROM Employee WHERE SSN = '" + empssn + "';")
            empname = emprow[0][0]
            emppassword = emprow[0][2]
            empaccesslevel = emprow[0][3]
            empbankcode = emprow[0][4]
            empbranchcode = emprow[0][5]

            frame.destroy()
            frame = tk.CTkFrame(root)
            frame.pack(expand=True)
            # Fields for EmployeeName, SSN, EmployeePassword, AccessLevel, BankCode, BranchCode
            employeeIDField = tk.CTkEntry(frame, placeholder_text="Employee ID")
            employeeIDField.insert(0, empssn)
            employeeIDField.pack(anchor=tk.CENTER, pady=10)
            employeeNameField = tk.CTkEntry(frame, placeholder_text="Employee Name")
            employeeNameField.insert(0, empname)
            employeeNameField.pack(anchor=tk.CENTER, pady=10)
            ssnField = tk.CTkEntry(frame, placeholder_text="SSN")
            ssnField.insert(0, empssn)
            ssnField.pack(anchor=tk.CENTER, pady=10)
            employeePasswordField = tk.CTkEntry(frame, placeholder_text="Employee Password")
            employeePasswordField.insert(0, emppassword)
            employeePasswordField.pack(anchor=tk.CENTER, pady=10)
            accessLevelField = tk.CTkEntry(frame, placeholder_text="Access Level")
            accessLevelField.insert(0, empaccesslevel)
            accessLevelField.pack(anchor=tk.CENTER, pady=10)
            

            def setBranches(bank):
                branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + bank + "';")
                branches = []
                for branch in branches_raw:
                    branches.append(branch[0])
                if len(branches) == 0:
                    branches.append("No Branches")
                    selectbranch.configure(values=branches, state="disabled")
                    selectbranch.set("No Branches")
                else:
                    selectbranch.configure(values=branches, state="normal")
                    selectbranch.set(empbranchcode)

            # Banks Menu
            banks_raw = adminObj.db.sendQuery("SELECT Code FROM Bank")
            banks = []
            for bank in banks_raw:
                banks.append(bank[0])
            selbanklabel = tk.CTkLabel(frame, text="Select Bank")
            selbanklabel.pack(anchor=tk.CENTER, pady=10)
            selectbank = tk.CTkOptionMenu(frame,values= banks,command=setBranches)
            
            selectbank.pack(anchor=tk.CENTER, pady=10)
            selectbank.set(empbankcode)
            
            # Branches Menu
            branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + selectbank.get() + "';")
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
                selectbranch.set(empbranchcode)
            selectbranch.pack(anchor=tk.CENTER, pady=10)
            
            # Button to finalize signup
            def finalizeSignup():
                name = employeeNameField.get()
                ssn = ssnField.get()
                password = employeePasswordField.get()
                accessLevel = accessLevelField.get()
                bank = selectbank.get()
                branch = selectbranch.get()
    #             ossn: Any,
                    # ename: Any,
                    # ssn: Any,
                    # password: Any,
                    # accessLevel: Any,
                    # bankCode: Any,
                    # branchCode: Any
                adminObj.updateEmployee(ssn, name, password, accessLevel, bank, branch)
                messagebox.showinfo("Employee Update", "Employee updated successfully")
                adminPage(root, frame)
            finalizeSignupButton = tk.CTkButton(frame, text="Finalize Update", command=finalizeSignup)
            finalizeSignupButton.pack(anchor=tk.CENTER, pady=10)
        
        def update_customer(root, frame, custssn):
            custrow = adminObj.db.sendQuery("SELECT * FROM Customer WHERE SSN = '" + custssn + "';")
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
            customerNameField = tk.CTkEntry(frame, placeholder_text="Customer Name")
            customerNameField.insert(0, custname)
            customerNameField.pack(anchor=tk.CENTER, pady=10)
            ssnField = tk.CTkEntry(frame, placeholder_text="SSN")
            ssnField.insert(0, custssn)
            ssnField.pack(anchor=tk.CENTER, pady=10)
            customerAddressField = tk.CTkEntry(frame, placeholder_text="Customer Address")
            customerAddressField.insert(0, custaddress)
            customerAddressField.pack(anchor=tk.CENTER, pady=10)
            phoneField = tk.CTkEntry(frame, placeholder_text="Phone")
            phoneField.insert(0, custphone)
            phoneField.pack(anchor=tk.CENTER, pady=10)
            customerPasswordField = tk.CTkEntry(frame, placeholder_text="Customer Password")
            customerPasswordField.insert(0, custpassword)
            customerPasswordField.pack(anchor=tk.CENTER, pady=10)

            def setBranches(bank):
                branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + bank + "';")
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
            banks_raw = adminObj.db.sendQuery("SELECT Code FROM Bank")
            banks = []
            for bank in banks_raw:
                banks.append(bank[0])
            selbanklabel = tk.CTkLabel(frame, text="Select Bank")
            selbanklabel.pack(anchor=tk.CENTER, pady=10)
            selectbank = tk.CTkOptionMenu(frame,values= banks,command=setBranches)
            selectbank.pack(anchor=tk.CENTER, pady=10)
            selectbank.set(custbankcode)
            
            # Branches Menu
            branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + selectbank.get() + "';")
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
            def finalizeSignup():
                #CustomerName, SSN, CustomerAddress, Phone, CustomerPassword, BankCode, BranchCode
                name = customerNameField.get()
                ssn = ssnField.get()
                password = customerPasswordField.get()
                phone = phoneField.get()
                address = customerAddressField.get()
                bank = selectbank.get()
                branch = selectbranch.get()
                # cname: Any,
                # ssn: Any,
                # address: Any,
                # phone: Any,
                # password: Any,
                # bankCode: Any,
                # branchCode: Any
                adminObj.updateCustomer(ssn, name, address, phone, password, bank, branch)
                messagebox.showinfo("Customer Signup", "Customer signed up successfully")
                adminPage(root, frame)
            finalizeSignupButton = tk.CTkButton(frame, text="Finalize Signup", command=finalizeSignup)
            finalizeSignupButton.pack(anchor=tk.CENTER, pady=10)
            pass
        # Add your update user details logic here

    # Function to handle the 'Add bank' button click
    def add_bank(root, frame):
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)


        # Fields for BankName, BankCode, BankAddress
        bankNameField = tk.CTkEntry(frame, placeholder_text="Bank Name")
        bankNameField.pack(anchor=tk.CENTER, pady=10)
        bankCodeField = tk.CTkEntry(frame, placeholder_text="Bank Code")
        bankCodeField.pack(anchor=tk.CENTER, pady=10)
        bankAddressField = tk.CTkEntry(frame, placeholder_text="Bank Address")
        bankAddressField.pack(anchor=tk.CENTER, pady=10)

        # Button to finalize Add
        def finalizeAdd():
            # BankName, BankCode, BankAddress
            name = bankNameField.get()
            code = bankCodeField.get()
            address = bankAddressField.get()
            adminObj.addBank(name, code, address)
            messagebox.showinfo("Bank Add", "Bank added successfully")
            adminPage(root, frame)
        finalizeAddButton = tk.CTkButton(frame, text="Finalize Add", command=finalizeAdd)
        finalizeAddButton.pack(anchor=tk.CENTER, pady=10)
    
    # Function to handle the 'delete bank' button click
    def delete_bank(root, frame):
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)

        # Banks Menu
        banks_raw = adminObj.db.sendQuery("SELECT Code FROM Bank")
        banks = []
        for bank in banks_raw:
            banks.append(bank[0])
        selbanklabel = tk.CTkLabel(frame, text="Select Bank")
        selbanklabel.pack(anchor=tk.CENTER, pady=10)
        selectbank = tk.CTkOptionMenu(frame,values= banks)
        selectbank.pack(anchor=tk.CENTER, pady=10)

        # Button to finalize delete
        def finalizeDelete():
            # BankCode
            code = selectbank.get()
            adminObj.deleteBank(code)
            messagebox.showinfo("Bank Delete", "Bank deleted successfully")
            adminPage(root, frame)
        finalizeDeleteButton = tk.CTkButton(frame, text="Finalize Delete", command=finalizeDelete)
        finalizeDeleteButton.pack(anchor=tk.CENTER, pady=10)
    # Function to handle the 'Add bank branch' button click
    def add_bank_branch(root ,frame):
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)

        # Fields for BranchNum, BranchAddress, BankCode

        branchNumField = tk.CTkEntry(frame, placeholder_text="Branch Number")
        branchNumField.pack(anchor=tk.CENTER, pady=10)
        branchAddressField = tk.CTkEntry(frame, placeholder_text="Branch Address")
        branchAddressField.pack(anchor=tk.CENTER, pady=10)
        # Banks Menu
        banks_raw = adminObj.db.sendQuery("SELECT Code FROM Bank")
        banks = []
        for bank in banks_raw:
            banks.append(bank[0])
        selbanklabel = tk.CTkLabel(frame, text="Select Bank")
        selbanklabel.pack(anchor=tk.CENTER, pady=10)
        selectbank = tk.CTkOptionMenu(frame,values= banks)
        selectbank.set(banks[0])
        selectbank.pack(anchor=tk.CENTER, pady=10)

        # Button to finalize Add
        def finalizeAdd():
            # BranchNum, BranchAddress, BankCode
            num = branchNumField.get()
            address = branchAddressField.get()
            bank = selectbank.get()
            adminObj.addBranch(num, address, bank)
            messagebox.showinfo("Branch Add", "Branch added successfully")
            adminPage(root, frame)
        finalizeAddButton = tk.CTkButton(frame, text="Finalize Add", command=finalizeAdd)
        finalizeAddButton.pack(anchor=tk.CENTER, pady=10)
        BackButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
        BackButton.pack(anchor=tk.CENTER, pady=10)

    # Function to handle the 'delete bank branch' button click
    def delete_bank_branch(root, frame):
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)

        def setBranches(bank):
            branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + bank + "';")
            branches = []
            for branch in branches_raw:
                branches.append(branch[0])
            if len(branches) == 0:
                branches.append("No Branches")
                selectbranch.configure(values=branches, state="disabled")
                selectbranch.set("No Branches")
            else:
                selectbranch.configure(values=branches, state="normal")
                selectbranch.set(branches[0])

        # Banks Menu
        banks_raw = adminObj.db.sendQuery("SELECT Code FROM Bank")
        banks = []
        for bank in banks_raw:
            banks.append(bank[0])
        selbanklabel = tk.CTkLabel(frame, text="Select Bank")
        selbanklabel.pack(anchor=tk.CENTER, pady=10)
        selectbank = tk.CTkOptionMenu(frame,values= banks,command=setBranches)
        selectbank.pack(anchor=tk.CENTER, pady=10)
        
        # Branches Menu
        branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + selectbank.get() + "';")
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
            selectbranch.set(branches[0])
        selectbranch.pack(anchor=tk.CENTER, pady=10)

        # Button to finalize delete
        def finalizeDelete():
            # BranchNum
            num = selectbranch.get()
            bank = selectbank.get()
            adminObj.deleteBranch(num, bank)
            messagebox.showinfo("Branch Delete", "Branch deleted successfully")
            adminPage(root, frame)
        finalizeDeleteButton = tk.CTkButton(frame, text="Finalize Delete", command=finalizeDelete)
        finalizeDeleteButton.pack(anchor=tk.CENTER, pady=10)
        BackButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
        BackButton.pack(anchor=tk.CENTER, pady=10)

    # Function to handle the 'Show list of loans' button click
    def show_loans(root, frame):
        rows = adminObj.showLoansDetails()
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)
        # Add Header
        showLoans = tk.CTkLabel(frame, text="All Loans", font=("Arial", 30))
        showLoans.pack(anchor=tk.CENTER, pady=10)
        rows.insert(0, ['EmployeeName', 'Customer Name', 'Loan Type', 'Balance', 'Status', 'EmployeeSSN', 'CustomerSSN', 'PaidBalance', 'Loan ID', 'LoanTypeID'])
        height = len(rows)
        width = len(rows[0])
        loanFrame = tk.CTkScrollableFrame(frame, width=root.winfo_screenwidth())
        loanFrame.pack(anchor=tk.CENTER, pady=10)
        for i in range(height): #Rows
            for j in range(width): #Columns
                b = tk.CTkLabel(loanFrame, text=rows[i][j])
                b.grid(row=i, column=j,padx=10, pady=10)
        # Add Back Button
        backButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
        backButton.pack(anchor=tk.CENTER, pady=10)
        
    # Function to handle the 'Show list of customers' button click
    def showCustomers(root, frame):
        rows = adminObj.showCustomers()
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)
        # Add Header
        showCustomers = tk.CTkLabel(frame, text="All Customers", font=("Arial", 30))
        showCustomers.pack(anchor=tk.CENTER, pady=10)
        rows.insert(0, ['Name', 'SSN', 'Address', 'Phone', 'Password', 'BankCode', 'BranchCode'])
        height = len(rows)
        width = len(rows[0])
        custFrame = tk.CTkScrollableFrame(frame, width=root.winfo_screenwidth())
        custFrame.pack(anchor=tk.CENTER, pady=10)
        for i in range(height): #Rows
            for j in range(width): #Columns
                b = tk.CTkLabel(custFrame, text=rows[i][j])
                b.grid(row=i, column=j,padx=10, pady=10)
        # Add Back Button
        backButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
        backButton.pack(anchor=tk.CENTER, pady=10)

    # Function to handle the 'Perform operations on loans' button click
    def perform_loan_operations():
        # Add your perform loan operations logic here
        messagebox.showinfo("Perform Loan Operations", "Perform loan operations button clicked")

    # Create and configure the buttons
    sign_up_btn = tk.CTkButton(frame, text="Sign up", command= lambda: sign_up(root,frame))
    update_details_btn = tk.CTkButton(frame, text="Update User Details", command=lambda: update_user_details(root,frame))
    add_bank_btn = tk.CTkButton(frame, text="Add Bank", command=lambda: add_bank(root,frame))
    delete_bank_btn = tk.CTkButton(frame, text="Delete Bank", command=lambda: delete_bank(root,frame))
    add_branch_btn = tk.CTkButton(frame, text="Add Bank Branch", command=lambda: add_bank_branch(root,frame))
    delete_branch_btn = tk.CTkButton(frame, text="Delete Bank Branch", command=lambda: delete_bank_branch(root,frame))
    show_loans_btn = tk.CTkButton(frame, text="Show List of Loans", command=lambda: show_loans(root,frame))
    showCustomers_btn = tk.CTkButton(frame, text="Show List of Customers", command=lambda: showCustomers(root,frame))
    perform_loan_operations_btn = tk.CTkButton(frame, text="Perform Operations on Loans", command=lambda: perform_loan_operations(root,frame))

    # Place the buttons on the screen
    sign_up_btn.pack(anchor=tk.CENTER, pady=10)
    update_details_btn.pack(anchor=tk.CENTER, pady=10)
    add_bank_btn.pack(anchor=tk.CENTER, pady=10)
    delete_bank_btn.pack(anchor=tk.CENTER, pady=10)
    add_branch_btn.pack(anchor=tk.CENTER, pady=10)
    delete_branch_btn.pack(anchor=tk.CENTER, pady=10)
    show_loans_btn.pack(anchor=tk.CENTER, pady=10)
    showCustomers_btn.pack(anchor=tk.CENTER, pady=10)
    perform_loan_operations_btn.pack(anchor=tk.CENTER, pady=10)


    
    pass

def LoginPage(root, frame):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)

    def login(root, frame, empID, empPassword):
        global adminObj
        adminObj = Admin("", empID, empPassword)
        if (adminObj.validateAdmin() == False):
            messagebox.showerror("Login Failed", "Invalid Credentials")
            return
        else:
            adminPage(root, frame)
        pass
    # Create the Employee, Admin, and Customer buttons centered on the screen
    empIDField = tk.CTkEntry(frame, placeholder_text="Employee ID")
    empIDField.pack(anchor=tk.CENTER, pady=10)
    empPasswordField = tk.CTkEntry(frame, placeholder_text="Password")
    empPasswordField.pack(anchor=tk.CENTER, pady=10)
    loginButton = tk.CTkButton(frame, text="Login", command=lambda:login(root, frame, empIDField.get(), empPasswordField.get()))
    loginButton.pack(anchor=tk.CENTER, pady=10)

