import customer
import customtkinter as tk
from tkinter import messagebox
# import module in ../Views/Employee.py
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Views.Employee import *

global empObj
def tellerCustDetails(root, frame, ssn):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)
    customer.custDetails(frame, ssn)

    # Button to go to the deposit page
    depositButton = tk.CTkButton(frame, text="Deposit", command=lambda:depositPage(root, frame, ssn))
    depositButton.pack(anchor=tk.CENTER, pady=10)
    # Button to go to the withdraw page
    withdrawButton = tk.CTkButton(frame, text="Withdraw", command=lambda:withdrawPage(root, frame, ssn))
    withdrawButton.pack(anchor=tk.CENTER, pady=10)
    # Button to go back to the previous page
    backButton = tk.CTkButton(frame, text="Back", command=lambda:tellerPage(root, frame))
    backButton.pack(anchor=tk.CENTER, pady=10)
    
    
def deposit(root, frame, customerID, amount):
    # TODO: Deposit the amount into the customer's account
    #       Print a success message if the deposit was successful

    # TESTING: Print the amount to deposit
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)
    label = tk.CTkLabel(frame, text="Deposited " + amount + " into account " + customerID)
    label.pack(anchor=tk.CENTER, pady=10)
    backButton = tk.CTkButton(frame, text="Back", command=lambda:tellerCustDetails(root, frame, customerID))
    backButton.pack(anchor=tk.CENTER, pady=10)

def depositPage(root, frame, customerID):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)
    # Field to enter amount to deposit
    amountField = tk.CTkEntry(frame, placeholder_text="Amount")
    amountField.bind("<Return>", lambda:deposit(root, frame, customerID, amountField.get()))
    amountField.pack(anchor=tk.CENTER, pady=10)
    # Button to deposit the amount
    depositButton = tk.CTkButton(frame, text="Deposit", command=lambda:deposit(root, frame, customerID, amountField.get()))
    depositButton.pack(anchor=tk.CENTER, pady=10)
    backButton = tk.CTkButton(frame, text="Back", command=lambda:tellerCustDetails(root, frame, customerID))
    backButton.pack(anchor=tk.CENTER, pady=10)
    

def withdraw(root, frame, customerID, amount):
    # TODO: Withdraw the amount from the customer's account
    #       Print a success message if the withdrawal was successful
    #       Print an error message if the withdrawal was unsuccessful
    def success(root, frame, customerID, amount):
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)
        label = tk.CTkLabel(frame, text="Withdrew " + amount + " from account " + customerID)
        label.pack(anchor=tk.CENTER, pady=10)
        backButton = tk.CTkButton(frame, text="Back", command=lambda:tellerCustDetails(root, frame, customerID))
        backButton.pack(anchor=tk.CENTER, pady=10)
    def error(root, frame, customerID):
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)
        label = tk.CTkLabel(frame, text="Insufficient funds")
        label.pack(anchor=tk.CENTER, pady=10)
        backButton = tk.CTkButton(frame, text="Back", command=lambda:tellerCustDetails(root, frame, customerID))
        backButton.pack(anchor=tk.CENTER, pady=10)
    # TESTING: Print the amount to withdraw
    success(root, frame, customerID, amount)

def withdrawPage(root, frame, customerID):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)
    # Field to enter amount to withdraw
    amountField = tk.CTkEntry(frame, placeholder_text="Amount")
    amountField.pack(anchor=tk.CENTER, pady=10)
    # Button to withdraw the amount
    withdrawButton = tk.CTkButton(frame, text="Withdraw", command=lambda:withdraw(root, frame, customerID, amountField.get()))
    withdrawButton.pack(anchor=tk.CENTER, pady=10)
    #Button to go back to the previous page
    backButton = tk.CTkButton(frame, text="Back", command=lambda:tellerCustDetails(root, frame, customerID))
    backButton.pack(anchor=tk.CENTER, pady=10)

