import customtkinter as tk
import tkinter.messagebox as messagebox
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Views.Admin import *
import employee as emp

global adminObj

def adminPage(root, frame):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)

    # Welcome message

    welcomeLabel = tk.CTkLabel(frame, text="Welcome, " + adminObj.name, font=("Arial", 20, "bold"))
    welcomeLabel.pack(anchor=tk.CENTER, pady=15, padx=15)
    # Function to handle the 'Sign up' button click
    def sign_up(root, frame):
        def signup_employee(root, frame):
            frame.destroy()
            frame = tk.CTkFrame(root)
            frame.pack(expand=True)
            # Fields for EmployeeName, SSN, EmployeePassword, AccessLevel, BankCode, BranchCode
            nameLabel = tk.CTkLabel(frame, text="Employee Name")
            nameLabel.grid(row=0, column=0, padx=10, pady=2)
            employeeNameField = tk.CTkEntry(frame)
            employeeNameField.grid(row=1, column=0, padx=10, pady=2)

            accessLevelLabel = tk.CTkLabel(frame, text="Access Level")
            accessLevelLabel.grid(row=0, column=1, padx=10, pady=2, columnspan=2)
            accessLevelField = tk.CTkEntry(frame)
            accessLevelField.grid(row=1, column=1, padx=10, pady=2, columnspan=2)

            ssnLabel = tk.CTkLabel(frame, text="SSN")
            ssnLabel.grid(row=4, column=0, padx=10, pady=2)
            ssnField = tk.CTkEntry(frame)
            ssnField.grid(row=5, column=0, padx=10, pady=2)
            employeePasswordLabel = tk.CTkLabel(frame, text="Employee Password")
            employeePasswordLabel.grid(row=4, column=1, padx=10, pady=2)
            employeePasswordField = tk.CTkEntry(frame)
            employeePasswordField.grid(row=5, column=1, padx=10, pady=2)
            

            def setBranches(bank):
                branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + bank + "';")
                branches = []
                for branch in branches_raw:
                    branches.append(branch[0])
                if len(branches) == 0:
                    branches.append("No Branches")
                    selectbranch.configure(values=branches, state="disabled")
                    selectbranch.set("No Branches")
                    finalizeSignupButton.configure(state="disabled")
                else:
                    selectbranch.configure(values=branches, state="normal")
                    selectbranch.set(branches[0])
                    finalizeSignupButton.configure(state="normal")

            # Banks Menu
            banks_raw = adminObj.db.sendQuery("SELECT Code FROM Bank")
            banks = []
            for bank in banks_raw:
                banks.append(bank[0])
            selbanklabel = tk.CTkLabel(frame, text="Select Bank")
            selbanklabel.grid(row=6, column=0, padx=10, pady=2)
            selectbank = tk.CTkOptionMenu(frame,values= banks,command=setBranches)
            selectbank.grid(row=7, column=0, padx=10, pady=2)
            
            # Button to finalize signup
            def finalizeSignup():
                name = employeeNameField.get()
                if name == "":
                    messagebox.showerror("Employee Signup", "Employee name cannot be empty")
                    return
                ssn = ssnField.get()
                if len(ssn) > 9 or not ssn.isdigit():
                    messagebox.showerror("Employee Signup", "SSN has to be 9 digits")
                    return
                password = employeePasswordField.get()
                if password == "":
                    messagebox.showerror("Employee Signup", "Employee password cannot be empty")
                    return
                
                accessLevel = accessLevelField.get()
                if not accessLevel.isdigit():
                    messagebox.showerror("Employee Signup", "Access level has to be a number")
                    return
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
            finalizeSignupButton.grid(row=8, column=0, columnspan=2, pady=10, sticky ="EW")

            # Branches Menu
            branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + selectbank.get() + "';")
            branches = []
            for branch in branches_raw:
                branches.append(branch[0])
            selbranchlabel = tk.CTkLabel(frame, text="Select Branch")
            selbranchlabel.grid(row=6, column=1, padx=10, pady=2)

            if len(branches) == 0:
                branches.append("No Branches")
                selectbranch = tk.CTkOptionMenu(frame,values=branches, state="disabled")
                selectbranch.set("No Branches")
                finalizeSignupButton.configure(state="disabled")
            else:
                selectbranch = tk.CTkOptionMenu(frame,values=branches, state="normal")
                selectbranch.set(branches[0])
                finalizeSignupButton.configure(state="normal")
            selectbranch.grid(row=7, column=1, padx=10, pady=2)
            
           
            BackButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
            BackButton.grid(row=9, column=0, columnspan=2, pady=10, sticky ="EW")
        def signup_customer(root, frame):
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

            def setBranches(bank):
                branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + bank + "';")
                branches = []
                for branch in branches_raw:
                    branches.append(branch[0])
                if len(branches) == 0:
                    branches.append("No Branches")
                    selectbranch.configure(values=branches, state="disabled")
                    selectbranch.set("No Branches")
                    finalizeSignupButton.configure(state="disabled")
                else:
                    selectbranch.configure(values=branches, state="normal")
                    selectbranch.set(branches[0])
                    finalizeSignupButton.configure(state="normal")

            # Banks Menu
            banks_raw = adminObj.db.sendQuery("SELECT Code FROM Bank")
            banks = []
            for bank in banks_raw:
                banks.append(bank[0])
            selbanklabel = tk.CTkLabel(frame, text="Select Bank")
            selbanklabel.grid(row=6, column=0, padx=10, pady=2)
            selectbank = tk.CTkOptionMenu(frame,values= banks,command=setBranches)
            selectbank.grid(row=7, column=0, padx=10, pady=2)
            
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
                bank = selectbank.get()
                branch = selectbranch.get()
                adminObj.signUpCustomer(name, ssn, address, phone, password, bank, branch)
                messagebox.showinfo("Customer Signup", "Customer signed up successfully")
                adminPage(root, frame)
            finalizeSignupButton = tk.CTkButton(frame, text="Finalize Signup", command=finalizeSignup)
            finalizeSignupButton.grid(row=8, column=0, columnspan=2, pady=10, sticky ="EW")

            # Branches Menu
            branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + selectbank.get() + "';")
            branches = []
            for branch in branches_raw:
                branches.append(branch[0])
            selbranchlabel = tk.CTkLabel(frame, text="Select Branch")
            selbranchlabel.grid(row=6, column=1, padx=10, pady=2)

            if len(branches) == 0:
                branches.append("No Branches")
                selectbranch = tk.CTkOptionMenu(frame,values=branches, state="disabled")
                selectbranch.set("No Branches")
                finalizeSignupButton.configure(state="disabled")
            else:
                selectbranch = tk.CTkOptionMenu(frame,values=branches, state="normal")
                selectbranch.set(branches[0])
                finalizeSignupButton.configure(state="normal")
            selectbranch.grid(row=7, column=1, padx=10, pady=2)
            
            
            BackButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
            BackButton.grid(row=9, column=0, columnspan=2, pady=10, sticky ="EW")
        
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
        BackButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
        BackButton.pack(anchor=tk.CENTER, pady=10)

    # Function to handle the 'Update user details' button click
    def update_user_details(root,frame):
        def update_employee(root, frame, empssn):
            emprow = adminObj.db.sendQuery("SELECT * FROM Employee WHERE SSN = '" + empssn + "';")
            # TESTINF
            if len(emprow) == 0:
                messagebox.showerror("Employee Update", "Employee with SSN " + empssn + " does not exist")
                return

            empname = emprow[0][0]
            emppassword = emprow[0][2]
            empaccesslevel = emprow[0][3]
            empbankcode = emprow[0][4]
            empbranchcode = emprow[0][5]

            frame.destroy()
            frame = tk.CTkFrame(root)
            frame.pack(expand=True)
            # Fields for EmployeeName, SSN, EmployeePassword, AccessLevel, BankCode, BranchCode
            idLabel = tk.CTkLabel(frame, text="Employee ID")
            idLabel.grid(row=0, column=0, padx=10, pady=2)
            employeeIDField = tk.CTkEntry(frame)
            employeeIDField.insert(0, empssn)
            employeeIDField.grid(row=1, column=0, padx=10, pady=2)
            
            nameLabel = tk.CTkLabel(frame, text="Employee Name")
            nameLabel.grid(row=0, column=1, padx=10, pady=2)
            employeeNameField = tk.CTkEntry(frame)
            employeeNameField.insert(0, empname)
            employeeNameField.grid(row=1, column=1, padx=10, pady=2)

            accessLabel = tk.CTkLabel(frame, text="Access Level")
            accessLabel.grid(row=2, column=0, padx=10, pady=2, columnspan=2)
            accessField = tk.CTkEntry(frame)
            accessField.insert(0, empaccesslevel)
            accessField.grid(row=3, column=0, padx=10, pady=2, columnspan=2)

            ssnLabel = tk.CTkLabel(frame, text="SSN")
            ssnLabel.grid(row=4, column=0, padx=10, pady=2)
            ssnField = tk.CTkEntry(frame)
            ssnField.insert(0, empssn)
            ssnField.grid(row=5, column=0, padx=10, pady=2)

            passwordLabel = tk.CTkLabel(frame, text="Password")
            passwordLabel.grid(row=4, column=1, padx=10, pady=2)
            employeePasswordField = tk.CTkEntry(frame)
            employeePasswordField.insert(0, emppassword)
            employeePasswordField.grid(row=5, column=1, padx=10, pady=2)
            

            def setBranches(bank):
                branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + bank + "';")
                branches = []
                for branch in branches_raw:
                    branches.append(branch[0])
                if len(branches) == 0:
                    branches.append("No Branches")
                    selectbranch.configure(values=branches, state="disabled")
                    selectbranch.set("No Branches")
                    finalizeUpdateButton.configure(state="disabled")
                else:
                    selectbranch.configure(values=branches, state="normal")
                    selectbranch.set(empbranchcode)
                    finalizeUpdateButton.configure(state="normal")

            # Banks Menu
            banks_raw = adminObj.db.sendQuery("SELECT Code FROM Bank")
            banks = []
            for bank in banks_raw:
                banks.append(bank[0])
            selbanklabel = tk.CTkLabel(frame, text="Select Bank")
            selbanklabel.grid(row=6, column=0, padx=10, pady=2)
            selectbank = tk.CTkOptionMenu(frame,values= banks,command=setBranches)
            
            selectbank.grid(row=7, column=0, padx=10, pady=2)
            selectbank.set(empbankcode)
            
            # Button to finalize signup
            def finalizeUpdate():
                name = employeeNameField.get()
                if name == "":
                    messagebox.showerror("Employee Update", "Name cannot be empty")
                    return
                ssn = ssnField.get()
                if len(ssn) != 9:
                    messagebox.showerror("Employee Update", "SSN must be 9 digits")
                    return
                password = employeePasswordField.get()
                if password == "":
                    messagebox.showerror("Employee Update", "Password cannot be empty")
                    return
                accessLevel = accessField.get()
                if not accessLevel.isdigit():
                    messagebox.showerror("Employee Update", "Access Level must be a number")
                    return
                bank = selectbank.get()
                branch = selectbranch.get()

                adminObj.updateEmployee(ssn, name, ssn, password, accessLevel, bank, branch)
                messagebox.showinfo("Employee Update", "Employee updated successfully")
                adminPage(root, frame)
            finalizeUpdateButton = tk.CTkButton(frame, text="Finalize Update", command=finalizeUpdate)
            finalizeUpdateButton.grid(row=8, column=0, padx=10, pady=2, columnspan=2, sticky="EW")

            # Branches Menu
            branches_raw = adminObj.db.sendQuery("SELECT BranchNumber FROM Branch WHERE BankCode = '" + selectbank.get() + "';")
            branches = []
            for branch in branches_raw:
                branches.append(branch[0])
            selbranchlabel = tk.CTkLabel(frame, text="Select Branch")
            selbranchlabel.grid(row=6, column=1, padx=10, pady=2)

            if len(branches) == 0:
                branches.append("No Branches")
                selectbranch = tk.CTkOptionMenu(frame,values=branches, state="disabled")
                selectbranch.set("No Branches")
                finalizeUpdateButton.configure(state="disabled")
            else:
                selectbranch = tk.CTkOptionMenu(frame,values=branches, state="normal")
                selectbranch.set(empbranchcode)
                finalizeUpdateButton.configure(state="normal")
            selectbranch.grid(row=7, column=1, padx=10, pady=2)
            
            
            BackButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
            BackButton.grid(row=9, column=0, padx=10, pady=2, columnspan=2, sticky="EW")
        def update_customer(root, frame, custssn):
            #TODO Apply grid and form validation to all widgets
            custrow = adminObj.db.sendQuery("SELECT * FROM Customer WHERE SSN = '" + custssn + "';")
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
            def finalizeUpdate():
                #CustomerName, SSN, CustomerAddress, Phone, CustomerPassword, BankCode, BranchCode
                name = customerNameField.get()
                ssn = ssnField.get()
                password = customerPasswordField.get()
                phone = phoneField.get()
                address = customerAddressField.get()
                bank = selectbank.get()
                branch = selectbranch.get()

                adminObj.updateCustomer(ssn, name, ssn, address, phone, password, bank, branch)
                messagebox.showinfo("Customer Signup", "Customer signed up successfully")
                adminPage(root, frame)
            finalizeUpdateButton = tk.CTkButton(frame, text="Finalize Signup", command=finalizeUpdate)
            finalizeUpdateButton.pack(anchor=tk.CENTER, pady=10)
            BackButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
            BackButton.pack(anchor=tk.CENTER, pady=10)
            pass
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)

        idField = tk.CTkEntry(frame, placeholder_text="SSN")
        idField.pack(anchor=tk.CENTER, pady=10)
        updateEmpbtn = tk.CTkButton(frame, text="Update Employee", command=lambda:update_employee(root, frame, idField.get()))
        updateEmpbtn.pack(anchor=tk.CENTER, pady=10)
        updateCustbtn = tk.CTkButton(frame, text="Update Customer", command=lambda:update_customer(root, frame, idField.get()))
        updateCustbtn.pack(anchor=tk.CENTER, pady=10)
        BackButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
        BackButton.pack(anchor=tk.CENTER, pady=10)

    # Function to handle the 'Add bank' button click
    def add_bank(root, frame):
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)


        # Fields for BankName, BankCode, BankAddress
        fieldsFrame = tk.CTkFrame(frame)
        fieldsFrame.pack(anchor=tk.CENTER, pady=10, padx=10)

        nameLabel = tk.CTkLabel(fieldsFrame, text="Bank Name")
        nameLabel.grid(row=0, column=0, pady=2, padx=10)
        bankNameField = tk.CTkEntry(fieldsFrame)
        bankNameField.grid(row=0, column=1, pady=2, padx=10)

        codeLabel = tk.CTkLabel(fieldsFrame, text="Bank Code")
        codeLabel.grid(row=1, column=0, pady=2, padx=10)
        bankCodeField = tk.CTkEntry(fieldsFrame)
        bankCodeField.grid(row=1, column=1, pady=2, padx=10)

        addressLabel = tk.CTkLabel(fieldsFrame, text="Bank Address")
        addressLabel.grid(row=2, column=0, pady=2, padx=10)
        bankAddressField = tk.CTkEntry(fieldsFrame)
        bankAddressField.grid(row=2, column=1, pady=2, padx=10)

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
        BackButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
        BackButton.pack(anchor=tk.CENTER, pady=10)
    
    # Function to handle the 'delete bank' button click
    # TODO APPLY GRID
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
        selbanklabel.pack(anchor=tk.CENTER, pady=2, padx=10)
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
        finalizeDeleteButton.pack(anchor=tk.CENTER, pady=20)
        BackButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
        BackButton.pack(anchor=tk.CENTER, pady=20)
    # Function to handle the 'Add bank branch' button click
    def add_bank_branch(root ,frame):
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)

        # Fields for BranchNum, BranchAddress, BankCode
        fieldsFrame = tk.CTkFrame(frame)
        fieldsFrame.pack(anchor=tk.CENTER, pady=10, padx=10)

        numLabel = tk.CTkLabel(fieldsFrame, text="Branch Number")
        numLabel.grid(row=0, column=0, pady=2, padx=10)
        branchNumField = tk.CTkEntry(fieldsFrame)
        branchNumField.grid(row=0, column=1, pady=2, padx=10)

        addressLabel = tk.CTkLabel(fieldsFrame, text="Branch Address")
        addressLabel.grid(row=1, column=0, pady=2, padx=10)
        branchAddressField = tk.CTkEntry(fieldsFrame)
        branchAddressField.grid(row=1, column=1, pady=2, padx=10)
        # Banks Menu
        banks_raw = adminObj.db.sendQuery("SELECT Code FROM Bank")
        banks = []
        for bank in banks_raw:
            banks.append(bank[0])
        selbanklabel = tk.CTkLabel(fieldsFrame, text="Select Bank")
        selbanklabel.grid(row=2, column=0, pady=2, padx=10)
        selectbank = tk.CTkOptionMenu(fieldsFrame,values= banks)
        selectbank.set(banks[0])
        selectbank.grid(row=2, column=1, pady=2, padx=10)

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

    #TODO APPLY GRID
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

    # Function to handle the 'Add Account' button click
    def add_account(root, frame):
        #accountType, accountNumber, balance, customerSSN, employeeID
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)

        # Fields for accountType, accountNumber, balance, customerSSN, employeeID
        fieldsFrame = tk.CTkFrame(frame)
        fieldsFrame.pack(anchor=tk.CENTER, pady=10, padx=10)

        customerSSNLabel = tk.CTkLabel(fieldsFrame, text="Customer SSN")
        customerSSNLabel.grid(row=0, column=0, pady=2, padx=10)
        customerSSNField = tk.CTkEntry(fieldsFrame)
        customerSSNField.grid(row=0, column=1, pady=2, padx=10)

        accountTypes = ["Checking", "Saving"]
        accountTypeLabel = tk.CTkLabel(fieldsFrame, text="Account Type")
        accountTypeLabel.grid(row=1, column=0, pady=2, padx=10)
        accountTypeMenu = tk.CTkOptionMenu(fieldsFrame, values=accountTypes)
        accountTypeMenu.grid(row=1, column=1, pady=2, padx=10)

        accountNumberLabel = tk.CTkLabel(fieldsFrame, text="Account Number")
        accountNumberLabel.grid(row=2, column=0, pady=2, padx=10)
        accountNumberField = tk.CTkEntry(fieldsFrame)
        accountNumberField.grid(row=2, column=1, pady=2, padx=10)

        balanceLabel = tk.CTkLabel(fieldsFrame, text="Balance")
        balanceLabel.grid(row=3, column=0, pady=2, padx=10)
        balanceField = tk.CTkEntry(fieldsFrame)
        balanceField.grid(row=3, column=1, pady=2, padx=10)

        def finalizeAdd():
            accountType = accountTypeMenu.get()
            accountNumber = accountNumberField.get()
            if accountNumber == "":
                messagebox.showerror("Error", "Account Number cannot be empty")
                return
            balance = balanceField.get()
            if balance == "" or not balance.isdigit():
                messagebox.showerror("Error", "Balance cannot be empty and must be a number")
                return
            customerSSN = customerSSNField.get()
            if customerSSN == "" or not customerSSN.isdigit():
                messagebox.showerror("Error", "Customer SSN cannot be empty and must be a number")
                return
            try:
                adminObj.addAccount(accountType, accountNumber, balance, customerSSN)
                messagebox.showinfo("Account Add", "Account added successfully")
                adminPage(root, frame)
            except:
                messagebox.showerror("Error", "Customer does not exist")
                return

        createAccountButton = tk.CTkButton(frame, text="Create Account", command=lambda:finalizeAdd())
        createAccountButton.pack(anchor=tk.CENTER, pady=10)


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
        loanFrame = tk.CTkScrollableFrame(frame,width=920)
        loanFrame.pack(pady=10)
        for i in range(height): #Rows
            for j in range(width): #Columns
                b = tk.CTkLabel(loanFrame, text=rows[i][j])
                b.grid(row=i, column=j,padx=10, pady=10)
        # Add Back Button
        backButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
        backButton.pack(anchor=tk.CENTER, pady=10)
        
    def show_loans_type(root, frame):
        rows = adminObj.showLoansType()
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
        custFrame = tk.CTkScrollableFrame(frame, width=650)
        custFrame.pack(anchor=tk.CENTER, pady=10)
        for i in range(height): #Rows
            for j in range(width): #Columns
                b = tk.CTkLabel(custFrame, text=rows[i][j])
                b.grid(row=i, column=j,padx=10, pady=10)
        # Add Back Button
        backButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
        backButton.pack(anchor=tk.CENTER, pady=10)

    # Function to handle the 'Show list of employees' button click
    def showEmployees(root, frame):
        rows = adminObj.showEmployees()
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)
        # Add Header
        showEmployees = tk.CTkLabel(frame, text="All Employees", font=("Arial", 30))
        showEmployees.pack(anchor=tk.CENTER, pady=10)
        rows.insert(0, ['Name', 'SSN', 'Password', 'Access Level', 'Bank Code', 'Branch Code'])
        height = len(rows)
        width = len(rows[0])
        empFrame = tk.CTkScrollableFrame(frame, width=650)
        empFrame.pack(anchor=tk.CENTER, pady=10)
        for i in range(height):
            for j in range(width):
                b = tk.CTkLabel(empFrame, text=rows[i][j])
                b.grid(row=i, column=j,padx=10, pady=10)
        # Add Back Button
        backButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
        backButton.pack(anchor=tk.CENTER, pady=10)

    # Function to handle the 'Perform operations on loans' button click
    def perform_loan_operations(root, frame):
        # Function to handle the 'New Loan' button click
        def LoanOperations(root, frame, prevPage = adminPage):
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
                loanDetails = adminObj.db.sendQuery(f"SELECT * FROM Loan WHERE id = {loanID}")
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

                
                # Get loan type name from loan type id
                loanTypes_raw = adminObj.showLoansType()
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
                    
                    adminObj.updateLoan(loanID, loanStatus)
                    messagebox.showinfo("Loan Update", "Loan updated successfully")
                    adminPage(root, frame)
                
                # Add Update Button
                updateButton = tk.CTkButton(frame, text="Update", command=lambda:updateLoan(root, frame))
                updateButton.grid(row=8, column=0, pady=10, padx=10, columnspan=2, sticky="EW")
                backButton = tk.CTkButton(frame, text="Back", command=lambda:prevPage(root, frame))
                backButton.grid(row=9, column=0, pady=10, padx=10, columnspan=2, sticky="EW")

            searchbtn = tk.CTkButton(frame, text="Search", command=lambda:searchLoan(root, frame))
            searchbtn.grid(row=2, column=0, pady=10, padx=10, columnspan=2, sticky="EW")
           
            backButton = tk.CTkButton(frame, text="Back", command=lambda:prevPage(root, frame))
            backButton.grid(row=3, column=0, pady=10, padx=10, columnspan=2, sticky="EW")
        # Function to handle the 'Add new loan' button click
        def newLoan(root, frame):
            frame.destroy()
            frame = tk.CTkFrame(root)
            frame.pack(expand=True)
            # Add Header
            newLoan = tk.CTkLabel(frame, text="New Loan", font=("Arial", 30))
            newLoan.grid(row=0, column=0, pady=10, padx=10)
            # Add Labels and Entry Boxes
            customerSSNLabel = tk.CTkLabel(frame, text="Customer SSN")
            customerSSNLabel.grid(row=1, column=0, pady=2, padx=10)
            customerSSNEntry = tk.CTkEntry(frame)
            customerSSNEntry.grid(row=1, column=1, pady=2, padx=10)


            
            loanTypes_raw = adminObj.showLoansType()
            loanTypes = []
            for loan in loanTypes_raw:
                loanTypes.append(loan[0])
            
            loanTypeLabel = tk.CTkLabel(frame, text="Loan Type")
            loanTypeLabel.grid(row=2, column=0, pady=2, padx=10)
            loanTypeMenu = tk.CTkOptionMenu(frame, values = loanTypes)
            loanTypeMenu.grid(row=2, column=1, pady=2, padx=10)

            balanceLabel = tk.CTkLabel(frame, text="Balance")
            balanceLabel.grid(row=3, column=0, pady=2, padx=10)
            balanceEntry = tk.CTkEntry(frame)
            balanceEntry.grid(row=3, column=1, pady=2, padx=10)
            # Add Button
            def addLoan():
                loanType = loanTypeMenu.get()
                # Get the loan type ID
                loanTypeID = loanTypes.index(loanType) + 1
                balance = balanceEntry.get()
                loanStatus = "REQ"
                employeeSSN = adminObj.ssn
                customerSSN = customerSSNEntry.get()
                
                adminObj.addLoan(loanTypeID, balance, loanStatus, employeeSSN, customerSSN)
                messagebox.showinfo("New Loan", "Loan added successfully")
                adminPage(root, frame)
            addLoanButton = tk.CTkButton(frame, text="Add Loan", command=addLoan)
            addLoanButton.grid(row=4, column=0, pady=10, padx=10, columnspan=2, sticky="EW")
            backButton = tk.CTkButton(frame, text="Back", command=lambda:perform_loan_operations(root, frame))
            backButton.grid(row = 5, column= 0, pady=10, padx=10,columnspan=2, sticky="EW")
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)

        newLoanBtn = tk.CTkButton(frame, text="New Loan", command=lambda:newLoan(root, frame))
        newLoanBtn.pack(anchor=tk.CENTER, pady=10)
        loanOperationsBtn = tk.CTkButton(frame, text="Update Loan", command=lambda:LoanOperations(root, frame))
        loanOperationsBtn.pack(anchor=tk.CENTER, pady=10)
        backButton = tk.CTkButton(frame, text="Back", command=lambda:adminPage(root, frame))
        backButton.pack(anchor=tk.CENTER, pady=10)

    # Create and configure the buttons
    sign_up_btn = tk.CTkButton(frame, text="Sign up", command= lambda: sign_up(root,frame))
    update_details_btn = tk.CTkButton(frame, text="Update User Details", command=lambda: update_user_details(root,frame))
    add_account_btn = tk.CTkButton(frame, text="Add Account", command=lambda: add_account(root,frame))
    add_bank_btn = tk.CTkButton(frame, text="Add Bank", command=lambda: add_bank(root,frame))
    delete_bank_btn = tk.CTkButton(frame, text="Delete Bank", command=lambda: delete_bank(root,frame))
    add_branch_btn = tk.CTkButton(frame, text="Add Bank Branch", command=lambda: add_bank_branch(root,frame))
    delete_branch_btn = tk.CTkButton(frame, text="Delete Bank Branch", command=lambda: delete_bank_branch(root,frame))
    show_loans_btn = tk.CTkButton(frame, text="Show List of Loans", command=lambda: show_loans(root,frame))
    show_loans_type_btn = tk.CTkButton(frame, text="Show List of Loan Types", command=lambda: show_loans_type(root,frame))
    showCustomers_btn = tk.CTkButton(frame, text="Show List of Customers", command=lambda: showCustomers(root,frame))
    showEmployees_btn = tk.CTkButton(frame, text="Show List of Employees", command=lambda: showEmployees(root,frame))
    perform_loan_operations_btn = tk.CTkButton(frame, text="Perform Operations on Loans", command=lambda: perform_loan_operations(root,frame))

    # Place the buttons on the screen
    sign_up_btn.pack(anchor=tk.CENTER, pady=10)
    update_details_btn.pack(anchor=tk.CENTER, pady=10)
    add_account_btn.pack(anchor=tk.CENTER, pady=10)
    add_bank_btn.pack(anchor=tk.CENTER, pady=10)
    delete_bank_btn.pack(anchor=tk.CENTER, pady=10)
    add_branch_btn.pack(anchor=tk.CENTER, pady=10)
    delete_branch_btn.pack(anchor=tk.CENTER, pady=10)
    show_loans_btn.pack(anchor=tk.CENTER, pady=10)
    show_loans_type_btn.pack(anchor=tk.CENTER, pady=10)
    showCustomers_btn.pack(anchor=tk.CENTER, pady=10)
    showEmployees_btn.pack(anchor=tk.CENTER, pady=10)
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
    empPasswordField = tk.CTkEntry(frame, placeholder_text="Password", show="*")
    empPasswordField.pack(anchor=tk.CENTER, pady=10)
    loginButton = tk.CTkButton(frame, text="Login", command=lambda:login(root, frame, empIDField.get(), empPasswordField.get()))
    loginButton.pack(anchor=tk.CENTER, pady=10)

