import tkinter as tk
from tkinter import Toplevel, Label, Button
from ui.employee.employee_generate_invoice_screen import GenerateInvoice
from ui.employee.employee_view_invoice_screen import ViewInvoice

class EmployeeMenu:
    
    def __init__(self, employee_screen, cursor, selected_company_id, connection, employee_id):
        self.selected_company_id = selected_company_id
        print(f'EmployeeMenu: {self.selected_company_id}')
        self.employee_screen = employee_screen  # Store the reference to the EmployeeScreen instance
        self.window = Toplevel(employee_screen)
        self.cursor = cursor
        self.connection = connection
        self.employee_id = employee_id
        self.window.title("Employee Menu")
        self.window.geometry("400x300")
        
        Label(self.window, text="Employee Menu", font=("times new roman", 24, "bold"), fg="black").pack(pady=10)

        Button(self.window, text="Generate Invoice", font=("times new roman", 14), command=self.open_generate_invoice).pack(pady=10)
        Button(self.window, text="View Invoice", font=("times new roman", 14), command=self.open_view_invoice).pack(pady=10)
        Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def open_generate_invoice(self):
        self.window.withdraw()  # Hide the Employee Menu
        GenerateInvoice(self, self.window, self.cursor, self.selected_company_id, self.connection, self.employee_id)  # Open the Generate Invoice screen

    def open_view_invoice(self):
        self.window.withdraw()  # Hide the Employee Menu
        ViewInvoice(self,self.window, self.cursor, self.selected_company_id, self.connection)  # Open the View Invoice screen

    def go_back(self):
        self.window.destroy()  # Close the Employee Menu
        self.employee_screen.deiconify()  # Show the Employee Screen again
