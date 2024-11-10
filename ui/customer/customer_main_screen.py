import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry
from tkinter import ttk  # For the table

class CustomerMainScreen:
    def __init__(self, root, login_screen):
        self.login_screen = login_screen
        self.window = Toplevel(root)
        self.window.title("Customer Main Screen")
        self.window.geometry("500x400")

        Label(self.window, text="Customer Main Screen", font=("times new roman", 24, "bold")).pack(pady=10)
        
        Label(self.window, text="Enter Invoice ID:", font=("times new roman", 14)).pack(pady=5)
        self.invoice_entry = Entry(self.window, font=("times new roman", 14))
        self.invoice_entry.pack(pady=5)

        Button(self.window, text="Submit", font=("times new roman", 14), command=self.print_invoice_id).pack(pady=10)

        # Back button
        Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

        # Dummy data for the table
        self.table_data = [
            {"invoice_id": "INV001", "invoice_date": "2024-01-01"},
            {"invoice_id": "INV002", "invoice_date": "2024-02-15"},
            {"invoice_id": "INV003", "invoice_date": "2024-03-20"},
        ]

        # Table for displaying invoice data
        self.invoice_table = ttk.Treeview(self.window, columns=("invoice_id", "invoice_date"), show="headings")
        self.invoice_table.heading("invoice_id", text="Invoice ID")
        self.invoice_table.heading("invoice_date", text="Invoice Date")
        self.invoice_table.pack(pady=10)

        # Insert dummy data into the table
        for item in self.table_data:
            self.invoice_table.insert("", "end", values=(item["invoice_id"], item["invoice_date"]))

    def print_invoice_id(self):
        invoice_id = self.invoice_entry.get()
        print(f"Entered Invoice ID: {invoice_id}")

    def go_back(self):
        self.window.destroy()
        self.login_screen.window.deiconify()
