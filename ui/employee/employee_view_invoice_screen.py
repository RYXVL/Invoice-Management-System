import tkinter as tk
from tkinter import Toplevel, Label, Button

class ViewInvoice:
    
    def __init__(self, employee_menu, cursor, selected_company_id, connection):
        self.employee_menu = employee_menu  # Store the reference to the EmployeeMenu instance
        self.window = Toplevel()
        self.cursor = cursor
        self.connection = connection
        self.selected_company_id = selected_company_id
        print(f'ViewInvoice: {self.selected_company_id}')
        self.window.title("View Invoice")
        self.window.geometry("400x300")
        
        Label(self.window, text="View Invoice", font=("times new roman", 24, "bold"), fg="black").pack(pady=10)
        Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def go_back(self):
        self.window.destroy()  # Close the View Invoice window
        self.employee_menu.window.deiconify()  # Show the Employee Menu again
