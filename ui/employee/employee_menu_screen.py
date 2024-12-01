from tkinter import Toplevel, Label, Button
from ui.employee.employee_generate_invoice_screen import GenerateInvoice
from ui.employee.employee_view_invoice_screen import ViewInvoice

class EmployeeMenu:
    
    def __init__(self, employee_screen, cursor, selected_company_id, connection, employee_id):
        self.selected_company_id = selected_company_id
        self.employee_screen = employee_screen  # Store the reference to the EmployeeScreen instance
        self.window = Toplevel(employee_screen)
        self.cursor = cursor
        self.connection = connection
        self.employee_id = employee_id
        self.window.title("Employee Menu")
        self.window.geometry("400x300")
        
        Label(self.window, text="Employee Menu", font=("times new roman", 24, "bold"), fg="black").pack(pady=10)

        # Generate Invoice button (c3 color)
        generate_invoice_button = Button(self.window, text="Generate Invoice", font=("times new roman", 14), command=self.open_generate_invoice, bg="#4f8fc0", fg="white")
        generate_invoice_button.pack(pady=10)

        # View Invoice button (c3 color)
        view_invoice_button = Button(self.window, text="View Invoice", font=("times new roman", 14), command=self.open_view_invoice, bg="#4f8fc0", fg="white")
        view_invoice_button.pack(pady=10)

        # Back button (c4 color)
        back_button = Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back, bg="#26648e", fg="white")
        back_button.pack(pady=10)

    def open_generate_invoice(self):
        self.window.withdraw()  # Hide the Employee Menu
        GenerateInvoice(self, self.window, self.cursor, self.selected_company_id, self.connection, self.employee_id)  # Open the Generate Invoice screen

    def open_view_invoice(self):
        self.window.withdraw()  # Hide the Employee Menu
        ViewInvoice(self,self.window, self.cursor, self.selected_company_id, self.connection)  # Open the View Invoice screen

    def go_back(self):
        self.window.destroy()  # Close the Employee Menu
        self.employee_screen.deiconify()  # Show the Employee Screen again
