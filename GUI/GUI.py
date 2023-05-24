import customtkinter as tk
import GUI.employee as emp
import GUI.admin
import GUI.customer as cust
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import Report.report as report


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
    # Create the Report button centered on the screen
    reportButton = tk.CTkButton(frame, text="Report", command=lambda:report.display_reports(root, frame))
    reportButton.pack(anchor=tk.CENTER, pady=10)

   

root = tk.CTk()
root.geometry("1000x600")
root.title("Banking System")
mainPage(root)
root.mainloop() 