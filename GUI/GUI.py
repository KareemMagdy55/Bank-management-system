import customtkinter as tk
import employee as emp
import admin
import customer as cust


tk.set_appearance_mode("System")
tk.set_default_color_theme("dark-blue")

def mainPage(root):
    # Page with button for Employee, Admin, and Customer
    frame = tk.CTkFrame(root)
    frame.pack(expand=True)
    # Create the Employee, Admin, and Customer buttons centered on the screen
    employeeButton = tk.CTkButton(frame, text="Employee", command=lambda:emp.LoginPage(root, frame))
    employeeButton.pack(anchor=tk.CENTER, pady=10)
    adminButton = tk.CTkButton(frame, text="Admin", command=lambda:admin.LoginPage(root, frame))
    adminButton.pack(anchor=tk.CENTER, pady=10)
    customerButton = tk.CTkButton(frame, text="Customer", command=lambda:cust.LoginPage(root, frame))
    customerButton.pack(anchor=tk.CENTER, pady=10)

   

root = tk.CTk()
root.geometry("750x500")
root.title("Banking System")
mainPage(root)
root.mainloop() 