import tkinter as tk
from tkinter import Toplevel, Label, Button, StringVar, OptionMenu
from ui.employee.employee_menu_screen import EmployeeMenu

class EmployeeScreen:
    
    def __init__(self, root, home_screen, cursor, connection):
        self.home_screen = home_screen
        self.window = Toplevel(root)
        self.prev_screen = root
        self.cursor = cursor
        self.connection = connection
        self.window.title("Employee Screen")
        self.window.geometry("400x400")
        Label(self.window, text="Employee Screen", font=("times new roman", 24, "bold"), fg="black").pack(pady=10)

        Label(self.window, text="Username:", font=("times new roman", 14)).pack(pady=5)
        self.username_entry = tk.Entry(self.window, font=("times new roman", 14))
        self.username_entry.pack(pady=5)

        Label(self.window, text="Password:", font=("times new roman", 14)).pack(pady=5)
        self.password_entry = tk.Entry(self.window, font=("times new roman", 14), show="*")
        self.password_entry.pack(pady=5)

        Label(self.window, text="Select Company:", font=("times new roman", 14)).pack(pady=5)
        self.company_var = StringVar()
        self.company_dropdown = OptionMenu(self.window, self.company_var, *self.fetch_company_names())
        self.company_dropdown.config(font=("times new roman", 12), bg="#ffe3b3")  # c1 color
        self.company_dropdown.pack(pady=5)

        # Login button (c3 color)
        login_button = Button(self.window, text="Login", font=("times new roman", 14), command=self.login_action, bg="#4f8fc0", fg="white")
        login_button.pack(pady=10)

        # Back button (c4 color)
        back_button = Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back, bg="#26648e", fg="white")
        back_button.pack(pady=10)

    def fetch_company_names(self):
        self.cursor.execute("SELECT company_id, company_name FROM Company")
        queryResult = self.cursor.fetchall()
        companyToID = {}
        for row in queryResult:
            companyToID[row[1]] = row[0]
        companies = [row[1] for row in queryResult]
        self.companyToID = companyToID
        if companies:
            self.company_var.set(companies[0])  # Default selection if available
        return companies

    def go_back(self):
        self.window.destroy()
        self.prev_screen.deiconify()
    
    def login_action(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        selected_company = self.company_var.get()
        self.cursor.execute(f"SELECT employee_password, employee_id FROM employee WHERE company_id = {self.companyToID[selected_company]} AND employee_user_name =  '{username}' AND is_admin = 0;")
        result = self.cursor.fetchall()
        if len(result) == 0:
            print("Invalid company ID, username or no employee access!")
            return
        if password != result[0][0]:
            print("Wrong password entered!")
            return
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Selected Company: {selected_company}")
        print(f"Employee ID: {result[0][1]}")
        self.window.withdraw()  # Hide the Employee Screen
        EmployeeMenu(self.window, self.cursor, self.companyToID[selected_company], self.connection, result[0][1])  # Open Employee Menu with the current window and cursor
