import tkinter as tk
from tkinter import Toplevel, Label, Button, StringVar, OptionMenu
from ui.admin.admin_menu import AdminMenu

class AdminScreen:

    def __init__(self, root, home_screen, cursor):
        self.home_screen = home_screen
        self.window = Toplevel(root)
        self.cursor = cursor
        self.prev_screen = root
        self.window.title("Admin Screen")
        self.window.geometry("400x400")
        Label(self.window, text="Admin Screen", font=("times new roman", 24, "bold"), fg="black").pack(pady=10)

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
        self.cursor.execute("SELECT company_name FROM Company")
        companies = [row[0] for row in self.cursor.fetchall()]
        if companies:
            self.company_var.set(companies[0])  # Set default selection
        return companies

    def go_back(self):
        self.window.destroy()
        self.prev_screen.deiconify()

    def login_action(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        selected_company = self.company_var.get()
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Selected Company: {selected_company}")
        self.window.withdraw()
        AdminMenu(self.window, self.cursor)