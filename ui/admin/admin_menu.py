import tkinter as tk
from tkinter import Toplevel, Label, Button

class AdminMenu:

    def __init__(self, admin_screen):
        self.admin_screen = admin_screen
        self.window = Toplevel()
        self.window.title("Admin Menu")
        self.window.geometry("400x500")

        Label(self.window, text="Admin Menu", font=("times new roman", 24, "bold")).pack(pady=10)

        buttons = [
            "Add Product", "Remove Product", "Create Employee", "Delete Employee",
            "Delete Customer", "Update Company Details", "Update Customer", "Update Employee"
        ]

        for btn_text in buttons:
            Button(self.window, text=btn_text, font=("times new roman", 14), command=lambda: None).pack(pady=5)

        Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def go_back(self):
        self.window.destroy()
        self.admin_screen.deiconify()