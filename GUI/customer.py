import customtkinter as tk
from tkinter import messagebox
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import Views.Customer as cust
import GUI.employee as emp
global custObj


def custDetails(root, frame):
    
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)

    custRow = custObj.db.sendQuery("SELECT * FROM customer WHERE ssn = '" + custObj.ssn + "'")[0]
    name = custObj.name
    address = custRow[2]
    phone = custRow[3]
    totalBalance = custObj.db.sendQuery("SELECT SUM(balance) FROM account WHERE CustomerSSN = '" + custObj.ssn + "'")[0][0]


    # Welcome message
    welcomeLabel = tk.CTkLabel(frame, text="Welcome, " + name, font=("Arial", 20))
    welcomeLabel.grid(row=0, column=0, columnspan=2, pady=10)

    ssnLabel = tk.CTkLabel(frame, text="SSN: ")
    ssnLabel.grid(row=1, column=0)
    ssnValue = tk.CTkLabel(frame, text=custObj.ssn)
    ssnValue.grid(row=1, column=1, pady=3, padx=10)

    nameLabel = tk.CTkLabel(frame, text="Name: ")
    nameLabel.grid(row=2, column=0)
    nameValue = tk.CTkLabel(frame, text=name)
    nameValue.grid(row=2, column=1, pady=3, padx=10)

    addressLabel = tk.CTkLabel(frame, text="Address: " )
    addressLabel.grid(row=3, column=0)
    addressValue = tk.CTkLabel(frame, text=address)
    addressValue.grid(row=3, column=1, pady=3, padx=10)
    
    phoneLabel = tk.CTkLabel(frame, text="Phone: ")
    phoneLabel.grid(row=4, column=0)
    phoneValue = tk.CTkLabel(frame, text=phone)
    phoneValue.grid(row=4, column=1, pady=3, padx=10)

    balanceLabel = tk.CTkLabel(frame, text="Total Balance: EGP")
    balanceLabel.grid(row=5, column=0)
    balanceValue = tk.CTkLabel(frame, text=totalBalance)
    balanceValue.grid(row=5, column=1, pady=3, padx=10)

    # Create the buttons for list of accounts, list of loans, request loan, and logout

    def listAccounts(root, frame):
       
        custAccts = custObj.db.sendQuery("SELECT Number, AccountType, Balance FROM account WHERE CustomerSSN = '" + custObj.ssn + "'")
        if len(custAccts) == 0:
            messagebox.showerror("Error", "No accounts found")
            custDetails(root, frame)
            return
        
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)
        showCustomers = tk.CTkLabel(frame, text="Your Accounts", font=("Arial", 20))
        showCustomers.pack(anchor=tk.CENTER, pady=10)
        custAccts.insert(0, ["Account Number","Account Type", "Balance"])
        acctsFrame = tk.CTkScrollableFrame(frame, width=350)
        acctsFrame.pack(expand=True)

        height = len(custAccts)
        width = len(custAccts[0])

        for i in range(height): #Rows
            for j in range(width): #Columns
                b = tk.CTkLabel(acctsFrame, text=custAccts[i][j])
                b.grid(row=i, column=j,padx=10, pady=10)
        
        

        # Create the back button
        backButton = tk.CTkButton(frame, text="Back", command=lambda:custDetails(root, frame))
        backButton.pack(anchor=tk.CENTER, pady=10)

    def startLoan(root, frame):
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)

        # Create the loan id entry
        loanIdLabel = tk.CTkLabel(frame, text="Loan ID")
        loanIdLabel.grid(row=0, column=0, pady=10)
        loanIdEntry = tk.CTkEntry(frame)
        loanIdEntry.grid(row=0, column=1, pady=10)

        # Create the start button
        def startLoan():
            loanID = loanIdEntry.get()
            if loanID == "":
                messagebox.showerror("Error", "Please enter a loan ID")
                return
            try:
                custObj.startLoan(loanID)
                messagebox.showinfo("Success", "Loan started successfully")
                custDetails(root, frame)
            except:
                messagebox.showerror("Error", "Loan ID not found")
                return
            
        startButton = tk.CTkButton(frame, text="Start", command=startLoan)
        startButton.grid(row=1, column=0, pady=10, padx=10, columnspan=2, sticky="EW")
        backButton = tk.CTkButton(frame, text="Back", command=lambda:custDetails(root, frame))
        backButton.grid(row=2, column=0, pady=10, padx=10, columnspan=2, sticky="EW")
        pass
    def requestLoan(root, frame):
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
        customerSSNEntry.insert(0, custObj.ssn)
        customerSSNEntry.configure(state="disabled")


        
        loanTypes_raw = custObj.db.sendQuery("SELECT loantype FROM loantype")
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
            if balance == "":
                messagebox.showerror("Error", "Please enter a balance")
                return
            try:
                custObj.requestLoan(loanTypeID, balance)
                messagebox.showinfo("Success", "Loan requested successfully")
                custDetails(root, frame)
            except:
                messagebox.showerror("Error", "Loan request failed")
                return
            
        addLoanButton = tk.CTkButton(frame, text="Add Loan", command=addLoan)
        addLoanButton.grid(row=4, column=0, pady=10, padx=10, columnspan=2, sticky="EW")
        backButton = tk.CTkButton(frame, text="Back", command=lambda:custDetails(root, frame))
        backButton.grid(row = 5, column= 0, pady=10, padx=10,columnspan=2, sticky="EW")

    listAccountsButton = tk.CTkButton(frame, text="List Accounts", command=lambda:listAccounts(root, frame))
    listAccountsButton.grid(row=6, column=0, pady=10, padx=10, columnspan=2, sticky="EW")

    startLoanButton = tk.CTkButton(frame, text="Start Loan", command=lambda:startLoan(root, frame))
    startLoanButton.grid(row=7, column=0, pady=10, padx=10, columnspan=2, sticky="EW")

    requestLoanButton = tk.CTkButton(frame, text="Request Loan", command=lambda:requestLoan(root, frame))
    requestLoanButton.grid(row=8, column=0, pady=10, padx=10, columnspan=2, sticky="EW")        

    

def LoginPage(root, frame):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)

    # SSN field
    ssnLabel = tk.CTkLabel(frame, text="SSN")
    ssnLabel.pack(anchor=tk.CENTER, pady=2)
    ssnEntry = tk.CTkEntry(frame)
    ssnEntry.pack(anchor=tk.CENTER, pady=10)

    # Password field
    passwordLabel = tk.CTkLabel(frame, text="Password")
    passwordLabel.pack(anchor=tk.CENTER, pady=2)
    passwordEntry = tk.CTkEntry(frame, show="*")
    passwordEntry.pack(anchor=tk.CENTER, pady=10)

    # Login button
    def login():
        ssn = ssnEntry.get()
        password = passwordEntry.get()
        global custObj
        custObj = cust.Customer("",ssn, password)
        if custObj.validateCustomer():
            custDetails(root, frame)
        else:
            messagebox.showerror("Error", "Invalid SSN or password")
    loginButton = tk.CTkButton(frame, text="Login", command=login)
    loginButton.pack(anchor=tk.CENTER, pady=10)
