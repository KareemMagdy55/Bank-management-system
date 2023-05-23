import customtkinter as tk

def custDetails(frame, ssn):
    
    # TODO: Get customer details from database
    name = "John Doe"
    address = "123 Main St"
    phone = "1234567890"
    balance = "1000"


    #FOR TESTING
    ssnLabel = tk.CTkLabel(frame, text="SSN: " + ssn)
    ssnLabel.pack(anchor=tk.CENTER, pady=10)
    nameLabel = tk.CTkLabel(frame, text="Name: " + name)
    nameLabel.pack(anchor=tk.CENTER, pady=10)
    addressLabel = tk.CTkLabel(frame, text="Address: " + address)
    addressLabel.pack(anchor=tk.CENTER, pady=10)
    phoneLabel = tk.CTkLabel(frame, text="Phone: " + phone)
    phoneLabel.pack(anchor=tk.CENTER, pady=10)

    balanceLabel = tk.CTkLabel(frame, text="Balance: EGP" + balance)
    balanceLabel.pack(anchor=tk.CENTER, pady=10)

def LoginPage(root, frame):
    frame.destroy()
    frame = tk.CTkFrame(root)
    frame.pack(anchor=tk.CENTER, pady=10)

    # SSN field
    ssnLabel = tk.CTkLabel(frame, text="SSN")
    ssnLabel.pack(anchor=tk.CENTER, pady=10)
    ssnEntry = tk.CTkEntry(frame)
    ssnEntry.pack(anchor=tk.CENTER, pady=10)

    # Password field
    passwordLabel = tk.CTkLabel(frame, text="Password")
    passwordLabel.pack(anchor=tk.CENTER, pady=10)
    passwordEntry = tk.CTkEntry(frame, show="*")
    passwordEntry.pack(anchor=tk.CENTER, pady=10)

    # Login button
    def login():
        ssn = ssnEntry.get()
        password = passwordEntry.get()
        # TODO: Add login logic here
        if ssn == '123' and password == '123':
            custDetails(frame, ssn)
        else:
            tk.messagebox.showerror("Error", "Invalid SSN or password")