def displayAllLoans(root, frame):
    rows = empObj.db.sendQuery("SELECT * FROM Loan WHERE EmployeeSSN = " + empObj.ssn + ";")
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

# Load all loans that belong to employee
def displayAllLoansWindow(root, frame):
    
    displayAllLoans(root, frame)
    backButton = tk.CTkButton(frame, text="Back", command=lambda:loanPage(root, frame))
    backButton.pack(anchor=tk.CENTER, pady=10)

def searchLoan(root, frame):
    # Allows to search for a loan by loan number then displays the loan with approve and deny if status is requested
    def search(root, frame, loanNumber):
        frame.destroy()
        frame = tk.CTkFrame(root)
        frame.pack(expand=True)

        # Get loan by loan number
        loan = empObj.db.sendQuery("SELECT * FROM loan WHERE id = " + loanNumber + ";")

        # Display loan
        if loan is None:
            label = tk.CTkLabel(frame, text="No loan")
            label.pack(anchor=tk.CENTER, pady=10)
        else:
            label = tk.CTkLabel(frame, text=loan)
            label.pack(anchor=tk.CENTER, pady=10)
            if loan[0][7] == "Requested":
                approveButton = tk.CTkButton(frame, text="Approve", command=lambda:approve(root, frame, loanNumber))
                approveButton.pack(anchor=tk.CENTER, pady=10)
                denyButton = tk.CTkButton(frame, text="Deny", command=lambda:deny(root, frame, loanNumber))
                denyButton.pack(anchor=tk.CENTER, pady=10)
        backButton = tk.CTkButton(frame, text="Back", command=lambda:loanPage(root, frame))
        backButton.pack(anchor=tk.CENTER, pady=10)
    
    def approve(root, frame, loanNumber):
        # Approve the loan
        empObj.db.sendQuery("UPDATE loan SET status = 'Approved' WHERE id = " + loanNumber + ";")
        search(root, frame, loanNumber)
    
    def deny(root, frame, loanNumber):
        # Deny the loan
        empObj.db.sendQuery("UPDATE loan SET status = 'Denied' WHERE id = " + loanNumber + ";")
        search(root, frame, loanNumber)
    
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)
    # Field to enter loan number
    loanNumberField = tk.CTkEntry(frame, placeholder_text="Loan Number")
    loanNumberField.pack(anchor=tk.CENTER, pady=10)
    # Button to search for loan
    searchButton = tk.CTkButton(frame, text="Search", command=lambda:search(root, frame, loanNumberField.get()))
    searchButton.pack(anchor=tk.CENTER, pady=10)
    # Button to go back to the previous page
    backButton = tk.CTkButton(frame, text="Back", command=lambda:loanPage(root, frame))
    backButton.pack(anchor=tk.CENTER, pady=10)

def loanPage(root, frame):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)
    # display all loans
    loanButton = tk.CTkButton(frame, text="Display All Loans", command=lambda:displayAllLoans(root, frame))
    loanButton.pack(anchor=tk.CENTER, pady=10)
    # search for a loan
    loanButton = tk.CTkButton(frame, text="Search for a Loan", command=lambda:searchLoan(root, frame))
    loanButton.pack(anchor=tk.CENTER, pady=10)
    # Button to go back to the previous page
    backButton = tk.CTkButton(frame, text="Back", command=lambda:console(root, frame))
    backButton.pack(anchor=tk.CENTER, pady=10)

def console(root, frame):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)
    # Welcome message
    empName = empObj.name;
    label = tk.CTkLabel(frame, text="Welcome, " + empName)
    label.pack(anchor=tk.CENTER, pady=10)

    # Loan operations button
    loanButton = tk.CTkButton(frame, text="Loan Operations", command=lambda:loanPage(root, frame))
    loanButton.pack(anchor=tk.CENTER, pady=10)

    # Account operations button
    accountButton = tk.CTkButton(frame, text="Account Operations", command=lambda:accountPage(root, frame))
    accountButton.pack(anchor=tk.CENTER, pady=10)

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

