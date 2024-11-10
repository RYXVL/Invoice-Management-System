import tkinter as tk
from tkinter import Toplevel, Label, Button, StringVar, OptionMenu

class CustomerLoginScreen:
    def __init__(self, customer_screen, cursor):
        self.customer_screen = customer_screen
        self.window = Toplevel()
        self.cursor = cursor
        self.window.title("Customer Login")
        self.window.geometry("400x400")
        
        Label(self.window, text="Login", font=("times new roman", 24, "bold")).pack(pady=10)
        
        Label(self.window, text="Username:", font=("times new roman", 14)).pack(pady=5)
        self.username_entry = tk.Entry(self.window, font=("times new roman", 14))
        self.username_entry.pack(pady=5)

        Label(self.window, text="Password:", font=("times new roman", 14)).pack(pady=5)
        self.password_entry = tk.Entry(self.window, font=("times new roman", 14), show="*")
        self.password_entry.pack(pady=5)

        Label(self.window, text="Select Company:", font=("times new roman", 14)).pack(pady=5)
        self.company_var = StringVar()
        self.company_dropdown = OptionMenu(self.window, self.company_var, *self.fetch_company_names())
        self.company_dropdown.config(font=("times new roman", 12))
        self.company_dropdown.pack(pady=5)

        Button(self.window, text="Login", font=("times new roman", 14), command=self.login_action).pack(pady=10)
        Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def fetch_company_names(self):
        self.cursor.execute("SELECT company_id, company_name FROM Company")
        queryResult = self.cursor.fetchall()
        print(queryResult)
        companyToID = {}
        for row in queryResult:
            companyToID[row[1]] = row[0]
        companies = [row[1] for row in queryResult]
        self.companyToID = companyToID
        if companies:
            self.company_var.set(companies[0])  # Set default selection
        return companies

    def login_action(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        selected_company = self.company_var.get()
        print(f"Login Username: {username}")
        print(f"Login Password: {password}")
        print(f"Selected Company: {selected_company}")
    
    def login_action(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        selected_company = self.company_var.get()
        self.cursor.execute(f"SELECT customer_password FROM customer WHERE company_id = {self.companyToID[selected_company]} AND customer_user_name =  '{username}'")
        result = self.cursor.fetchall()
        if len(result) == 0:
            print("Invalid company ID or username!")
            return
        if password != result[0][0]:
            print("Wrong password entered!")
            return
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Selected Company: {selected_company}")

    def go_back(self):
        self.window.destroy()
        self.customer_screen.deiconify()
